from django.db import models


categories = (
    ('Technology','Techonology'),
    ('Business', 'Business'),
    ('World News','World News'),
    ('Sesign','Design'),
)

class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, default='Anonymous')
    category = models.CharField(max_length=200, choices=categories, default='technology')
    description = models.CharField(max_length=1000, default='')
    text = models.TextField(max_length=10000)
    pub_date = models.DateTimeField('data published')