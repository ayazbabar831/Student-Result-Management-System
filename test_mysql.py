# insert_sensitive_data.py
import mysql.connector

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'dreamteam',
    'database': 'quest_result_system'
}

# Student data from your list (first 30 students)
students_data = [
    # Format: (roll_no, name, father_name, phone, cnic, district)
        ("24SW01", "Sania Batool", "Afshad Ali Abro", "03091153541", "4520449861196", "Khairpur Mirs"),
    ("24SW02", "Shahzaib Khan", "Riaz Hussin", "03053212835", "4520820366283", "Khairpur Mirs"),
    ("24SW03", "Muhammad Safeer", "Khair Muhammad", "03153752574", "4340705070181", "Shahdad Kot"),
    ("24SW04", "Alishba Farooq", "Muhammad Farooq Khan", "03273671168", "4540299753052", "Shaheed Benazirabad"),
    ("24SW05", "Muhammad Bilal", "Munwar Hussain", "03178267353", "4520139742751", "Khairpur Mirs"),
    ("24SW06", "Dildar Ali", "Sijawal Mahar", "03022796694", "4510395747377", "Ghotki"),
    ("24SW07", "Zulfiqar Ali", "Khando alias Noor Hassan", "03009674436", "4510250562003", "Ghotki"),
    ("24SW08", "Qurban Ali Zardari", "Juman Khan", "03075706728", "4530380537863", "Naushehro Feroze"),
    ("24SW10", "Rafia Noor", "Muhammad Ismail Shaikh", "03126322478", "4550241499330", "Sukkur"),
    ("24SW11", "Haziq Khan", "Zahid Khan", "03177887243", "4550503968445", "Sukkur"),
    ("24SW13", "Shahid Satar", "Abdul Sattar Shaikh", "03123461026", "4550128663933", "Sukkur"),
    ("24SW14", "Aqsa Khalid", "Khalid Hussain Samo", "03299673485", "4530407792442", "Naushehro Feroze"),
    ("24SW15", "Shahriyar Ahmed", "Naeem Ahmed", "03193491057", "4530504154977", "Naushehro Feroze"),
    ("24SW16", "Fatima Ahmed", "Irshad Ahmed", "03061535716", "4530453857664", "Naushehro Feroze"),
    ("24SW17", "Muhammad Paryal", "Shah Ali", "03183257236", "4530504186637", "Naushehro Feroze"),
    ("24SW18", "Muhammad Musawar", "Attique Rehman", "03001700551", "4520178218817", "Khairpur Mirs"),
    ("24SW19", "Abdul Nafay Anas", "Abdul Wajid Pirzado", "03288264864", "4550405178051", "Sukkur"),
    ("24SW20", "Awais", "Muhammad Nawaz", "03462693109", "4320534084947", "Larkano"),
    ("24SW22", "Shahzad Hussain", "Attullah", "03003437168", "4340304048681", "Shahdad Kot"),
    ("24SW23", "Tabeer Hussain", "Rafiq Ahmed Samo", "03173652704", "4330463578733", "Shikarpur"),
    ("24SW24", "Mehdi Hassan", "Shamsuddin Baloch", "03079863303", "4330431563367", "Shikarpur"),
    ("24SW25", "Mansoor Ali", "Muhammad Khan", "03123119174", "4170306935229", "Tando Allahyar"),
    ("24SW26", "Romaisa", "Muhammad Toufique", "03313504664", "4180206252306", "Matiari"),
    ("24SW27", "Ali Hyder Balal", "Sher Zaman Balal", "03161085834", "4180206635179", "Matiari"),
    ("24SW30", "Prithvee Raj", "Durga Das", "03009375351", "4130297315727", "Hyderabad"),
    ("24SW32", "Jawad Ali", "Arshad Ali", "03072558258", "4110366449221", "Badin"),
    ("24SW33", "Kalpna", "Dongro Mal", "03120367311", "4420223373962", "Mirpurkhas"),
    ("24SW34", "Mahadev", "Chetan", "03283297001", "4410326258839", "Mirpurkhas"),
    ("24SW36", "Jashan", "Gordhan", "03493174393", "4430389540531", "Tharparkar"),
    ("24SW38", "Ayaz Babar", "Ghulam Fareed", "03303251089", "4420379455701", "Sanghar"),
    ("24SW39", "Kartik Kumar", "Gulab", "03325059074", "4420591913721", "Sanghar"),
    ("24SW41", "Areesha", "Zahid Rasheed", "03194043747", "4540314482248", "Shaheed Benazirabad"),
    ("24SW43", "Salman", "Muhammad Aslam", "03033500606", "4540303906199", "Shaheed Benazirabad"),
    ("24SW44", "Mariam Khalid", "Muhammad Khalid", "03178745234", "4540258796120", "Shaheed Benazirabad"),
    ("24SW45", "Tanveer Hussain", "Nishan Ali", "03198424398", "4520684248007", "Khairpur Mirs"),
    ("24SW46", "Mujahid Hussain", "Fayaz Ali", "03082276248", "4530251909231", "Naushehro Feroze"),
    ("24SW47", "Javeria", "Abdul Rab", "03170294306", "4530322650358", "Shaheed Benazirabad"),
    ("24SW49", "Fiza Batool Gul", "Mazhar Memon", "03183032527", "4180206545924", "Matiari"),
    ("24SW50", "Zafar Ali", "Qurban Ali", "03053928510", "4510415433259", "Ghotki"),
    ("24SW51", "Hamid Ali", "Ghulam Asghar Pirzada", "03163976971", "4520399535451", "Khairpur Mirs"),
    ("24SW52", "Awais Ali", "Qurban Ali", "03240220546", "4350406531513", "Kashmore"),
    ("24SW53", "Junaid", "Ghulam Mustafa", "03002914791", "4540229426983", "Shaheed Benazirabad"),
    ("24SW54", "Abdul Samad", "Muhammad Hashim Abbasi", "03009202441", "4220189045485", "Karachi"),
]

