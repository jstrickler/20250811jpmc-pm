import sqlite3

# conn = sqlite3.Connection(...)
#     sqlite3.connect(":memory:")
with sqlite3.connect("../DATA/presidents.db") as conn:  # connect to the database

    s3_cursor = conn.cursor()  # get a cursor object

    # select specified columns from all presidents
    s3_cursor.execute('''
        select termnum, firstname, lastname, party
        from presidents
    ''')  # execute a SQL statement

    # c.fetchall()  c.fetchmany(1000) c.fetchone()
    for term, firstname, lastname, party in s3_cursor:
        print(f"{term:2d} {firstname:25} {lastname:20} {party}")
    print()

