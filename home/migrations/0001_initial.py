# Generated by Django 5.0.3 on 2024-03-09 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='handover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Shift', models.CharField(choices=[('Day', 'Day'), ('Night', 'Night')], max_length=50)),
                ('Handover_From', models.CharField(max_length=300)),
                ('Handover_To', models.CharField(max_length=300)),
                ('Tasks_In_Progress', models.TextField(blank=True, null=True)),
                ('Important_Notes', models.TextField(blank=True, null=True)),
                ('Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
