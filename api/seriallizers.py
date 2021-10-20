from api.models import Quotes
from rest_framework import serializers


class QuotesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quotes
        fields = ["meta_data", "data"]
