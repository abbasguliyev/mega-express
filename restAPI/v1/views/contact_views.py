from rest_framework import status, generics
from rest_framework.response import Response
from contact.models import Contact

from restAPI.v1.serializers.contact_serializers import ContactSerializer

class ContactListCreateAPIView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer