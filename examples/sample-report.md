# Sample Vulnerability Report

## Finding: Missing Content Security Policy

**Severity:** Medium  
**Category:** Security Misconfiguration  
**Affected URL:** `https://example.com/`

## Summary

The application does not return a `Content-Security-Policy` header. Without CSP, the impact of Cross-Site Scripting may increase because the browser has fewer restrictions on script execution sources.

## Steps to reproduce

1. Send a GET request to the affected URL.
2. Review response headers.
3. Observe that `Content-Security-Policy` is missing.

## Evidence

```http
HTTP/1.1 200 OK
Content-Type: text/html
```

## Impact

If an XSS vulnerability is introduced elsewhere, missing CSP may make exploitation easier and increase user/session risk.

## Recommendation

Implement a restrictive CSP. Example starting point:

```http
Content-Security-Policy: default-src 'self'; object-src 'none'; frame-ancestors 'none'; base-uri 'self'
```

Tune the policy based on application requirements and test in report-only mode before enforcement.

## Retest status

Pending.
