from mysql import connector
from door.config import config

_conn = None

def _connect():
    global conn
    section = config['mysql']
    
    user  = section['user']
    pass_ = section['pass']
    db    = section['db']
    host  = section['host']
    port  = section['port']
    
    _conn = connector.connect(user=user

def get_conn():
    if not conn or not conn.ping():
        _connect()
    return conn
