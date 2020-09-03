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
        # returned_params = []

        subject = parameters.get('subject', None)
        stop = parameters.get('stop', None)
        comune = parameters.get('comune', None)
        checkin = parameters.get('checkin', None)
        shop_enum = parameters.get('shop_enum', None)
        information = parameters.get('information', None)
        info_equipment = parameters.get('info_equipment', None)
        path_difficulty = parameters.get('path_difficulty', None)
        regione = parameters.get('region', None)
        time_period = parameters.get('time_period', None)

        print(parameters)

        if subject == 'mean of transport' and stop is not None and comune is not None:
            query = '2'
        elif subject == 'hotel' and checkin is not None:
            if comune is not None and comune != '':
                query = '3'
                # returned_params = ['name', 'starthour', 'endhour', 'stars', 'street']
                required_params = ['comune', 'checkin']
            else:
                query = '6'
                # returned_params = ['name', 'starthour', 'endhour', 'stars', 'street', 'city']
        elif subject == 'Shop' and shop_enum is not None:
            if regione is not None and regione != '':
                query = '4'
            elif 'position' in information:
                query = '7'
            else:
                query = '5'
        elif subject == 'ActivityPath':
            if path_difficulty is not None:
                if time_period is not None and time_period != '':
                    query = '8'
                elif info_equipment is not None and info_equipment != '':
                    query = '9'
                elif path_difficulty == 'smooth':
                    query = '12'
                else:
                    query = '14'

        print(query)
        response = {
            "query": query
        }
        return JsonResponse(response)


class TemplateSelectionView(View):
    def get(self, request):
        query = parameters.get('query', None)

        template = 'Sorry something went wrong'

        if query == '3':
            template = 'The hotel {name} starts checkin at {starthour} and ends at {endhour}.'
        elif query == '2':
            template = 'At the stop {name}, you can find the following mean of transport: {transports}.'
        elif query == '6':
            template = 'The hotel {name} in {city} starts checkin at {starthour} and ends at {endhour}.'
        elif query == '4':
            template = 'The {shop_enum} in {city} are: {shops}.'
        elif query == '5':
            template = 'The {shop_enum} in {city} ({region}) are: {shops}.'
        elif query == '7':
            template = 'The {shop_enum} {name} is in {address}, {city} ({region}).'
        elif query == '8':
            template = 'The {difficulty} difficulty activity path with duration {time} are: {paths}.'

        response = {
            "template": template
        }
        return JsonResponse(response)

