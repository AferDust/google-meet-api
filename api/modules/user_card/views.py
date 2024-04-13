from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from api.models import Card
from .serializers import CardSerializer


class CardListCreateView(generics.ListCreateAPIView):
    serializer_class = CardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Filter the queryset to only include cards owned by the logged-in user
        return Card.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Assign the logged-in user as the owner of the card
        serializer.save(user=self.request.user)


class CardDestroyView(generics.DestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Ensure that a user can only delete their own cards
        return Card.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        card = get_object_or_404(Card, pk=kwargs['pk'])
        return super().delete(request, *args, **kwargs)
