from rest_framework import serializers

from myapp.models import DrfNews


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrfNews
        fields = '__all__'
