from faker import Faker

fake = Faker()

def get_user():
    fake_user = {
        'name' : fake.name(),
        'address' : fake.address(),
        'created_at' : fake.year()
    }
    return fake_user