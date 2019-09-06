# Generated by Django 2.2.4 on 2019-08-06 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asics',
            fields=[
                ('asic', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('testbeds', models.TextField(blank=True, null=True)),
                ('short_name', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'asics',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CompletedJobs',
            fields=[
                ('submit_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('submit_date', models.DateTimeField()),
                ('submitter', models.CharField(max_length=30)),
                ('build', models.TextField()),
                ('testsuite', models.CharField(max_length=30)),
                ('testbed', models.CharField(blank=True, max_length=30, null=True)),
                ('asic', models.CharField(blank=True, max_length=30, null=True)),
                ('priority', models.PositiveIntegerField()),
                ('eta', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(max_length=9)),
                ('status_date', models.DateTimeField()),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('results', models.TextField(blank=True, null=True)),
                ('logs', models.TextField(blank=True, null=True)),
                ('final_image_path', models.TextField(blank=True, null=True)),
                ('final_issu_image_path', models.TextField(blank=True, null=True)),
                ('scheduled_testsuite', models.CharField(blank=True, max_length=30, null=True)),
                ('flags', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'completed_jobs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FlagDetails',
            fields=[
                ('flag_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('flag_id', models.CharField(max_length=3, unique=True)),
            ],
            options={
                'db_table': 'flag_details',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SubmittedJobs',
            fields=[
                ('submit_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('submit_date', models.DateTimeField()),
                ('submitter', models.CharField(max_length=30)),
                ('build', models.TextField()),
                ('testsuite', models.CharField(max_length=30)),
                ('testbed', models.CharField(blank=True, max_length=30, null=True)),
                ('asic', models.CharField(blank=True, max_length=30, null=True)),
                ('priority', models.PositiveIntegerField()),
                ('eta', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(max_length=9)),
                ('status_date', models.DateTimeField()),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('results', models.TextField(blank=True, null=True)),
                ('logs', models.TextField(blank=True, null=True)),
                ('final_image_path', models.TextField(blank=True, null=True)),
                ('final_issu_image_path', models.TextField(blank=True, null=True)),
                ('scheduled_testsuite', models.CharField(blank=True, max_length=30, null=True)),
                ('flags', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'submitted_jobs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Testbeds',
            fields=[
                ('testbed', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
                ('asic', models.CharField(max_length=10)),
                ('devicetype', models.CharField(max_length=10)),
                ('support', models.CharField(max_length=20)),
                ('status', models.CharField(blank=True, max_length=4, null=True)),
                ('lock_status', models.CharField(blank=True, max_length=8, null=True)),
                ('lock_owner', models.CharField(blank=True, max_length=30, null=True)),
                ('lock_msg', models.TextField(blank=True, null=True)),
                ('itgen_ip', models.CharField(blank=True, max_length=20, null=True)),
                ('current_job', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'testbeds',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Testsuites',
            fields=[
                ('testsuite', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('eta', models.PositiveIntegerField()),
                ('unsupported_asics', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'testsuites',
                'managed': False,
            },
        ),
    ]
