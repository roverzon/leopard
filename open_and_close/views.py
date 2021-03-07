from django.http.response import JsonResponse
from rest_framework import status

from open_and_close.models import OpenClose
from open_and_close.serializers import OpenCloseSerializer
from rest_framework.decorators import api_view

from polygon import RESTClient
from datetime import datetime

import pandas as pd


@api_view(['GET'])
def open_and_close_detail_init(request, symbol):
    if request.method == 'GET':

        start_date = request.GET.get('from_')
        end_date = request.GET.get('end_')

        if end_date is None:
            end_date = datetime.now().strftime('%Y-%m-%d')

        dates = pd.bdate_range(start=start_date, end=end_date)

        with RESTClient(auth_key='u8arVdihlX_6p_pRuvRUwa94YmI4Zrny') as client:

            for date in dates:
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

        return JsonResponse({'message': 'Trading Data Save successfully'},  status=status.HTTP_200_OK)


@api_view(['GET'])
def open_and_close_detail(request, symbol):
    if request.method == 'GET':
        open_and_close = OpenClose.objects.all()
        tdate = request.GET.get('tdate')

        if symbol is not None:
            open_and_close = open_and_close.filter(symbol__iexact=symbol, tdate__iexact=tdate)

            open_and_close_serializer = OpenCloseSerializer(open_and_close, many=True)
            return JsonResponse(open_and_close_serializer.data, safe=False, )