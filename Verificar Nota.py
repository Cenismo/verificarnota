import os
import time
import requests
import telebot
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv

load_dotenv()

# Carregar os valores das variáveis de ambiente
TOKEN = os.getenv("TELEGRAM_TOKEN")  # Token do bot do Telegram
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")  # ID do chat do Telegram para enviar as mensagens
LOGIN = os.getenv("LOGIN")  # Meu login para acessar o site
PASSWORD = os.getenv("PASSWORD")  # Minha senha para acessar o site

bot = telebot.TeleBot(TOKEN)

# Função para enviar mensagem para o chat do Telegram
def enviar_mensagem(mensagem):
    bot.send_message(CHAT_ID, mensagem)

while True:
    # Configurar o Chrome para rodar sem cabeçalho
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    # Inicializar o driver do Chrome
    driver = webdriver.Chrome(executable_path="C:\\Users\\pablo\\Downloads\\ChromeDriver\\chromedriver.exe", options=chrome_options)
    driver.get("https://intranet.fucape.br/webapp/public/autenticacao?tipoUsuario=1")

    # Localizar o campo de login e preencher
    login_field = driver.find_element_by_name("login")
    login_field.send_keys(LOGIN)

    # Localizar o campo de senha e preencher 
    password_field = driver.find_element_by_name("password")
    password_field.send_keys(PASSWORD)

    # Enviar o formulário de login
    password_field.send_keys(Keys.RETURN)

    time.sleep(5)

    # Fazer a requisição para a API com as credenciais autenticadas
    url = "https://intranet.fucape.br/webapp/api/boletim/disciplinas?anoLetivo=2023&periodoLetivo=1"
    cookies = driver.get_cookies()
    session = requests.Session()

    for cookie in cookies:
        session.cookies.set(cookie['name'], cookie['value'])

    response = session.get(url)

    if response.status_code == 200:
        data = response.json()
        for disciplina in data:
            if disciplina['descricao'] == 'Econometria II':
                etapas = disciplina['etapas']
                for etapa in etapas:
                    if etapa['sigla'] == '2B':
                        if etapa['nota'] is not None:
                            mensagem = "Saiu"
                        else:
                            mensagem = "Não saiu"
                        enviar_mensagem(mensagem)
                        break
    else:
        enviar_mensagem(f"Erro na solicitação: {response.status_code}")

    # Fechar o navegador
    driver.quit()

    # Aguardar 20 minutos antes de fazer a próxima verificação
    time.sleep(1200)
