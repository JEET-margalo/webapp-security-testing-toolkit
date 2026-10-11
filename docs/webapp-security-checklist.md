# Web Application Security Testing Checklist

Use this checklist only for authorized testing.

## Recon and mapping

- Identify application roles and permission levels
- Map public and authenticated endpoints
- Review technologies, frameworks, and exposed versions
- Capture baseline requests with Burp Suite or OWASP ZAP

## Authentication

- Test login rate limiting and lockout behavior
- Check password reset token expiry and reuse
- Validate MFA bypass scenarios if MFA exists
- Verify session invalidation after logout/password change

## Authorization

- Test horizontal privilege escalation between users
- Test vertical privilege escalation between roles
- Check direct object reference patterns in IDs and UUIDs
- Validate API authorization on every sensitive endpoint

## Input validation

- Test reflected/stored XSS in user-controlled fields
- Test SQL injection using safe payloads and manual validation
- Check file upload extension, MIME type, and content validation
- Validate server-side enforcement, not only client-side controls

## API security

- Check BOLA/BFLA issues
- Validate JWT expiry, issuer, audience, and algorithm handling
- Test mass assignment on JSON body fields
- Review CORS behavior for sensitive endpoints

## Security headers and browser controls

- Strict-Transport-Security
- Content-Security-Policy
- X-Frame-Options or CSP frame-ancestors
- X-Content-Type-Options
- Referrer-Policy
- Permissions-Policy

## Reporting

For every finding include:

- Title and severity
- Affected endpoint
- Steps to reproduce
- Impact
- Evidence
- Remediation
- Retest status
