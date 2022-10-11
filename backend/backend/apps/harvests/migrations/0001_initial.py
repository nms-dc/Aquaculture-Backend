# Generated by Django 3.2.14 on 2022-10-04 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        ('cycle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Harvests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('harvest_type', models.CharField(choices=[('F', 'Full Harvest'), ('P', 'Partial Harvest')], default='F', max_length=400, null=True)),
                ('total_kgs', models.IntegerField(default=0, null=True)),
                ('is_chill_kill', models.BooleanField(default=True)),
                ('harvest_date', models.DateField(auto_now=True)),
                ('temperature', models.IntegerField(default=0, null=True)),
                ('harvest_notes', models.CharField(default='1', max_length=400, null=True)),
                ('harvest_cost', models.IntegerField(default=0, null=True)),
                ('animal_count_1', models.IntegerField(default=0, null=True)),
                ('total_kg_1', models.IntegerField(default=0, null=True)),
                ('price_kg_1', models.IntegerField(default=0, null=True)),
                ('cycle', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cycle.cycle')),
                ('sold_to', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
        ),
        migrations.CreateModel(
            name='HarvestPondImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=400, null=True)),
                ('image', models.FileField(null=True, upload_to='pond_images')),
                ('images', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pond_images', to='harvests.harvests')),
            ],
        ),
        migrations.CreateModel(
            name='HarvestLogisticImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=400, null=True)),
                ('image', models.FileField(null=True, upload_to='log_images')),
                ('images', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='log_images', to='harvests.harvests')),
            ],
        ),
        migrations.CreateModel(
            name='HarvestAnimalImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=400, null=True)),
                ('image', models.FileField(null=True, upload_to='ani_images')),
                ('images', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ani_images', to='harvests.harvests')),
            ],
        ),
        migrations.CreateModel(
            name='AddAnimal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal_count', models.IntegerField(default=0, null=True)),
                ('total_kg', models.IntegerField(default=0, null=True)),
                ('price_kg', models.IntegerField(default=0, null=True)),
                ('adding_animal', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='animal_images', to='harvests.harvests')),
            ],
        ),
    ]
