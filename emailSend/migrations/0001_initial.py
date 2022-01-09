# Generated by Django 3.0.7 on 2022-01-09 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddUserData',
            fields=[
                ('user_id', models.AutoField(default='', primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=122)),
                ('Enter_email_to_send', models.CharField(max_length=122)),
                ('cities', models.CharField(choices=[('mumbai', 'mumbai'), ('delhi', 'delhi'), ('bangalore', 'bangalore'), ('chennai', 'chennai'), ('kolkata', 'kolkata')], max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='SuccessFullySentEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=122)),
                ('Enter_email_to_send', models.CharField(max_length=122)),
                ('cities', models.CharField(max_length=256)),
                ('time_of_send_mail', models.DateTimeField()),
            ],
        ),
    ]
