# app.py - FIXED VERSION
from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'quest-university-project-2024'

def get_db_connection():
    """Connect to MySQL database"""
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='dreamteam',
            database='quest_result_system',
            auth_plugin='mysql_native_password'
        )
        return conn
    except mysql.connector.Error as err:
        print(f"✗ Database Error: {err}")
        flash(f'Database connection failed: {err}', 'error')
        return None
    except Exception as e:
        print(f"✗ General Error: {e}")
        flash('Database connection failed', 'error')
        return None

# Homepage
@app.route('/')
def home():
    return render_template('index.html')

# Search results - SIMPLIFIED WORKING VERSION
@app.route('/search', methods=['POST'])
def search_results():
    roll_no = request.form.get('roll_no', '').strip().upper()
    
    print(f"🔍 Searching for: {roll_no}")  # Debug
    
    if not roll_no:
        flash('Please enter a roll number', 'error')
        return redirect(url_for('home'))
    
    conn = get_db_connection()
    if not conn:
        return redirect(url_for('home'))
    
    cursor = conn.cursor(dictionary=True)
    
    try:
        print(f"📊 Executing query...")  # Debug
        cursor.execute("SELECT * FROM students WHERE roll_no = %s", (roll_no,))
        student = cursor.fetchone()
        print(f"📊 Query result: {student}")  # Debug
        
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
            
            print(f"✅ Found student: {student['name']}")  # Debug
            return render_template('results.html', student=student)
        else:
            cursor.close()
            conn.close()
            print(f"❌ Student not found: {roll_no}")  # Debug
            flash(f'Student not found: {roll_no}', 'error')
            return redirect(url_for('home'))
            
    except Exception as e:
        print(f"❌ SEARCH ERROR: {str(e)}")  # Debug
        cursor.close()
        conn.close()
        flash(f'Error: {str(e)}', 'error')
        return redirect(url_for('home'))

# Batch results - SIMPLIFIED
@app.route('/batch/<int:batch_year>')
def batch_results(batch_year):
    print(f"📊 Loading batch: {batch_year}")  # Debug
    
    conn = get_db_connection()
    if not conn:
        flash('Database connection failed', 'error')
        return redirect(url_for('home'))
    
    cursor = conn.cursor(dictionary=True)
    
    try:
        # Get students
        cursor.execute("SELECT * FROM students WHERE batch_year = %s ORDER BY roll_no", (batch_year,))
        students = cursor.fetchall()
        print(f"📊 Found {len(students)} students")  # Debug
        
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
        print(f"📊 Stats: {stats}")  # Debug
        
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
                             batch_year=batch_year)
        
    except Exception as e:
        print(f"❌ BATCH ERROR: {str(e)}")  # Debug
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        flash(f'Error: {str(e)}', 'error')
        return redirect(url_for('home'))

# Test route to check database
@app.route('/test/db')
def test_db():
    conn = get_db_connection()
    if not conn:
        return "<h1>Database Connection Failed</h1>"
    
    cursor = conn.cursor(dictionary=True)
    
    try:
        # Test query
        cursor.execute("SELECT 'SUCCESS' as status, DATABASE() as db, USER() as user")
        result = cursor.fetchone()
        
        # Count students
        cursor.execute("SELECT COUNT(*) as count FROM students")
        count = cursor.fetchone()
        
        # Try a specific student
        cursor.execute("SELECT * FROM students WHERE roll_no = '22SW01'")
        student = cursor.fetchone()
        
        cursor.close()
        conn.close()
        
        return f"""
        <h1>Database Test</h1>
        <p><b>Status:</b> {result['status']}</p>
        <p><b>Database:</b> {result['db']}</p>
        <p><b>User:</b> {result['user']}</p>
        <p><b>Total Students:</b> {count['count']}</p>
        <p><b>Test Student (22SW01):</b> {student['name'] if student else 'Not found'}</p>
        <p><a href="/">Back to Home</a></p>
        """
        
    except Exception as e:
        return f"<h1>Error: {str(e)}</h1>"

if __name__ == '__main__':
    print("\n" + "="*60)
    print("QUAID-E-AWAM UNIVERSITY RESULT SYSTEM")
    print("="*60)
    print("Starting server...")
    print("Homepage: http://localhost:5000")
    print("Test DB: http://localhost:5000/test/db")
    print("="*60 + "\n")
    
    app.run(debug=True, port=5000)