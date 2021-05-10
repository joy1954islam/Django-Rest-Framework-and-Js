from rest_framework import serializers
from .models import PersonalInformation


class PersonInformationSerializers(serializers.ModelSerializer):
    class Meta:
        model = PersonalInformation
        fields = '__all__'
