import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Lorem ipsum dolor sit amet. Et numquam rerum et consequatur tempore rem molestiae quas et magni mollitia et galisum omnis sed dolorem culpa. Est eius perferendis ut laudantium dolores qui tempore rerum nam rerum repellendus. Id quod rerum ab quis earum id neque maiores At praesentium modi nam veniam animi. Et debitis rerum non possimus ipsa sed officiis esse ut reprehenderit quos nam aliquid obcaecati et maxime beatae sed autem amet.")

if __name__ == '__main__':
    app = ApplicationBuilder().token("7647849717:AAE9ZvS3m7ToFZM-UGL71WnscKwZGTzWOVo").build()

    app.add_handler(CommandHandler("start", start))

    print("Bot started")
    app.run_polling()
