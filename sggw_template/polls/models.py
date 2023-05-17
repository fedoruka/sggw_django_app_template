from django.db import models


class Poll(models.Model):
    title = models.TextField(max_length=256)
    question = models.TextField(max_length=256)
    image_url = models.TextField(max_length=512, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"


class AnwserOption(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    text = models.TextField(max_length=256)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.poll.title} -> {self.text} ({self.votes} votes)"
