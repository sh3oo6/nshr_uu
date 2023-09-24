from telethon import TelegramClient
from telethon import TelegramClient, events, Button, errors
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.sync import TelegramClient, events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.sessions import StringSession
import asyncio, json, os, re
api_id = 2192036
api_hash = '3b86a67fc4e14bd9dcfc2f593e75c841'
bot_token = '6496026190:AAGZIYS_bMfjI7YX1tlV50NQ33YgzbrxiXs'

# We have to manually call "start" if we want an explicit bot token
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

# But then we can use the client instance as usual
async def Add_NUMBER(event, api_id, api_hash, phone_numbe):
    try:
        phone_number = phone_numbe.replace('+', '').replace(' ', '')
        iqthon = TelegramClient(phone_numbe, api_id, api_hash)
        await iqthon.connect()

        if not await iqthon.is_user_authorized():
            request = await iqthon.send_code_request(phone_number)

            async with bot.conversation(event.chat_id, timeout=300) as conv:
                # verification code
                await conv.send_message("__ارسل الكود الذي وصلك.. ضع علامة ( - ) بين كل رقم:__")
                response_verification_code = await conv.get_response()
                verification_code = str(response_verification_code.message).replace('-', '')

                try:
                    login = await iqthon.sign_in(phone_number, code=int(verification_code))
                except errors.SessionPasswordNeededError:
                    await conv.send_message("__الحساب محمي بكلمة السر, ارسل كلمة السر :__")
                    password = await conv.get_response()

                    await iqthon.sign_in(phone_number, password=password.text)
                    await iqthon.disconnect()

        return "تم اضافة الرقم بنجاح ✅"
    except Exception as error:
        return str(error)


@bot.on(events.CallbackQuery(data="add_number"))
async def Callbacks(event):
    await event.delete()
    try:
        # get information from user
        async with bot.conversation(event.chat_id, timeout=300) as conv:
            await conv.send_message('Api i ?')
            api_id_msg = await conv.get_response()
            api_id = api_id_msg.text

            await conv.send_message('Api hash ?')
            api_hash_msg = await conv.get_response()
            api_hash_msg = api_hash_msg.text

            await conv.send_message('Phone number ?')
            phone_number_msg = await conv.get_response()
            phone_number_msg = phone_number_msg.text
            open('prift.txt' , 'w').write(phone_number_msg)
            await conv.send_message(f'''
Api i : `{api_id}`
Api hash : `{api_hash_msg}`
Phone number : `{phone_number_msg}`

جاري تسجيل الدخول
''')

        result = await Add_NUMBER(event, int(api_id), api_hash_msg, phone_number_msg)
        await event.reply(result)
        c = os.popen(f"screen -S {phone_number_msg} -dm bash -c 'python3 Dex_nshr.py; exec sh'")
        print(c)
        if c:
            try:
                await event.edit(c.read())
            except:
                await event.edit('True')
        else:
            try:
                await event.edit(c.errors)
            except:
                await event.edit("False")
    except Exception as error:
        pass
async def StartButtons(event, role):
    if role == 1:
        buttons = [[Button.inline("➕", "add_number")]]
    await event.reply("›:ُِ 𝗗َِ𝗘َِ𝗫.#¹ :)", buttons=buttons)


# BOT START
@bot.on(events.NewMessage(pattern='/start'))
async def BotOnStart(event):
    await StartButtons(event,1)
bot.run_until_disconnected()
