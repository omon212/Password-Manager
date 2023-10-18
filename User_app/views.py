from django.shortcuts import render
from rest_framework.views import APIView
from .models import User, Password
import random
from .serializers import UserSerializer, PasswordSerializer,LoginSerializer
from rest_framework.response import Response


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
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"User created successfully"},status=201)
        else:
            return Response(serializer.errors,status=400)



class PasswordAplication(APIView):
    serializer_class = PasswordSerializer
    queryset = Password.objects.all()
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Password created successfully"},status=201)
        else:
            return Response(serializer.errors,status=400)


class Login(APIView):
    serializer_class = LoginSerializer
    qeryset = User.objects.all()
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        if username is None or password is None:
            return Response({"error":"Please provide both username and password"},status=400)
        user = User.objects.filter(username=username,password=password)
        return Response({"message":"Login successfully"},status=200)

