import sqlite3


connection = sqlite3.connect("database.db")

cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS cloud_cost(
    id INTEGER PRIMARY KEY,
    service TEXT,
    cost REAL
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS security_events(
    id INTEGER PRIMARY KEY,
    event TEXT,
    severity TEXT,
    date TEXT
)
""")


cursor.execute("""
INSERT INTO cloud_cost(service, cost)
VALUES
('EC2', 100),
('S3', 50),
('Database', 80)
""")


cursor.execute("""
INSERT INTO security_events(event, severity, date)
VALUES
('Failed Login Attempts', 'High', '15/07/2026'),
('New User Created', 'Medium', '20/07/2026'),
('Port Scan Detected', 'Low', '25/07/2026')
""")


connection.commit()

connection.close()


print("Database updated successfully")