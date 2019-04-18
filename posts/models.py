from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

User = get_user_model()


class Video(models.Model):
    user = models.ForeignKey(User, related_name='videos',
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=512)
    video = models.FileField(upload_to='videos/', null=True)
    date = models.DateTimeField(auto_now_add=True)
    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.PositiveIntegerField(default=0)
    category = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)

    def get_absoulte_url(self):
        return reverse_lazy('post_details', pk=self.pk)

    def __str__(self):
        return f'{self.title}'


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, related_name='votes', on_delete=models.CASCADE)
    value = models.IntegerField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user) + ':' + str(self.video) + ':' + str(self.value)

    class Meta:
        unique_together = ("user", "video", "value")


class Message(models.Model):
    name = models.CharField(max_length=512)
    email = models.CharField(max_length=512)
    message = models.CharField(max_length=1024)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
