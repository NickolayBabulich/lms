# Generated by Django 4.2.7 on 2023-11-16 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0006_alter_payments_payment_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usr', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]