from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo, ParseMode
from telegram.ext import CallbackContext

from messages import welcome_message, partnership, comments, lang_msg
from keyboards import main_keyboard, info_keyboard, comments_keyboard, lang_keyboard


def start(update: Update, context: CallbackContext) -> None:
    bot = context.bot

    bot.send_message(
        chat_id=update.message.chat.id,
        text=welcome_message.format(name=update.effective_user.first_name),
        reply_markup=main_keyboard,
    )


def send_cart(update: Update, context: CallbackContext) -> None:
    bot = context.bot

    bot.send_message(
        chat_id=update.message.chat.id,
        text="<b> Sizning savatingiz bo'sh </b>",
        parse_mode=ParseMode.HTML,
    )


def send_partnership(update: Update, context: CallbackContext) -> None:
    bot = context.bot

    bot.send_message(chat_id=update.message.chat.id, text=partnership)


def send_info(update: Update, context: CallbackContext) -> None:
    bot = context.bot

    bot.send_message(
        chat_id=update.message.chat.id,
        text="Kerakli bo'limni tanlang ⬇️",
        reply_markup=info_keyboard,
    )


def send_comments(update: Update, context: CallbackContext) -> None:
    bot = context.bot

    bot.send_message(
        chat_id=update.message.chat.id,
        text=comments,
        reply_markup=comments_keyboard,
        parse_mode=ParseMode.HTML,
    )


def send_languages(update: Update, context: CallbackContext) -> None:
    bot = context.bot

    bot.send_message(
        chat_id=update.message.chat.id,
        text=lang_msg,
        reply_markup=lang_keyboard,
    )


def select_lang(update: Update, context: CallbackContext) -> None:
    bot = context.bot

    if update.callback_query.data.endswith("uz"):
        lang = "uzbek"
    elif update.callback_query.data.endswith("ru"):
        lang = "rus"
    else:
        lang = "nomalum"

    bot.send_message(
        chat_id=update.callback_query.message.chat.id, text=f"{lang} tili talandi"
    )
