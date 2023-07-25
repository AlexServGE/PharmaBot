import logging
from SqlApiSel_fd.SqlApiSel import SqlApiSel

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)


class ConversationDailyProcurements:

    def __init__(self, updater, dispatcher, logger):
        self.updater = updater
        self.dispatcher = dispatcher
        self.logger = logger

    def pharmbot_ver001_test_session(self):

        # Определяем константы этапов разговора
        global CATEGORY, FEDERALREGION
        CATEGORY, FEDERALREGION = range(2)

        # Определяем обработчик разговоров `ConversationHandler`
        # с состояниями CATEGORY и FEDERALREGION
        conv_handler = ConversationHandler(  # здесь строится логика разговора
            # точка входа в разговор
            entry_points=[CommandHandler('start', self.start)],
            # этапы разговора, каждый со своим списком обработчиков сообщений
            states={
                CATEGORY: [MessageHandler(Filters.regex('^(21.20.23.112: Вещества контрастные)$'), self.category)],
                FEDERALREGION: [MessageHandler(Filters.regex('^(Центральный|Северо-Западный|Южный|'
                                                             'Приволжский|Уральский|Сибирский|'
                                                             'Дальневосточный|Северо-Кавказский)$'),
                                               self.federal_region)],
            },
            # точка выхода из разговора
            fallbacks=[CommandHandler('cancel', self.cancel)],
        )

        # Добавляем обработчик разговоров `conv_handler`
        self.dispatcher.add_handler(conv_handler)

    # функция обратного вызова точки входа в разговор
    def start(self, update, context):
        # Список кнопок для ответа
        reply_keyboard = [['21.20.23.112: Вещества контрастные']]
        # Создаем простую клавиатуру для ответа
        markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        # Начинаем разговор с вопроса
        update.message.reply_text(
            'Добрый день! Вас приветствует PharmaBot. '
            'Я здесь, чтобы помочь быть в курсе закупок лекарственных препаратов 44-ФЗ.  '
            'Команда /cancel, чтобы прекратить разговор.\n\n'
            'Выберите категорию лекарственных препаратов, по которой хотел бы получить информацию об актуальных закупках (будут показаны публикации, вышедшие вчера и позавчера):',
            reply_markup=markup_key, )

        global user_filters
        user_filters = list()

        # переходим к этапу `CATEGORY`, это значит, что ответ
        # отправленного сообщения в виде кнопок будет список
        # обработчиков, определенных в виде значения ключа `CATEGORY`
        return CATEGORY

    # Обрабатываем ответ по категории лекарственных препаратов
    def category(self, update, context):
        # определяем пользователя
        user = update.message.from_user
        # Пишем в журнал ответ пользователя
        self.logger.info("Пользователь %s - %s", user.first_name, update.message.text)

        # Список кнопок для ответа
        reply_keyboard = [['Центральный', 'Северо-Западный', 'Южный'],
                          ['Приволжский', 'Уральский', 'Сибирский'],
                          ['Дальневосточный', 'Северо-Кавказский']]
        # Создаем простую клавиатуру для ответа
        markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

        # Наполняем список фильтров, выбранных пользователем для передачи в SqlApiSel
        text = update.message.text
        user_filters.append(text)
        # context.bot.send_message(update.effective_chat.id,
        #                          f'{update.effective_user.first_name} - написал - {text} ')

        # Следующее сообщение с удалением клавиатуры `ReplyKeyboardRemove`
        update.message.reply_text(
            'Выберите федеральный округ, по которому Вы хотели бы получить данные.',
            reply_markup=markup_key,
        )
        # переходим к этапу `FEDERALREGION`
        return FEDERALREGION

    # Обрабатываем ответ по федеральному округу
    def federal_region(self, update, context):
        # определяем пользователя
        user = update.message.from_user
        # Пишем в журнал сведения с федеральным округом
        self.logger.info("Пользователь %s - %s", user.first_name, update.message.text)

        # Отвечаем на сообщение с федеральным округом
        update.message.reply_text(
            'Данные скоро будут отображены'
        )

        # Наполняем список фильтров, выбранных пользователем для передачи в SqlApiSel
        text = update.message.text
        user_filters.append(text)
        # context.bot.send_message(update.effective_chat.id,
        #                          f'{update.effective_user.first_name} - написал - {text} ')

        # Создаем связь с SQL, чтобы получить данные и передать пользователю
        sql_api_sel = SqlApiSel()
        selected_data_list = sql_api_sel.sql_select_daily_procurements(user_filters)
        for procurement in selected_data_list:
            context.bot.send_message(update.effective_chat.id,"\n".join(procurement))



        # переходим к этапу `LOCATION`
        return ConversationHandler.END

    # Обрабатываем команду /skip для фото
    # def skip_photo(self,update, _):
    #     # определяем пользователя
    #     user = update.message.from_user
    #     # Пишем в журнал сведения о фото
    #     logger.info("Пользователь %s не отправил фото.", user.first_name)
    #     # Отвечаем на сообщение с пропущенной фотографией
    #     update.message.reply_text(
    #         'Держу пари, ты выглядишь великолепно! А теперь пришлите мне'
    #         ' свое местоположение, или /skip если параноик.'
    #     )
    #     # переходим к этапу `LOCATION`
    #     return LOCATION

    # Обрабатываем команду /cancel если пользователь отменил разговор
    def cancel(self, update, context):
        # определяем пользователя
        user = update.message.from_user
        # Пишем в журнал о том, что пользователь не разговорчивый
        self.logger.info("Пользователь %s отменил разговор.", user.first_name)
        # Отвечаем на отказ поговорить
        update.message.reply_text(
            'Моё дело предложить - Ваше отказаться'
            'Будет скучно - пишите.',
            reply_markup=ReplyKeyboardRemove()
        )
        # Заканчиваем разговор.
        return ConversationHandler.END


if __name__ == '__main__':
    pass
