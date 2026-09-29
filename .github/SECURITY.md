# Security Policy

## Supported Versions

We actively support and provide security updates for the following versions of **GitHub Activity Lab**:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

---

## Reporting a Vulnerability

The GitHub Activity Lab team and maintainers take application and supply-chain security seriously. If you believe you have discovered a vulnerability, please follow responsible disclosure guidelines:

1. **Do not create a public GitHub issue.**
2. Report the vulnerability privately via [GitHub Private Vulnerability Reporting](https://github.com/UmeshCode1/lets-connect/security/advisories/new) or by emailing the project maintainer at [umesh.code1@gmail.com](mailto:umesh.code1@gmail.com).
3. Include detailed reproduction steps, proof-of-concept payloads, and affected versions.

### Our Commitment
- We will acknowledge receipt of your report within **48 hours**.
- We will provide an initial assessment and coordinate a remediation timeline.
- Once a fix is verified, a patched release and credit disclosure will be published.

---

## Action Security Best Practices

When integrating `activity-lab` into your GitHub Actions workflows:

- **Least Privilege**: Always specify minimal workflow permissions (e.g. `permissions: contents: read`).
- **Secrets Management**: Store API keys (`ANTHROPIC_API_KEY`) as encrypted repository secrets. Never hardcode credentials in workflow files.
- **Untrusted Inputs**: Action runners sanitize pull request titles and descriptions to prevent shell command injection.
