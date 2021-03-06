# Generated by Django 2.2.3 on 2019-07-15 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=68)),
                ('content', models.TextField(blank=True, max_length=200, null=True)),
                ('type', models.CharField(choices=[('json', 'json'), ('plaintext', 'plaintext'), ('binary', 'binary')], max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_name', models.CharField(blank=True, max_length=68)),
                ('properties', models.ManyToManyField(related_name='properties', to='api_devs_n_props.Property')),
            ],
        ),
    ]
