from rest_framework import serializers
from watchlists.models import WatchList


class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList

        fields = (
            'id',
            'name',
            'watchlist_tags',
            'symbol_cnt',
            'created_date',
            'is_default'
        )
