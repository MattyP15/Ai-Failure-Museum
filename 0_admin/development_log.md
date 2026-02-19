Development Log 

22 January 2026
Matthew
•	Set up the GitHub repository and created the initial folder structure matching the CW1 submission layout (0_admin, 1_report, 2_handover_pack, 3_ethics_and_licensing, 4_code, 5_presentation).
•	Added placeholder files to each folder so the structure was visible on GitHub.
•	Uploaded initial report files and removed a mistakenly created licence file.
Luqman
•	Read through the full project specification in detail before the kickoff meeting.
•	Identified all the Django tasks that would need to be completed across the sprint.
•	Led the kickoff meeting, explained the spec requirements to the group, and divided the Django work between the four backend developers (Matthew, Kate, Osama, Stan).

2–3 February 2026
Louis
•	Added a functional requirements document to the repository.
•	Added a success criteria document outlining how the project will be evaluated.
•	Included a WCAG compliance link in the success criteria to acknowledge accessibility obligations.
•	Updated the functional requirements with additional detail.
•	Added a set of AI failure case studies to begin building the exhibit dataset.
Luqman
•	Chaired the requirements and planning meeting.
•	Produced a detailed breakdown of all Django tasks from the spec and allocated them between the four Django developers, confirming who is responsible for which features.
•	Checked in with individual team members during the week to make sure everyone understood their tasks.

9 February 2026
Stan
•	Created the initial website HTML templates using a dark mode design.
•	Added style.css to accompany the templates.
Matthew
•	Updated the README with project information.

10 February 2026
Osama
•	Started the Django project inside the failureMuseum folder.
•	Moved all Django code into the 4_code folder to match the submission structure.
•	Linked together the main page, category page, and login page.
•	Added instructions for running the server locally to the README.
•	Merged the code move via pull request #4.
Hyam
•	Created the initial development log for Sprint 1.
Luqman
•	Chaired the technical check-in meeting.
•	Went round each team member to get a progress update and flagged any blockers.
•	Confirmed the data model requirements from the spec and made sure the team's model plan covered everything needed.
•	Identified that the .venv folder had been accidentally committed to GitHub and flagged it to Kate to fix.

11 February 2026
Kate
•	Added groundwork for the curator artefact upload feature.
•	Started building the curator tool upload functionality.

12 February 2026
Kate
•	Reorganised and created several new files for the project structure.
•	Updated the README.
•	Added 'quickstart' files to help with local setup.
•	Updated views.py and curator views.
•	Added a .env.example file so secret keys are documented but not committed.
•	Updated security settings.
Luqman
•	Mid-week check-in with all Django developers to confirm tasks from the previous meeting were on track.
•	Verified that the .env.example and .gitignore fixes had been completed.

15 February 2026
Osama
•	Finished building the artefact model.
Kate
•	Updated migrations to reflect model changes.
•	Fixed several bugs.

16 February 2026
Kate
•	Major refactoring session: relocated files from /djangocode to /museum.
•	Cleaned up and fixed various issues across the codebase.
•	Updated .gitignore and requirements.
•	Removed the .venv folder from the repository.
•	Updated views.py with minor formatting improvements.
•	Updated admin.py.
•	Created a proper .gitignore file.
•	Worked on merging the Artefact-model branch into Curator-Security-Model-MERGE.
•	Resolved merge conflicts.
•	Updated the README multiple times.
Osama
•	Fixed a naming error — all occurrences of "Artefact" had been used where "Exhibit" was intended, and corrected this throughout.
•	Fixed CSS on the category and login pages.
•	Added a home button to the category page.
Louis
•	Added merge information for branches to the README.
Luqman
•	Chaired the integration and sprint push meeting.
•	Reviewed progress across the whole team and identified that the dataset (exhibits, quiz questions) was the main risk area.
•	Ran through the full CW1 submission checklist against the spec and identified all outstanding items.
•	Divided the remaining documentation tasks between team members and agreed deadlines for each.

17 February 2026
Matthew
•	Implemented user authentication and role-based access control (visitor / curator roles).
•	Built quiz gamification functionality (points and badge system).
•	Implemented the privacy 'delete my data' feature.
•	Restored the app, data, and tests folders after a previous issue.
•	Added seed fixture for demo data.
•	Added demo data loading instructions to the README.
Kate
•	Connected quiz functionality to exhibits (views, URLs, HTML).
•	Created the setupdemousers management command.
•	Fixed bugs in category.py and case-related files.
•	Created categories.json fixture.
•	Updated the data model (models.py).
•	Updated seed data and .json fixture files to the new format.
•	Fixed redirection issues and model-related bugs.
•	Re-done migrations following model changes.
•	Fixed a bug in URLs.
•	Added delete functionality for exhibits.
•	Bug fixes across multiple files.
•	Updated quiz functionality.
•	Deleted leftover junk files.
Osama
•	Changed background colours to make quiz results more readable.
Luqman
•	Chased up outstanding documentation tasks with each team member.
•	Checked in with Louis on case study content progress and confirmed more exhibits were being written to reach the 20+ target.
•	Monitored overall progress and made sure the team stayed focused ahead of the deadline.

18 February 2026
Osama
•	Made several attempts to get the site hosted online.
•	Changed allowed hosts settings to support deployment.
•	Added an admin page button visible only when logged in as a superuser.
•	Updated buttons in base.html.
•	Added a home button to the login page and changed the logout button on the category page.
•	Fixed redirect behaviour so non-curators can't access curator functions.
•	Fixed login for visitors.
Kate
•	Fixed the logout button.
•	Added a button to open the curator dashboard.
•	Created register.html for user registration.
•	Connected and added content to the privacy policy page.
•	Cleaned up various files.
•	Merged the Curator-Security-Model-MERGE branch.
Luqman
•	Checked in with Osama on deployment progress and helped look through error logs.
•	Followed up with all team members on their outstanding documentation items ahead of the submission.

19 February 2026
Osama
•	Merged the hosting branch via pull request #35 (Trying-to-host).
•	Fixed the demo data.
•	Added a new demo user.
•	Fixed further issues with demo data.
•	Removed redundant packages from requirements.
•	Fixed demo data again after further issues.
Kate
•	Rewrote a key component that needed improving.
Luqman
•	Chaired the pre-submission meeting.
•	Went through the full submission checklist and confirmed what was done and what was still outstanding.
•	Assigned remaining tasks to team members with a hard end-of-day deadline.
•	Did a final check of the submission materials before the ZIP was put together.

Log last updated: 19 February 2026

