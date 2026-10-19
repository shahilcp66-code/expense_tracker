from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView
from EXPAPP.serializers import UserSerializer,ExpenseSerializer
from django.contrib.auth.models import User
from rest_framework import authentication,permissions
from EXPAPP.models import ExpenseModel
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter

# Create your views here.

class UserRegister(CreateAPIView):
    serializer_class=UserSerializer

    def perform_create(self,serializer):
        return User.objects.create_user(**serializer.validated_data)

class ExpenseCreateList(CreateAPIView,ListAPIView):
    serializer_class=ExpenseSerializer
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self,serializer):
        user=self.request.user
        return serializer.save(owner=user)

    def get_queryset(self):
        return ExpenseModel.objects.filter(owner=self.request.user)
    filter_backends=[
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter

    ]
    filterset_fields=["title"]
    search_fields=["category","payment"]
    ordering_fields=["amount","created_at"]

class ExpenseRetrieveUpdateDestroy(RetrieveAPIView,DestroyAPIView,UpdateAPIView):
    serializer_class=ExpenseSerializer
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        return ExpenseModel.objects.filter(owner=self.request.user)



    
