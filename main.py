import settings

from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler,
)

from settings import TOKEN
from callbacks import (
    start,
    send_cart,
    send_partnership,
    send_info,
    send_comments,
    send_languages,
    select_lang,
)


def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # command handlers
    dispatcher.add_handler(
        handler=CommandHandler(command=["start", "boshlash"], callback=start)
    )

    # message handler
    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.text("🏠 Bosh menyu"),
            callback=start,
        )
    )
    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.text("📥Savat"),
            callback=send_cart,
        )
    )
    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.text("💼 Hamkorlik"),
            callback=send_partnership,
        )
    )
    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.text("ℹ️ Ma'lumot"),
            callback=send_info,
        )
    )
    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.text("✍️ Izoh qoldirish"),
            callback=send_comments,
        )
    )
    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.text("🌐 Tilni tanlash"),
            callback=send_languages,
        )
    )

    # callbackquery handlers
    dispatcher.add_handler(
        handler=CallbackQueryHandler(callback=select_lang, pattern="lang:")
    )

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
