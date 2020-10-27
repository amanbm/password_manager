import sqlite3


f = open("password.txt", "r")
PASSWORD = f.readline() 
PASSWORD = PASSWORD[:-1]

connect = input("Enter password: ")


while connect != PASSWORD:
    connect = input("Enter password: ")
    if connect == "q":
        exit()

conn = sqlite3.connect("safe.db")
c = conn.cursor()

try:

    c.execute("""CREATE TABLE SAFE (
             SERVICE TEXT,
             PASSWORD TEXT)
             """)

    conn.commit()

    print("database created")

except:
    print("database already exists")






while True:
    print("*"*15)
    print("COMMANDS:")
    print("q = quite the program")
    print("gp = get password")
    print("sp = store password")
    print("*"*15)
    input_ = input(":")

    if input_ == "q":
        break
    if input_ == "gp":
        service = input("What service would you like your password for? ")
        c.execute("SELECT PASSWORD FROM SAFE WHERE SERVICE='{}'".format(service))
        result = c.fetchall()
        if(len(result) == 0):
            print("service does not exist yet")
        else:
            print("Password: {}".format(result))
        


    if input_ == "sp":
        service = input("What service? ")
        password = input("Password for service: ")
        c.execute("SELECT PASSWORD FROM SAFE WHERE SERVICE='{}'".format(service))
        if(len(c.fetchall()) > 0):
                print("password already exists")
                if(input("would you like to overwrite(y/n)? ") == "y"):
                    c.execute("UPDATE SAFE SET PASSWORD='{}' WHERE SERVICE='{}'".format(password, service))

        else:
            string = "INSERT INTO SAFE VALUES ('{}', '{}')".format(service, password)
            c.execute(string)

        conn.commit()
        print("password set")






conn.close()
