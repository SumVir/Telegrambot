from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '6690162796:AAH0rOSHMs7JeloydISzkRcjt847kzgRYoM'
BOT_USERNAME: Final='@H4c6erbot'


# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Salam, Mən kibertəhlükəsizlik üzrə sənə məsləhətlər vermək üçün burdayam. :) ')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Mən bir botam, Danışmaq üçün nə isə yazın zəhmət olmasa.')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Bu bir Custom commanddir')



# Responses

def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Salamlar'
    
    if 'necəsən' in processed:
        return 'Yaxşı, Sən?'
    
    if 'məndə yaxşı' in processed:
        return 'Əla'
    
    if 'şifrə' in processed:
        return 'Güclü şifrə rəqəmsal hesablarınızı və şəxsi məlumatlarınızı qorumaq üçün vacibdir. Bu mürəkkəb və təsadüfi ardıcıllıq təşkil edən hərflərin (həm böyük, həm də kiçik hərf), rəqəmlərin və simvolların birləşməsidir. Şifrənin gücü onun müxtəlif hücum formalarına, məsələn, brute-force cəhdlərinə qarşı durmaq qabiliyyətindədir' 
                                                         
    return 'Nə dediyiniz başa düşmürəm.'

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
    app = Application.builder().token(TOKEN).build()


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









