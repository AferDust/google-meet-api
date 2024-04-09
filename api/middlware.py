from google.oauth2 import id_token
from google.auth.transport import requests
import requests

from config.settings import GOOGLE_OAUTH2_CLIENT_CONFIG


class GoogleOAuth2Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Default to None for unauthenticated requests
        request.user_info = None

        # Extract the token from the Authorization header
        token = request.META.get('HTTP_AUTHORIZATION')
        if token:
            token = token.replace("Bearer ", "", 1)
            user_info = verify_token(token)

            if user_info is not None:
                # Token is valid, and user_info was retrieved
                request.user_info = user_info
            else:
                # Token is invalid or verification failed; user_info remains None
                pass

        response = self.get_response(request)
        return response


def verify_token(access_token):
    # Google's OAuth 2.0 Token Info endpoint
    url = f"https://www.googleapis.com/oauth2/v3/tokeninfo?access_token={access_token}"

    # Make the GET request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # The request was successful; parse the response JSON
        user_info = response.json()

        # Optionally, check if the 'aud' (audience) value in the response matches your app's client ID
        # if user_info.get('aud') != YOUR_CLIENT_ID:
        #     return None

        return user_info
    else:
        # The request failed; handle the error
        print(f"Failed to verify token: {response.text}")
        return None
