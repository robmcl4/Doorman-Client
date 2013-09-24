import os
import sys
import logging
import logging.handlers

# bring door into scope
_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if not _path in sys.path:
    sys.path.append(_path)

from door.db import event, heartbeat
from door import detector

# set up logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
sh  = logging.StreamHandler()
rfh = logging.handlers.RotatingFileHandler(
                        os.path.join(_path, "door.log"),
                        maxBytes=2048,
                        backupCount=3)
fmt = logging.Formatter("%(asctime)s : %(name)s : %(message)s", 
                        "%Y-%m-%d %H:%M:%S")
sh.setFormatter(fmt)
rfh.setFormatter(fmt)
logger.addHandler(sh)
logger.addHandler(rfh)

# ------ Main Program -----------
def main():
    heartbeat.start()
    logger.info("Detecting ...")
    while True:
        ev = detector.wait_for_event()
        if ev == detector.DOOR_OPEN:
            logger.info("Open")
            event.record_open()
        else:
            logger.info("Close")
            event.record_close()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Shutting down ...")
    except Exception, e:
        logging.exception(e)
