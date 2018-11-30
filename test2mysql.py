import pymysql.cursors

#
# ex table in mysql:
# CREATE TABLE `users` (
#   `id` int(11) NOT NULL AUTO_INCREMENT,
#   `email` varchar(255) COLLATE utf8_bin NOT NULL,
#   `password` varchar(255) COLLATE utf8_bin NOT NULL,
#   PRIMARY KEY (`id`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
# AUTO_INCREMENT=1 ;


commandvar = ' '
# username = input('Welcome. Please enter your username. \n >')
username = "manager"
# password = input('Please enter your password. \n >')
# connect to db
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='1277700ryan',
                             db='mydatabase',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
print("Made connection...")


def helpfunctionmanager():
    helpstr = """Viewing user guide.
    List of commands:
    > help \t\t\t (displays this user guide)
    > stop \t\t\t (stops program)
    > viewinfo \t\t (views personal info: ID, Assigned Project, leader, location}
    > itemreport \t (generates report)
    > volunreport \t (generates personnel report)
    > reserve \t\t (reserves an item in stock)
    > remove \t\t (removes an item from stock)
    > addvolun \t\t (adds a volunteer)
    > modifyvolun \t (change a volunteer's data)
    > deletevolun \t (delete a volunteer)"""
    print(helpstr)
    return


def helpfunctionvolun():
    helpstrb = """Viewing user guide.
        List of commands:
        > help \t\t (displays this user guide)
        > stop \t\t (stops program)
        > viewinfo \t (views personal info: ID, Name, Password, Assigned Project(s), leader, position) 
        > itemreport \t (generates report)
        > changepass \t (change your password)
        """
    print(helpstrb)
    return


def viewinfo():
    print('viewing info')
    return


def itemreport():
    print('itemreport')
    return


def volunreport():
    print('volunreport')
    return


def reserve():
    print('reserve')
    return


def remove():
    print('remove')
    return


def addvolun():
    print('Adding new volunteer...')

    voname = input("Enter name: ")
    volocc = input("Enter task: ")
    leadid = input("Enter project leader id: ")
    password = input("Enter new password: ")

    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `Volunteer` (name, occupation, leader_id, password) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (voname, volocc, leadid, password))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
        print("New volunteer added: ")
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `Volunteer` WHERE `name`=%s AND `password`=%s"
            cursor.execute(sql, (voname, password,))
            result = cursor.fetchone()
            print(result)

            # for row in cursor:
            #   print(row)

    finally:
        #   connection.close()

        return


def modifyvolun():
    volid = input("Enter the ID of the volunteer whose info you wish to modify: \n > ")
    cmmd2 = input("What would you like to modify? \n"
                  "'name', 'task', 'superior', 'password' \n > ")
    if cmmd2 == 'name':
        newname = input("Enter the new name: \n > ")
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE Volunteer SET `name`=%s WHERE `volun_id`=%s"
                cursor.execute(sql, (newname, volid))

            connection.commit()
            print("Data Updated.")

            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT * FROM `Volunteer` WHERE `volun_id`=%s"
                cursor.execute(sql, (volid,))
                result = cursor.fetchone()
                print(result)

        finally:
            return
    elif cmmd2 == 'task':
        newtask = input("Enter the new task: \n > ")
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE Volunteer SET `occupation`=%s WHERE `volun_id`=%s"
                cursor.execute(sql, (newtask, volid))

            connection.commit()
            print("Data Updated.")

            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT * FROM `Volunteer` WHERE `volun_id`=%s"
                cursor.execute(sql, (volid,))
                result = cursor.fetchone()
                print(result)

        finally:
            return
    elif cmmd2 == 'superior':
        newsup = input("Enter the new superior's ID: \n > ")
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE Volunteer SET `leader_ID`=%s WHERE `volun_id`=%s"
                cursor.execute(sql, (newsup, volid))

            connection.commit()
            print("Data Updated.")

            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT * FROM `Volunteer` WHERE `volun_id`=%s"
                cursor.execute(sql, (volid,))
                result = cursor.fetchone()
                print(result)

        finally:
            return
    elif cmmd2 == 'password':
        newpass = input("Enter the new password (must be less than ten char long, unique): \n > ")
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE Volunteer SET `password`=%s WHERE `volun_id`=%s"
                cursor.execute(sql, (newpass, volid))

            connection.commit()
            print("Data Updated.")

            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT * FROM `Volunteer` WHERE `volun_id`=%s"
                cursor.execute(sql, (volid,))
                result = cursor.fetchone()
                print(result)

        finally:
            return
    else:
        print("Command not found.")
        return


def deletevolun():
    deletvol = input("Enter the ID of the volunteer to be deleted: \n >")
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM `Volunteer` WHERE `volun_id`=%s"
            cursor.execute(sql, (deletvol,))

        connection.commit()
        print("Volunteer removed.")
    finally:
        return


def changepass():
    volid = input("Enter your ID num: \n >")
    newpass = input("Enter the new password (must be less than ten char long, unique): \n > ")
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE Volunteer SET `password`=%s WHERE `volun_id`=%s"
            cursor.execute(sql, (newpass, volid))

        connection.commit()
        print("Data Updated.")
    finally:
        return


if username == 'manager':
    helpfunctionmanager()

    while commandvar != 'stop':
        commandvar = input("-> ")

        if commandvar == 'help':
            helpfunctionmanager()
        elif commandvar == 'stop':
            print('Goodbye.')
        elif commandvar == 'viewinfo':
            viewinfo()
        elif commandvar == 'itemreport':
            itemreport()
        elif commandvar == 'volunreport':
            volunreport()
        elif commandvar == 'reserve':
            reserve()
        elif commandvar == 'remove':
            remove()
        elif commandvar == 'addvolun':
            addvolun()
        elif commandvar == 'modifyvolun':
            modifyvolun()
        elif commandvar == 'deletevolun':
            deletevolun()
        else:
            print('Command not found. Type "help" to view all possible commands. '
                  'Be sure to omit any spaces when entering commands.')
elif username == 'volunteer':
    helpfunctionvolun()

    while commandvar != 'stop':
        commandvar = input("-> ")

        if commandvar == 'help':
            helpfunctionvolun()
        elif commandvar == 'stop':
            print('Goodbye.')
        elif commandvar == 'viewinfo':
            viewinfo()
        elif commandvar == 'itemreport':
            itemreport()
        elif commandvar == 'changepass':
            changepass()
        else:
            print('Command not found. Type "help" to view all possible commands. '
                  'Be sure to omit any spaces when entering commands.')

"""
try:
    with connection.cursor() as cursor:
        # create a new record
        sql = "INSERT INTO 'tablename' ('attribute', 'attribute') VALUES (%s, %s)"
        cursor.execute(sql, ('attributetoinsert', 'attributetoinsert'))

        connection.commit()
        # must commit to save changes

    with connection.cursor() as cursor:
        # read a single record ex
        sql = "SELECT 'id', 'password' FROM 'users' WHERE 'email' =%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)

finally:
    connection.close()
"""
connection.close()
