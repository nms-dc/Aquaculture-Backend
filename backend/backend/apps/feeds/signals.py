
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from feeds.models import Feeds
from ponds.models import PondGraphs, PondAnalytics
from cycle.models import CycleAnalytics
from farms.models import FarmAnalytics


@receiver(post_save, sender=Feeds)
def compute_graph(sender, instance, created, *args, **kwargs):
    default_list = ['feeds']
    feed_type = instance.feed_type.type
    if instance.value is None:
        instance_value = 0
    else:
        instance_value = instance.value
    already_exists = None
    if not created:
        already_exists = PondGraphs.objects.filter(extra_info__feed_id=instance.id)
    if created and feed_type in default_list:
        PondGraphs.objects.create(farm=instance.cycle.Pond.farm,
                                  pond=instance.cycle.Pond,
                                  time=instance.time,
                                  abw=None,
                                  total_feed=instance_value if feed_type == default_list[0] else None,
                                  extra_info={'feed_id': instance.id}
                                  )
    elif feed_type in default_list and not created:
        pond_graph_instance = already_exists.first()
        pond_graph_instance.time = instance.time
        pond_graph_instance.abw = None
        pond_graph_instance.total_feed = float(instance_value) if feed_type == default_list[0] else None
        pond_graph_instance.save()


@receiver(post_save, sender=Feeds)
def compute_analytics(sender, instance, created, *args, **kwargs):
    default_list = ['feeds', 'probiotics']
    feed_type = instance.feed_type.type
    if instance.value is None:
        instance_value = 0
    else:
        instance_value = instance.value
    already_exists_cycle = CycleAnalytics.objects.filter(cycle=instance.cycle, pond=instance.cycle.Pond,
                                                         farm=instance.cycle.Pond.farm)
    feed_value = Feeds.objects.filter(cycle=instance.cycle).values()
    exists_feeds = 0
    for feed in feed_value:
        exists_feeds += feed['value']
    if already_exists_cycle.exists() and feed_type == default_list[0]:
        cycle_analytics_instance = already_exists_cycle.first()
        cycle_analytics_instance.total_feed = instance_value + exists_feeds
        cycle_analytics_instance.save()
    elif not already_exists_cycle.exists() and feed_type == default_list[0]:
        CycleAnalytics.objects.create(farm=instance.cycle.Pond.farm,
                                      pond=instance.cycle.Pond,
                                      cycle=instance.cycle,
                                      total_feed=instance_value,
                                      total_probiotics=0,
                                      harvest_amount=0,
                                      extra_info={'feed_id': instance.id})
    if already_exists_cycle.exists() and feed_type == default_list[1]:
        cycle_analytics_instance = already_exists_cycle.first()
        cycle_analytics_instance.total_probiotics += instance_value
        cycle_analytics_instance.save()
    elif not already_exists_cycle.exists() and feed_type == default_list[1]:
        CycleAnalytics.objects.create(farm=instance.cycle.Pond.farm,
                                      pond=instance.cycle.Pond,
                                      cycle=instance.cycle,
                                      total_feed=instance_value,
                                      total_probiotics=instance_value,
                                      harvest_amount=0,
                                      extra_info={'feed_id': instance.id})
    already_exists_pond = PondAnalytics.objects.filter(pond=instance.cycle.Pond, farm=instance.cycle.Pond.farm)
    if already_exists_pond.exists() and feed_type == default_list[0]:
        pond_analytics_instance = already_exists_pond.first()
        pond_analytics_instance.total_feed += instance_value
        pond_analytics_instance.save()
    elif not already_exists_pond.exists() and feed_type == default_list[0]:
        PondAnalytics.objects.create(farm=instance.cycle.Pond.farm,
                                     pond=instance.cycle.Pond,
                                     total_feed=instance_value,
                                     harvest_amount=0,
                                     extra_info={'feed_id': instance.id})
    already_exists_farm = FarmAnalytics.objects.filter(farm=instance.cycle.Pond.farm)
    if already_exists_farm.exists() and feed_type == default_list[0]:
        farm_analytics_instance = already_exists_farm.first()
        farm_analytics_instance.total_feed = farm_analytics_instance.total_feed + instance_value
        farm_analytics_instance.save()
    elif not already_exists_farm.exists() and feed_type == default_list[0]:
        FarmAnalytics.objects.create(farm=instance.cycle.Pond.farm,
                                     total_feed=instance_value,
                                     harvest_amount=0,
                                     extra_info={'feed_id': instance.id})


@receiver(post_delete, sender=Feeds)
def recalculate_feedtotal(sender, instance, *args, **kwargs):
    print("measurement delete siganl executing")
    default_list = ['feeds', 'probiotics']
    feed_type = instance.feed_type.type
    if instance.value is None:
        instance_value = 0
    else:
        instance_value = instance.value
    already_exists_cycle = CycleAnalytics.objects.filter(cycle=instance.cycle, pond=instance.cycle.Pond,
                                                         farm=instance.cycle.Pond.farm)
    feed_value = Feeds.objects.filter(cycle=instance.cycle).values()
    exists_feeds = 0
    for feed in feed_value:
        exists_feeds += feed['value']
        print(exists_feeds)
    if already_exists_cycle.exists() and feed_type == default_list[0]:
        cycle_analytics_instance = already_exists_cycle.first()
        cycle_analytics_instance.total_feed = instance_value + exists_feeds
        cycle_analytics_instance.save()

    if already_exists_cycle.exists() and feed_type == default_list[1]:
        cycle_analytics_instance = already_exists_cycle.first()
        cycle_analytics_instance.total_probiotics += instance_value
        cycle_analytics_instance.save()
