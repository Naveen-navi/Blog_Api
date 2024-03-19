from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from  rest_framework.generics import GenericAPIView
from rest_framework.exceptions import AuthenticationFailed
from drf_yasg.utils import swagger_auto_schema
from .models import User

import jwt, datetime
from .response import *
class RegisterView(GenericAPIView):
    serializer_class = UserSerializer
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    


class LoginView(GenericAPIView):
    serializer_class = UserSerializer['email', 'password']
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response
    
class UserView(GenericAPIView):
    # serializer_class = UserSerializer
    @swagger_auto_schema(responses={200: loginResponse,400:errorResponse})
    # @action(detail=False, methods=['get'])
    def get(self, request):
        token = request.COOKIES.get('jwt')
        try:

            if not token:
                raise AuthenticationFailed('Unauthenticated!')

            try:
                payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            except jwt.ExpiredSignatureError:
                raise AuthenticationFailed('Unauthenticated!')

            user = User.objects.filter(id=payload['id']).first()
            serializer = UserSerializer(user)
            return Response({'status':200,
                             'message': "Sucessful",
                             'data':serializer.data
                            })
        except:
            return Response({'status':400,
                             'message': "Failed ",
                             'data':[]
                            })
    

class LogoutView(GenericAPIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response




