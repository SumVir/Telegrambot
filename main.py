from typing import Final
from telegram import Update,InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler
from config import TELEGRAM_TOKEN, BOT_USERNAME, OWNER_ID, SQLALCHEMY_DATABASE_URI


# Commands

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Text to be displayed above the list of commands
    intro_text = f"Xoş gördük, Mən kibertəhlükəsizlik üzrə tövsiyə vermək məqsədilə yaradılmış bir Botam."
    
    
    # Options to be displayed as buttons
    options = [['Şifrə haqqında'], ['Link haqqında'], ['Əlaqə saxla']]

    # Create a list of InlineKeyboardButton objects
    keyboard = [[InlineKeyboardButton(text, callback_data=text) for text in row] for row in options]

    # Create an InlineKeyboardMarkup with the list of InlineKeyboardButton objects
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Combine the intro text and options
    full_text = f"{intro_text}\n\n"
    full_text += "Zəhmət olmasza, Mövzu seçin:"

    await update.message.reply_text(full_text, reply_markup=reply_markup)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('/start-a basın\n\nİrad və ya Təklifin var?\nYaradıcıya yaz --> https://t.me/elsenoraccount')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Bu əmr gələcəkdə yenilənəcəkdir')



# Responses

def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'salam' in processed or 'hello'in processed or 'salam aleykum'in processed or 'hey'in processed or 'hi'in processed:
        return 'Salamlar, Xoş gördük. Bugün necəsiz? '
    
    if 'sən?' in processed or 'sen?' in processed or 'sən' in processed or 'sen' in processed:
        return 'Mən yaxşıyam :)'

    if 'necəsən' in processed or 'nətərsən' in processed or 'netersen' in processed or 'nəvar nəyox' in processed:
        return 'Yaxşı, Sən?'
    
    if 'məndə yaxşı' in processed or 'yaxşı' in processed or 'orta' in processed or 'super' in processed or 'ela' in processed:
        return 'Əla, həmişə yaxşı ol'
    
    if 'pis' in processed or 'pisəm'  in processed or 'belədə' in processed or 'belede'in processed or 'yaxşı deyiləm' in processed:
        return 'Heç nə olmaz, bir gün hərşey yaxşı olacağ. Bu həyatda çətinlik yaşayan tək sən deyilsən, unutma.'

    if 'şifrə' in processed:
        return 'Güclü şifrə rəqəmsal hesablarınızı və şəxsi məlumatlarınızı qorumaq üçün vacibdir. Bu mürəkkəb və təsadüfi ardıcıllıq təşkil edən hərflərin (həm böyük, həm də kiçik hərf), rəqəmlərin və simvolların birləşməsidir. Şifrənin gücü onun müxtəlif hücum formalarına, məsələn, brute-force cəhdlərinə qarşı durmaq qabiliyyətindədir. Şifrə 8-16 simvol uzunluğunda olmalıdır. Zəif şifrə nümunə: "Elçin1985" . Güclü şifrə nümunə: "Tr@in$&72Blu3"' 
    
    if 'link'  in processed or 'linklər' in processed:
        return 'Onlayn həyatda naviqasiya çoxsaylı linklərlə qarşılaşmağı əhatə edir. Bəziləri dəyərli məlumatlara aparsada bizi, digərləri də fişinq cəhdləri kimi risklər yarada bilər. 1. HTTPS-i yoxlayın. Qanuni veb saytlar təhlükəsiz ünsiyyət üçün HTTPS-dən istifadə edir. Linkin "http://" əvəzinə "https://" ilə başladığından əmin olun. 2. Üzərinə gətirin, Klik etməyin. Təyinat yerinə baxmaq üçün klikləmədən siçanınızı linkin üzərinə gətirin. URL-in gözlənilən mənbə ilə uyğunlaşdığını yoxlayın. 3. Qısaldılmış URL-lərdən çəkinin. Qısaldılmış URL-lər həqiqi təyinatı gizlədə bilər. Klikləmədən əvvəl tam linki aşkar etmək üçün URL genişləndirmə xidmətlərindən istifadə edin.                                                      '
    
    if 'mövzu'  in processed or 'mövzular' in processed or 'start' in processed:
        return 'Mövzular üçün /start '

    return 'Sizi başa düşmədim, Söz lüğətim kiçikdir. Zəhmət olmazsa /start basın. Və ya /help .'

async def handle_button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Handle button click events
    query = update.callback_query
    clicked_button = query.data

    if clicked_button == 'Şifrə haqqında':
        await query.message.reply_text('Güclü şifrə rəqəmsal hesablarınızı və şəxsi məlumatlarınızı qorumaq üçün vacibdir. Bu mürəkkəb və təsadüfi ardıcıllıq təşkil edən hərflərin (həm böyük, həm də kiçik hərf), rəqəmlərin və simvolların birləşməsidir. Şifrənin gücü onun müxtəlif hücum formalarına, məsələn, brute-force cəhdlərinə qarşı durmaq qabiliyyətindədir. Şifrə 8-16 simvol uzunluğunda olmalıdır. Zəif şifrə nümunə: "Elçin1985" . Güclü şifrə nümunə: "Tr@in$&72Blu3"')
    elif clicked_button == 'Link haqqında':
        await query.message.reply_text('Onlayn həyatda naviqasiya çoxsaylı linklərlə qarşılaşmağı əhatə edir. Bəziləri dəyərli məlumatlara aparsada bizi, digərləri də fişinq cəhdləri kimi risklər yarada bilər. 1. HTTPS-i yoxlayın. Qanuni veb saytlar təhlükəsiz ünsiyyət üçün HTTPS-dən istifadə edir. Linkin "http://" əvəzinə "https://" ilə başladığından əmin olun. 2. Üzərinə gətirin, Klik etməyin. Təyinat yerinə baxmaq üçün klikləmədən siçanınızı linkin üzərinə gətirin. URL-in gözlənilən mənbə ilə uyğunlaşdığını yoxlayın. 3. Qısaldılmış URL-lərdən çəkinin. Qısaldılmış URL-lər həqiqi təyinatı gizlədə bilər. Klikləmədən əvvəl tam linki aşkar etmək üçün URL genişləndirmə xidmətlərindən istifadə edin. ')
    elif clicked_button == 'Əlaqə saxla':    
        await query.message.reply_text(' https://t.me/elsenoraccount')   



async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}" ')

    if message_type == 'group':
        if BOT_USERNAME in text: 
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else: 
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

     
   
if __name__ == '__main__':
    print('Starting bot... ')
    app = Application.builder().token(TELEGRAM_TOKEN).build()


    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    
  
    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    # Buttons
    app.add_handler(CallbackQueryHandler(handle_button_click))
    
    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)







