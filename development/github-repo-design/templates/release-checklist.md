# Release Checklist

Step-by-step checklist for publishing a new release. Fill in the version number and work through each section.

**Release version:** `vX.Y.Z`
**Release date:** YYYY-MM-DD
**Release manager:** @username

---

## Pre-Release

- [ ] All CI checks pass on `main`
- [ ] No open blockers or critical bugs for this milestone
- [ ] All planned PRs for this release are merged
- [ ] Dependencies are up to date (`npm outdated` / `pip list --outdated`)

---

## Version Bump

- [ ] Determine version increment following [SemVer](https://semver.org/):
  - **Patch** (x.y.Z) — bug fixes, no API changes
  - **Minor** (x.Y.0) — new features, backward compatible
  - **Major** (X.0.0) — breaking changes
- [ ] Update version in package manifest (`package.json`, `pyproject.toml`, `Cargo.toml`, etc.)
- [ ] Update version in any hardcoded references (docs, badges, constants)
- [ ] Run tests after version bump to confirm nothing broke

---

## Changelog

- [ ] Update `CHANGELOG.md` with all changes since last release:
  - **Added** — new features
  - **Changed** — changes to existing functionality
  - **Deprecated** — features to be removed in future
  - **Removed** — features removed in this release
  - **Fixed** — bug fixes
  - **Security** — vulnerability fixes
- [ ] Review changelog for clarity and completeness
- [ ] (Optional) Auto-generate from Conventional Commits:
  ```bash
  # Example with conventional-changelog
  npx conventional-changelog -p angular -i CHANGELOG.md -s
  ```

---

## Commit and Tag

- [ ] Commit version bump and changelog:
  ```bash
  git add -A
  git commit -m "chore: release vX.Y.Z"
  ```
- [ ] Create annotated git tag:
  ```bash
  git tag -a vX.Y.Z -m "Release vX.Y.Z"
  ```
- [ ] Push commit and tag:
  ```bash
  git push origin main
  git push origin vX.Y.Z
  ```

---

## Publish

- [ ] **npm:** `npm publish` (with `--tag next` for pre-releases)
- [ ] **PyPI:** `python -m build && twine upload dist/*`
- [ ] **Crates.io:** `cargo publish`
- [ ] **Docker Hub:** `docker build -t image:vX.Y.Z . && docker push image:vX.Y.Z`
- [ ] (Or let CI handle publishing via tag-triggered workflow)

---

## GitHub Release

- [ ] Create GitHub Release from the tag:
  ```bash
  gh release create vX.Y.Z --title "vX.Y.Z" --notes-file CHANGELOG_EXCERPT.md
  ```
  Or create manually via GitHub UI:
  - Go to Releases > Draft a new release
  - Select the tag `vX.Y.Z`
  - Paste changelog excerpt as release notes
  - Attach any binary artifacts
- [ ] Mark as pre-release if applicable
- [ ] (Optional) Use GitHub's auto-generated release notes as a starting point

---

## Post-Release

- [ ] Verify the published package installs correctly:
  ```bash
  npm install PACKAGE@vX.Y.Z    # or pip install, cargo install, etc.
  ```
- [ ] Verify GitHub Release page looks correct
- [ ] Update documentation site if versioned separately
- [ ] Announce the release:
  - [ ] GitHub Discussions / project blog
  - [ ] Social media (Twitter/X, Mastodon, etc.)
  - [ ] Discord / Slack community channels
  - [ ] (Optional) Email newsletter
- [ ] Close the milestone in GitHub Issues
- [ ] Update project board / roadmap

---

## Rollback Plan

If a critical issue is found after release:

1. **Yank/unpublish** the broken version if possible (`npm unpublish`, `cargo yank`)
2. Fix the issue on `main`
3. Release a patch version (vX.Y.Z+1) following this same checklist
4. Post an incident note in the GitHub Release or Discussions
