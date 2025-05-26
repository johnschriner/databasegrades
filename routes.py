from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, login_manager
from models import User, DatabaseEntry

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return redirect(url_for('dashboard'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        user = User.query.filter_by(email=email).first()
        if user:
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('User not found.')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/submit', methods=['GET', 'POST'])
@login_required
def submit():
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