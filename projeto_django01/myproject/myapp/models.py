# Marshmallow example
import os
from pprint import pprint
from dynamorm import DynaModel
from marshmallow import fields


class Thing(DynaModel):
    class Table:
        resource_kwargs = {
            'region_name': 'us-east-1'
        }
        name = 'table-teste'.format(env=os.environ.get('ENVIRONMENT', 'dev'))
        hash_key = 'hash'
        sort_key = 'sort'
        read = 10
        write = 10

    class Schema:
        key2 = fields.String()
        key1 = fields.String()
        key3 = fields.String()
        key4 = fields.String()
        hash = fields.String(required=True)
        sort = fields.String(required=True)
        coluna = fields.List(cls_or_instance=fields.Float())

    def say_hello(self):
        print("{coluna}".format(
            coluna1=self.coluna1
        ))


if __name__ == '__main__':
    thing = Thing.get(hash="hash", sort="sort")
    if thing:
        print("\nItens requiridos com sucesso:\n")
        pprint(thing.say_hello())
