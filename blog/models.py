from django.db import models
from django.utils.text import slugify


class postModel(models.Model):
    author = models.CharField(max_length=45, blank=True)
    judul = models.CharField(max_length=50)
    categories = (
        ('Berita', 'Berita'),
        ('Jurnal', 'Jurnal'),
        ('Buku', 'Buku'),
        ('Pendidikan', 'Pendidikan'),
        ('Artikel', 'Artikel')
    )
    kategori = models.CharField(max_length=25, choices=categories)
    konten = models.TextField()
    slug = models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.judul)
        super(postModel, self).save()

    def __str__(self):
        return '{}. {}'.format(self.id, self.judul)
