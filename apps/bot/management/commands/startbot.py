from aiogram import executor
from django.core.management import BaseCommand

from apps.bot.bot import dp


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        async def on_startup(_):
            print('Бот вышел в онлайн')

        executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
