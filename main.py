import sqlite3
from sqlite3 import Error
from sqlite3 import Connection
import argparse
import os
from harold import Harold

def create_conn():
    try:
        conn = sqlite3.connect("C:\\Users\\gb_mo\\Documents\\Work\\Coding\\Haroldv4\\database.db")
        return conn
    except Error as e:
        print(e)
    return None


def create_users(conn: Connection):
    sql = """
            CREATE TABLE IF NOT EXISTS users (
                username text NOT NULL UNIQUE PRIMARY KEY,
                path text,
                song_plays integer
            );"""
    c = conn.cursor()
    c.execute(sql)


def main():

    parser = argparse.ArgumentParser(description="Process command line variables")
    parser.add_argument("--debug", "-d", action="store_true")

    conn = create_conn()
    c = conn.cursor()
    create_users(conn)

    go = True
    while go:
        action = input("Input desired action (Create user (USER) or View users (VIEW) or Clear table (CLEAR) or exit (QUIT)): \n")
        if action == "CREATE":
            run = True
            while run:
                user_in = input("Input username: ")
                if user_in == "quit":
                    run = False
                else:
                    args = user_in.split(" ")
                    c.execute(
                        'INSERT INTO Users(username, path, song_plays) VALUES( "{username}", "C:\\Users\\gb_mo\\Documents\\Work\\Coding\\Haroldv4\\database.db", 0)'.format(
                            username=args[0]))
        elif action == "VIEW":
            c.execute('SELECT * FROM users')
            rows = c.fetchall()
            for row in rows:
                print(row)
        elif action == "QUIT":
            go = False
        elif action == "CLEAR":
            c.execute("DROP TABLE users")
            create_users(conn)


if __name__ == "__main__":
    main()
