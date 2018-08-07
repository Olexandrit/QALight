import telepot

chat_id = 605857925
TOKEN  = '635583256:AAEmQXtTb7pI7q39Z6OXNXCfsymnNfNGWaA'

bot = telepot.Bot(TOKEN)
bot.sendMessage(chat_id, 'Hello')