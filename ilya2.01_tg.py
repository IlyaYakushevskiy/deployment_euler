import telebot, openai

bot = telebot.TeleBot('5263610136:AAH-uuoIVWVK2fIrQx3ajxK_-v299C_Z48Q')

@bot.message_handler(func=lambda message: True)
def get_codex(message):
    response = openai.Completion.create(
        api_key= "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",
        model="curie:ft-personal-2022-07-05-16-18-35",
        prompt='"""\n{}\n"""'.format(message.text),
        temperature=0.3,
        max_tokens=50,
        #top_p=1,
        #frequency_penalty=0,
        #presence_penalty=0,
        #stop=['"""'])

    bot.send_message(message.chat.id,
    f'```python\n{response}\n```',
                     #f'```python\n{response["choices"][0]["text"]}\n```',
    parse_mode="Markdown")
# Запускаем бота
bot.polling(non_stop=True, interval=0)

