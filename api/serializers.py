from rest_framework import serializers
from base.models import Item, AuditProgramRepo, RiskRepo

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class AuditProgramRepoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditProgramRepo
        fields = '__all__'

class RiskRepoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskRepo
        fields = '__all__'