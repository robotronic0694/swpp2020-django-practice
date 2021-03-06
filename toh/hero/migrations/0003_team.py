# Generated by Django 3.1.1 on 2020-10-15 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0002_hero_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leader_set', to='hero.hero')),
                ('members', models.ManyToManyField(related_name='teams', to='hero.Hero')),
            ],
        ),
    ]
