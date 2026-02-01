# seed_data_corrected.py
import mysql.connector
import random

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'dreamteam',  # Add your MySQL password here
    'database': 'quest_result_system'
}

def generate_random_gpa():
    """Generate random GPA between 2.0 and 4.0"""
    return round(random.uniform(2.5, 4.0), 2)

# 2022 Batch = 5th Semester (51 students)
students_22 = [
    ("22SW01", "Mr. Muhammad Umair", "Jawaid Hassan", 2022, "5th"),
    ("22SW02", "Ms. Razia", "Muhammad Tahir", 2022, "5th"),
    ("22SW03", "Mr. Ashique Hussain", "Abdul Ghani", 2022, "5th"),
    ("22SW04", "Mr. Abdul Qavi", "Muhammad Usman", 2022, "5th"),
    ("22SW05", "Mr. Sajjad Hussain", "Muhammad Saleh", 2022, "5th"),
    ("22SW06", "Mr. Abdul Rehman Sudais", "Saleemullah", 2022, "5th"),
    ("22SW07", "Ms. Muqadas Hussain", "Khalid Hussain", 2022, "5th"),
    ("22SW10", "Mr. Meekaeel Jameel", "Ghulam Sarwar", 2022, "5th"),  # Note: Missing 22SW08, 22SW09
    ("22SW11", "Mr. Osama", "Nizam U Din", 2022, "5th"),
    ("22SW12", "Mr. Ahsan Abbas", "Ghulam Asghar", 2022, "5th"),
    ("22SW13", "Mr. Abdul Khalique", "Gull Sher", 2022, "5th"),
    ("22SW14", "Mr. Bharat Kumar", "Jeevan Ram", 2022, "5th"),
    ("22SW15", "Mr. Tafheem Ahmed", "Naseem Ahmed", 2022, "5th"),
    ("22SW17", "Mr. Abdul Majid", "Abdul Ghaffar", 2022, "5th"),  # Note: Missing 22SW16
    ("22SW18", "Mr. Faraz Ul Zamman", "Zulfiqar Ali", 2022, "5th"),
    ("22SW20", "Mr. Syed Mushtaque Hussain", "Syed Hizbullah Shah", 2022, "5th"),  # Missing 22SW19
    ("22SW21", "Mr. Majid Hussain", "Imam Ali", 2022, "5th"),
    ("22SW22", "Mr. Imran Hussain", "Ali Khan", 2022, "5th"),
    ("22SW24", "Mr. Hitesh Kumar", "Jani", 2022, "5th"),  # Missing 22SW23
    ("22SW25", "Mr. Javed Ali", "Muhammad Soomar", 2022, "5th"),
    ("22SW26", "Mr. Syed Saifullah Shah", "Salamullah Shah", 2022, "5th"),
    ("22SW27", "Mr. Amanullah", "Ali Ashgar", 2022, "5th"),
    ("22SW29", "Mr. Bashir Ahmed", "Ahmed Khan", 2022, "5th"),  # Missing 22SW28
    ("22SW30", "Mr. Muhammad Muzamil", "Imadad Ali", 2022, "5th"),
    ("22SW31", "Mr. Noman", "Muhammad Shareef", 2022, "5th"),
    ("22SW32", "Mr. Kaliash Kumar", "Lal Chand", 2022, "5th"),
    ("22SW33", "Mr. Muhammad Ahmed Raza", "Muhammad Shakeel", 2022, "5th"),
    ("22SW34", "Ms. Manahil Khan", "Muhammad Aamir", 2022, "5th"),
    ("22SW35", "Mr. Taqi Ur Rehman", "Muhammad Badar Us Sallam", 2022, "5th"),
    ("22SW36", "Ms. Misbah", "Muhammad Azeem", 2022, "5th"),
    ("22SW37", "Mr. Nazam Uddin", "Shah Bux", 2022, "5th"),
    ("22SW38", "Mr. Muhammad Muzzamil", "Allah Dad", 2022, "5th"),
    ("22SW39", "Ms. Mariyam Majeed", "Abdul Majeed Hashmani", 2022, "5th"),
    ("22SW40", "Mr. Yasir Nazeer Bharo", "Nazeer Ahmed Bharo", 2022, "5th"),
    ("22SW41", "Mr. Abdul Ahad", "Ghulam Mustafa", 2022, "5th"),
    ("22SW43", "Mr. Ali Yawar", "Khalid Hussain", 2022, "5th"),  # Missing 22SW42
    ("22SW44", "Mr. Hasnain Anwer", "Ali Anwar", 2022, "5th"),
    ("22SW46", "Ms. Mary Florence", "Anwar Masih", 2022, "5th"),  # Missing 22SW45
    ("22SW47", "Ms. Unzila", "Hamid Ahmed", 2022, "5th"),
    ("22SW48", "Ms. Kashaf Ud Duja", "Abdul Wahab", 2022, "5th"),
    ("22SW49", "Mr. Yasir Arfat", "Javed Ahmed", 2022, "5th"),
    ("22SW50", "Mr. Muhammad Shaheryar Khan", "Muhammad Khan", 2022, "5th"),
    ("22SW51", "Mr. Anees Ul Rehman", "Badaruddin", 2022, "5th"),
    ("22SW52", "Mr. Hassan Raza", "Muhammad Ismail", 2022, "5th"),
    ("22SW53", "Mr. Chandan Lal", "Lal Chand", 2022, "5th"),
    ("22SW54", "Mr. Sheeraz Khan", "Zulfiqar Ali", 2022, "5th"),
    ("22SW55", "Mr. Abrar Ali", "Aijaz Ali", 2022, "5th"),
    ("22SW56", "Mr. Musaib Ur Rehman", "Khalil Ur Rehman", 2022, "5th"),
    ("22SW57", "Mr. Sarop", "Lal Chand", 2022, "5th"),
    ("22SW58", "Mr. Mohammad Hamza Hussain", "Haji Hamid Hussain", 2022, "5th"),
    ("22SW59", "Mr. Faraz Ali", "Moaj Ali", 2022, "5th"),
    # Note: Missing 22SW60 onward (if any)
]

