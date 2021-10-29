# Generated by Django 3.2.8 on 2021-10-26 15:19

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('watchlist_app', '0004_watchlist_platform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watchlist', to='watchlist_app.streamplatform'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('description', models.CharField(max_length=200, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('review_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('watchlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='watchlist_app.watchlist')),
            ],
        ),
    ]
