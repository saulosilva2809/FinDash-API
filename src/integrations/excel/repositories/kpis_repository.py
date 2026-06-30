import pandas as pd

from decimal import Decimal

from excel.config import DATA_PATH
from excel.repositories import BaseRepository


class KpisRepository(BaseRepository):
    def __init__(self):
        super().__init__(DATA_PATH)

    def _gross_revenue(self, **filters) -> Decimal:
        return sum(
            self.data['ValorTotal']
        )
    
    def _revenue_received(self, **filters) -> Decimal:
        return sum(
            self.data.loc[
                self.data['Status'] == 'Pago',
                'ValorTotal'
            ]
        )
    
    def _revenue_pending(self, **filters) -> Decimal:
        return sum(
            self.data.loc[
                self.data['Status'] == 'Pendente',
                'ValorTotal'
            ]
        )
    
    def _revenue_canceled(self, **filters) -> Decimal:
        return sum(
            self.data.loc[
                self.data['Status'] == 'Cancelado',
                'ValorTotal'
            ]
        )
    
    def _net_revenue(self, **filters) -> Decimal:
        total_discounts = self._discounts(**filters)['total_discounts']
        total_freights = self._freights(**filters)['total_freights']
        total_taxes = self._taxes(**filters)['total_taxes']

        outputs = total_discounts + total_freights + total_taxes

        return self._gross_revenue() - outputs
    
    def _net_revenue_received(self, **filters) -> Decimal:
        paid_sales_discounts = self._discounts(**filters)['paid_sales_discounts']
        freight_paid_sales = self._freights(**filters)['freight_paid_sales']
        taxes_paid_sales = self._taxes(**filters)['taxes_paid_sales']

        outputs = paid_sales_discounts + freight_paid_sales + taxes_paid_sales

        return self._revenue_received(**filters) - outputs

    def _discounts(self, **filters) -> dict:
        total_discounts = sum(
            self.data['Desconto']
        )

        paid_sales_discounts = sum(
            self.data.loc[
                self.data['Status'] == 'Pago',
                'Desconto'
            ]
        )

        pending_sales_discounts = sum(
            self.data.loc[
                self.data['Status'] == 'Pendente',
                'Desconto'
            ]
        )

        canceled_sales_discounts = sum(
            self.data.loc[
                self.data['Status'] == 'Cancelado',
                'Desconto'
            ]
        )

        return {
            'total_discounts': total_discounts,
            'paid_sales_discounts': paid_sales_discounts,
            'pending_sales_discounts': pending_sales_discounts,
            'canceled_sales_discounts': canceled_sales_discounts,
        }
    
    def _freights(self, **filters) -> dict:
        total_freight = sum(
            self.data['Frete']
        )

        freight_paid_sales = sum(
            self.data.loc[
                self.data['Status'] == 'Pago',
                'Frete'
            ]
        )

        pending_sales_freights = sum(
            self.data.loc[
                self.data['Status'] == 'Pendente',
                'Frete'
            ]
        )

        canceled_sales_freights = sum(
            self.data.loc[
                self.data['Status'] == 'Cancelado',
                'Frete'
            ]
        )

        return {
            'total_freights': total_freight,
            'freight_paid_sales': freight_paid_sales,
            'pending_sales_freights': pending_sales_freights,
            'canceled_sales_freights': canceled_sales_freights,
        }

    def _taxes(self, **filters) -> dict:
        total_taxes = sum(
            self.data['Impostos']
        )

        taxes_paid_sales = sum(
            self.data.loc[
                self.data['Status'] == 'Pago',
                'Impostos'
            ]
        )

        pending_sales_taxes = sum(
            self.data.loc[
                self.data['Status'] == 'Pendente',
                'Impostos'
            ]
        )

        canceled_sales_taxes = sum(
            self.data.loc[
                self.data['Status'] == 'Cancelado',
                'Impostos'
            ]
        )

        return {
            'total_taxes': total_taxes,
            'taxes_paid_sales': taxes_paid_sales,
            'pending_sales_taxes': pending_sales_taxes,
            'canceled_sales_taxes': canceled_sales_taxes,
        }
    
    def _average_ticket_overall(self, **filters) -> Decimal:
        return self._gross_revenue(**filters) / self._sales(**filters)['total_sales'] 
    
    def _average_ticket_paid_sales(self, **filters) -> Decimal:
        return self._revenue_received(**filters) / self._sales(**filters)['total_sales_paid']

    def _quantity_sold(self, **filters) -> dict:
        total_quantity_sold = sum(
            self.data['Quantidade']
        )

        total_sold_paid = sum(
            self.data.loc[
                self.data['Status'] == 'Pago',
                'Quantidade'
            ]
        )

        total_sold_pending = sum(
            self.data.loc[
                self.data['Status'] == 'Pendente',
                'Quantidade'
            ]
        )

        total_sold_canceled = sum(
            self.data.loc[
                self.data['Status'] == 'Cancelado',
                'Quantidade'
            ]
        )

        return {
            'total_quantity_sold': total_quantity_sold,
            'total_sold_paid': total_sold_paid,
            'total_sold_pending': total_sold_pending,
            'total_sold_canceled': total_sold_canceled,
        }

    def _sales(self, **filters) -> dict:
        total_sales = self.data.shape[0]

        total_sales_paid = self.data.loc[
            self.data['Status'] == 'Pago',
            'ID'
        ].shape[0]

        total_pending_sales = self.data.loc[
            self.data['Status'] == 'Pendente',
            'ID'
        ].shape[0]

        total_canceled_sales = self.data.loc[
            self.data['Status'] == 'Cancelado',
            'ID'
        ].shape[0]

        return {
            'total_sales': total_sales,
            'total_sales_paid': total_sales_paid,
            'total_pending_sales': total_pending_sales,
            'total_canceled_sales': total_canceled_sales,
        }
    
    def _recipe_per_day(self, **filters) -> dict:
        df = self.data.copy()
        df['date'] = df['Data'].dt.date

        grouped = df.groupby(['date', 'Status']).agg(
            total_sales=('ID', 'nunique'),
            total_revenue=('ValorTotal', 'sum')
        ).reset_index()

        result = {}

        for _, row in grouped.iterrows():
            date = str(row['date'])
            status = row['Status']

            if date not in result:
                result[date] = {'date': date}

            result[date][status] = {
                'total_sales': int(row['total_sales']),
                'total_revenue': float(row['total_revenue'])
            }

        final_result = list(result.values())

        return final_result
   
    def _recipe_per_month(self, **filters) -> dict:
        df = self.data.copy()
        df['month'] = df['Data'].dt.to_period('M')

        grouped = df.groupby(['month', 'Status']).agg(
            total_sales=('ID', 'nunique'),
            total_revenue=('ValorTotal', 'sum')
        ).reset_index()

        result = {}

        for _, row in grouped.iterrows():
            month = str(row['month'])
            status = row['Status']

            if month not in result:
                result[month] = {'month': month}

            result[month][status] = {
                'total_sales': int(row['total_sales']),
                'total_revenue': float(row['total_revenue'])
            }

        final_result = list(result.values())

        return final_result
    
    def _recipe_per_year(self, **filters) -> dict:
        df = self.data.copy()
        df['year'] = df['Data'].dt.to_period('Y')

        grouped = df.groupby(['year', 'Status']).agg(
            total_sales=('ID', 'nunique'),
            total_revenue=('ValorTotal', 'sum')
        ).reset_index()

        result = {}

        for _, row in grouped.iterrows():
            year = str(row['year'])
            status = row['Status']

            if year not in result:
                result[year] = {'year': year}

            result[year][status] = {
                'total_sales': int(row['total_sales']),
                'total_revenue': float(row['total_revenue'])
            }

        final_result = list(result.values())

        return final_result
    
    def _percentage_growth_between_periods(self, **filters):
        df = self.data.copy()

        # cria a coluna do mes
        df['month'] = df['Data'].dt.to_period('M')

        # agrupa por mes
        grouped = (
            df.groupby('month')
            .agg(
                total_sales=('ID', 'nunique'),
                total_revenue=('ValorTotal', 'sum'),
            )
            .sort_index() # ordernar os meses
            .reset_index()
        )

        # calcula o crescimento e a receita
        grouped['growth_percentage'] = (
            grouped['total_revenue']
            .pct_change()
            .mul(100)
            .round(2)
        )

        return grouped.to_dict(orient='records')

    def response(self, **filters):
        return {
            'gross_revenue': self._gross_revenue(**filters),
            'revenue_received': self._revenue_received(**filters),
            'revenue_pending': self._revenue_pending(**filters),
            'revenue_canceled': self._revenue_canceled(**filters),
            'net_revenue': self._net_revenue(**filters),
            'net_revenue_received': self._net_revenue_received(**filters),
            'discounts': self._discounts(**filters),
            'freights': self._freights(**filters),
            'taxes': self._taxes(**filters),
            'average_ticket_overall': self._average_ticket_overall(**filters),
            'average_ticket_paid_sales': self._average_ticket_paid_sales(**filters),
            'quantity_sold': self._quantity_sold(**filters),
            'sales': self._sales(**filters),
            'recipe_per_day': self._recipe_per_day(**filters),
            'recipe_per_month': self._recipe_per_month(**filters),
            'recipe_per_year': self._recipe_per_year(**filters),
            'percentage_growth_between_periods': self._percentage_growth_between_periods(**filters)
        }
