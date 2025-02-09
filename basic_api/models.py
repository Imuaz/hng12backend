from django.db import models

class User(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    github_url = models.URLField()

    def __str__(self):
        return self.email