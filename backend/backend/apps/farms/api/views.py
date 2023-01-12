from urllib.request import FancyURLopener
from rest_framework import status
from django.db.models import Q
import copy
from ponds.models import Ponds
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from accounts.models import User, create_username
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from farms.models import Farms, FarmCertification, FarmImage, FeedLots
from farms.api.serializers import FarmSerializer, FarmSummarySerializer, FarmPondRelationSerializer,\
    FarmCycleRelationSerializer, FeedLotsSerializer, FeedlotFilterSerializer,  FeedProSerializer, FeedAllSerializer
from django.views.decorators.csrf import csrf_exempt
from ponds.api.serializers import PondSummaryOnlySerializer
from measurements.models import MeasurementMaster, Measurement


class FarmView(viewsets.ModelViewSet):
    queryset = Farms.objects.all()
    serializer_class = FarmSerializer
    authentication_classes = []
    permission_classes = [AllowAny]
    http_method_names = ['post', 'get', 'patch', 'retrieve', 'put']

    @action(detail=True, methods=['get'], url_path='get-farm-summary',)
    @csrf_exempt
    def get_farm_summary(self, request, *args, **kwargs):
        farm = self.get_object()
        result = FarmSummarySerializer(instance=farm, context={'request': request}).data
        return Response({"result": result})

    @action(detail=True, methods=['get'], url_path='get-related-ponds',)
    @csrf_exempt
    def get_related_ponds(self, request, *args, **kwargs):
        farm = self.get_object()
        result = FarmPondRelationSerializer(instance=farm, context={'request': request}).data
        return Response({"result": result})

    @action(detail=True, methods=['get'], url_path='get-notification',)
    @csrf_exempt
    def get_notification(self, request, *args, **kwargs):
        my_list_two = []
        farm = self.get_object()
        ponds = Ponds.objects.filter(Q(farm=farm, active_cycle_id__isnull=False))
        for pond in ponds:
            import datetime
            real_date1 = datetime.datetime.strptime(str(pond.active_cycle_date), '%Y-%m-%d')
            real_date2 = datetime.datetime.today()
            date_range = real_date2 - real_date1
            dates = list()
            for days in range(0, date_range.days+1):
                dates.append((real_date1 + datetime.timedelta(days)).strftime('%Y-%m-%d'))
            dates.reverse()
            for date in dates:
                my_dict = {}
                measure = Measurement.objects.filter(cycle__id=pond.active_cycle_id,
                                                     time__date=date).order_by('-time').values_list('measurement_type__id', flat=True)
                not_accesed = MeasurementMaster.objects.filter(~Q(id__in=list(measure))).values_list('measurement_type',
                                                                                                     flat=True)
                ponds_data = Ponds.objects.get(id=pond.id)
                serializer = PondSummaryOnlySerializer(ponds_data).data
                try:
                    notif = [x for x in my_list_two if x['date'] == date]
                    if len(notif):
                        data = serializer
                        data["pending_records"] = list(not_accesed)
                        notif[0]["notification"].append(data)
                    else:
                        my_dict["date"] = date
                        my_dict["notification"] = [serializer]
                        my_dict["notification"][0]["pending_records"] = list(not_accesed)
                        my_list_two.append(my_dict)
                except KeyError:
                    my_dict["date"] = date
                    my_dict["notification"] = [serializer]
                    my_dict["notification"][0]["pending_records"] = list(not_accesed)
                    my_list_two.append(my_dict)
        return Response(my_list_two)

    @action(detail=True, methods=['get'], url_path='get-related-cycle',)
    @csrf_exempt
    def get_related_cycle(self, request, *args, **kwargs):
        farm = self.get_object()
        result = FarmCycleRelationSerializer(instance=farm, context={'request': request}).data
        return Response({"result": result})

    @action(detail=True, methods=['get'], url_path='get-feed-lots',)
    @csrf_exempt
    def get_feed_lots(self, request, *args, **kwargs):
        farm = self.get_object()
        result = FeedlotFilterSerializer(instance=farm, context={'request': request}).data
        return Response({"result": result})

    @action(detail=True, methods=['get'], url_path='get-probiotics-lots',)
    @csrf_exempt
    def get_probiotics_lots(self, request, *args, **kwargs):
        farm = self.get_object()
        result = FeedProSerializer(instance=farm, context={'request': request}).data
        return Response({"result": result})
    
    
    @action(detail=True, methods=['get'], url_path='get-feedlots',)
    @csrf_exempt
    def get_feedlots(self, request, *args, **kwargs):
        farm = self.get_object()
        print(farm)
        result = FeedAllSerializer(instance=farm, context={'request': request}).data
        return Response({"result": result})
    


class FeedLotsView(viewsets.ModelViewSet):
    queryset = FeedLots.objects.all()
    serializer_class = FeedLotsSerializer
    authentication_classes = []
    permission_classes = [AllowAny]
    http_method_names = ['post', 'get', 'patch', 'retrieve', 'put']

    @action(detail=True, methods=['get'], url_path='F',)
    @csrf_exempt
    def get_F(self, request, *args, **kwargs):
        farm = self.get_object()
        result = FeedlotFilterSerializer(instance=farm, context={'request': request}).data
        return Response({"result": result})

    @action(detail=True, methods=['get'], url_path='P',)
    @csrf_exempt
    def get_P(self, request, *args, **kwargs):
        farm = self.get_object()
        result = FeedProSerializer(instance=farm, context={'request': request}).data
        return Response({"result": result})
