# Generated by Django 2.1.5 on 2019-03-03 01:02

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('moneybook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReceiptImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_thumbnail', imagekit.models.fields.ProcessedImageField(upload_to='receipt')),
            ],
        ),
    ]
