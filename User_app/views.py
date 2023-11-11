from django.shortcuts import render
from rest_framework.views import APIView
from .models import User, Password
import random
from .serializers import UserSerializer, PasswordSerializer, LoginSerializer, User_passwords_seralizer
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema


class PasswordGeneratorLevel1(APIView):

    def get(self, request):
        # all alphabet and numbers in List

        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u", "v", "w", "x", "y", "z",
                    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
                    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                    "U", "V", "W", "X", "Y", "Z"]
        # password list
        password = ""

        for i in range(8):
            password += random.choice(alphabet)
        return Response({"password": password}, status=200)


# Create your views here.

class PasswordGeneratorLevel2(APIView):
    def get(self, request):
        # all alphabet and numbers in List

        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u", "v", "w", "x", "y", "z",
                    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
                    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                    "U", "V", "W", "X", "Y", "Z",
                    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ";"]
        # password list
        password = ""

        # must 2 sybols and 2 numbers in password
        for i in range(2):
            password += random.choice(alphabet[26:35])
        for i in range(2):
            password += random.choice(alphabet[62:])
        for i in range(4):
            password += random.choice(alphabet)

        return Response({"password": password}, status=200)


class PasswordGeneratorLevel3(APIView):
    def get(self, request):
        # all alphabet and numbers in List

        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u", "v", "w", "x", "y", "z",
                    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
                    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                    "U", "V", "W", "X", "Y", "Z",
                    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ";"]
        # password list
        password = ""

        # must 2 sybols and 2 numbers in password
        for i in range(2):
            password += random.choice(alphabet[26:35])
        for i in range(2):
            password += random.choice(alphabet[62:])
        for i in range(12):
            password += random.choice(alphabet)

        return Response({"password": password}, status=200)


class UserRegistration(APIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=201)
        else:
            return Response(serializer.errors, status=400)


class PasswordAplication(APIView):

    serializer_class = PasswordSerializer
    queryset = Password.objects.all()

    @swagger_auto_schema(request_body=PasswordSerializer)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Password created successfully"}, status=201)
        else:
            return Response(serializer.errors, status=400)


class Login(APIView):
    serializer_class = LoginSerializer
    qeryset = User.objects.all()

    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if username is None or password is None:
            return Response({"error": "Please provide both username and password"}, status=400)
        user = User.objects.filter(username=username, password=password)
        return Response({"message": "Login successfully"}, status=200)


class Show_all_userpasswords(APIView):
    serializer_class = PasswordSerializer
    queryset = Password.objects.all()

    def get(self, request):
        user = Password.objects.all()
        list_user = {}
        for i in user:
            print(i.user)
            list_user[str(i.user)] = [i.password, i.name_of_applications, i.time]
        return Response(list_user, status=200)


class User_passwords(APIView):
    serializer_class = User_passwords_seralizer
    queryset = Password.objects.all()

    @swagger_auto_schema(User_passwords_seralizer)
    def post(self, request):
        print(True)
        username = request.data.get('username')
        info_id = User.objects.all().filter(username=username)
        for i in info_id:
            foydalanuvchi_idsi = i.id
        info_passwords = Password.objects.all().filter(user=foydalanuvchi_idsi)
        ser = PasswordSerializer(info_passwords,many=True)
        return Response(ser.data)
