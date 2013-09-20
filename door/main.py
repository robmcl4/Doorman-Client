import os
import sys

# bring door into scope
_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if not _path in sys.path:
    sys.path.append(_path)

from door import detector
from door.db import event

# main detection loop
while True:
    ev = detector.wait_for_event()
    if ev == detector.DOOR_OPEN:
        print("Open")
        event.record_open()
    else:
        print("Close")
        event.record_close()
