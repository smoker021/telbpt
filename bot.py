from telegram.ext import Application, CommandHandler, MessageHandler, filters
from groq import Groq

# توکن‌ها (اگه جدید گرفتی، جایگزین کن)
TELEGRAM_TOKEN = "7835233611:AAHyk-wxC2y57nBJlHJT--E3Y5oOys_zITA"
GROQ_API_KEY = "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"

# تنظیم Groq
client = Groq(api_key=GROQ_API_KEY)

# تابع برای گرفتن جواب از Groq
async def get_groq_response(message):
    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": message}],
            model="llama-3.3-70b-versatile",
            max_tokens=150
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"خطا: {str(e)}"

# تابع برای مدیریت پیام‌های کاربران
async def handle_message(update, context):
    user_message = update.message.text
    groq_reply = await get_groq_response(user_message)
    await update.message.reply_text(groq_reply)

# تابع دستور شروع
async def start(update, context):
    await update.message.reply_text("سلام! من ربات هوش مصنوعی‌ام. هر سوالی داری بپرس!")

# راه‌اندازی ربات
def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()

if __name__ == "__main__":
    main()
