<p align="center">
  <img src="https://img.shields.io/github/license/LeoLin990405/github-repo-design-skill?style=flat-square" alt="License">
  <img src="https://img.shields.io/github/stars/LeoLin990405/github-repo-design-skill?style=flat-square" alt="Stars">
  <img src="https://img.shields.io/github/issues/LeoLin990405/github-repo-design-skill?style=flat-square" alt="Issues">
  <img src="https://img.shields.io/badge/Claude%20Code-Skill-8A2BE2?style=flat-square&logo=anthropic&logoColor=white" alt="Claude Code Skill">
</p>

<h1 align="center">GitHub Repo Design Skill</h1>

<p align="center">
  <strong>A comprehensive GitHub repository design toolkit for Claude Code</strong><br>
  <em>15 modules covering repo setup, documentation, collaboration, quality, and advanced topics</em>
</p>

<p align="center">
  <a href="#features">Features</a> &bull;
  <a href="#quick-start">Quick Start</a> &bull;
  <a href="#modules">Modules</a> &bull;
  <a href="#templates">Templates</a> &bull;
  <a href="#project-structure">Project Structure</a> &bull;
  <a href="#contributing">Contributing</a> &bull;
  <a href="#license">License</a>
</p>

---

## Features

| Feature | Description |
|---------|-------------|
| **Repo Structure** | Best-practice directory layouts and essential file scaffolding |
| **README Design** | Badge configuration, shields.io integration, and README templates |
| **CI/CD Pipelines** | GitHub Actions workflow templates for lint, test, build, and deploy |
| **Security** | Dependabot, CodeQL, secret scanning, and SECURITY.md guidance |
| **Versioning** | SemVer, Conventional Commits, and automated changelog generation |
| **Issue & PR Templates** | Bug report, feature request, and pull request templates |
| **Community Building** | Discussions, contributor recognition, sponsors, and CODEOWNERS |
| **Internationalization** | Multi-language README support and i18n patterns |
| **Monorepo Support** | Monorepo structure, tooling, and CI strategies |
| **Intent Routing** | Auto-routes user requests to the right modules and templates |

---

## Quick Start

### Install as a Claude Code Skill

```bash
cd ~/.claude/skills
git clone https://github.com/LeoLin990405/github-repo-design-skill.git github-repo-design
```

### Usage

The toolkit auto-routes based on your request:

```text
"Set up a new repo"            -> Setup modules + new-repo-checklist
"Create a README"              -> readme module + readme-template
"Add CI/CD"                    -> cicd module + ci-workflow-template
"Prepare a release"            -> versioning module + release-checklist
"Use the security module"      -> 08-security
"Show monorepo best practices" -> 09-monorepo
```

---

## Modules

| # | Phase | Module | What It Covers |
|---|-------|--------|----------------|
| 01 | Setup | [structure](modules/01-structure/) | Project directory layout, essential files |
| 02 | Documentation | [readme](modules/02-readme/) | README design, badges, shields.io, tools |
| 03 | Setup | [config](modules/03-config/) | LICENSE, CONTRIBUTING, SECURITY, CODEOWNERS |
| 04 | Collaboration | [templates](modules/04-templates/) | Bug reports, feature requests, PR templates |
| 05 | Setup | [settings](modules/05-settings/) | Topics, social preview, branch protection |
| 06 | Quality | [cicd](modules/06-cicd/) | GitHub Actions workflows, CI/CD pipelines |
| 07 | Advanced | [profile](modules/07-profile/) | GitHub Profile README |
| 08 | Quality | [security](modules/08-security/) | Dependabot, CodeQL, secret scanning |
| 09 | Advanced | [monorepo](modules/09-monorepo/) | Monorepo structure and tooling |
| 10 | Documentation | [docs](modules/10-docs/) | Documentation site integration |
| 11 | Quality | [versioning](modules/11-versioning/) | SemVer, Conventional Commits, changelogs |
| 12 | Quality | [quality](modules/12-quality/) | Linting, pre-commit hooks, EditorConfig |
| 13 | Collaboration | [community](modules/13-community/) | Discussions, contributor recognition, sponsors |
| 14 | Documentation | [i18n](modules/14-i18n/) | Multi-language README, internationalization |
| 15 | Documentation | [faq](modules/15-faq/) | Frequently asked questions |

---

## Templates

Ready-to-use templates for common repository tasks:

| Template | Use Case |
|----------|----------|
| [new-repo-checklist](templates/new-repo-checklist.md) | Step-by-step checklist for setting up a new GitHub repo |
| [readme-template](templates/readme-template.md) | Universal README template for any project |
| [ci-workflow-template](templates/ci-workflow-template.yml) | GitHub Actions CI pipeline (lint, test, build, deploy) |
| [release-checklist](templates/release-checklist.md) | Release checklist (version bump, changelog, tag, publish) |

### Recipes

Module combinations by project type:

| Project Type | Modules | Templates |
|---|---|---|
| **Small utility / library** | 01 + 02 + 03 | new-repo-checklist, readme-template |
| **Open source project** | 01-06 + 08 + 11-13 | All templates |
| **Enterprise project** | 01-06 + 08 + 11 + 12 | ci-workflow-template, release-checklist |
| **Documentation-heavy** | 01-03 + 10 + 14 + 15 | readme-template |
| **Monorepo** | 01-03 + 06 + 09 + 11 + 12 | ci-workflow-template, release-checklist |

---

## Project Structure

```
github-repo-design-skill/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.yml
│   │   ├── feature_request.yml
│   │   └── config.yml
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/
│       └── claude-review.yml
├── modules/
│   ├── 01-structure/
│   ├── 02-readme/
│   │   ├── README.md
│   │   ├── badges.md
│   │   └── tools.md
│   ├── 03-config/
│   ├── 04-templates/
│   ├── 05-settings/
│   ├── 06-cicd/
│   ├── 07-profile/
│   ├── 08-security/
│   ├── 09-monorepo/
│   ├── 10-docs/
│   ├── 11-versioning/
│   ├── 12-quality/
│   ├── 13-community/
│   ├── 14-i18n/
│   └── 15-faq/
├── templates/
│   ├── new-repo-checklist.md
│   ├── readme-template.md
│   ├── ci-workflow-template.yml
│   └── release-checklist.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
└── SKILL.md
```

---

## Contributing

Contributions are welcome! Please read the [Contributing Guide](CONTRIBUTING.md) for details on the process for submitting pull requests, reporting bugs, and suggesting features.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

<p align="center">
  <sub>Built with collaboration between human and AI</sub>
</p>
