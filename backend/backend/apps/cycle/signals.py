from django.db.models.signals import post_save
from django.dispatch import receiver
from measurements.models import Measurement, MeasurementMaster
from feeds.models import Feeds, FeedType
from cycle.models import Cycle
from farms.models import FarmAnalytics, FeedLots


@receiver(post_save, sender=Cycle)
def copy_measurements(sender, instance, created, *args, **kwargs):
    if instance.pond_transfered_from:
        cycle_id = Cycle.objects.filter(Pond=instance.pond_transfered_from, is_active=True).first()
        measurement_data = Measurement.objects.filter(cycle=cycle_id)
        measure_data = list(measurement_data.values())
        if measure_data:
            for measurement in measure_data:
                master = MeasurementMaster.objects.filter(id=measurement['measurement_type_id']).first()
                print('measure block', measurement)
                if master.measurement_type == 'abw':
                    print('measurement data creating')
                    Measurement.objects.create(
                        cycle=instance,
                        measurement_type_id=master.id,
                        value=measurement['value'],
                        time=measurement['time'],
                        notes=measurement['notes'],
                        created_by_id=measurement['created_by_id'],
                        updated_by_id=measurement['updated_by_id']
                    )

        feeding_data = Feeds.objects.filter(cycle=cycle_id)
        feed_data = list(feeding_data.values())
        if feed_data:
            for feed in feed_data:
                master = FeedType.objects.filter(id=feed['feed_type_id']).first()
                print('feed data')
                if master.type == 'feeds':
                    print('feed data creating')
                    Feeds.objects.create(
                        cycle=instance,
                        feed_type=master,
                        value=feed_data[0]['value'],
                        time=feed_data[0]['time'],
                        price_per_kg=feed_data[0]['price_per_kg'],
                        is_probiotic_mixed=feed_data[0]['price_per_kg'],
                        created_by_id=feed_data[0]['created_by_id'],
                        updated_by_id=feed_data[0]['updated_by_id']
                    )
    else:
        print('measure_data-not found')