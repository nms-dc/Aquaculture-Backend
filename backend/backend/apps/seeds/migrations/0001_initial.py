# Generated by Django 3.2.14 on 2022-10-04 13:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Seeds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.IntegerField(null=True)),
                ('date_received', models.CharField(max_length=400, null=True)),
                ('number_of_eggs', models.IntegerField(null=True)),
                ('createdAt', models.DateTimeField(auto_now=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('date_sold', models.DateTimeField()),
                ('date_hatched', models.DateTimeField()),
                ('qr_code_id', models.IntegerField(null=True)),
                ('quality', models.CharField(default='good', max_length=400, null=True)),
                ('weight', models.IntegerField(null=True)),
                ('price', models.IntegerField(null=True)),
                ('seed_company_id', models.IntegerField(null=True)),
                ('purchased_by_companyid', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
        ),
        migrations.CreateModel(
            name='SeedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(null=True, upload_to='seedpicture_uploads')),
                ('fish_ids', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fish_id', to='seeds.seeds')),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
