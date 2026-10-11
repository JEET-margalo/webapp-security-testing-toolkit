from __future__ import annotations

import sys

import requests

from .utils import DEFAULT_TIMEOUT, USER_AGENT

TEST_ORIGIN = "https://attacker.example"


def check_cors(url: str) -> int:
    response = requests.get(
        url,
        timeout=DEFAULT_TIMEOUT,
        allow_redirects=True,
        headers={"Origin": TEST_ORIGIN, "User-Agent": USER_AGENT},
    )

    acao = response.headers.get("Access-Control-Allow-Origin")
    acac = response.headers.get("Access-Control-Allow-Credentials")

    print(f"URL: {response.url}")
    print(f"Status: {response.status_code}")
    print(f"Access-Control-Allow-Origin: {acao}")
    print(f"Access-Control-Allow-Credentials: {acac}\n")

    findings = 0
    if acao == "*" and acac and acac.lower() == "true":
        findings += 1
        print("[HIGH] Wildcard origin with credentials enabled")
        print("Fix: Do not use '*' when credentials are allowed. Use an allowlist of trusted origins.")
    elif acao == TEST_ORIGIN:
        findings += 1
        print("[MEDIUM] Reflected arbitrary Origin header")
        print("Fix: Validate Origin against a strict allowlist before reflecting it.")
    elif acao == "*":
        print("[INFO] Wildcard CORS is enabled. Confirm the endpoint exposes only public data.")
    else:
        print("[OK] No obvious arbitrary CORS trust detected with the test origin.")

    return findings


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python -m websec_tools.cors https://example.com")
        raise SystemExit(2)
    findings = check_cors(sys.argv[1])
    raise SystemExit(1 if findings else 0)


if __name__ == "__main__":
    main()
