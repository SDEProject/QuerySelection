import requests
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from requests import Response
from rest_framework import viewsets, mixins
from travelando import settings
import json


OTHER_SUBJECTS = ['Restaurant', 'Attraction', 'EmergencyService']


# Create your views here.
class QuerySelectionView(View):
    def get(self, request):
        parameters = request.GET
        query = ''

        subject = parameters.get('subject', None)
        comune = parameters.get('comune', None)
        checkin = parameters.get('checkin', None)
        shop_enum = parameters.get('shop_enum', None)
        information = parameters.get('information', None)
        info_equipment = parameters.get('info_equipment', None)
        path_difficulty = parameters.get('path_difficulty', None)
        regione = parameters.get('region', None)
        time_period = parameters.get('time_period', None)
        poi_activity_from = parameters.get('poi_activity_from', None)
        poi_activity_to = parameters.get('poi_activity_to', None)
        path_number = parameters.get('path_number', None)

        status_code = 200

        print(parameters)

        if subject == 'Hotel':
            if checkin is not None and checkin != '':
                if comune is not None and comune != '':
                    query = '3'
                else:
                    query = '6'
            elif comune is not None and comune != '':
                query = '25'
            elif regione is not None and regione != '':
                query = '26'
            else:
                query = '29'
        elif subject == 'Shop' and shop_enum is not None and shop_enum != '':
            if comune is not None and comune != '':
                query = '28'
            elif regione is not None and regione != '':
                query = '4'
            elif information == 'position':
                query = '7'
            else:
                query = '5'
        elif subject == 'ActivityPath':
            if path_difficulty is not None and len(path_difficulty) > 0:
                if info_equipment is not None and info_equipment != '':
                    query = '9'
                elif path_difficulty == 'smooth':
                    query = '12'
                else:
                    query = '14'
            elif info_equipment is not None and info_equipment != '':
                query = '27'
            elif poi_activity_from is not None and poi_activity_from != '':
                if poi_activity_to is not None and poi_activity_to != '':
                    query = '18'
                else:
                    query = '17'
            elif path_number is not None and path_number != '':
                query = '19'
            else:
                status_code = 400
                return JsonResponse({"text": "Query selection failed"}, status=status_code)
        elif subject is not None and subject in OTHER_SUBJECTS:
            if comune is not None and comune != '':
                query = '30'
            elif regione is not None and regione != '':
                query = '31'
            else:
                query = '32'
        else:
            status_code = 400
            return JsonResponse({"text": "Query selection failed"}, status=status_code)

        print(query)
        response = {
            "query": query
        }
        return JsonResponse(response, status=status_code)



