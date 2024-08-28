# Generated by Django 4.2.15 on 2024-08-16 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('content', models.TextField()),
                ('published_date', models.DateTimeField(null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'My-Post',
                'verbose_name_plural': 'My-Posts',
                'ordering': ['-created_date'],
            },
        ),
    ]
