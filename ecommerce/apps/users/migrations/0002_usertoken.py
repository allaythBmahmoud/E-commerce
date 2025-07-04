# Generated by Django 4.2 on 2023-04-11 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, max_length=32, null=True, unique=True, verbose_name='Token')),
                ('token_type', models.CharField(blank=True, choices=[('su', 'SignUp token'), ('ce', 'Change email token'), ('pr', 'Password reset token')], max_length=2, null=True, verbose_name='Token type')),
                ('token_owner', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Token owner email')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Token creation date')),
                ('expired', models.BooleanField(default=False, verbose_name='Token expired')),
            ],
            options={
                'verbose_name': 'token',
                'verbose_name_plural': 'Tokens',
            },
        ),
    ]
