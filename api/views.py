from django.shortcuts import render
# from django.http import JsonResponse
from students.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET','POST'])
def studentsView(request):
    # manual serialization
    # students = Student.objects.all()
    # student_list = list(students.values())
    # return JsonResponse(student_list,safe=False)
    if(request.method == 'GET'):
        students = Student.objects.all()
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif(request.method == 'POST'):
        serializer = StudentSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    return Response({'message':'Method not allowed'},status=status.HTTP_405_METHOD_NOT_ALLOWED)