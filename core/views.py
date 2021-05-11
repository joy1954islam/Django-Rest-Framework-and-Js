from django.shortcuts import render
from .serializers import PersonInformationSerializers
from .models import PersonalInformation
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def personal_information_list(request):
    """
    List all code Personal Information, or create a new Personal Information.
    """
    if request.method == 'GET':
        personal = PersonalInformation.objects.all()
        serializer = PersonInformationSerializers(personal, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PersonInformationSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def personal_information_detail(request, pk):
    """
    Retrieve, update or delete a code Personal Information.
    """
    try:
        personal = PersonalInformation.objects.get(pk=pk)
    except PersonalInformation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PersonInformationSerializers(personal)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PersonInformationSerializers(personal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        personal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def personal_information(request):
    return render(request, 'personal_information_list.html')
