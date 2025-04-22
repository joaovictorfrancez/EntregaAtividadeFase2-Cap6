FIAP - Faculdade de Informática e Admnistração Paulista


Sistema de Gestão de Estoque de Insumos Agrícolas

👨‍🎓 Integrantes:
João Victor Francez
Rafael Lima Jordão
Nelson Ruiz Gimenes Junior
Diego Rodrigo Bahr
Caique de Souza Maulen

👩‍🏫 Professores:
Tutor(a)
Leonardo Ruiz Orabona
Coordenador(a)
André Godoi

📜 Descrição
Esta tarefa tem como objetivo desenvolver um sistema simples, funcional e automatizado de **gestão de estoque de insumos agrícolas**, com base em Python, permitindo:

- Cadastro de insumos e definição de estoque mínimo;
- Registro de entrada e saída de produtos;
- Consulta do estoque atual;
- Alerta automático de insumos abaixo do nível mínimo;
- Armazenamento e leitura de dados em arquivos JSON;
- Geração de relatórios em arquivos .txt;
- Integração com banco de dados Oracle.


📁 Estrutura de pastas
A seguir, a organização dos arquivos e diretórios do projeto:

- Fase2_Tarefa_Cap6_Main.py

  -     Arquivo principal da aplicação. Contém o menu interativo e executa as funções do sistema.

- Tarefas/Fase2_Tarefa_Cap6_Funcoes.py

      - Módulo com todas as funções do sistema, incluindo:
    
        - Cadastro de insumos
            
        - Entrada e saída de estoque
            
        - Geração de alertas
            
        - Manipulação de arquivos JSON e TXT
            
        - Envio e exclusão de dados no banco Oracle

- estoque.json
  -     Arquivo de dados em formato JSON contendo os insumos registrados no sistema.

- estoque.txt
  -     Relatório em texto com o status atualizado do estoque, gerado automaticamente pelo sistema.

- README.md
  -     arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

- requirements.txt
  -     Arquivo opcional contendo a especificação da versão do Python utilizada no projeto (Python 3+), adotado como boa prática de versionamento.

🔧 Como executar o código

✅ Pré-requisitos

- Python 3.8 ou superior
- Oracle SQL Developer (com banco Oracle XE configurado)
  
🚀 Passo a passo 
1. Abra o terminal no PyCharm ou VSCode
2. Acesse a pasta do projeto
3. Execute o script principal
4. Navegue pelo menu no terminal:
Utilizando os números de 1 a 10 para acessar as funcionalidades:

Cadastro, movimentação e alerta de estoque

Salvar/consultar arquivos JSON e TXT

Integração com banco Oracle: inserção, listagem e exclusão



