# Generated by Django 4.2.7 on 2024-02-04 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0005_remove_student_name_alter_student_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='Category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobapp.category'),
        ),
    ]
