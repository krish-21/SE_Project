# Generated by Django 3.1.3 on 2020-11-20 21:56

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateConfirmed', models.DateField()),
                ('caseType', models.CharField(choices=[('Local', 'Local'), ('Imported', 'Imported')], max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=300)),
                ('x', models.FloatField(default=0.0)),
                ('y', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=80)),
                ('idNumber', models.CharField(max_length=20)),
                ('dateOfBirth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Virus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('commonName', models.CharField(max_length=50)),
                ('maxInfectiousPeriod', models.CharField(max_length=3)),
            ],
            options={
                'verbose_name_plural': 'Viruses',
            },
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateFrom', models.DateField()),
                ('dateTo', models.DateField()),
                ('category', models.CharField(choices=[('Visit', 'Visit'), ('Residence', 'Residence'), ('Workplace', 'Workplace')], max_length=20)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.case')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.location')),
            ],
        ),
        migrations.AddField(
            model_name='case',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.patient'),
        ),
        migrations.AddField(
            model_name='case',
            name='virus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.virus'),
        ),
        migrations.CreateModel(
            name='StaffUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('chpStaffNumber', models.CharField(max_length=7, unique=True, verbose_name='CHP Stuff Number')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
