###  1. What is the difference between SAST, DAST, and secrets scanning, and why should all be part of a CI/CD pipeline?

| Type        | Description                                                                 | Example Tools          |
|-------------|-----------------------------------------------------------------------------|------------------------|
| **SAST**    | Static Application Security Testing — analyzes source code for vulnerabilities before execution. | `Bandit`, `Semgrep`    |
| **DAST**    | Dynamic Application Security Testing — analyzes a running application to find runtime vulnerabilities. | `OWASP ZAP`            |
| **Secrets Scanning** | Scans code for accidentally committed credentials, tokens, and secrets.           | `Gitleaks`              |

**Why include all three?**

Each method addresses different types of risks at different stages:
- **SAST** catches code-level issues during development.
- **DAST** detects issues during runtime.
- **Secrets scanning** prevents accidental leaks of sensitive information.

Together, they provide a **layered and complete security posture** throughout the SDLC.


###  2. Why is storing secrets in code dangerous? What’s a secure alternative?

**Risks of storing secrets in code:**
- Exposes sensitive credentials to anyone with repo access
- Secrets can be accidentally pushed to public repositories
- Attackers actively scan GitHub for leaked secrets

**Secure alternatives:**
- Use **environment variables**
- Store secrets in secure services:
  - **GitHub Actions Secrets**
  - **AWS Secrets Manager**
  - **HashiCorp Vault**
  - **Azure Key Vault**
- Never hardcode passwords, API keys, tokens, or database credentials


### 3. How does adding these scans to a pipeline help enforce Shift-Left Security?

**Shift-Left Security** means integrating security earlier in the development lifecycle — during coding, not just at deployment.

**Benefits of pipeline-integrated scanning:**
- Automatically detects vulnerabilities before code reaches production
- Encourages developers to write secure code from the start
- Reduces remediation time and cost
- Makes security a shared responsibility (DevSecOps)

Scanning in CI/CD ensures security becomes a **built-in process**, not an afterthought.


### 4. If a scan fails in your pipeline, what is the next step for a developer or DevOps engineer?

1. **Review the scan report** uploaded as a pipeline artifact:
   - Check what caused the failure (file, line number, rule, etc.)
   - Determine the severity (critical, high, medium, low)

2. **Take action:**
   - For SAST: Refactor or patch the vulnerable code
   - For DAST: Apply runtime fixes (e.g., input validation, proper headers)
   - For secrets: Revoke and rotate the exposed secret immediately

3. **Push a fix** and re-run the pipeline

4. **(Optional)**: If it’s a false positive:
   - Document and safely ignore it using configuration or inline comments (with justification)


