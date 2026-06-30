from decimal import Decimal
from pydantic import BaseModel


class KpisDTO(BaseModel):
    gross_revenue: Decimal # receita bruta
    revenue_received: Decimal # receita recebida
    revenue_pending: Decimal # receita pendente
    revenue_canceled: Decimal # receita cancelada
    net_revenue: Decimal # receita líquida
    net_revenue_received: Decimal # receita líquida recebida
    discounts: dict # descontos totais, descontos de vendas pagas, canceladas e pendentes
    freights: dict # fretes totais, fretes de vendas pagas, canceladas e pendentes
    taxes: dict # impostos totais, impostos de vendas pagas, canceladas e pendentes
    average_ticket_overall: Decimal # ticket médio geral
    average_ticket_paid_sales: Decimal # ticket médio das vendas pagas
    quantity_sold: int # quantidade total vendida, pagas, pendentes e canceladas
    sales: dict # quantidade total de vendas, pagas, pendentes e canceladas
    recipe_per_day: dict # vendas por dia
    recipe_per_month: dict # vendas por mes
    recipe_per_year: dict # vendas por ano
    percentage_growth_between_periods: dict # crescimento percentual entre períodos
