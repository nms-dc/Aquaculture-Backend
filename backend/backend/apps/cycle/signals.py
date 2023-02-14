from django.db.models.signals import post_save
from django.dispatch import receiver
from measurements.models import Measurement, MeasurementMaster
from cycle.models import Cycle
from farms.models import FarmAnalytics
#from cycle.api.serializers import MeasurementSerializer

@receiver(post_save, sender=Cycle)
def copy_measurements(sender, instance, created, *args, **kwargs):
    print('hello world from cycle siganls')
   
    if instance.pond_transfered_from:
        cycle_id = Cycle.objects.filter(Pond = instance.pond_transfered_from, is_active = True).first()
        measurement_data = Measurement.objects.filter(cycle = cycle_id)
        measure_data = list(measurement_data.values())
        print('measure_data',measure_data)
        if measure_data:
            print(measure_data)
            for measurement in measure_data:
                # if measurement['measurement_type_id'] == 1  or measurement['measurement_type_id'] ==8:
                master = MeasurementMaster.objects.filter(id =measurement['measurement_type_id'] ).first()
                print('measurement_type',master)
                if master.measurement_type=='feeds'  or master.measurement_type=='abw':
                    Measurement.objects.create(
                        cycle=instance,
                        measurement_type=master,
                        value=measurement['value'],
                        time=measurement['time'],
                        lot=measurement['lot_id'],
                        price_per_kg=measurement['price_per_kg'],
                        notes=measurement['notes'],
                        is_probiotic_mixed=measurement['is_probiotic_mixed']
                    )
    else:
        print('measure_data-not found')
        

        
        
        
    