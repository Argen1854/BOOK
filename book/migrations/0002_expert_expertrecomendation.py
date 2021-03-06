# Generated by Django 4.0.1 on 2022-01-23 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('activity', models.CharField(choices=[('reader', 'reader'), ('manga', 'manga'), ('writer', 'writer')], max_length=100)),
                ('information', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ExpertRecomendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expert_rec', to='book.booklist')),
                ('expert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expert_book', to='book.expert')),
            ],
        ),
    ]
