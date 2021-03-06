from django.db import models


class Photographer(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()

    def __unicode__(self):
        return self.name + '(' + self.email + ')'


class Album(models.Model):
    Draft, Published, Archived = range(3)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=130)
    publication_date = models.DateTimeField()
    status = models.IntegerField(null=True, blank=True, default=None)
    author = models.ForeignKey(Photographer)

    def __unicode__(self):
        return self.name + ' - ' + self.author.name


class Picture(models.Model):
    image_file = models.ImageField(upload_to='uploads')
    description = models.CharField(max_length=300)
    album = models.ForeignKey(Album)
    price = models.DecimalField(max_digits=4, decimal_places=2)