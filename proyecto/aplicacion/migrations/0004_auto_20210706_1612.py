# Generated by Django 3.2 on 2021-07-06 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0003_auto_20210706_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competencia',
            name='id',
        ),
        migrations.RemoveField(
            model_name='medio',
            name='id',
        ),
        migrations.RemoveField(
            model_name='publicacion',
            name='id',
        ),
        migrations.RemoveField(
            model_name='tipo_medio',
            name='id',
        ),
        migrations.AlterField(
            model_name='competencia',
            name='cod_competencia',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='medio',
            name='cod_medio',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='cod_publicacion',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tipo_medio',
            name='cod_tipo_medio',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]