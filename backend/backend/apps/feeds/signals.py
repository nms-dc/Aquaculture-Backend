
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from feeds.models import Feeds, FeedType
from ponds.models import PondGraphs, PondAnalytics
from cycle.models import CycleAnalytics,Cycle
from farms.models import FarmAnalytics
import pandas as pd



# @receiver(post_save, sender=Feeds)
# def compute_graph(sender, instance, created, *args, **kwargs):
#     default_list = ['feeds']
#     feed_type = instance.feed_type.type
#     if instance.value is None:
#         instance_value = 0
#     else:
#         instance_value = instance.value
#     already_exists = None
#     if not created:
#         already_exists = PondGraphs.objects.filter(extra_info__feed_id=instance.id)
#     if created and feed_type in default_list:
#         PondGraphs.objects.create(farm=instance.cycle.Pond.farm,
#                                   pond=instance.cycle.Pond,
#                                   time=instance.time,
#                                   abw=None,
#                                   total_feed=instance_value if feed_type == default_list[0] else None,
#                                   extra_info={'feed_id': instance.id}
#                                   )
#     elif feed_type in default_list and not created:
#         pond_graph_instance = already_exists.first()
#         pond_graph_instance.time = instance.time
#         pond_graph_instance.abw = None
#         pond_graph_instance.total_feed += float(instance_value) if feed_type == default_list[0] else None
#         pond_graph_instance.save()


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
    exists_probiotics = 0
    if feed_type == default_list[0]:
        df = pd.DataFrame(feed_value)
        exists_feeds = df['value'].sum()
        
    elif feed_type == default_list[0]:
        df = pd.DataFrame(feed_value)
        exists_probiotics = df['value'].sum()
    if already_exists_cycle.exists() and feed_type == default_list[0]:
        cycle_analytics_instance = already_exists_cycle.first()
        cycle_analytics_instance.total_feed = exists_feeds
        print(exists_feeds)
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
        cycle_analytics_instance.total_probiotics = exists_probiotics
        cycle_analytics_instance.save()
    elif not already_exists_cycle.exists() and feed_type == default_list[1]:
        CycleAnalytics.objects.create(farm=instance.cycle.Pond.farm,
                                      pond=instance.cycle.Pond,
                                      cycle=instance.cycle,
                                      total_feed=instance_value,
                                      total_probiotics=instance_value,
                                      harvest_amount=0,
                                      extra_info={'feed_id': instance.id})
    # already_exists_pond = PondAnalytics.objects.filter(pond=instance.cycle.Pond, farm=instance.cycle.Pond.farm)
    # pond_cycles = Cycle.objects.filter(Pond=instance.cycle.Pond).values()
    # cycle_ids = []
    # for cycle in pond_cycles:
    #     cycle_ids.append(cycle['id'])
    
    # all_feed_value = 0
    # for id in cycle_ids:
    #     feed_value = Feeds.objects.filter(cycle=id).values()
    
    #     exists_feeds = 0
    #     exists_probiotics = 0
    #     if feed_type == default_list[0]:
    #         df = pd.DataFrame(feed_value)
    #         exists_feeds = df['value'].sum()
    #         all_feed_value += exists_feeds
    # print('pond_feed',all_feed_value)
    # if already_exists_pond.exists() and feed_type == default_list[0]:
    #     pond_analytics_instance = already_exists_pond.first()
    #     pond_analytics_instance.total_feed += instance.value
    #     pond_analytics_instance.save()
    # elif not already_exists_pond.exists() and feed_type == default_list[0]:
    #     PondAnalytics.objects.create(farm=instance.cycle.Pond.farm,
    #                                  pond=instance.cycle.Pond,
    #                                  total_feed=instance_value,
    #                                  harvest_amount=0,
    #                                  extra_info={'feed_id': instance.id})
    # already_exists_farm = FarmAnalytics.objects.filter(farm=instance.cycle.Pond.farm)
    # if already_exists_farm.exists() and feed_type == default_list[0]:
    #     farm_analytics_instance = already_exists_farm.first()
    #     farm_analytics_instance.total_feed = farm_analytics_instance.total_feed + instance_value
    #     farm_analytics_instance.save()
    # elif not already_exists_farm.exists() and feed_type == default_list[0]:
    #     FarmAnalytics.objects.create(farm=instance.cycle.Pond.farm,
    #                                  total_feed=instance_value,
    #                                  harvest_amount=0,
    #                                  extra_info={'feed_id': instance.id})


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
    exists_probiotics =0
    if feed_type == default_list[0]:
        df = pd.DataFrame(feed_value)
        exists_feeds = df['value'].sum()
        
    elif feed_type == default_list[0]:
        df = pd.DataFrame(feed_value)
        exists_probiotics = df['value'].sum()
    if already_exists_cycle.exists() and feed_type == default_list[0]:
        cycle_analytics_instance = already_exists_cycle.first()
        cycle_analytics_instance.total_feed = exists_feeds
        cycle_analytics_instance.save()

    if already_exists_cycle.exists() and feed_type == default_list[1]:
        cycle_analytics_instance = already_exists_cycle.first()
        cycle_analytics_instance.total_probiotics = exists_probiotics
        cycle_analytics_instance.save()
