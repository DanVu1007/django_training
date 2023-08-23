# Generated by Django 4.2.3 on 2023-08-09 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MegaMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use_on_fe', models.BooleanField(default=False)),
                ('banner', models.ImageField(blank=True, null=True, upload_to='megamenu_images/')),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
                ('categories', models.IntegerField(blank=True, null=True)),
                ('content', models.TextField()),
                ('show_categories', models.BooleanField(default=True)),
                ('level_category', models.IntegerField(default=3)),
                ('sequence', models.IntegerField(default=1)),
                ('megamenus', models.ManyToManyField(to='megamenu.megamenu')),
            ],
        ),
        migrations.AddConstraint(
            model_name='megamenu',
            constraint=models.UniqueConstraint(condition=models.Q(('use_on_fe', True)), fields=('use_on_fe',), name='unique_active_row'),
        ),
    ]
