# Распознавание речи

Этот код предназначен для обработки входящих сообщений бота ВК и Телеграмм!
Использует Dialogflow API для обработки текстовых запросов.

## Депой

Тут можно проверить бота Телеграмм в работе: [Telegramm](https://telegram.me/Speech_recognition_py_bot)

Тут можно проверить бота Вконтакте в работе: [Vk](https://vk.com/public221222014)

## Запуск

- Скачайте код
- Установите зависимости
- Запустите бота командой `python3 tg_bot.py/vk_bot.py`

## Установка зависимостей:

Операционная система Windows
 - Запускаем CMD (можно через Win+R, дальше вводим`cmd`) и вписываем команду`cd /D <путь к папке со скриптами>`

Операционная система Linux
 - Запускаем Terminal (Ctrl + Alt + T) и вписываем команду`cd /D <путь к папке со скриптами>`

Операционная система macOS
 - Запускаем Terminal (Вид>Терминал) и вписываем команду`cd /D <путь к папке со скриптами>`

```pip install -r requirements.txt```

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 3 переменные:
- `TG_BOT_TOKEN` — Получить [тут](https://telegram.me/BotFather)
- `TG_USER_ID` — Получить [тут](https://telegram.me/my_id_bot)
- `GOOGLE_PROJECT_ID` — Получить [тут](https://support.google.com/a/answer/10070793?hl=ru)
- `GOOGLE_APPLICATION_CREDENTIALS` — Путь до файла credentials.json. Получить [тут](https://cloud.google.com/docs/authentication/api-keys)
- `VK_GROUP_TOKEN` — Получить [тут](https://dvmn.org/filer/canonical/1556554255/101/)

## Версия Python: 
Я использовал Python `3.8.3`, но он должен работать на любой более новой версии.

## Цель проекта:
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).

## Автор
(2023) Zaitsev Vladimir

## Пример результата для Telegram:
![image](https://dvmn.org/filer/canonical/1569214094/323/)

## Пример результата для Вконтакте:
![image](https://dvmn.org/filer/canonical/1569214089/322/)
