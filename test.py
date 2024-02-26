import faker
import requests
from faker import Faker
from data import Url


# def create_user():
#     payload = {'email': Faker().first_name(),
#                'password': Faker().password(length=10),
#                'name': Faker().first_name()
#                }
#
#     resource = requests.post(Url.CREATE_USER, json=payload)
#
#     print(resource.status_code)
#
#
# create_user()


def test_can_create_user():
    payload = {'email': Faker().first_name(),
               'password': Faker().password(length=10),
               'name': Faker().first_name()
               }
    response = requests.post(Url.CREATE_USER, data=payload)
    print(response.status_code)

test_can_create_user()
