# Web App Test Plan

> Fill in each section to define your test plan. Remove sections that do not apply.

## Overview

| Field | Value |
|-------|-------|
| **App Name** | _Name of the web application_ |
| **URL** | `http://localhost:3000` |
| **Framework** | React / Next.js / Vue / Svelte / Other |
| **Test Tool** | Playwright |
| **Browser(s)** | Chromium / Firefox / WebKit / All |

## Environment Setup

### Prerequisites

| Dependency | Version | Install |
|-----------|---------|---------|
| Node.js | `>=18` | `brew install node` |
| Playwright | `latest` | `npm install -D @playwright/test` |
| Browsers | -- | `npx playwright install` |

### Configuration

```bash
# Start the app
npm run dev

# Verify it is running
curl http://localhost:3000
```

### Environment Variables

| Variable | Value | Purpose |
|----------|-------|---------|
| `BASE_URL` | `http://localhost:3000` | App URL |
| `TEST_USER` | `test@example.com` | Test account |
| `TEST_PASSWORD` | `(from .env.test)` | Test account password |

## Test Scenarios

### Scenario 1: _User Login_

| Field | Value |
|-------|-------|
| **Priority** | High / Medium / Low |
| **Preconditions** | Test user exists in database |
| **Category** | Auth / Navigation / CRUD / UI / Performance |

**Steps:**

| # | Action | Expected Result |
|---|--------|----------------|
| 1 | Navigate to `/login` | Login form is visible |
| 2 | Enter valid email and password | Fields accept input |
| 3 | Click "Sign In" button | Redirect to `/dashboard` |
| 4 | Check page content | Welcome message contains username |

**Playwright Sketch:**

```python
page.goto("/login")
page.fill("[name=email]", "test@example.com")
page.fill("[name=password]", "password")
page.click("button[type=submit]")
expect(page).to_have_url("/dashboard")
expect(page.locator("h1")).to_contain_text("Welcome")
```

### Scenario 2: _Page Navigation_

| Field | Value |
|-------|-------|
| **Priority** | High |
| **Preconditions** | User is logged in |
| **Category** | Navigation |

**Steps:**

| # | Action | Expected Result |
|---|--------|----------------|
| 1 | Click "Settings" in nav | Navigate to `/settings` |
| 2 | Click browser back button | Return to previous page |
| 3 | Click logo | Navigate to home page |

### Scenario 3: _Form Submission_

_Copy the scenario block above for each additional test scenario._

## Error Scenarios

| Scenario | Trigger | Expected Behavior |
|----------|---------|-------------------|
| Invalid login | Wrong password | Error message displayed, no redirect |
| Network failure | Disconnect network | Graceful error message, retry option |
| 404 page | Navigate to `/nonexistent` | Custom 404 page displayed |
| Session expired | Wait for token expiry | Redirect to login with message |

## Visual / Screenshot Tests

| Page | Viewport | Screenshot Name |
|------|----------|----------------|
| Home | 1280x720 | `home-desktop.png` |
| Home | 375x667 | `home-mobile.png` |
| Dashboard | 1280x720 | `dashboard-desktop.png` |

## Performance Checks

| Metric | Target | How to Measure |
|--------|--------|---------------|
| Page load time | < 3s | `page.goto()` + timing API |
| Largest Contentful Paint | < 2.5s | Performance observer |
| No console errors | 0 errors | `page.on("console")` listener |

## Execution Checklist

- [ ] Environment is running and accessible
- [ ] Test accounts are provisioned
- [ ] All high-priority scenarios pass
- [ ] All medium-priority scenarios pass
- [ ] Error scenarios handled gracefully
- [ ] Screenshots captured for visual review
- [ ] No console errors during test run
- [ ] Test results documented

## Notes

_Add any additional context, known issues, or special instructions here._
