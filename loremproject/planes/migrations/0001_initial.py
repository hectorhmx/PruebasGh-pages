# Generated by Django 2.0.5 on 2018-05-12 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Degrees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Titulo')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('image', models.ImageField(blank=True, null=True, upload_to='courses', verbose_name='Imagen')),
                ('url', models.URLField(max_length=100, verbose_name='URL')),
                ('clave', models.IntegerField(verbose_name='Clave')),
            ],
            options={
                'verbose_name': 'plan_estudio',
                'verbose_name_plural': 'planes_estudio',
                'ordering': ['clave'],
            },
        ),
    ]
