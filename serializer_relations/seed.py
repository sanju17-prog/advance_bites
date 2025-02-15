from faker import Faker
faker = Faker()
from .models import Singer, Song

def create_singer(n = 100):
    for _ in range(n):
        _ = Singer.objects.create(
            name=faker.name(),
            gender=faker.random_element(elements=('female','male')),
        )
    return "singers created!!"

def create_song(n = 100):
    for _ in range(n):
        singers = Singer.objects.all()
        _ = Song.objects.create(
            title=faker.sentence(nb_words=3),
            duration=faker.random_int(min=1, max=10),
            singer_id=faker.random_element(elements=singers).id,
        )
    return "songs created!!"