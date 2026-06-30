# 📊 Requisitos do Dashboard Financeiro

## Objetivo

O dashboard tem como objetivo transformar uma planilha Excel em uma ferramenta completa de análise financeira, fornecendo indicadores, gráficos, tabelas e insights que auxiliem na tomada de decisão.

---

# 1. Indicadores (KPIs)

Os KPIs devem ficar posicionados na parte superior da tela para fornecer uma visão rápida da situação financeira.

## Financeiros

* Receita Total
* Despesas Totais
* Lucro Líquido
* Margem de Lucro (%)
* Ticket Médio
* Quantidade Vendida
* Total de Transações
* Clientes Ativos
* Total de Fornecedores
* Contas em Aberto
* Cancelamentos
* Valor Total de Impostos

---

# 2. Evolução Financeira

### Objetivo

Apresentar a evolução da empresa ao longo do tempo.

### Dados necessários

* Data
* Receita
* Despesa
* Lucro

### Visualização

Gráfico de linhas contendo:

* Receita por dia
* Receita por semana
* Receita por mês
* Receita por ano

---

# 3. Receita x Despesa

### Objetivo

Comparar receitas e despesas ao longo do tempo.

### Visualização

Gráfico de barras contendo:

* Receita
* Despesa
* Lucro

Agrupados por período.

---

# 4. Distribuição das Despesas

### Objetivo

Mostrar onde a empresa está gastando dinheiro.

### Agrupamentos

* Categoria
* Centro de Custo

### Visualização

Gráfico Pizza ou Donut.

---

# 5. Fluxo de Caixa

### Objetivo

Mostrar o comportamento financeiro da empresa.

### Informações

* Entradas
* Saídas
* Saldo acumulado

### Visualização

Gráfico de linha.

---

# 6. Receita por Estado

### Objetivo

Mostrar quais estados geram maior faturamento.

### Dados

* Estado
* Valor Total

### Visualização

Mapa do Brasil.

---

# 7. Receita por Cidade

### Objetivo

Exibir o faturamento por cidade.

### Visualização

Ranking Top 10.

---

# 8. Top Clientes

### Objetivo

Identificar os clientes mais importantes.

### Informações

* Cliente
* Receita
* Quantidade de Pedidos

### Visualização

Tabela.

---

# 9. Produtos Mais Vendidos

### Objetivo

Mostrar os produtos com maior desempenho.

### Informações

* Produto
* Quantidade Vendida
* Receita
* Lucro

### Visualização

Tabela.

---

# 10. Formas de Pagamento

### Objetivo

Identificar os meios de pagamento mais utilizados.

### Dados

* PIX
* Cartão
* TED
* Dinheiro
* Boleto

### Visualização

Gráfico Pizza ou Donut.

---

# 11. Centro de Custo

### Objetivo

Mostrar quais setores apresentam maiores despesas.

### Visualização

Gráfico de barras.

---

# 12. Ranking de Vendedores

### Objetivo

Comparar o desempenho comercial.

### Informações

* Vendedor
* Receita
* Quantidade de Pedidos
* Ticket Médio

### Visualização

Tabela.

---

# 13. Calendário Financeiro

### Objetivo

Descobrir padrões de vendas durante o mês.

### Visualização

Heatmap (Calendário).

---

# 14. Cancelamentos

### Objetivo

Analisar perdas financeiras.

### Informações

* Quantidade
* Percentual
* Valor perdido

---

# 15. Impostos

### Objetivo

Acompanhar os impostos pagos.

### Visualização

Gráfico por mês.

---

# 16. Quantidade Vendida

### Objetivo

Mostrar o volume de produtos vendidos ao longo do tempo.

### Visualização

Gráfico de barras ou linha.

---

# 17. Filtros

O dashboard deve permitir filtrar todas as informações por:

* Ano
* Mês
* Dia
* Cliente
* Produto
* Categoria
* Subcategoria
* Estado
* Cidade
* Centro de Custo
* Vendedor
* Forma de Pagamento
* Tipo (Receita ou Despesa)
* Status

---

# 18. Tabela Completa

Uma tabela contendo todos os registros da planilha.

## Funcionalidades

* Pesquisa
* Ordenação
* Paginação
* Exportação para CSV

---

# 19. Insights Inteligentes

O sistema deverá gerar automaticamente análises sobre os dados.

## Exemplos

* Receita aumentou X% em relação ao período anterior.
* Receita caiu X%.
* Marketing aumentou seus gastos em X%.
* O cliente X representa Y% da receita total.
* PIX representa Z% dos recebimentos.
* O vendedor X foi o que mais faturou.
* A margem média foi de X%.
* As maiores vendas acontecem em determinado dia da semana.
* Existe concentração de receita em poucos clientes.
* Tendências e possíveis riscos financeiros.

---

# 20. Exportação

Permitir exportar os resultados em:

* PDF
* Excel
* CSV

Além da opção de impressão do dashboard.

---

# Dados necessários na planilha

## Informações temporais

* Data
* Ano
* Mês
* Dia

## Informações financeiras

* Receita
* Despesa
* Valor Total
* Desconto
* Frete
* Impostos

## Clientes

* Cliente

## Produtos

* Produto
* Categoria
* Subcategoria
* Quantidade

## Organização

* Centro de Custo
* Vendedor
* Fornecedor

## Localização

* Estado
* Cidade

## Pagamentos

* Forma de Pagamento

## Controle

* Tipo
* Status

---

# Objetivo Final

O dashboard deve oferecer uma visão executiva e operacional da empresa, permitindo que qualquer usuário faça upload de uma planilha Excel e obtenha automaticamente:

* KPIs financeiros
* Gráficos interativos
* Rankings
* Comparativos
* Filtros dinâmicos
* Tabela completa das transações
* Insights automáticos
* Exportação de relatórios

O foco é transformar dados brutos em informações úteis para apoiar decisões estratégicas e operacionais.
