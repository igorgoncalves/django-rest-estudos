# Generated by Django 2.0.6 on 2019-05-01 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_auto_20190425_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='foto',
            field=models.ImageField(default='', upload_to='images'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='endereco',
            name='cliente',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='enderecos', to='clientes.Cliente'),
        ),
    ]