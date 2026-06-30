# 📊 Especificação do Dashboard Financeiro

## Objetivo

O sistema deverá permitir que qualquer usuário faça upload de uma
planilha Excel contendo movimentações financeiras e gerar
automaticamente um dashboard completo.

> **Importante sobre o campo `Status`**
>
> Nem toda venda representa receita realizada.
>
> -   **Pago** → venda efetivamente concluída.
> -   **Pendente** → venda registrada, mas ainda não recebida.
> -   **Cancelado** → venda cancelada, não deve compor indicadores de
>     receita realizada.
>
> Sempre que aplicável, os KPIs deverão diferenciar **Receita Bruta**,
> **Receita Recebida**, **Receita Pendente** e **Receita Cancelada**.

------------------------------------------------------------------------

## Estrutura da Planilha

-   ID
-   Data
-   Ano
-   Mes
-   Dia
-   Cliente
-   Fornecedor
-   Produto
-   Categoria
-   Subcategoria
-   Quantidade
-   PrecoUnitario
-   ValorTotal
-   Desconto
-   Frete
-   Impostos
-   FormaPagamento
-   CentroCusto
-   Vendedor
-   Estado
-   Cidade
-   Tipo
-   Status

------------------------------------------------------------------------

# Filtros

Todos os componentes devem responder aos filtros:

-   Data Inicial / Final
-   Ano
-   Mês
-   Dia
-   Cliente
-   Fornecedor
-   Produto
-   Categoria
-   Subcategoria
-   Estado
-   Cidade
-   Centro de Custo
-   Forma de Pagamento
-   Vendedor
-   Tipo
-   Status

------------------------------------------------------------------------

# KPIs Financeiros

-   Receita Bruta
-   Receita Recebida (Status = Pago)
-   Receita Pendente
-   Receita Cancelada
-   Receita Líquida (ValorTotal - Desconto - Frete - Impostos)
-   Receita Líquida Recebida
-   Total de Descontos
-   Total de Fretes
-   Total de Impostos
-   Ticket Médio Geral
-   Ticket Médio das Vendas Pagas
-   Quantidade Total Vendida
-   Número Total de Vendas
-   Número de Vendas Pagas
-   Número de Vendas Pendentes
-   Número de Vendas Canceladas
-   Receita por Dia, Mês e Ano
-   Receita Acumulada
-   Crescimento percentual entre períodos

# KPIs Comerciais

-   Clientes ativos
-   Produtos vendidos
-   Categorias
-   Subcategorias
-   Estados atendidos
-   Cidades atendidas
-   Vendedores ativos
-   Fornecedores
-   Formas de pagamento
-   Centros de custo

# Rankings

-   Top 10 clientes
-   Top 10 produtos
-   Top 10 categorias
-   Top 10 vendedores
-   Top 10 estados
-   Top 10 cidades
-   Top 10 fornecedores

# Gráficos

-   Evolução da receita
-   Receita por categoria
-   Receita por produto
-   Receita por cliente
-   Receita por vendedor
-   Receita por estado
-   Receita por cidade
-   Receita por forma de pagamento
-   Receita por centro de custo
-   Distribuição por Status
-   Heatmap de faturamento
-   Mapa do Brasil por receita

# Insights

-   Receita cresceu/caiu
-   Ticket médio aumentou/diminuiu
-   Cliente com maior faturamento
-   Produto mais vendido
-   Categoria mais vendida
-   Estado com maior faturamento
-   Forma de pagamento predominante
-   Percentual de vendas pagas
-   Percentual de pendências
-   Percentual de cancelamentos
-   Tendências de crescimento e queda
-   Curva ABC de clientes
-   Curva ABC de produtos
-   Alertas de aumento de cancelamentos
-   Alertas de redução da receita recebida

# Exportação

-   PDF
-   Excel
-   CSV
-   Impressão do dashboard

# Objetivo Final

Gerar automaticamente KPIs, gráficos, rankings, comparativos, heatmaps,
mapas, tabelas e insights totalmente dinâmicos, respeitando os filtros e
o **Status** de cada transação para que indicadores financeiros reflitam
corretamente vendas pagas, pendentes e canceladas.
