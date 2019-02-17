from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # username = models.CharField("nick", max_length=100, unique=True)
    # email = models.EmailField("email", max_length=254)
    # password = models.CharField("password", max_length=254)
    # name = models.CharField("name", max_length=100, blank=True)
    # first_name = models.CharField("firstname", max_length=100, blank=True)
    # last_name = models.CharField("lastname", max_length=100, blank=True)
    middle_name = models.CharField("middlename", max_length=100, blank=True, null=True)
    common_experience = models.DateField("common experience", blank=True, null=True)
    interests_description = models.TextField("interests description", blank=True, null=True)
    date_of_birth = models.DateField("date of birth", blank=True, null=True)
    # created_datetime = models.DateField("creation datetime", auto_now_add=True)
    last_modified_datetime = models.DateTimeField("last modified datetime", auto_now=True)
    # relations

    # meta
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Topic(models.Model):
    header = models.CharField("header", max_length=254)
    content_text = models.TextField("topic text")
    allow_comments = models.BooleanField("allow comments", default=True)
    creation_datetime = models.DateTimeField("creation datetime", auto_now_add=True)
    last_modified_dateime = models.DateTimeField("last modified datetim", auto_now=True)
    # relations
    posted_by = models.ForeignKey(User, verbose_name="related user", on_delete=models.CASCADE)
    # show_for = models.ManyToManyField(User, verbose_name="related posts")

    # meta
    class Meta:
        verbose_name = "Topic"
        verbose_name_plural = "Topics"


class Comment(models.Model):
    content_text = models.TextField("comment text")
    allow_comments = models.BooleanField("allow comments", default=True)
    creation_datetime = models.DateTimeField("creation datetime", auto_now_add=True)
    last_modified_datetime = models.DateTimeField("last modified datetime", auto_now=True)
    # relations
    posted_by = models.ForeignKey(User, verbose_name="related user", on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, verbose_name="related object", on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    # meta
    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"


class File(models.Model):
    file_content = models.FileField(upload_to="files/")
    # relations
    user = models.ForeignKey(User, verbose_name="related user", on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, verbose_name="related object", on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    # meta
    class Meta:
        verbose_name = "File"
        verbose_name_plural = "Files"


class Image(models.Model):
    file_content = models.ImageField(upload_to="images/")
    # relations
    user = models.ForeignKey(User, verbose_name="related user", on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, verbose_name="related object", on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    # meta
    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"


class Carma(models.Model):
    like = models.BooleanField("likes", default=True)
    # relations
    user = models.ForeignKey(User, verbose_name="related user", on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, verbose_name="related object", on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    # meta
    class Meta:
        verbose_name = "Carma"
        verbose_name_plural = "Carmas"


class MapLabel(models.Model):
    # coordinates = ...db_index=True
    header = models.CharField("header", max_length=100, db_index=True)
    description = models.TextField("description", blank=True, null=True)
    creation_datetime = models.DateTimeField("creation datetime", auto_now_add=True)
    last_modified_datetime = models.DateTimeField("last modified datetime", auto_now=True)
    # relations
    user = models.ForeignKey(User, verbose_name="related user", on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, verbose_name="related object", on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    # meta
    class Meta:
        verbose_name = "MapLabel"
        verbose_name_plural = "MapLabels"


class KeyWord(models.Model):
    keyword = models.SlugField("keyword", max_length=100, db_index=True)
    # relations
    content_type = models.ForeignKey(ContentType, verbose_name="related object", on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    # meta
    class Meta:
        verbose_name = "KeyWord"
        verbose_name_plural = "KeyWords"


class HashTag(models.Model):
    hashtag = models.SlugField("hashtag", max_length=100, db_index=True)
    # relations
    content_type = models.ForeignKey(ContentType, verbose_name="related object", on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    # meta
    class Meta:
        verbose_name = "HashTag"
        verbose_name_plural = "HashTags"


# to remove
"""
class NewsWall(models.Model):
    last_update_datetime = models.DateTimeField("last update datetime", auto_now=True)
    # relations
    user = models.OneToOneField(User, verbose_name="related user")
    topics = models.ManyToManyField(Topic, verbose_name="related topics")

    # meta
    class Meta:
        verbose_name = "NewsWall"
        verbose_name_plural = "NewsWalls"
"""
