# Generated by Django 4.2.1 on 2023-05-17 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0001_initial'),
        ('aparato_electro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AparatoProveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aparatoe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aparato_electro.aparatoe')),
                ('proveedores', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedores.proveedores')),
            ],
        ),
        migrations.AddField(
            model_name='aparatoe',
            name='aparatomasProveedor',
            field=models.ManyToManyField(through='aparato_electro.AparatoProveedor', to='proveedores.proveedores', verbose_name='AparatoProveedor'),
        ),
    ]