# 2023 Batch = 3rd Semester (47 students)
students_23 = [
    ("23SW01", "Basit Baig", "Mujamil Baig", 2023, "3rd"),
    ("23SW02", "Shahzaman", "Gul Sher", 2023, "3rd"),
    ("23SW03", "Fateh Mohammad", "Mukhtiar Ali", 2023, "3rd"),
    ("23SW04", "Muhammad Soomer", "Aijaz Ali", 2023, "3rd"),
    ("23SW05", "Farhan Ali", "Amjad Ali", 2023, "3rd"),
    # Missing: 23SW06, 23SW07, 23SW08
    ("23SW09", "Muhammad Shaheer", "Nadeem Ismail", 2023, "3rd"),
    # Missing: 23SW10, 23SW11, 23SW12
    ("23SW13", "Abdul Samad", "Abdul Raheem", 2023, "3rd"),
    # Missing: 23SW14
    ("23SW15", "Ihsan Ali", "Khair Muhammad", 2023, "3rd"),
    ("23SW16", "M. Anas Alias Wali Muhammad", "Aijaz Ali Abbasi", 2023, "3rd"),
    ("23SW17", "Abdul Samad Watio", "Yaseen Ali", 2023, "3rd"),
    ("23SW18", "Rumaisa Abbas", "Ghulam Abbas", 2023, "3rd"),
    ("23SW19", "Zahid Ali", "Muhammad Uris", 2023, "3rd"),
    # Missing: 23SW20
    ("23SW21", "Muhammad Faheem", "Muhammad Tahir", 2023, "3rd"),
    ("23SW22", "Sheeraz Ali Channa", "Irshad Ali", 2023, "3rd"),
    # Missing: 23SW23
    ("23SW24", "Nasir Ali", "Shahid Ahmed", 2023, "3rd"),
    ("23SW25", "Muhammad Saqib Kandhir", "M Dawood Kandhir", 2023, "3rd"),
    ("23SW26", "Bisma Shaikh", "Abdul Rouf", 2023, "3rd"),
    ("23SW27", "Shoaib Ali Shaikh", "Abdul Rouf", 2023, "3rd"),
    ("23SW28", "Najaf Ali", "Ali Murad", 2023, "3rd"),
    ("23SW29", "Ghulam Qadir", "Khalid Hussain", 2023, "3rd"),
    ("23SW30", "Muhammad Zaid", "Abdul Hafeez", 2023, "3rd"),
    ("23SW31", "Hassnain Ali", "Sajjad Ahmed", 2023, "3rd"),
    ("23SW32", "Usman Ghani Noonari", "Gulam Shabir", 2023, "3rd"),
    ("23SW33", "Rohit Kumar Aahuja", "Haresh Kumar", 2023, "3rd"),
    ("23SW34", "Abdul Samad", "Iqbal Ahmed", 2023, "3rd"),
    ("23SW35", "M. Khalil Ur Rehman", "Muhammad Latif", 2023, "3rd"),
    ("23SW36", "Raheel", "Riaz Ahmed", 2023, "3rd"),
    ("23SW37", "Muhammad Oan", "Iftikhar Ahmed", 2023, "3rd"),
    ("23SW38", "Atif Noonari", "Abdul Gaffar", 2023, "3rd"),
    # Missing: 23SW39
    ("23SW40", "Tazaeen Zahra", "Yar Muhammad", 2023, "3rd"),
    ("23SW41", "Saqib Ali Alias Hassnain", "Mubarak Nizamani", 2023, "3rd"),
    ("23SW42", "Mushahid Hussain", "Ghulam Hussain", 2023, "3rd"),
    # Missing: 23SW43, 23SW44
    ("23SW45", "Muhammad Qasim", "Rao M Aslam", 2023, "3rd"),
    # Missing: 23SW46
    ("23SW47", "Aeiraf Fatima", "Muhammad Akhtar", 2023, "3rd"),
    # Missing: 23SW48
    ("23SW49", "Syed Ahmed Ali", "Syed Danish Ali", 2023, "3rd"),
    ("23SW50", "Kumail Ali", "Wajid Ali Soomro", 2023, "3rd"),
    ("23SW51", "Kumail Abbas", "Asif Ali", 2023, "3rd"),
    ("23SW52", "Qamar Nisa", "Muhammad Ali", 2023, "3rd"),
    ("23SW53", "Memoona Chandio", "Abdul Fattah", 2023, "3rd"),
    ("23SW54", "Ume Rubab Memon", "Abdul Jabbar", 2023, "3rd"),
    ("23SW55", "Azam Memon", "Amjad Ali", 2023, "3rd"),
    ("23SW56", "Sadiq Ali", "Mohammad Iqbal", 2023, "3rd"),
    ("23SW57", "Haq Nawaz", "Alam Gir", 2023, "3rd"),
    ("23SW58", "Hamna", "Asghar Ali", 2023, "3rd"),
    ("23SW59", "Kinza", "Abdul Ghaffar", 2023, "3rd"),
    ("23SW60", "Muntazir Ali", "Ali Gohar", 2023, "3rd"),
    ("23SW61", "Sara", "Fazal Rehman", 2023, "3rd"),
]

