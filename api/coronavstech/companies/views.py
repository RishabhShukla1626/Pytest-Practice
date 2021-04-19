from rest_framework import viewsets
from .serializers import CompanySerializer
from .models import Companies
from rest_framework.pagination import PageNumberPagination

# Create your views here.


class CompanyViewSet(viewsets.ModelViewSet):

    serializer_class = CompanySerializer
    queryset = Companies.objects.all().order_by("-last_updated")
    pagination_class = PageNumberPagination
