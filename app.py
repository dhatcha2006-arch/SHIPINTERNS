import os
from flask import Flask, render_template, jsonify, request, send_from_directory

app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), 'frontend', 'templates'),
    static_folder=os.path.join(os.path.dirname(__file__), 'frontend', 'static'),
    static_url_path='/static'
)
app.config['SECRET_KEY'] = 'skillforge-dev-secret-key-2026'

# --- PUBLIC ROUTES ---
@app.route('/')
def home():
    return render_template('public/index.html')

@app.route('/about')
def about():
    return render_template('public/about.html')

@app.route('/programs')
def programs():
    return render_template('public/programs.html')

@app.route('/internships')
def internships():
    return render_template('public/internships.html')

@app.route('/contact')
def contact():
    return render_template('public/contact.html')

@app.route('/careers')
def careers():
    return render_template('public/careers.html')

# --- AUTH ROUTES ---
@app.route('/auth/login')
def login():
    return render_template('auth/login.html')

@app.route('/auth/register')
def register():
    return render_template('auth/register.html')

@app.route('/auth/forgot-password')
def forgot_password():
    return render_template('auth/forgot_password.html')

# --- STUDENT ROUTES ---
@app.route('/student/dashboard')
def student_dashboard():
    return render_template('student/dashboard.html')

@app.route('/student/profile')
def student_profile():
    return render_template('student/profile.html')

@app.route('/student/apply')
def student_apply():
    return render_template('student/apply.html')

@app.route('/student/application-status')
def student_application_status():
    return render_template('student/application_status.html')

@app.route('/student/courses')
def student_courses():
    return render_template('student/courses.html')

@app.route('/student/courses/<int:course_id>')
def student_course_details(course_id):
    return render_template('student/course_details.html', course_id=course_id)

@app.route('/student/roadmap')
def student_roadmap():
    return render_template('student/roadmap.html')

@app.route('/student/lesson')
def student_lesson():
    return render_template('student/lesson.html')

@app.route('/student/progress')
def student_progress():
    return render_template('student/progress.html')

@app.route('/student/assignments')
def student_assignments():
    return render_template('student/assignments.html')

@app.route('/student/assignments/<int:assignment_id>/submit')
def student_assignment_submit(assignment_id):
    return render_template('student/assignment_submit.html', assignment_id=assignment_id)

@app.route('/student/coding-assessment')
def student_coding_assessment():
    return render_template('student/coding_assessment.html')

@app.route('/student/quiz')
def student_quiz():
    return render_template('student/quiz.html')

@app.route('/student/attendance')
def student_attendance():
    return render_template('student/attendance.html')

@app.route('/student/daily-report')
def student_daily_report():
    return render_template('student/daily_report.html')

@app.route('/student/evaluations')
def student_evaluations():
    return render_template('student/evaluations.html')

@app.route('/student/analytics')
def student_analytics():
    return render_template('student/analytics.html')

# --- MENTOR ROUTES ---
@app.route('/mentor/dashboard')
def mentor_dashboard():
    return render_template('mentor/dashboard.html')

@app.route('/mentor/allocations')
def mentor_allocations():
    return render_template('mentor/allocations.html')

@app.route('/mentor/feedback')
def mentor_feedback():
    return render_template('mentor/feedback.html')

# --- PROJECTS & COLLABORATION ROUTES ---
@app.route('/projects/dashboard')
def project_dashboard():
    return render_template('projects/dashboard.html')

@app.route('/projects/tasks')
def project_tasks():
    return render_template('projects/tasks.html')

@app.route('/projects/github-submit')
def github_submit():
    return render_template('projects/github_submit.html')

@app.route('/projects/zoom-meet')
def zoom_meet():
    return render_template('projects/zoom_meet.html')

@app.route('/projects/google-meet')
def google_meet():
    return render_template('projects/google_meet.html')

# --- CERTIFICATES ---
@app.route('/certificates/view/<cert_id>')
def certificate_view(cert_id):
    return render_template('certificates/view.html', cert_id=cert_id)

@app.route('/certificates/verify')
@app.route('/certificates/verify/<cert_id>')
def certificate_verify(cert_id=None):
    return render_template('certificates/verify.html', cert_id=cert_id)

# --- ADMIN & HR PORTALS ---
@app.route('/admin/dashboard')
def admin_dashboard():
    return render_template('admin/dashboard.html')

@app.route('/employee/portal')
def employee_portal():
    return render_template('employee/portal.html')

# --- API ENDPOINTS (COORDINATED WITH ARI) ---
@app.route('/api/v1/health')
def api_health():
    return jsonify({"status": "healthy", "service": "SkillForge Frontend-Backend Gateway", "version": "1.0.0"})

@app.route('/api/v1/auth/login', methods=['POST'])
def api_login():
    data = request.get_json() or {}
    email = data.get('email', '')
    role = 'student'
    if 'mentor' in email:
        role = 'mentor'
    elif 'admin' in email:
        role = 'admin'
    elif 'hr' in email or 'emp' in email:
        role = 'employee'
    return jsonify({
        "success": True,
        "token": "sf_token_" + os.urandom(12).hex(),
        "user": {
            "id": 101,
            "name": "Dhatchanamoorthi Anbazhagan",
            "email": email or "dhatcha2006@skillforge.edu",
            "role": role,
            "cohort": "Spring 2026 Full Stack Cohort"
        }
    })

@app.route('/api/v1/auth/register', methods=['POST'])
def api_register():
    data = request.get_json() or {}
    return jsonify({
        "success": True,
        "message": "Registration successful. Welcome to SkillForge!",
        "user": data
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
