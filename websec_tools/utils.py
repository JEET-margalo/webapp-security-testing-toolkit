from __future__ import annotations

import requests

DEFAULT_TIMEOUT = 10
USER_AGENT = "webapp-security-testing-toolkit/1.0"


def get(url: str) -> requests.Response:
    """Send a safe GET request with a clear user agent."""
    return requests.get(
        url,
        timeout=DEFAULT_TIMEOUT,
        allow_redirects=True,
        headers={"User-Agent": USER_AGENT},
    )
