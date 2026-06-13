from bot.application import create_app
from utils.logger import setup_logger

logger = setup_logger()

logger.info("Bot is starting...")

def main():
    app = create_app()

    print("Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()