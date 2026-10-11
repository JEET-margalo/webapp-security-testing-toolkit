from __future__ import annotations

import json
import sys
from datetime import datetime, timezone

import jwt


def _format_timestamp(value):
    if not isinstance(value, int):
        return value
    return datetime.fromtimestamp(value, tz=timezone.utc).isoformat()


def inspect_token(token: str) -> int:
    header = jwt.get_unverified_header(token)
    claims = jwt.decode(token, options={"verify_signature": False})

    print("Header:")
    print(json.dumps(header, indent=2))
    print("\nClaims:")
    printable_claims = {
        key: _format_timestamp(value) if key in {"iat", "nbf", "exp"} else value
        for key, value in claims.items()
    }
    print(json.dumps(printable_claims, indent=2))

    findings = 0
    alg = str(header.get("alg", "")).lower()
    if alg == "none":
        findings += 1
        print("\n[HIGH] JWT uses alg=none. Reject unsigned tokens server-side.")
    if "exp" not in claims:
        findings += 1
        print("\n[MEDIUM] JWT has no exp claim. Use short-lived access tokens.")
    if "aud" not in claims:
        print("\n[INFO] JWT has no aud claim. Consider audience validation for APIs.")

    return findings


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python -m websec_tools.jwt_inspect <jwt>")
        raise SystemExit(2)
    findings = inspect_token(sys.argv[1])
    raise SystemExit(1 if findings else 0)


if __name__ == "__main__":
    main()
