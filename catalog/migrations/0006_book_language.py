# Generated by Django 4.0.1 on 2022-01-12 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_language_alter_author_options_alter_book_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ManyToManyField(help_text='Select language for this book', to='catalog.Language'),
        ),
    ]