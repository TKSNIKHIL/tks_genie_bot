from typing import Final
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '8117919143:AAEoinEVHHCqbCvwPBDzgkeE7L4omMv7BcI'
BOT_USERNAME: Final = '@TKSGPT_BOT'

# --- Commands ---

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [['View Catalog', 'Connect with sales team'],
                ['View Size Guide', 'View Instagram'],
                ['Give Feedback']]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    await update.message.reply_text(
        "Hey there! 👋 I’m the TKS Genie from THE KLASSIC STORE — here to help you browse, shop, and style your way through our fab collection. Let’s get started!",
        reply_markup=reply_markup
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am a TKS GENIE! Please type something so I can respond.')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command!')

# --- Main Message Handler ---

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    chat_id = update.message.chat.id

       # Greeting detection
    greetings = ['hi', 'hey', 'hello']
    if any(greet in text for greet in greetings):
        await update.message.reply_text("Hey there! 👋 Type /start to continue.")
        return

    if text == 'view catalog':
        keyboard = [['Fabric Type', 'Products']]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text('📚 What would you like to explore?', reply_markup=reply_markup)
        return

    if text == 'fabric type':
        keyboard = [['DYED Fabrics'], ['Mill Print Fabrics'], ['Value Added Fabrics'], ['⬅ Back']]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text('🧵 Choose a fabric category:', reply_markup=reply_markup)
        return

    if text == 'dyed fabrics':
        keyboard = [['ROTO', 'Velvet'], ['Lycra', 'Taiwan'], ['⬅ Back to Fabric Type']]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text('🎨 Choose a dyed fabric:', reply_markup=reply_markup)
        return

    if text == 'mill print fabrics':
        keyboard = [['ROTO Prints', 'Taiwan Prints'], ['⬅ Back to Fabric Type']]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text('🖼️ Choose a mill print fabric:', reply_markup=reply_markup)
        return

    if text == 'value added fabrics':
        keyboard = [['Sequence & Shimmer', 'Foil Work'], ['⬅ Back to Fabric Type']]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text('✨ Choose a value added fabric:', reply_markup=reply_markup)
        return

    if text == '⬅ back to fabric type':
        keyboard = [['DYED Fabrics'], ['Mill Print Fabrics'], ['Value Added Fabrics'], ['⬅ Back']]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text('🧵 Back to fabric categories:', reply_markup=reply_markup)
        return

    if text == 'products':
        keyboard = [['Table Cover', 'Cushion Cover'], ['Chair Cover', 'Fabric Ceilings'], ['⬅ Back']]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text('🛒 Choose a product category:', reply_markup=reply_markup)
        return

    if text == '⬅ back':
        keyboard = [['View Catalog', 'Connect with sales team'],
                    ['View Size Guide', 'View Instagram'],
                    ['Give Feedback']]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text('🔙 Back to main menu:', reply_markup=reply_markup)
        return

    # --- Specific Fabric Replies ---



    if text == 'roto':
        message = """\
🧵 ROTTO DYED – Width: 40 inches
A vibrant, polyester-based fabric perfect for colorful mandap draping — ideal for both indoor and outdoor events.

🎨 Explore the full shade range — we have 30+ stunning colors ready in stock!
💬 Need pricing? Click below to connect with a sales executive instantly.
👉 https://wa.me/919730300218"""
        await update.message.reply_text(message)
        await update.message.reply_document(document=open(r"e:\The Klassic Store py\shadecards\MICRO SHADE CARD.pdf", "rb"))
        await update.message.reply_document(document=open(r"e:\The Klassic Store py\shadecards\ROTTO DYED SHADES (2).pdf", "rb"))
        return




    if text == 'Velvet':
        message = """\
🪡 DYED STRETCH VELVET

Width: 5 ft

A rich, elegant fabric perfect for table covers, ceiling draping, and decor accents — adds depth and luxury to any setup.

✨ Available in two quality options: 5.5 MTR and 3.5 MTR.

🎨 View our shade card to explore the full range of colors in stock.

🧵 Soft. Stretchy. Stunning. Ideal for premium event styling.

💬 Need pricing or details? Tap below to connect with our sales team instantly

👉 https://wa.me/919730300218"""
        await update.message.reply_text(message)
        await update.message.reply_document(document=open(r"e:\The Klassic Store py\shadecards\VELVET SHADE CARD.pdf", "rb"))
        return



    if text == 'lycra':
        message = """\
🌟 BRIGHT LYCRA – 

Width: 54 inches

As the name suggests, it’s a bright, soft, and shiny fabric — perfect for chair tie-backs, ceiling draping, and event décor.

✨ Fabric quality: 28 GEJ — smooth, flexible, and vibrant.

🎨 Explore our shade card to view all available colors and find your perfect match.

💬 Want prices or more info? Click below to chat with our sales team instantly!

👉 https://wa.me/919730300218"""
        await update.message.reply_text(message)
        await update.message.reply_document(document=open(r"e:\The Klassic Store py\shadecards\LYCRA SHADE CARD.pdf", "rb"))
        return



    if text == 'Taiwan':
        message = """\
TAIWAN FABRIC

Width: 5 ft

A sturdy, durable fabric ideal for side masking, stage masking, and ceiling coverage — designed to deliver structure and support for event setups.

✨ Fabric quality: 14 KG — strong, reliable, and event-ready.

💬 Need pricing or more details? Tap below to connect with our sales team instantly!

👉 https://wa.me/919730300218"""
        await update.message.reply_text(message)
        return

    if text == 'roto prints':
        message = """\
ROTTO PRINTS – 

Width: 40 inches

Bold. Stylish. Unmissable.

Our premium polyester-based printed fabric is perfect for eye-catching mandaps, vibrant backdrops, table overlays, and event decor that leaves a lasting impression — indoors or outdoors.

🎨 ready-to-ship designs available in stock — from traditional to trendy!

📦 Bulk orders? No waiting – Just wow.

💬 Tap to connect with our sales expert now:

👉 https://wa.me/919730300218

🧵 Crafted by The Klassic Store – Where creativity meets celebration."""
        await update.message.reply_text(message)
        await update.message.reply_document(document=open(r"e:\The Klassic Store py\shadecards\ROTTO PRINTS (3).pdf", "rb"))
        await update.message.reply_document(document=open(r"e:\The Klassic Store py\shadecards\ROTTO PRINTS-2 (1).pdf", "rb"))


        return

    if text == 'taiwan prints':
        await update.message.reply_text('🖼️ Taiwan Prints — floral & abstract styles in stock.')
        return

    if text == 'sequence & shimmer':
        await update.message.reply_text('✨ Sequence & shimmer fabrics available in gold, silver, and more shades. DM for price.')
        return

    if text == 'foil work':
        await update.message.reply_text('✨ Foil work fabrics — starting from ₹60/meter. View catalog or ask for video.')
        return

    if text == 'table cover':
        await update.message.reply_text('🪑 Table Covers available in velvet and lycra. DM us for designs.')
        return

    if text == 'connect with sales team':
        await update.message.reply_text(
            '''📞 💬 Connect with our sales team on WhatsApp:
👉 https://wa.me/919730300218
👉 https://wa.me/919730300217''')
        return

    if text == 'view size guide':
        await update.message.reply_text('📏 View the size guide here: https://yourwebsite.com/size-guide')
        return

    if text == 'view instagram':
        await update.message.reply_text('📸 Follow us on Instagram: https://instagram.com/theklassicstore')
        return

    if text == 'give feedback':
        await update.message.reply_text('''💬 We'd Love to Hear From You!
Have any feedback, suggestions, or just want to share your experience?
We're all ears! 👂
Simply drop us a message on WhatsApp 👉 wa.me/918379996555
Our team is here and happy to connect with you!

''')
        return

    # Fallback
    await update.message.reply_text('❓ I didn’t understand that. Please select a button or type a valid command.')

# --- Error Handler ---

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

# --- Main Bot Setup ---

if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    # Command Handlers
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # Message Handler
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Error Handler
    app.add_error_handler(error)

    # Polling
    print('Polling...')
    app.run_polling(poll_interval=3)
