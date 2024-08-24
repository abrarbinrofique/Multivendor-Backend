from rest_framework.response import Response

def throw_unauthenticated(request):
    if not request.user.is_authenticated:
        return Response({
            "error": "Unauthorized action",
        })