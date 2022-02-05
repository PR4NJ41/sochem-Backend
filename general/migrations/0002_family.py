# Generated by Django 3.1.2 on 2022-02-05 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('roll_no', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('batch', models.CharField(max_length=10)),
                ('house', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
