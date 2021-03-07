from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from portfolios.models import Portfolio
from portfolios.serializers import PortfolioSerializer

from datetime import datetime

import json

@api_view(['GET'])
def positions_list(request):
    return

@api_view(['POST'])
def position_create(request):
    return
