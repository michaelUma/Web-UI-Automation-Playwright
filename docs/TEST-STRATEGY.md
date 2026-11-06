# UI Automation Test Strategy

## Scope
Basic login flow and authenticated inventory display on SauceDemo.

## Locator strategy
Prefer accessible roles and labels, then stable data-test attributes. Avoid brittle positional CSS selectors.

## Reliability
- Wait for observable conditions, not arbitrary delays.
- Keep tests independent.
- Use isolated browser contexts.
- Capture screenshots/traces when investigating failures.
- Investigate flaky tests rather than repeatedly rerunning them.

## Extensions
Add cart workflows, checkout validation, keyboard navigation, focus order, and accessibility checks. Automated accessibility scans supplement manual evaluation.

## Boundaries
This is a learning example, not proof of exhaustive testing or a production certification.
