# SkillForge Architecture & Frontend Engineering Specification

## Architecture Overview
SkillForge is built using a decoupled, modular Flask Jinja2 + Bootstrap 5.3 + Vanilla ES6 architecture. The frontend strictly avoids AI slop, decorative gradients, and ungrounded templates in favor of a clean, human-crafted engineering design system.

### Core Principles (Unslop Standard):
1. **4px Grid Discipline:** All margins, paddings, gaps, and heights follow strict multiples of 4px.
2. **Slate Neutral Ramp:** Consistent neutral palette from `--sf-slate-50` to `--sf-slate-900` with one primary brand accent (`#2563EB`).
3. **No Colored Glowing Blobs:** Soft, neutral 1px hairline borders (`rgba(15, 23, 42, 0.08)`) with natural shadows.
4. **Nested Radii Rule:** Controls: `8px`, Cards: `12px`, Modals: `16px`.
5. **Human Typography:** Inter for crisp headings and interface text; JetBrains Mono for code blocks and tabular metrics.

## 30 Production Modules
1. Public Website: Home (`/`)
2. About Us (`/about`)
3. Training Programs (`/programs`)
4. Internship Listings (`/internships`)
5. Contact Page (`/contact`)
6. Careers Page (`/careers`)
7. Login (`/auth/login`)
8. Register (`/auth/register`)
9. Password Recovery (`/auth/forgot-password`)
10. Student Dashboard (`/student/dashboard`)
11. Student Profile & Skill Passport (`/student/profile`)
12. Internship Application Form (`/student/apply`)
13. Application Status Tracker (`/student/application-status`)
14. Course Catalog (`/student/courses`)
15. Course Details & Syllabus (`/student/courses/<id>`)
16. Learning Roadmap Tree (`/student/roadmap`)
17. Video & Lesson Player (`/student/lesson`)
18. Assignment Dashboard (`/student/assignments`)
19. Assignment Submission Workspace (`/student/assignments/<id>/submit`)
20. In-Browser Coding Assessment Studio (`/student/coding-assessment`)
21. Timed Quiz & Examination Engine (`/student/quiz`)
22. Mentor Dashboard (`/mentor/dashboard`)
23. Mentor Allocation Directory (`/mentor/allocations`)
24. Mentor Grading Workspace (`/mentor/feedback`)
25. Live Supervised Project (`/projects/dashboard`)
26. Project Task Tracking & Kanban (`/projects/tasks`)
27. GitHub PR Review Submission (`/projects/github-submit`)
28. Zoom Virtual Classroom (`/projects/zoom-meet`)
29. Google Meet Scheduler (`/projects/google-meet`)
30. Attendance & Daily Work Reports (`/student/attendance`, `/student/daily-report`, `/certificates/view/<id>`, `/certificates/verify`, `/admin/dashboard`, `/employee/portal`, `/student/analytics`)
