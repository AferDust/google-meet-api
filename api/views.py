from django.shortcuts import redirect
from google_auth_oauthlib.flow import Flow
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build


#
#
# class GoogleCalendarEvents(APIView):
#     def get(self, request):
#
#         SERVICE_ACCOUNT_FILE = 'carbon-zone-417117-e22bb594e631.json'
#         scopes = ["https://www.googleapis.com/auth/calendar"]
#
#         credentials = service_account.Credentials.from_service_account_file(
#             SERVICE_ACCOUNT_FILE, scopes=scopes)
#         service = build('calendar', 'v3', credentials=credentials)
#
#         calendar_id = 'primary'
#         events_result = service.events().list(calendarId=calendar_id, maxResults=10).execute()
#         events = events_result.get('items', [])
#
#         # Extract relevant event information
#         event_list = []
#         for event in events:
#             event_summary = event.get('summary', 'No Summary')
#             event_start = event.get('start', {}).get('dateTime', 'No Start Time')
#             event_end = event.get('end', {}).get('dateTime', 'No End Time')
#             event_list.append({'summary': event_summary, 'start': event_start, 'end': event_end})
#
#         return Response({'events': event_list})


# class GoogleLogInAPIView(APIView):
#
#     def get(self, request):
#         client_config = {
#             "web": {
#                 "client_id": "722494925006-7s80gcjt08kpfcdkcc4515ppe8m8gt6u.apps.googleusercontent.com",
#                 "project_id": "carbon-zone-417117",
#                 "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#                 "token_uri": "https://oauth2.googleapis.com/token",
#                 "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#                 "client_secret": "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",
#                 "redirect_uris": [
#                     "https://oauth.pstmn.io/v1/callback"
#                 ]
#             }
#         }
#
#         flow = Flow.from_client_config(client_config, scopes=['https://www.googleapis.com/auth/calendar'])
#         flow.redirect_uri = 'http://127.0.0.1:8000/api/google/callback'
#
#         authorization_url, state = flow.authorization_url(
#             access_type='offline',
#             include_granted_scopes='true')
#
#         return redirect(authorization_url)
#
#
# class CallBackAPIView(APIView):
#
#     def post(self, request):
#         state = request.GET.get('state', '')
#         code = request.GET.get('code', '')
#
#         flow = Flow.from_client_secrets_file('credentials.json',
#                                              scopes=['https://www.googleapis.com/auth/calendar'],
#                                              state=state)
#         flow.redirect_uri = 'http://127.0.0.1:8000/api/google/calendar'
#
#         flow.fetch_token(code=code)
#
#         credentials = flow.credentials
#         request.session['credentials'] = {
#             'token': credentials.token,
#             'refresh_token': credentials.refresh_token,
#             'token_uri': credentials.token_uri,
#             'client_id': credentials.client_id,
#             'client_secret': credentials.client_secret,
#             'scopes': credentials.scopes
#         }
#
#         return Response("Google Calendar access granted.", status=status.HTTP_200_OK)
#
#
# class GoogleCalendarAPIView(APIView):
#
#     def get(self, request):
#         creds_data = request.session.get('credentials')
#         credentials = Credentials(**creds_data)
#
#         service = build('calendar', 'v3', credentials=credentials)
#
#         event = {
#             'summary': 'Appointment',
#             'location': '800 Howard St., San Francisco, CA 94103',
#             'description': 'A chance to hear more about Google\'s developer products.',
#             'start': {
#                 'dateTime': '2024-05-28T09:00:00-07:00',
#                 'timeZone': 'America/Los_Angeles',
#             },
#             'end': {
#                 'dateTime': '2024-05-28T17:00:00-07:00',
#                 'timeZone': 'America/Los_Angeles',
#             },
#         }
#
#         event_result = service.events().insert(calendarId='primary', body=event).execute()
#
#         return Response(f"Event created: {event_result.get('htmlLink')}", status=status.HTTP_200_OK)


class TestAPIView(APIView):

    def get(self, request):
        return Response(data="Hello i passed test", status=status.HTTP_200_OK)