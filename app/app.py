from flask import Flask
import mysql.connector
import os

app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(
        host=os.environ["DB_HOST"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        database=os.environ["DB_NAME"],
        port=3306
    )


@app.route("/")
def home():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT id, name, email FROM users")
    users = cursor.fetchall()

    cursor.close()
    connection.close()

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>AWS 3-Tier Application</title>
    </head>
    <body>
        <h1>AWS 3-Tier Application</h1>
        <h2>Application Server</h2>
        <h3>Users from RDS MySQL</h3>
        <ul>
    """

    for user in users:
        html += f"<li>{user['id']} - {user['name']} - {user['email']}</li>"

    html += """
        </ul>
    </body>
    </html>
    """

    return html


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)