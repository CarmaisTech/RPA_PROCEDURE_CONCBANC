import logging 
import os
import traceback
from src.model.banco_dados import BancoDados
from src.model.enviar_email import ConexaoEmail
from datetime import date, timedelta 


def main_concbanc():
        with open(r'C:\RPA\RPA_PROCEDURE_CONCBANC\log_rpa_procedure_concbanc.txt', 'w') as f:
                pass

        logging.basicConfig(filename=r'C:\RPA\RPA_PROCEDURE_CONCBANC\log_rpa_procedure_concbanc.txt', level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s',
                datefmt='%d/%m/%Y %I:%M:%S %p')
        banco_dados = BancoDados()
        conexao_email = ConexaoEmail()

        try:
                logging.info("EXECUTANDO PROCEDURE CONCBANK..")
                print("EXECUTANDO PROCEDURE CONCBANK..")
                data_atual = date.today()
                data_inicial = (data_atual - timedelta(5)).strftime("%m/%d/%Y")
                data_final = (data_atual - timedelta(1)).strftime("%m/%d/%Y")
        
         
                banco_dados.conectar()
                banco_dados.executar_procedure(procedure="up_concbanc_baixa_adforn",data_inicial=data_inicial,data_final=data_final)
                conexao_email.enviar_email(titulo="Procedure concbanc")
                banco_dados.fechar_conexao()
                print("Processo Finalizado")
                logging.info("Processo Finalizado")

        except:
                mgs = traceback.format_exc()
                logging.info(mgs)
                print(mgs)



    
