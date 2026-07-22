from django.db import models


class FavoriteTrain(models.Model):
    train_number = models.CharField(max_length=10)
    train_name = models.CharField(max_length=100)

    def __str__(self):
        return self.train_name


class SearchHistory(models.Model):
    train_number = models.CharField(max_length=10)
    train_name = models.CharField(max_length=100)
    searched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.train_name