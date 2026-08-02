from flask import Flask, render_template
import sqlite3
from correlation import analyze_risk

app = Flask(__name__)


def get_data():

    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("SELECT SUM(cost) FROM cloud_cost")
    total_cost = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM security_events")
    alerts = cursor.fetchone()[0]

    connection.close()

    return total_cost, alerts


@app.route("/")
def dashboard():

    total_cost, alerts = get_data()

    risk, message = analyze_risk(total_cost, alerts)

    return render_template(
        "dashboard.html",
        cost=total_cost,
        alerts=alerts,
        risk=risk,
        message=message
    )


if __name__ == "__main__":
    app.run(debug=True)