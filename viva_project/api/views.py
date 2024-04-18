from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MatchSerializer
from base.models import Match

class MatchView(APIView):
    def post(self, request):
        serializer = MatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        matches = Match.objects.all()
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)

# class JournalEntryViewSet(viewsets.ModelViewSet):
#     queryset = JournalEntry.objects.all()
#     serializer_class = JournalEntrySerializer