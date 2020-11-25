"""Please do the coding below and send me your github link:

A retailer offers a rewards program to its customers, awarding points based on each recorded purchase.
A customer receives 2 points for every dollar spent over $100 in each transaction, plus 1 point for every dollar spent
 over $50 in each transaction
(e.g. a $120 purchase = 2x$20 + 1x$50 = 90 points).

Given a record of every transaction during a three month period, calculate the reward points earned for each customer
 per month and total."""

import sqlite3
import math
import datetime
database = "example.db"


def db_connect(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn


class Transaction:
    def __init__(self):
        self.conn = db_connect(database)
        self.cur = self.conn.cursor()

    def getrecords(self, cid):
        for row in self.cur.execute(f"SELECT * FROM transactions where customerid={cid} order by customerid, date DESC"):
            print(f'Customer: {row[3]} earned {self.rewards(row[2])} rewards earned on a {row[1]} with a transaction '
                  f'total of {row[2]}')

    def rewards(self, totalspent):
        if totalspent <= 50:
            return 0
        elif totalspent <= 100:
            return totalspent - 50
        else:
            doublepoints = totalspent - 100
            return math.floor(50 + 2 * doublepoints)

if __name__ == '__main__':
    t = Transaction()
    t.getrecords(2)
