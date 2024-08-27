from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import UserProfile
from .utils import throw_unauthenticated
from .constants import USER_TYPES

@api_view()
def profile(request):
    res = throw_unauthenticated(request)
    if res: return res
    profile = UserProfile.objects.get(user=request.user)
    return Response({
        "type": profile.type, 
        "address": profile.shipping_address,
    })

@api_view(http_method_names=['PUT'])
def set_type(request):
    res = throw_unauthenticated(request)
    if res: return res
    try:
        if request.data["type"] == "none" or request.data["type"] not in [x[0] for x in USER_TYPES]:
            return Response({
                "error": "Invalid type",
            })
        profile = UserProfile.objects.get(user=request.user)
        if profile.type != "none":
            return Response({
                "error": "You cannot set type multiple times.",
            })
        profile.type = request.data["type"]
        profile.save()
        return Response({
            "message": "success",
        })
    except:
        return Response({
            "error": "Invalid request",
        })

@api_view(http_method_names=['PUT'])
def set_shipping_address(request):
    res = throw_unauthenticated(request)
    if res: return res
    if "address" not in request.data:
        return Response({
            "error": "No address was provided",
        })
    profile = UserProfile.objects.get(user=request.user)
    profile.shipping_address = request.data["address"]
    profile.save()

    return Response({
        "message": "success",
    })
