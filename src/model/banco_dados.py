import pymssql
from dotenv import load_dotenv
import os
import logging
from datetime import date, timedelta
from traceback import format_exc
load_dotenv()
class BancoDados:
    def __init__(self):
        self.localhost = os.getenv("LOCALHOST")
        self.user = os.getenv("USER")
        self.senha = os.getenv("SENHA")
        self.banco = os.getenv("BANCO")
        self.cursor = ""
        self.dataAtual = date.today()

    def conectar(self) -> None:
        try:
            self.conn = pymssql.connect(self.localhost, self.user, self.senha, self.banco)
            self.cursor = self.conn.cursor()
            logging.info("Conexão com banco de dados estabelecida com sucesso.")
            print("Conexão com banco de dados estabelecida com sucesso.")
        except Exception as e:
            logging.error(f"Erro ao tentar conectar com o banco de dados: {e}")
            print("Erro ao tentar conectar com o banco de dados. Veja o log para detalhes.")
            print(format_exc())
            logging.error(format_exc())

    def executar_procedure(self,procedure, data_inicial, data_final) -> None:
        if not self.cursor:
            logging.warning("Cursor não inicializado. Conectando automaticamente...")
            self.conectar()

        # data_inicial = (self.dataAtual - timedelta(days=5)).strftime("%m/%d/%Y")
        # data_final = (self.dataAtual - timedelta(days=1)).strftime("%m/%d/%Y")

        print(f"Executando procedure: {procedure} de {data_inicial} até {data_final}")
        logging.info(f"Executando procedure: {procedure} de {data_inicial} até {data_final}")
        try:
            self.cursor.execute(f"EXEC {procedure} '{data_inicial}', '{data_final}'")
            self.conn.commit()
            print("Procedure executada com sucesso.")
            logging.info("Procedure executada com sucesso.")
        except Exception as e:
            logging.error("Erro ao executar procedure.")
            logging.error(format_exc())
            print("Erro ao executar procedure. Verifique os logs para mais detalhes.")

    def fechar_conexao(self) -> None:
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        logging.info("Conexão com banco de dados encerrada.")


