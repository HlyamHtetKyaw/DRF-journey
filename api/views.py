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

@api_view(['GET','PUT','DELETE'])
def studentsDetailView(request,pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({'message':'Student not found'},status=status.HTTP_404_NOT_FOUND)
    
    if(request.method == 'GET'):
        serializer = StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif(request.method == 'PUT'):
        serializer = StudentSerializer(student,data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif(request.method == 'DELETE'):
        student.delete()
        return Response({'messae':'Student deleted successfully'},status = status.HTTP_204_NO_CONTENT)