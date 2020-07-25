# Generated by Django 3.0.7 on 2020-07-25 18:21

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Accounts', '0009_auto_20200725_1821'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annonce',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('budget', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('favorite', models.ManyToManyField(blank=True, related_name='favorite', to='Accounts.ProfileUser')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.ProfileUser')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='MpArtisan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ImageAnnonce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, default='image_default.jpg', null=True, upload_to='images/')),
                ('annonce_images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='Annonce.Annonce')),
            ],
        ),
    ]