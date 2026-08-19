#!/usr/bin/env python3
"""Validate this repo's manifests against their published schemas.

server.json is the record the official MCP registry publishes from, and
glama.json is what Glama reads to verify listing ownership. Both are hand-edited
and neither is exercised by any build, so a typo here silently degrades our
directory listings instead of failing anything. This is the check that catches it.
"""

import json
import sys
import urllib.request

import jsonschema

CHECKS = [
    ("server.json", "https://static.modelcontextprotocol.io/schemas/2025-12-11/server.schema.json"),
    ("glama.json", "https://glama.ai/mcp/schemas/server.json"),
]


def fetch(url: str) -> dict:
    # glama.ai returns 403 to urllib's default User-Agent, so send a real one.
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/json",
            "User-Agent": "clueso-mcp-manifest-validator (+https://github.com/clueso-ai/clueso-mcp)",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def main() -> int:
    failed = False
    for path, schema_url in CHECKS:
        try:
            document = json.load(open(path))
        except (OSError, json.JSONDecodeError) as exc:
            print(f"FAIL {path}: not readable as JSON — {exc}")
            failed = True
            continue
        try:
            jsonschema.validate(document, fetch(schema_url))
        except jsonschema.ValidationError as exc:
            location = "/".join(str(p) for p in exc.absolute_path) or "(root)"
            print(f"FAIL {path}: at {location}: {exc.message}")
            failed = True
            continue
        except Exception as exc:  # network / schema fetch problems
            print(f"FAIL {path}: could not validate against {schema_url} — {exc}")
            failed = True
            continue
        print(f"ok   {path} validates against {schema_url}")

    # The registry rejects a re-publish of an existing version, so drift between
    # server.json and the live registry is the failure mode that actually bites.
    try:
        registry = fetch("https://registry.modelcontextprotocol.io/v0/servers?search=io.clueso")
        local = json.load(open("server.json"))
        published = {
            s.get("server", s).get("version")
            for s in registry.get("servers", [])
            if s.get("server", s).get("name") == local.get("name")
        }
        if local.get("version") in published:
            print(
                f"FAIL server.json: version {local['version']} is already published "
                f"for {local['name']} (published: {sorted(v for v in published if v)}). Bump it."
            )
            failed = True
        else:
            print(f"ok   server.json version {local.get('version')} is not yet published")
    except Exception as exc:
        print(f"warn could not cross-check the registry (non-fatal): {exc}")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
