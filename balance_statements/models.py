from django.db import models


class BalanceSheet(models.Model):
    symbol = models.CharField(max_length=10, blank=False, default='')
    report_type = models.CharField(max_length=255, blank=False, default='')
    fiscal_date_ending = models.DateTimeField(default='1900-01-01')
    fiscal_year = models.CharField(max_length=10,default='1900-01-01')
    reported_currency = models.CharField(max_length=255, blank=False, default='USD')
    total_assets = models.FloatField(default=0.0)
    intangible_assets = models.FloatField(default=0.0)
    earning_assets = models.FloatField(default=0.0)
    other_current_assets = models.FloatField(default=0.0)
    total_liabilities = models.FloatField(default=0.0)
    total_shareholder_equity = models.FloatField(default=0.0)
    deferred_long_term_liabilities = models.FloatField(default=0.0)
    other_current_liabilities = models.FloatField(default=0.0)
    common_stock = models.FloatField(default=0.0)
    retained_earnings = models.FloatField(default=0.0)
    other_liabilities = models.FloatField(default=0.0)
    goodwill = models.FloatField(default=0.0)
    other_assets = models.FloatField(default=0.0)
    cash = models.FloatField(default=0.0)
    total_current_liabilities = models.FloatField(default=0.0)
    short_term_debt = models.FloatField(default=0.0)
    current_long_term_debt = models.FloatField(default=0.0)
    other_shareholder_equity = models.FloatField(default=0.0)
    property_plant_equipment = models.FloatField(default=0.0)
    total_current_assets = models.FloatField(default=0.0)
    long_term_investment = models.FloatField(default=0.0)
    net_tangible_assets = models.FloatField(default=0.0)
    short_term_investment = models.FloatField(default=0.0)
    net_receivables = models.FloatField(default=0.0)
    long_term_debt = models.FloatField(default=0.0)
    inventory = models.FloatField(default=0.0)
    accounts_payable = models.FloatField(default=0.0)
    total_permanent_equity = models.FloatField(default=0.0)
    additional_paid_in_capital = models.FloatField(default=0.0)
    common_stock_total_equity = models.FloatField(default=0.0)
    preferred_stock_total_equity = models.FloatField(default=0.0)
    retained_earnings_total_equity = models.FloatField(default=0.0)
    treasury_stock = models.FloatField(default=0.0)
    accumulated_amortization = models.FloatField(default=0.0)
    other_non_current_assets = models.FloatField(default=0.0)
    deferred_long_term_aseet_charges = models.FloatField(default=0.0)
    total_non_current_assets = models.FloatField(default=0.0)
    capital_lease_obligations = models.FloatField(default=0.0)
    total_long_term_debt = models.FloatField(default=0.0)
    other_non_current_liabilities = models.FloatField(default=0.0)
    deferred_long_term_asset_charges = models.FloatField(default=0.0)
    total_non_current_liabilities = models.FloatField(default=0.0)
    negative_goodwill = models.FloatField(default=0.0)
    warrants = models.FloatField(default=0.0)
    preferred_stock_redeemable = models.FloatField(default=0.0)
    capital_surplus = models.FloatField(default=0.0)
    liabilities_and_shareholder_equity = models.FloatField(default=0.0)
    cash_and_short_term_investments = models.FloatField(default=0.0)
    accumulated_depreciation = models.FloatField(default=0.0)
    common_stock_shares_outstanding = models.FloatField(default=0.0)

    def to_dict(self):
        return {'symbol':self.symbol,
                'report_type':self.report_type,
                'fiscal_date_ending':self.fiscal_date_ending,
                'reported_currency':self.reported_currency,
                'total_assets':self.total_assets,
                'intangible_assets':self.intangible_assets,
                'earning_assets':self.earning_assets,
                'other_current_assets':self.other_current_assets,
                'total_liabilities':self.total_liabilities,
                'total_shareholder_equity':self.total_shareholder_equity,
                'deferred_long_term_liabilities':self.deferred_long_term_liabilities,
                'other_current_liabilities':self.other_current_liabilities,
                'common_stock':self.common_stock,
                'retained_earnings':self.retained_earnings,
                'other_liabilities':self.other_liabilities,
                'goodwill':self.goodwill,
                'other_assets':self.other_assets,
                'cash':self.cash,
                'total_current_liabilities':self.total_current_liabilities,
                'short_term_debt':self.short_term_debt,
                'current_long_term_debt':self.current_long_term_debt,
                'other_shareholder_equity':self.other_shareholder_equity,
                'property_plant_equipment':self.property_plant_equipment,
                'total_current_assets':self.total_current_assets,
                'long_term_investment':self.long_term_investment,
                'net_tangible_assets':self.net_tangible_assets,
                'short_term_investment':self.short_term_investment,
                'net_receivables':self.net_receivables,
                'long_term_debt':self.long_term_debt,
                'inventory':self.inventory,
                'accounts_payable':self.accounts_payable,
                'total_permanent_equity':self.total_permanent_equity,
                'additional_paid_in_capital':self.additional_paid_in_capital,
                'common_stock_total_equity':self.common_stock_total_equity,
                'preferred_stock_total_equity':self.preferred_stock_total_equity,
                'retained_earnings_total_equity':self.retained_earnings_total_equity,
                'treasury_stock':self.treasury_stock,
                'accumulated_amortization':self.accumulated_amortization,
                'other_non_current_assets':self.other_non_current_assets,
                'deferred_long_term_aseet_charges':self.deferred_long_term_aseet_charges,
                'total_non_current_assets':self.total_non_current_assets,
                'capital_lease_obligations':self.capital_lease_obligations,
                'total_long_term_debt':self.total_long_term_debt,
                'other_non_current_liabilities':self.other_non_current_liabilities,
                'deferred_long_term_asset_charges':self.deferred_long_term_asset_charges,
                'total_non_current_liabilities':self.total_non_current_liabilities,
                'negative_goodwill':self.negative_goodwill,
                'warrants':self.warrants,
                'preferred_stock_redeemable':self.preferred_stock_redeemable,
                'capital_surplus':self.capital_surplus,
                'liabilities_and_shareholder_equity':self.liabilities_and_shareholder_equity,
                'cash_and_short_term_investments':self.cash_and_short_term_investments,
                'accumulated_depreciation':self.accumulated_depreciation,
                'common_stock_shares_outstanding':self.common_stock_shares_outstanding
        }

