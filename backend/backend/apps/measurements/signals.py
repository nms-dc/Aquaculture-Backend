from django.db.models.signals import post_save
from django.dispatch import receiver
from measurements.models import Measurement
from ponds.models import PondGraphs, PondAnalytics
from cycle.models import CycleAnalytics
from farms.models import FarmAnalytics

@receiver(post_save, sender=Measurement)
def compute_graph(sender, instance, created, *args, **kwargs):
    default_list = ['feeds', 'abw']
    measure_type = instance.measurement_type.measurement_type
    already_exists = None
    if not created:
        # already_exists = PondGraphs.objects.filter(extra_info__contains=[{'measurement_id': instance.id}])
        already_exists = PondGraphs.objects.filter(extra_info__measurement_id=instance.id)
    if created and measure_type in default_list:
        PondGraphs.objects.create(farm=instance.cycle.Pond.farm,
            pond=instance.cycle.Pond,
            time=instance.time,
            abw=instance.value if measure_type == default_list[1] else None,
            total_feed=instance.value if measure_type == default_list[0] else None,
            extra_info={'measurement_id': instance.id}
        )
    elif already_exists.first() and measure_type in default_list and not created:
        pond_graph_instance = already_exists.first()
        print('pond_graph_instance', pond_graph_instance.abw)
        # pond_graph_instance.farm=instance.cycle.Pond.farm
        # pond_graph_instance.pond=instance.cycle.Pond
        pond_graph_instance.time=instance.time
        pond_graph_instance.abw=float(instance.value) if measure_type == default_list[1] else None
        pond_graph_instance.total_feed=float(instance.value) if measure_type == default_list[0] else None
        pond_graph_instance.save()


@receiver(post_save, sender=Measurement)
def compute_analytics(sender, instance, created, *args, **kwargs):
    default_list = ['feeds']
    measure_type = instance.measurement_type.measurement_type
    already_exists_cycle = CycleAnalytics.objects.filter(cycle=instance.cycle, pond=instance.cycle.Pond, farm=instance.cycle.Pond.farm)
    if already_exists_cycle.exists() and measure_type == default_list[0]:
        cycle_analytics_instance = already_exists_cycle.first()
        cycle_analytics_instance.total_feed += instance.value
        cycle_analytics_instance.save()
    elif not already_exists_cycle.exists() and measure_type == default_list[0]:
        CycleAnalytics.objects.create(farm=instance.cycle.Pond.farm,
            pond=instance.cycle.Pond,
            cycle=instance.cycle,
            total_feed=instance.value,
            harvest_amount=0,
            extra_info={'measurement_id': instance.id}
        )
    already_exists_pond =PondAnalytics.objects.filter(pond=instance.cycle.Pond, farm=instance.cycle.Pond.farm)
    if already_exists_pond.exists() and measure_type == default_list[0]:
        pond_analytics_instance = already_exists_pond.first()
        pond_analytics_instance.total_feed += instance.value
        pond_analytics_instance.save()
    elif not already_exists_pond.exists() and measure_type == default_list[0]:
        PondAnalytics.objects.create(farm=instance.cycle.Pond.farm,
            pond=instance.cycle.Pond,
            total_feed=instance.value,
            harvest_amount=0,
            extra_info={'measurement_id': instance.id}
        )

    already_exists_farm =FarmAnalytics.objects.filter(farm=instance.cycle.Pond.farm)
    if already_exists_farm.exists() and measure_type == default_list[0]:
        farm_analytics_instance = already_exists_pond.first()      
        farm_analytics_instance.total_feed = farm_analytics_instance.total_feed + instance.value
        farm_analytics_instance.save()
    elif not already_exists_farm.exists() and measure_type == default_list[0]:
        FarmAnalytics.objects.create(farm=instance.cycle.Pond.farm,
            total_feed=instance.value,
            harvest_amount=0,
            extra_info={'measurement_id': instance.id}
        )
