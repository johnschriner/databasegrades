from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, login_manager
from models import User, DatabaseEntry
<<<<<<< HEAD
from flask import Markup
=======
>>>>>>> 6d1f5582c6f68a1fd0acf1d3102045c88a3a33e6

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    entries = DatabaseEntry.query.all()
    return render_template('index.html', entries=entries)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Placeholder login (replace with Google OAuth later)
    if request.method == 'POST':
        email = request.form['email']
        user = User.query.filter_by(email=email).first()
        if user:
            login_user(user)
            return redirect(url_for('index'))
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
        return redirect(url_for('index'))
    return render_template('submit.html')
<<<<<<< HEAD

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


=======
>>>>>>> 6d1f5582c6f68a1fd0acf1d3102045c88a3a33e6
