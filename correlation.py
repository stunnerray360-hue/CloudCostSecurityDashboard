def analyze_risk(total_cost, security_alerts):

    # Cost anomaly threshold
    if total_cost > 200 and security_alerts > 5:
        risk = "HIGH"
        message = "Possible cloud resource abuse or account compromise"

    elif total_cost > 200 or security_alerts > 5:
        risk = "MEDIUM"
        message = "Unusual activity detected, investigation recommended"

    else:
        risk = "LOW"
        message = "Cloud activity appears normal"

    return risk, message