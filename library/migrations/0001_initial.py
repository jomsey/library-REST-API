# Generated by Django 4.1.4 on 2022-12-17 08:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the author', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title of the book', max_length=500)),
                ('book_cover', models.URLField()),
                ('description', models.TextField(help_text='Brief description of the book')),
                ('publication_date', models.DateField(help_text='Date this book was published')),
                ('type', models.CharField(choices=[('REL', 'Religion'), ('NOV', 'Novel'), ('HIS', 'History'), ('TXB', 'Text Book')], help_text='Book genre', max_length=3)),
                ('language', models.CharField(choices=[('ENG', 'English'), ('FRE', 'French'), ('ARA', 'Arabic'), ('SWA', 'Swahili')], max_length=3)),
                ('authors', models.ManyToManyField(help_text='The authors of the book', related_name='books', to='library.author')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the publisher', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='LibraryUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_taken', models.DateField(auto_now=True)),
                ('return_date', models.DateField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book')),
                ('taken_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(help_text='The publisher of the book', null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.publisher'),
        ),
    ]