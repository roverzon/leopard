from django.http.response import JsonResponse
from rest_framework import status

from overviews.models import Overview
from tickers.models import Ticker
from open_and_close.models import OpenClose
from overviews.serializers import OverviewSerializer
from rest_framework.decorators import api_view
from polygon import RESTClient

from alpha_vantage.fundamentaldata import FundamentalData
from datetime import datetime


@api_view(['GET'])
def overview_list(request):
    if request.method == 'GET':
        companies = Overview.objects.all()

        symbol = request.GET.get('symbol', None)
        if symbol is not None:
            companies = companies.filter(symbol__icontains=symbol, status=status.HTTP_200_OK)

        companies_serializer = OverviewSerializer(companies, many=True)
        return JsonResponse(companies_serializer.data, safe=False, )


@api_view(['GET'])
def overview_detail(request, symbol):
    try:
        company = Overview.objects.get(symbol=symbol)

        if request.method == 'GET':
            company_serializer = OverviewSerializer(company)
            return JsonResponse(company_serializer.data)

    except:
        return JsonResponse({'message': 'The company does not exist'},  status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def overview_init(request):

    if request.method == 'GET':

        symbol = request.GET.get('symbol')

        data = FundamentalData(key='I7WB8M63PERU90OY', output_format='pandas')
        company_overview, meta_data = data.get_company_overview(symbol=symbol)

        num_cols = ['EBITDA', 'Beta', 'PERatio',
                    'PEGRatio', 'BookValue', 'DividendPerShare',
                    'DividendYield', 'Beta', 'EPS']
        for col in num_cols:
            if company_overview[col].values[0] == 'None':
                company_overview[col] = 0.0
            else:
                pass

        date_cols = ['DividendDate', 'ExDividendDate', 'LastSplitDate']

        for col in date_cols:
            if company_overview[col].values[0] == 'None':
                company_overview[col] = '1901-01-01'
            else:
                pass

        co = Overview(
            tid=datetime.now().strftime('%Y-%m-%d') + '_' + symbol,
            symbol=company_overview['Symbol'].values[0],
            asset_type=company_overview['AssetType'].values[0],
            name=company_overview['Name'].values[0],
            exchange=company_overview['Exchange'].values[0],
            currency=company_overview['Currency'].values[0],
            sector=company_overview['Sector'].values[0],
            industry=company_overview['Industry'].values[0],
            full_time_employees=company_overview['FullTimeEmployees'].values[0],
            fiscal_year_end=company_overview['FiscalYearEnd'].values[0],
            latest_quarter=company_overview['LatestQuarter'].values[0],
            market_capitalization=company_overview['MarketCapitalization'].values[0],
            ebitda=company_overview['EBITDA'].values[0],
            pe_ratio=company_overview['PERatio'].values[0],
            peg_ratio=company_overview['PEGRatio'].values[0],
            book_value=company_overview['BookValue'].values[0],
            dividend_per_share=company_overview['DividendPerShare'].values[0],
            dividend_yield=company_overview['DividendYield'].values[0],
            eps=company_overview['EPS'].values[0],
            revenue_per_share_ttm=company_overview['RevenuePerShareTTM'].values[0],
            profit_margin=company_overview['ProfitMargin'].values[0],
            operating_margin_ttm=company_overview['OperatingMarginTTM'].values[0],
            return_on_assets_ttm=company_overview['ReturnOnAssetsTTM'].values[0],
            return_on_equity_ttm=company_overview['ReturnOnEquityTTM'].values[0],
            revenue_ttm=company_overview['RevenueTTM'].values[0],
            gross_profit_ttm=company_overview['GrossProfitTTM'].values[0],
            diluted_eps_ttm=company_overview['DilutedEPSTTM'].values[0],
            quarterly_earning_growth_yoy=company_overview['QuarterlyEarningsGrowthYOY'].values[0],
            quarterly_revenue_growth_yoy=company_overview['QuarterlyRevenueGrowthYOY'].values[0],
            analyst_target_price=company_overview['AnalystTargetPrice'].values[0],
            trailing_pe=company_overview['TrailingPE'].values[0],
            forward_pe=company_overview['ForwardPE'].values[0],
            price_to_sales_ratio_ttm=company_overview['PriceToSalesRatioTTM'].values[0],
            price_to_book_ratio=company_overview['PriceToBookRatio'].values[0],
            ev_to_revenue=company_overview['EVToRevenue'].values[0],
            ev_to_ebitda=company_overview['EVToEBITDA'].values[0],
            beta=company_overview['Beta'].values[0],
            p52_week_high=company_overview['52WeekHigh'].values[0],
            p52_week_low=company_overview['52WeekLow'].values[0],
            p50_day_moving_average=company_overview['50DayMovingAverage'].values[0],
            p200_day_moving_average=company_overview['200DayMovingAverage'].values[0],
            shares_outstanding=company_overview['SharesOutstanding'].values[0],
            short_ratio=company_overview['ShortRatio'].values[0],
            short_percent_outstanding=company_overview['ShortPercentOutstanding'].values[0],
            short_percent_float=company_overview['ShortPercentFloat'].values[0],
            percent_insiders=company_overview['PercentInsiders'].values[0],
            percent_institutions=company_overview['PercentInstitutions'].values[0],
            forword_annual_dividend_rate=company_overview['ForwardAnnualDividendRate'].values[0],
            forword_annual_dividend_yield=company_overview['ForwardAnnualDividendYield'].values[0],
            payout_ratio=company_overview['PayoutRatio'].values[0],
            dividend_date=company_overview['DividendDate'].values[0],
            exdividend_date=company_overview['ExDividendDate'].values[0],
            last_split_factor=company_overview['LastSplitFactor'].values[0],
            last_split_date=company_overview['LastSplitDate'].values[0]
        )

        co.save()

        return JsonResponse({'message': 'save successflly'},  status=status.HTTP_200_OK)


@api_view(['GET'])
def overview_init_from_polygon(request):
    if request.method == 'GET':
        tickers = Ticker.objects.all()
        overviews = []

        for ticker in tickers:
            try:
                data = FundamentalData(key='I7WB8M63PERU90OY', output_format='pandas')
                symbol = ticker.symbol
                company_overview, meta_data = data.get_company_overview(symbol=symbol)
                num_cols = ['EBITDA', 'Beta', 'PERatio',
                                'PEGRatio', 'BookValue', 'DividendPerShare',
                                'DividendYield', 'Beta', 'EPS']

                for col in num_cols:
                    if company_overview[col].values[0] == 'None':
                        company_overview[col] = 0.0
                    else:
                        pass

                date_cols = ['DividendDate', 'ExDividendDate', 'LastSplitDate']

                for col in date_cols:
                    if company_overview[col].values[0] == 'None':
                        company_overview[col] = '1901-01-01'
                    else:
                        pass
                overviews.append(company_overview)
            except:
                print(ticker)
                pass

        for company_overview in overviews:
            co = Overview(
                    tid=datetime.now().strftime('%Y-%m-%d') + '_' + company_overview['Symbol'].values[0],
                    symbol=company_overview['Symbol'].values[0],
                    asset_type=company_overview['AssetType'].values[0],
                    name=company_overview['Name'].values[0],
                    exchange=company_overview['Exchange'].values[0],
                    currency=company_overview['Currency'].values[0],
                    sector=company_overview['Sector'].values[0],
                    industry=company_overview['Industry'].values[0],
                    full_time_employees=company_overview['FullTimeEmployees'].values[0],
                    fiscal_year_end=company_overview['FiscalYearEnd'].values[0],
                    latest_quarter=company_overview['LatestQuarter'].values[0],
                    market_capitalization=company_overview['MarketCapitalization'].values[0],
                    ebitda=company_overview['EBITDA'].values[0],
                    pe_ratio=company_overview['PERatio'].values[0],
                    peg_ratio=company_overview['PEGRatio'].values[0],
                    book_value=company_overview['BookValue'].values[0],
                    dividend_per_share=company_overview['DividendPerShare'].values[0],
                    dividend_yield=company_overview['DividendYield'].values[0],
                    eps=company_overview['EPS'].values[0],
                    revenue_per_share_ttm=company_overview['RevenuePerShareTTM'].values[0],
                    profit_margin=company_overview['ProfitMargin'].values[0],
                    operating_margin_ttm=company_overview['OperatingMarginTTM'].values[0],
                    return_on_assets_ttm=company_overview['ReturnOnAssetsTTM'].values[0],
                    return_on_equity_ttm=company_overview['ReturnOnEquityTTM'].values[0],
                    revenue_ttm=company_overview['RevenueTTM'].values[0],
                    gross_profit_ttm=company_overview['GrossProfitTTM'].values[0],
                    diluted_eps_ttm=company_overview['DilutedEPSTTM'].values[0],
                    quarterly_earning_growth_yoy=company_overview['QuarterlyEarningsGrowthYOY'].values[0],
                    quarterly_revenue_growth_yoy=company_overview['QuarterlyRevenueGrowthYOY'].values[0],
                    analyst_target_price=company_overview['AnalystTargetPrice'].values[0],
                    trailing_pe=company_overview['TrailingPE'].values[0],
                    forward_pe=company_overview['ForwardPE'].values[0],
                    price_to_sales_ratio_ttm=company_overview['PriceToSalesRatioTTM'].values[0],
                    price_to_book_ratio=company_overview['PriceToBookRatio'].values[0],
                    ev_to_revenue=company_overview['EVToRevenue'].values[0],
                    ev_to_ebitda=company_overview['EVToEBITDA'].values[0],
                    beta=company_overview['Beta'].values[0],
                    p52_week_high=company_overview['52WeekHigh'].values[0],
                    p52_week_low=company_overview['52WeekLow'].values[0],
                    p50_day_moving_average=company_overview['50DayMovingAverage'].values[0],
                    p200_day_moving_average=company_overview['200DayMovingAverage'].values[0],
                    shares_outstanding=company_overview['SharesOutstanding'].values[0],
                    short_ratio=company_overview['ShortRatio'].values[0],
                    short_percent_outstanding=company_overview['ShortPercentOutstanding'].values[0],
                    short_percent_float=company_overview['ShortPercentFloat'].values[0],
                    percent_insiders=company_overview['PercentInsiders'].values[0],
                    percent_institutions=company_overview['PercentInstitutions'].values[0],
                    forword_annual_dividend_rate=company_overview['ForwardAnnualDividendRate'].values[0],
                    forword_annual_dividend_yield=company_overview['ForwardAnnualDividendYield'].values[0],
                    payout_ratio=company_overview['PayoutRatio'].values[0],
                    dividend_date=company_overview['DividendDate'].values[0],
                    exdividend_date=company_overview['ExDividendDate'].values[0],
                    last_split_factor=company_overview['LastSplitFactor'].values[0],
                    last_split_date=company_overview['LastSplitDate'].values[0]
            )

            co.save()

        return JsonResponse({'message': 'save successflly'},  status=status.HTTP_200_OK)



@api_view(['GET'])
def overview_all(request, symbol):

    if request.method == 'GET':
        data = FundamentalData(key='I7WB8M63PERU90OY', output_format='pandas')
        company_overview, meta_data = data.get_company_overview(symbol=symbol)

        num_cols = ['EBITDA', 'Beta', 'PERatio',
                    'PEGRatio', 'BookValue', 'DividendPerShare',
                    'DividendYield', 'Beta', 'EPS']
        for col in num_cols:
            if company_overview[col].values[0] == 'None':
                company_overview[col] = 0.0
            else:
                pass

        date_cols = ['DividendDate', 'ExDividendDate', 'LastSplitDate']

        for col in date_cols:
            if company_overview[col].values[0] == 'None':
                company_overview[col] = '1901-01-01'
            else:
                pass

        co = Overview(
            tid=datetime.now().strftime('%Y-%m-%d') + '_' + symbol,
            symbol=company_overview['Symbol'].values[0],
            asset_type=company_overview['AssetType'].values[0],
            name=company_overview['Name'].values[0],
            exchange=company_overview['Exchange'].values[0],
            currency=company_overview['Currency'].values[0],
            sector=company_overview['Sector'].values[0],
            industry=company_overview['Industry'].values[0],
            full_time_employees=company_overview['FullTimeEmployees'].values[0],
            fiscal_year_end=company_overview['FiscalYearEnd'].values[0],
            latest_quarter=company_overview['LatestQuarter'].values[0],
            market_capitalization=company_overview['MarketCapitalization'].values[0],
            ebitda=company_overview['EBITDA'].values[0],
            pe_ratio=company_overview['PERatio'].values[0],
            peg_ratio=company_overview['PEGRatio'].values[0],
            book_value=company_overview['BookValue'].values[0],
            dividend_per_share=company_overview['DividendPerShare'].values[0],
            dividend_yield=company_overview['DividendYield'].values[0],
            eps=company_overview['EPS'].values[0],
            revenue_per_share_ttm=company_overview['RevenuePerShareTTM'].values[0],
            profit_margin=company_overview['ProfitMargin'].values[0],
            operating_margin_ttm=company_overview['OperatingMarginTTM'].values[0],
            return_on_assets_ttm=company_overview['ReturnOnAssetsTTM'].values[0],
            return_on_equity_ttm=company_overview['ReturnOnEquityTTM'].values[0],
            revenue_ttm=company_overview['RevenueTTM'].values[0],
            gross_profit_ttm=company_overview['GrossProfitTTM'].values[0],
            diluted_eps_ttm=company_overview['DilutedEPSTTM'].values[0],
            quarterly_earning_growth_yoy=company_overview['QuarterlyEarningsGrowthYOY'].values[0],
            quarterly_revenue_growth_yoy=company_overview['QuarterlyRevenueGrowthYOY'].values[0],
            analyst_target_price=company_overview['AnalystTargetPrice'].values[0],
            trailing_pe=company_overview['TrailingPE'].values[0],
            forward_pe=company_overview['ForwardPE'].values[0],
            price_to_sales_ratio_ttm=company_overview['PriceToSalesRatioTTM'].values[0],
            price_to_book_ratio=company_overview['PriceToBookRatio'].values[0],
            ev_to_revenue=company_overview['EVToRevenue'].values[0],
            ev_to_ebitda=company_overview['EVToEBITDA'].values[0],
            beta=company_overview['Beta'].values[0],
            p52_week_high=company_overview['52WeekHigh'].values[0],
            p52_week_low=company_overview['52WeekLow'].values[0],
            p50_day_moving_average=company_overview['50DayMovingAverage'].values[0],
            p200_day_moving_average=company_overview['200DayMovingAverage'].values[0],
            shares_outstanding=company_overview['SharesOutstanding'].values[0],
            short_ratio=company_overview['ShortRatio'].values[0],
            short_percent_outstanding=company_overview['ShortPercentOutstanding'].values[0],
            short_percent_float=company_overview['ShortPercentFloat'].values[0],
            percent_insiders=company_overview['PercentInsiders'].values[0],
            percent_institutions=company_overview['PercentInstitutions'].values[0],
            forword_annual_dividend_rate=company_overview['ForwardAnnualDividendRate'].values[0],
            forword_annual_dividend_yield=company_overview['ForwardAnnualDividendYield'].values[0],
            payout_ratio=company_overview['PayoutRatio'].values[0],
            dividend_date=company_overview['DividendDate'].values[0],
            exdividend_date=company_overview['ExDividendDate'].values[0],
            last_split_factor=company_overview['LastSplitFactor'].values[0],
            last_split_date=company_overview['LastSplitDate'].values[0]
        )

        try:
            co.save()
        except:
            pass

        start_date = request.GET.get('from_')

        end_date = request.GET.get('end_')

        if end_date is None:
            end_date = datetime.now().strftime('%Y-%m-%d')

        dates = pd.bdate_range(start=start_date, end=end_date)

        with RESTClient(auth_key='u8arVdihlX_6p_pRuvRUwa94YmI4Zrny') as client:

            for date in dates:
                try:
                    rep = client.stocks_equities_daily_open_close(symbol=symbol, date=date.strftime('%Y-%m-%d'))
                    if rep.symbol != '':
                        openAndClose = OpenClose(
                            tid=rep.from_ + '_' + rep.symbol,
                            symbol=symbol,
                            tdate=datetime.strptime(rep.from_, '%Y-%m-%d'),
                            open=rep.open,
                            high=rep.high,
                            low=rep.low,
                            close=rep.close,
                            afterHours=rep.after_hours,
                            preMarket=rep.preMarket,
                            volumne=rep.volume
                        )
                        try:
                            openAndClose.save()
                        except:
                            pass
                    else:
                        pass
                except:
                    pass

    return JsonResponse({'message': 'save successflly'},  status=status.HTTP_200_OK)
