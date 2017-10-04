from rest_framework import serializers
from snippets.models import Statistics


class StatisticsSerializer(serializers.Serializer):
    externalId = serializers.CharField(required=False, allow_blank=True, max_length=100)
    agentId = serializers.CharField(required=False, allow_blank=True, max_length=100)
    startDate = serializers.DateField()
    numberOfEmails = serializers.IntegerField()
    numberOfCalls = serializers.IntegerField()
    averageDuration = serializers.IntegerField()
    averageHoldingDuration = serializers.IntegerField()
    isResolved = serializers.BooleanField(default=False)
    nps = serializers.IntegerField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Statistics.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.externalId = validated_data.get('externalId', instance.externalId)
        instance.agentId = validated_data.get('agentId', instance.agentId)
        instance.startDate = validated_data.get('startDate', instance.startDate)
        instance.numberOfEmails = validated_data.get('numberOfEmails', instance.numberOfEmails)
        instance.numberOfCalls = validated_data.get('numberOfCalls', instance.numberOfCalls)
        instance.averageDuration = validated_data.get('averageDuration', instance.averageDuration)
        instance.averageHoldingDuration=validated_data.get('averageHoldingDuration',instance.averageHoldingDuration)
        instance.isResolved = validated_data.get('isResolved', instance.isResolved)
        instance.nps = validated_data.get('nps', instance.nps)
        instance.save()
        return instance