def update_student_data():
    try:
        # Connect to database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        print("✅ Connected to database successfully!")
        print(f"📊 Updating {len(students_data)} students with sensitive information...")
        print("-" * 80)
        
        updated_count = 0
        not_found = []
        
        for roll_no, name, father_name, phone, cnic, district in students_data:
            # First check if student exists
            cursor.execute("SELECT roll_no, name, fname FROM students WHERE roll_no = %s", (roll_no,))
            student = cursor.fetchone()
            
            if student:
                # Update the student with sensitive data
                update_sql = """
                UPDATE students 
                SET phone = %s, cnic = %s, district = %s 
                WHERE roll_no = %s
                """
                cursor.execute(update_sql, (phone, cnic, district, roll_no))
                updated_count += 1
                print(f"✅ {roll_no}: {name} - Updated")
                print(f"   📞 Phone: {phone}")
                print(f"   🆔 CNIC: {cnic}")
                print(f"   📍 District: {district}")
                print()
            else:
                not_found.append(roll_no)
                print(f"❌ {roll_no}: NOT FOUND in database")
        
        conn.commit()
        
        print("-" * 80)
        print(f"✅ UPDATE COMPLETE!")
        print(f"   Successfully updated: {updated_count} students")
        print(f"   Not found in database: {len(not_found)} students")
        
        if not_found:
            print(f"   Missing roll numbers: {', '.join(not_found)}")
        
        # Display updated students
        print("\n📋 UPDATED STUDENTS LIST:")
        print("-" * 80)
        cursor.execute("""
            SELECT roll_no, name, fname, phone, cnic, district 
            FROM students 
            WHERE phone IS NOT NULL 
            ORDER BY roll_no
        """)
        
        updated_students = cursor.fetchall()
        
        for student in updated_students:
            print(f"{student[0]} - {student[1]} | 📞 {student[3]} | 🆔 {student[4]} | 📍 {student[5]}")
        
        cursor.close()
        conn.close()
        
    except mysql.connector.Error as err:
        print(f"❌ Database error: {err}")
    except Exception as e:
        print(f"❌ Error: {e}")

def check_current_data():
    """Check what data is currently in the database"""
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        
        print("\n🔍 CHECKING CURRENT DATABASE STATE:")
        print("-" * 80)
        
        # Check total students
        cursor.execute("SELECT COUNT(*) as total FROM students")
        total = cursor.fetchone()['total']
        print(f"Total students in database: {total}")
        
        # Check students with sensitive data
        cursor.execute("""
            SELECT COUNT(*) as with_data 
            FROM students 
            WHERE phone IS NOT NULL OR cnic IS NOT NULL OR district IS NOT NULL
        """)
        with_data = cursor.fetchone()['with_data']
        print(f"Students with sensitive data: {with_data}")
        
        # Show first 10 students with data
        cursor.execute("""
            SELECT roll_no, name, phone, cnic, district 
            FROM students 
            WHERE phone IS NOT NULL 
            ORDER BY roll_no 
            LIMIT 10
        """)
        
        print("\n📋 First 10 students with sensitive data:")
        print("-" * 80)
        for student in cursor.fetchall():
            print(f"{student['roll_no']} - {student['name']}")
            print(f"   📞 {student['phone']}")
            print(f"   🆔 {student['cnic']}")
            print(f"   📍 {student['district']}")
            print()
        
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("=" * 80)
    print("QUAID-E-AWAM UNIVERSITY - SENSITIVE DATA INSERTION")
    print("=" * 80)
    
    # First check current state
    check_current_data()
    
    print("\n" + "=" * 80)
    print("STARTING DATA UPDATE...")
    print("=" * 80)
    
    # Update the data
    update_student_data()
    
    print("\n" + "=" * 80)
    print("FINAL CHECK:")
    print("=" * 80)
    
    # Check final state
    check_current_data()