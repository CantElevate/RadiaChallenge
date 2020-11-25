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
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute(f'select * from transactions where date={datetime.datetime.now().date()}')
print(c.fetchall())



def rewards(totalspent):
    if totalspent <= 50:
        return 0
    elif totalspent <= 100:
        return totalspent - 50
    else:
        doublepoints = totalspent - 100
        return math.floor(50 + 2 * doublepoints)




