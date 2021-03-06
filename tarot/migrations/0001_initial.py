# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-09-22 00:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_published', models.BooleanField()),
                ('published_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='GenericCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('image_link', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creator_only', models.BooleanField()),
                ('name', models.CharField(max_length=100)),
                ('number', models.PositiveIntegerField(blank=True, null=True)),
                ('custom_designation', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MajorArcana',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('image_link', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creator_only', models.BooleanField()),
                ('number', models.IntegerField(choices=[(0, 'The Fool'), (1, 'The Magician'), (2, 'The High Priestess'), (3, 'The Empress'), (4, 'The Emperor'), (5, 'The Hierophant'), (6, 'The Lovers'), (7, 'The Chariot'), (8, 'Strength'), (9, 'The Hermit'), (10, 'Wheel of Fortune'), (11, 'Justice'), (12, 'The Hanged Man'), (13, 'Death'), (14, 'Temperance'), (15, 'The Devil'), (16, 'The Tower'), (17, 'The Star'), (18, 'The Moon'), (19, 'The Sun'), (20, 'Judgement'), (21, 'The World')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MinorArcana',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('image_link', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creator_only', models.BooleanField()),
                ('suit', models.IntegerField(choices=[(1, 'Swords'), (2, 'Cups'), (3, 'Wands'), (4, 'Pentacles')])),
                ('rank', models.IntegerField(choices=[(1, 'Ace'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five'), (6, 'Six'), (7, 'Seven'), (8, 'Eight'), (9, 'Nine'), (10, 'Ten'), (11, 'Page'), (12, 'Knight'), (13, 'Queen'), (14, 'King')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit_line', models.TextField()),
                ('copyright_owner', models.TextField()),
                ('copyright_status', models.IntegerField()),
                ('hide_from_searches', models.BooleanField()),
                ('allow_pinning', models.BooleanField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='minorarcana',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tarot.Profile'),
        ),
        migrations.AddField(
            model_name='minorarcana',
            name='decks',
            field=models.ManyToManyField(to='tarot.Deck'),
        ),
        migrations.AddField(
            model_name='majorarcana',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tarot.Profile'),
        ),
        migrations.AddField(
            model_name='majorarcana',
            name='decks',
            field=models.ManyToManyField(to='tarot.Deck'),
        ),
        migrations.AddField(
            model_name='genericcard',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tarot.Profile'),
        ),
        migrations.AddField(
            model_name='genericcard',
            name='decks',
            field=models.ManyToManyField(to='tarot.Deck'),
        ),
        migrations.AddField(
            model_name='deck',
            name='curator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tarot.Profile'),
        ),
    ]
