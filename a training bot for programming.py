import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder,ReplyKeyboardBuilder # для инлайн кнопок
from aiogram.types import CallbackQuery, InputFile, ReplyKeyboardRemove
from aiogram.types import Message
from aiogram.types.input_file import FSInputFile # для отправки локалььных файлов
from aiogram import Router, F

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="")
# Диспетчер
dp = Dispatcher()
# Инлайн кнопки
builder = InlineKeyboardBuilder()
bs = ReplyKeyboardBuilder()


# Хэндлер на команду /start
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.reply("Добро пожаловать в бота")
    chat_id = message.chat.id
    await message.answer("Если вам нужна помощь, пожалуйста, введите /help")
    buttons = [
        [
        types.KeyboardButton(text="help"),
        types.KeyboardButton(text="Меню"),
        types.KeyboardButton(text="Settings")
        # settings (здесь будет настроки такие выбор языка и покупка премиума)
        ],
    ]
    
    # @dp.message(commands="start")
    # async def cmd_test1(message: types.Message):
    #     await message.reply("Добро пожаловать в бота")
    #     chat_id = message.chat.id #работает и для приватного(лс) чата и для общих чатов (групп)

    keyboard = types.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    await message.answer("Выберите действие", reply_markup=keyboard)


# Помощь 
class Help():
    def __init__(self):
        pass
        
    def com_help(self):
        # Хэндлер на команду /help
        # @dp.message(Command("help"))
        @dp.message(lambda message: message.text == "help")
        async def help(message: types.Message):
            await message.answer('Чем мы можем вам помочь?')
            # help_button = ("1 - Проблемы с ботом, 2 - Проблемы связи")
            # help_answer = input('Введите свою проблему: ')
            help_button = [
                    [
                    types.KeyboardButton(text='Проблемы с ботом'),
                    types.KeyboardButton(text='Проблемы связи'),
                    types.KeyboardButton(text='Другое')
                    ],
                ]
            keyboard = types.ReplyKeyboardMarkup(keyboard=help_button,resize_keyboard=True,input_field_placeholder='Введите описание ошибки')
            await message.answer('Выберите нужную проблему',reply_markup=keyboard)

    def plob_bot(self):
        # @dp.message(Command("Проблемы с ботом"))
        @dp.message(lambda message: message.text == 'Проблемы с ботом')
        async def problemsbot(message: types.Message):
            await message.answer('Мы устраним проблему в ближайшем обновлении')
            help_button = [
                    [
                    types.KeyboardButton(text='Проблемы связи'),
                    types.KeyboardButton(text='Другое')
                    ],
                ]
            keyboard_1 = types.ReplyKeyboardMarkup(keyboard=help_button,resize_keyboard=True,input_field_placeholder='Введите описание ошибки')
            await message.answer('Спасибо за обращение!',reply_markup=keyboard_1)
    
    # @dp.message(lambda message: message.text == 'Проблемы с ботом')   для пользовательских обращений
    def prob_line(self):
        @dp.message(lambda message: message.text == "Проблемы связи")
        async def problemsline(message: types.Message):
            await message.answer('Наши системные администраторы уже трудятся над вашей проблемой!')
            help_button = [
                    [
                    types.KeyboardButton(text='Проблемы с ботом'),
                    types.KeyboardButton(text='Другое')
                    ],
                ]
            keyboard_2 = types.ReplyKeyboardMarkup(keyboard=help_button,resize_keyboard=True,input_field_placeholder='Введите описание ошибки')
            await message.answer('Спасибо за обращение!',reply_markup=keyboard_2)
        
    def oth(self):
        @dp.message(lambda message: message.text == "Другое")
        async def other(message: types.Message):
            await message.answer('Выберите подходящий пункт и нажмите на кнопку')
            help_button = [
                    [
                    types.KeyboardButton(text='Меню'),
                    types.KeyboardButton(text='help')
                    ],
                ]
            keyboard_3 = types.ReplyKeyboardMarkup(keyboard=help_button,resize_keyboard=True)
            await message.answer('Спасибо за обращение!',reply_markup=keyboard_3)
card_help = Help()
card_help.com_help()
card_help.plob_bot()
card_help.prob_line()
card_help.oth()

