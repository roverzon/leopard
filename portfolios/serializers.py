from rest_framework import serializers
from portfolios.models import Portfolio


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio

        fields = (
            'id',
            'name',
            'symbols',
            'weights',
            'budgets',
            'total_budget',
            'start_date',
            'end_date'
        )
