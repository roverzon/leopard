from rest_framework import serializers
from open_and_close.models import OpenClose


class OpenCloseSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenClose

        fields = (
            'id',
            'symbol',
            'tdate',
            'open',
            'close',
            'high',
            'volume',
            'afterMarket',
            'preMarket'
        )