from django.http.response import JsonResponse
from users.models import CustomUser as User
from rest_framework import status
from rest_framework.decorators import api_view
from datetime import datetime
from watchlists.models import WatchList
from watchlists.models import WatchListToSymbol
from watchlists.serializers import WatchListSerializer
import json


@api_view(['GET'])
def watchlist_list(request):
    username = request.GET.get('username', None)
    user_id = User.objects.get(username=username).id
    watchlists = WatchList.objects.filter(user_id=user_id)
    watchlists_serializer = WatchListSerializer(watchlists, many=True)
    return JsonResponse(watchlists_serializer.data, safe=False, status=status.HTTP_200_OK)


@api_view(['POST'])
def watchlist_create(request):
    print(request.body)
    body = json.loads(request.body)
    user = User.objects.get(email=body['email'])
    symbol = body['symbol']

    is_have = 1 if len(WatchList.objects.filter(user_id=user.id)) > 0 else 0

    if is_have > 0:
        try:
            WatchListToSymbol.objects.get(symbol=symbol)
            pass
        except:
            default_watchlist = WatchList.objects.get(user=user, is_default=True)
            default_watchlist.symbol_cnt += 1
            default_watchlist.save(update_fields=['symbol_cnt'])
            watchlistToSymbol = WatchListToSymbol(
                user=user,
                watchlist=default_watchlist,
                symbol=body['symbol']
            )
            watchlistToSymbol.save()
    else:
        watchlist = WatchList(
            user=user,
            watchlist_tags=['default'],
            created_at=datetime.now(),
            updated_at=datetime.now(),
            symbol_cnt=1,
            is_default=True
        )
        watchlist.save()

        default_watchlist = WatchList.objects.get(user=user, is_default=True)
        watchlistToSymbol = WatchListToSymbol(
            user=user,
            watchlist=default_watchlist,
            symbol=body['symbol']
        )
        watchlistToSymbol.save()

    return JsonResponse({"message": "saved successfully"}, status=status.HTTP_200_OK)
