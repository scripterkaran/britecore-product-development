# Generated by Django 2.0.2 on 2018-02-06 14:11

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FormTemplateField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=60)),
                ('type', models.CharField(choices=[('text', 'Text'), ('number', 'Integer'), ('date', 'Date'), ('enum', 'Multiple Choice')], max_length=10)),
                ('meta', jsonfield.fields.JSONField(blank=True, null=True)),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='risk_type.FormTemplate')),
            ],
        ),
        migrations.CreateModel(
            name='RiskType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('template', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='risk_type.FormTemplate')),
            ],
        ),
        migrations.CreateModel(
            name='RiskTypeField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=60)),
                ('type', models.CharField(choices=[('text', 'Text'), ('number', 'Integer'), ('date', 'Date'), ('enum', 'Multiple Choice')], max_length=10)),
                ('meta', jsonfield.fields.JSONField(blank=True, null=True)),
                ('risk_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='risk_type.RiskType')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='risktypefield',
            unique_together={('label', 'risk_type')},
        ),
    ]