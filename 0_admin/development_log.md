Development Log — AI Failure Museum (COMM2020)
Sprint 1 activity log based on GitHub commit history. Team: Mathew, Osama, Kate, Stan, Louis, Hyam, Luqman 
________________________________________
22 January 2026
Mathew
•	Set up the GitHub repository and created the folder structure for the CW1 submission (0_admin, 1_report, 2_handover_pack, 3_ethics_and_licensing, 4_code, 5_presentation)
•	Added placeholder files to each folder
•	Uploaded initial report files and removed a mistakenly created licence file
Luqman
•	Read through the full project spec before the kickoff meeting
•	Identified all the Django tasks that would need doing across the sprint
•	Led the kickoff meeting, explained the spec to the group, and divided the Django work between the four backend developers (Mathew, Kate, Osama, Louis)
________________________________________
2–3 February 2026
Stan
•	Added a functional requirements document to the repository
•	Added a success criteria document
•	Added a WCAG compliance link to the success criteria
•	Updated the functional requirements with more detail
•	Added initial AI failure case studies to start the exhibit dataset
Luqman
•	Chaired the requirements and planning meeting
•	Produced a breakdown of all Django tasks from the spec and assigned them to the four Django developers
•	Checked in with team members during the week to make sure everyone was clear on their tasks
________________________________________
9 February 2026
Louis
•	Created the initial website HTML templates using a dark mode design
•	Added style.css
Mathew
•	Updated the README
________________________________________
10 February 2026
Osama
•	Started the Django project in the failureMuseum folder
•	Moved Django code into the 4_code folder to match the submission structure
•	Linked the main page, category page, and login page together
•	Added instructions for running the server locally to the README
•	Merged the code move via pull request #4
Hyam
•	Created the initial development log for Sprint 1
Luqman
•	Chaired the technical check-in meeting
•	Went round the group to get progress updates and flagged blockers
•	Checked the data model requirements from the spec and made sure the team's plan covered everything
•	Spotted that the .venv folder had been accidentally committed and flagged it to Kate
________________________________________
11 February 2026
Kate
•	Added groundwork for the curator artefact upload feature
•	Started building the curator tool upload functionality
________________________________________
12 February 2026
Kate
•	Reorganised and created several new project files
•	Updated the README
•	Added quickstart files to help with local setup
•	Updated views.py and curator views
•	Added a .env.example file so secret keys are documented but not committed
•	Updated security settings
Luqman
•	Mid-week check-in with all Django developers to make sure tasks from the last meeting were on track
•	Verified the .env.example and .gitignore fixes had been done
________________________________________
15 February 2026
Osama
•	Finished the artefact model
Kate
•	Updated migrations to reflect model changes
•	Fixed several bugs
________________________________________
16 February 2026
Kate
•	Relocated files from /djangocode to /museum to tidy up the project structure
•	Cleaned up and fixed various issues across the codebase
•	Updated .gitignore and requirements
•	Removed the .venv folder from the repository
•	Updated views.py with minor formatting improvements
•	Updated admin.py
•	Created a proper .gitignore
•	Merged the Artefact-model branch into Curator-Security-Model-MERGE
•	Resolved merge conflicts
•	Updated the README multiple times
Osama
•	Fixed a naming error — 'Artefact' had been used throughout where 'Exhibit' was intended and corrected it everywhere
•	Fixed CSS on the category and login pages
•	Added a home button to the category page
Stan
•	Added branch merge information to the README
Luqman
•	Chaired the integration and sprint push meeting
•	Reviewed progress across the team and flagged that the dataset (exhibits, quiz questions) was the main risk
•	Went through the full CW1 submission checklist against the spec and listed all outstanding items
•	Divided remaining documentation tasks between team members with agreed deadlines
________________________________________
17 February 2026
Mathew
•	Implemented user authentication and role-based access control (visitor / curator roles)
•	Built quiz gamification (points and badge system)
•	Implemented the privacy delete-my-data feature
•	Restored the app, data, and tests folders after a previous issue
•	Added seed fixture for demo data
•	Added demo data loading instructions to the README
Kate
•	Connected quiz functionality to exhibits (views, URLs, HTML)
•	Created the setupdemousers management command
•	Fixed bugs in category.py and case-related files
•	Created categories.json fixture
•	Updated models.py
•	Updated seed data and .json fixtures to the new format
•	Fixed redirection issues and model bugs
•	Re-done migrations after model changes
•	Fixed a bug in URLs
•	Added delete functionality for exhibits
•	General bug fixes across multiple files
•	Updated quiz functionality
•	Deleted leftover junk files
Osama
•	Changed background colours to make quiz results more readable
Luqman
•	Chased up outstanding documentation tasks with each team member
•	Checked in with Stan on case study progress and confirmed more exhibits were being written to hit the 20+ target
•	Monitored overall progress and kept the team focused ahead of the deadline
________________________________________
18 February 2026
Osama
•	Made several attempts to get the site hosted online
•	Changed allowed hosts settings for deployment
•	Added an admin page button that only shows when logged in as a superuser
•	Updated buttons in base.html
•	Added a home button to the login page and changed the logout button on the category page
•	Fixed redirect behaviour so non-curators can't access curator functions
•	Fixed login for visitors
Kate
•	Fixed the logout button
•	Added a button to open the curator dashboard
•	Created register.html for user registration
•	Connected and added content to the privacy policy page
•	Cleaned up various files
•	Merged the Curator-Security-Model-MERGE branch
Luqman
•	Checked in with Osama on deployment progress and helped look through error logs
•	Followed up with all team members on outstanding documentation items
________________________________________
19 February 2026
Osama
•	Merged the hosting branch via pull request #35
•	Fixed the demo data
•	Added a new demo user for the marker
•	Removed redundant packages from requirements
•	Further demo data fixes
Kate
•	Rewrote a component that needed improving
Luqman
•	Chaired the pre-submission meeting
•	Went through the full submission checklist and confirmed what was done and what was outstanding
•	Assigned remaining tasks to team members with a hard end-of-day deadline
•	Did a final check of the submission materials before the ZIP was put together
________________________________________
Last updated: 19 February 2026

