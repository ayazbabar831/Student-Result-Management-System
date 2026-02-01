# app.py - COMPLETE VERSION WITH ADMIN FEATURES
from flask import Flask, render_template, request, redirect, url_for, flash, session
import mysql.connector
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'quest-university-project-2024-secret-key-admin'

# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'dreamteam',
    'database': 'quest_result_system',
    'auth_plugin': 'mysql_native_password'
}

def get_db_connection():
    """Connect to MySQL database"""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as err:
        print(f"✗ Database Error: {err}")
        flash('Database connection failed. Please try again later.', 'error')
        return None

# ============ ADMIN FUNCTIONS ============
def is_admin_logged_in():
    """Check if admin is logged in - SIMPLE VERSION"""
    return session.get('admin_logged_in') == True

# ============ ROUTES ============

# Homepage
@app.route('/')
def home():
    return render_template('index.html', is_admin=is_admin_logged_in())
# Admin Login
# Admin Login - ULTRA SIMPLE VERSION
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    # If already logged in, redirect to home
    if session.get('admin_logged_in'):
        flash('Already logged in as admin!', 'info')
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()
        
        print(f"🔐 DEBUG: Login attempt - Username: {username}, Password: {password}")
        
        # ULTRA SIMPLE - Hardcoded credentials
        if username == "admin" and password == "quest1234":
            session['admin_logged_in'] = True
            session['admin_username'] = username
            print("✅ DEBUG: Login SUCCESS - Setting session")
            flash('🎉 Admin login successful!', 'success')
            return redirect(url_for('home'))
        else:
            print(f"❌ DEBUG: Login FAILED - Expected: admin/quest1234, Got: {username}/{password}")
            flash('❌ Invalid credentials. Use: admin / quest1234', 'error')
    
    return render_template('admin_login.html')
# Admin Logout
@app.route('/admin/logout')
def admin_logout():
    session.clear()
    flash('Admin logged out successfully', 'success')
    return redirect(url_for('home'))

@app.route('/search', methods=['GET', 'POST'])
def search_results():
    # Handle both GET (from batch page links) and POST (from search form)
    if request.method == 'POST':
        roll_no = request.form.get('roll_no', '').strip().upper()
    else:
        roll_no = request.args.get('roll_no', '').strip().upper()
    
    print(f"🔍 Searching for: {roll_no}")
    print(f"🔐 Admin status: {is_admin_logged_in()}")
    
    if not roll_no:
        flash('Please enter a roll number', 'error')
        return redirect(url_for('home'))
    
    conn = get_db_connection()
    if not conn:
        return redirect(url_for('home'))
    
    cursor = conn.cursor(dictionary=True)
    
    try:
        cursor.execute("SELECT * FROM students WHERE roll_no = %s", (roll_no,))
        student = cursor.fetchone()
        
        if student:
            # Convert decimal to float
            student['gpa'] = float(student['gpa'])
            
            # Handle created_at
            if isinstance(student['created_at'], str):
                try:
                    student['created_at'] = datetime.strptime(student['created_at'], '%Y-%m-%d %H:%M:%S')
                except:
                    student['created_at'] = datetime.now()
            
            cursor.close()
            conn.close()
            
            # Debug print
            print(f"✅ Found student: {student['roll_no']}")
            print(f"📞 Student has phone: {student.get('phone')}")
            print(f"🆔 Student has CNIC: {student.get('cnic')}")
            print(f"📍 Student has district: {student.get('district')}")
            print(f"👑 Admin logged in: {is_admin_logged_in()}")
            
            # PASS is_admin TO THE TEMPLATE
            is_admin = is_admin_logged_in()
            
            return render_template('results.html', 
                                 student=student, 
                                 is_admin=is_admin,
                                 has_sensitive_info=bool(student.get('phone') or student.get('cnic') or student.get('district')))
        else:
            cursor.close()
            conn.close()
            flash(f'Student not found: {roll_no}', 'error')
            return redirect(url_for('home'))
            
    except Exception as e:
        print(f"❌ SEARCH ERROR: {str(e)}")
        cursor.close()
        conn.close()
        flash(f'Error: {str(e)}', 'error')
        return redirect(url_for('home'))
