import json
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

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
)


# -----------------------------
# Helper: parse JSON members
# -----------------------------
def parse_members(data, key="members"):
    """
    Handles members from FormData:
    members comes as a string JSON -> convert to list
    """
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
@api_view(["GET", "POST"])
@parser_classes([MultiPartParser, FormParser])
def pitch_register(request):

    if request.method == "GET":
        qs = PitchRegistration.objects.all().order_by("-created_at")
        serializer = PitchRegistrationSerializer(qs, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST
    data = request.data.copy()

    if not parse_members(data, key="members"):
        return Response({"members": ["Value must be valid JSON."]}, status=status.HTTP_400_BAD_REQUEST)

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
