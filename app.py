from flask import Flask, render_template
import sqlite3
from correlation import analyze_risk

app = Flask(__name__)


def get_data():

    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    # Total cloud cost
    cursor.execute("SELECT SUM(cost) FROM cloud_cost")
    total_cost = cursor.fetchone()[0]

    if total_cost is None:
        total_cost = 0


    # Security event count
    cursor.execute("SELECT COUNT(*) FROM security_events")
    alerts = cursor.fetchone()[0]


    # Cloud cost chart data
    cursor.execute("SELECT service, cost FROM cloud_cost")
    cost_data = cursor.fetchall()

    services = []
    costs = []

    for item in cost_data:
        services.append(item[0])
        costs.append(item[1])


    # Security events data
    cursor.execute("SELECT event, severity FROM security_events")
    security_data = cursor.fetchall()


    connection.close()


    return (
        total_cost,
        alerts,
        services,
        costs,
        security_data
    )



@app.route("/")
def dashboard():

    (
        total_cost,
        alerts,
        services,
        costs,
        security_data

    ) = get_data()


    risk, message, finding, recommendation, anomaly_score = analyze_risk(
        total_cost,
        alerts
    )


    return render_template(
        "dashboard.html",
        cost=total_cost,
        alerts=alerts,
        risk=risk,
        message=message,
        finding=finding,
        recommendation=recommendation,
        anomaly_score=anomaly_score,
        services=services,
        costs=costs,
        security_data=security_data
    )



if __name__ == "__main__":
    app.run(debug=True)