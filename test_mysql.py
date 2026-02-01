# check_database.py
import mysql.connector

print("Checking your MySQL database...")
print("="*60)

try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='dreamteam',
        database='quest_result_system'
    )
    
    cursor = conn.cursor(dictionary=True)
    print("✓ Connected to quest_result_system database")
    
    # Show tables
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    print(f"\nTables in database:")
    for table in tables:
        print(f"  - {list(table.values())[0]}")
    
    # Check if students table exists
    cursor.execute("SHOW TABLES LIKE 'students'")
    has_students = cursor.fetchone()
    
    if has_students:
        print("\n✓ 'students' table exists")
        
        # Show table structure
        cursor.execute("DESCRIBE students")
        columns = cursor.fetchall()
        print("\nTable structure:")
        for col in columns:
            print(f"  {col['Field']}: {col['Type']}")
        
        # Count students
        cursor.execute("SELECT COUNT(*) as count FROM students")
        count = cursor.fetchone()
        print(f"\n✓ Total students: {count['count']}")
        
        # Show first 5 students
        cursor.execute("SELECT roll_no, name, gpa FROM students LIMIT 5")
        students = cursor.fetchall()
        print("\nFirst 5 students:")
        for student in students:
            print(f"  {student['roll_no']}: {student['name']} - GPA: {student['gpa']}")
    
    else:
        print("\n✗ 'students' table does NOT exist")
        
    cursor.close()
    conn.close()
    
except mysql.connector.Error as err:
    print(f"\n✗ Error: {err}")
    print("\nPossible issues:")
    print("1. Database doesn't exist")
    print("2. Wrong database name")
    print("3. Wrong password")
    print("4. MySQL not running")

print("\n" + "="*60)