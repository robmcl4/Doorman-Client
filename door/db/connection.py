from mysql import connector
from door.config import config
import os

_conn = None
_path = os.path.dirname(os.path.abspath(__file__))
_key_dir = os.path.join(_path, "ssl")

def _connect():
    global _conn
    section = config['mysql']
    
    user  = section['user']
    pass_ = section['pass']
    db    = section['database']
    host  = section['host']
    port  = section['port']
    
    ssl_ca   = os.path.join(_key_dir, "ca-cert.pem")
    ssl_cert = os.path.join(_key_dir, "client-cert.pem")
    ssl_key  = os.path.join(_key_dir, "client-key.pem")
    
    _conn = connector.connect(user=user, 
                              passwd   =pass_, 
                              db       =db, 
                              host     =host, 
                              port     =port,
                              ssl_ca   =ssl_ca,
                              ssl_cert =ssl_cert,
                              ssl_key  =ssl_key,
                              ssl_verify_cert=True)

def get_conn():
    if not _conn or not _conn.ping():
        _connect()
    return _conn
