import requests
import json
from django.http.response import JsonResponse
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from api.models import Quotes
from api.seriallizers import QuotesSerializer
from rest_framework.decorators import api_view


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from dotenv import dotenv_values

config = dotenv_values(".env")


class QioteView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        quotes = Quotes.objects.all()
        quotes_serializer = QuotesSerializer(quotes, many=True)
        return JsonResponse(quotes_serializer.data, safe=False)

    def post(self, request):
        url = config["URL"] + config["KEY"]
        print(url)
        r = requests.get(url=url)
        quotes_data = r.json()
        return JsonResponse(quotes_data)


def save_quotes():
    url = config["URL"] + config["KEY"]
    r = requests.get(url=url)
    quotes_data = r.json()
    key_list = ["meta_data", "data"]
    final_dict = dict(zip(key_list, list(quotes_data.values())))
    quotes_serializer = QuotesSerializer(data=final_dict)
    if quotes_serializer.is_valid():
        quotes_serializer.save()


@api_view(["GET"])
def obtain_auth_token(request):
    print("-------------------", request.headers)
    for user in User.objects.all():
        token = Token.objects.get_or_create(user=user)[0]
        print(type(token))
        return JsonResponse({"token": str(token)})
