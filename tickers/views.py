from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from tickers.models import Ticker

from rest_framework.decorators import api_view
from datetime import datetime

import requests


@api_view(['GET'])
def polygon_all_tickers(request):
    default_host = 'https://api.polygon.io'
    polygon_url = default_host + '/vX/reference/tickers?limit=500&apiKey='
    apiKey = 'u8arVdihlX_6p_pRuvRUwa94YmI4Zrny'

    url = polygon_url + apiKey

    limit_query_times = 30
    ncount = 0
    next_page_path = ''
    rest = 0
    all_tickers = []

    for t in range(limit_query_times):
        if ncount == 0:
            rep = requests.get(url).json()
            next_page_path = rep['next_page_path']
            all_tickers.extend(rep['results'])
        else:
            url = default_host + next_page_path
            rep = requests.get(url).json()
            all_tickers.extend(rep['results'])
            if rest > 0 and 'next_page_path' in rep:
                next_page_path = rep['next_page_path']
            else:
                break
        print(next_page_path)

        rest = limit_query_times - ncount
        ncount += 1

    for t in all_tickers:

        cik = t['cik'] if 'cik' in t else ''
        composite_figi = t['composite_figi'] if 'composite_figi' in t else ''
        share_class_figi = t['share_class_figi'] if 'share_class_figi' in t else ''

        ticker = Ticker(
            symbol=t['ticker'],
            name =t['name'],
            market = t['market'],
            locale = t['locale'],
            active = t['active'],
            cik = cik,
            composite_figi = composite_figi,
            share_class_figi = share_class_figi,
            currency_name = t['currency_name'],
            last_updated_utc = t['last_updated_utc'],
            created_at=datetime.now().strftime('%Y-%m-%d')
        )

        try:
            ticker.save()
        except:
            pass

    return JsonResponse({'message': 'query all tickers from Polygon.io'},  status=status.HTTP_200_OK)

