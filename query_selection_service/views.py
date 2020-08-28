import requests
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from requests import Response
from rest_framework import viewsets, mixins
from travelando import settings
import json


# Create your views here.
class QuerySelectionView(View):
    def get(self, request):
        parameters = request.GET
        query = ''
        returned_params = []

        subject = parameters.get('subject', None)
        stop = parameters.get('stop', None)
        comune = parameters.get('comune', None)
        checkin = parameters.get('checkin', None)
        shop_enum = parameters.get('shop_enum', None)
        information = parameters.get('information', None)
        info_equipment = parameters.get('info_equipment', None)
        path_difficulty = parameters.get('path_difficulty', None)
        regione = parameters.get('regione', None)
        time_period = parameters.get('time_period', None)

        print(parameters)

        if subject == 'mean of transport' and stop is not None and comune is not None:
            query = '2'
        elif subject == 'hotel' and checkin is not None:
            if comune is not None and comune != '':
                query = '3'
                returned_params = ['name', 'starthour', 'endhour', 'stars', 'street']
            else:
                query = '6'
                returned_params = ['name', 'starthour', 'endhour', 'stars', 'street', 'city']
        elif subject == 'Shop' and shop_enum is not None:
            if regione is not None:
                query = '4'
            elif 'position' in information:
                query = '7'
            else:
                query = '5'
        elif subject == 'Activity path' and path_difficulty is not None:
            if time_period is not None:
                query = '8'
            elif info_equipment is not None:
                query = '9'
            elif path_difficulty == 'smooth':
                query = '12'
            elif regione is not None:
                query = '14'
            else:
                query = '15'

        response = {
            "query": query,
            "returned_params": returned_params
        }
        return JsonResponse(response)

