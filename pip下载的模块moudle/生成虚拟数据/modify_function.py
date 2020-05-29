"""
install: pip install faker
function：faker自定义功能
file: modify_function.py
author: ScCcWe
time: 2019-12-28
"""
from faker import Faker

fake = Faker()

from faker.providers import BaseProvider


class Provider(BaseProvider):
    def foo(self):
        return 'bar'


fake.add_provider(Provider)

print(fake.foo())
