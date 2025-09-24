import os
import logging
from typing import Final

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import spacy


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


TELEGRAM_TOKEN: Final[str | None] = os.getenv("TELEGRAM_TOKEN")
SPACY_MODEL: Final[str] = os.getenv("SPACY_MODEL", "en_core_web_sm")


def build_nlp(model_name: str) -> spacy.language.Language:
    try:
        return spacy.load(model_name)
    except OSError:
        raise RuntimeError(
            f"spaCy model '{model_name}' is not installed.\n"
            f"Install it with: python -m spacy download {model_name}"
        )


nlp = build_nlp(SPACY_MODEL)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Hi! I'm your spaCy-powered assistant. Send me a sentence and I'll extract entities and parts of speech."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "/start - greet\n"
        "/help - this message\n"
        "/model - show current spaCy model"
    )


async def model_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Using spaCy model: {SPACY_MODEL}")


def analyze_text(text: str) -> str:
    doc = nlp(text)

    ents = [f"{ent.text} ({ent.label_})" for ent in doc.ents]
    tokens = [f"{t.text}/{t.pos_}" for t in doc]

    lines: list[str] = []
    if ents:
        lines.append("Entities: " + ", ".join(ents))
    else:
        lines.append("Entities: (none detected)")

    lines.append("Tokens: " + ", ".join(tokens))

    return "\n".join(lines)


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        text = update.message.text or ""
        if not text.strip():
            await update.message.reply_text("Please send some text to analyze.")
            return
        summary = analyze_text(text)
        await update.message.reply_text(summary)
    except Exception as exc:  # graceful fallback
        logger.exception("Error analyzing text")
        await update.message.reply_text(
            "Sorry, I couldn't process that. Try a different sentence or shorter text."
        )


def build_app(token: str) -> Application:
    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("model", model_command))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), echo))
    return application


def main() -> None:
    if not TELEGRAM_TOKEN:
        raise RuntimeError("TELEGRAM_TOKEN environment variable is not set.")
    app = build_app(TELEGRAM_TOKEN)
    logger.info("Bot starting...")
    app.run_polling()


if __name__ == "__main__":
    main()


