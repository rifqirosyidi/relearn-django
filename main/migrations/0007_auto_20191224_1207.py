# Generated by Django 3.0.1 on 2019-12-24 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20191224_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_series',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.TutorialSeries', verbose_name='Series'),
        ),
    ]