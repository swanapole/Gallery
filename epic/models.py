from django.db import models


class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    @classmethod
    def delete_category(cls,name):
        cls.objects.filter(name = name).delete()

class Location(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    @classmethod
    def delete_location(cls,name):
        cls.objects.filter(name = name).delete()

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length = 30)
    image_description = models.TextField()
    image_category = models.ForeignKey(Category,on_delete = models.CASCADE)
    image_location = models.ForeignKey(Location,on_delete = models.CASCADE)

    def save_image(self):
        self.save()

    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(image_category__name__contains = search_term)
        return images
