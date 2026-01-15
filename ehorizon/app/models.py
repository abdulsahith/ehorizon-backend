# models.py
from django.db import models
from django.core.exceptions import ValidationError

# models.py

def abstract_upload_path(instance, filename):
    return f"pitch_abstracts/{instance.team_name}/{filename}"


def gamethon_upload_path(instance, filename):
    return f"gamethon/{instance.team_name}/{filename}"

def webify_upload_path(instance, filename):
    return f"webify/{instance.team_name}/{filename}"

def mech_upload_path(instance, filename):
    return f"mech/{instance.team_name}/{filename}"

def build_upload_path(instance, filename):
    return f"build/{instance.team_name}/{filename}"

def electric_upload_path(instance, filename):
    return f"electric/{instance.team_name}/{filename}"
def master_upload_path(instance, filename):
    return f"master/{instance.team_name}/{filename}"

def ipl_upload_path(instance, filename):
    return f"ipl/{instance.team_name}/{filename}"

def thirai_upload_path(instance, filename):
    return f"thirai/{instance.team_name}/{filename}"

def talentia_upload_path(instance, filename):
    return f"talentia/{instance.team_name}/{filename}"


class PitchRegistration(models.Model):
    team_name = models.CharField(max_length=120)
    trl_level = models.IntegerField()
    theme = models.CharField(max_length=50)
    abstract_pdf = models.FileField(upload_to=abstract_upload_path)
    members = models.JSONField()   # list of members
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team_name


class GameathonRegistration(models.Model):
    team_name = models.CharField(max_length=120)
    event_name = models.CharField(max_length=50, default="gameathon")  # fixed for this model

    # Team lead fields (simple)
    lead_name = models.CharField(max_length=100)
    lead_roll = models.CharField(max_length=50)
    lead_department = models.CharField(max_length=50)
    lead_year = models.CharField(max_length=10)
    lead_mobile = models.CharField(max_length=20)
    lead_email = models.EmailField()

    # Members list (JSON)
    team_members = models.JSONField(default=list)   # [{name,roll,dept,year,mobile,email}, ...]

    # payment screenshot files (optional)
    payment_screenshots = models.FileField(upload_to=gamethon_upload_path, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.team_name} ({self.event_name})"


class WebifyRegistration(models.Model):
    team_name = models.CharField(max_length=120)
    event_name = models.CharField(max_length=50, default="webify")  # fixed for this model

    # Team lead fields (simple)
    lead_name = models.CharField(max_length=100)
    lead_roll = models.CharField(max_length=50)
    lead_department = models.CharField(max_length=50)
    lead_year = models.CharField(max_length=10)
    lead_mobile = models.CharField(max_length=20)
    lead_email = models.EmailField()

    # Members list (JSON)
    team_members = models.JSONField(default=list)   # [{name,roll,dept,year,mobile,email}, ...]

    # payment screenshot files (optional)
    payment_screenshots = models.FileField(upload_to=webify_upload_path, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.team_name} ({self.event_name})"
    

class MechRegistration(models.Model):
    team_name = models.CharField(max_length=120)
    event_name = models.CharField(max_length=50, default="mech")   

    # Team lead fields (simple)
    lead_name = models.CharField(max_length=100)
    lead_roll = models.CharField(max_length=50)
    lead_department = models.CharField(max_length=50)
    lead_year = models.CharField(max_length=10)
    lead_mobile = models.CharField(max_length=20)
    lead_email = models.EmailField()

    
    team_members = models.JSONField(default=list)   

     
    payment_screenshots = models.FileField(upload_to=mech_upload_path, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.team_name} ({self.event_name})"
    

class BuildRegistration(models.Model):
    team_name = models.CharField(max_length=120)
    event_name = models.CharField(max_length=50, default="build")   

    # Team lead fields (simple)
    lead_name = models.CharField(max_length=100)
    lead_roll = models.CharField(max_length=50)
    lead_department = models.CharField(max_length=50)
    lead_year = models.CharField(max_length=10)
    lead_mobile = models.CharField(max_length=20)
    lead_email = models.EmailField()

    
    team_members = models.JSONField(default=list)   

     
    payment_screenshots = models.FileField(upload_to=build_upload_path, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.team_name} ({self.event_name})"
    
class ElectricRegistration(models.Model):
    team_name = models.CharField(max_length=120)
    event_name = models.CharField(max_length=50, default="electric")   

    # Team lead fields (simple)
    lead_name = models.CharField(max_length=100)
    lead_roll = models.CharField(max_length=50)
    lead_department = models.CharField(max_length=50)
    lead_year = models.CharField(max_length=10)
    lead_mobile = models.CharField(max_length=20)
    lead_email = models.EmailField()

    
    team_members = models.JSONField(default=list)   

     
    payment_screenshots = models.FileField(upload_to=electric_upload_path, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.team_name} ({self.event_name})"
    
class MasterRegistration(models.Model):
    team_name = models.CharField(max_length=120)
    event_name = models.CharField(max_length=50, default="master")   

    # Team lead fields (simple)
    lead_name = models.CharField(max_length=100)
    lead_roll = models.CharField(max_length=50)
    lead_department = models.CharField(max_length=50)
    lead_year = models.CharField(max_length=10)
    lead_mobile = models.CharField(max_length=20)
    lead_email = models.EmailField()

    
    team_members = models.JSONField(default=list)   

     
    payment_screenshots = models.FileField(upload_to=master_upload_path, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.team_name} ({self.event_name})"
    
class IPLRegistration(models.Model):
    team_name = models.CharField(max_length=120)
    event_name = models.CharField(max_length=50, default="ipl")   

    # Team lead fields (simple)
    lead_name = models.CharField(max_length=100)
    lead_roll = models.CharField(max_length=50)
    lead_department = models.CharField(max_length=50)
    lead_year = models.CharField(max_length=10)
    lead_mobile = models.CharField(max_length=20)
    lead_email = models.EmailField()

    
    team_members = models.JSONField(default=list)   

     
    payment_screenshots = models.FileField(upload_to=ipl_upload_path, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.team_name} ({self.event_name})"
    
class ThiraiRegistration(models.Model):
    team_name = models.CharField(max_length=120)
    event_name = models.CharField(max_length=50, default="thirai")   

    # Team lead fields (simple)
    lead_name = models.CharField(max_length=100)
    lead_roll = models.CharField(max_length=50)
    lead_department = models.CharField(max_length=50)
    lead_year = models.CharField(max_length=10)
    lead_mobile = models.CharField(max_length=20)
    lead_email = models.EmailField()

    
    team_members = models.JSONField(default=list)   

     
    payment_screenshots = models.FileField(upload_to=thirai_upload_path, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.team_name} ({self.event_name})"
    
class TalentiaRegistration(models.Model):
    team_name = models.CharField(max_length=120)
    event_name = models.CharField(max_length=50, default="talentia")   

    # Team lead fields (simple)
    lead_name = models.CharField(max_length=100)
    lead_roll = models.CharField(max_length=50)
    lead_department = models.CharField(max_length=50)
    lead_year = models.CharField(max_length=10)
    lead_mobile = models.CharField(max_length=20)
    lead_email = models.EmailField()

    
    team_members = models.JSONField(default=list)   

     
    payment_screenshots = models.FileField(upload_to=talentia_upload_path, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.team_name} ({self.event_name})"