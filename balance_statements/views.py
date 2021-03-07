from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from balance_statements.models import BalanceSheet
from balance_statements.serializers import BalanceSheetSerializer
from rest_framework.decorators import api_view

from alpha_vantage.fundamentaldata import FundamentalData
from datetime import datetime
from collections import OrderedDict


@api_view(['GET'])
def balancesheet_list(request):
    if request.method == 'GET':
        balancesheets = BalanceSheet.objects.all()

        symbol = request.GET.get('symbol', None)
        if symbol is not None:
            balancesheets = balancesheets.filter(symbol__icontains=symbol, status=status.HTTP_200_OK)

        balancesheet_serializer = BalanceSheetSerializer(balancesheets, many=True)
        return JsonResponse(balancesheet_serializer.data, safe=False, )


@api_view(['GET'])
def symbol_balancesheet_list(request, symbol):
    if request.method == 'GET':
        balancesheetT = OrderedDict()
        if symbol is not None:
            balancesheets = BalanceSheet.objects.filter(symbol=symbol)
            balancesheetT['fiscal_date_ending'] = [ balancesheet.fiscal_date_ending for balancesheet in balancesheets ]
            balancesheetT['fiscal_year'] = [ balancesheet.fiscal_year for balancesheet in balancesheets ]
            balancesheetT['reported_currency'] = [ balancesheet.reported_currency for balancesheet in balancesheets ]
            balancesheetT['total_assets'] = [ balancesheet.total_assets for balancesheet in balancesheets ]
            balancesheetT['intangible_assets'] = [ balancesheet.intangible_assets for balancesheet in balancesheets ]
            balancesheetT['earning_assets'] = [ balancesheet.earning_assets for balancesheet in balancesheets ]
            balancesheetT['other_current_assets'] = [ balancesheet.other_current_assets for balancesheet in balancesheets ]
            balancesheetT['total_liabilities'] = [ balancesheet.total_liabilities for balancesheet in balancesheets ]
            balancesheetT['total_shareholder_equity'] = [ balancesheet.total_shareholder_equity for balancesheet in balancesheets ]
            balancesheetT['deferred_long_term_liabilities'] = [ balancesheet.deferred_long_term_liabilities for balancesheet in balancesheets ]
            balancesheetT['other_current_liabilities'] = [ balancesheet.other_current_liabilities for balancesheet in balancesheets ]
            balancesheetT['common_stock'] = [ balancesheet.common_stock for balancesheet in balancesheets ]
            balancesheetT['retained_earnings'] = [ balancesheet.retained_earnings for balancesheet in balancesheets ]
            balancesheetT['other_liabilities'] = [ balancesheet.other_liabilities for balancesheet in balancesheets ]
            balancesheetT['goodwill'] = [ balancesheet.goodwill for balancesheet in balancesheets ]
            balancesheetT['other_assets'] = [ balancesheet.other_assets for balancesheet in balancesheets ]
            balancesheetT['cash'] = [ balancesheet.cash for balancesheet in balancesheets ]
            balancesheetT['total_current_liabilities'] = [ balancesheet.total_current_liabilities for balancesheet in balancesheets ]
            balancesheetT['short_term_debt'] = [ balancesheet.short_term_debt for balancesheet in balancesheets ]
            balancesheetT['current_long_term_debt'] = [ balancesheet.current_long_term_debt for balancesheet in balancesheets ]
            balancesheetT['other_shareholder_equity'] = [ balancesheet.other_shareholder_equity for balancesheet in balancesheets ]
            balancesheetT['property_plant_equipment'] = [ balancesheet.property_plant_equipment for balancesheet in balancesheets ]
            balancesheetT['total_current_assets'] = [ balancesheet.total_current_assets for balancesheet in balancesheets ]
            balancesheetT['long_term_investment'] = [ balancesheet.long_term_investment for balancesheet in balancesheets ]
            balancesheetT['net_tangible_assets'] = [ balancesheet.net_tangible_assets for balancesheet in balancesheets ]
            balancesheetT['short_term_investment'] = [ balancesheet.short_term_investment for balancesheet in balancesheets ]
            balancesheetT['net_receivables'] = [ balancesheet.net_receivables for balancesheet in balancesheets ]
            balancesheetT['long_term_debt'] = [ balancesheet.long_term_debt for balancesheet in balancesheets ]
            balancesheetT['inventory'] = [ balancesheet.inventory for balancesheet in balancesheets ]
            balancesheetT['accounts_payable'] = [ balancesheet.accounts_payable for balancesheet in balancesheets ]
            balancesheetT['total_permanent_equity'] = [ balancesheet.total_permanent_equity for balancesheet in balancesheets ]
            balancesheetT['additional_paid_in_capital'] = [ balancesheet.additional_paid_in_capital for balancesheet in balancesheets ]
            balancesheetT['common_stock_total_equity'] = [ balancesheet.common_stock_total_equity for balancesheet in balancesheets ]
            balancesheetT['preferred_stock_total_equity'] = [ balancesheet.preferred_stock_total_equity for balancesheet in balancesheets ]
            balancesheetT['retained_earnings_total_equity'] = [ balancesheet.retained_earnings_total_equity for balancesheet in balancesheets ]
            balancesheetT['treasury_stock'] = [ balancesheet.treasury_stock for balancesheet in balancesheets ]
            balancesheetT['accumulated_amortization'] = [ balancesheet.accumulated_amortization for balancesheet in balancesheets ]
            balancesheetT['other_non_current_assets'] = [ balancesheet.other_non_current_assets for balancesheet in balancesheets ]
            balancesheetT['deferred_long_term_aseet_charges'] = [ balancesheet.deferred_long_term_aseet_charges for balancesheet in balancesheets ]
            balancesheetT['total_non_current_assets'] = [ balancesheet.total_non_current_assets for balancesheet in balancesheets ]
            balancesheetT['capital_lease_obligations'] = [ balancesheet.capital_lease_obligations for balancesheet in balancesheets ]
            balancesheetT['total_long_term_debt'] = [ balancesheet.total_long_term_debt for balancesheet in balancesheets ]
            balancesheetT['other_non_current_liabilities'] = [ balancesheet.other_non_current_liabilities for balancesheet in balancesheets ]
            balancesheetT['deferred_long_term_asset_charges'] = [ balancesheet.deferred_long_term_asset_charges for balancesheet in balancesheets ]
            balancesheetT['total_non_current_liabilities'] = [ balancesheet.total_non_current_liabilities for balancesheet in balancesheets ]
            balancesheetT['negative_goodwill'] = [ balancesheet.negative_goodwill for balancesheet in balancesheets ]
            balancesheetT['warrants'] = [ balancesheet.warrants for balancesheet in balancesheets ]
            balancesheetT['preferred_stock_redeemable'] = [ balancesheet.preferred_stock_redeemable for balancesheet in balancesheets ]
            balancesheetT['capital_surplus'] = [ balancesheet.capital_surplus for balancesheet in balancesheets ]
            balancesheetT['liabilities_and_shareholder_equity'] = [ balancesheet.liabilities_and_shareholder_equity for balancesheet in balancesheets ]
            balancesheetT['cash_and_short_term_investments'] = [ balancesheet.cash_and_short_term_investments for balancesheet in balancesheets ]
            balancesheetT['accumulated_depreciation'] = [ balancesheet.accumulated_depreciation for balancesheet in balancesheets ]
            balancesheetT['common_stock_shares_outstanding'] = [ balancesheet.common_stock_shares_outstanding for balancesheet in balancesheets ]

    return JsonResponse(balancesheetT, safe=False, )


