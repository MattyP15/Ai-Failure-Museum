# Development Log — AI Failure Museum (COMM2020)

> **Sprint 1 activity log based on GitHub commit history.**
> Contributors: MattyP15 (John), oaz201, Lola120321, kw699, guegjie, hyamhyamhyam

---

## 22 January 2026

**MattyP15**
- Set up the GitHub repository and created the initial folder structure matching the CW1 submission layout (`0_admin`, `1_report`, `2_handover_pack`, `3_ethics_and_licensing`, `4_code`, `5_presentation`).
- Added placeholder files to each folder so the structure was visible on GitHub.
- Uploaded initial report files and removed a mistakenly created licence file.

---

## 2–3 February 2026

**kw699**
- Added a functional requirements document to the repository.
- Added a success criteria document outlining how the project will be evaluated.
- Included a WCAG compliance link in the success criteria to acknowledge accessibility obligations.
- Updated the functional requirements with additional detail.
- Added a set of AI failure case studies to the repository to begin building the exhibit dataset.

---

## 9 February 2026

**guegjie**
- Created the initial website HTML templates using a dark mode design.
- Added `style.css` to accompany the templates.

**MattyP15**
- Updated the README with project information.

---

## 10 February 2026

**oaz201**
- Started the Django project inside the `failureMuseum` folder.
- Moved all Django code into the `4_code` folder to match the submission structure.
- Linked together the main page, category page, and login page.
- Added instructions for running the server locally to the README.
- Merged the code move via pull request #4.

**hyamhyamhyam**
- Created the initial development log for Sprint 1.

---

## 11 February 2026

**Lola120321**
- Added groundwork for the curator artefact upload feature.
- Started building the curator tool upload functionality.

---

## 12 February 2026

**Lola120321**
- Reorganised and created several new files for the project structure.
- Updated the README.
- Added 'quickstart' files to help with local setup.
- Updated `views.py` and curator views.
- Added a `.env.example` file so secret keys are documented but not committed.
- Updated security settings.

---

## 15 February 2026

**oaz201**
- Finished building the artefact model.

**Lola120321**
- Updated migrations to reflect model changes.
- Fixed several bugs.

---

## 16 February 2026

**Lola120321**
- Major refactoring session: relocated files from `/djangocode` to `/museum`.
- Cleaned up and fixed various issues across the codebase.
- Updated `.gitignore` and requirements.
- Removed the `.venv` folder from the repository (it should not be version controlled).
- Updated `views.py` with minor formatting improvements.
- Updated `admin.py`.
- Created a proper `.gitignore` file.
- Worked on merging the `Artefact-model` branch into `Curator-Security-Model-MERGE`.
- Resolved merge conflicts.
- Updated the README multiple times.
- Tested branch rebasing.

**oaz201**
- Fixed a naming error — all occurrences of "Artefact" had been used where "Exhibit" was intended, and corrected this throughout.
- Fixed CSS on the category and login pages.
- Added a home button to the category page.

**kw699**
- Added merge information for branches to the README.

---

## 17 February 2026

**MattyP15**
- Implemented user authentication and role-based access control (visitor / curator roles).
- Built quiz gamification functionality (points and badge system).
- Implemented the privacy 'delete my data' feature.
- Restored the app, data, and tests folders after a previous issue.
- Added seed fixture for demo data.
- Added demo data loading instructions to the README.

**Lola120321**
- Major day of development: connected quiz functionality to exhibits.
- Pasted and integrated HTML for the quiz pages, updated URLs and views to support quiz routing.
- Created the `setupdemousers` management command.
- Fixed bugs in `category.py` and case-related files.
- Created `categories.json` fixture.
- Updated the data model (`models.py`).
- Updated seed data and `.json` fixture files to match the new format.
- Fixed redirection issues and model-related bugs.
- Re-done migrations following model changes.
- Fixed a bug in URLs.
- Added delete functionality for exhibits.
- Bug fixes across multiple files.
- Updated quiz functionality.
- Deleted leftover junk files.
- Minor general update.

**oaz201**
- Changed background colours to make quiz results more readable.

---

## 18 February 2026

**oaz201**
- Made several attempts to get the site hosted online (`trying to host`, `trying`, `trying 2`).
- Changed allowed hosts settings to support deployment.
- Added an admin page button visible only when logged in as a superuser.
- Updated buttons in `base.html`.
- Added a home button to the login page and changed the logout button on the category page.
- Fixed redirect behaviour so non-curators can't access curator functions.
- Fixed login for visitors.

**Lola120321**
- Fixed the logout button.
- Added a button to open the curator dashboard.
- Created `register.html` for user registration.
- Connected and added content to the privacy policy page.
- Cleaned up various files.
- Merged the `Curator-Security-Model-MERGE` branch.

---

## 19 February 2026

**oaz201**
- Merged the hosting branch via pull request #35 (`Trying-to-host`).
- Fixed the demo data.
- Added a new demo user.
- Fixed further issues with demo data.
- Removed redundant packages from requirements.
- Fixed demo data again after further issues.

**Lola120321**
- Rewrote a component (noted in commit as "Rewrite of the thingy").

---

*Log last updated: 19 February 2026*
