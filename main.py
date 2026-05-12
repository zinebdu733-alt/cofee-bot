from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import os

TOKEN = os.environ.get("TOKEN")
CANAL = "https://t.me/HERO38iserelivraison"
TELEGRAM_CMD = "https://t.me/coffeeisere"
WHATSAPP_NUM = "https://wa.me/33753400705"
WHATSAPP_GROUP = "https://chat.whatsapp.com/IG88nsy502C1va1Svg0Zvi?mode=gi_t"

PHOTO_URL = "https://i.ibb.co/9m7GSy4X/IMG-2887.jpg"

MENU_TEXT = (
    "COFFEE ISERE\n\n"
    "Livraison rapide - Qualite premium\n\n"
    "Bienvenue dans notre univers\n"
    "Choisis une option ci-dessous"
)

PRODUITS_TEXT = (
    "NOS PRODUITS\n\n"
    "Selection premium - Stock limite\n\n"
    "Pour commander, contacte-nous directement"
)

def menu_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Voir nos Produits", callback_data="produits")],
        [InlineKeyboardButton("Commander sur Telegram", url=TELEGRAM_CMD)],
        [InlineKeyboardButton("WhatsApp Direct", url=WHATSAPP_NUM)],
        [InlineKeyboardButton("Rejoindre le Groupe", url=WHATSAPP_GROUP)],
        [InlineKeyboardButton("Notre Canal Officiel", url=CANAL)],
    ])

def retour_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Retour au Menu", callback_data="retour")],
    ])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_photo(
            photo=PHOTO_URL,
            caption=MENU_TEXT,
            reply_markup=menu_keyboard(),
            parse_mode="Markdown"
        )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "produits":
        try:
            await query.edit_message_caption(
                caption=PRODUITS_TEXT,
                reply_markup=retour_keyboard(),
                parse_mode="Markdown"
            )
        except Exception:
            await query.message.reply_text(
                PRODUITS_TEXT,
                reply_markup=retour_keyboard(),
                parse_mode="Markdown"
            )
        await query.message.reply_photo(photo=PHOTO_URL)

    elif query.data == "retour":
        try:
            await query.edit_message_caption(
                caption=MENU_TEXT,
                reply_markup=menu_keyboard(),
                parse_mode="Markdown"
            )
        except Exception:
            await query.message.reply_photo(
                photo=PHOTO_URL,
                caption=MENU_TEXT,
                reply_markup=menu_keyboard(),
                parse_mode="Markdown"
            )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()

if __name__ == "__main__":
    main()
