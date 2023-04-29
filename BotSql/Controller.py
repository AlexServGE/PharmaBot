import logging

from telegram.ext import (
    Updater,
)

from Bot_fd.ConversationDailyProcurements import ConversationDailyProcurements


class Controller:

    def __init__(self, token):
        self.updater = Updater(token)
        self.dispatcher = self.updater.dispatcher
        self.logger = self.start_logging()
        self.conversation_daily_procurements = ConversationDailyProcurements(self.updater,self.dispatcher,self.logger)
        self.start_bot()


    def start_logging(self):
        # Ведение логов
        logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
        )
        return logging.getLogger(__name__)

    def start_bot(self):
        # Запуск бота
        self.conversation_daily_procurements.pharmbot_ver001_test_session()
        self.updater.start_polling()
        self.updater.idle()
