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
                username text NOT NULL PRIMARY KEY,
                path text,
                song_plays integer
            );"""
    c = conn.cursor()
    c.execute("DROP TABLE users")
    c.execute(sql)


def main():

    parser = argparse.ArgumentParser(description="Process command line variables")
    parser.add_argument("--debug", "-d", action="store_true")

    conn = create_conn()
    c = conn.cursor()
    create_users(conn)
    h = Harold()
    h.run()

    run = True
    while run:
        user_in = input("Input username")
        if user_in == "quit":
            run = False
        else:
            args = user_in.split(" ")
            c.execute("""INSERT INTO Users(username, path, song_plays) VALUES( {username}, )""".format(username=args[0]))


if __name__ == "__main__":
    main()
