from rest_framework import serializers
from .models import NumbersSum


class NumbersSumSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    number_one = serializers.IntegerField()
    number_two = serializers.IntegerField()
    number_sum = serializers.IntegerField(required=False)

    def create(self, validated_data):
        return NumbersSum.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.number_sum = validated_data.get(
            "number_sum",
            instance.number_sum,
        )
        instance.save()
        return instance
