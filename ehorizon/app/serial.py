# serial.py
from rest_framework import serializers
from .models import (PitchRegistration,GameathonRegistration,WebifyRegistration,MechRegistration,BuildRegistration,ElectricRegistration,MasterRegistration,IPLRegistration,ThiraiRegistration,TalentiaRegistration,Admin
,RisingRegistration,StartupRegistration,IPRRegistration,BusinessRegistration,ProductRegistration,StocksRegistration,BplanRegistration,DetxRegistration)

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
        
class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = "__all__"

class RisingRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RisingRegistration
        fields = "__all__"

class StartupRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StartupRegistration
        fields = "__all__"

class IPRRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPRRegistration
        fields = "__all__"

class BusinessRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessRegistration
        fields = "__all__"

class ProductRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRegistration
        fields = "__all__"

class StocksRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StocksRegistration
        fields = "__all__"

class BplanRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BplanRegistration
        fields = "__all__"

class DetxRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetxRegistration
        fields = "__all__"