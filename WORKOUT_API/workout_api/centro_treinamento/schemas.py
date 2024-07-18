
from typing import Annotated

from pydantic import Field

from WORKOUT_API.contrib.schemas import BaseSchemas


class CentroTreinamento(BaseSchemas):
    nome: Annotated[str, Field(description='Nome do Centro de Treinamento', examples=[
                               'CT King'], max_length=20)]
    endereco: Annotated[str, Field(description='Endereço do Centro de Treinamento', examples=[
        'Av Lima 34'], max_length=60)]
    proprietario: Annotated[str, Field(description='Proprietario do Centro de Treinamento', examples=[
        'Junior'], max_length=30)]
