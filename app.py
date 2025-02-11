from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

db_config = {
    "host": "10.0.2.7",
    "user": "root",
    "password": "password",
    "database": "student_db"
}

def get_student_details(roll_number):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students WHERE roll_number = %s", (roll_number,))
        student = cursor.fetchone()
        conn.close()
        return student
    except Exception as e:
        return {"error": str(e)}

@app.route('/student', methods=['GET'])
def fetch_student():
    roll_number = request.args.get('roll_number')
    if not roll_number:
        return jsonify({"error": "Roll number is required"}), 400
    student = get_student_details(roll_number)
    if student:
        return jsonify(student)
    else:
        return jsonify({"message": "Student not found"}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
