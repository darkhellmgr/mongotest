from djongo import models

class BlogContent(models.Model):
    comment = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    class Meta:
        abstract = True



class BlogPost(models.Model):
    h1 = models.CharField(max_length=100)
    content = models.EmbeddedModelField(
        model_container=BlogContent,
    )
    def __str__(self):
        return self.h1


class NewBlog(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

    class Meta:
        abstract = True

class Entry(models.Model):
    _id = models.ObjectIdField()
    blog = models.EmbeddedModelField(
        model_container=NewBlog,
    )