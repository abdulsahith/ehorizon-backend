from django.contrib import admin
from .models import (
    PitchRegistration,
    GameathonRegistration,
    BuildRegistration,
    WebifyRegistration,
    ElectricRegistration,
    IPLRegistration,
    MasterRegistration,
    MechRegistration,
    ThiraiRegistration,
    TalentiaRegistration,
)
# Register your models here.

admin.site.register(PitchRegistration)
admin.site.register(GameathonRegistration)
admin.site.register(BuildRegistration)
admin.site.register(WebifyRegistration)
admin.site.register(ElectricRegistration)
admin.site.register(IPLRegistration)
admin.site.register(MasterRegistration)
admin.site.register(ThiraiRegistration)
admin.site.register(MechRegistration)
admin.site.register(TalentiaRegistration)