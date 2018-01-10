from dateutil.parser import parse

def isDate(string):
    try:
        parse(string)
        return True
    except ValueError:
        return False

def isDay(s):
    test = s == 'SUN' or s == 'MON' or s == 'TUE' or s == 'WED' or s == 'THU' or s == 'FRI' or s == 'SAT'
    if test:
        return True
    return False

with open('/Users/p/Desktop/Python/Facebook/NLP-Event-Detector/PastEvents_Jun2015-Jan2018.txt') as f:
    events = f.readlines()

#First pass cleaning
#removes basic things
i = 0
while i < (len(events)):
    event = events[i]
    if event == '\n':
        _ = events.pop(i)
    elif '\xc2' in event or 'went' in event or 'friends' in event:
        _ = events.pop(i)
    elif '\n' in event:
        events[i] = event.replace('\n', '')
    else:
        i+=1

#Second pass cleaning
#removing any days and dates
i = 0
while i < len(events):
    event = events[i]
    if isDay(event):
        _ = events.pop(i)
    elif isDate(event):
        _ = events.pop(i)
    else:
        i+=1

#Third pass cleaning
#removing event details who invited you
i = 0
while i < len(events):
    event = events[i]
    if 'invited you' in event:
        _ = events.pop(i)
    elif 'Went' in event or 'interested' in event or 'Nadia' in event:
        _ = events.pop(i)
    elif "You couldn't go." == event:
        _ = events.pop(i)
    elif "Event Canceled" == event:
        _ = events.pop(i)
    else:
        i+=1

import pickle

pickle.dump( events, open( "cleanedEvents", "wb" ) )
#events = pickle.load(open('cleanedEvents.p', 'rb'))
