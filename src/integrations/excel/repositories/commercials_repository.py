from excel.config import DATA_PATH
from excel.repositories import BaseRepository


class CommercialsRepository(BaseRepository):
    def __init__(self):
        super().__init__(DATA_PATH)

    def _active_clients(self, **filters) -> int:
        return self.data['Cliente'].nunique()

    def _products_sold(self, **filters) -> int:
        return self.data['Produto'].nunique()

    def _categories(self, **filters) -> int:
        return self.data['Categoria'].nunique()

    def _subcategories(self, **filters) -> int:
        return self.data['Categoria'].nunique()

    def _states_served(self, **filters) -> int:
        return self.data['Estado'].nunique()

    def _active_sellers(self, **filters) -> int:
        return self.data['Vendedor'].nunique()

    def _suppliers(self, **filters) -> int:
        return self.data['Fornecedor'].nunique()

    def _payment_methods(self, **filters) -> int:
        return self.data['FormaPagamento'].nunique()

    def _cost_centers(self, **filters) -> int:
        return self.data['FormaPagamento'].nunique()

    def response(self, **filters):
        return {
            'active_clients': self._active_clients(**filters),
            'products_sold': self._products_sold(**filters),
            'categories': self._categories(**filters),
            'subcategories': self._subcategories(**filters),
            'states_served': self._states_served(**filters),
            'active_sellers': self._active_sellers(**filters),
            'suppliers': self._suppliers(**filters),
            'payment_methods': self._payment_methods(**filters),
            'cost_centers': self._cost_centers(**filters),
        }
