import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id


def write_message(sender, message):
    authorize.method('messages.send', {'user_id': sender, 'message': message,
                                       'random_id': get_random_id()})


token = '--TOKEN--'
authorize = vk_api.VkApi(token=token)

# VkLongPoll -- передает серверу вк что мы хотим использовать именно этот тип апи
longpoll = VkLongPoll(authorize)
score = 0
question_number = 0
for event in longpoll.listen():
    # event.text -- содержит ли новое смс текст
    # event.to_me -- отправить мне
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        reseived_message = event.text  # Полученное сообщение
        sender = event.user_id
        if question_number == 0:
            write_message(sender, "Привет! Хочешь сыграть в викторину? Отвечай 'Да' или 'Нет'")
            # !
            question_number += 1

        elif question_number == 1:
            if reseived_message.lower() == "да":
                write_message(sender, "Вопрос 1: Какого цвета небо?")
                question_number += 1
            else:
                write_message(sender, "Жаль. До встречи!")
                question_number = 0

        elif question_number == 2:
            if reseived_message.lower() == "синий":
                write_message(sender, "Правильно! +1 очко")
                score += 1
            else:
                write_message(sender, "Неправильно. Правильный ответ - синий")
                question_number += 1

        elif question_number == 3:
            write_message(sender, "Вопрос 2: Сколько ног у человека?")
            question_number += 1
        elif question_number == 4:
            if reseived_message == "2":
                write_message(sender, "Правильно! +1 очко")
                score += 1
            else:
                write_message(sender, "Неправильно. Правильный ответ - 2")
            question_number += 1
        elif question_number == 5:
            write_message(sender, "Вопрос 3: Какая самая большая планета в Солнечной системе?")
            question_number += 1
        elif question_number == 6:
            if reseived_message.lower() == "юпитер":
                write_message(sender, "Правильно! +1 очко")
                score += 1
            else:
                write_message(sender, "Неправильно. Правильный ответ - Юпитер")
            question_number += 1
        elif question_number == 7:
            write_message(sender, "Вопрос 4: Какая самая маленькая страна в мире?")
            question_number += 1
        elif question_number == 8:
            if reseived_message.lower() == "ватикана":
                write_message(sender, "Правильно! +1 очко")
                score += 1
            else:
                write_message(sender, "Неправильно. Правильный ответ - Ватикан")
            question_number += 1
        elif question_number == 9:
            write_message(sender, "Вопрос 5: Сколько дней в году?")
            question_number += 1
        elif question_number == 10:
            if reseived_message == "365":
                write_message(sender, "Правильно! +1 очко")
                score += 1
            else:
                write_message(sender, "Неправильно. Правильный ответ - 365")
            question_number += 1
            write_message(sender, f"Викторина окончена! Вы набрали {score} очков!")
            question_number = 0
        elif reseived_message == "Счёт":
            write_message(sender, f"Ваш текущий счёт: {score} очков")
        else:
            write_message(sender, "Я вас не понимаю...")

