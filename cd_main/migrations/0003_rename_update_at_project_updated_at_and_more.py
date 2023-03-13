# Generated by Django 4.1.7 on 2023-03-13 19:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cd_main', '0002_rename_creation_date_project_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='date_of_birth',
            new_name='birth_date',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='full_name',
            new_name='fullname'
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(help_text='Enter project description', max_length=8192),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(help_text='Enter project title', max_length=127),
        ),
        migrations.AlterField(
            model_name='projecttypes',
            name='code',
            field=models.CharField(max_length=127),
        ),
        migrations.AlterField(
            model_name='projecttypes',
            name='title',
            field=models.CharField(max_length=127),
        ),
        migrations.AlterField(
            model_name='skill',
            name='code',
            field=models.CharField(max_length=127),
        ),
        migrations.AlterField(
            model_name='skill',
            name='title',
            field=models.CharField(max_length=127),
        ),
    ]
