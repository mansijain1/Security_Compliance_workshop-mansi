# DAY -1 CORE CONCEPTS

1. Explain the concept of shift-left security and why it is important in DevSecOps.

    - Definition: Integrating security earlier in the software development lifecycle (left side of the pipeline).
    - Goal:  Identify and fix security issues during development, not after deployment.

    - Importance in DevSecOps
        - Reduces cost and effort to fix vulnerabilities.
        - Improves overall security posture.
        - Encourages developer ownership of security.

2. How does detecting secrets early in the CI/CD pipeline prevent production vulnerabilities?

    - Prevents: Accidental exposure of API keys, passwords, tokens in production.
    - Benefits:
        - Stops secrets from reaching public repos or logs.
        - Enables faster remediation.
        - Ensures compliance and audit readiness.

3. What strategies can be used to store secrets securely instead of hardcoding them?

    - Use environment variables.
    - Store secrets in secrets managers like:
        - AWS Secrets Manager
        - HashiCorp Vault
        - Azure Key Vault
        - Google Secret Manager
    - Use CI/CD tools’ secret management (e.g., GitHub Actions Secrets, GitLab CI Variables).

4. Describe a situation where a secret could still be exposed even after scanning, and how to prevent it.

    - Example: A secret is scanned and removed from code, but still exists in Git history or logs.
    - Prevention:
        - Use tools like `git-secrets`, `truffleHog`, or `gitleaks`.
        - Purge secrets from Git history (`git filter-repo` or `BFG Repo-Cleaner`).
        - Rotate and revoke compromised secrets immediately.
        - Implement pre-commit hooks and enforce policies.