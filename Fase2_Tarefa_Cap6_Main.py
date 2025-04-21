from Tarefas.Fase2_Tarefa_Cap6_Funcoes import *
import oracledb

ARQUIVO_JSON = 'estoque.json'

def menu():
    print("""
==== Sistema de Gestão de Insumos Agrícolas ====

1 - Cadastrar novo insumo
2 - Entrada de estoque 
3 - Saída de estoque JSON
4 - Consultar estoque JSON
5 - Gerar alerta de estoque baixo - JSON
6 - Salvar dados
7 - Gerar relatório em .txt
8 - Listar estoque no banco de dados (Oracle)
9 - Apagar insumo no banco de dados (Oracle)
0 - Sair
""")

def main():
    insumos = carregar_dados(ARQUIVO_JSON)

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_insumo(insumos)
            enviar_para_oracle(insumos[-1])
        elif opcao == '2':
            entrada_estoque(insumos)
        elif opcao == '3':
            saida_estoque(insumos)
        elif opcao == '4':
            listar_insumos(insumos)
        elif opcao == '5':
            gerar_alertas(insumos)
        elif opcao == '6':
            salvar_dados(insumos, ARQUIVO_JSON)
        elif opcao == '7':
            gerar_relatorio_txt(insumos)
        elif opcao == '8':
            listar_insumos_oracle()
        elif opcao == '9':
            deletar_insumo_oracle()
        elif opcao == '0':
            print("Encerrando...")
            break
        else:
            print("⚠️ Opção inválida.")

if __name__ == "__main__":
    main()
