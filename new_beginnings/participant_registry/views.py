from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Participant
from .serializers import ParticipantSerializer


@api_view(['GET', 'PUT'])
def participant(request):
    
    # Get all participants
    if request.method == 'GET':
        try:
            participant = Participant.objects.all()
            serializer = ParticipantSerializer(participant, many=True)
            return Response(serializer.data, status=status.HTTP_302_FOUND)
        except Participant.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # Add new participant
    elif request.method == 'PUT':
        serializer = ParticipantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.data)
            return Response(removeNone(serializer.data), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE'])
def editParticipant(request, reference_number):

    # Retrieve participant information by reference number
    if request.method == 'GET':
        try:
            participant = Participant.objects.get(reference_number=reference_number)
            serializer = ParticipantSerializer(participant, many=False)
            return Response(serializer.data, status=status.HTTP_302_FOUND)
        except Participant.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # Update participant information by reference number
    elif request.method == 'POST':
        try:
            participant = Participant.objects.get(reference_number=reference_number)
        except Participant.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ParticipantSerializer(data=request.data)
        if serializer.is_valid():
            cleaned_data = removeNone(serializer.data)
            serializer.update(participant, cleaned_data)
            return Response(cleaned_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Remove participant information by reference number
    elif request.method == 'DELETE':
        try:
            participant = Participant.objects.get(reference_number=reference_number)
        except Participant.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        participant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def removeNone(d):
    return dict((k, v) for k, v in d.items() if v is not None)



