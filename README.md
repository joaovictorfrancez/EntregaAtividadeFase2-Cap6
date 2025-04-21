![image](https://github.com/user-attachments/assets/8b01d4b0-7067-4ffd-92cd-939f6d2821fa)




# 🧪 Projeto: Sistema de Gestão de Estoque de Insumos Agrícolas

## 🌱 Contextualização

O agronegócio é um dos setores mais importantes da economia brasileira, responsável por grande parte do PIB nacional. Um dos desafios enfrentados pelos produtores rurais, especialmente os pequenos e médios, está na **gestão de insumos agrícolas**, como sementes, fertilizantes e defensivos.

A ausência de ferramentas tecnológicas acessíveis para esse fim pode resultar em:
- Falta de controle da quantidade disponível,
- Perdas financeiras por vencimento de produtos,
- Interrupção de processos produtivos por falta de insumos no momento certo.

## 💡 Solução Proposta

Esta tarefa tem como objetivo desenvolver um sistema simples, funcional e automatizado de **gestão de estoque de insumos agrícolas**, com base em Python, permitindo:

- Cadastro de insumos e definição de estoque mínimo;
- Registro de entrada e saída de produtos;
- Consulta do estoque atual;
- Alerta automático de insumos abaixo do nível mínimo;
- Armazenamento e leitura de dados em arquivos JSON;
- Geração de relatórios em arquivos .txt;
- Simulação de integração com banco de dados Oracle.

As funcionalidades foram definidas de acordo com a solicitação da tarefa "Cap 6 - Python e além".


## 🧰 Tecnologias e Conteúdos Aplicados

Tomamos com o base para este projeto os ensinamentos obtidos nos conteúdos dos capítulos 3, 4, 5 e 6 da Fase 2 "Campo da inovação - Uma plantação de códigos" do curso FIAP, com aplicação prática:

- ✅ **Subalgoritmos (funções)**: Modularização de ações como cadastro, movimentação de estoque e geração de relatórios;
- ✅ **Estruturas de dados**: Uso de listas e dicionários para controle dos insumos;
- ✅ **Manipulação de arquivos**: Leitura e escrita de dados em arquivos JSON e TXT;
- ✅ **Conexão com banco de dados (Oracle)**: Simulação de envio dos dados ao banco.

## 🛠️ Funcionalidades da Aplicação

- `Cadastrar novo insumo`
- `Registrar entrada de estoque`
- `Registrar saída de estoque`
- `Consultar todos os insumos`
- `Exibir alerta de estoque baixo`
- `Salvar dados em JSON`
- `Gerar relatório em TXT`
- `Simular envio de dados ao banco Oracle`

## 🗂️ Estrutura do Projeto
A seguir, a organização dos arquivos e diretórios do projeto:

- main.py

  -     Arquivo principal da aplicação. Contém o menu interativo e executa as funções do sistema.

- Tarefas/Fase2_Tarefa_Cap6_Funcoes.py

      - Módulo com todas as funções do sistema, incluindo:
    
        - Cadastro de insumos
            
        - Entrada e saída de estoque
            
        - Geração de alertas
            
        - Manipulação de arquivos JSON e TXT
            
        - Simulação de envio ao banco Oracle''

- estoque.json
  -     Arquivo de dados em formato JSON contendo os insumos registrados no sistema.

- estoque.txt
  -     Relatório em texto com o status atualizado do estoque, gerado automaticamente pelo sistema.

- README.md
  -     Documento de apresentação do projeto, com explicações sobre o problema, a solução proposta, funcionalidades implementadas e instruções de execução.

- requirements.txt
  -     Arquivo opcional contendo a especificação da versão do Python utilizada no projeto (Python 3+), adotado como boa prática de versionamento.
