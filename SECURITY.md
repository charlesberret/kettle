# Security policy

Kettle is pre-release software. Security fixes are currently provided for the
latest commit on `main` in the affected repository.

Please do not open a public issue for a suspected vulnerability. Use GitHub's
private vulnerability reporting in the affected repository:

- [Kettle core](https://github.com/charlesberret/kettle-core/security/advisories/new)
- [Kettle for VS Code](https://github.com/charlesberret/kettle-vscode/security/advisories/new)
- [Kettle desktop](https://github.com/charlesberret/kettle-desktop/security/advisories/new)

Include the affected version or commit, reproduction steps, impact, and any
suggested mitigation. Do not include private project data unless it is
essential and you have agreed on a secure transfer method.

Code-of-conduct concerns may use the
[Kettle product-home private report](https://github.com/charlesberret/kettle/security/advisories/new);
identify the report as a conduct matter rather than a vulnerability.

Kettle currently supports a single-user, loopback-only core. Remote or
multi-user deployment is not supported.
