# Authorized Web Application Security Test Plan

## Scope

- Target application: `<application-url>`
- Test window: `<date/time>`
- Allowed testing: Manual web/API testing, authenticated role testing, safe automation
- Not allowed: Denial of service, destructive testing, social engineering

## Tools

- Burp Suite / OWASP ZAP
- Postman
- Nmap for approved host discovery only
- Python helper scripts from this repository

## Methodology

1. Confirm scope and authorization
2. Map application and API endpoints
3. Test authentication and session management
4. Test authorization and access control
5. Validate input handling and injection risks
6. Review CORS, JWT, and security headers
7. Document evidence and business impact
8. Share remediation guidance
9. Perform retesting

## Deliverables

- Executive summary
- Technical findings with severity
- Proof-of-concept evidence
- Remediation recommendations
- Retest results
