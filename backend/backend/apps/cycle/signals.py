from django.db.models.signals import post_save
from django.dispatch import receiver
from measurements.models import Measurement, MeasurementMaster
from feeds.models import Feeds, FeedType
from cycle.models import Cycle
from farms.models import FarmAnalytics, FeedLots
#from cycle.api.serializers import MeasurementSerializer

@receiver(post_save, sender=Cycle)
def copy_measurements(sender, instance, created, *args, **kwargs):
    if instance.pond_transfered_from:
        cycle_id = Cycle.objects.filter(Pond = instance.pond_transfered_from, is_active = True).first()
        measurement_data = Measurement.objects.filter(cycle = cycle_id)
        measure_data = list(measurement_data.values())
        if measure_data:
            for measurement in measure_data:
                # if measurement['measurement_type_id'] == 1  or measurement['measurement_type_id'] ==8:
                master = MeasurementMaster.objects.filter(id=measurement['measurement_type_id'] ).first()
                # lots = FeedLots.objects.filter(id=measurement['lot_id']).first()
                if master.measurement_type =='abw':
                    Measurement.objects.create(
                        cycle=instance,
                        measurement_type=master,
                        value=measurement['value'],
                        time=measurement['time'],
                        notes=measurement['notes'],
						created_by=measurement['created_by'],
						updated_by=measurement['updated_by']
                    )
					
        # Now insert data from feeds 
        feeding_data = Feeds.objects.filter(cycle = cycle_id)
        feed_data = list(feeding_data.values())
        if feed_data:
            for feed in feed_data:
                master = FeedType.objects.filter(id=feed['feed_type_id'] ).first()
                if master.type=='feeds':
                    Feeds.objects.create(
                        cycle=instance,
                        feed_type=master,
                        value=feed_data[0]['value'],
                        time=feed_data[0]['time'],
                        price_per_kg=feed_data[0]['price_per_kg'],
                        is_probiotic_mixed=feed_data[0]['price_per_kg'],
                        #created_by=feed_data[0]['created_by'],
                        #updated_by=feed_data[0]['updated_by']
                    )
    else:
        print('measure_data-not found')
    