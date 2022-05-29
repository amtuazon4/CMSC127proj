import mysql.connector as mariadb

mariadb_connection = mariadb.connect(
    user="user1",
    password="user1",
    host="localhost",
    port="3306",
    database = "task_record"
    )

create_cursor = mariadb_connection.cursor()

def menu():
    print("----------------------------------")
    print("Menu")
    print("[1] Add/Create Task")
    print("[2] Edit Task")
    print("[3] Delete Task")
    print("[4] View Task (all)")
    print("----------------------------------")
    print("Choice: ")

# menu()

def addTask():
    taskID = int(input("Please input a 2 digit task id: "))
    taskName = str(input("Please input the name of the task: "))
    taskDesc = str(input("Please input description of the task: "))
    taskDeadline = str(input("Please input the deadline of the task (YYYY-MM-DD): "))

    the_command = "INSERT INTO task VALUES (" + str(taskID) + ", \"" + taskName + "\", \"" + taskDesc + "\" , CURDATE(), STR_TO_DATE(\"" + taskDeadline + "\" , \"%Y-%m-%d\"), \"Ongoing\", 001)"

    create_cursor.execute(the_command)
    mariadb_connection.commit()


def editTask():
    create_cursor.execute("SELECT Task_id FROM task")
    data = create_cursor.fetchall()
    
    taskIDs = []
    for x in data:
        taskIDs.append(x[0])
    
    if(len(taskIDs)==0):
        print("There is no data in the database.")
        return

    taskID = int(input("Please input the task id to be edited: "))

    if(taskID in taskIDs):
        taskName = str(input("Please input the new name of the task: "))
        taskDesc = str(input("Please input the new description of the task: "))
        taskDeadline = str(input("Please input the new deadline of the task (YYYY-MM-DD): "))
        # UPDATE task SET Name=<Name>, Description=<Description>, Deadline=STR_TO_DATE(<Deadline>, “%Y-%m-%d”) WHERE Task_id = <Task_id>;

        the_command = "UPDATE task SET Name=\"" + taskName + "\", Description=\"" + taskDesc + "\", Deadline=STR_TO_DATE(\"" + taskDeadline + "\", \"%Y-%m-%d\") WHERE Task_id = " + str(taskID)
        create_cursor.execute(the_command)
        mariadb_connection.commit()
    else:
        print("The Task id you inputted is not in the database.")



def deleteTask():
    create_cursor.execute("SELECT Task_id FROM task")
    data = create_cursor.fetchall()
    
    taskIDs = []
    for x in data:
        taskIDs.append(x[0])

    if(len(taskIDs)==0):
        print("There is no data in the database.")
        return

    taskID = int(input("Please input the task id to be deleted: "))

    if(taskID in taskIDs):
        #DELETE FROM task WHERE Task_id = <Task_id>;

        the_command = "DELETE FROM task WHERE Task_id = " + str(taskID)
    
        create_cursor.execute(the_command)
        mariadb_connection.commit()
    else:
        print("The Task id you inputted is not in the database.")

    


def viewTask():
    create_cursor.execute("SELECT Task_id FROM task")
    data = create_cursor.fetchall()
    
    taskIDs = []
    for x in data:
        taskIDs.append(x[0])

    if(len(taskIDs)==0):
        print("There is no data in the database.")
        return
    
    create_cursor.execute("SELECT * FROM task")
    data = create_cursor.fetchall()

    for x in data:
        print("Task id:\t\t" + str(x[0]))
        print("Task name:\t\t" + x[1])
        print("Task description:\t" + x[2])
        print("Date posted:\t\t" + str(x[3]))
        print("Deadline:\t\t" + str(x[4]))
        print("Status:\t\t\t" + x[5])
        #Category id for now
        print("Category:\t\t" + str(x[6]))
        print()
