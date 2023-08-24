from django.db import models

# Create your models here.
class MegaMenu(models.Model):
    name = models.CharField(max_length=255,default='mega', null=False)
    use_on_fe = models.BooleanField(default=False)
    banner = models.ImageField(upload_to='megamenu_images/', blank=True, null=True)

    class Meta:
        # Define a unique constraint on the use_on_fe field to ensure only one row can have True
        constraints = [
            models.UniqueConstraint(fields=['use_on_fe'], condition=models.Q(use_on_fe=True), name='unique_active_row')
        ]

    def save(self, *args, **kwargs):
        # If the instance's use_on_fe attribute is being set to True,
        # set all other rows' use_on_fe to False before saving
        if self.use_on_fe:
            MegaMenu.objects.exclude(pk=self.pk).update(use_on_fe=False)
        super(MegaMenu, self).save(*args, **kwargs)

    def __str__(self):
        return "%s - (%s)" % (self.name, self.pk)

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    categories = models.IntegerField(blank=True, null=True)
    content = models.TextField()
    show_categories = models.BooleanField(default=True)
    level_category = models.IntegerField(default=3)
    sequence = models.IntegerField(default=1)
    
    megamenus = models.ManyToManyField(MegaMenu)
