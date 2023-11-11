from pyrogram import Client, filters, idle
from pyrogram.handlers import MessageHandler, EditedMessageHandler
import pickle
from random import randint
from datetime import date

from online import api_id, api_hash


with open('penis_metr', 'rb') as file:
    penis_data = pickle.load(file)


async def penisometr(client, message):
    if message.text == '/penis':
        grow = randint(1, 6)
        if message.from_user.id in penis_data.keys():
            if (date.today().day - penis_data[message.from_user.id][1].day) > 0:
                penis_data[message.from_user.id][1] = date.today()
                penis_data[message.from_user.id][0] += grow
                if message.from_user.id == 1073955978 or message.from_user.id == 888146890:
                    await message.reply_text(
                        f"Твой klitor на {grow} см. ближе к небу!\n\nТеперь он целых {penis_data[message.from_user.id][0]} см!!!",
                        quote=True)
                else:
                    await message.reply_text(f"Твой penis на {grow} см. ближе к небу!\n\nТеперь он целых {penis_data[message.from_user.id][0]}см!!!", quote=True)
            else:
                if message.from_user.id == 1073955978 or message.from_user.id == 888146890:
                    await message.reply_text(
                        f"Хватит теребить свой {penis_data[message.from_user.id][0]} см. клитор, приходи завтра", quote=True)
                else:
                    await message.reply_text(
                        f"Сегодня ты уже измерял свой стручечек {penis_data[message.from_user.id][0]} см, приходи завтра.",
                        quote=True)
        else:
            if message.from_user.id == 1073955978 or message.from_user.id == 888146890:
                penis_data[message.from_user.id] = [6, date.today()]
                await message.reply_photo(photo=r"C:\Users\robor\Downloads\photo_2023-10-12_23-12-26.jpg",
                    quote=True, caption=f"Твой klitor {penis_data[message.from_user.id][0]} см.",)
            else:
                penis_data[message.from_user.id] = [grow, date.today()]
                await message.reply_text(
                    f"Твой penis {penis_data[message.from_user.id][0]}см.\n\nНе круто, кушай больше капусты.",
                    quote=True)
        with open('penis_metr', 'wb') as file:
            pickle.dump(penis_data, file)


shutka = Client('shutka', api_id=api_id, api_hash=api_hash, device_model="iPhone 13 Pro Max",
                system_version="14.8.1",
                app_version="8.4",
                lang_code="en",
                )

shutka.add_handler(MessageHandler(penisometr, filters=filters.chat(-1001532147285)))

shutka.start()

idle()
