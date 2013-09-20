"""
  detecter.py
  
  Detects when the door is open or closed, provides helpful
  methods for interfacing.
  
  Author: Robert McLaughlin
"""

import logging
from door.config import config
logger = logging.getLogger(__name__)

# importing may go bad, at least log a relevant message first
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    logger.critical(
      "Error importing RPi.GPIO! Do you have superuser privileges?"
    )
    raise


DOOR_OPEN, DOOR_CLOSE = range(2)
_channel = 0
_last_state = None

def _setup():
    global _last_state
    global _channel
    _channel = int(config['pins']['pin_num'])
    mode = config['pins']['mode']
    GPIO.setmode(GPIO.BVM if mode == 'BCM' else GPIO.BOARD)
    GPIO.setup(_channel, GPIO.IN)
    _last_state = _door_state(_read_pin_avg())

def _read_pin_avg(n=1000):
    """
        Averages the value from the pin and then
        returns the rounded result (zero or one)
    """
    sum_ = 0
    for i in range(n-1):
        sum_ += GPIO.input(_channel)
    return 1 if sum_ > n//2 else 0

def _door_state(pin_avg):
    """
        Return the state that corresponds to the given pin reading
    """
    return DOOR_OPEN if pin_avg else DOOR_CLOSE

def _pin_state(door_state):
    """
        Return the pin reading that corresponds to this door state
    """
    return 1 if door_state == DOOR_OPEN else 0

def wait_for_event():
    """
        Wait for the next edge to be detected
    """
    global _last_state
    _last_state = DOOR_OPEN if _last_state == DOOR_CLOSE else DOOR_CLOSE
    target_state = _pin_state(_last_state)
    
    while True:
        avg = _read_pin_avg()
        print(avg)
        if avg == target_state:
            break
    
    return _last_state

def _debug():


_setup()
