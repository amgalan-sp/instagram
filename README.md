# Космический Инстаграм

В данном проекте подгружаются фотографии с последнего запуска Spacex, или коллекции Хаббл в ваш аккаунт в Инстаграмме

### Как установить

Для начала Вам нужно создать файл .env, в котором должны быть прописаны значения
```Python3
username=you_username
password=your_password
```
и сохранить его в коренной папке.

Если данные введены правильно, при выполнении файла spacegram.py высветится: `INFO - Instabot Started`, `INFO - Logged-in successfully `
, что означает успешную авторизацию в Instagram.

Python3 должен быть уже установлен.
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
Далее, вам необходимо при выполнении скрипта spacegram.py ввести формат файла (расширение изображения), в котором вы хотели бы скачать из серверов Spacex или hubble, и загрузить в Instagram, а также в случае использования hubble - ввести название коллекции фотографий hubble - news, holiday_cards, wallpaper, spacecraft, printshop, или stsci_gallery и т.д.
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
