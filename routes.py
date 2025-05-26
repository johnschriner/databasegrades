from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, login_manager
from models import User, DatabaseEntry
from flask_dance.contrib.google import google


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return redirect(url_for('dashboard'))

@app.route("/login")
def login():
    if not google.authorized:
        print("❌ Not authorized, redirecting to Google...")
        return redirect(url_for("google.login"))

    resp = google.get("/oauth2/v2/userinfo")
    print("✅ Google response:", resp.json())  # 👈 Add this line

    email = resp.json()["email"]
    print("👤 Email returned:", email)

    user = User.query.filter_by(email=email).first()
    if not user:
        user = User(email=email, role='viewer')
        db.session.add(user)
        db.session.commit()

    login_user(user)
    return redirect(url_for("dashboard"))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/submit', methods=['GET', 'POST'])
@login_required
def submit():
    if current_user.role not in ['editor', 'admin']:
        flash("You don't have permission to submit entries.")
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        entry = DatabaseEntry(
            name=request.form['name'],
            url=request.form['url'],
            grade=request.form['grade'],
            tracker_score=float(request.form.get('tracker_score', 0)),
            accessibility_score=float(request.form.get('accessibility_score', 0)),
            open_format_score=float(request.form.get('open_format_score', 0)),
            notes=request.form.get('notes'),
            created_by=current_user.id
        )
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('submit.html')

@app.route('/users', methods=['GET', 'POST'])
@login_required
def manage_users():
    if current_user.role != 'admin':
        return "Unauthorized", 403

    if request.method == 'POST':
        user_id = request.form['user_id']
        new_role = request.form['new_role']
        user = User.query.get(user_id)
        if user:
            user.role = new_role
            db.session.commit()

    users = User.query.order_by(User.email).all()
    return render_template('users.html', users=users)



@app.route('/dashboard')
def dashboard():
    entries = DatabaseEntry.query.all()

    def grade_color(grade):
        colors = {
            'A': 'green', 'B': 'limegreen', 'C': 'gold',
            'D': 'orange', 'F': 'red'
        }
        return colors.get(grade.upper(), 'gray')

    return render_template('dashboard.html', entries=entries, grade_color=grade_color)