"""
Shows basic usage of the Google Calendar API. Creates a Google Calendar API
service object and outputs a list of the next 10 events on the user's calendar.
"""
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import httplib2
from datetime import datetime, timedelta
import sys

# Setup the Calendar API
# SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('calendar', 'v3', http=creds.authorize(Http()))
# service = build('calendar', 'v3', http=creds.authorize(Http(proxy_info=httplib2.ProxyInfo(httplib2.socks.PROXY_TYPE_SOCKS5, '192.168.234.1', 8123))))






# sample
# event = {
#   'summary': 'Google I/O 2015',
#   'location': '800 Howard St., San Francisco, CA 94103',
#   'description': 'A chance to hear more about Google\'s developer products.',
#   'start': {
#     'dateTime': '2015-05-28T09:00:00-07:00',
#     'timeZone': 'America/Los_Angeles',
#   },
#   'end': {
#     'dateTime': '2015-05-28T17:00:00-07:00',
#     'timeZone': 'America/Los_Angeles',
#   },
#   'recurrence': [
#     'RRULE:FREQ=DAILY;COUNT=2'
#   ],
#   'attendees': [
#     {'email': 'lpage@example.com'},
#     {'email': 'sbrin@example.com'},
#   ],
#   'reminders': {
#     'useDefault': False,
#     'overrides': [
#       {'method': 'email', 'minutes': 24 * 60},
#       {'method': 'popup', 'minutes': 10},
#     ],
#   },
# }

# event = service.events().insert(calendarId='primary', body=event).execute()
# print 'Event created: %s' % (event.get('htmlLink'))

# set startTime deplay Minutes
params = sys.argv[1:]
if len(params) > 0:
  startTimeDelayMinutes = int(params[0])
else:
  startTimeDelayMinutes = 30

startTime = datetime.now() + timedelta(minutes=startTimeDelayMinutes)
endTime = startTime + timedelta(minutes=5)

def strftime(time1):
  return time1.strftime("%Y-%m-%dT%H:%M:%S")

# reminders.method:
#   popup: app notification
#   email: email
event = {
  "summary": "reminder-%s" % strftime(startTime),
  "start": {
    "dateTime": "%s+08:00" % strftime(startTime)
  },
  "end": {
    "dateTime": "%s+08:00" % strftime(endTime)
  },
  "reminders": {
    "overrides": [{
      "method": "email",
      "minutes": 0
    }],
    "useDefault": False
  }
}
event = service.events().insert(calendarId='primary', body=event).execute()
print('Event created: %s' % (event.get('htmlLink')))



# Call the Calendar API
now = datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
print('Getting the upcoming 10 events')
events_result = service.events().list(calendarId='primary', timeMin=now,
                                      maxResults=10, singleEvents=True,
                                      orderBy='startTime').execute()
events = events_result.get('items', [])

if not events:
    print('No upcoming events found.')
for event in events:
    start = event['start'].get('dateTime', event['start'].get('date'))
    print(start, event['summary'])
