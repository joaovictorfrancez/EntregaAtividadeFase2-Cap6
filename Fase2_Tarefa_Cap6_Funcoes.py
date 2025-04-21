import json

def carregar_dados(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def salvar_dados(insumos, nome_arquivo):
    with open(nome_arquivo, 'w') as f:
        json.dump(insumos, f, indent=4)


def cadastrar_insumo(insumos):
    nome = input("Nome do insumo: ")
    tipo = input("Tipo do insumo (ex: fertilizante, semente): ")
    unidade = input("Unidade (ex: kg, L, un): ")

    try:
        quantidade = float(input("Quantidade inicial: "))
        quantidade_min = float(input("Quantidade mínima: "))
    except ValueError:
        print("⚠️ Digite um valor numérico válido.")
        return

    insumo = {
        "nome": nome,
        "tipo": tipo,
        "unidade": unidade,
        "quantidade": quantidade,
        "quantidade_minima": quantidade_min
    }
    insumos.append(insumo)
    print("✅ Insumo cadastrado com sucesso!")


def listar_insumos(insumos):
    if not insumos:
        print("⚠️ Nenhum insumo cadastrado.")
        return

    for i, insumo in enumerate(insumos, 1):
        print(
            f"{i}. {insumo['nome']} | {insumo['quantidade']} {insumo['unidade']} (mín.: {insumo['quantidade_minima']})")


def entrada_estoque(insumos):
    listar_insumos(insumos)
    try:
        idx = int(input("Selecione o número do insumo para entrada: ")) - 1
        qtd = float(input("Quantidade a adicionar: "))
        insumos[idx]['quantidade'] += qtd
        print("✅ Entrada registrada.")
    except (IndexError, ValueError):
        print("⚠️ Operação inválida.")


def saida_estoque(insumos):
    listar_insumos(insumos)
    try:
        idx = int(input("Selecione o número do insumo para saída: ")) - 1
        qtd = float(input("Quantidade a retirar: "))
        if qtd > insumos[idx]['quantidade']:
            print("❌ Estoque insuficiente!")
        else:
            insumos[idx]['quantidade'] -= qtd
            print("✅ Saída registrada.")
    except (IndexError, ValueError):
        print("⚠️ Operação inválida.")


def gerar_alertas(insumos):
    print("\n🔔 Insumos com estoque abaixo do mínimo:")
    for insumo in insumos:
        if insumo['quantidade'] < insumo['quantidade_minima']:
            print(
                f"- {insumo['nome']}: {insumo['quantidade']} {insumo['unidade']} (mín.: {insumo['quantidade_minima']})")


def gerar_relatorio_txt(insumos, nome_arquivo='estoque.txt'):
    with open(nome_arquivo, 'w+') as f:
        for insumo in insumos:
            f.write(
                f"{insumo['nome']} - {insumo['quantidade']} {insumo['unidade']} (mín.: {insumo['quantidade_minima']})\n")
    print(f"📄 Relatório gerado em {nome_arquivo}")


import oracledb

def enviar_para_oracle(insumo):
    try:
        oracledb.init_oracle_client(lib_dir=None)

        conn = oracledb.connect(
            user="estoque",
            password="estoque123",
            dsn="192.168.15.24:1521/XEPDB1"
        )
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO insumos (nome, tipo, unidade, quantidade, quantidade_minima)
            VALUES (:1, :2, :3, :4, :5)
        """, (
            insumo["nome"],
            insumo["tipo"],
            insumo["unidade"],
            insumo["quantidade"],
            insumo["quantidade_minima"]
        ))

        conn.commit()
        cursor.close()
        conn.close()
        print("✅ Insumo enviado ao banco Oracle com sucesso!")
    except Exception as erro:
        print("❌ Erro ao enviar para o Oracle:", erro)

def listar_insumos_oracle():
    try:
        oracledb.init_oracle_client(lib_dir=None)

        conn = oracledb.connect(
            user="estoque",  # ou o usuário que você está usando
            password="estoque123",
            dsn="192.168.15.24:1521/XEPDB1"
        )

        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, tipo, unidade, quantidade, quantidade_minima FROM insumos")

        print("\n📋 Insumos cadastrados no banco Oracle:")
        resultados = cursor.fetchall()
        if not resultados:
            print("⚠️ Nenhum insumo encontrado no banco Oracle.")
        else:
            for row in resultados:
                print(f"ID: {row[0]} | Nome: {row[1]} | Tipo: {row[2]} | Unidade: {row[3]} | "
                      f"Qtd: {row[4]} | Mín.: {row[5]}")

        cursor.close()
        conn.close()
    except Exception as e:
        print("❌ Erro ao listar insumos do Oracle:", e)

def deletar_insumo_oracle():
    try:
        oracledb.init_oracle_client(lib_dir=None)

        conn = oracledb.connect(
            user="estoque",
            password="estoque123",
            dsn="192.168.15.24:1521/XEPDB1"
        )

        cursor = conn.cursor()

        # Listar antes de apagar
        cursor.execute("SELECT id, nome FROM insumos ORDER BY id")
        resultados = cursor.fetchall()

        if not resultados:
            print("⚠️ Nenhum insumo encontrado para exclusão.")
            return

        print("\n📋 Insumos disponíveis para exclusão:")
        for row in resultados:
            print(f"ID: {row[0]} | Nome: {row[1]}")

        # Solicitar o ID a ser deletado
        id_para_apagar = input("\nDigite o ID do insumo que deseja apagar: ")

        # Confirmar exclusão
        confirmacao = input(f"Tem certeza que deseja apagar o insumo ID {id_para_apagar}? (s/n): ")
        if confirmacao.lower() != 's':
            print("❌ Exclusão cancelada.")
            return

        cursor.execute("DELETE FROM insumos WHERE id = :id", {'id': id_para_apagar})
        conn.commit()

        if cursor.rowcount == 0:
            print("⚠️ Nenhum insumo com esse ID foi encontrado.")
        else:
            print(f"✅ Insumo com ID {id_para_apagar} apagado com sucesso.")

        cursor.close()
        conn.close()

    except Exception as e:
        print("❌ Erro ao apagar insumo do Oracle:", e)
