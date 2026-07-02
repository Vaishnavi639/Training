from flask import Flask, request, render_template_string
import mysql.connector
import os
import time

app = Flask(__name__)

MYSQL_HOST = os.getenv("MYSQL_SERVER")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")


def get_db_connection():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )


# Wait for MySQL
for i in range(30):
    try:
        conn = get_db_connection()
        conn.close()
        print("Connected to MySQL")
        break
    except Exception as e:
        print("Waiting for MySQL...")
        time.sleep(5)


# Create table if not exists
try:
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255)
    )
    """)

    conn.commit()
    cursor.close()
    conn.close()

except Exception as e:
    print(e)


HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Flask + MySQL</title>
</head>
<body>
    <h2>Add User</h2>

    <form method="POST">
        <input type="text" name="name" placeholder="Enter Name" required>
        <button type="submit">Save</button>
    </form>

    <h3>Stored Users</h3>
    <ul>
        {% for user in users %}
            <li>{{ user[1] }}</li>
        {% endfor %}
    </ul>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():

    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == "POST":
        name = request.form["name"]

        cursor.execute(
            "INSERT INTO users (name) VALUES (%s)",
            (name,)
        )

        conn.commit()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template_string(HTML, users=users)


@app.route("/health")
def health():
    return "Healthy", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)