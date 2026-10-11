from __future__ import annotations

import sys
from dataclasses import dataclass

from .utils import get


@dataclass(frozen=True)
class HeaderCheck:
    name: str
    risk: str
    recommendation: str


SECURITY_HEADERS = [
    HeaderCheck(
        "Strict-Transport-Security",
        "Missing HSTS may allow SSL stripping attacks.",
        "Set Strict-Transport-Security with max-age and includeSubDomains after confirming HTTPS is stable.",
    ),
    HeaderCheck(
        "Content-Security-Policy",
        "Missing CSP increases impact of XSS vulnerabilities.",
        "Define a restrictive Content-Security-Policy and avoid unsafe-inline where possible.",
    ),
    HeaderCheck(
        "X-Frame-Options",
        "Missing clickjacking protection.",
        "Set X-Frame-Options: DENY/SAMEORIGIN or use CSP frame-ancestors.",
    ),
    HeaderCheck(
        "X-Content-Type-Options",
        "Missing MIME sniffing protection.",
        "Set X-Content-Type-Options: nosniff.",
    ),
    HeaderCheck(
        "Referrer-Policy",
        "Referrer leakage may expose sensitive URL data.",
        "Set Referrer-Policy: strict-origin-when-cross-origin or stricter.",
    ),
    HeaderCheck(
        "Permissions-Policy",
        "Browser features may be exposed more broadly than required.",
        "Disable unused browser features using Permissions-Policy.",
    ),
]


def analyze(url: str) -> int:
    response = get(url)
    print(f"URL: {response.url}")
    print(f"Status: {response.status_code}\n")

    findings = 0
    for check in SECURITY_HEADERS:
        value = response.headers.get(check.name)
        if value:
            print(f"[OK] {check.name}: {value}")
        else:
            findings += 1
            print(f"[MISSING] {check.name}")
            print(f"  Risk: {check.risk}")
            print(f"  Fix:  {check.recommendation}")
    return findings


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python -m websec_tools.headers https://example.com")
        raise SystemExit(2)
    findings = analyze(sys.argv[1])
    raise SystemExit(1 if findings else 0)


if __name__ == "__main__":
    main()
