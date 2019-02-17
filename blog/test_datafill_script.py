from faker import Factory
from . import models


fake = Factory.create()

for x in range(0, 10):
    models.User.create(
        username=fake.name(),
        email=fake.free_email(),
        password=fake.password(length=10),
        firstname=fake.first_name,
        lastname=fake.last_name,
        common_experience=fake.time_delta(),
        interests_description=fake.text(),
        date_of_birth=fake.date(pattern="%Y-%m-%d"))
"""
for x in xrange(0, 10):
    #create topic
    #create MapLabel
    for y in xrange(0, 10):
        #TODO: files model, images model
        #create comments with keywords, hashtags and maplabels
        for z in xrange(0, 10):
    #randomly like or dislike
    #for couple of commnets create answers
"""
