from django.shortcuts import render
from .models import NewCase
from .serializers import FillNewCaseSerializer,GetAllCaseSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
# Create your views here.

@swagger_auto_schema(
        methods=['POST'],
        request_body=FillNewCaseSerializer,
        operation_description='Create New Case'
)

@api_view(['POST'])
def create_case(request):
    if request.method == 'POST':
        new_case_serializer = FillNewCaseSerializer(data=request.data)
        if new_case_serializer.is_valid():
            new_case_serializer.save()
            return Response(new_case_serializer.data, status=status.HTTP_201_CREATED)
        return Response(new_case_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_cases(request):
    get_all = NewCase.objects.all()
    if request.method=='GET':
        get_all_case_serializer = GetAllCaseSerializer(get_all, many=True)
        return Response(get_all_case_serializer.data,status=status.HTTP_200_OK)