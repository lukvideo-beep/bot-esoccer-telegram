import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
import os
from telegram import Bot

# Telegram
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
bot = Bot(token=TELEGRAM_TOKEN) if TELEGRAM_TOKEN else None

def enviar(mensagem):
    if bot and CHAT_ID:
        try:
            bot.send_message(chat_id=CHAT_ID, text=mensagem, disable_notification=False)
        except:
            pass

print("BOT IMPECÁVEL v16 - RENDER + TELEGRAM - 20/11/2025")
print("Greens caindo direto no teu celular!\n")

OVER_KINGS = ["JAB","CARNAGE","MEXICAN","YAKUZA","PABLO","GANGER_29","DMITRIY","WINSTRIKE","SATO","GROOT","ALBACK","CYPHER"]

def atualizar_kings():
    global OVER_KINGS
    try:
        r = requests.get("https://esoccerbet.org/best-players/")
        soup = BeautifulSoup(r.text, 'html.parser')
        novos = []
        for row in soup.select('table tr')[1:25]:
            cols = row.find_all('td')
            if len(cols) > 2:
                player = cols[1].text.strip().upper()
                if 3 <= len(player) <= 12:
                    novos.append(player)
        if novos:
            OVER_KINGS = novos[:20]
            enviar(f" PLAYERS ATUALIZADOS: {', '.join(OVER_KINGS[:10])}...")
    except:
        pass

ultima = 0

while True:
    try:
        if time.time() - ultima > 10800:  # 3 horas
            atualizar_kings()
            ultima = time.time()

        r = requests.get("https://esoccerbet.org/fifa-8-minutes/", timeout=15)
        soup = BeautifulSoup(r.text, 'html.parser')

        for row in soup.find_all('tr'):
            if 'vs' not in row.text: continue
            try:
                cell = row.find('a') or row.find('span')
                if not cell: continue
                texto = cell.text
                if '(' not in texto: continue

                home = texto.split('vs')[0].strip()
                away = texto.split('vs')[1].strip()
                hp = home.split('(')[-1].replace(')', '').strip().upper()
                ap = away.split('(')[-1].replace(')', '').strip().upper()

                odd = row.find_all('td')[-1].text.strip().replace('@','')
                if not odd.replace('.','').isdigit(): continue
                over35 = float(odd)

                if (hp in OVER_KINGS or ap in OVER_KINGS) and over35 >= 2.00:
                    mensagem = f"""
GREEN IMPECÁVEL v16
{home} vs {away}
Players: {hp} × {ap}
Over 3.5 gols @ {over35:.2f}
{datetime.now().strftime('%H:%M:%S')} → METE NA BETANO AGORA!!!
                    """
                    print(mensagem)
                    enviar(mensagem)
            except:
                continue

        time.sleep(16)

    except Exception as e:
        print("Erro ignorado:", e)
        time.sleep(20)
