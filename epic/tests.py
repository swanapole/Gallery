from django.test import TestCase
from .models import Image,Category,Location
# Create your tests here.

class CategoryTestCase(TestCase):

    def setUp(self):
        self.food = Category(name = 'delicacies')

    def test_instance(self):
        self.assertTrue(isinstance(self.delicacies, Category))

    def tearDown(self):
        Category.objects.all().delete()

    def test_save_category(self):
        self.delicacies.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        self.delicacies.delete_category('delicacies')
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 0)
class LocationTestCase(TestCase):
    def setUp(self):
        self.nyali = Location(name = 'Nyali')

    def test_instance(self):
        self.assertTrue(isinstance(self.sychelles, Location))

    def tearDown(self):
        Location.objects.all().delete()

    def test_save_location(self):
        self.sychelles.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_location(self):
        self.nyali.delete_location('sychelles')
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)

class ImageTestCase(TestCase):
    def setUp(self):
        # Creating a new category and saving it
        self.new_category = Category(name = 'delicacies')
        self.new_category.save_category()

        # Creat a new location and saving it
        self.new_location = Location(name = 'sychelles')
        self.new_location.save_location()

        self.new_image = Image(image_name = 'Test Image',image_description = 'Test Description',image_category = self.new_category,image_location = self.new_location)
        self.new_image.save_image()

    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()

    def test_save_image(self):
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)
