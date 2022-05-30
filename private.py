from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
# Mamaklı tarafından düzenlendi. 

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                "https://ibb.co/FKWzS3F",
                caption=(f"""**selamün aleyküm {message.from_user.mention} 🎵\nBen @Mamaklimbot!\nMüzik dinle diye varım . Ban yetkisiz, Ses yönetimi yetkisi verip, Asistanı gruba ekle ama kızlara yürür bilgin olsun.\n\nDüzen Tasarım [@Sendenolmazbiyol](https://t.me/Sendenolmazbiryol).**"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ Grubuna gidelim bebeğim ❱ ➕", url=f"https://t.me/Mamaklimbot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔊 Sese gelen asistan", url="https://t.me/sendenolmazbiryol"
                    ),
                    InlineKeyboardButton(
                        "💬 Kaynatmak için", url="https://t.me/Sendenolmazbiyol"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🧩 Nasıl çalacağın" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "Resmi Kanal 🇹🇷", url=f"https://t.me/Mamaklininchannnel"
                    )
                ]
                
           ]
        ),
    )
  


@Client.on_message(command(["bilgi", f"bilgi@Sendenolmazbiyol"]))
async def bilgi(_, message: Message):
      await message.reply_text(" ❗ Not:\n Botun aktif çalışması için şu üç yetkiye ihtiyaç vardır:\n- Mesaj silme yetkisi,\n- Bağlantı ile davet etme yetkisi,\n- Sesli sohbeti yönetme yetkisi.", 
      reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🔴 Herkes için komutlar", callback_data="herkes")
                 ],[                     
                     InlineKeyboardButton(
                         "⚫ Amdinler için komutlar", callback_data="admin")
                 ],[
                     InlineKeyboardButton(
                         "Ana menü🏠", callback_data="cbstart")
                 ],[
                     InlineKeyboardButton(
                         "⚙ Geliştirici", url="https://t.me/SendenOlmazBiyol")
                 ]
             ]
         )
    )


@Client.on_callback_query(filters.regex("cbbilgi"))
async def cbbilgi(_, query: CallbackQuery):
    await query.edit_message_text(" ❗ Not:\nBotun aktif çalışması için şu üç yetkiye ihtiyaç vardır:\n- Mesaj silme yetkisi,\n- Bağlantı ile davet etme yetkisi,\n- Sesli sohbeti yönetme yetkisi.", 
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton(
            "✨Herkes için Komutlar", callback_data ="herkes")
        ],
        [
          InlineKeyboardButton(
            "👑Yönetici Komutları",callback_data ="admin")
        ],
        [
          InlineKeyboardButton(
            "🏠Ana Menü", callback_data="cbstart")
        ],
        [
          InlineKeyboardButton(
            "⚙ Geliştirici", url="https://t.me/SendenolmazBiYol")
        ]
      ]
     ))


@Client.on_callback_query(filters.regex("herkes"))
async def herkes(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Selam {query.from_user.mention}!\nBu botun herkes için komut menüsü 😉\n\n ▶️ /oynat - şarkı çalmak için youtube url'sine veya şarkı dosyasına yanıt verme\n ▶️ /oynat <song name> - istediğiniz şarkıyı çal\n 🔴 \n 🎵 /bul <song name> - istediğiniz şarkıları hızlı bir şekilde bulun\n 🎵 /vbul istediğiniz videoları hızlı bir şekilde bulun\n 🔍 /ara <query> - youtube'da ayrıntıları içeren videoları arama\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "⚙ Geliştirici", url="https://t.me/SendenOlmazBiYol")
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ Geri ⬅️", callback_data="cbbilgi")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("admin"))
async def admin(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Selam {query.from_user.mention}!\nBu botun adminler için komut menüsü 🤩\n\n ▶️ /devam - şarkı çalmaya devam et\n ⏸️ /durdur - çalan parçayı duraklatmak için\n 🔄 /atla- Sıraya alınmış müzik parçasını atlatır.\n ⏹ /son - müzik çalmayı durdurma\n 🔼 /ver botun sadece yönetici için kullanılabilir olan komutlarını kullanabilmesi için kullanıcıya yetki ver\n 🔽 /al botun yönetici komutlarını kullanabilen kullanıcının yetkisini al\n\n ⚪ /asistan - Müzik asistanı grubunuza katılır.\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "⚙ Geliştirici", url="https://t.me/Sendenolmazbiyol")
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ Geri ⬅️", callback_data="cbbilgi")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(f"""**selamün aleyküm {query.from_user.mention} 🎵\nBen @Mamaklimbot!\nSana müzik çalacam. Ban yetkisiz, Ses yönetimi yetkisi verip, Asistanı gruba ekleyiniz.\n\nDüzen Tasarım [Mamaklı 🎙️](https://t.me/Sendenolmazbiyol).**""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ Grubuna gidelim bebeğim ❱ ➕", url=f"https://t.me/Sendenolmazbiyol?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔊 Sese gelen Asistan", url="https://t.me/Sendenolmazbiryol"
                    ),
                    InlineKeyboardButton(
                        "💬 Kaynatmak için", url="https://t.me/Sendenolmazbiyol"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🌀 Nasıl çalışırım" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "Resmi Kanal 🇹🇷", url=f"https://t.me/mamaklininchannnel"
                    )
                ]
                
           ]
        ),
    )
