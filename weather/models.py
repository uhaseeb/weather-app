from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class SearchHistory(models.Model):
    search = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name="search_history", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Search Histroy"
        verbose_name_plural = "Search Histories"

    def __str__(self):
        return self.search
    
class Favorites(models.Model):
    search = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name="favorites", on_delete=models.CASCADE)

    def __str__(self):
        return self.search
    