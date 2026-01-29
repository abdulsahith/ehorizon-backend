import json
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone


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
    Admin,
    RisingRegistration,
    StartupRegistration,
    IPRRegistration,
    BusinessRegistration,
    ProductRegistration,
    StocksRegistration,
    BplanRegistration,
    DetxRegistration,
)

from .serial import (
    PitchRegistrationSerializer,
    GamethonRegistrationSerializer,
    BuildRegistrationSerializer,
    WebifyRegistrationSerializer,
    ElectricRegistrationSerializer,
    IPLRegistrationSerializer,
    MasterRegistrationSerializer,
    MechRegistrationSerializer,
    ThiraiRegistrationSerializer,
    TalentiaRegistrationSerializer,
    AdminSerializer,
    RisingRegistrationSerializer,
    StartupRegistrationSerializer,
    IPRRegistrationSerializer,
    BusinessRegistrationSerializer,
    ProductRegistrationSerializer,
    StocksRegistrationSerializer,
    BplanRegistrationSerializer,
    DetxRegistrationSerializer,

)


# -----------------------------
# Helper: parse JSON members
# -----------------------------
def parse_members(data, key="members"):
     
    raw = data.get(key, "[]")

    # if it comes as list like ['[...]'] unwrap it
    if isinstance(raw, list) and len(raw) == 1:
        raw = raw[0]

    if isinstance(raw, str):
        try:
            data[key] = json.loads(raw)
        except json.JSONDecodeError:
            return False
    return True


# -----------------------------
# PITCH (uses members)
# -----------------------------

@api_view(["POST"])
def pitch_send_mail(request):
    team_id = request.data.get("team_id")
    subject = request.data.get("subject", "").strip()
    content = request.data.get("content", "").strip()

    if not team_id:
        return Response({"error": "team_id is required"}, status=400)
    if not subject:
        return Response({"error": "subject is required"}, status=400)
    if not content:
        return Response({"error": "content is required"}, status=400)

    try:
        team = PitchRegistration.objects.get(id=team_id)
    except PitchRegistration.DoesNotExist:
        return Response({"error": "Team not found"}, status=404)

    members = team.members or []
    recipients = [m.get("email", "").strip() for m in members if m.get("email")]
    recipients = [r for r in recipients if r]

    if not recipients:
        return Response({"error": "No valid member emails found"}, status=400)

    # ✅ if you want to block re-sending uncomment this:
    # if team.mail_sent:
    #     return Response({"error": "Mail already sent for this team"}, status=400)

    try:
        send_mail(
            subject=subject,
            message=content,
            from_email=None,   # uses DEFAULT_FROM_EMAIL
            recipient_list=recipients,
            fail_silently=False,
        )
    except Exception as e:
        return Response({"error": str(e)}, status=500)

    team.mail_sent = True
    team.mail_sent_at = timezone.now()
    team.mail_sent_subject = subject
    team.save(update_fields=["mail_sent", "mail_sent_at", "mail_sent_subject"])

    return Response(
        {"message": "Mail sent", "recipients": len(recipients)},
        status=status.HTTP_200_OK
    )

