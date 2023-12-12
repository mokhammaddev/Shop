from django.db import models
from account.models import Account


def image_path(instance, filename):
    return f"shop/{instance}/{filename}"


class Blog(models.Model):
    title = models.CharField(max_length=221)
    content = models.TextField()
    image = models.ImageField(upload_to=image_path)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    message = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username}'s comment"


class Contact(models.Model):
    name = models.CharField(max_length=221)
    email = models.EmailField(unique=True, null=True, blank=True)
    message = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