# Batch results
@app.route('/batch/<int:batch_year>')
def batch_results(batch_year):
    conn = get_db_connection()
    if not conn:
        flash('Database connection failed', 'error')
        return redirect(url_for('home'))
    
    cursor = conn.cursor(dictionary=True)
    
    try:
        # Get students
        cursor.execute("SELECT * FROM students WHERE batch_year = %s ORDER BY roll_no", (batch_year,))
        students = cursor.fetchall()
        
        # Get statistics
        cursor.execute("""
            SELECT 
                COUNT(*) as total,
                AVG(gpa) as avg_gpa,
                MAX(gpa) as max_gpa,
                MIN(gpa) as min_gpa
            FROM students WHERE batch_year = %s
        """, (batch_year,))
        
        stats = cursor.fetchone()
        
        # Convert decimal to float
        for student in students:
            student['gpa'] = float(student['gpa'])
        
        stats['avg_gpa'] = float(stats['avg_gpa'])
        stats['max_gpa'] = float(stats['max_gpa'])
        stats['min_gpa'] = float(stats['min_gpa'])
        
        cursor.close()
        conn.close()
        
        return render_template('batch_results.html', 
                             students=students, 
                             stats=stats,
                             batch_year=batch_year,
                             is_admin=is_admin_logged_in())
        
    except Exception as e:
        print(f"❌ BATCH ERROR: {str(e)}")
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        flash(f'Error: {str(e)}', 'error')
        return redirect(url_for('home'))

# Test route
@app.route('/test/db')
def test_db():
    conn = get_db_connection()
    if not conn:
        return "<h1>Database Connection Failed</h1>"
    
    cursor = conn.cursor(dictionary=True)
    
    try:
        cursor.execute("SELECT 'SUCCESS' as status, DATABASE() as db, USER() as user")
        result = cursor.fetchone()
        
        cursor.execute("SELECT COUNT(*) as count FROM students")
        count = cursor.fetchone()
        
        cursor.execute("SELECT roll_no, name, phone, cnic, district FROM students WHERE roll_no IN ('24SW20', '24SW22', '24SW23', '24SW24', '24SW25')")
        students_with_info = cursor.fetchall()
        
        cursor.close()
        conn.close()
        
        html = f"""
        <h1>Database Test</h1>
        <p><b>Status:</b> {result['status']}</p>
        <p><b>Database:</b> {result['db']}</p>
        <p><b>User:</b> {result['user']}</p>
        <p><b>Total Students:</b> {count['count']}</p>
        
        <h2>Students with Sensitive Info:</h2>
        <table border="1" cellpadding="5">
            <tr>
                <th>Roll No</th><th>Name</th><th>Phone</th><th>CNIC</th><th>District</th>
            </tr>
        """
        
        for student in students_with_info:
            html += f"""
            <tr>
                <td>{student['roll_no']}</td>
                <td>{student['name']}</td>
                <td>{student['phone'] or 'N/A'}</td>
                <td>{student['cnic'] or 'N/A'}</td>
                <td>{student['district'] or 'N/A'}</td>
            </tr>
            """
        
        html += """
        </table>
        <p><a href="/">Back to Home</a></p>
        <p><a href="/admin/login">Admin Login</a></p>
        """
        
        return html
        
    except Exception as e:
        return f"<h1>Error: {str(e)}</h1>"

if __name__ == '__main__':
    print("\n" + "="*60)
    print("QUAID-E-AWAM UNIVERSITY RESULT SYSTEM")
    print("="*60)
    print("Starting server...")
    print("Homepage: http://localhost:5000")
    print("Admin Login: http://localhost:5000/admin/login")
    print("Test DB: http://localhost:5000/test/db")
    print("="*60 + "\n")
    
    app.run(debug=True, port=5000)
@app.route('/debug/session')
def debug_session():
    return f"""
    <h1>Session Debug</h1>
    <pre>Session Data: {dict(session)}</pre>
    <p>is_admin_logged_in(): {is_admin_logged_in()}</p>
    <p><a href="/admin/login">Go to Login</a></p>
    <p><a href="/admin/logout">Logout</a></p>
    <p><a href="/">Home</a></p>
    """