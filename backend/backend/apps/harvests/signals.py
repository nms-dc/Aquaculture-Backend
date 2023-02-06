from django.db.models.signals import post_save
from django.dispatch import receiver
from harvests.models import Harvests
from ponds.models import PondGraphs, PondAnalytics
from cycle.models import CycleAnalytics
from farms.models import FarmAnalytics


@receiver(post_save, sender=Harvests)
def compute_harvest_analytics(sender, instance, created, *args, **kwargs):
    if instance.total_kgs is None :
        instance_total_kgs = 0
    else :
        instance_total_kgs = instance.total_kgs
    already_exists_cycle = CycleAnalytics.objects.filter(cycle=instance.cycle, pond=instance.cycle.Pond,
                                                         farm=instance.cycle.Pond.farm)

    if already_exists_cycle.exists():
        cycle_analytics_instance = already_exists_cycle.first()
        cycle_analytics_instance.harvest_amount += instance_total_kgs
        cycle_analytics_instance.save()
    elif not already_exists_cycle.exists():
        CycleAnalytics.objects.create(farm=instance.cycle.Pond.farm,
                                      pond=instance.cycle.Pond,
                                      cycle=instance.cycle,
                                      total_feed=0,
                                      harvest_amount=instance_total_kgs,
                                      extra_info={'harvest_id': instance.id})
    already_exists_pond = PondAnalytics.objects.filter(pond=instance.cycle.Pond, farm=instance.cycle.Pond.farm)
    if already_exists_pond.exists():
        pond_analytics_instance = already_exists_pond.first()
        pond_analytics_instance.harvest_amount += instance_total_kgs
        pond_analytics_instance.save()
    elif not already_exists_pond.exists():
        PondAnalytics.objects.create(farm=instance.cycle.Pond.farm,
                                     pond=instance.cycle.Pond,
                                     harvest_amount=instance_total_kgs,
                                     total_feed=0,
                                     extra_info={'harvest_id': instance.id})

    already_exists_farm = FarmAnalytics.objects.filter(farm=instance.cycle.Pond.farm)
    if already_exists_farm.exists():
        farm_analytics_instance = already_exists_farm.first()
        farm_analytics_instance.harvest_amount += instance_total_kgs
        farm_analytics_instance.save()
    elif not already_exists_farm.exists():
        FarmAnalytics.objects.create(farm=instance.cycle.Pond.farm,
                                     harvest_amount=instance_total_kgs,
                                     total_feed=0,
                                     extra_info={'harvest_id': instance.id})
