from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8641834002:AAH21eeFetbZZhVPcP-r8_GwfBEyfST6VsY"
CANAL = "https://t.me/HERO38iserelivraison"
TELEGRAM_CMD = "https://t.me/coffeeisere"
WHATSAPP_NUM = "https://wa.me/33753400705"
WHATSAPP_GROUP = "https://chat.whatsapp.com/IG88nsy502C1va1Svg0Zvi?mode=gi_t"

PHOTOS = [
    "https://i.ibb.co/9m7GSy4X/IMG-2887.jpg",
]

MENU_TEXT = (
    "『 🌑 *C O F F E E  I S È R E* 🌑 』\n"
    "━━━━━━━━━━━━━━━━━━━\n"
    "💙 *Qualité Premium • Livraison Rapide*\n"
    "━━━━━━━━━━━━━━━━━━━\n\n"
    "Bienvenue dans notre univers 🖤\n"
    "Que puis-je faire pour toi ? ⬇️"
)

def menu_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📸 Nos Produits", callback_data="produits")],
        [InlineKeyboardButton("📲 Commander via Telegram", url=TELEGRAM_CMD)],
        [InlineKeyboardButton("📞 Nous contacter WhatsApp", url=WHATSAPP_NUM)],
        [InlineKeyboardButton("👥 Groupe WhatsApp", url=WHATSAPP_GROUP)],
        [InlineKeyboardButton("🌑 Rejoindre le Canal", url=CANAL)],
    ])

def retour_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Retour au Menu", callback_data="retour")],
    ])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(
        photo="https://i.ibb.co/9m7GSy4X/IMG-2887.jpg",
        caption=MENU_TEXT,
        reply_markup=menu_keyboard(),
        parse_mode="Markdown"
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "produits":
        await query.edit_message_caption(
            caption="📸 *Nos Produits* 🖤\n\nVoici nos produits disponibles :",
            reply_markup=retour_keyboard(),
            parse_mode="Markdown"
        )
        for photo in PHOTOS:
            await query.message.reply_photo(photo=photo)

    elif query.data == "retour":
        await query.edit_message_caption(
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