# 2024 Batch = 1st Semester (48 students)
students_24 = [
    ("24SW01", "Ms. Sania Batool", "Afshad Ali Abro", 2024, "1st"),
    ("24SW02", "Mr. Shahzaib Khan", "Riaz Hussain", 2024, "1st"),
    ("24SW03", "Mr. Muhammad Safeer", "Khair Muhammad", 2024, "1st"),
    ("24SW04", "Ms. Alishba Farooq", "Muhammad Faeooq", 2024, "1st"),
    ("24SW05", "Mr. Muhammad Bilal", "Munawar Hussain", 2024, "1st"),
    ("24SW06", "Mr. Dildar Ali", "Sijawal Mahar", 2024, "1st"),
    ("24SW07", "Mr. Zulfiqar Ali", "Khando alias Noor Hassan", 2024, "1st"),
    ("24SW08", "Mr. Qurban Ali", "Juman Khan", 2024, "1st"),
    ("24SW09", "Ms. Ayesha Sanam", "Muhammad Ramzan", 2024, "1st"),
    ("24SW10", "Ms. Rafia Noor", "Muhammad Ismail", 2024, "1st"),
    ("24SW11", "Mr. Haziq Khan", "Zahid Khan", 2024, "1st"),
    ("24SW12", "Mr. Ansarullah", "Lutfullah Bhutto", 2024, "1st"),
    ("24SW13", "Mr. Shahid Sattar", "Abdul Sattar Shaikh", 2024, "1st"),
    ("24SW14", "Ms. Aqsa Khalid", "Khalid Hussain Samo", 2024, "1st"),
    ("24SW15", "Mr. Shahyiyar Ahmed", "Naeem Ahmed", 2024, "1st"),
    ("24SW16", "Ms. Fatima Ahmed", "Irshad Ahmed", 2024, "1st"),
    ("24SW17", "Mr. Muhammad Paryal", "Shah Ali", 2024, "1st"),
    ("24SW18", "Mr. Muhammad Musawar", "Attique Rehman", 2024, "1st"),
    ("24SW19", "Mr. Abdul Nafay Anas", "Abdul Wajid", 2024, "1st"),
    ("24SW20", "Mr. Awais", "Muhammad Nawaz", 2024, "1st"),
    ("24SW21", "Mr. Abubakar", "Muhammad Ismail", 2024, "1st"),
    ("24SW22", "Mr. Shahzad Hussain", "Attaullah", 2024, "1st"),
    ("24SW23", "Mr. Tabeer Hussain Samo", "Rafique Ahmed", 2024, "1st"),
    ("24SW24", "Mr. Mehdi Hassan", "Shamsuddin Baloch", 2024, "1st"),
    ("24SW25", "Mr. Mansoor Ali", "Muhammad Khan", 2024, "1st"),
    ("24SW26", "Ms. Romaisa", "Muhammad Toufique", 2024, "1st"),
    ("24SW27", "Mr. Ali Hyder", "Sherzaman", 2024, "1st"),
    # Missing: 24SW28, 24SW29
    ("24SW30", "Mr. Prithvee Raj", "Durga Das", 2024, "1st"),
    ("24SW31", "Mr. Furqan", "Shamsuddin", 2024, "1st"),
    ("24SW32", "Mr. Jawad Ali", "Arshad Ali", 2024, "1st"),
    ("24SW33", "Ms. Kalpna", "Dongro Mal", 2024, "1st"),
    ("24SW34", "Mr. Mahadev", "Chetan", 2024, "1st"),
    # Missing: 24SW35
    ("24SW36", "Mr. Jashan", "Gordhan", 2024, "1st"),
    # Missing: 24SW37
    ("24SW38", "Mr. Ayaz Babar", "Ghulam Fareed", 2024, "1st"),
    ("24SW39", "Mr. Kartik Kumar", "Gulab", 2024, "1st"),
    # Missing: 24SW40
    ("24SW41", "Ms. Areesha Zahid", "Zahid Rasheed", 2024, "1st"),
    # Missing: 24SW42
    ("24SW43", "Mr. Salman", "Muhammad Aslam", 2024, "1st"),
    ("24SW44", "Ms. Mariam Khalid", "Muhammad Khalid", 2024, "1st"),
    ("24SW45", "Mr. Tanveer Hussain", "Nishan Ali Arain", 2024, "1st"),
    ("24SW46", "Mr. Mujahid Hussain", "Fyaz Ali", 2024, "1st"),
    ("24SW47", "Ms. Javeria", "Abdul Rab", 2024, "1st"),
    # Missing: 24SW48
    ("24SW49", "Ms. Fiza Batool Gul", "Mazhar Memon", 2024, "1st"),
    ("24SW50", "Mr. Zafar Ali", "Qurban Ali", 2024, "1st"),
    ("24SW51", "Mr. Hamid Ali", "Ghulam Asghar Pirzado", 2024, "1st"),
    ("24SW52", "Mr. Awais Ali", "Qurban Ali", 2024, "1st"),
    ("24SW53", "Mr. Junaid", "Ghulam Mustafa", 2024, "1st"),
    ("24SW54", "Mr. Abdul Samad", "Muhammad Hashim Abbasi", 2024, "1st"),
    ("24SW55", "Mr. Mansoor Rehman", "Mir Nawaz", 2024, "1st"),
]

