# serial.py
from rest_framework import serializers
from .models import PitchRegistration,GameathonRegistration,WebifyRegistration,MechRegistration,BuildRegistration,ElectricRegistration,MasterRegistration,IPLRegistration,ThiraiRegistration,TalentiaRegistration

class PitchRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PitchRegistration
        fields = "__all__"


class GamethonRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameathonRegistration
        fields = "__all__"

class WebifyRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebifyRegistration
        fields = "__all__"

class BuildRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildRegistration
        fields = "__all__"

class MechRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MechRegistration
        fields = "__all__"


class MasterRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterRegistration
        fields = "__all__"

class ElectricRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectricRegistration
        fields = "__all__"

class IPLRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPLRegistration
        fields = "__all__"

class ThiraiRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThiraiRegistration
        fields = "__all__"

class TalentiaRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TalentiaRegistration
        fields = "__all__"