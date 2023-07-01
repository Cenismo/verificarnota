# Automação de Verificação de Notas - Intranet

Este é um código Python que automatiza a verificação de notas em um site da intranet. Ele utiliza as bibliotecas Selenium e Requests para interagir com o site e obter os dados necessários. Além disso, o código também utiliza a biblioteca Telebot para enviar as informações das notas para um chat do Telegram.

## Configuração

Antes de executar o código, é necessário fazer algumas configurações:

1. Certifique-se de ter o Python instalado em seu ambiente.
2. Instale as bibliotecas necessárias.
3. Crie um arquivo `.env` na mesma pasta do código e defina as seguintes variáveis de ambiente:
   - `TELEGRAM_TOKEN`: Token do bot do Telegram.
   - `TELEGRAM_CHAT_ID`: ID do chat do Telegram para enviar as mensagens.
   - `LOGIN`: Seu login para acessar o site.
   - `PASSWORD`: Sua senha para acessar o site.

## Execução

Após configurar as variáveis de ambiente, você pode executar o código Python usando o comando `python main.py` no terminal. O código irá realizar a verificação das notas da disciplina "Econometria II" e enviar uma mensagem para o chat do Telegram com o resultado.

## Dependências

O código utiliza as seguintes bibliotecas Python:

- `requests`: Utilizada para fazer requisições HTTP à API do site.
- `telebot`: Utilizada para interagir com o bot do Telegram e enviar mensagens.
- `selenium`: Utilizada para automatizar a interação com o site.
- `python-dotenv`: Utilizada para carregar as variáveis de ambiente a partir do arquivo `.env`.

Certifique-se de instalar essas bibliotecas antes de executar o código.

## Observações

- O código está configurado para rodar em modo headless, o que significa que o navegador não será aberto durante a execução. Se desejar visualizar o processo, você pode remover a opção `--headless` na configuração do Chrome.
- O tempo de espera entre as verificações está definido como 20 minutos (1200 segundos) no código (`time.sleep(1200)`). Você pode ajustar esse valor de acordo com suas necessidades.

