from django.db.models import Count
from rest_framework import permissions, filters
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from drf_api.permissions import OwnerOrReadOnly
from .models import Contact
from .serializers import ContactSerializer


class ContactList(ListCreateAPIView):
    """
    Displays a list of all the reports sent by user
    and their information.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'owner__username',
        'title',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ContactDetail(RetrieveUpdateDestroyAPIView):
    """
    Display contact detail.
    The owner of the report can edit and delete their report here.
    """
    permission_classes = [OwnerOrReadOnly]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
