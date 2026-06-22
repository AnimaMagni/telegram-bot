from bot.application import create_app
from utils.logger import setup_logger
from database.models import create_tables

logger = setup_logger()

logger.info("Bot is starting...")

def main():

    create_tables()

    app = create_app()

    print("Bot is running...")

    app.run_polling()



if __name__ == "__main__":
    main()

    