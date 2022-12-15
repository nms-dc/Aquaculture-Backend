from django.db.models.signals import post_save
from django.dispatch import receiver
from measurements.models import Measurement
from ponds.models import PondGraphs

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

