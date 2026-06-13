from bot.application import create_app


def main():
    app = create_app()

    print("Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()