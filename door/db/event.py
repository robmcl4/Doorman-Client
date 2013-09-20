"""
  event.py
  
  Contains a door event
  
  Author: Robert McLaughlin
"""
from door.db import connection

def _record(type_):
    """
        Record a type of event
    """
    conn = connection.get_conn()
    curs = conn.cursor()
    curs.execute("insert into events (type) values (%s)", (type_,))
    curs.close()
    conn.commit()

def record_open():
    _record("open")

def record_close():
    _record("close")
