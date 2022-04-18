from email.message import EmailMessage
import smtplib
import time


EMAIL_LOGIN = 'contaprog01@gmail.com'
EMAIL_SENHA = 'p123456p'
EMAIL_CHEFE = 'contaprog01@gmail.com'

def enviar_email_aberto():
    mensagem = EmailMessage()
    mensagem['To'] = EMAIL_CHEFE
    mensagem['From'] = EMAIL_LOGIN
    mensagem['Subject'] = f'CHAMADO ABERTO'

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as servidor:
        servidor.login(EMAIL_LOGIN, EMAIL_SENHA)
        servidor.send_message(mensagem)

#ROTA DOIS
EMAIL_LOGIN = 'contaprog01@gmail.com'
EMAIL_SENHA = 'p123456p'
EMAIL_CHEFE = 'contaprog01@gmail.com'

def enviar_email_fechado():
    mensagem = EmailMessage()
    mensagem['To'] = EMAIL_CHEFE
    mensagem['From'] = EMAIL_LOGIN
    mensagem['Subject'] = f'CHAMADO FECHADO' + ',' +time.ctime()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as servidor:
        servidor.login(EMAIL_LOGIN, EMAIL_SENHA)
        servidor.send_message(mensagem)

