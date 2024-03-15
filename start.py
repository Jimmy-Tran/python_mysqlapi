import requests
import json
import mysql.connector
import keyboard

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="", # Enter password here
    auth_plugin="mysql_native_password"
)


# print(response)
# print(mydb)


def database_menu():
    mycursor = mydb.cursor()
    print("MENU")
    print("1. Create DB")
    print("2. Delete DB")
    print("3. Show DB")
    print("4. Exit")
    choice = input("")
    if choice == "1":
        print("Creating db..")
        mycursor.execute("CREATE DATABASE IF NOT EXISTS Schuberg")
        database_menu()
    elif choice == "2":
        print('Deleting db..')
        mycursor.execute("DROP DATABASE IF EXISTS Schuberg")
        database_menu()
    elif choice == "3":
        mycursor.execute("SHOW DATABASES")
        # print(mycursor.fetchall())
        for db in mycursor:
            print(db)
        database_menu()
    elif choice == '4':
        quit()


def retrieve_api():
    res = requests.get(
        '') # Revoked for privacy
    response = json.loads(res.text)
    print(response)


def menu():
    print("Welcome to menu selection"
          "\n[A] Open database menu"
          "\n[B] Receive API Information"
          "\n[X] Close the menu\n")
    key = input()
    if key.lower() == "a":
        database_menu()
    elif key.lower() == "b":
        retrieve_api()
    elif key.lower() == "x":
        quit()


menu()