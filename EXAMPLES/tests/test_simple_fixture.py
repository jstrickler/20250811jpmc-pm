from datetime import date
import pytest
import sqlite3
import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
president_db_path = os.path.join(THIS_DIR, 'presidents.db')

db_conn = sqlite3.connect(president_db_path)  # open relative to EXAMPLES
db_cursor = db_conn.cursor()
db_cursor.row_factory = sqlite3.Row  # set the row factory to be a Row object

def get_presidents():
    db_cursor.execute('select * from presidents')
    return db_cursor.fetchall()

@pytest.mark.parametrize('president', get_presidents())
def test_dob_is_valid_date(president):
    assert isinstance(president['birthdate'], str)