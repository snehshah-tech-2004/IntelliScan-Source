# db_manager.py
import sqlite3
import os
import datetime

DB_FOLDER = "Scanner_DB"


def get_db_path():
    """Returns path like Scanner_DB/06-2026/06-2026.db"""
    now = datetime.date.today()
    month_str = now.strftime("%m-%Y")  # 06-2026
    folder = os.path.join(DB_FOLDER, month_str)
    os.makedirs(folder, exist_ok=True)
    return os.path.join(folder, f"{month_str}.db")


def init_db():
    """Creates tables if they don't exist. Call once on startup."""
    path = get_db_path()
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS SENSOR_LOG (
            ID          INTEGER PRIMARY KEY AUTOINCREMENT,
            DATE        TEXT NOT NULL,
            TIME        TEXT NOT NULL,
            SLAVE_ID    INTEGER NOT NULL,
            CH01 REAL, CH02 REAL, CH03 REAL, CH04 REAL,
            CH05 REAL, CH06 REAL, CH07 REAL, CH08 REAL,
            CH09 REAL, CH10 REAL, CH11 REAL, CH12 REAL,
            CH13 REAL, CH14 REAL, CH15 REAL, CH16 REAL,
            CH17 REAL, CH18 REAL, CH19 REAL, CH20 REAL,
            CH21 REAL, CH22 REAL, CH23 REAL, CH24 REAL
        )
    """)
    c.execute("""
            CREATE TABLE IF NOT EXISTS EVENT_LOG (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                DATE TEXT NOT NULL,
                TIME TEXT NOT NULL,
                USERNAME TEXT,
                EVENT_TYPE TEXT,
                DESCRIPTION TEXT
            )
        """)
    c.execute("""
        CREATE INDEX IF NOT EXISTS IDX_DATE_SLAVE
        ON SENSOR_LOG (DATE, SLAVE_ID)
    """)
    conn.commit()
    conn.close()
    print(f"[DB] Initialized: {path}")


def write_row(slave_id, date, time_str, values):
    """
    values = list of 24 floats/None (scaled channel values)
    """
    path = get_db_path()
    cols = [f"CH{i:02d}" for i in range(1, 25)]
    placeholders = ",".join(["?"] * (3 + 24))
    sql = f"""
        INSERT INTO SENSOR_LOG (DATE, TIME, SLAVE_ID, {",".join(cols)})
        VALUES ({placeholders})
    """
    row_data = [date, time_str, slave_id] + [
        (v if v is not None and v != "" else None) for v in values
    ]
    try:
        conn = sqlite3.connect(path)
        conn.execute(sql, row_data)
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"[DB] Write error slave {slave_id}: {e}")


def query_slave_day(slave_id, date_str):
    """date_str format: '01-06-2026'"""
    path = get_db_path()
    if not os.path.exists(path):
        return []
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute(
        """
        SELECT DATE, TIME,
               CH01, CH02, CH03, CH04, CH05, CH06,
               CH07, CH08, CH09, CH10, CH11, CH12,
               CH13, CH14, CH15, CH16, CH17, CH18,
               CH19, CH20, CH21, CH22, CH23, CH24
        FROM SENSOR_LOG
        WHERE SLAVE_ID = ? AND DATE = ?
        ORDER BY TIME ASC
    """,
        (slave_id, date_str),
    )
    rows = c.fetchall()
    conn.close()
    return rows


def query_slave_range(slave_id, date_from, date_to):
    """date_from, date_to: 'DD-MM-YYYY'"""
    path = get_db_path()
    if not os.path.exists(path):
        return []
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute(
        """
        SELECT DATE, TIME,
               CH01, CH02, CH03, CH04, CH05, CH06,
               CH07, CH08, CH09, CH10, CH11, CH12,
               CH13, CH14, CH15, CH16, CH17, CH18,
               CH19, CH20, CH21, CH22, CH23, CH24
        FROM SENSOR_LOG
        WHERE SLAVE_ID = ? AND DATE BETWEEN ? AND ?
        ORDER BY DATE ASC, TIME ASC
    """,
        (slave_id, date_from, date_to),
    )
    rows = c.fetchall()
    conn.close()
    return rows


def write_event(username, event_type, description):

    path = get_db_path()

    now = datetime.datetime.now()

    date_str = now.strftime("%d-%m-%Y")
    time_str = now.strftime("%H:%M:%S")

    try:
        conn = sqlite3.connect(path)

        conn.execute(
            """
            INSERT INTO EVENT_LOG
            (
                DATE,
                TIME,
                USERNAME,
                EVENT_TYPE,
                DESCRIPTION
            )
            VALUES (?, ?, ?, ?, ?)
        """,
            (date_str, time_str, username, event_type, description),
        )

        conn.commit()
        conn.close()

    except Exception as e:
        print(f"[EVENT LOG ERROR] {e}")


"""
By Slave ID only
-- All data ever recorded for Slave 2
SELECT * FROM SENSOR_LOG WHERE SLAVE_ID = 2 ORDER BY DATE ASC, TIME ASC;

