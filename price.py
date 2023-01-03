import functools
import colored
from colorama import Fore, Style
from time import sleep


@functools.lru_cache(maxsize = None) #ОЧИЩЕННЯ КЕШУ
def price():
    from binance.client import Client

    client = Client()
    Money_TRX = 1000   #ГРОШІ ЯКІ Є НА КОШИЛЬКУ
    while 1:
        TRXUSDT_p = str(client.get_symbol_ticker(symbol="TRXUSDT"))[32:-5] #ЗІБРАННЯ ДАННИХ ПРО ЦІНУ ТРХ
        TRXUSDT_n = str(client.get_symbol_ticker(symbol="TRXUSDT"))[12:-26] #ЗІБРАННЯ ДАННИХ ПРО НАЗВУ ТРХ

        BTCUSDT_p = str(client.get_symbol_ticker(symbol="BTCUSDT"))[32:-8] #ЗІБРАННЯ ДАННИХ ПРО ЦІНУ BTC
        BTCUSDT_n = str(client.get_symbol_ticker(symbol="BTCUSDT"))[12:-30] #ЗІБРАННЯ ДАННИХ ПРО НАЗВУ BTC

        TRXBTC_p = str(client.get_symbol_ticker(symbol="TRXBTC"))[31:-2] #ЗІБРАННЯ ДАННИХ ПРО ЦІНУ ТРХ ДО ВТС
        TRXBTC_n = str(client.get_symbol_ticker(symbol="TRXBTC"))[12:-25] #ЗІБРАННЯ ДАННИХ ПРО НАЗВУ ТРХ ДО ВТС

        print(f"""Назва: {TRXUSDT_n} Ціна: {TRXUSDT_p}
Назва: {BTCUSDT_n} Ціна: {BTCUSDT_p}
Назва: {TRXBTC_n} Ціна: {TRXBTC_p}""",flush=True)

#Rozpoczęcie skryptu obliczeniowego
        #     qty - КІЛЬКІСТЬ
        qtyUSDT = float(TRXUSDT_p) * Money_TRX
        qtyBTC = qtyUSDT / float(BTCUSDT_p)
        qtyTRX = qtyBTC / float(TRXBTC_p)
        result = qtyTRX - Money_TRX

        if qtyTRX > Money_TRX:
            print(Fore.LIGHTGREEN_EX + f"Заробіток TRX: {round(result,2)}"+ Style.RESET_ALL)
        if qtyTRX < Money_TRX:
            print(Fore.RED + f"Втрата TRX: {round(result,2)*(-1)}"+ Style.RESET_ALL)
        if qtyTRX == Money_TRX:
            print(Fore.YELLOW + "Безубиток"+ Style.RESET_ALL)


        price.cache_clear() #ОЧИЩЕННЯ КЕШУ
        sleep(5)
