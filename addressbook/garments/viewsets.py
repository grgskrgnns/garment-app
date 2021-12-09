# api/viewsets.py

from rest_framework import viewsets
from djongo import models
from rest_framework.permissions import IsAuthenticated
from .models import Garment
from .serializers import GarmentSerializer


class ContactViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    #queryset = Garment.objects.all()
    queryset = Garment.objects.all()
    serializer_class = GarmentSerializer

    
    def get_queryset(self):
        qs = super().get_queryset()

        # Get only contact about current authenticated user
        #qs = qs.filter(user=self.request.user)
        
        # Add search capabilities
        search = self.request.query_params.get("search", None)
        if search and len(search)>=3:
            qs = Garment.objects.filter(            
                models.Q(product_id__contains=search)
                | models.Q(product_description__contains=search)
            )
        else:
            qs = Garment.objects.none()

        return qs
   