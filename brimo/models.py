from django.db import models
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.urls import reverse


class Image(models.Model):

    class Meta:
        verbose_name = 'Bilde'
        verbose_name_plural = 'Bilder'

    name = models.CharField('Navn', max_length=100)
    imagefile = models.ImageField('Bildefil', upload_to='images')

    def __str__(self):
        return self.name

    @property
    def url(self):
        return reverse('image', kwargs={'imageid': self.id})

    def image_tag(self):
        if self.imagefile:
            return mark_safe(f'<img style="max-width: 40%;" src="{escape(self.url)}">')
        return ''
    image_tag.short_description = 'Bilde'


class Juxtaposition(models.Model):

    class Meta:
        verbose_name = 'Sammenligning'
        verbose_name_plural = 'Sammenligninger'

    name = models.CharField('Navn', max_length=100)
    before = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='juxtaposition_before', verbose_name='Før')
    after = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='juxtaposition_after', verbose_name='Etter')

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


class PortfolioCategory(models.Model):

    class Meta:
        verbose_name = 'Porteføljekategori'
        verbose_name_plural = 'Porteføljekategorier'

    name = models.CharField('Navn', max_length=100)
    short_description = models.TextField('Kort beskrivelse')
    description = models.TextField('Beskrivelse')

    def __str__(self):
        return self.name

    @property
    def url(self):
        return reverse('portfolio_category', kwargs={
            'catid': self.id,
            'slug': f'-{self.name}'
        })
