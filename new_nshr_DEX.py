from telethon.sync import TelegramClient, events
import asyncio
import re , requests
try:
    client = open('prift.txt', 'r').read().replace('\n', '')
    DEX = TelegramClient('dex1' , 22160733, 'c95e81b40eba3404ac130f4a9f235e4c')
    DEX.connect()
except Exception as k : print(k)
@DEX.on(events.NewMessage(outgoing=True, pattern="x"))
async def Dex1(event):
    try:
        information = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
        sleeptime = information[0]
        messagess = information[1]
        text = information[2]
        await event.delete()
        fo = open(f'{client}.txt', 'w')
        fo.write('on')
        fo.close()
    except:
        await event.edit('طريقة تفعيل النشر خاطأ\nيرجئ تطبيق الاوامر والشرح بشكل صحيح\nلعرض الاوامر فقط اكتب ( الاوامر )')
    for _ in range(int(messagess)) :
        try:
            file = open(f'{client}.txt', 'r')
            if 'on' in file.read():
                await event.client.send_message(event.chat_id, text)
                file.close()
                await asyncio.sleep(int(sleeptime))
            elif 'off' in file.read():
                file.close()
                break
        except:pass
# # # # # #
@DEX.on(events.NewMessage(outgoing=True, pattern='User'))
async def _(event):
    information = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    print(information)
    user = re.sub(r'@', '', information[0])
    p = requests.get(f"https://fragment.com/username/{user}").text
    if "On auction" in p or 'Available' in p:
        await event.edit(' مرفوع مزاد✅ ')
    elif 'Sold' in p:
        await event.edit(' مرفوع ومباع ايضا في المزاد✅ ')
    elif 'Taken' in p:
        await event.edit(' ما مرفوع مزاد❎ ')


@DEX.on(events.NewMessage(pattern='id'))
async def _(event):
    try:
        me = await DEX.get_me()
        id = me.id
        await event.edit(str(id))
    except:pass


@DEX.on(events.NewMessage(pattern="s"))
async def _(event):
    open(f'{client}.txt', 'w').write('off')
    await event.edit('''تم توقيف النشر انتضر بقدر الوقت المضاف للنشر 
لعدم حدوث اخطاء في التوقيف''')

@DEX.on(events.NewMessage(pattern="f"))
async def _(event):
    await event.edit('''•————————•
Welcame 
السورس شغال بدون اخطاء
Channel : @iiiNil
•————————•''')

@DEX.on(events.NewMessage(pattern="الاوامر"))
async def _(event):
    await event.edit('''للنشر :
 اكتب x بعدها الوقت بين رسالة ورسالة بعدها عدد الرسائل
بعدها تكتب رسالتك ( الكليشة ) ، مثال 
x 300 100 ( كليشتك )

لتوقيف النشر  :
اكتب حرف s لتوقيف النشر ويجب الانتضار وقت بقد الوقت المضاف للنشر قبل البدأ بالنشر الجديد 
يعني :  يجب الانتضار 300 ثانية لاننا كتبنا في المثال 300 ثانية لكي نبدأ بالنشر الجديد 

للفحص اكتب f 

اذاعة خاص :
للاذاعة في الخاص اكتب Dex + رسالتك (كليشتك) مثال
Dex اهلاً وسهلاً

لاضهار ايديك اكتب id 

لفحص يوزر ما اذا كان مرفوع مزاد او لا او مرفوع ومباع اكتب User + يوزرك ، مثال
User @LuLuu
اذا واجهت مشاكل راسلني 
Owner : @LuLuu ,  Channel : @iiiNil''')

DEX.run_until_disconnected()
