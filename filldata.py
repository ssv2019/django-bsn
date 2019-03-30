#!/usr/bin/env python
import os
import sys

from faker import Factory
from blog import models

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bsn.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

fake = Factory.create('en_US')
num_of_users = 3
num_of_posts = 3
num_of_comments = 3
num_of_answers = 2
num_of_likes = 10
num_of_dislikes = 1
num_of_maplabels = 3
num_of_hashtags = 3
num_of_keywords = 3
num_of_files = 1
num_of_images = 2

for x in range(0, num_of_users):
    username = fake.word()
    posted_by = models.User.objects.create(
        username=username,
        email=fake.free_email(),
        password=fake.password(length=10),
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        common_experience=fake.date_time(),
        interests_description=fake.text(),
        date_of_birth=fake.date(pattern="%Y-%m-%d"))
    for y in range(0, num_of_posts):
        print(y)
        topic = models.Topic.objects.create(
            header=fake.sentence(nb_words=6, variable_nb_words=True),
            content_text=fake.text(max_nb_chars=2000),
            posted_by=posted_by)
        topic_id = topic.id

        for i in range(0, num_of_images):
            models.Image.objects.create(
                user=posted_by,
                file_content="/home/ser/dev/web/bsn/bsn/media/images/palms.jpg",
                content_object=models.Topic.objects.get(id=topic_id))
        for f in range(0, num_of_files):
            models.File.objects.create(
                user=posted_by,
                file_content="/home/ser/dev/web/bsn/bsn/media/files/FILE",
                content_object=models.Topic.objects.get(id=topic_id))
        for m in range(0, num_of_maplabels):
            models.MapLabel.objects.create(
                header=fake.sentence(nb_words=6, variable_nb_words=True),
                description=fake.text(max_nb_chars=100),
                user=posted_by,
                content_object=models.Topic.objects.get(id=topic_id))
        for h in range(0, num_of_hashtags):
            models.HashTag.objects.create(
                hashtag="#" + fake.word(),
                content_object=models.Topic.objects.get(id=topic_id))
        for k in range(0, num_of_keywords):
            models.KeyWord.objects.create(
                keyword=fake.word(),
                content_object=models.Topic.objects.get(id=topic_id))
        for li in range(0, num_of_likes):
            models.Carma.objects.create(
                user=posted_by,
                content_object=models.Topic.objects.get(id=topic_id))
        for disli in range(0, num_of_dislikes):
            models.Carma.objects.create(
                user=posted_by,
                like="False",
                content_object=models.Topic.objects.get(id=topic_id))
        for c in range(0, num_of_comments):
            comment = models.Comment.objects.create(
                posted_by=posted_by,
                content_text=fake.text(max_nb_chars=200),
                content_object=models.Topic.objects.get(id=topic_id))
            comment_id = comment.id
            for like in range(0, num_of_likes):
                models.Carma.objects.create(
                    user=posted_by,
                    content_object=models.Comment.objects.get(id=comment_id))
            for dislike in range(0, num_of_dislikes):
                models.Carma.objects.create(
                    user=posted_by,
                    like="False",
                    content_object=models.Comment.objects.get(id=comment_id))
            for a in range(0, num_of_answers):
                answer = models.Comment.objects.create(
                    posted_by=posted_by,
                    content_text=fake.text(max_nb_chars=200),
                    content_object=models.Comment.objects.get(id=comment_id))
                answer_id = answer.id
                for like2 in range(0, num_of_likes):
                    models.Carma.objects.create(
                        user=posted_by,
                        content_object=models.Comment.objects.get(id=answer_id))
                for dislike2 in range(0, num_of_dislikes):
                    models.Carma.objects.create(
                        user=posted_by,
                        like="False",
                        content_object=models.Comment.objects.get(id=answer_id))
