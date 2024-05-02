import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CafeWebsite.settings')
import django
django.setup()
import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from CafeApp.models import Dish


@pytest.mark.django_db
def test_create_dish():
    dish = Dish.objects.create(
        name="Test Dish",
        description="Test Description",
        category="Test Category",
        price=10,
        image=SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
    )

    assert dish.pk is not None

    assert dish.name == "Test Dish"
    assert dish.description == "Test Description"
    assert dish.category == "Test Category"
    assert dish.price == 10

    assert dish.image.name != 'default_dish.jpg'
