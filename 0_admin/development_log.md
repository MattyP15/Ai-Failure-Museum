Development Log 


**Sprint 1 Focus:** Project Initiation, Vertical Slice Prototype, and Core Infrastructure.

Activity Log

| Date | Team Member | Category | Activity Description |
| :--- | :--- | :--- | :--- |
| **2026-01-22** | Mathew | Infrastructure | **Repo Setup:** Initialised GitHub repository, created folder structure (0_admin, 1_report, etc.), and added placeholder files. Uploaded initial report drafts. |
| **2026-01-22** | Luqman | Management | **Kickoff:** Led the kickoff meeting, analysed the project specification, and divided Django backend tasks among developers (Mathew, Kate, Osama, Louis). |
| **2026-02-02** | Stan | Planning | **Requirements:** Added Functional Requirements and Success Criteria documents (including WCAG compliance). Started the initial AI failure case study dataset. |
| **2026-02-03** | Luqman | Management | **Sprint Planning:** Chaired the requirements meeting. Produced a task breakdown of specification requirements and assigned them to developers. |
| **2026-02-09** | Louis | Frontend | **UI Initialisation:** Created initial HTML templates with a Dark Mode design and added `style.css`. |
| **2026-02-09** | Mathew | Docs | **Documentation:** Updated the README.md to reflect project structure. |
| **2026-02-10** | Osama | Backend | **Django Init:** Started the Django project, set up the virtual environment (`venv`), and configured `.gitignore`. |
| **2026-02-10** | Kate | Backend | **Models:** Defined core Django models (`Exhibit`, `Quiz`) and ran initial migrations. |
| **2026-02-11** | Osama | Backend | **Routing:** Created views for the Home and Gallery pages and configured `urls.py`. |
| **2026-02-11** | Kate | Backend | **Admin:** Configured `admin.py` to register models for the Curator interface. |
| **2026-02-12** | Osama | Frontend | **Templates:** Created the `base.html` layout and configured static file serving. |
| **2026-02-12** | Louis | Frontend | **Exhibits:** Built the `exhibit_detail.html` template and applied styling. |
| **2026-02-12** | Hyam | Management | **Risk:** Created the initial Risk Register. |
| **2026-02-12** | Stan | Ethics | **Compliance:** Drafted the Ethical Considerations document. |
| **2026-02-13** | Osama | Data | **Seeding:** Updated the Quiz model, structured the JSON data, and wrote the seed script for the database. |
| **2026-02-13** | Mathew | Backend | **Gamification:** Implemented Quiz logic views and score calculation. |
| **2026-02-14** | Kate | Auth | **User Accounts:** Created the Custom User Model and templates for Login/Register. |
| **2026-02-14** | Louis | UI/UX | **Navigation:** Implemented the Navbar and Footer; conducted responsive design checks. |
| **2026-02-15** | Osama | Backend | **Search:** Implemented search functionality for exhibits. |
| **2026-02-15** | Mathew | Gamification | **Points:** Implemented the points system and leaderboard logic. |
| **2026-02-15** | Stan | Content | **Exhibits:** Expanded exhibit content. |
| **2026-02-16** | Hyam | Legal | **Privacy:** Drafted the Privacy Policy. |
| **2026-02-16** | Luqman | Management | **Process:** Conducted pre-submission checks and updated the Kanban board. |
| **2026-02-17** | Kate | Accessibility | **Audit:** Conducted accessibility audit and added ARIA labels. |
| **2026-02-17** | Louis | UI/UX | **Polish:** Refined CSS and fixed color contrast issues. |
| **2026-02-17** | Stan | Content | **Finalisation:** Completed writing for 20+ exhibit case studies. |
| **2026-02-18** | Osama | DevOps | **Deployment:** Configured `ALLOWED_HOSTS`, fixed deployment redirects, and added superuser admin controls. |
| **2026-02-18** | Kate | Frontend | **Integration:** Connected Privacy Policy page, created `register.html`, added Curator Dashboard button, and merged Security branch. |
| **2026-02-18** | Luqman | Management | **Support:** Assisted with deployment debugging and followed up on documentation tasks. |
| **2026-02-19** | Osama | DevOps | **Final Polish:** Merged hosting branch (PR #35), fixed demo data, and added demo user credentials. |
| **2026-02-19** | Kate | Refactoring | **Code Quality:** Refactored quiz functionality and updated settings for deployment. |
| **2026-02-19** | Luqman | Management | **Submission:** Chaired pre-submission meeting, verified the checklist, assigned final deadlines, and validated the final ZIP artifact. |
| **2026-02-19** | Hyam | Docs | **Development Log:** Created and formatted the development log. Uploaded CW1 process documents (risk register, meeting minutes, kanban export). |
| **2026-02-19** | Mathew | Testing | **Tests:** Added initial automated test suite covering RBAC, gamification, forms, curator views, quiz API, and data deletion. |

---

**Sprint 2 Focus:** Feature Expansion, Content Creation, Scope Pivot, and Final Delivery.

| Date | Team Member | Category | Activity Description |
| :--- | :--- | :--- | :--- |
| **2026-02-28** | Kate | Infrastructure | **Dependencies:** Updated `requirements.txt` for Sprint 2 with additional packages. |
| **2026-03-02** | Kate | Backend | **Models:** Updated models and views to prepare for new Sprint 2 features (categories, archiving, comments). |
| **2026-03-02** | Louis | Frontend | **UI:** Began Sprint 2 frontend work on layout and page structure improvements. |
| **2026-03-03** | Osama | Backend | **Artefacts:** Added the ability to attach artefact files to exhibits via the curator interface (PR #50). |
| **2026-03-06** | Osama | Backend | **Merge & Fix:** Merged the artefact branch into main and fixed migration issues caused by the merge. |
| **2026-03-07** | Louis | Frontend | **UI:** Continued CSS separation and general UI improvements across pages. |
| **2026-03-11** | Osama | Bug Fix | **Artefact Fix:** Fixed artefact display issue on exhibit detail pages. |
| **2026-03-13** | Kate | Backend | **Categories:** Edited the Category model, added category to admin panel, implemented archiving functionality with archive/unarchive toggle, and added view tracking notifications. |
| **2026-03-13** | Louis | Frontend | **CSS:** Separated CSS into individual stylesheets per page for maintainability. |
| **2026-03-14** | Louis | Bug Fix | **Spelling Fix:** Corrected all occurrences of "archieved" to "archived" across the codebase. |
| **2026-03-15** | Osama | Backend | **Quiz Changes:** Updated quiz mechanics and scoring logic. |
| **2026-03-16** | Louis | Frontend | **UI Polish:** Small fixes to footer, dashboard, and main page layouts. |
| **2026-03-17** | Louis | Frontend | **Dashboard UI:** Built the filter interface for the curator dashboard with archive/unarchive buttons and category filtering. |
| **2026-03-17** | Kate | Backend | **Archive Fix:** Fixed the archive toggle functionality and updated README. |
| **2026-03-17** | Hyam | Management | **Scope Decision:** Confirmed the pivot from 1 failure category (Environmental) to 8 categories across the full dataset. Began restructuring exhibit content. |
| **2026-03-19** | Osama | Backend | **Quiz Merge:** Merged enhanced quiz functionality branch (PR #52), adding more question types and improved scoring. |
| **2026-03-19** | Louis | Frontend | **Login Redesign:** Redesigned the login page and edit exhibit page. Fixed various UI bugs. |
| **2026-03-19** | Kate | Backend | **Comments:** Implemented the Comment model and started building the comment section for exhibit pages. Updated forms to include comment functionality. Rebuilt category structure. |
| **2026-03-19** | Luqman | Frontend | **Login Page:** Worked on the CSS and HTML for the login and register pages. |
| **2026-03-20** | Kate | Backend | **Bookmarks:** Implemented the Bookmark model and toggle functionality, allowing visitors to bookmark exhibits and view them at `/my-bookmarks/`. |
| **2026-03-21** | Kate | Backend | **Community Submissions:** Added the UserSubmission model with pending/approved/denied status workflow. Implemented visitor submission form and curator review pool. |
| **2026-03-21** | Luqman | Frontend | **Register Page:** Created `register.css` and further developed the register page design. |
| **2026-03-21** | Louis | Frontend | **Bookmarking UI:** Implemented bookmarking UI elements and simple upload interface for the dashboard. |
| **2026-03-22** | Osama | Backend | **Timelines:** Added the TimelineEvent model and integrated timeline editing into the curator exhibit editor (PR #53). Updated create_exhibit page styling. |
| **2026-03-22** | Osama | Backend | **Deployment:** Changed database configuration for Render production deployment. Added artefact files to the media folder. |
| **2026-03-22** | Kate | Backend | **View Tracking:** Fixed view count display in templates. Updated categories and settings for production. |
| **2026-03-22** | Luqman | Frontend | **Quiz Styling:** Changed quiz pages from dark mode to light mode. Updated quiz CSS. |
| **2026-03-22** | Mathew | Backend | **View Tracking:** Fixed exhibit view tracking with two successive bug fix commits. Merged Sprint-2-features branch. |
| **2026-03-22** | Louis | Frontend | **Dashboard Features:** Added explore page, fixed dashboard features, and updated base template for consistent header across all pages. |
| **2026-03-22** | Hyam | Data | **Fixtures:** Added initial data fixtures (exhibits.json and quizzes.json) containing all 20 exhibits and 40 quizzes with 200 questions. |
| **2026-03-23** | Hyam | Content | **Exhibit Data:** Uploaded final exhibit and quiz data covering all 8 categories. Added D3.js interactive force-directed graph to the homepage. Refactored `main.html` for improved structure and added a carousel feature. |
| **2026-03-23** | Osama | Data | **Accounts:** Created `Accounts.json` fixture for demo user accounts and updated README with full setup instructions and credentials. |
| **2026-03-23** | Kate | Frontend | **Final Pages:** Updated about page. Added terms of service and accessibility pages. Fixed login and register page issues. Removed D3 graph after testing. Various bug fixes and formatting. Created `launch.py` convenience script. |
| **2026-03-23** | Louis | Bug Fix | **Final Fixes:** Bug fixes, formatting corrections, SPAG (spelling, punctuation, and grammar) fixes across the site. Changed points awarded per quiz. Added explore page and fixed dashboard features. |
| **2026-03-24** | Hyam | Management | **Documentation:** Coordinated final CW2 documentation package. Updated risk register for Sprint 2. Prepared submission materials. |
| **2026-03-24** | Hyam | Content | **Artefacts:** Finalised all 20 supporting artefact visualisations (data vis diagrams with stand-in data) in PNG format with consistent naming convention. |
