from django.db import models
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.urls import reverse


class Image(models.Model):

    name = models.CharField('Navn', max_length=100)
    imagefile = models.ImageField('Bildefil', upload_to='images')

    def __str__(self):
        return self.name

    @property
    def url(self):
        return reverse('image', kwargs={'imageid': self.id})

    def image_tag(self):
        return mark_safe(f'<img style="max-width: 40%;" src="{escape(self.url)}">')
    image_tag.short_description = 'Bilde'


class Juxtaposition(models.Model):

    name = models.CharField('Navn', max_length=100)
    before = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='juxtaposition_before')
    after = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='juxtaposition_after')

    def __str__(self):
        return self.name

    @property
    def url(self):
        return reverse('juxtapose', kwargs={'juxid': self.id})

    def tag(self):
        return mark_safe(f"""
        <div class="juxtapose">
          <img src="{escape(self.before.url)}" data-label="Før">
          <img src="{escape(self.after.url)}" data-label="Etter">
        </div>
        """)
