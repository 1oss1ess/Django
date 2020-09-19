from rest_framework import generics
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from ..models import ParliamentMembers
from .serializers import ParliamentSerializer


class ParliamentListView(generics.ListAPIView):
    authentication_classes = (TokenAuthentication,)

    serializer_class = ParliamentSerializer

    def get_queryset(self):
        queryset = ParliamentMembers.objects.all()
        selected_with = self.request.query_params.get('pp', None)
        date_of_birth = self.request.query_params.get('dob', None)
        if selected_with is not None:
            queryset = queryset.filter(selected_with__icontains=selected_with)
        if date_of_birth is not None:
            year = date_of_birth[0:4]
            month = date_of_birth[4:6]
            day = date_of_birth[6:]
            date_of_birth = day + '/' + month + '/' + year
            queryset = queryset.filter(date_birth__icontains=date_of_birth)
        return queryset


class ParliamentDetailView(generics.RetrieveAPIView):
    queryset = ParliamentMembers.objects.all()
    serializer_class = ParliamentSerializer


class ParliamentSearchListView(generics.ListAPIView):
    serializer_class = ParliamentSerializer

    def get_queryset(self):
        queryset = ParliamentMembers.objects.all()
        name = self.request.GET.get('q', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset
