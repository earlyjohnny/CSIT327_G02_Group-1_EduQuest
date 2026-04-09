from django.db import models

class Announcement(models.Model):
    headline = models.CharField(max_length=255)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

class Feedback(models.Model):
    rating = models.IntegerField()
    comments = models.TextField()
    submission_date = models.DateTimeField(auto_now_add=True)

class Document(models.Model):
    file_name = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    file_type = models.CharField(max_length=50, blank=True)
    file_size = models.IntegerField(blank=True, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.file:
            self.file_type = self.file.name.split('.')[-1]  # gets extension
            self.file_size = self.file.size  # gets file size in bytes
        super().save(*args, **kwargs)