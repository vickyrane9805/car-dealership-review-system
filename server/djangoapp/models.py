from django.db import models

class Dealer(models.Model):

    name = models.CharField(max_length=100)

    city = models.CharField(max_length=100)

    state = models.CharField(max_length=100)

    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Review(models.Model):

    dealer = models.ForeignKey(
        Dealer,
        on_delete=models.CASCADE
    )

    reviewer_name = models.CharField(max_length=100)

    review_text = models.TextField()

    purchase_date = models.DateField()

    def __str__(self):
        return self.reviewer_name
    
class Car(models.Model):

    make = models.CharField(max_length=100)

    model = models.CharField(max_length=100)

    year = models.IntegerField()

    def __str__(self):
        return f"{self.make} {self.model}"