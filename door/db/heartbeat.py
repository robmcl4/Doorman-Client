import logging
import threading
import time
from door.db import connection

logger = logging.getLogger(__name__)

def _send():
    conn = connection.get_conn()
    curs = conn.cursor()
    curs.execute("update heartbeat set last = NOW()")
    curs.close()
    conn.commit()
    logger.info("Sent heartbeat")

def _heartbeater():
    while True:
        _send()
        time.sleep(3*60-3)

def start():
    """
        Start sending asyncronous hartbeats
    """
    logger.info("Starting heartbeater")
    th = threading.Thread(target=_heartbeater)
    th.setDaemon(True)
    th.start()
