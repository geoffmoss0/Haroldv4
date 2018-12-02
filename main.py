import sqlite3
from sqlite3 import Error
from sqlite3 import Connection
import argparse
import os
from pygame import mixer


def create_conn() -> bool:
    try:
        conn = sqlite3.connect("C:\\Users\\gb_mo\\Documents\\Work\\Coding\\Haroldv4\\database.db")
        return conn
    except Error as e:
        print(e)
    return None


def create_users(conn :Connection):
    sql = """CREATE TABLE IF NOT EXISTS Users (
                username text NOT NULL PRIMARY KEY
                path text
                song_plays integer
            );"""
    c = conn.cursor()
    c.execute(sql)


def main():
    # mixer.init()
    # mixer.music.load("C:\\Users\\gb_mo\\Downloads\\LandOfRuins.mp3");
    # mixer.music.play()

    parser = argparse.ArgumentParser(description="Process command line variables")
    parser.add_argument("--debug", "-d", action="store_true")

    conn = create_conn()
    create_users()


if __name__ == "__main__":
    main()
