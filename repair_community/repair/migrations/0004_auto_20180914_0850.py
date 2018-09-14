# Generated by Django 2.1.1 on 2018-09-14 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0003_auto_20180914_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('00', 'not assigned'), ('01', 'assigned'), ('02', 'waiting for device'), ('03', 'recived'), ('04', 'under repair'), ('05', 'under testing'), ('06', 'repair complete'), ('07', 'shipped back to client'), ('08', 'case closed')], default='00', max_length=2),
        ),
    ]
