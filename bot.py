#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import logging
import json
from datetime import datetime
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from api import API_TRADING
from bs4 import BeautifulSoup
import requests
from emoji import emojize

# Cargar variables de entorno
load_dotenv()

# Configurar logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Funciones de los comandos
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Responde al comando /start."""
    await update.message.reply_text("¡Hola! Soy tu bot, listo para ayudarte.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Responde al comando /help."""
    await update.message.reply_text("Usa /start para comenzar y otros comandos para explorar.")

#async def shib(update: Update, context: ContextTypes.DEFAULT_TYPE):
#    """Responde al comando /shib."""
#    value = {"name": "Shiba Inu", "symbol": "SHIB", "price": "0.00001", "last_updated": datetime.now().isoformat()}
#    await print_message(update, value)

async def shib(update, context):
    """Send a message when the command /shib is issued."""
    api_trading = API_TRADING("shib")
    print(api_trading)
    value = json.loads(api_trading.trading())
    await print_message(update, value)
    #update.message.reply_text('El precio de #{symbol} es: ${price}'.format( symbol=value["symbol"],  price=value["price"]))#, "\n","Actualización: ", str(value["last_updated"]))

async def eth(update, context):
    """Send a message when the command /shib is issued."""
    api_trading = API_TRADING("eth")
    value = json.loads(api_trading.trading())
    await print_message(update, value)
    #update.message.reply_text('El precio de #{symbol} es: ${price}'.format( symbol=value["symbol"],  price=value["price"]))
    #update.message.reply_text(value)

async def hotdoge(update, context):
    """Send a message when the command /hotdoge is issued."""
    api_trading = API_TRADING("hotdoge")
    value = json.loads(api_trading.trading())
    await print_message(update, value)
    #update.message.reply_text('El precio de #{symbol} es: ${price}'.format( symbol=value["symbol"],  price=value["price"]))
    # update.message.reply_text(value)
    #update.message.reply_text('El hotdoge es una vaina vergataria Tío Joder!!')

async def doge(update, context):
    """Send a message when the command /doge is issued."""
    api_trading = API_TRADING("doge")
    value = json.loads(api_trading.trading())
    await print_message(update, value)
    #update.message.reply_text(value)

async def btc(update, context):
    """Send a message when the command /btc is issued."""
    api_trading = API_TRADING("btc")
    value = json.loads(api_trading.trading())
    await print_message(update, value)
    #update.message.reply_text(value)

async def pvu(update, context):
    """Send a message when the command /pvu is issued."""
    api_trading = API_TRADING("pvu")
    value = json.loads(api_trading.trading())
    await print_message(update, value)
    #update.message.reply_text(value)def cakeup(update, context):

async def fomobaby(update, context):
    """Send a message when the command /fomobaby is issued."""
    api_trading = API_TRADING("fomobaby")
    value = json.loads(api_trading.trading())
    await print_message(update, value)

async def pit(update, context):
    """Send a message when the command /pit is issued."""
    api_trading = API_TRADING("pit")
    value = json.loads(api_trading.trading())
    await print_message(update, value)
    #update.message.reply_text(value)

async def pit_scraper(update, context):
    """Send a message when the command /pit is issued."""
    #https://poocoin.app/tokens/0xa57ac35ce91ee92caefaa8dc04140c8e232c2e50 #PIT
    r = requests.get('https://coinmarketcap.com/currencies/pitbull')
    time.sleep(5)  # 5 seconds
    soup = BeautifulSoup(r.text, 'lxml')
    #print(soup)
    result = soup.find("div", class_="priceValue")
    print(result)
    #print("Pitbull Price: {0:.13f}".format(float(result.text[1:])))
    price = float("{0:.13f}".format(float(result.text[1:])))

    # datetime object containing current date and time
    now = datetime.now()
    print("now =", now)
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    if(price <= 0.000000000095):
        message = "Pitbull (#PIT) = "+result.text+" "+emojize(":green_heart:", use_aliases=True)+" << Compre >>\n"+dt_string
        telegram_send.send(messages=[message])
    elif price > 0.00000000010:
        message = "Pitbull (#PIT) = "+result.text+" "+emojize(":heart:", use_aliases=True)+" << Venda >>\n"+dt_string
        telegram_send.send(messages=[message])
    else:
        message = "Pitbull (#PIT) = "+result.text+" "+emojize(":blue_heart:", use_aliases=True)+" << Venda >>\n"+dt_string
        telegram_send.send(messages=[message])

    #print(soup.prettify())
    #api_trading = API_TRADING("pit")
    #value = json.loads(api_trading.trading())
    await print_message_market(update, message)
    #update.message.reply_text(value)

async def cakeup(update, context):
    """Send a message when the command /cakeup is issued."""
    api_trading = API_TRADING("cakeup")
    value = json.loads(api_trading.trading())
    await print_message(update, value)
    #update.message.reply_text(value)

async def feg(update, context):
    """Send a message when the command /feg is issued."""
    api_trading = API_TRADING("feg")
    value = json.loads(api_trading.trading())
    await print_message(update, value)
    #update.message.reply_text(value)

async def crypto(update, context):
    """Send a message when the command /feg is issued."""
    api_trading = API_TRADING(context.args[0].strip())
    value = json.loads(api_trading.trading())
    await print_message(update, value)
    #update.message.reply_text(value)

# Otras funciones de los comandos (doge, eth, etc.) pueden seguir la misma estructura

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Repite los mensajes del usuario."""
    await update.message.reply_text(update.message.text)

# Funciones auxiliares
async def print_message(update: Update, value):
    date = datetime.fromisoformat(value["last_updated"][:-1])
    date = date.strftime("%d-%m-%Y %H:%M:%S")
    variation = float(value["percent_change_1h"])
    if variation > 0:
        icon = "🟢"
    else:
        icon = "🔴"
    await update.message.reply_text(
        f'El precio de {value["name"]} (#{value["symbol"]}) es: ${value["price"]} {abs(variation)}% {icon}\nFecha: {date}'
    )

# Función principal
def main():
    """Inicia el bot."""
    # Crear la aplicación con el token
    application = Application.builder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()

    # Registrar comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("shib", shib))
    application.add_handler(CommandHandler("hotdoge", hotdoge))
    application.add_handler(CommandHandler("doge", doge))
    application.add_handler(CommandHandler("eth", eth))
    application.add_handler(CommandHandler("btc", btc))
    application.add_handler(CommandHandler("pvu", pvu))
    application.add_handler(CommandHandler("pit", pit))
    application.add_handler(CommandHandler("cakeup", cakeup))
    application.add_handler(CommandHandler("fomobaby", fomobaby))
    application.add_handler(CommandHandler("feg", feg))
    application.add_handler(CommandHandler("pit_market", pit_scraper))
    application.add_handler(CommandHandler("crypto", crypto))


    # Registrar mensajes no comandos
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Ejecutar el bot
    application.run_polling()

def print_message_market(update, value):
    update.message.reply_text(value)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


if __name__ == '__main__':
    main()
