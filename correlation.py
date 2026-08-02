def analyze_risk(total_cost, security_alerts):

    # Calculate cloud cost score
    if total_cost > 300:
        cost_score = 80
    elif total_cost > 200:
        cost_score = 60
    else:
        cost_score = 30


    # Calculate security score
    if security_alerts > 5:
        security_score = 80
    elif security_alerts > 2:
        security_score = 50
    else:
        security_score = 20


    # Overall anomaly score
    anomaly_score = int((cost_score + security_score) / 2)


    # Determine risk level
    if anomaly_score >= 70:

        risk = "HIGH"
        message = "High probability of abnormal cloud and security activity"
        finding = "Significant anomaly detected from cost and security correlation"
        recommendation = "Investigate cloud resources, user activity, and security logs immediately"


    elif anomaly_score >= 40:

        risk = "MEDIUM"
        message = "Unusual activity detected, investigation recommended"
        finding = "Abnormal cloud cost or security activity detected"
        recommendation = "Monitor activities and perform security audit checks"


    else:

        risk = "LOW"
        message = "Cloud activity appears normal"
        finding = "No significant anomaly detected"
        recommendation = "Continue normal monitoring"


    return (
        risk,
        message,
        finding,
        recommendation,
        anomaly_score
    )