import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

##fake script
import random
from first_app.models import AccessRecord,WebPage,Topic
from faker import Faker

fakeGen = Faker()
topics =['Search','Social','MAr','NEWS','games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(num=5):

    for entry in range(num):

        top = add_topic()
        fake_url = fakeGen.url()
        fake_date = fakeGen.date()
        fake_name = fakeGen.company()

        webpg = WebPage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
    print("populating")
    populate(10)
    print("populated")
