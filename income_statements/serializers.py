from rest_framework import serializers
from income_statements.models import Income


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income

        fields = (
            'id',
            'symbol',
            'report_type',
            'fiscal_date_ending',
            'fiscal_year',
            'reported_currency',
            'total_revenue',
            'total_operating_expense',
            'cost_of_revenue',
            'gross_profit',
            'ebit',
            'net_income',
            'research_and_development',
            'effect_of_accounting_charges',
            'income_before_tax',
            'minority_interest',
            'selling_general_administrative',
            'other_non_operating_income',
            'operating_income',
            'other_operating_expense',
            'interest_expense',
            'tax_provision',
            'interest_income',
            'net_interest_income',
            'extraordinary_items',
            'non_recurring',
            'other_items',
            'income_tax_expense',
            'total_other_income_expense',
            'discontinued_operations',
            'net_income_from_continuing_operations',
            'net_income_applicable_to_common_shares',
            'preferred_stock_and_other_adjustments'
        )