from django.db.models.signals import post_save
from django.dispatch import receiver
from measurements.models import Measurement
from ponds.models import PondGraphs, PondAnalytics
from cycle.models import CycleAnalytics
from farms.models import FarmAnalytics


@receiver(post_save, sender=Measurement)
def compute_graph(sender, instance, created, *args, **kwargs):
    print("measurement siganl executing")
    default_list = ['abw']
    measure_type = instance.measurement_type.measurement_type
    if instance.value is None :
        instance_value = 0
    else :
        instance_value = instance.value
    already_exists = None
    if not created:
        already_exists = PondGraphs.objects.filter(extra_info__measurement_id=instance.id)
    if created and measure_type in default_list:
        PondGraphs.objects.create(farm=instance.cycle.Pond.farm,
            pond=instance.cycle.Pond,
            time=instance.time,
            abw=instance_value if measure_type == default_list[0] else None,
            total_feed=None,
            extra_info={'measurement_id': instance.id}
        )
    elif measure_type in default_list and not created:
        pond_graph_instance = already_exists.first()
        pond_graph_instance.time = instance.time
        pond_graph_instance.abw = float(instance_value) if measure_type == default_list[0] else None
        pond_graph_instance.total_feed =  None
        pond_graph_instance.save()

