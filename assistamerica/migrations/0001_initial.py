# Generated by Django 2.0.4 on 2018-04-22 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_created=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(max_length=21)),
                ('policy_no', models.CharField(max_length=99)),
                ('insured', models.CharField(max_length=100)),
                ('end_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('end_date',),
            },
        ),
    ]
