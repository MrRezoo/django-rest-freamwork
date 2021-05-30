from django.db import models


class Car(models.Model):
    model = models.CharField(max_length=20)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.model} {self.year}'


# Create your models here.
class Person(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='users', null=True)
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name
