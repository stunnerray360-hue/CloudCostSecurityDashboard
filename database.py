import sqlite3


connection = sqlite3.connect("database.db")

cursor = connection.cursor()


cursor.execute("""
CREATE TABLE cloud_cost(
    id INTEGER PRIMARY KEY,
    service TEXT,
    cost REAL
)
""")


cursor.execute("""
CREATE TABLE security_events(
    id INTEGER PRIMARY KEY,
    event TEXT,
    severity TEXT
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
INSERT INTO security_events(event, severity)
VALUES
('Failed Login Attempts', 'High'),
('New User Created', 'Medium'),
('Port Scan Detected', 'Low')
""")


connection.commit()
connection.close()

print("Database created successfully")