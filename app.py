from flask import Flask, jsonify, render_template
import mysql.connector

app = Flask(__name__)

def get_database_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='studentlist'
    )
    return connection

@app.route('/data', methods=['GET'])
def get_data():
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM student_info')
    rows = cursor.fetchall()
    data = []
    for row in rows:
        data.append({'id': row[0], 'name': row[1], 'dept': row[2], 'course': row[3]})
    connection.close()
    return render_template('list.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)


