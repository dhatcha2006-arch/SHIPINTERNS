# SkillForge – Internship & Training Academy Management Platform

SkillForge is a production-grade, enterprise-ready internship and training academy management platform connecting students, mentors, corporate training partners, and administrators.

## Technology Stack
- **Frontend:** HTML5, CSS3, Bootstrap 5.3, Vanilla JavaScript (ES6+), Jinja2 Templates, Fetch API
- **Backend:** Python Flask REST APIs
- **Design Philosophy:** Human-Crafted, Anti-Slop, Strict 4px Scale, High-Contrast Typography
- **Primary Contributor:** dhatcha2006 (Lead Frontend Developer)

## 30 Completed Pull Requests & Implementation Roadmap
- [x] **PR #1**: `feat/01-frontend-setup` - Frontend setup, Jinja base template, unified API client, pytest runner
- [x] **PR #2**: `feat/02-design-system` - Core design tokens, layout grid, component styling, interactive toast library
- [x] **PR #3**: `feat/03-nav-sidebar-footer` - Responsive public navbar, footer, role-aware sidebar and application topbar
- [x] **PR #4**: `feat/04-academy-homepage` - Academy landing page with value proposition, live preview card and metric counters
- [x] **PR #5**: `feat/05-about-and-programs` - About Us, Training Programs, Contact and Careers pages
- [x] **PR #6**: `feat/06-internship-listing` - Filterable internship catalog with domain tags and stipend cards
- [x] **PR #7**: `feat/07-auth-suite` - Login with role demo switcher, intern registration with track selector, password recovery
- [x] **PR #8**: `feat/08-student-dashboard` - Intern cockpit with sprint progress metrics, active deliverables and mentor card
- [x] **PR #9**: `feat/09-student-profile` - Student profile with official cryptographic Skill Passport and verified competency badges
- [x] **PR #10**: `feat/10-internship-application` - Multi-step internship application wizard and real-time status tracker timeline
- [x] **PR #11**: `feat/11-course-listing` - Curriculum course catalog with progress tracking and syllabus previews
- [x] **PR #12**: `feat/12-course-details` - Interactive syllabus accordion with module breakdown and evaluation rubric
- [x] **PR #13**: `feat/13-learning-roadmap` - Interactive 8-sprint learning roadmap with progress nodes and lock states
- [x] **PR #14**: `feat/14-lesson-interface` - Lesson reader with video player mock, transcript tabs, and module playlist
- [x] **PR #15**: `feat/15-assignment-dashboard` - Assignments dashboard with deadline countdowns, mentor reviewer tags and rubric scores
- [x] **PR #16**: `feat/16-assignment-submission` - Assignment submission workspace with PR verification, remarks editor and quality checklist
- [x] **PR #17**: `feat/17-coding-assessment` - In-browser coding assessment studio with split-pane code editor and automated test runner
- [x] **PR #18**: `feat/18-quiz-interface` - Timed examination engine with question navigator, timer countdown, and instant grade evaluation
- [x] **PR #19**: `feat/19-mentor-dashboard` - Mentor velocity cockpit with pending PR review queue and intern squad allocation
- [x] **PR #20**: `feat/20-mentor-allocation` - Mentor capacity meter, squad allocation table, and 1-on-1 scheduling flow
- [x] **PR #21**: `feat/21-live-project-dashboard` - Live supervised project dashboard and interactive Agile Kanban task tracking board
- [x] **PR #22**: `feat/22-github-submission` - GitHub pull request submission interface with automated CI/CD test verification
- [x] **PR #23**: `feat/23-zoom-meeting` - Zoom virtual classroom interface with participant video stage, control toggles, and secure token isolation
- [x] **PR #24**: `feat/24-google-meet` - Google Meet scheduling workspace with time slot selector, session links and calendar dispatch
- [x] **PR #25**: `feat/25-attendance-dashboard` - Attendance dashboard with check-in timestamping, monthly heatmap calendar, and regularization requests
- [x] **PR #26**: `feat/26-daily-work-reports` - Structured daily work report (DWR) logger with mentor verification history
- [x] **PR #27**: `feat/27-evaluation-and-feedback` - Student evaluation scorecard and mentor interactive rubric grading workspace
- [x] **PR #28**: `feat/28-certificate-verification` - High-fidelity certificate viewer and public cryptographic verification portal
- [x] **PR #29**: `feat/29-admin-and-hr-portal` - Admin cohort governance console and HR corporate talent sourcing portal
- [x] **PR #30**: `feat/30-polish-qa-documentation` - Student analytics dashboard, full end-to-end test suite, and architecture documentation

## Running the Application
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run Flask application
python app.py

# 3. Run test suite
pytest frontend/tests/
```
Application will be available at `http://127.0.0.1:5000/`.
