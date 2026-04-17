# New Repository Checklist

Step-by-step checklist for setting up a new GitHub repository. Work through each phase in order.

---

## Phase 1: Initialize

- [ ] Create repository on GitHub (or `git init` locally)
- [ ] Choose visibility: public or private
- [ ] Add `.gitignore` (use [gitignore.io](https://www.toptal.com/developers/gitignore) or GitHub's templates)
- [ ] Choose and add `LICENSE` file
  - MIT — permissive, most common for open source
  - Apache 2.0 — permissive with patent protection
  - GPL-3.0 — copyleft, requires derivative works to be open source
- [ ] Create initial `README.md` (see [readme-template](readme-template.md))
- [ ] Make initial commit and push

**Reference:** [01-structure](../modules/01-structure/), [03-config](../modules/03-config/)

---

## Phase 2: Repository Settings

- [ ] Add descriptive **About** section (short description + URL)
- [ ] Add **Topics** tags (language, framework, domain — up to 20)
- [ ] Upload **Social preview image** (1280x640px recommended)
- [ ] Configure **default branch** name (main)
- [ ] Enable/disable **Wikis**, **Issues**, **Discussions** as needed
- [ ] Set up **branch protection rules** for default branch:
  - [ ] Require pull request reviews (1+ approvals)
  - [ ] Require status checks to pass
  - [ ] Require branches to be up to date
  - [ ] Restrict who can push

**Reference:** [05-settings](../modules/05-settings/)

---

## Phase 3: Documentation

- [ ] Write complete `README.md` with:
  - [ ] Project name and description
  - [ ] Status badges (build, coverage, version, license)
  - [ ] Quick start / installation instructions
  - [ ] Usage examples
  - [ ] Contributing link
  - [ ] License info
- [ ] Add `CONTRIBUTING.md` with contribution guidelines
- [ ] Add `CODE_OF_CONDUCT.md` (use [Contributor Covenant](https://www.contributor-covenant.org/))
- [ ] Add `SECURITY.md` with vulnerability reporting instructions
- [ ] Add `CHANGELOG.md` (or plan to auto-generate from commits)

**Reference:** [02-readme](../modules/02-readme/), [03-config](../modules/03-config/)

---

## Phase 4: Templates

- [ ] Create `.github/ISSUE_TEMPLATE/bug_report.yml` (YAML form)
- [ ] Create `.github/ISSUE_TEMPLATE/feature_request.yml` (YAML form)
- [ ] Create `.github/ISSUE_TEMPLATE/config.yml` (optional: blank issue toggle, external links)
- [ ] Create `.github/PULL_REQUEST_TEMPLATE.md`
- [ ] Add `.github/CODEOWNERS` file

**Reference:** [04-templates](../modules/04-templates/)

---

## Phase 5: CI/CD

- [ ] Set up GitHub Actions CI workflow (see [ci-workflow-template](ci-workflow-template.yml)):
  - [ ] Lint step
  - [ ] Test step
  - [ ] Build step
- [ ] Add status badge to README
- [ ] Set up branch protection to require CI to pass
- [ ] (Optional) Add deploy workflow for releases
- [ ] (Optional) Add scheduled workflow for dependency updates

**Reference:** [06-cicd](../modules/06-cicd/)

---

## Phase 6: Security

- [ ] Enable **Dependabot** alerts and security updates
- [ ] Add `dependabot.yml` for automated version updates
- [ ] (Optional) Enable **CodeQL** analysis
- [ ] (Optional) Enable **secret scanning**
- [ ] Review and configure **security advisories**

**Reference:** [08-security](../modules/08-security/)

---

## Phase 7: Quality (Optional)

- [ ] Add `.editorconfig` for consistent formatting
- [ ] Set up linter configuration (ESLint, Prettier, Ruff, etc.)
- [ ] Add pre-commit hooks (via Husky, pre-commit, or lefthook)
- [ ] Configure **Conventional Commits** (commitlint + commitizen)
- [ ] Set up code coverage reporting

**Reference:** [12-quality](../modules/12-quality/), [11-versioning](../modules/11-versioning/)

---

## Phase 8: Community (Optional, for Open Source)

- [ ] Enable **GitHub Discussions**
- [ ] Add **funding** links (`.github/FUNDING.yml`)
- [ ] Set up **All Contributors** or similar recognition
- [ ] Add **Good First Issue** labels for newcomers
- [ ] Write a welcoming first-time contributor experience

**Reference:** [13-community](../modules/13-community/)

---

## Verification

After completing the checklist:

- [ ] README renders correctly on GitHub
- [ ] All links in README work
- [ ] CI workflow runs successfully on push
- [ ] Branch protection is active
- [ ] Issue/PR templates appear when creating new issues/PRs
- [ ] Repository appears in GitHub search for relevant topics
