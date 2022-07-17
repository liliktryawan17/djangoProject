# Generated by Django 4.0.5 on 2022-07-13 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='author',
            field=models.CharField(blank=True, max_length=45),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='kategori',
            field=models.CharField(choices=[('Berita', 'Berita'), ('Jurnal', 'Jurnal'), ('Buku', 'Buku'), ('Pendidikan', 'Pendidikan'), ('Artikel', 'Artikel')], max_length=25),
        ),
    ]