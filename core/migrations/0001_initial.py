# Generated by Django 3.2.8 on 2021-10-07 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=255)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_belong', to='core.teams')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_name', models.CharField(max_length=255)),
                ('match_time', models.DateTimeField()),
                ('away_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_away', to='core.teams')),
                ('home_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_home', to='core.teams')),
            ],
        ),
    ]
