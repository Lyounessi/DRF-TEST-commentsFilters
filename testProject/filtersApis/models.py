from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Pages(models.Model):

    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Posts(models.Model):
    content = models.TextField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField()
    time_created = models.TimeField()
    page = models.ForeignKey(Pages, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Comments(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    date_created = models.DateField()
    time_created = models.TimeField()

    def __str__(self):
        return str(self.post.id)


class Replys(models.Model):
    reply = models.TextField()
    date_created = models.DateField()
    time_created = models.TimeField()
    replied_by = models.ForeignKey(User, on_delete=models.CASCADE)
    linked_comment = models.ForeignKey(Comments, on_delete=models.CASCADE)

    def __str__(self):
        return self.replied_by


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    page = models.ForeignKey(Pages, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
