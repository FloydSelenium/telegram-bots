from importlib.abc import Finder
from telethon import TelegramClient, sync

try:
    findex = open("A:/BigDeal/Release/TempId.txt")

    index = int(findex.readline())

    finput = open(f"A:/BigDeal/Release/Bots/bot{str(index)}/Reserve/Data.txt")

    index = int(finput.readline())
    api_id = int(finput.readline())
    api_hash = finput.readline()
    api_hash = api_hash.replace('\n', '')
    print("Data read done")

finally:
    finput.close()
    findex.close()

#print("Connecting")

client = TelegramClient('Login', api_id, api_hash)
client.start()