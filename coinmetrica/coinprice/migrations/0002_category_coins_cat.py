# Generated by Django 4.2.4 on 2023-11-11 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coinprice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='coins',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='coinprice.category'),
        ),
    ]
