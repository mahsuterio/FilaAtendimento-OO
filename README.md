# FilaAtendimento-OO
Projeto da matéria de Programação II que consiste em uma fila de atendimento orientado a objeto em Python. Há diversas classes para que o fluxo de atendimento de uma central funcione de forma correta, além de relatórios e análises do tempo gasto em cada atendimento.

# SISTEMA DE SIMULAÇÃO DE FILAS

O sistema simula o funcionamento de uma central de atendimento utilizando estruturas de fila, orientação a objetos e simulação em tempo discreto. O programa permite executar cenários previamente definidos em arquivos CSV ou gerar clientes aleatoriamente durante a execução. Além da simulação, o sistema coleta métricas de desempenho, registra os eventos ocorridos e gera relatórios em arquivos .txt.

---

# FUNCIONALIDADES

O sistema permite:

- simular a chegada de clientes ao longo do tempo;
- armazenar clientes em estruturas de fila;
- utilizar múltiplos atendentes;
- executar política FIFO e atendimento prioritário;
- gerar clientes a partir de arquivos CSV e aleatoriamente;
- utilizar uma seed para reproduzir experimentos;
- registrar eventos detalhados com a opção --verbose;
- calcular métricas de desempenho;
- salvar automaticamente relatórios das simulações.

---

# ESTRUTURA DO PROJETO

O projeto está organizado da seguinte maneira:

trabalho_filas/
│
├── main.py
├── configuracao.py
├── simulacao.py
├── central.py
├── cliente.py
├── atendente.py
├── fila.py
├── gerador.py
├── estatisticas.py
├── registro.py
├── relatorio.py
│
├── dados/
│   ├── cenario_fifo_10.csv
│   ├── cenario_prioridade_20.csv
│   └── cenario_prioridade_30.csv
│
├── relatorios/
│
└── tutorial e comandos/
    ├── entregáveis/

# PRINCIPAIS ARQUIVOS

- main.py: recebe e valida os argumentos da linha de comando.
- configuracao.py: armazena as configurações utilizadas na execução.
- simulacao.py: controla o tempo e coordena a execução da simulação.
- central.py: gerencia filas, atendentes e distribuição dos clientes.
- cliente.py: representa os clientes.
- atendente.py: representa os atendentes da central.
- fila.py: contém as classes Fila e FilaPrioritaria.
- gerador.py: cria clientes, atendentes e clientes aleatórios.
- estatisticas.py: calcula as métricas da simulação.
- registro.py: registra os eventos ocorridos durante a execução.
- relatorio.py: apresenta e salva os resultados em arquivos .txt.

---

# REQUISITOS

O projeto utiliza:
- Python 3
- biblioteca pandas

Para instalar o pandas, caso necessário, no terminal, digite: pip install pandas

---

# EXECUÇÃO

O programa é executado através do arquivo main.py via argumentos. No terminal, pode-se digitar:

python3 main.py --help 

para saber como digitar corretamente os argumentos e executar o programa.

---

# MODO ARQUIVO

No modo arquivo, os clientes são carregados a partir de um arquivo CSV. Nesse modo, todos os clientes existentes no arquivo são processados. A simulação continua até que todos os clientes sejam atendidos.

# FORMATO DO ARQUIVO CSV

Os arquivos devem possuir a seguinte estrutura:

id,tipo,chegada,duracao
1,comum,0,3
2,prioritario,1,2
3,tecnico,2,4

Cada coluna representa:

- id: identificador do cliente;
- tipo: tipo de cliente[comum, prioritario, tecnico];
- chegada: instante em que o cliente chega ao sistema;
- duracao: quantidade de unidades de tempo necessárias para concluir o atendimento.

---

# MODO ALEATÓRIO

No modo aleatório, clientes são gerados automaticamente durante a execução. Nesse modo, a simulação termina quando o tempo informado em --tempo é atingido, mesmo que todos os clientes nao tenham sido atendidos ou terminado de serem atendidos. Dessa forma, podem existir ao final:

- clientes já atendidos;
- clientes ainda aguardando na fila;
- clientes ainda em atendimento.

A utilização de uma --seed permite repetir a mesma sequência pseudoaleatória em diferentes execuções.

---

# ARGUMENTOS DISPONÍVEIS

Para visualizar os argumentos e sua descrição, no terminal digite:
python3 main.py --help

---

# POLÍTICAS DE ATENDIMENTO

# FIFO

Na política FIFO , os clientes são atendidos de acordo com a ordem de chegada. O primeiro cliente a entrar na fila será o primeiro a sair quando houver um atendente disponível.

Exemplo:

Cliente 1
Cliente 2
Cliente 3

Ordem de atendimento: Cliente 1 → Cliente 2 → Cliente 3

# PRIORIDADE

Na política de prioridade, clientes prioritários recebem tratamento diferenciado. A implementação utiliza alternância entre categorias de clientes para evitar que clientes comuns permaneçam esperando indefinidamente.

Um exemplo de sequência de atendimento é:

