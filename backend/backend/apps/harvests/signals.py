from django.db.models.signals import post_save
from django.dispatch import receiver
from harvests.models import Harvests
from ponds.models import PondGraphs, PondAnalytics
from cycle.models import CycleAnalytics
from farms.models import FarmAnalytics
import pandas as pd


@receiver(post_save, sender=Harvests)
def compute_harvest_analytics(sender, instance, created, *args, **kwargs):
    if instance.total_kgs is None :
        instance_total_kgs = 0
    else :
        instance_total_kgs = instance.total_kgs
    already_exists_cycle = CycleAnalytics.objects.filter(cycle=instance.cycle, pond=instance.cycle.Pond,
                                                         farm=instance.cycle.Pond.farm)
    
    #getting all the harvest connected to the cycle and summarize the harvest_amount in each harvest for cycle analytics
    same_cycle_harvests = Harvests.objects.filter(cycle = instance.cycle).values()
    total_harvest_df = pd.DataFrame(same_cycle_harvests)
    #print(total_harvest_df['total_kgs'])
    total_kgs_sum = total_harvest_df['total_kgs'].sum()

    if already_exists_cycle.exists():
        cycle_analytics_instance = already_exists_cycle.first()
        cycle_analytics_instance.harvest_amount = total_kgs_sum
        cycle_analytics_instance.save()
    elif not already_exists_cycle.exists():
        CycleAnalytics.objects.create(farm=instance.cycle.Pond.farm,
                                      pond=instance.cycle.Pond,
                                      cycle=instance.cycle,
                                      total_feed=0,
                                      harvest_amount=instance_total_kgs,
                                      extra_info={'harvest_id': instance.id})
    already_exists_pond = PondAnalytics.objects.filter(pond=instance.cycle.Pond, farm=instance.cycle.Pond.farm)
    #getting all the cycleAnalytics connected to the pond and summarize the harvest_amount in each cycle analytics for pond analytics
    same_pond_cycle_analytics = CycleAnalytics.objects.filter(pond=instance.cycle.Pond).values()
    cycle_analytics_df = pd.DataFrame(same_pond_cycle_analytics)
    total_harvest_amount = cycle_analytics_df['harvest_amount'].sum()
    #print(same_pond_cycle_analytics)
    if already_exists_pond.exists():
        pond_analytics_instance = already_exists_pond.first()
        pond_analytics_instance.harvest_amount = total_harvest_amount
        pond_analytics_instance.save()
    elif not already_exists_pond.exists():
        PondAnalytics.objects.create(farm=instance.cycle.Pond.farm,
                                     pond=instance.cycle.Pond,
                                     harvest_amount=instance_total_kgs,
                                     total_feed=0,
                                     extra_info={'harvest_id': instance.id})

    already_exists_farm = FarmAnalytics.objects.filter(farm=instance.cycle.Pond.farm)
    #getting all the pondAnalytics connected to the farm and summarize the harvest_amount in each pond analytics for farm analytics
    same_farm_pond_analytics = PondAnalytics.objects.filter(farm=instance.cycle.Pond.farm).values()
    pond_analytics_df = pd.DataFrame(same_farm_pond_analytics)
    total_harvest_amount = pond_analytics_df['harvest_amount'].sum()
    print(same_farm_pond_analytics)
    if already_exists_farm.exists():
        farm_analytics_instance = already_exists_farm.first()
        farm_analytics_instance.harvest_amount = total_harvest_amount
        farm_analytics_instance.save()
    elif not already_exists_farm.exists():
        FarmAnalytics.objects.create(farm=instance.cycle.Pond.farm,
                                     harvest_amount=instance_total_kgs,
                                     total_feed=0,
                                     extra_info={'harvest_id': instance.id})
