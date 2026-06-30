import pandas as pd

from abc import ABC, abstractmethod
from decimal import Decimal


class BaseRepository(ABC):
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = self._read_raw_excel()
        self._handle_numbers()

    def _read_raw_excel(self) -> pd.DataFrame:
        try:
            return pd.read_excel(self.file_path, engine='openpyxl')
        except Exception as e:
            print(f'Error reading file {self.file_path}: {e}')
            return pd.DataFrame()
        
    def _handle_numbers(self):
        for column in [
            'PrecoUnitario',
            'ValorTotal',
            'Desconto',
            'Frete',
            'Impostos',
        ]:
            self.data[column] = self.data[column].map(lambda x: Decimal(str(x)))

    @abstractmethod
    def response(self, **filters) -> list[dict] | dict:
        pass