class Menu():
    def __init__(self):
        pass
    
    def m(self):
        # print(f"{self.one} Вы в главном меню")
        
        #  Меню
        @dp.message(lambda message: message.text == "Меню")
        async def menu(message: types.Message):
            # await message.answer('Вы в главном меню')
            help_button = [
                    [
                    types.KeyboardButton(text='Python'),
                    types.KeyboardButton(text='Системное Администрирование'),
                    types.KeyboardButton(text='C++'),
                    ],
                ]
            keyboard_4 = types.ReplyKeyboardMarkup(keyboard=help_button,resize_keyboard=True)
            await message.answer('Выберите подходящий пункт',reply_markup=keyboard_4)
    
    def py(self): # Python
        # отвечаем на меню
        @dp.message(lambda message: message.text == "Python")
        async def python(message: types.Message):
            # Отправка файла по ссылке
            await bot.send_photo(
                message.chat.id, photo="https://office-guru.ru/wp-content/uploads/2021/08/High_resolution_wallpaper_background_ID_77701763881.jpg",
                caption=f"Python - это высокоуровневый, объектно-ориентированный язык программирования,"
                        "он является гибким языком, который подходит для веб-разработки,"
                        "анализа данных, машинного обучения и многого другого."
                        "\nPython предлагает удобочитаемый код и поддерживает разные парадигмы программирования."
                        "\nОн включает большой стандартный библиотечный запас и может работать на разных платформах.",
                reply_to_message_id = message.message_id
            )
            python_button = [
                    [
                    types.KeyboardButton(text= 'Меню'),
                    types.KeyboardButton(text= 'Python-1'),
                    types.KeyboardButton(text= 'Python-2'),
                    types.KeyboardButton(text= 'Python-3'),
                    ],
                ]
            keyboard_python = types.ReplyKeyboardMarkup(keyboard=python_button,resize_keyboard=True)
            await message.answer('Выберите подходящий пункт',reply_markup=keyboard_python)
            
        @dp.message(lambda message: message.text == 'Python-1')
        async def python_1(message: types.Message):
            py1_button = [
                [
                types.KeyboardButton(text= 'Списки'),
                types.KeyboardButton(text= 'Переменные'),
                types.KeyboardButton(text= 'Множества'),
                types.KeyboardButton(text= 'Циклы'),
                types.KeyboardButton(text= 'f-строки'),
                ],
            ]
            keyboard_python_1 = types.ReplyKeyboardMarkup(keyboard=py1_button,resize_keyboard=True)
            await message.answer('Выберите подходящий пункт',reply_markup=keyboard_python_1)
        # Списки
        @dp.message(lambda message: message.text == 'Списки')
        async def lists(message: types.Message):
            list_buttons = [
                [
                types.KeyboardButton(text = "Меню"),
                types.KeyboardButton(text = "Python-1")
                ],
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard=list_buttons, resize_keyboard=True)
            await message.answer(text='Чтобы вернуться в меню нажмите кнопку меню',reply_markup=keyboard)          
            list_text = ['Списки в Python представляют собой упорядоченные коллекции элементов, которые могут быть разных типов.'
                         'Они являются изменяемыми, что означает возможность добавления, удаления и изменения элементов после создания списка.'
                         'Списки индексируются, начиная с нуля, и поддерживают отрицательные индексы для обращения к элементам с конца списка.'
                         'Создание списка может быть выполнено несколькими способами: Пустой список: my_list = []'
                         'Список с элементами: my_list = ["apple", "banana", "cherry"] Создание списка через генератор: my_list = [x**2 for x in range(6)]'
                         'Доступ к элементам списка осуществляется через индексацию: my_list[0] вернет первый элемент списка.'
                         'Также возможно обращение к элементам с конца списка через отрицательные индексы: my_list[-1] вернет последний элемент.' 
                         'Добавление элементов в список выполняется с помощью метода append: my_list.append("orange").'
                         'Удаление элементов может быть выполнено через del или remove (для удаления по значению).'
                         'Списки поддерживают различные операции, такие как конкатенация (+), умножение (*) для повторения списка,'
                         'срезы для извлечения подсписков, а также методы для работы с элементами списка, например,'
                         'sort для сортировки элементов. Длина списка определяется функцией len.'
                         ]
            list_text_2 = [
                         'Пример использования списков:fruits = ["apple", "banana", "cherry"]'
                         'print(fruits) # Вывод: apple, banana, cherry'
                         '# Добавление элемента'
                         'fruits.append("orange")'
                         'print(fruits) # Вывод: apple, banana, cherry, orange'
                         '# Удаление элемента'
                         'del fruits[1]'
                         'print(fruits) # Вывод: apple, cherry, orange'
                         '# Сортировка списка'
                         'fruits.sort()'
                         'print(fruits) # Вывод: apple, cherry, orange'
                         ]
            await message.answer('\n'.join(list_text))
            await asyncio.sleep(3) # приостанавливаем программу на 3 сек
            await message.answer('\n'.join(list_text_2))
        # Переменные
        @dp.message(lambda message: message.text == 'Переменные')
        async def var(message: types.Message):
            var_buttons = [
                [
                types.KeyboardButton(text = "Меню"),
                types.KeyboardButton(text = "Python-1")
                ],
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard = var_buttons, resize_keyboard=True)
            await message.answer(text='Чтобы вернуться в меню нажмите кнопку меню',reply_markup=keyboard)          
            var_text = [
                        'Переменные в Python играют ключевую роль в хранении и манипулировании данными.'
                        'Они представляют собой ячейки памяти, которым присвоены имена, позволяющие ссылаться на данные.'
                        'В отличие от некоторых других языков программирования, в Python не нужно явно указывать тип переменной при её объявлении;'
                        'Python автоматически определяет тип переменной на основе присвоенного значения.Объявление переменныхДля объявления переменной достаточно присвоить ей значение:'
                        'x = 5 y = "Python" z = 3.14 Здесь x, y, и z являются переменными, которым присвоены значения соответственно 5, "Python" и 3.14.'
                        'Типы переменныхPython поддерживает динамическую типизацию, что означает, что тип переменной может меняться в процессе выполнения программы.'
                        'Основные типы данных включают:int (целые числа): 1, -3, 1000 float (числа с плавающей точкой): 3.14, -0.001, 1e10 str (строки): "Hello", "Python" bool (булевы значения):'
                        'True, False Присваивание значений переменным Изменение значения переменной происходит путем присвоения нового значения: x = 10']
            var_text_1 = [
                        'print(x) # Выведет: 10'
                        'x = 20'
                        'print(x) # Выведет: 20'
                        'Множественное присваиваниеPython позволяет выполнять множественное присваивание, что делает инициализацию нескольких переменных более компактной:a, b, c = 5, 3.14, "Python"'
                        'Глобальные и локальные переменныеВ Python существуют глобальные и локальные переменные. Глобальные переменные объявляются вне функций и доступны из любой части кода.'
                        'Локальные переменные объявляются внутри функций и доступны только в этой функции. Для изменения глобальной переменной внутри функции используется ключевое слово global : x = 10'
                        'def update_variable():'
                        ' global x'
                        ' x = 20'
                        'update_variable()'
                        'print(x) # Выведет: 20'
                        'Переменные являются фундаментальным элементом программирования, позволяющим хранить, извлекать и манипулировать данными в программах.'
            ]
            await message.answer('\n'.join(var_text))
            await asyncio.sleep(3) # приостанавливаем программу на 3 сек
            await message.answer('\n'.join(var_text_1))
        # Множества
        @dp.message(lambda message: message.text == 'Множества')
        async def sets(message: types.Message):
            sets_buttons = [
                [
                types.KeyboardButton(text = "Меню"),
                types.KeyboardButton(text = "Python-1")
                ],
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard = sets_buttons, resize_keyboard=True)
            await message.answer(text='Чтобы вернуться в меню нажмите кнопку меню',reply_markup=keyboard) 
            sets_text = [
             f'\n Множество (set) в Python - это изменяемый набор уникальных и неупорядоченных элементов.'
             f'\n Оно может содержать только неизменяемые объекты, такие как целые числа, числа с плавающей точкой, строки и кортежи.'
             f'\n Уникальность означает, что каждый элемент множества не повторяется, а неупорядоченность означает, что элементы не имеют определенного порядка.'
             f'\n Создание множеств возможно несколькими способами:Использование фигурных скобок для непосредственного указания элементов: my_set = {{1, 2, 3}}.'
             f'\n Преобразование списка или кортежа в множество: my_set = set([1, 2, 3]) или my_set = set((1, 2, 3)).'
             f'\n Объединение множеств с помощью метода union().Для проверки принадлежности элемента множеству используется оператор in, который возвращает True, если элемент присутствует в множестве, и False в противном случае.'
             f'\n Удаление элементов из множества осуществляется методами remove(), discard(), clear() и pop().'
             f'\n Множества поддерживают математические операции, такие как объединение, пересечение, разность и симметричная разность.'
             f'\n Важно помнить, что множества не сохраняют порядок элементов и не допускают дублирования элементов.'   
            ]
            await message.answer('\n'.join(sets_text))
        #cycles 
        @dp.message(lambda message: message.text == 'Циклы')
        async def cycles(message: types.Message):
            cycles_buttons = [
                [
                types.KeyboardButton(text = "Меню"),
                types.KeyboardButton(text = "Python-1")
                ],
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard = cycles_buttons, resize_keyboard=True)
            await message.answer(text='Чтобы вернуться в меню нажмите кнопку меню',reply_markup=keyboard) 
            
            cycles_text = ['Циклы в Python представляют собой конструкции, позволяющие повторять выполнение блока кода определенное количество раз или до тех пор, пока не будет выполнено заданное условие.'
                           'В Python существует два основных типа циклов: for и while.']
            cycles_text_for = ['Цикл for'
                               'Цикл for используется для перебора элементов в последовательности, такой как список, кортеж, строка или диапазон чисел.'
                               'Синтаксис цикла for следующий:'
                               'for item in sequence:'
                               '# Код, который должен быть выполнен для каждого элемента последовательности'
                               '# Пример использования цикла for для вывода на экран всех элементов списка:'
                               'fruits = "apple", "banana", "cherry"'
                               'for fruit in fruits:'
                               'print(fruit)']
            cycles_text_while = [
                                f'\n Цикл while'
                                f'\n Цикл while используется для выполнения блока кода до тех пор, пока заданное условие остается истинным.'
                                f'\n Синтаксис цикла while следующий:'
                                f'\n while condition:'
                                f'\n Код, который должен быть выполнен, пока условие истинно'
                                f'\n Пример использования цикла while для подсчета до 10:'
                                f'\n count = 0'
                                f'\n while count < 10:'
                                f'\n print(count)'
                                f'\n count += 1'
                                ]
            cycles_text_operation = [f'\n Операторы управления циклами' 
                                     f'\n В Python существуют операторы, позволяющие управлять ходом выполнения циклов.'
                                     f'\n К ним относятся:'
                                     f'\n break - прерывает выполнение текущего цикла.'
                                     f'\n continue - пропускает оставшуюся часть текущей итерации цикла и переходит к следующей.'
                                     ]
            cycles_text_nested = [f'\n Вложенные циклы'
                                  f'\n В Python можно использовать вложенные циклы, то есть один цикл может быть вложен внутрь другого.'
                                  f'\n Пример использования вложенных циклов для вывода таблицы умножения:'
                                  f'\n for i in range(1, 11):'
                                  f'\n     for j in range(1, 11):'
                                  f'\n         print(i, "x", j, "=", i * j)'
                                  ]
            cycles_text_infinity = [f'\n Бесконечные циклы'
                                    f'\n Бесконечный цикл - это цикл, который никогда не заканчивается.'
                                    f'\n В Python бесконечный цикл можно создать, используя while без условия или используя while с условием, которое всегда истинно.'
                                    f'\n Пример бесконечного цикла:'
                                    f'\n while True:'
                                    f'\n # Код, который будет выполняться бесконечно'
                                    ]
            
            await message.answer('\n'.join(cycles_text))
            await asyncio.sleep(3) 
            await message.answer('\n'.join(cycles_text_for))
            await asyncio.sleep(3) 
            await message.answer('\n'.join(cycles_text_while))
            await asyncio.sleep(3) 
            await message.answer('\n'.join(cycles_text_operation))
            await asyncio.sleep(3) 
            await message.answer('\n'.join(cycles_text_nested)) 
            await asyncio.sleep(3) 
            await message.answer('\n'.join(cycles_text_infinity))      
        # f-lines
        @dp.message(lambda message: message.text == 'f-строки')
        async def flines(message: types.Message):
            flines_buttons = [
                [
                types.KeyboardButton(text = "Меню"),
                types.KeyboardButton(text = "Python-1")
                ],
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard = flines_buttons, resize_keyboard=True)
            await message.answer(text='Чтобы вернуться в меню нажмите кнопку меню',reply_markup=keyboard) 
            
            flines_text = [
                           f'\n F-строки в Python - это новый способ форматирования строк, появившийся в версии 3.6.'
                           f'\n Они позволяют встраивать выражения и значения переменных непосредственно в строку, делая код более читаемым и эффективным.'
                           f'\n Синтаксис f-строк начинается с буквы “f” перед строкой, за которой следуют выражения в фигурных скобках.'
                           f'\n Пример использования f-строк:name = "Дмитрий"'
                           f'\n age = 25'
                           f'\n print(f"Меня зовут {{name}}. Мне {{age}} лет.")'
                           ]
            flines_text_1 = [
                f'\n F-строки поддерживают расширенное форматирование чисел, дат и даже вызов методов объектов и функций.'
                f'\n Это делает их мощным инструментом для создания шаблонов и генерации текста.'
                f'\n Преимущества f-строк:Улучшенная читаемость кода за счет встраивания выражений и переменных непосредственно в строку.'
                f'\n Повышенная эффективность по сравнению с другими методами форматирования, такими как format() и %-форматирование.'
                f'\n Гибкость в использовании арифметических операций, вызовов методов и функций внутри строк.Пример использования f-строк для форматирования чисел:from math import pi'
                f'\n print(f"Значение числа pi: {{pi:.2f}}")'
                f'\n Пример использования f-строк для форматирования даты:from datetime import datetime as dt'
                f'\n now = dt.now()'
                f'\n print(f"Текущее время {{now:%d.%m.%Y %H:%M}}")'
                f'\n F-строки предоставляют удобный и эффективный способ работы со строками в Python, делая процесс разработки более приятным и продуктивным.'
            ]
            await message.answer('\n'.join(flines_text))
            await asyncio.sleep(3) 
            await message.answer('\n'.join(flines_text_1))   


        @dp.message(lambda message: message.text == 'Python-2')
        async def python_2(message: types.Message):
            py2_button = [
                [
                types.KeyboardButton(text= 'Мат-опер'),
                types.KeyboardButton(text= 'Словарь'),
                types.KeyboardButton(text= 'Функция'),
                types.KeyboardButton(text= 'Библиотека'),
                ],
            ]
            keyboard_python_2 = types.ReplyKeyboardMarkup(keyboard=py2_button,resize_keyboard=True)
            await message.answer('Выберите подходящий пункт',reply_markup=keyboard_python_2)
        # Математические операции
        @dp.message(lambda message: message.text == 'Мат-опер')
        async def mathematical_operations(message: types.Message):
            mathematical_operations_buttons = [
                [
                types.KeyboardButton(text = "Меню"),
                types.KeyboardButton(text = "Python-2")
                ],
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard = mathematical_operations_buttons, resize_keyboard=True)
            await message.answer(text='Чтобы вернуться в меню нажмите кнопку меню',reply_markup=keyboard)
            
            
            text_mathematical_operations = [f'\n Математические операции в Python включают в себя основные арифметические операции, такие как сложение, вычитание, умножение и деление, а также возведение в степень и работу с остатком от деления.'
                                            f'\n Эти операции могут быть выполнены как с целыми числами, так и с числами с плавающей точкой.'
                                            ]
            text_mathematical_operations_1 = [  f'\n Основные арифметические операции'
                                                f'\n Сложение: +'
                                                f'\n Вычитание: -'
                                                f'\n Умножение: *'
                                                f'\n Деление: /'
                                                f'\n Возведение в степень: **'
                                                ]
            text_mathematical_operations_2 = [
                                              f'\n Работа с остатком от деления'
                                              f'\n Остаток от деления в Python обозначается символом %.'
                                              f'\n Эта операция возвращает остаток от деления левого операнда на правый.'
                                              f'\n Пример: '
                                              f'\n 12 % 5 # Возвращает 2, так как 12 делится на 5 с остатком 2.'
                                              ]
            text_mathematical_operations_3 = [
                                              f'\n Приоритет операций'
                                              f'\n В Python, как и в большинстве языков программирования, существует определенный порядок выполнения операций.'
                                              f'\n Сначала выполняются операции в скобках, затем возведение в степень, потом умножение и деление, и наконец сложение и вычитание.'
                                              f'\n Если необходимо изменить порядок выполнения операций, можно использовать круглые скобки для группировки выражений.'
                                              f'\n Пример:'
                                              f'\n (5 + 3) * 2 # Сначала выполнится сложение в скобках, затем умножение.'
                                              ]
            text_mathematical_operations_4 = [
                                              f'\n Математические функции'
                                              f'\n Python предоставляет ряд встроенных математических функций, таких как abs(), pow(), sqrt(), sin(), cos(), tan(), и многие другие.'
                                              f'\n Эти функции позволяют выполнять более сложные математические вычисления, такие как нахождение квадратного корня, синуса угла, косинуса угла и т.д.'
                                              f'\n Пример использования функции pow() для возведения числа в степень:'
                                              f'\n pow(2, 3) # Возводит число 2 в степень 3, возвращая 8.'
                                              ]
        
            await message.answer('\n'.join(text_mathematical_operations))
            await asyncio.sleep(3) 
            await message.answer('\n'.join(text_mathematical_operations_1))
            await asyncio.sleep(3)
            await message.answer('\n'.join(text_mathematical_operations_2))
            await asyncio.sleep(3) 
            await message.answer('\n'.join(text_mathematical_operations_3))
            await asyncio.sleep(3) 
            await message.answer('\n'.join(text_mathematical_operations_4))
         #   
        # Словарь
        @dp.message(lambda message: message.text == 'Словарь')
        async def dictionary(message: types.Message):
            
            dictionary_buttons = [
                [
                types.KeyboardButton(text = "Меню"),
                types.KeyboardButton(text = "Python-2")
                ],
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard = dictionary_buttons, resize_keyboard=True)
            await message.answer(text='Чтобы вернуться в меню нажмите кнопку меню',reply_markup=keyboard)
            
            
            text_dictionary = [
                               f'\n Словарь в Python является неупорядоченной коллекцией произвольных объектов, доступ к которым осуществляется по ключу.'
                               f'\n Словари используются, когда необходимо создать гибкую структуру данных, обеспечивающую быстрый поиск элементов.'
                               ]
            text_dictionary_1 = [
                                f'\n Создание словаря'
                                f'\n Создать словарь в Python можно несколькими способами:'
                                f'\n Использование литерала:'
                                f'\n d = {{"dict": 1, "dictionary": 2}}'
                                f'\n Использование встроенной функции dict():'
                                f'\n d = dict(short="dict", long="dictionary")'
                                f'\n Использование метода fromkeys() для создания словаря из заданной последовательности элементов:'
                                f'\n keys = {{1,2,3,4,5,6}}'
                                f'\n values = "value"'
                                f'\n d = dict.fromkeys(keys, values)'
                                f'\n Использование генераторных выражений:'
                                f'\n d = {{a: a**2 for a in range(7)}}'
                                ]
            text_dictionary_2 = [
                                f'\n Доступ к элементам словаря'
                                f'\n Доступ к элементам словаря осуществляется по ключу, используя квадратные скобки:'
                                f'\n d = {{"dict": 1, "dictionary": 2}}'
                                f'\n print(d["dict"]) # Выведет: 1'
                                f'\n Добавление и удаление элементов'
                                f'\n Добавление новых элементов в словарь выполняется с помощью оператора присваивания:'
                                f'\n d = {{"dict": 1, "dictionary": 2}}'
                                f'\n d["new_key"] = "new_value"'
                                f'\n Удаление элементов из словаря возможно с помощью метода pop() или del:'
                                f'\n d = {{"dict": 1, "dictionary": 2}}'
                                f'\n del d["dict"]'
                                ]
            text_dictionary_3 = [
                f'\n Проверка наличия ключа'
                f'\n Проверить наличие ключа в словаре можно с помощью оператора in:'
                f'\n d = {{"dict": 1, "dictionary": 2}}'
                f'\n if "dict" in d:'
                f'\n  print("Ключ "dict" присутствует в словаре")'
                f'\n Итерация по словарю'
                f'\n Итерировать по ключам словаря можно с помощью цикла for:'
                f'\n d = {{"dict": 1, "dictionary": 2}}'
                f'\n for key in d:'
                f'\n  print(key)'
            ]
            await message.answer('\n'.join(text_dictionary))
            await message.answer('\n'.join(text_dictionary_1))
            await message.answer('\n'.join(text_dictionary_2))
            await message.answer('\n'.join(text_dictionary_3))
        # Функция
        @dp.message(lambda message: message.text == 'Функция')
        async def function(message: types.Message):
            function_buttons = [
                [
                types.KeyboardButton(text = "Меню"),
                types.KeyboardButton(text = "Python-2")
                ],
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard = function_buttons, resize_keyboard=True)
            await message.answer(text='Чтобы вернуться в меню нажмите кнопку меню',reply_markup=keyboard)
            
            text_function = [
                            f'\n Функции в Python представляют собой фрагменты программного кода, решающие определенную задачу. Они позволяют избежать дублирования кода и обеспечивают его повторное использование. Синтаксис создания функции начинается с ключевого слова def, за которым следует имя функции и ее параметры в скобках.'
                            f'\n Внутри функции можно выполнять различные операции, включая вычисления и возврат значения с помощью ключевого слова return.'
                            f'\n Функции могут принимать аргументы, которые передаются им при вызове. Также возможно создание функций с параметрами по умолчанию и аргументами переменной длины. Это делает функции гибкими и удобными в использовании.'
                            f'\n Python поддерживает передачу аргументов как по значению, так и по ссылке, в зависимости от типа объекта. Это позволяет эффективно работать с данными разных типов.'
                            f'\n Для документирования функций используются docstrings, которые описывают их назначение и поведение. Это помогает другим разработчикам лучше понимать код и облегчает его поддержку.'
                            f'\n В Python также есть возможность создавать анонимные функции с помощью лямбда-выражений, что особенно полезно для создания простых функций на лету.'
                            f'\n Функции играют важную роль в разработке на Python, делая код более читаемым, поддерживаемым и расширяемым.'
                            ]
            await message.answer('\n'.join(text_function))
        # Библиотека
        @dp.message(lambda message: message.text == 'Библиотека')
        async def library(message: types.Message):
            library_buttons = [
                [
                types.KeyboardButton(text = "Меню"),
                types.KeyboardButton(text = "Python-2")
                ],
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard = library_buttons, resize_keyboard=True)
            await message.answer(text='Чтобы вернуться в меню нажмите кнопку меню',reply_markup=keyboard)
            
            text_library = [
                f'\n Библиотеки Python представляют собой наборы функций и инструментов, созданных другими разработчиками, которые помогают в написании кода и расширяют возможности языка программирования Python. Они позволяют использовать уже написанный код в разных проектах, сокращая время разработки и улучшая качество кода. Библиотеки охватывают широкий спектр областей, включая машинное обучение, обработку данных, создание веб-приложений и многое другое.'
                f'\n Для установки библиотек используется менеджер пакетов pip, который позволяет легко и быстро устанавливать пакеты из репозиториев. После установки библиотеки её можно импортировать в свой проект и использовать её функции и классы.'
                f'\n Примеры популярных библиотек включают numpy для научных вычислений, pandas для работы с данными, matplotlib для визуализации данных, scikit-learn для машинного обучения, Flask для создания веб-приложений и многие другие.'
                f'\n Использование библиотек является важной частью процесса разработки на Python, позволяя разработчикам сосредоточиться на решении конкретных задач, а не на создании базовых функций с нуля.'
                ]
            await message.answer('\n'.join(text_library))
      
      
        @dp.message(lambda message: message.text == 'Python-3')
        async def python_3(message: types.Message):
            py3_button = [
                [
                types.KeyboardButton(text= 'ООП'),
                types.KeyboardButton(text= 'Строки'),
                types.KeyboardButton(text= 'Типы данных'),
                types.KeyboardButton(text= 'Кортеж'),
                ],
            ]
            keyboard_python_3 = types.ReplyKeyboardMarkup(keyboard=py3_button,resize_keyboard=True)
            await message.answer('Выберите подходящий пункт',reply_markup=keyboard_python_3)
        # OOP
        @dp.message(lambda message: message.text == 'ООП')
        async def oop (message: types.Message):
            oop_buttons = [
                [
                types.KeyboardButton(text = "Меню"),
                types.KeyboardButton(text = "Python-3")
                ],
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard = oop_buttons, resize_keyboard=True)
            await message.answer(text='Чтобы вернуться в меню нажмите кнопку меню',reply_markup=keyboard)
            
            oop = [
                   f'\n ООП в Python основывается на принципах инкапсуляции, наследования, полиморфизма, абстракции и композиции.'
                   f'\n Инкапсуляция объединяет данные и методы в классах, скрывая их от внешнего мира.'
                   f'\n Наследование позволяет создавать новые классы на основе существующих, наследуя их свойства и методы.'
                   f'\n Полиморфизм позволяет объектам с одинаковым интерфейсом иметь разные реализации методов.'
                   f'\n Абстракция создает упрощенные модели объектов, фокусируясь на основных характеристиках, игнорируя детали.'
                   f'\n Композиция объединяет существующие объекты для создания новых.Python поддерживает все эти принципы, предоставляя инструменты и библиотеки для работы с объектами.'
                   f'\n Особенностью ООП в Python является отсутствие строгой инкапсуляции, так как все атрибуты и методы по умолчанию открыты.'
                   f'\n Однако, существует соглашение об именовании, где атрибуты и методы, начинающиеся с подчеркивания, считаются внутренними и не должны использоваться извне.'
                   f'\n Также в Python есть магические методы, позволяющие определять поведение объектов в различных ситуациях, например, __str__ для строкового представления объекта. Python поддерживает множественное наследование, что позволяет создавать более гибкие иерархии классов, но требует осторожности из-за возможных конфликтов имен.' 
                   f'\n Для улучшения читаемости кода и удобства работы с объектами в Python используются декораторы, такие как @property, позволяющий использовать методы как атрибуты, и @staticmethod, определяющий статический метод без доступа к состоянию объекта.'
                   f'\n ООП в Python широко применяется в разработке программного обеспечения, позволяя создавать структурированные, модульные и легко поддерживаемые проекты.'
                   ]
            await message.answer('\n'.join(oop))
        # Строка
        @dp.message(lambda message: message.text == "Строки")
        async def string(message: types.Message):
            string_buttons = [
                [
                types.KeyboardButton(text = "Меню"),
                types.KeyboardButton(text = "Python-3")
                ],
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard = string_buttons, resize_keyboard=True)
            await message.answer(text='Чтобы вернуться в меню нажмите кнопку меню',reply_markup=keyboard)
            
            text_string = [
                f'\n В Python строки представляют собой упорядоченные последовательности символов, используемые для хранения и представления текстовой информации.'
                f'\n Они являются одним из основных типов данных в Python и могут содержать любые символы, включая буквы, цифры, специальные символы и пробелы. '
                f'\n Для создания строки в Python можно использовать одинарные или двойные кавычки.'
                f'\n Например:'
                f'\n a = "Это строка"'
                f'\n b = "Это тоже строка"'
                f'\n В Python есть несколько способов работы со строками. Вот некоторые из них:'
                f'\n Конкатенация - объединение двух или более строк в одну. Для этого используется оператор +. Например:a = "Привет"'
                f'\n b = "Мир!"'
                f'\n print(a + b) # Вывод: ПриветМир!'
                f'\n Дублирование - создание копии строки заданное количество раз. Для этого используется оператор *. Например:a = "Привет"'
                f'\n print(a * 3) # Вывод: ПриветПриветПривет'
                f'\n Срез - извлечение подстроки из строки. Для этого используется оператор [start:end], где start - индекс первого символа подстроки, а end - индекс символа после последнего символа подстроки. Например:a = "Привет, мир!"'
                f'\n print(a[7:12]) # Вывод: мир!'
                f'\n Методы строк - в Python есть множество методов для работы со строками. Некоторые из них:len() - возвращает длину строки.upper() - переводит строку в верхний регистр.lower() - переводит строку в нижний регистр.replace() - заменяет подстроку в строке другой подстрокой.Это лишь некоторые способы работы со строками в Python. Полный список методов и операторов можно найти в документации Python.'
            ]
            await message.answer('\n'.join(text_string)) 
        # Типы данных
        @dp.message(lambda message: message.text == "Типы данных")
        async def types_of_data(message: types.Message):
            types_of_data_buttons = [
                [
                types.KeyboardButton(text = "Меню"),
                types.KeyboardButton(text = "Python-3")
                ],
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard = types_of_data_buttons, resize_keyboard=True)
            await message.answer(text='Чтобы вернуться в меню нажмите кнопку меню',reply_markup=keyboard)
            
            text_types_of_data = [
                f'\n В Python существует несколько основных типов данных:'
                f'\n Числа: Включают целые числа (int),'
                f'\n числа с плавающей точкой (float) и комплексные числа (complex).'
                f'\n Строки: Последовательности символов, заключенные в кавычки (одинарные или двойные).'
                f'\n Списки: Изменяемые упорядоченные коллекции элементов, разделенных запятыми и заключенных в квадратные скобки.' 
                f'\n Кортежи: Неизменяемые упорядоченные коллекции элементов, разделенных запятыми и заключенных в круглые скобки.'
                f'\n Словари: Неупорядоченные коллекции пар ключ-значение, заключенные в фигурные скобки.'
                f'\n Множества: Неупорядоченные коллекции уникальных элементов, разделенных запятыми и заключенных в фигурные скобки.' 
                f'\n Python также поддерживает логический тип данных, который может принимать значения True или False.'
                f'\n Каждый тип данных имеет свои уникальные характеристики и возможности использования.'
                f'\n Например, списки и словари являются изменяемыми, что позволяет добавлять, удалять и изменять элементы после создания.'
                f'\n Кортежи и строки, напротив, являются неизменяемыми, что делает их более безопасными для использования в некоторых случаях.' 
                f'\n Важно помнить, что в Python типы данных не нужно явно объявлять при создании переменной, как это делается в некоторых других языках программирования.'
                f'\n Вместо этого Python автоматически определяет тип данных на основе значения, присвоенного переменной.'
            ]
            await message.answer('\n'.join(text_types_of_data))
        # Кортеж
        @dp.message(lambda message: message.text == "Кортеж")
        async def the_tuple(message: types.Message):
            typle_buttons = [
                [
                types.KeyboardButton(text = "Меню"),
                types.KeyboardButton(text = "Python-3")
                ],
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard = typle_buttons, resize_keyboard=True)
            await message.answer(text='Чтобы вернуться в меню нажмите кнопку меню',reply_markup=keyboard)
            
            text_tuple = [
                f'\nКортежи в Python - это неизменяемые последовательности, которые могут содержать элементы разных типов.'
                f'\nОни похожи на списки, но в отличие от них, кортежи нельзя изменять после создания.'
                f'\nЭто делает их полезными для хранения данных, которые не должны изменяться в ходе выполнения программы.'
                f'\nКортежи создаются с помощью круглых скобок () и могут содержать любое количество элементов, включая ноль.'
                f'\nДля создания кортежа с одним элементом необходимо добавить запятую после элемента, чтобы Python распознал его как кортеж.' 
                f'\nДоступ к элементам кортежа осуществляется через индексы, начиная с 0.'
                f'\nКортежи могут содержать элементы разных типов, включая числа, строки, списки и даже другие кортежи.'
                f'\nИзменение элементов кортежа напрямую невозможно, но можно создать новый кортеж, комбинируя существующие.'
                f'\nОсновные методы и функции для работы с кортежами включают count(), который возвращает количество вхождений элемента в кортеж, и index(), который возвращает индекс первого вхождения элемента.'
                f'\nТакже можно использовать срезы для создания новых кортежей на основе существующих.'
                f'\nКортежи часто используются для хранения координат точек в 2D или 3D пространстве, а также для возврата нескольких значений из функций.'
                f'\nОни могут быть использованы в качестве ключей словаря благодаря своей неизменности.'
                f'\nСоветы по работе с кортежами включают использование их для неизменяемых данных, использование распаковки кортежей для удобного присваивания значений переменным, избегание вложенных кортежей и использование именованных кортежей для улучшения читаемости кода.'
            ]
            await message.answer('\n'.join(text_tuple))
        

        
        # test
    
    def tests(self): # Тест по Python
        # Обьяевляем диспечер для теста по питону
        @dp.message(lambda message: message.text == '/testpyth')
        async def test_py(message: types.Message):
            await message.reply("Давайте начнем тест!")
            chat_id = message.chat.id
            # await message.answer("Если вам нужна помощь, пожалуйста, введите /help")
            buttons = [
                [
                types.KeyboardButton(text="Меню")
                ],
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
            await message.answer(text = "Вопрос:'1. if', '2. while', '3. for' Выберите вариант ответа 1, 2, 3", reply_markup=keyboard)
        
        
            class QuizState:
                    def __init__(self):
                        self.question_number = 0
                        self.correct_answers = 0

                    quiz_data = [
                    {
                        "question": "Вопрос 1: Какой из следующих операторов используется для ветвления в Python?",
                        "options": ["1. if", "2. while", "3. for"],
                        "correct_answer": 0
                    },
                    {
                        "question": "Вопрос 2: Что из нижеперечисленного является встроенным типом данных в Python?",
                        "options": ["1. Строка", "2. Список", "3. Кортеж"],
                        "correct_answer": 2
                    },
                    {
                        "question": "Вопрос 3: Что вернет следующий код? a = 5 b = 10 print((a + b) / (a - b))",
                        "options": ["1. 15", "2. 20", "3. 1.5"],
                        "correct_answer": 1
                    },
                    {
                        "question": "Вопрос 4: Какой специальный метод используется для создания string representation объекта в Python?",
                        "options": ["1. len", "2. str", "3. eq"],
                        "correct_answer": 1
                    },
                    {
                        "question": "Вопрос 5: Что будет выведено на экран в результате выполнения следующего кода? arr = [1, 2, 3, 4, 5] for item in arr: print(item)",
                        "options": ["1. Ничего", "2. 1", "3. 1,2,3,4,5"],
                        "correct_answer": 2
                    }
                    ]   

            state = QuizState()
            async def start_quiz(message: types.Message):
                await message.answer(state.quiz_data[state.question_number]['question'] + "\n" + '\t\n'.join(state.quiz_data[state.question_number]['options']))   
            @dp.message()
            async def check_answer(message: types.Message):
                # user_answer_index = int(message.text) - 1
                if message.text is not None:
                # try:
                    user_answer_index = int(message.text) - 1
                else:
                # except ValueError:
                    user_answer_index = 0
                correct_answer_index = state.quiz_data[state.question_number]['correct_answer']

                if user_answer_index == correct_answer_index:
                    state.correct_answers += 1
                    await message.answer("Вы ответили верно!")
                else:
                    await message.answer("Вы ответили неверно. Правильный ответ: "
                                        f"{state.quiz_data[state.question_number]['options'][correct_answer_index]}")

                state.question_number += 1

                if state.question_number < len(state.quiz_data):
                    await message.answer(state.quiz_data[state.question_number]['question'] + "\n" + '\t\n'.join(state.quiz_data[state.question_number]['options']))
                else:
                    await message.answer(f"Ваш итоговый балл: {state.correct_answers} \n нажмите кнопку меню чтобы выйти в меню")
    
    def sysadm(self):# Системное администрирование
        
        @dp.message(lambda message: message.text == "Системное Администрирование")
        async def sysadm(message: types.Message):
            
            sysadm_button = [
                [
                types.KeyboardButton(text= 'Меню'), 
                types.KeyboardButton(text= 'Читать дальше'),
                ],
            ]
            keyboard_python_1 = types.ReplyKeyboardMarkup(keyboard=sysadm_button,resize_keyboard=True)
            await message.answer('Выберите подходящий пункт',reply_markup=keyboard_python_1)
            
            text_sysadm_list = [
                [ # Процессы Linux
                 
                    f'\n Управление фоновыми заданиями Команды jobs, bg (background) и fg (foreground) позволяют управлять заданиями, выполняющимися на переднем и заднем планах:'
                    f'\n jobs выводит список фоновых процессов'
                    f'\n fg номер переводит процесс на передний план'
                    f'\n bg номер переводит процесс на задний план'
                    f'\n Посмотрим список фоновых процессов:'
                    f'\n $ jobs'
                    f'\n [1]   Запущен          nice gzip < /dev/zero > /dev/null &'
                    f'\n [2]-  Запущен          nice bzip2 < /dev/zero > /dev/null &'
                    f'\n $ jobs -l'
                    f'\n [1]   3380 Запущен          nice gzip < /dev/zero > /dev/null &'
                    f'\n [2]-  3381 Запущен          nice bzip2 < /dev/zero > /dev/null &'
                    f'\n Знак «плюс» означает «текущее», т.е. то, с которым мы работаем сейчас. Знак «минус» означает «предыдущее». Если мы завершим текущее — то предыдущее станет текущим. Команды fg и bg без номера задания будут работать с текущим.'
                    f'\n Переведем третье задание (текущее) на передний план:'
                    f'\n $ fg'
                    f'\n nice xz < /dev/zero > /dev/null'
                    f'\n Теперь терминал ожидает окончания выполнения задания. Поскольку задание у нас бесконечное — терминал будет занят бесконечно. Приостановим эту задачу с помощью Ctrl+Z:'
                    f'\n ^Z'
                    f'\n [3]+  Остановлен    nice xz < /dev/zero > /dev/null'
                    f'\n $ jobs -l'
                    f'\n [1]   3380 Запущен          nice gzip < /dev/zero > /dev/null &'
                    f'\n [2]-  3381 Запущен          nice bzip2 < /dev/zero > /dev/null &'
                    f'\n [3]+  3382 Остановлено      nice xz < /dev/zero > /dev/null'
                    f'\n Теперь, чтобы продолжить её выполнение в фоновом режиме:'
                    f'\n $ bg'
                    f'\n [3]+ nice xz < /dev/zero > /dev/null &'
                    f'\n $ jobs -l'
                    f'\n [1]   3380 Запущен          nice gzip < /dev/zero > /dev/null &'
                    f'\n [2]-  3381 Запущен          nice bzip2 < /dev/zero > /dev/null &'
                    f'\n Чтобы завершить фоновое задание, надо переместить его на передний план, а потом завершить с помощью Ctrl+C:'
                    f'\n $ fg 1'
                    f'\n nice gzip < /dev/zero > /dev/null'
                    f'\n $ jobs -l'
                    f'\n [2]-  3381 Запущен          nice bzip2 < /dev/zero > /dev/null &'
                    f'\n [3]+  3382 Запущен          nice xz < /dev/zero > /dev/null &'
                    ],
                [ # Протоколы (DHCP,SSH,http/https,tcp/udp) 
                f'\n DHCP \n (Dynamic Host Configuration Protocol) - протокол динамической настройки хостов, позволяющий автоматически назначать IP-адреса, маски подсети, шлюзы по умолчанию и другие параметры конфигурации сети. DHCP упрощает администрирование сетей, уменьшая необходимость ручной настройки каждого устройства.'
                f'\n SSH \n (Secure Shell) - протокол защищенного удаленного доступа, обеспечивающий безопасную передачу данных и команд между клиентом и сервером. SSH использует шифрование для защиты передаваемых данных, делая возможным безопасное удаленное управление системами и передачу конфиденциальной информации.'
                f'\n HTTP \n (HyperText Transfer Protocol) - основной протокол для передачи гипертекста в интернете. HTTP используется для запроса и получения веб-страниц, изображений, видео и других ресурсов с веб-сайтов. HTTPS (HTTP Secure) - это защищенный вариант HTTP, использующий шифрование для обеспечения безопасности передаваемых данных.'
                f'\n TCP \n (Transmission Control Protocol) и UDP (User Datagram Protocol) - два основных транспортных протокола в модели OSI. TCP обеспечивает надежную передачу данных с контролем ошибок и подтверждением доставки, что делает его идеальным для приложений, требующих гарантированной доставки данных. UDP, напротив, ориентирован на скорость и эффективность, жертвуя надежностью ради быстрой передачи данных, что подходит для приложений реального времени, таких как потоковое мультимедиа.'
                f'\n SMB \n (Server Message Block) - протокол сетевого файлового обмена, разработанный Microsoft для совместного использования файлов, принтеров и других ресурсов в сетях. SMB используется в операционных системах семейства Windows для обмена данными между компьютерами и доступа к сетевым ресурсам.'
                f'\n RDP \n (Remote Desktop Protocol) - проприетарный протокол прикладного уровня, разработанный Microsoft для обеспечения удаленного доступа к рабочему столу компьютера. RDP позволяет пользователям удаленно управлять компьютером, включая возможность просмотра экрана, управления мышью и клавиатурой, а также запуска приложений. RDP широко используется в корпоративных средах для удаленного администрирования серверов и рабочих станций, а также для предоставления услуг удаленного рабочего стола конечным пользователям.'    
                ], 
                [ # DNS(dig,nslookup)
                    f'\n DNS \n (Domain Name System) является системой доменных имен, которая позволяет преобразовывать удобочитаемые имена веб-сайтов и других сетевых ресурсов в числовые IP-адреса, необходимые для установления соединения между клиентом и сервером. В Linux существует несколько способов просмотра DNS-информации, включая использование команд nslookup и dig.'
                    f'\n Использование команды nslookup \n Команда nslookup позволяет выполнять различные типы запросов к DNS-серверам. Для просмотра DNS-информации о конкретном хосте или домене, можно использовать следующий синтаксис: \n nslookup имя_хоста; \n Например, чтобы узнать IP-адрес сайта example.com, введите: \n nslookup example.com'
                    f'\n Использование команды dig \n Команда dig предоставляет более детальный и гибкий способ работы с DNS. Она позволяет задавать различные параметры запроса, такие как тип запроса, серверы для запроса и многое другое. \n Синтаксис использования dig для просмотра DNS-информации следующий: dig домен_или_хост \nНапример, чтобы узнать IP-адрес сайта example.com, введите: dig example.com'
                ],
                [ # Техническая составляющая пк
                f'Техническая составляющая ПК для системного администратора включает в себя следующие ключевые аспекты:'
                f'\n 1)Вычислительное оборудование: Это сердце любой компьютерной системы. Сюда входят процессоры, материнские платы, оперативная память, видеокарты и другие компоненты, обеспечивающие обработку данных.'
                f'\n 2)Коммутационное оборудование: Включает сетевые карты, модемы, маршрутизаторы и коммутаторы, которые обеспечивают связь между различными устройствами в сети.'
                f'\n 3)_Вспомогательное инженерно-техническое оборудование: Системы охлаждения, блоки питания, корпуса и другие компоненты, обеспечивающие стабильную работу всей системы.'
                f'\n 4)Каналы связи: Это физическая среда, через которую передаются данные, например, Ethernet, Wi-Fi, USB и другие.'
                f'\n 5)Системное программное обеспечение (СПО): Операционные системы, драйверы устройств, утилиты для управления системой и обеспечения её безопасности.'
                f'\n 6)Прикладное программное обеспечение (ППО): Программы, используемые для выполнения конкретных задач, таких как обработка текстов, работа с базами данных, веб-браузеры и т.д.'
                f'\n 7)Системный администратор отвечает за настройку, обслуживание и поддержку этих компонентов, обеспечивая их бесперебойную работу и безопасность.'
                ],
                [ # osint(maltego,amass)
                    f'\n Maltego \n Maltego – это программное обеспечение, предназначенное для разведки и криминалистики, разработанное компанией Paterva из Претории, Южная Африка. Программа была выпущена 23 октября 2007 года и доступна для операционных систем Windows, macOS и Linux. \
                    Maltego фокусируется на анализе данных из открытых источников и визуализации этой информации в графическом формате, подходящем для ручного анализа связей и датамайнинга. Программа позволяет создавать пользовательские графики, представляя любой дополнительный тип информации в дополнение к основным имеющимся типам объектов. \
                    Основные области применения Maltego включают анализ социальных сетей, OSINT API, самостоятельные узлы частных данных и компьютерные сети, а также принадлежность к социальным сетям. Программа расширяет охват данных за счет интеграции с различными партнерами, включая записи DNS, записи whois, поисковые системы, службы социальных сетей, различные API и метаданные. \
                    Maltego предлагает платное клиентское ПО для настольных компьютеров с возможностью самостоятельного размещения серверов, а также бесплатное коммерческое клиентское программное обеспечение для настольных ПК под названием Maltego CaseFile. \
                    Программа широко используется компаниями, исследователями безопасности и частными детективами для анализа данных и выявления связей между объектами.'
                    
                    f'\n Amass \n Amass – это инструмент для разведки и картографирования сетей, разработанный с целью облегчения процесса сбора информации о целевых объектах. Он представляет собой фреймворк с открытым исходным кодом, предназначенный для специалистов по информационной безопасности и исследователей, занимающихся анализом уязвимостей.\
                    Amass использует методы сбора данных из открытых источников, такие как DNS-запросы, сканирование веб-страниц, анализ данных поисковых систем и другие техники, чтобы получить информацию о целевой системе или организации. Инструмент помогает идентифицировать активы, связанные с объектом исследования, и визуализировать полученные данные, что упрощает процесс анализа и понимания структуры сети.\
                    Amass поддерживает модульную структуру, позволяющую пользователям выбирать конкретные функции для выполнения задач разведки. Это делает его гибким инструментом, который можно адаптировать под различные сценарии использования, от пассивного сбора информации до активного тестирования на проникновение.\
                    Инструмент доступен для установки на различных платформах, включая Linux, macOS и Windows, и может быть использован как в исследовательских целях, так и для решения практических задач в области информационной безопасности.',
                 ],
                [ # введение в кибербез
                    f'\n Кибербезопасность \n Кибербезопасность – это комплекс мер, направленных на защиту компьютерных систем, сетей и данных от несанкционированного доступа, неправомерного использования и повреждения. Она включает в себя широкий спектр мероприятий, начиная от технических аспектов защиты информации и заканчивая организационными мерами по обеспечению безопасности.\
                    Кибербезопасность играет ключевую роль в современном мире, где информационные технологии пронизывают все сферы жизни общества. С ростом числа киберугроз, таких как кибератаки, киберпреступления и кибертерроризм, важность обеспечения надежной защиты информационных активов становится все более актуальной.\
                    Основные аспекты кибербезопасности включают в себя:\
                    Защита от вредоносного ПО: Использование антивирусного программного обеспечения, регулярное обновление программного обеспечения и операционных систем.\
                    Шифрование данных: Применение криптографических алгоритмов для защиты конфиденциальной информации.\
                    Управление доступом: Ограничение доступа к информационным ресурсам на основе ролей и разрешений.\
                    Мониторинг и обнаружение вторжений: Использование систем обнаружения вторжений и мониторинга событий безопасности.\
                    Обучение и осведомленность персонала: Повышение уровня знаний и навыков сотрудников в области кибербезопасности.\
                    Кибербезопасность является неотъемлемой частью любой современной организации, стремящейся защитить свои информационные активы и обеспечить непрерывность бизнеса.'
                 ], 
                [ # рассказывается про конфигурирование OS(Kali,Ubuntu,Fedora,Debian)
                 
                    # конфигурирование Kali
                    f'\n Конфигурирование операционной системы Kali Linux представляет собой процесс настройки и оптимизации системы для выполнения специфических задач, связанных с информационной безопасностью и тестированием на проникновение.\
                    Этот процесс включает в себя несколько ключевых этапов, направленных на повышение безопасности, стабильности и эффективности работы системы.\
                    Обновление системы: Первым шагом является обновление списка пакетов и установка последних версий программ и компонентов системы. Это позволяет обеспечить актуальность и безопасность системы.\
                    Создание надежного пользователя: Создание нового пользователя с ограниченными правами для повседневного использования помогает снизить риск несанкционированного доступа к системе.\
                    Настройка сети: Обеспечение стабильного сетевого соединения и настройка сетевых параметров, таких как IP-адрес, маска подсети и шлюз по умолчанию, критически важно для успешного взаимодействия с сетью.\
                    Установка SSH сервера: Установка и настройка SSH сервера обеспечивает удаленный доступ к системе, что является необходимым инструментом для многих задач информационной безопасности.\
                    Настройка брандмауэра: Использование брандмауэра, такого как ufw, для управления сетевым трафиком и обеспечения дополнительной защиты системы.\
                    Настройка времени и даты: Правильная настройка времени и даты важна для корректной работы многих системных служб и приложений.\
                    Установка драйверов и дополнительного ПО: Установка необходимых драйверов и программного обеспечения, включая инструменты для тестирования на проникновение, повышает функциональность и эффективность работы системы.\
                    Резервное копирование: Регулярное создание резервных копий важных данных предотвращает потерю информации в случае сбоя системы.\
                    Эти шаги представляют собой основу для начальной настройки Kali Linux, однако в зависимости от конкретных потребностей и целей использования системы, могут потребоваться дополнительные настройки и конфигурации.'
                    
                    # конфигурирование Ubuntu
                    f'\n Конфигурирование операционной системы Ubuntu, как и любой другой Linux-системы, включает в себя настройку множества параметров, начиная от базовых настроек системы и заканчивая более специфическими параметрами, такими как конфигурация сети, безопасность и управление пользователями.\
                    Основные конфигурационные файлы Ubuntu расположены в каталоге /etc, который является хранилищем для большинства системных настроек. Эти файлы включают в себя /etc/fstab для настройки монтирования файловых систем, /etc/hosts для сопоставления IP-адресов с именами хостов, /etc/nsswitch.conf для настройки порядка разрешения имён, /etc/passwd и /etc/shadow для управления учётными записями пользователей, а также множество других файлов, отвечающих за различные аспекты работы системы.\
                    Конфигурирование Ubuntu может включать в себя изменение содержимого этих файлов вручную, однако рекомендуется использовать официальные инструменты управления пакетами и конфигурацией, такие как dpkg, apt и systemctl, для обеспечения безопасности и согласованности изменений.\
                    Также важным аспектом является использование механизмов безопасности, таких как шифрование диска, настройка брандмауэра и установка обновлений безопасности.\
                    В целом, конфигурирование Ubuntu требует глубокого понимания работы Linux и его компонентов, а также умения работать с командной строкой и инструментами управления системой.'
                   
                    # конфигурирование Fedora
                    f'\n Конфигурирование операционной системы Fedora, как и любой другой Linux-системы, включает в себя настройку множества параметров, начиная от базовых настроек системы и заканчивая более специфическими параметрами, такими как конфигурация сети, безопасность и управление пользователями.\
                    Основные конфигурационные файлы Fedora расположены в каталоге /etc, который является хранилищем для большинства системных настроек. Эти файлы включают в себя /etc/fstab для настройки монтирования файловых систем, /etc/hosts для сопоставления IP-адресов с именами хостов, /etc/nsswitch.conf для настройки порядка разрешения имён, /etc/passwd и /etc/shadow для управления учётными записями пользователей, а также множество других файлов, отвечающих за различные аспекты работы системы.\
                    Конфигурирование Fedora может включать в себя изменение содержимого этих файлов вручную, однако рекомендуется использовать официальные инструменты управления пакетами и конфигурацией, такие как dnf, rpm и systemctl, для обеспечения безопасности и согласованности изменений.\
                    Также важным аспектом является использование механизмов безопасности, таких как шифрование диска, настройка брандмауэра и установка обновлений безопасности.\
                    В целом, конфигурирование Fedora требует глубокого понимания работы Linux и его компонентов, а также умения работать с командной строкой и инструментами управления системой.'
                ], 
            ]
                
            current_text_index = 0
            while current_text_index < len(text_sysadm_list):
                mes = await message.answer('\n'.join(text_sysadm_list[current_text_index]))
                document = FSInputFile('')
                await bot.send_document(message.chat.id, document)
                await message.answer("Читать дальше?")
                await asyncio.sleep(2)
                #break
        
                @dp.message(lambda message: message.text == "Читать дальше")
                async def handle_read_more(text: Message):
                    nonlocal current_text_index
                    current_text_index += 1
                    if current_text_index < len(text_sysadm_list):
                        await message.answer('\n'.join(text_sysadm_list[current_text_index]))
                        #document = FSInputFile('/home/sla/Рабочий стол/kod/бот телеграмм/docs/Михалков.pdf')
                        #await bot.send_document(message.chat.id, document)
                        if current_text_index == 3:
                            document = FSInputFile('')    
                            await bot.send_document(message.chat.id, document)
                        await message.answer("Читать дальше?")
                        await asyncio.sleep(2)
                        if current_text_index == 4:
                            document = FSInputFile('')    
                            await bot.send_document(message.chat.id, document)
                        await message.answer("Читать дальше?")
                        await asyncio.sleep(2)
                        if current_text_index == 5:
                            document = FSInputFile('')    
                            await bot.send_document(message.chat.id, document)
                        await message.answer("Читать дальше?")
                        await asyncio.sleep(2)
                    else:
                            await message.answer("Больше информации нет.")
                            await asyncio.sleep(2)
                            current_text_index = 0
                break
                
    def cpp(self):
        
        # отвечаем на меню
        @dp.message(lambda message: message.text == "C++")
        async def cpp(message: types.Message):
            # Отправка файла по ссылке
            await bot.send_photo(
                message.chat.id, photo="https://s.digitalocean.ru/upload/1702019548_684.jpg",
                caption=f'C++ - это компилируемый, статически типизированный язык программирования общего назначения, который поддерживает парадигмы процедурного, объектно-ориентированного и обобщённого программирования. \
                    Он сочетает в себе свойства как высокоуровневых, так и низкоуровневых языков, что делает его подходящим для широкого спектра задач, включая разработку операционных систем, разнообразных прикладных программ, драйверов устройств, приложений для встраиваемых систем, высокопроизводительных серверов и компьютерных игр.',
                reply_to_message_id = message.message_id
            )
            cpp_button = [
                    [
                    types.KeyboardButton(text= 'Меню'),
                    types.KeyboardButton(text= 'Изучать'),
                    ],
                ]
            keyboard_cpp = types.ReplyKeyboardMarkup(keyboard=cpp_button,resize_keyboard=True)
            await message.answer('Выберите подходящий пункт',reply_markup=keyboard_cpp)
        @dp.message(lambda message: message.text == 'Изучать')
        async def learn_cpp(message: types.Message):
            cpp_button = [
                
                [
                    types.KeyboardButton(text= 'Типы данных С++'),
                    types.KeyboardButton(text= 'Переменные С++'),
                    types.KeyboardButton(text= 'f-строки С++'),    
                ],
                [
                    types.KeyboardButton(text= 'Массивы'),    
                    types.KeyboardButton(text= 'Множества С++'),
                    types.KeyboardButton(text= 'Циклы С++'),
                    types.KeyboardButton(text= 'Функии С++')
                ],
            ]
            keyboard_cpp_1 = types.ReplyKeyboardMarkup(keyboard=cpp_button,resize_keyboard=True)
            await message.answer('Выберите подходящий пункт',reply_markup=keyboard_cpp_1)
        # Списки
        @dp.message(lambda message: message.text == 'Массивы')
        async def arrays(message: types.Message):
            list_buttons = [
                [
                types.KeyboardButton(text = "Меню"),
                types.KeyboardButton(text = "C++")
                ],
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard=list_buttons, resize_keyboard=True)
            await message.answer(text='Чтобы вернуться в меню нажмите кнопку меню',reply_markup=keyboard)          
            array_text = [f'\n Массивы в C++ представляют собой последовательность объектов одного типа, занимающих смежные области памяти. Они могут быть одномерными, двумерными и многомерными, причем двумерные массивы аналогичны матрицам в математике.\
                Массивы характеризуются такими параметрами, как размер массива (число элементов), размер элемента (число байтов на элемент), имя массива (идентификатор) и адрес массива (адрес первого элемента).']
            array_text_2 = [f'В C++ массивы могут быть созданы как автоматически (размеры известны на момент компиляции), так и динамически (размеры неизвестны до выполнения программы). Автоматические массивы выделяются в стеке, что ограничивает их размер, в то время как динамические массивы создаются в куче, позволяя использовать большие объемы памяти.\
                \n Для работы с массивами используются циклы, позволяющие перебирать элементы массива и выполнять над ними различные операции. \n Важно помнить, что при работе с массивами необходимо учитывать их размер, чтобы избежать выхода за пределы массива и возникновения ошибок.']
            await message.answer('\n'.join(array_text))
            await asyncio.sleep(3) # приостанавливаем программу на 3 сек
            await message.answer('\n'.join(array_text_2))
        # Переменные
        
        @dp.message(lambda message: message.text == 'Переменные С++')
        async def var_cpp(message: types.Message):
            cpp_buttons = [
                [
                types.KeyboardButton(text = "Меню"),
                types.KeyboardButton(text = "C++")
                ],
            ]
            keyboard_cpp_buttons = types.ReplyKeyboardMarkup(keyboard = cpp_buttons, resize_keyboard=True)
            await message.answer(text='Чтобы вернуться в меню нажмите кнопку меню',reply_markup=keyboard_cpp_buttons)          
            var_text_cpp = [f'\n Переменные в C++ являются именованными ячейками памяти, предназначенными для хранения данных. Они могут быть разных типов, таких как int для целых чисел, float для чисел с плавающей точкой, double для повышенной точности чисел с плавающей точкой, char для символов и bool для логических значений.\
                        Объявление переменной включает указание её типа и имени. Например, int myAge = 25; объявляет переменную myAge типа int и инициализирует её значением 25.']
            var_text_1_cpp = [f'\n Переменные могут быть локальными, объявленными внутри функции или блока, и глобальными, объявленными вне всех функций. Глобальные переменные доступны из любой точки программы, в то время как локальные видны только в пределах своего блока.\
                            Область видимости переменной определяет, где она доступна для использования. Например, локальная переменная видна только внутри функции, в которой она объявлена.\
                            Важно следить за типами переменных, чтобы избежать ошибок при их использовании. Некорректное использование типов может привести к ошибкам во время выполнения программы.']
            await message.answer('\n'.join(var_text_cpp))
            await asyncio.sleep(3) # приостанавливаем программу на 3 сек
            await message.answer('\n'.join(var_text_1_cpp))
        # Множества
        @dp.message(lambda message: message.text == 'Множества С++')
        async def sets(message: types.Message):
            sets_buttons = [
                [
                types.KeyboardButton(text = "Меню"),
                types.KeyboardButton(text = "C++")
                ],
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard = sets_buttons, resize_keyboard=True)
            await message.answer(text='Чтобы вернуться в меню нажмите кнопку меню',reply_markup=keyboard) 
            sets_text = [
                        'Множества в C++ представляют собой контейнеры, которые автоматически сортируют добавляемые элементы в порядке возрастания.\
                        Они определены в стандартной библиотеке шаблонов (STL) через класс set. Особенностью множеств является то, что при добавлении одинаковых значений, множество будет хранить только один его экземпляр.\
                        Это отличает их от мультимножеств (multiset), которые могут содержать дубликаты.\
                        Для использования множеств необходимо подключить библиотеку <set>:\
                        #include <set>\
                        Объявление множества выглядит следующим образом:\
                        set<тип_элемента> имя_множества;\
                        где тип_элемента указывает тип элементов, которые будут храниться в множестве, а имя_множества - имя самого множества.\
                        Множества поддерживают следующие основные операции:\
                        empty() - проверяет отсутствие элементов в контейнере;\
                        size() - возвращает количество элементов в контейнере;\
                        clear() - очищает контейнер;\
                        insert() - добавляет элементы в контейнер;\
                        erase() - удаляет элементы из контейнера;\
                        count() - возвращает количество элементов, соответствующих определенному ключу;\
                        find() - находит элемент с конкретным ключом;\
                        lower_bound() и upper_bound() - возвращают итераторы на первый элемент не менее или больше определенного значения соответственно.']
            await message.answer('\n'.join(sets_text))
        #cycles 
        @dp.message(lambda message: message.text == 'Циклы С++')
        async def cycles(message: types.Message):
            cycles_buttons = [
                [
                types.KeyboardButton(text = "Меню"),
                types.KeyboardButton(text = "C++")
                ],
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard = cycles_buttons, resize_keyboard=True)
            await message.answer(text='Чтобы вернуться в меню нажмите кнопку меню',reply_markup=keyboard) 
            
            cycles_text = [
                            'Циклы в C++ используются для многократного выполнения блока кода до тех пор, пока выполняется заданное условие.\
                            Существует несколько типов циклов:\
                            Цикл while - это цикл с предусловием, который проверяет условие перед выполнением тела цикла. Если условие истинно, тело цикла выполняется. Пример:\
                            while (условие) {{\
                             // тело цикла\
                            }}\
                            Цикл do-while - это цикл с постусловием, который выполняет тело цикла хотя бы один раз, а затем проверяет условие.\
                            Если условие истинно, цикл повторяется. Пример:\
                            do {{\
                             // тело цикла\
                            }} while (условие);\
                            Цикл for - это цикл со счетчиком, который состоит из трех частей: инициализации, условия и шага. Пример:\
                            for (инициализация; условие; шаг) {{\
                             // тело цикла\
                            }}\
                            В C++ также доступны операторы break и continue, которые позволяют досрочно выйти из цикла или перейти к следующей итерации соответственно.']
            
            
            await message.answer('\n'.join(cycles_text))
            await asyncio.sleep(3)     
        # f-lines
        @dp.message(lambda message: message.text == 'f-строки С++')
        async def flines(message: types.Message):
            flines_buttons = [
                [
                types.KeyboardButton(text = "Меню"),
                types.KeyboardButton(text = "C++")
                ],
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard = flines_buttons, resize_keyboard=True)
            await message.answer(text='Чтобы вернуться в меню нажмите кнопку меню',reply_markup=keyboard) 
            
            flines_text = [
                        f'В C++ f-строки представляют собой новый способ форматирования строк, введенный в стандарте C++17.\
                        Они позволяют встраивать выражения непосредственно в строковые литералы, что упрощает процесс форматирования и делает код более читаемым.\
                        Синтаксис f-строк следующий: f"выражение". Выражение может быть любым допустимым выражением C++, которое будет вычислено и подставлено в строку.\
                        Это позволяет легко вставлять значения переменных, результаты вычислений и даже вызовы функций прямо в строковые литералы.\
                        Пример использования f-строк:\
                        #include <iostream>\
                        using namespace std;\
                        int main() {{\
                         int num = 5;\
                         cout << f"Число равно {{num}}." << endl;\
                         return 0;\
                        }}\
                        В этом примере значение переменной num будет подставлено в строку, и на экран выведется сообщение "Число равно 5.".\
                        F-строки предоставляют удобный способ форматирования строк, особенно когда требуется вставить динамические данные в строку.\
                        Они могут значительно упростить код и сделать его более понятным.']
            await message.answer('\n'.join(flines_text))
            await asyncio.sleep(3) 
        # Функции
        @dp.message(lambda message: message.text == 'Функции С++')
        async def funct(message: types.Message):
            flines_buttons = [
                [
                types.KeyboardButton(text = "Меню"),
                types.KeyboardButton(text = "C++")
                ],
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard = flines_buttons, resize_keyboard=True)
            await message.answer(text='Чтобы вернуться в меню нажмите кнопку меню',reply_markup=keyboard) 
            
            funct_text = ['']
            funct_text_1 = ['']
            await message.answer('\n'.join(funct_text))
            await asyncio.sleep(3) 
            await message.answer('\n'.join(funct_text_1))   
        # Типы данных
        @dp.message(lambda message: message.text == 'Типы данных С++')
        async def tipes_of_data(message: types.Message):
            flines_buttons = [
                [
                types.KeyboardButton(text = "Меню"),
                types.KeyboardButton(text = "C++")
                ],
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard = flines_buttons, resize_keyboard=True)
            await message.answer(text='Чтобы вернуться в меню нажмите кнопку меню',reply_markup=keyboard) 
            
            tipes_of_data_text = ['']
            tipes_of_data_text_1 = ['']
            await message.answer('\n'.join(tipes_of_data_text))
            await asyncio.sleep(3) 
            await message.answer('\n'.join(tipes_of_data_text_1))  
        

card_menu = Menu()
card_menu.m() # кнопки главное меню
card_menu.py() # питон
card_menu.tests() # тест по питону
card_menu.sysadm() # Системное администрирование
card_menu.cpp() # C++


# Хэндлер на команду /echo
@dp.message(Command("echo"))
async def talk(message: types.Message):
    await message.answer(f'Я тебя не понимаю')
         
# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)



asyncio.run(main())
