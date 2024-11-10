############################### Validação de Índices de Dataset no Pandas ###############################

Este projeto permite verificar se uma cadeia informada pelo usuário representa um índice válido para datasets do Pandas em Python. A validação é feita usando uma expressão regular que cobre os padrões de índices numéricos, intervalos e nomes de colunas entre aspas.


################################ Como Executar no Google Colab ################################

1- Acesse o Google Colab em https://colab.research.google.com/.

2- No canto superior direito, clique em Arquivo > Novo notebook.

3- No novo notebook, crie uma célula de código e copie o código Python abaixo para essa célula:



################################ de Índices para Teste ################################
Abaixo estão alguns exemplos de índices para você testar manualmente no Google Colab:

Índices Válidos:
0 - Índice numérico
-5 - Índice numérico negativo
2:5 - Intervalo numérico positivo
5:-3 - Intervalo numérico positivo-negativo
'Name' - Nome de coluna com aspas simples
"Column Name" - Nome de coluna com aspas duplas e espaço
'Start':'End' - Intervalo de colunas com aspas simples
"Begin":"Finish" - Intervalo de colunas com aspas duplas
Índices Inválidos
"Some random text" - Não é um índice válido
'Invalid:Index' - Formato incorreto de aspas e nomes de coluna
"Wrong Format: - Formato incorreto com aspas duplas
Esses exemplos ajudarão você a entender quais índices são aceitos pelo programa e quais não são.

################################Observação################################
O programa foi desenvolvido para auxiliar a validação de índices de dataset no Pandas, garantindo que o formato dos índices seja compatível antes de aplicar manipulações nos dados.

