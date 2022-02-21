# Generated by Django 3.1.14 on 2022-02-21 03:15

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='EduBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(default='none', max_length=255)),
                ('author', models.CharField(default='none', max_length=255)),
                ('publisher', models.CharField(default='none', max_length=255)),
                ('publish_date', models.DateTimeField(blank=True, null=True)),
                ('right_price', models.BigIntegerField(blank=True, null=True)),
                ('sales_price', models.BigIntegerField(blank=True, null=True)),
                ('isbn', models.BigIntegerField(blank=True, null=True)),
                ('url', models.CharField(default='none', max_length=1024)),
                ('page', models.BigIntegerField(blank=True, null=True)),
                ('crawl_date', models.DateTimeField(blank=True, null=True)),
                ('edu_tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EduMetadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('market', models.CharField(default='none', max_length=255)),
                ('rank', models.BigIntegerField(blank=True, null=True)),
                ('sales_point', models.BigIntegerField(blank=True, null=True)),
                ('crawl_date', models.DateTimeField(blank=True, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edu_book.edubook')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]