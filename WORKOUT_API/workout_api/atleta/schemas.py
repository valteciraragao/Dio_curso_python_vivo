from typing import Annotated

from pydantic import Field, PositiveFloat
from workout_api.contrib.schemas import BaseSchemas, OutMixin


class Atleta(BaseSchemas):
    nome: Annotated[str, Field(
        description='Nome do Atleta', examples=['Joao'], max_length=50)]
    cpf: Annotated[str, Field(
        description='CPF do Atleta', examples=['12345678900'], max_length=11)]
    idade: Annotated[int, Field(
        description='Idade do Atleta', examples=[20], max_length=50)]
    peso: Annotated[PositiveFloat, Field(
        description='Peso do Atleta', examples=[75.5])]
    altura: Annotated[PositiveFloat, Field(
        description='Altura do Atleta', examples=[1.76])]
    sexo: Annotated[PositiveFloat, Field(
        description='Sexo do Atleta', examples=['M'], max_length=1)]


class AtletaIn(Atleta):
    pass


class AtletaOut(Atleta, OutMixin):
    pass
