# Generated by Django 3.2 on 2021-04-30 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(default='None', max_length=300),
        ),
        migrations.AlterField(
            model_name='order',
            name='productId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='userId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.user'),
        ),
        migrations.AlterField(
            model_name='storage',
            name='productId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.product'),
        ),
    ]