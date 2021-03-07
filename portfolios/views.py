from users.models import CustomUser as User
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from portfolios.models import Portfolio
from portfolios.serializers import PortfolioSerializer

from datetime import datetime

import json


@api_view(['POST'])
def portfolio_create(request):

    if request.method == 'POST':
        body = json.loads(request.body)
        user = User.objects.get(email=body['email'])

        port = Portfolio(
            user=user,
            name=body['name'],
            symbols=body['symbols'],
            weights=body['weights'],
            budgets=body['budgets'],
            total_budget=body['total_budgets'],
            start_date=body['start_date'],
            end_date=body['end_date'],
            created_time= datetime.now().strftime('%Y-%m-%d'),
            updated_time= datetime.now().strftime('%Y-%m-%d')
        )

        try:
            port.save()
        except:
            print("Portfolio Save wrong")

        return JsonResponse(body, status=status.HTTP_200_OK)


@api_view(['GET'])
def portfolio_list(request):
    if request.method == 'GET':
        ports = Portfolio.objects.all()

    portfolio_serializer = PortfolioSerializer(ports, many=True)
    return JsonResponse(portfolio_serializer.data, safe=False, )
