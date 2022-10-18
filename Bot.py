from telethon import TelegramClient, sync
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import time

chanels = []
chats = []

try:
    finput = open(f"Data.txt")

    index = int(finput.readline())
    api_id = int(finput.readline())
    api_hash = finput.readline()
    api_hash = api_hash.replace('\n', '')

    fchanels = open("A:/BigDeal/Release/Chanels.txt")
    fchats = open("A:/BigDeal/Release/Chats.txt")
    lines = fchanels.readlines()

    for line in lines:
        chanels.append(line.strip())

    chlines = fchats.readlines()
    for chline in chlines:
        chats.append(chline.strip())

    print("Data read done")
except Exception as ex:
    print(ex)
    time.sleep(5)
finally:
    finput.close()
    fchanels.close()
    fchats.close()

client = TelegramClient('Bot', api_id, api_hash)
client.start()
flag = False
while(not flag):
    try:
        for i in range(len(lines)):
            try:
                client(JoinChannelRequest(chanels[i]))
                print("Channels OK!")
            except Exception as ex:
                print(ex)
                time.sleep(5)
            finally:
                print("-----------------")

        for i in range(len(chlines)):
            try:
                client(ImportChatInviteRequest(chats[i]))
                print("Chat OK!")
            except Exception as ex:
                print(ex)
                time.sleep(5)
                try:
                    client(ImportChatInviteRequest(chats[i]))
                    print("Chat OK!")
                except Exception as ex:
                    print(ex)
                    time.sleep(5)
                finally:
                    print("-----------------")
            finally:
                print("-----------------")

        time.sleep(1)
        bot_link = 'ArutFreeekonomist_bot'

        try:
            client.send_message(bot_link, '/start')
            time.sleep(3)
            messages = client.get_messages('ArutFreeekonomist_bot')
            time.sleep(3)
            messages[0].click(text='Я ПОДПИСАЛСЯ(-АСЬ) ✅')
            print("Button OK!")
            getmessages = client.get_messages('goldapple_ru', limit=100)
        except Exception as ex:
            print(ex)
            messages = client.get_messages('ArutFreeekonomist_bot')
            time.sleep(3)
            messages[0].click(text='Я ПОДПИСАЛСЯ(-АСЬ) ✅')
            time.sleep(3)
            print(ex)
            print("Button Error!")
            getmessages = client.get_messages('goldapple_ru', limit=100)
            time.sleep(5)
        finally:
            print("-----------------")
        time.sleep(3)

        i = 0
        time.sleep(2)
        for message in getmessages:
            time.sleep(0.1)
            #print(message.message)
            print (str(i))
            i+=1
            try:
                getmessages[i-1].click(text='Участвую!')
                print("button OK!")
            except Exception as ex:
                print(ex)
                print("Button Error!")
            finally:
                print("-----------------")
        flag = True
    except Exception as es:
        print(es)
