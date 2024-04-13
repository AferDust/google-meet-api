from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from google_auth_oauthlib.flow import Flow

from django.shortcuts import redirect

from api.permissions import IsGoogleAuthenticated
from api.auth.serializers import UserSerializer
from config import settings


class GoogleOAuth2AuthorizationAPIView(APIView):

    def get(self, request):
        flow = Flow.from_client_config(
            settings.GOOGLE_OAUTH2_CLIENT_CONFIG,
            scopes=[
                'openid',
                'https://www.googleapis.com/auth/userinfo.profile',
                'https://www.googleapis.com/auth/userinfo.email'
            ],
            redirect_uri="http://127.0.0.1:8000/api/auth/callback"
        )

        authorization_url, state = flow.authorization_url(
            access_type='offline',
            include_granted_scopes='true',
        )

        request.session['state'] = state
        return redirect(authorization_url)


class GoogleOAuth2CallbackAPIView(APIView):

    def get(self, request):
        state = request.session.get('state', '')

        flow = Flow.from_client_config(
            settings.GOOGLE_OAUTH2_CLIENT_CONFIG,
            scopes=[
                'openid',
                'https://www.googleapis.com/auth/userinfo.profile',
                'https://www.googleapis.com/auth/userinfo.email'
            ],
            state=state,
            redirect_uri="http://127.0.0.1:8000/api/auth/callback"
        )

        flow.fetch_token(authorization_response=request.build_absolute_uri())
        credentials = flow.credentials

        request.session['credentials'] = {
            'token': credentials.token,
            'refresh_token': credentials.refresh_token,
            'token_uri': credentials.token_uri,
            'client_id': credentials.client_id,
            'client_secret': credentials.client_secret,
            'scopes': credentials.scopes
        }

        return Response({'access_token': credentials.token})


class GetUserGoogleTokemAPIView(APIView):
    permission_classes = [IsGoogleAuthenticated]

    def get(self, request):
        return Response({"message": "You have access!",
                         "profile": request.user_info
                         })

class RegistrationCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
