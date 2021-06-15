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
        name = 'django-tabela'.format(env=os.environ.get('ENVIRONMENT', 'dev'))
        hash_key = 'key_partition'
        read = 10
        write = 10

    class Schema:
        key_partition = fields.String(required=True)
        carga_do_banco = fields.Dict(required=True)
        corrente = fields.String()
        tensão = fields.String()
        dados = fields.Number()
        dados2 = fields.Number()

    def say_hello(self):
        print("{dados}".format(
            dados=self.dados,
            carga_da_banco=self.carga_do_banco,
            corrente=self.corrente,
            tensão=self.tensão,

        ))


if __name__ == '__main__':
    thing = Thing.get(key_partition="key_partition")
    if thing:
        print("\nItens requiridos com sucesso:\n")
        pprint(thing.say_hello())