prioritario → comum → prioritario → comum → comum

A ordem de chegada dentro de cada categoria é preservada.

------------------------------------------------------------------------------------------------------------------

# SIMULAÇÃO E TEMPO

A simulação ocorre em unidades discretas de tempo, a cada unidade são realizadas etapas:

1. verificar a chegada de novos clientes;
2. inserir os clientes na fila;
3. processar os atendimentos em andamento;
4. verificar atendimentos concluídos;
5. liberar atendentes;
6. retirar clientes da fila;
7. iniciar novos atendimentos;
8. registrar estatísticas da simulação.

Exemplo de eventos registrados:
[000] Simulação iniciada
[000] Cliente 1 chegou
[000] Cliente 1 entrou na fila
[000] Atendente 1 iniciou atendimento do Cliente 1
[002] Cliente 1 terminou atendimento

Ao utilizar --verbose, o programa apresenta os eventos da simulação no terminal. Ao final da execução, o sistema calcula diferentes métricas.

------------------------------------------------------------------------------------------------------------------

# MÉTRICAS

# CLIENTES

São registrados:

- clientes que chegaram;
- clientes atendidos;
- clientes aguardando;
- clientes ainda em atendimento.

# TEMPO DE ESPERA

O tempo de espera de cada cliente é calculado por: tempo_inicio_atendimento - tempo_chegada

O sistema apresenta:
- espera média;
- espera mínima;
- espera máxima.

# TEMPO NO SISTEMA

O tempo total de um cliente no sistema é: tempo_fim_atendimento - tempo_chegada

# FILA

São registrados:
- tamanho médio da fila;
- tamanho máximo da fila.

# UTILIZAÇÃO DOS ATENDENTES

A utilização de cada atendente é calculada a partir da relação entre seu tempo ocupado e o tempo total da simulação, por exemplo:

Atendente 1: 82.50%
Atendente 2: 75.00%
Atendente 3: 32.50%

# VAZÃO

A vazão representa a quantidade de clientes que concluíram o atendimento por unidade de tempo: 
vazão = clientes atendidos / tempo simulado

-------------------------------------------------------------------------------------------------------------

# RELATÓRIOS

Cada execução gera automaticamente um arquivo .txt na pasta relatórios.

Os relatórios armazenam:
- configurações utilizadas;
- eventos da simulação (--verbose);
- métricas finais.

No modo arquivo, os nomes seguem o formato: `[entrada]_[politica]_[atendentes].txt`
Exemplo: cenario_fifo_10_FIFO_2.txt


No modo aleatório: `[politica]_[seed]_[tempo]_[atendentes].txt`
Exemplo: prioridade_42_40_3.txt

-- Caso já exista um relatório com o mesmo nome, um novo nome é gerado para evitar a sobrescrita do arquivo.

---

# CENÁRIOS DE ENTRADA

Foram preparados três cenários para testes reproduzíveis:

-- Cenário 1

10 clientes
Política: FIFO
Tipos: comum

Arquivo: dados/cenario_fifo_10.csv

-- Cenário 2

20 clientes
Política: prioridade
Tipos: comum e prioritario 

Arquivo: dados/cenario_prioridade_20.csv

-- Cenário 3

30 clientes
Política: prioridade
Tipos: comum, prioritario e tecnico

Arquivo: dados/cenario_prioridade_30.csv

---

# EXEMPLO DE RESULTADOS

Uma execução pode produzir uma saída no terminal e no relatório gerado:

--- RESULTADOS DA SIMULAÇÃO ---

Tempo simulado: 20
Clientes que chegaram: 9
Clientes atendidos: 8
Clientes aguardando: 0
Clientes em atendimento: 1

Espera média: 0.11
Espera mínima: 0
Espera máxima: 1

Tempo médio no sistema: 2.50

Tamanho médio da fila: 0.05
Tamanho máximo da fila: 1

Utilização dos atendentes:
Atendente 1: 60.00%
Atendente 2: 40.00%

Vazão: 0.40 clientes/unidade de tempo

---

# TESTES

O projeto possui testes destinados à validação dos componentes e da simulação. Também foram criados cenários em arquivos CSV para permitir a reprodução das execuções. Na pasta tutorial e comandos há arquivos .txt com as instruções argparse para colocar no terminal e executar a simulação. Exemplos:

-- FIFO com arquivo

python3 main.py --modo arquivo --entrada "dados\cenario_fifo_10.csv" --tempo 0 --atendentes 2 --prob-chegada 0 --tempo-min 0 --tempo-max 0 --prioritarios 0 --politica FIFO --seed 0 --verbose

-- Simulação aleatória com prioridade

python3 main.py --modo aleatorio --tempo 40 --atendentes 3 --prob-chegada 0.60 --tempo-min 1 --tempo-max 5 --prioritarios 0.30 --politica prioridade --seed 42 --verbose

---

# AUTORES

Projeto da disciplina de Programação II — Ciência de Dados — UFSC, 
desenvolvido por Marcela Gianini Sutério - 26101578.