By Date Range only
-- All slaves, between two dates
SELECT * FROM SENSOR_LOG 
WHERE DATE BETWEEN '01-06-2026' AND '15-06-2026'
ORDER BY DATE ASC, TIME ASC;

By Slave ID + Date Range
-- Slave 1, between two dates
SELECT * FROM SENSOR_LOG 
WHERE SLAVE_ID = 1
AND DATE BETWEEN '01-06-2026' AND '15-06-2026'
ORDER BY DATE ASC, TIME ASC;

By Slave ID + Time Range (same day)
-- Slave 1, on one specific day, between 09:00 and 17:00
SELECT * FROM SENSOR_LOG 
WHERE SLAVE_ID = 1
AND DATE = '01-06-2026'
AND TIME BETWEEN '09:00:00' AND '17:00:00'
ORDER BY TIME ASC;

By Slave ID + Date Range + Time Range (most useful for reports)
-- Slave 1, across multiple days, only between shift hours
SELECT * FROM SENSOR_LOG 
WHERE SLAVE_ID = 1
AND DATE BETWEEN '01-06-2026' AND '10-06-2026'
AND TIME BETWEEN '08:00:00' AND '18:00:00'
ORDER BY DATE ASC, TIME ASC;

Summary / Count queries
-- How many rows per slave per day
SELECT SLAVE_ID, DATE, COUNT(*) AS TOTAL_READINGS
FROM SENSOR_LOG
GROUP BY SLAVE_ID, DATE
ORDER BY DATE ASC, SLAVE_ID ASC;

-- Min, Max, Average of CH01 per slave per day
SELECT SLAVE_ID, DATE,
       MIN(CH01) AS MIN_CH01,
       MAX(CH01) AS MAX_CH01,
       ROUND(AVG(CH01), 2) AS AVG_CH01
FROM SENSOR_LOG
WHERE CH01 IS NOT NULL
GROUP BY SLAVE_ID, DATE
ORDER BY DATE ASC, SLAVE_ID ASC;

-- View All Events
SELECT *
FROM EVENT_LOG;

-- Latest Events First
SELECT *
FROM EVENT_LOG
ORDER BY ID DESC;

-- Last 20 Events
SELECT *
FROM EVENT_LOG
ORDER BY ID DESC
LIMIT 20;

-- All Login Events
SELECT *
FROM EVENT_LOG
WHERE EVENT_TYPE = 'LOGIN';

-- Failed Login Attempts
SELECT *
FROM EVENT_LOG
WHERE EVENT_TYPE = 'LOGIN_FAILED';

-- All Start Events
SELECT *
FROM EVENT_LOG
WHERE EVENT_TYPE = 'START';

-- All Stop Events
SELECT *
FROM EVENT_LOG
WHERE EVENT_TYPE = 'STOP';

-- All PDF Reports Generated
SELECT *
FROM EVENT_LOG
WHERE EVENT_TYPE = 'PDF';

-- All Configuration Changes
SELECT *
FROM EVENT_LOG
WHERE EVENT_TYPE = 'SETTINGS';

-- Events For Specific User
SELECT *
FROM EVENT_LOG
WHERE USERNAME = 'admin';

-- Events On Specific Date
SELECT *
FROM EVENT_LOG
WHERE DATE = '13-06-2026';

-- Events Between Dates
SELECT *
FROM EVENT_LOG
WHERE DATE >= '01-06-2026'
AND DATE <= '13-06-2026';

-- Count Total Logins
SELECT COUNT(*)
FROM EVENT_LOG
WHERE EVENT_TYPE='LOGIN';

-- Count Failed Logins
SELECT COUNT(*)
FROM EVENT_LOG
WHERE EVENT_TYPE='LOGIN_FAILED';

-- Count Reports Generated
SELECT COUNT(*)
FROM EVENT_LOG
WHERE EVENT_TYPE='PDF';

-- Most Active User
SELECT
    USERNAME,
    COUNT(*) AS TOTAL_EVENTS
FROM EVENT_LOG
GROUP BY USERNAME
ORDER BY TOTAL_EVENTS DESC;

-- Event Summary Dashboard Query
SELECT
    EVENT_TYPE,
    COUNT(*) AS COUNT
FROM EVENT_LOG
GROUP BY EVENT_TYPE;

-- Last System Start
SELECT *
FROM EVENT_LOG
WHERE EVENT_TYPE='START'
ORDER BY ID DESC
LIMIT 1;

-- Last PDF Generated
SELECT *
FROM EVENT_LOG
WHERE EVENT_TYPE='PDF'
ORDER BY ID DESC
LIMIT 1;

-- Everything That Happened Today
SELECT *
FROM EVENT_LOG
WHERE DATE = strftime('%d-%m-%Y','now','localtime');
"""
