from rest_framework.serializers import ModelSerializer, SerializerMethodField
from risk_management.risk_type.models import RiskType, RiskTypeField, TEXT, get_default_meta


class RiskTypeFieldSerializer(ModelSerializer):
    meta = SerializerMethodField()
    class Meta:
        model = RiskTypeField
        fields = ('id', 'meta', 'type','label')

    def get_meta(self, field):
        if field.meta:
            return field.meta
        return get_default_meta(field.type)

class RiskTypeListSerializer(ModelSerializer):
    class Meta:
        model = RiskType
        fields = ('id','name')

class RiskTypeDetailSerializer(ModelSerializer):
    fields = RiskTypeFieldSerializer(many=True)
    class Meta:
        model = RiskType
        fields = ('id', 'name', 'fields')




