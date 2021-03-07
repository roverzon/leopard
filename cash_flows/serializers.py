from rest_framework import serializers
from cash_flows.models import CashFlow


class CashFlowSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashFlow

        fields = (
            'id',
            'symbol',
            'report_type',
            'reported_currency',
            'fiscal_date_ending',
            'investments',
            'change_in_liabilities',
            'cashflow_from_investment',
            'other_cashflow_from_investment',
            'net_borrowings',
            'cashflow_from_financing',
            'other_cashflow_from_financing',
            'change_in_operating_activities',
            'net_income',
            'change_in_cash',
            'operating_cashflow',
            'other_operating_cashflow',
            'depreciation',
            'dividend_payout',
            'stock_sale_and_purchase',
            'change_in_inventory',
            'change_in_account_receivables',
            'change_in_net_income',
            'capital_expenditures',
            'change_in_receivables',
            'change_in_exchange_rate',
            'change_in_cash_and_cash_equivalents'
        )