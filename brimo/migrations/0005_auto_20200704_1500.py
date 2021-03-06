# Generated by Django 3.0.8 on 2020-07-04 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brimo', '0004_auto_20200704_1440'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': 'Bilde', 'verbose_name_plural': 'Bilder'},
        ),
        migrations.AlterModelOptions(
            name='juxtaposition',
            options={'verbose_name': 'Sammenligning', 'verbose_name_plural': 'Sammenligninger'},
        ),
        migrations.AlterModelOptions(
            name='portfoliocategory',
            options={'verbose_name': 'Porteføljekategori', 'verbose_name_plural': 'Porteføljekategorier'},
        ),
        migrations.AddField(
            model_name='portfoliocategory',
            name='short_description',
            field=models.TextField(default='', verbose_name='Kort beskrivelse'),
            preserve_default=False,
        ),
    ]
