from faker import Faker
import uuid
from random import randrange

fake = Faker()

class FakeData:
    first_name = fake.first_name()
    last_name  = fake.last_name()
    email = fake.ascii_email()
    phone_number = fake.msisdn()
    random_text = fake.paragraph(nb_sentences=5)
    id_number = uuid.uuid4().int
    date_of_birth = fake.date_of_birth()
    random_number = randrange(1,1000, 2)

    print([id_number, last_name, email, phone_number, random_text])
