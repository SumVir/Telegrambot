from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from config import TELEGRAM_TOKEN, BOT_USERNAME, OWNER_ID, SQLALCHEMY_DATABASE_URI


# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Salam, Mən kibertəhlükəsizlik üzrə sənə məsləhətlər vermək üçün burdayam. :)  Əmrlər listi: "şifrə", "link"')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Mən bir botam, Danışmaq üçün nə isə yazın zəhmət olmasa.')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Bu bir Custom əmrdir')



# Responses

def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'salam' in processed or 'hello'in processed or 'salam aleykum'in processed or 'hey'in processed:
        return 'Salamlar, Xoş gördük'
    
    if 'necəsən''hello' in processed or 'nətərsən' in processed or 'netersen' in processed or 'nəvar nəyox' in processed:
        return 'Yaxşı, Sən?'
    
    if 'məndə yaxşı' in processed or 'yaxşı' in processed or 'orta' in processed or 'super' in processed or 'ela' in processed:
        return 'Əla, həmişə yaxşı ol'
    
    if 'pis' in processed or 'pisəm'  in processed or 'belədə' in processed or 'belede'in processed or 'yaxşı deyiləm' in processed:
        return 'Heç nə olmaz, bir gün hərşey yaxşı olacağ. Bu həyatda çətinlik yaşayan tək sən deyilsən, unutma.'

    if 'şifrə' in processed:
        return 'Güclü şifrə rəqəmsal hesablarınızı və şəxsi məlumatlarınızı qorumaq üçün vacibdir. Bu mürəkkəb və təsadüfi ardıcıllıq təşkil edən hərflərin (həm böyük, həm də kiçik hərf), rəqəmlərin və simvolların birləşməsidir. Şifrənin gücü onun müxtəlif hücum formalarına, məsələn, brute-force cəhdlərinə qarşı durmaq qabiliyyətindədir. Şifrə 8-16 simvol uzunluğunda olmalıdır. Zəif şifrə nümunə: "Elçin1985" . Güclü şifrə nümunə: "Tr@in$&72Blu3"' 
    
    if 'link'  in processed or 'linklər' in processed:
        return 'Onlayn həyatda naviqasiya çoxsaylı linklərlə qarşılaşmağı əhatə edir. Bəziləri dəyərli məlumatlara aparsada bizi, digərləri də fişinq cəhdləri kimi risklər yarada bilər. 1. HTTPS-i yoxlayın. Qanuni veb saytlar təhlükəsiz ünsiyyət üçün HTTPS-dən istifadə edir. Linkin "http://" əvəzinə "https://" ilə başladığından əmin olun. 2. Üzərinə gətirin, Klik etməyin. Təyinat yerinə baxmaq üçün klikləmədən siçanınızı linkin üzərinə gətirin. URL-in gözlənilən mənbə ilə uyğunlaşdığını yoxlayın. 3. Qısaldılmış URL-lərdən çəkinin. Qısaldılmış URL-lər həqiqi təyinatı gizlədə bilər. Klikləmədən əvvəl tam linki aşkar etmək üçün URL genişləndirmə xidmətlərindən istifadə edin.                                                      '
        
    return 'Nə dediyinizi başa düşmürəm. Zəhmət olmasa, mənim bildiyim sözlərdən yazın VƏ YA düzgün əmri yazdığınızdan əmin olun. Əmrlər listi üçün "/start" yazın.'

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

    # Errors
    
    app.add_error_handler(error)

    # Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)









