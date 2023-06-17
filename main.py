#!/usr/bin/env python3

import sqlite3


# connect to db
con = sqlite3.connect("school.db")
cur = con.cursor()


def create():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    age = input("Enter age: ")
    cur.execute("""
        INSERT INTO Student(first_name, last_name, age)
        VALUES(?, ?, ?);""", (first_name, last_name, age))
    con.commit()


def read():
    res = cur.execute("SELECT * FROM Student;")
    print(res.fetchall())


def update():
    row = input("Enter id: ")
    first_name = input("Enter new first name: ")
    last_name = input("Enter new last name: ")
    age = input("Enter new age: ")
    cur.execute("""
        UPDATE Student
        SET first_name = ?, last_name = ?, age = ?
        WHERE id = ?;""", (first_name, last_name, age, row))
    con.commit()


def delete():
    row = input("Enter id: ")
    cur.execute("""
        DELETE FROM Student
        WHERE id = ?""", (row))
    con.commit()


def main():
    while True:
        print("""
Enter 'c' to create, 'r' to read, 'u' to update,
'd' to delete or 'q' to quit: """)
        print()
        prompt = input("crud> ")
        if prompt == "c":
            create()
        elif prompt == "r":
            read()
        elif prompt == "u":
            update()
        elif prompt == "d":
            delete()
        elif prompt == "q":
            break


if __name__ == "__main__":
    main()

