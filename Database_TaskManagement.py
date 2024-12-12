import mysql.connector


def connect():
    return mysql.connector.connect(
        host="localhost",         
        user="root",              
        password="",               
        database="task2"      
    )

# Note: Create database on XAMPP phpmyadmin first
def taskData():
    con = connect()
    cur = con.cursor()

    con.database = "task2"

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Tasks (
            task_id INT AUTO_INCREMENT PRIMARY KEY,
            taskName VARCHAR(255),
            startDate DATE,
            endDate DATE,
            Category VARCHAR(255),
            Priority VARCHAR(255),
            Status VARCHAR(255)
        )
    """)
    con.commit()
    con.close()

def addRec(entertask, startdate, enddate, category, priority, status):
    con = connect()
    cur = con.cursor()
    cur.execute("INSERT INTO Tasks (taskName, startDate, endDate, Category, Priority, Status) VALUES (%s, %s, %s, %s, %s, %s)", (entertask, startdate, enddate, category, priority, status))
    con.commit()
    con.close()

def viewData():
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM Tasks")
    rows = cur.fetchall()
    con.close()
    return rows

def deleteRec(task_id):
    con = connect()
    cur = con.cursor()
    cur.execute("DELETE FROM Tasks WHERE task_id = %s", (task_id,))
    con.commit()
    con.close()

def dataUpdate(task_id, taskname="", startdate="", enddate="", category="", priority="", status=""):
    con = connect()
    cur = con.cursor()
    cur.execute("""
        UPDATE Tasks 
        SET taskname = %s, startdate = %s, enddate = %s, category = %s, priority = %s, status = %s
        WHERE task_id = %s
    """, (taskname, startdate, enddate, category, priority, status, task_id))
    con.commit()
    con.close()

def Desc():
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM Tasks ORDER BY id DESC")
    rows = cur.fetchall()
    con.close()
    return rows

taskData()