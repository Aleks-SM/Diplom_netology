# Generated by Django 5.0.3 on 2024-05-06 16:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_user_type_alter_user_is_active_alter_user_username'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'Заказанная позиция', 'verbose_name_plural': 'Список позиций'},
        ),
        migrations.CreateModel(
            name='ConfirmEmailToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания token-a')),
                ('key', models.CharField(db_index=True, max_length=64, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='confirm_email_token', to=settings.AUTH_USER_MODEL, verbose_name='')),
            ],
            options={
                'verbose_name': 'Токен потверждения email',
                'verbose_name_plural': 'Токены потверждения',
            },
        ),
    ]
