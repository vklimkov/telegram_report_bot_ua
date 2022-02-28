# Юзер-Бот, що автоматизує репортування Телеграм каналів пропагандистів

## Форкнуто з - [репи](https://github.com/Antcating/telegram_report_bot_ua)

Цей Телеграм Юзер-Бот використовується для автоматизації репорту пропагандистьских каналів.

## Інсталяція

1. По-перше, вам необхідно інсталювати Python3. Python можна завантажити за [посиланням](https://www.python.org/).
2. Качаємо MongoDB. [link](https://www.mongodb.com/try/download/community?tck=docs_server)
3. 3. Запустіть консоль. Для цього використовуйте комбінацію клавіш Win+R, у з'явившомуся вікні напишіть cmd та натисніть enter
4. Далі виконуємо наступні команди:

```
git clone https://github.com/Antcating/telegram_report_bot_ua
cd telegram_report_bot_ua
pip install -r requirements.txt
```

4. Переходимо за посиланням https://my.telegram.org/, вводимо свій номер телефону та код авторизації
   <br>Переходимо у вкладку API development tools, пишемо любий App title та Short name
   <br>Нагорі отримуємо App api_id та App api_hash
   <br>**ПЕРЕДАВАТИ КОМУСЬ `api_id` та `api_hash` НІ В ЯКОМУ РАЗІ НЕ МОЖНА!!! Вони дают можливіть контролювати вашу персональну сторінку у Телеграмі.**

## Використання

1. Копіюємо і перейменовуємо `./example.env` на `./env`
2. Підставляємо в `./.env` свої `API_ID` та `API_HASH`
3. Далі запускаємо бота:`python main.py`
4. за запитом telegraf по черзі вводимо:

- Телефон вашого аккаунта у форматі +380ххххххххх
- Код автентифікації який прийде повідомленням у телеграм

3. Бот автоматично створить базу(MongoDB) і виставить пріорітети на кожен канал із файлу `telegram_db`, за замовчуванням 1. Після запуску буде брати щоразу канал, який використовувався найпізніше також візьме до уваги пріоритет із файлу.
   <br>**Правильно налаштована програма буде відображати такий результат:**
   <br><br>![image](https://user-images.githubusercontent.com/39994538/155859028-e83b5228-e711-4f21-bf4e-db9b1cfccb24.png)

Щоб використати інший аккаунт, треба видалили файл `session_new.session` у папці з програмою (або використати команду `del session_new.session`).

## Формат списку каналів для репорту
    someChannelName|1
    mostDangedChannelName|3
    someOtherChannelName|1
    

## Безпека телеграм-акаунту

Під час налаштування бота вам буде потрібно вказати одноразовий код на сайті my.telegram.org та у python модулі [telethon](https://github.com/LonamiWebs/Telethon). Перше - це офіційний сайт телеграму, друге - це дуже відомий модуль, код якого був перевірений досвідченими програмістами не один раз. Тож ваш акаунт не передається третім особам на протязі всього процесу налаштування та використання програми.
<br>Також програма емулює поведінку нового пристрою який використовує ваш акаунт. Ви можете побачити цей віртуальний пристрій в активних сеансах телеграму (Налаштування -> Приватність і безпека -> Показати всі сеанси). Він матиме таку ж назву і тип які ви вкажете під час реєстрації на my.telegram.org. _Після виконання програми ви можете видалити цей девайс з активних сеансів._

## Додаткова інформація

У теці проєкту знаходиться файл `telegram_db`, що містить у собі список пропагандистських каналів. Якщо ви маєте інформацію про інші канали, що не війшли у список, але заслуговують репорту - присилайте їх мені у [телеграм](https://www.t.me/Achating) або додавайте їх у реквестах на Github.
```
