from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8641834002:AAH21eeFetbZZhVPcP-r8_GwfBEyfST6VsY"
CANAL = "https://t.me/HERO38iserelivraison"
TELEGRAM_CMD = "https://t.me/coffeeisere"
WHATSAPP = "https://chat.whatsapp.com/IG88nsy502C1va1Svg0Zvi?mode=gi_t"

PHOTOS = [
    "https://i.ibb.co/9m7GSy4X/IMG-2887.jpg",
]

MENU_TEXT = (
    "『 🌑 *C O F F E E  I S È R E* 🌑 』\n"
    "━━━━━━━━━━━━━━━━━━━\n"
    "💙 *Qualité Premium • Livraison Rapide*\n"
    "━━━━━━━━━━━━━━━━━━━\n\n"
    "Bienvenue dans notre univers 🖤\n"
    "Que puis-je faire pour toi ? ⬇️"
)

TARIFS_TEXT = (
    "『 💙 *N O S  T A R I F S* 💙 』\n"
    "━━━━━━━━━━━━━━━━━━━\n\n"
    "🔹 *1g*   ┄┄┄┄┄  *30€*\n"
    "🔹 *5g*   ┄┄┄┄┄  *135€*\n"
    "🔹 *10g* ┄┄┄┄┄  *260€*\n"
    "🔹 *50g* ┄┄┄┄┄  *1 250€*\n\n"
    "━━━━━━━━━━━━━━━━━━━\n"
    "🍬 *Petit bonbon offert avec chaque commande*\n"
    "━━━━━━━━━━━━━━━━━━━\n\n"
    "👇 *Prêt à commander ?*"
)

def menu_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📸 Nos Produits", callback_data="produits")],
        [InlineKeyboardButton("💰 Nos Tarifs & Infos", callback_data="infos")],
        [InlineKeyboardButton("📲 Commander via Telegram", url=TELEGRAM_CMD)],
        [InlineKeyboardButton("💬 Commander via WhatsApp", url=WHATSAPP)],
        [InlineKeyboardButton("🌑 Rejoindre le Canal", url=CANAL)],
    ])

def tarifs_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📲 Commander via Telegram", url=TELEGRAM_CMD)],
        [InlineKeyboardButton("💬 Commander via WhatsApp", url=WHATSAPP)],
        [InlineKeyboardButton("🔙 Retour au Menu", callback_data="retour")],
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

    if query.data == "infos":
        await query.edit_message_caption(
            caption=TARIFS_TEXT,
            reply_markup=tarifs_keyboard(),
            parse_mode="Markdown"
        )

    elif query.data == "produits":
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