@api_view(["GET", "POST"])
@parser_classes([MultiPartParser, FormParser])
def pitch_register(request):

    if request.method == "GET":
        qs = PitchRegistration.objects.all().order_by("-created_at")
        serializer = PitchRegistrationSerializer(qs, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST
    data = request.data.copy()
    

    serializer = PitchRegistrationSerializer(data=data, context={"request": request})
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Pitch registration successful"}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -----------------------------
# GAMEATHON
# -----------------------------
@api_view(["GET", "POST"])
@parser_classes([MultiPartParser, FormParser])
def gameathon_register(request):

    if request.method == "GET":
        qs = GameathonRegistration.objects.all().order_by("-created_at")
        serializer = GamethonRegistrationSerializer(qs, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    data = request.data.copy()
    serializer = GamethonRegistrationSerializer(data=data, context={"request": request})
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Registered successfully"}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -----------------------------
# WEBIFY
# -----------------------------
@api_view(["GET", "POST"])
@parser_classes([MultiPartParser, FormParser])
def webify_register(request):

    if request.method == "GET":
        qs = WebifyRegistration.objects.all().order_by("-created_at")
        serializer = WebifyRegistrationSerializer(qs, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    data = request.data.copy()
    serializer = WebifyRegistrationSerializer(data=data, context={"request": request})
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Registered successfully"}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -----------------------------
# BUILDSCAPE
# -----------------------------
@api_view(["GET", "POST"])
@parser_classes([MultiPartParser, FormParser])
def buildscape_register(request):

    if request.method == "GET":
        qs = BuildRegistration.objects.all().order_by("-created_at")
        serializer = BuildRegistrationSerializer(qs, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    data = request.data.copy()

    # ✅ FIX: use BuildRegistrationSerializer (not Webify)
    serializer = BuildRegistrationSerializer(data=data, context={"request": request})
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Registered successfully"}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -----------------------------
# ELECTRICAL ODYSSEY
# -----------------------------
@api_view(["GET", "POST"])
@parser_classes([MultiPartParser, FormParser])
def electric_register(request):

    if request.method == "GET":
        qs = ElectricRegistration.objects.all().order_by("-created_at")
        serializer = ElectricRegistrationSerializer(qs, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    data = request.data.copy()
    serializer = ElectricRegistrationSerializer(data=data, context={"request": request})
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Registered successfully"}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -----------------------------
# IPL AUCTION
# -----------------------------
@api_view(["GET", "POST"])
@parser_classes([MultiPartParser, FormParser])
def ipl_register(request):

    if request.method == "GET":
        qs = IPLRegistration.objects.all().order_by("-created_at")
        serializer = IPLRegistrationSerializer(qs, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    data = request.data.copy()
    serializer = IPLRegistrationSerializer(data=data, context={"request": request})
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Registered successfully"}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -----------------------------
# MASTER CHEF
# -----------------------------
@api_view(["GET", "POST"])
@parser_classes([MultiPartParser, FormParser])
def master_register(request):

    if request.method == "GET":
        qs = MasterRegistration.objects.all().order_by("-created_at")
        serializer = MasterRegistrationSerializer(qs, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    data = request.data.copy()
    serializer = MasterRegistrationSerializer(data=data, context={"request": request})
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Registered successfully"}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -----------------------------
# MECH ARENA
# -----------------------------
@api_view(["GET", "POST"])
@parser_classes([MultiPartParser, FormParser])
def mech_register(request):

    if request.method == "GET":
        qs = MechRegistration.objects.all().order_by("-created_at")
        serializer = MechRegistrationSerializer(qs, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    data = request.data.copy()
    serializer = MechRegistrationSerializer(data=data, context={"request": request})
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Registered successfully"}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -----------------------------
# THIRAI TRIVIA
# -----------------------------
@api_view(["GET", "POST"])
@parser_classes([MultiPartParser, FormParser])
def thirai_register(request):

    if request.method == "GET":
        qs = ThiraiRegistration.objects.all().order_by("-created_at")
        serializer = ThiraiRegistrationSerializer(qs, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    data = request.data.copy()
    serializer = ThiraiRegistrationSerializer(data=data, context={"request": request})
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Registered successfully"}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -----------------------------
# TALENTIA
# -----------------------------
@api_view(["GET", "POST"])
@parser_classes([MultiPartParser, FormParser])
def talentia_register(request):

    if request.method == "GET":
        qs = TalentiaRegistration.objects.all().order_by("-created_at")
        serializer = TalentiaRegistrationSerializer(qs, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    data = request.data.copy()
    serializer = TalentiaRegistrationSerializer(data=data, context={"request": request})
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Registered successfully"}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


 
@api_view(["GET", "POST"])
@parser_classes([MultiPartParser, FormParser])
def rising_register(request):

    if request.method == "GET":
        qs = RisingRegistration.objects.all().order_by("-created_at")
        serializer = RisingRegistrationSerializer(qs, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    data = request.data.copy()
    serializer = RisingRegistrationSerializer(data=data, context={"request": request})
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Registered successfully"}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "POST"])
@parser_classes([MultiPartParser, FormParser])
def startup_register(request):

    if request.method == "GET":
        qs = StartupRegistration.objects.all().order_by("-created_at")
        serializer = StartupRegistrationSerializer(qs, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    data = request.data.copy()
    serializer = StartupRegistrationSerializer(data=data, context={"request": request})
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Registered successfully"}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
@parser_classes([MultiPartParser, FormParser])
def ipr_register(request):

    if request.method == "GET":
        qs = IPRRegistration.objects.all().order_by("-created_at")
        serializer = IPRRegistrationSerializer(qs, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    data = request.data.copy()
    serializer = IPRRegistrationSerializer(data=data, context={"request": request})
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Registered successfully"}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
@parser_classes([MultiPartParser, FormParser])
def business_register(request):

    if request.method == "GET":
        qs = BusinessRegistration.objects.all().order_by("-created_at")
        serializer = BusinessRegistrationSerializer(qs, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    data = request.data.copy()
    serializer = BusinessRegistrationSerializer(data=data, context={"request": request})
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Registered successfully"}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "POST"])
@parser_classes([MultiPartParser, FormParser])
def product_register(request):

    if request.method == "GET":
        qs = ProductRegistration.objects.all().order_by("-created_at")
        serializer = ProductRegistrationSerializer(qs, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    data = request.data.copy()
    serializer = ProductRegistrationSerializer(data=data, context={"request": request})
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Registered successfully"}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
@parser_classes([MultiPartParser, FormParser])
def stocks_register(request):

    if request.method == "GET":
        qs = StocksRegistration.objects.all().order_by("-created_at")
        serializer = StocksRegistrationSerializer(qs, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    data = request.data.copy()
    serializer = StocksRegistrationSerializer(data=data, context={"request": request})
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Registered successfully"}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
@parser_classes([MultiPartParser, FormParser])
def bplan_register(request):

    if request.method == "GET":
        qs = BplanRegistration.objects.all().order_by("-created_at")
        serializer = BplanRegistrationSerializer(qs, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    data = request.data.copy()
    serializer = BplanRegistrationSerializer(data=data, context={"request": request})
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Registered successfully"}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
@parser_classes([MultiPartParser, FormParser])
def detx_register(request):

    if request.method == "GET":
        qs = DetxRegistration.objects.all().order_by("-created_at")
        serializer = DetxRegistrationSerializer(qs, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    data = request.data.copy()
    serializer = DetxRegistrationSerializer(data=data, context={"request": request})
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Registered successfully"}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


 
 
 
 
 
 
 
 

@api_view(["POST", "GET"])
def admin_login(request):
    
    if request.method == "POST":
        username = request.data.get("username")
        password = request.data.get("password")
    else:  # GET
        username = request.query_params.get("username")
        password = request.query_params.get("password")

    if not username or not password:
        return Response(
            {"success": False, "message": "Username and password required"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        admin = Admin.objects.get(username=username, password=password)

        request.session["adname"] = admin.username
        request.session["category"] = admin.category

        return Response(
            {
                "success": True,
                "page": admin.category,           
                "message": "Login successful!",
                "data": AdminSerializer(admin).data,
            },
            status=status.HTTP_200_OK,
        )

    except Admin.DoesNotExist:
        return Response(
            {"success": False, "message": "Invalid username or password"},
            status=status.HTTP_401_UNAUTHORIZED,
        )
