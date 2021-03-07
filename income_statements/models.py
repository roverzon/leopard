from django.db import models


class Income(models.Model):
    symbol = models.CharField(max_length=255, blank=False, default='')
    report_type = models.CharField(max_length=255, blank=False, default='')
    fiscal_date_ending = models.DateTimeField()
    fiscal_year = models.CharField(max_length=10)
    reported_currency = models.CharField(max_length=10)
    total_revenue = models.FloatField()
    total_operating_expense = models.FloatField()
    cost_of_revenue = models.FloatField()
    gross_profit = models.FloatField()
    ebit = models.FloatField()
    net_income = models.FloatField()
    research_and_development = models.FloatField()
    effect_of_accounting_charges = models.FloatField()
    income_before_tax = models.FloatField()
    minority_interest = models.FloatField()
    selling_general_administrative = models.FloatField()
    other_non_operating_income = models.FloatField()
    operating_income = models.FloatField()
    other_operating_expense = models.FloatField()
    interest_expense = models.FloatField()
    tax_provision = models.FloatField()
    interest_income = models.FloatField()
    net_interest_income = models.FloatField()
    extraordinary_items = models.FloatField()
    non_recurring = models.FloatField()
    other_items = models.FloatField()
    income_tax_expense = models.FloatField()
    total_other_income_expense = models.FloatField()
    discontinued_operations = models.FloatField()
    net_income_from_continuing_operations = models.FloatField()
    net_income_applicable_to_common_shares = models.FloatField()
    preferred_stock_and_other_adjustments = models.FloatField()

    def to_dict(self):
        return {
            'symbol': self.symbol,
            'report_type': self.report_type,
            'fiscal_date_ending': self.fiscal_date_ending,
            'fiscal_year': self.fiscal_year,
            'reported_currency': self.reported_currency,
            'total_revenue': self.total_revenue,
            'total_operating_expense': self.total_operating_expense,
            'cost_of_revenue': self.cost_of_revenue,
            'gross_profit': self.gross_profit,
            'ebit': self.ebit,
            'net_income': self.net_income,
            'research_and_development': self.research_and_development,
            'effect_of_accounting_charges': self.effect_of_accounting_charges,
            'income_before_tax': self.income_before_tax,
            'minority_interest': self.minority_interest,
            'selling_general_administrative': self.selling_general_administrative,
            'other_non_operating_income': self.other_non_operating_income,
            'operating_income': self.operating_income,
            'other_operating_expense': self.other_operating_expense,
            'interest_expense': self.interest_expense,
            'tax_provision': self.tax_provision,
            'interest_income': self.interest_income,
            'net_interest_income': self.net_interest_income,
            'extraordinary_items': self.extraordinary_items,
            'non_recurring': self.non_recurring,
            'other_items': self.other_items,
            'income_tax_expense': self.income_tax_expense,
            'total_other_income_expense': self.total_other_income_expense,
            'discontinued_operations': self.discontinued_operations,
            'net_income_from_continuing_operations': self.net_income_from_continuing_operations,
            'net_income_applicable_to_common_shares': self.net_income_applicable_to_common_shares,
            'preferred_stock_and_other_adjustments': self.preferred_stock_and_other_adjustments
        }
