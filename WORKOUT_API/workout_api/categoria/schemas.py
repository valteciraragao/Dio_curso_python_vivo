
from typing import Annotated

from pydantic import Field

from WORKOUT_API.contrib.schemas import BaseSchemas


class Categoria(BaseSchemas):
    nome: Annotated[str, Field(description='Nome da Categoria', examples=[
                               'Scale'], max_length=10)]
