# Given a moment, determine the moment 
# that would be after a gigasecond has passed.

import datetime

def add(moment):
    return moment + datetime.timedelta(seconds=1e9)
