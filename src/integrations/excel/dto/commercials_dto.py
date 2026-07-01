from pydantic import BaseModel


class CommercialsDTO(BaseModel):
    active_clients: int # clientes ativos
    products_sold: int # produtos vendidos
    categories: int # categorias
    subcategories: int # subcategorias
    states_served: int # estados atendidos
    active_sellers: int # vendedores ativos
    suppliers: int # fornecedores
    payment_methods: int # formas de pagamento
    cost_centers: int # centros de custo