@api_view(['GET'])
def balancesheet_detail(request, pk):
    try:
        balancesheet = BalanceSheet.objects.get(pk=pk)

        if request.method == 'GET':
            balancesheet_serializer = BalanceSheetSerializer(balancesheet)
            return JsonResponse(balancesheet_serializer.data)

    except:
        return JsonResponse({'message': 'The company does not exist'},  status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def balancesheet_init_annual(request):

    if request.method == 'GET':

        symbol = request.GET.get('symbol')

        data = FundamentalData(key='I7WB8M63PERU90OY', output_format='pandas')
        balancesheets, vasymbol = data.get_balance_sheet_annual(symbol=symbol)

        for fical in balancesheets['fiscalDateEnding']:
            balancesheet = balancesheets[balancesheets['fiscalDateEnding'] == fical]

            for col in balancesheet.columns:
                if col not in ['fiscalDateEnding', 'reportedCurrency']:
                    if balancesheet[col].values[0] == 'None':
                        balancesheet[col] = 0.0
                    else:
                        pass
                else:
                    pass

            bs = BalanceSheet(
                symbol=symbol,
                report_type='annualReport',
                fiscal_date_ending= datetime.strptime(balancesheet['fiscalDateEnding'].values[0], '%Y-%m-%d'),
                fiscal_year= balancesheet['fiscalDateEnding'].values[0].split('-')[0],
                reported_currency=balancesheet['reportedCurrency'].values[0],
                total_assets = balancesheet['totalAssets'].values[0],
                intangible_assets = balancesheet['intangibleAssets'].values[0],
                earning_assets = balancesheet['earningAssets'].values[0],
                other_current_assets = balancesheet['otherCurrentAssets'].values[0],
                total_liabilities = balancesheet['totalLiabilities'].values[0],
                total_shareholder_equity = balancesheet['totalShareholderEquity'].values[0],
                deferred_long_term_liabilities = balancesheet['deferredLongTermLiabilities'].values[0],
                other_current_liabilities = balancesheet['otherCurrentLiabilities'].values[0],
                common_stock = balancesheet['commonStock'].values[0],
                retained_earnings = balancesheet['retainedEarnings'].values[0],
                other_liabilities = balancesheet['otherLiabilities'].values[0],
                goodwill = balancesheet['goodwill'].values[0],
                other_assets = balancesheet['otherAssets'].values[0],
                cash = balancesheet['cash'].values[0],
                total_current_liabilities = balancesheet['totalCurrentLiabilities'].values[0],
                short_term_debt = balancesheet['shortTermDebt'].values[0],
                current_long_term_debt = balancesheet['currentLongTermDebt'].values[0],
                other_shareholder_equity = balancesheet['otherShareholderEquity'].values[0],
                property_plant_equipment = balancesheet['propertyPlantEquipment'].values[0],
                total_current_assets = balancesheet['totalCurrentAssets'].values[0],
                long_term_investment = balancesheet['longTermInvestments'].values[0],
                net_tangible_assets = balancesheet['netTangibleAssets'].values[0],
                short_term_investment = balancesheet['shortTermInvestments'].values[0],
                net_receivables = balancesheet['netReceivables'].values[0],
                long_term_debt = balancesheet['longTermDebt'].values[0],
                inventory = balancesheet['inventory'].values[0],
                accounts_payable = balancesheet['accountsPayable'].values[0],
                total_permanent_equity = balancesheet['totalPermanentEquity'].values[0],
                additional_paid_in_capital = balancesheet['additionalPaidInCapital'].values[0],
                common_stock_total_equity = balancesheet['commonStockTotalEquity'].values[0],
                preferred_stock_total_equity = balancesheet['preferredStockTotalEquity'].values[0],
                retained_earnings_total_equity = balancesheet['retainedEarningsTotalEquity'].values[0],
                treasury_stock = balancesheet['treasuryStock'].values[0],
                accumulated_amortization = balancesheet['accumulatedAmortization'].values[0],
                other_non_current_assets = balancesheet['otherNonCurrrentAssets'].values[0],
                deferred_long_term_asset_charges = balancesheet['deferredLongTermAssetCharges'].values[0],
                total_non_current_assets = balancesheet['totalNonCurrentAssets'].values[0],
                capital_lease_obligations = balancesheet['capitalLeaseObligations'].values[0],
                total_long_term_debt = balancesheet['totalLongTermDebt'].values[0],
                other_non_current_liabilities = balancesheet['otherNonCurrentLiabilities'].values[0],
                total_non_current_liabilities = balancesheet['totalNonCurrentLiabilities'].values[0],
                negative_goodwill = balancesheet['negativeGoodwill'].values[0],
                warrants = balancesheet['warrants'].values[0],
                preferred_stock_redeemable = balancesheet['preferredStockRedeemable'].values[0],
                capital_surplus = balancesheet['capitalSurplus'].values[0],
                liabilities_and_shareholder_equity = balancesheet['liabilitiesAndShareholderEquity'].values[0],
                cash_and_short_term_investments = balancesheet['cashAndShortTermInvestments'].values[0],
                accumulated_depreciation = balancesheet['accumulatedDepreciation'].values[0],
                common_stock_shares_outstanding = balancesheet['commonStockSharesOutstanding'].values[0],
                
            )

            bs.save()

        return JsonResponse({'message': 'Annualy BalanceSheet Data Save successlly'},  status=status.HTTP_200_OK)


@api_view(['GET'])
def balancesheet_init_quarterly(request):

    if request.method == 'GET':
        symbol = request.GET.get('symbol')

        data = FundamentalData(key='I7WB8M63PERU90OY', output_format='pandas')
        qbalancesheets, vasymbol = data.get_balance_sheet_quarterly(symbol=symbol)

        for fical in qbalancesheets['fiscalDateEnding']:
            balancesheet = qbalancesheets[qbalancesheets['fiscalDateEnding'] == fical]

            for col in balancesheet.columns:
                if col not in ['fiscalDateEnding', 'reportedCurrency']:
                    if balancesheet[col].values[0] == 'None':
                        balancesheet[col] = 0.0
                    else:
                        pass
                else:
                    pass
            bs = BalanceSheet(
                    symbol=symbol,
                    report_type='annualReport',
                    fiscal_date_ending= datetime.strptime(balancesheet['fiscalDateEnding'].values[0], '%Y-%m-%d'),
                    fiscal_year=balancesheet['fiscalDateEnding'].values[0].split('-')[0],
                    reported_currency=balancesheet['reportedCurrency'].values[0],
                    total_assets = balancesheet['totalAssets'].values[0],
                    intangible_assets = balancesheet['intangibleAssets'].values[0],
                    earning_assets = balancesheet['earningAssets'].values[0],
                    other_current_assets = balancesheet['otherCurrentAssets'].values[0],
                    total_liabilities = balancesheet['totalLiabilities'].values[0],
                    total_shareholder_equity = balancesheet['totalShareholderEquity'].values[0],
                    deferred_long_term_liabilities = balancesheet['deferredLongTermLiabilities'].values[0],
                    other_current_liabilities = balancesheet['otherCurrentLiabilities'].values[0],
                    common_stock = balancesheet['commonStock'].values[0],
                    retained_earnings = balancesheet['retainedEarnings'].values[0],
                    other_liabilities = balancesheet['otherLiabilities'].values[0],
                    goodwill = balancesheet['goodwill'].values[0],
                    other_assets = balancesheet['otherAssets'].values[0],
                    cash = balancesheet['cash'].values[0],
                    total_current_liabilities = balancesheet['totalCurrentLiabilities'].values[0],
                    short_term_debt = balancesheet['shortTermDebt'].values[0],
                    current_long_term_debt = balancesheet['currentLongTermDebt'].values[0],
                    other_shareholder_equity = balancesheet['otherShareholderEquity'].values[0],
                    property_plant_equipment = balancesheet['propertyPlantEquipment'].values[0],
                    total_current_assets = balancesheet['totalCurrentAssets'].values[0],
                    long_term_investment = balancesheet['longTermInvestments'].values[0],
                    net_tangible_assets = balancesheet['netTangibleAssets'].values[0],
                    short_term_investment = balancesheet['shortTermInvestments'].values[0],
                    net_receivables = balancesheet['netReceivables'].values[0],
                    long_term_debt = balancesheet['longTermDebt'].values[0],
                    inventory = balancesheet['inventory'].values[0],
                    accounts_payable = balancesheet['accountsPayable'].values[0],
                    total_permanent_equity = balancesheet['totalPermanentEquity'].values[0],
                    additional_paid_in_capital = balancesheet['additionalPaidInCapital'].values[0],
                    common_stock_total_equity = balancesheet['commonStockTotalEquity'].values[0],
                    preferred_stock_total_equity = balancesheet['preferredStockTotalEquity'].values[0],
                    retained_earnings_total_equity = balancesheet['retainedEarningsTotalEquity'].values[0],
                    treasury_stock = balancesheet['treasuryStock'].values[0],
                    accumulated_amortization = balancesheet['accumulatedAmortization'].values[0],
                    other_non_current_assets = balancesheet['otherNonCurrrentAssets'].values[0],
                    deferred_long_term_asst_charges = balancesheet['deferredLongTermAssetCharges'].values[0],
                    total_non_current_assets = balancesheet['totalNonCurrentAssets'].values[0],
                    capital_lease_obligations = balancesheet['capitalLeaseObligations'].values[0],
                    total_long_term_debt = balancesheet['totalLongTermDebt'].values[0],
                    other_non_current_liabilities = balancesheet['otherNonCurrentLiabilities'].values[0],
                    total_non_current_liabilities = balancesheet['totalNonCurrentLiabilities'].values[0],
                    negative_goodwill = balancesheet['negativeGoodwill'].values[0],
                    warrants = balancesheet['warrants'].values[0],
                    preferred_stock_redeemable = balancesheet['preferredStockRedeemable'].values[0],
                    capital_surplus = balancesheet['capitalSurplus'].values[0],
                    liabilities_and_shareholder_equity = balancesheet['liabilitiesAndShareholderEquity'].values[0],
                    cash_and_short_term_investments = balancesheet['cashAndShortTermInvestments'].values[0],
                    accumulated_depreciation = balancesheet['accumulatedDepreciation'].values[0],
                    common_stock_shares_outstanding = balancesheet['commonStockSharesOutstanding'].values[0],

            )

            bs.save()

        return JsonResponse({'message': 'Quarterly BalanceShett Data Save successlly'},  status=status.HTTP_200_OK)
