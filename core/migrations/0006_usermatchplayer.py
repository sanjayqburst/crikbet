# Generated by Django 3.2.8 on 2021-10-07 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_usermatches_user_points'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMatchPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_user', to='core.usermatches')),
                ('user_player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_user', to='core.players')),
            ],
        ),
    ]