def seed_database():
    try:
        # Connect to database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        print("Connected to database successfully!")
        print(f"Total students to insert: {len(students_22) + len(students_23) + len(students_24)}")
        print("Batch distribution:")
        print(f"  - 2022 Batch (5th Semester): {len(students_22)} students")
        print(f"  - 2023 Batch (3rd Semester): {len(students_23)} students")
        print(f"  - 2024 Batch (1st Semester): {len(students_24)} students")
        
        # Clear existing data
        cursor.execute("DELETE FROM students")
        print("\nCleared existing student data...")
        
        # Combine all students
        all_students = students_22 + students_23 + students_24
        inserted_count = 0
        skipped_count = 0
        
        for roll_no, name, fname, batch_year, semester in all_students:
            gpa = generate_random_gpa()
            
            sql = """
            INSERT INTO students (roll_no, name, fname, gpa, batch_year, semester)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            
            values = (roll_no, name, fname, gpa, batch_year, semester)
            
            try:
                cursor.execute(sql, values)
                inserted_count += 1
            except mysql.connector.Error as err:
                print(f"Error inserting {roll_no}: {err}")
                skipped_count += 1
        
        conn.commit()
        
        print(f"\n{'='*60}")
        print("DATABASE SEEDING COMPLETE!")
        print(f"{'='*60}")
        print(f"Successfully inserted: {inserted_count} students")
        if skipped_count > 0:
            print(f"Skipped due to errors: {skipped_count} students")
        
        # Display sample data from each batch
        print(f"\n{'='*60}")
        print("SAMPLE DATA FROM EACH BATCH:")
        print(f"{'='*60}")
        
        batches = [2022, 2023, 2024]
        for batch in batches:
            cursor.execute("SELECT roll_no, name, fname, gpa, semester FROM students WHERE batch_year = %s LIMIT 2", (batch,))
            students = cursor.fetchall()
            
            print(f"\n{batch} Batch ({students[0][4]} Semester):")
            for student in students:
                print(f"  {student[0]} - {student[1]} | Father: {student[2]} | GPA: {student[3]}")
        
        # Display statistics
        cursor.execute("SELECT batch_year, COUNT(*), AVG(gpa) FROM students GROUP BY batch_year")
        stats = cursor.fetchall()
        
        print(f"\n{'='*60}")
        print("BATCH STATISTICS:")
        print(f"{'='*60}")
        for batch, count, avg_gpa in stats:
            print(f"Batch {batch}: {count} students | Average GPA: {avg_gpa:.2f}")
        
        cursor.close()
        conn.close()
        
    except mysql.connector.Error as err:
        print(f"Database error: {err}")

if __name__ == "__main__":
    seed_database()