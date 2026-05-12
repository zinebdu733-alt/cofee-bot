from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup

from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "REMETS_TON_TOKEN_ICI"

CANAL = "REMETS_TON_LIEN_CANAL_ICI"

TELEGRAM_CMD = "REMETS_TON_LIEN_TELEGRAM_ICI"

WHATSAPP_NUM = "REMETS_TON_LIEN_WHATSAPP_ICI"

WHATSAPP_GROUP = "REMETS_TON_LIEN_GROUPE_ICI"

PHOTOS = [

    "REMETS_TON_LIEN_IMAGE_ICI"

]

WELCOME_TEXT = (

    "*COFEE ISERE*\n"

    "━━━━━━━━━━━━━━━━━━\n"

    "Qualite Premium • Livraison Rapide\n"

    "Service discret • Disponible 7j/7\n\n"

    "Bienvenue dans notre univers.\n"

    "Que puis-je faire pour toi ?"

)

TARIFS_TEXT = (

    "*TARIFS PREMIUM*\n"

    "━━━━━━━━━━━━━━━━━━\n\n"

    "*1g*  ┄┄┄┄┄  *30€*\n"

    "*5g*  ┄┄┄┄┄  *135€*\n"

    "*10g* ┄┄┄┄┄  *260€*\n"

    "*50g* ┄┄┄┄┄  *1 250€*\n\n"

    "━━━━━━━━━━━━━━━━━━\n"

    "Petit cadeau offert avec chaque commande\n"

    "━━━━━━━━━━━━━━━━━━\n\n"

    "*Pret a commander ?*"

)

PRODUITS_TEXT = (

    "*CATALOGUE PRIVE*\n"

    "━━━━━━━━━━━━━━━━━━\n\n"

    "Voici nos produits disponibles.\n\n"

    "Qualite premium\n"

    "Livraison rapide\n"

    "Service discret"

)

def menu_keyboard():

    return InlineKeyboardMarkup([

        [InlineKeyboardButton("Catalogue Prive", callback_data="produits")],

        [InlineKeyboardButton("Tarifs Premium", callback_data="infos")],

        [InlineKeyboardButton("Commander via Telegram", url=TELEGRAM_CMD)],

        [InlineKeyboardButton("Support WhatsApp", url=WHATSAPP_NUM)],

        [InlineKeyboardButton("Groupe WhatsApp", url=WHATSAPP_GROUP)],

        [InlineKeyboardButton("Canal Officiel", url=CANAL)],

    ])

def retour_keyboard():

    return InlineKeyboardMarkup([

        [InlineKeyboardButton("Commander", url=TELEGRAM_CMD)],

        [InlineKeyboardButton("Support WhatsApp", url=WHATSAPP_NUM)],

        [InlineKeyboardButton("Retour au Menu", callback_data="retour")],

    ])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_photo(

        photo=PHOTOS[0],

        caption=WELCOME_TEXT,

        reply_markup=menu_keyboard(),

        parse_mode="Markdown"

    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    if query.data == "infos":

        await query.edit_message_caption(

            caption=TARIFS_TEXT,

            reply_markup=retour_keyboard(),

            parse_mode="Markdown"

        )

    elif query.data == "produits":

        await query.edit_message_caption(

            caption=PRODUITS_TEXT,

            reply_markup=retour_keyboard(),

            parse_mode="Markdown"

        )

    elif query.data == "retour":

        await query.edit_message_caption(

            caption=WELCOME_TEXT,

            reply_markup=menu_keyboard(),

            parse_mode="Markdown"

        )

def main():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(CallbackQueryHandler(button))

    print("Bot lance avec succes")

    app.run_polling()

if __name__ == "__main__":

    main()
