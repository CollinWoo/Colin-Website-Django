from django.db import models
from django import forms
from django.core.validators import FileExtensionValidator
import mimetypes
from mdeditor.fields import MDTextField

# Create your models here.
class ProjectCard(models.Model):

    #caption fields
    img_caption = models.CharField("Card Name", max_length=10, help_text = 'What does this card represent?')
    show_caption = models.BooleanField(default = True)

    #media fields
    media = models.FileField(
        "Video or Image Background",
        null = True,
        blank = True,
        upload_to = 'card_image',
        validators = [FileExtensionValidator(allowed_extensions=['mp4', 'jpg', 'jpeg', 'png'])],
    )
    extension = models.CharField("Background File Extension", max_length = 50, null = True, blank = True)
    is_img = models.BooleanField("Is the background an image", null = True, blank = True)

    description = models.CharField(max_length=200, help_text='Enter Description')
    link = models.URLField(help_text = 'Enter where this card links to', null = True, blank = True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    
    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.img_caption

    def get_media_extension(self):
        #gets the MIME type of the uploaded media file
        mime = self.media.file.content_type

        #converts MIME type to file extension
        extension = mimetypes.guess_extension(mime)

        return extension

    def is_image(self):
        if self.extension in ['.jpg', '.jpeg', '.png']:
            return True
        elif self.extension == '.mp4':
            return False
        #if the uploaded file does not have a valid file extension, return the null value
        else:
            return None

    def save(self, *args, **kwargs):
        self.is_img = self.is_image()
        super(ProjectCard, self).save(*args, **kwargs)
        
    #def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        #return reverse('model-detail-view', args=[str(self.id)])

class DescriptionPage(models.Model):
    title = models.CharField(max_length=500)
    slug = models.CharField(unique=True,max_length=500, primary_key = True)
    content = MDTextField()

    def __str__(self):
        return self.slug
    
