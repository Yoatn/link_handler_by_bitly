# link_handler_by_bitly

Приложение взаимодействует через API с сервисом bit.ly.<br/>
https://bitly.com - Сервис сокращения URL-адресов.<br/><br/>
В приложении реализовано:
* Сокращение URL пользователя до короткого URL (short_url) вида https://bit.ly/3GmqTqe.
* Получение информации о short_url:
  * Актуальность.
  * Количество переходов по данному short_URL за всё время.</br>

### Установка
Python3 должен быть уже установлен.</br> 
Для установки зависимостей используйте `pip` (или `pip3`, если есть конфликт с Python2):
```
pip install -r requirements.txt
```
Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html) для изоляции проекта.
___
### Создание short_url.
```
python main.py {users_url}      
```
Результат:
```
Битлинк https://bit.ly/3ASAjsg
```
___
### Проверка short_url.
```
python main.py https://bit.ly/3ASAjsg
 
```
Результат:
```
По Вашей ссылке прошли 3 раз(а)
```
### Некорректый ввод или неактуальный short_url
___
Результат:
```
Invalid URL.
```
___
Код написан в образовательных целях на онлайн курсе по Python [dvmn.org](https://dvmn.org)





