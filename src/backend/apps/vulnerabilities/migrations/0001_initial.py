# Generated by Django 4.0.5 on 2022-06-19 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CVE',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('published', models.DateField()),
                ('modified', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CWE',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('name', models.TextField()),
                ('abstraction', models.CharField(max_length=100)),
                ('structure', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('extended_description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('url', models.URLField(max_length=300, unique=True)),
                ('cve', models.ManyToManyField(to='vulnerabilities.cve')),
            ],
        ),
        migrations.CreateModel(
            name='Vector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vector', models.TextField(max_length=44)),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.FloatField(max_length=5, unique=True)),
                ('cve', models.ManyToManyField(to='vulnerabilities.cve')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('reference_data', models.ManyToManyField(to='vulnerabilities.reference')),
            ],
        ),
        migrations.CreateModel(
            name='Refsource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('reference_data', models.ManyToManyField(to='vulnerabilities.reference')),
            ],
        ),
        migrations.CreateModel(
            name='Format',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('format', models.CharField(max_length=20, unique=True)),
                ('cve', models.ManyToManyField(to='vulnerabilities.cve')),
            ],
        ),
        migrations.CreateModel(
            name='CVSSV2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.FloatField(max_length=5)),
                ('access_vector', models.CharField(choices=[('NETWORK', 'network'), ('LOCAL', 'local')], max_length=20)),
                ('access_complexity', models.CharField(choices=[('LOW', 'low'), ('HIGH', 'high')], max_length=20)),
                ('authentication', models.CharField(choices=[('NONE', 'none'), ('SINGLE', 'single')], max_length=20)),
                ('confidentiality_impact', models.CharField(choices=[('HIGH', 'high'), ('PARTIAL', 'partial'), ('COMPLETE', 'complete'), ('NONE', 'none')], max_length=20)),
                ('integrity_impact', models.CharField(choices=[('NONE', 'none'), ('HIGH', 'high'), ('PARTIAL', 'partial'), ('COMPLETE', 'complete')], max_length=20)),
                ('availability_impact', models.CharField(choices=[('COMPLETE', 'complete'), ('PARTIAL', 'partial'), ('NONE', 'none')], max_length=20)),
                ('base_score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('vector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vulnerabilities.vector')),
            ],
        ),
        migrations.CreateModel(
            name='CVSS3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.FloatField(max_length=5)),
                ('attack_vector', models.CharField(choices=[('NETWORK', 'network'), ('LOCAL', 'local')], max_length=20)),
                ('attack_complexity', models.CharField(choices=[('LOW', 'low'), ('HIGH', 'high')], max_length=20)),
                ('privileges_required', models.CharField(choices=[('NONE', 'none'), ('LOW', 'low')], max_length=20)),
                ('user_interaction', models.CharField(choices=[('NONE', 'none')], max_length=20)),
                ('scope', models.CharField(choices=[('UNCHANGED', 'unchanged')], max_length=20, null=True)),
                ('confidentiality_impact', models.CharField(choices=[('HIGH', 'high'), ('PARTIAL', 'partial'), ('COMPLETE', 'complete'), ('NONE', 'none')], max_length=20)),
                ('integrity_impact', models.CharField(choices=[('NONE', 'none'), ('HIGH', 'high'), ('PARTIAL', 'partial'), ('COMPLETE', 'complete')], max_length=20)),
                ('availability_impact', models.CharField(choices=[('COMPLETE', 'complete'), ('PARTIAL', 'partial'), ('NONE', 'none')], max_length=20)),
                ('base_score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('base_severity', models.CharField(choices=[('CRITICAL', 'critical'), ('HIGH', 'high'), ('CRITICAL', 'critical')], max_length=20)),
                ('vector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vulnerabilities.vector')),
            ],
        ),
        migrations.AddField(
            model_name='cve',
            name='cwe',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='vulnerabilities.cwe'),
        ),
        migrations.CreateModel(
            name='CPEMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_vulnerable', models.BooleanField()),
                ('uri', models.CharField(max_length=80, unique=True)),
                ('cve', models.ManyToManyField(to='vulnerabilities.cve')),
            ],
        ),
        migrations.CreateModel(
            name='BaseMetricV3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exploitability_score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('impact_score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cve', models.ManyToManyField(to='vulnerabilities.cve')),
                ('cvss_v3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vulnerabilities.cvssv2')),
            ],
        ),
        migrations.CreateModel(
            name='BaseMetricV2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('severity', models.CharField(choices=[('HIGH', 'high'), ('MEDIUM', 'medium'), ('LOW', 'low')], max_length=20)),
                ('exploitability_score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('impact_score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('is_obtain_all_privilege', models.BooleanField()),
                ('is_obtain_user_privilege', models.BooleanField()),
                ('is_obtain_other_privilege', models.BooleanField()),
                ('is_user_interaction_required', models.BooleanField()),
                ('cve', models.ManyToManyField(to='vulnerabilities.cve')),
                ('cvss_v2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vulnerabilities.cvssv2')),
            ],
        ),
        migrations.CreateModel(
            name='Assigner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('cve', models.ManyToManyField(to='vulnerabilities.cve')),
            ],
        ),
    ]
