from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
from datetime import date
from datetime import datetime
import traceback
class ConexaoEmail:
    def __init__(self):
        #TODO TRATA RETORNO DA FUNCAO CONEXAO
        self.__servidor = self.__conectar()



    def __conectar(self):
        try:
            caminho_credenciais = "C:\\RPA\\credenciais\\credenciais_gmail.txt"
            servidor_email = "smtp.gmail.com"
            porta_email = 587

            with open(caminho_credenciais, 'r') as credenciais_file:
                chaves = credenciais_file.readlines()
                if len(chaves) < 2:
                    raise ValueError("Arquivo de credenciais está incompleto.")
                self.usuario = chaves[0].strip()
                self.senha = chaves[1].strip()

            logging.info("Iniciando conexão com servidor SMTP: %s:%s", servidor_email, porta_email)
            self.conexao = smtplib.SMTP(servidor_email, porta_email)
            self.conexao.ehlo()
            self.conexao.starttls()
            self.conexao.login(self.usuario, self.senha)

            logging.info("Conexão com servidor de e-mail estabelecida com sucesso.")
            return self.conexao

        except Exception as e:
            logging.error("Erro ao tentar conectar com o servidor de e-mail: %s", e)
            logging.debug("Traceback completo:\n%s", traceback.format_exc())
            return None
        

        
    def enviar_email(self, titulo):
        #TODO RECEBER TITULO DO PARAMENTRO 
        """Monta e envia o e-mail"""
        try:
            data_atual = date.today().strftime('%d/%m/%Y')
            logging.info('Data formatada para o e-mail: %s', data_atual)

            destinatario = 'rpa.carmais@gmail.com'  # ou busque via dicionário de gestores
            assunto = f'RPA - {titulo} - {data_atual}'

            logging.info("Montando corpo do e-mail para: %s", destinatario)

            # Monta estrutura do e-mail
            message = MIMEMultipart("related")
            message['From'] = self.usuario
            message['To'] = self.usuario 
            message['Subject'] = assunto

            # Parte alternativa (HTML)
            msg_alternativa = MIMEMultipart('alternative')
            message.attach(msg_alternativa)

            corpo_html = f"""
            <html>
                <body>
                <h2>✅Bot informa que funcionou perfeitamente✅!!!! </h2>
                </body>
            </html>
            """
            msg_html = MIMEText(corpo_html, "html")
            msg_alternativa.attach(msg_html)


            # Envia o e-mail
            self.__servidor.sendmail(self.usuario, self.usuario, message.as_string())
            logging.info("E-mail enviado com sucesso para: %s", destinatario)
            print(f"Email enviado com sucesso! ")

        except Exception as e:
            logging.error("Erro ao enviar e-mail: %s", e)
            logging.debug("Traceback:\n%s", traceback.format_exc())
            print("Falha ao enviar o e-mail.")


                
            
if __name__ == "__main__":
    ConexaoEmail().__Conectar()


            

                    

    
