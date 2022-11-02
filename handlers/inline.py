from aiogram import types, Dispatcher
import hashlib


async def inline_wiki_handler(query: types.InlineQuery):
    text = query.query or "Python"
    link = f'https://ru.wikipedia.org/wiki/{text}'
    articles = [types.InlineQueryResultArticle(
        id=hashlib.md5(text.encode()).hexdigest(),
        title='WikiPedia',
        url=link,
        input_message_content=types.InputMessageContent(
            message_text=f'Ссылка\n{link}'
        ))]
    await query.answer(articles, cache_time=60)


def register_handler_inline(dp: Dispatcher):
    dp.register_inline_handler(inline_wiki_handler)
