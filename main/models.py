from django.db import models
import uuid

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # generator ID
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField(default=0)
    description = models.TextField()

    def __str__(self):
        return self.name

    # @property
    # def is_mood_strong(self):
    #     return self.mood_intensity > 5


    # INI BElUM DI MIGRATE!!
    # Jika terjadi perubahan model
    # python manage.py makemigrations
    # python manage.py migrate
    # 