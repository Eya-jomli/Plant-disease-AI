# Generated by Django 5.1.2 on 2024-10-26 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant_disease', '0003_pest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pest',
            name='type',
            field=models.CharField(choices=[('insecte', 'Insecte'), ('champignon', 'Champignon'), ('bacterie', 'Bactérie'), ('virus', 'Virus'), ('nematode', 'Nématode')], max_length=50),
        ),
        migrations.CreateModel(
            name='ControlProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('insecticide', 'Insecticide'), ('acaricide', 'Acaricide'), ('fongicide', 'Fongicide'), ('bactériostatique', 'Bactériostatique'), ('nématicide', 'Nématicide')], max_length=50)),
                ('description', models.TextField()),
                ('méthode_application', models.CharField(help_text="Méthode d'application du produit (ex: pulvérisation)", max_length=100)),
                ('efficacité', models.DecimalField(decimal_places=2, help_text='Efficacité en pourcentage', max_digits=5)),
                ('pests', models.ManyToManyField(related_name='control_products', to='plant_disease.pest')),
            ],
        ),
    ]