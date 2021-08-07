from django.db import models

"""
Post: (title, slug, content, photo, created_at, views, is_published)
Comment: (post, name, content, created_at)
"""


class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, verbose_name='URL', unique=True)
    content = models.TextField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    content = models.TimeField(max_length=1500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

    class Meta:
        ordering = ['-created_at']