@@ -20,36 +20,15 @@
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
        [InlineKeyboardButton("📞 Nous contacter WhatsApp", url=WHATSAPP_NUM)],
        [InlineKeyboardButton("👥 Groupe WhatsApp", url=WHATSAPP_GROUP)],
        [InlineKeyboardButton("🌑 Rejoindre le Canal", url=CANAL)],
    ])

def tarifs_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📲 Commander via Telegram", url=TELEGRAM_CMD)],
        [InlineKeyboardButton("📞 Nous contacter WhatsApp", url=WHATSAPP_NUM)],
        [InlineKeyboardButton("🔙 Retour au Menu", callback_data="retour")],
    ])

def retour_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Retour au Menu", callback_data="retour")],
@@ -67,14 +46,7 @@ async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "infos":
        await query.edit_message_caption(
            caption=TARIFS_TEXT,
            reply_markup=tarifs_keyboard(),
            parse_mode="Markdown"
        )

    elif query.data == "produits":
    if query.data == "produits":
        await query.edit_message_caption(
            caption="📸 *Nos Produits* 🖤\n\nVoici nos produits disponibles :",
            reply_markup=retour_keyboard(),
