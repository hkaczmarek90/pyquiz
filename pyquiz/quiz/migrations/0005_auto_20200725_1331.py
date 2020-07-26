# Generated by Django 3.0.8 on 2020-07-25 13:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0004_test_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='test',
        ),
        migrations.AddField(
            model_name='test',
            name='quiz_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='quiz.Quiz'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='test',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
