# Web Application Security Testing Toolkit

A practical Python toolkit and methodology repo for **authorized web application security testing**. It focuses on OWASP Web Top 10 checks, API security testing, and repeatable reporting workflows.

> Use only on applications you own or have explicit written permission to test.

## Highlights

- Security header review
- CORS misconfiguration checks
- JWT structure and claim inspection
- Lightweight URL health checks
- OWASP Web/API testing checklist
- Markdown vulnerability report template

## Why this repo

This project demonstrates hands-on application security skills useful for roles in VAPT, Web/API Security Testing, and Application Security Engineering.

## Quick start

```bash
python -m venv .venv
source .venv/Scripts/activate  # Windows Git Bash
pip install -r requirements.txt
```

Run a header check:

```bash
python -m websec_tools.headers https://example.com
```

Run a CORS check:

```bash
python -m websec_tools.cors https://example.com
```

Inspect a JWT safely without verifying signature:

```bash
python -m websec_tools.jwt_inspect eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.xxxxx.yyyyy
```

## Repository structure

```text
websec_tools/
  headers.py       # HTTP security header analyzer
  cors.py          # CORS configuration review
  jwt_inspect.py   # JWT decoder/claim review helper
  utils.py         # shared HTTP helpers
examples/
  sample-report.md
  test-plan.md
docs/
  webapp-security-checklist.md
```

## Skills demonstrated

- OWASP Web Top 10 testing methodology
- API security review mindset
- Python automation for security validation
- Clear security reporting and remediation guidance
- Responsible, permission-based testing

## Roadmap

- Add authenticated scan support using supplied session cookies
- Add JSON/CSV report output
- Add pytest tests for scanner modules
- Add OWASP API Top 10 checklist
- Add CI workflow for linting and tests
