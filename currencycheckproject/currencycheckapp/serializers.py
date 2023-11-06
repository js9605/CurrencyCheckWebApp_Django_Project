from rest_framework import serializers

class CurrencyInputSerializer(serializers.Serializer):
    currencies = serializers.ListField(child=serializers.CharField(), required=True)
