from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.exceptions import AuthenticationFailed

def get_user_from_token(token):
    try:
        # Decode the token
        decoded_token = AccessToken(token)
        user_id = decoded_token['user_id']    
    except (AuthenticationFailed, KeyError) as e:
        raise AuthenticationFailed('Invalid token')
    
    try:
        User = get_user_model()
        user = User.objects.get(id=user_id)
        return user

    except User.DoesNotExist:
        raise AuthenticationFailed('User not found')