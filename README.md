# Автофарм Agent 301

-  Можно загрузить сотни акков
-  Работа по ключу, без авторизации
-  Выполняет задания 
-  Крутит колесо


## Для выполнения заданий запускать task.py, для прокрута колеса wheel.py
Если нужно что б он каждые 24 часа проверял задания, если добавят дейлик, там есть функция стриков, то внизу кода измените строчку, там есть коммент

# Установка:
1. Установить python (Протестировано на 3.11)

2. Зайти в cmd(терминал) и вписывать
   Если сказали на раб стол винды
   ```
   cd Desktop
   ```
Если в другом месте, то ищите свой путь   

Переходим в папку скрипта:
   ```
   cd steamify
   ```
4. Установить модули
   
   ```
   pip install -r requirements.txt
   ```
 
   или
   
   ```
   pip3 install -r requirements.txt
   ```



5. Запуск
   ```
   python task.py
   ```

   или

   ```
   python3 task.py
   ```
   или wheel.py для прокрута колеса

# Или через Pycharm ГАЙД на любых системах и решения ошибок внизу гайда
https://telegra.ph/Avtoklikker-dlya-BLUM-GAJD-05-29
   



## Вставить в файл init_data ключи такого вида, каждый новый ключ с новой строки:
   ```
   query_id=xxxxxxxxxx&user=xxxxxxfirst_namexxxxxlast_namexxxxxxxusernamexxxxxxxlanguage_codexxxxxxxallows_write_to_pmxxxxxxx&auth_date=xxxxxx&hash=xxxxxxx
   query_id=xxxxxxxxxx&user=xxxxxxfirst_namexxxxxlast_namexxxxxxxusernamexxxxxxxlanguage_codexxxxxxxallows_write_to_pmxxxxxxx&auth_date=xxxxxx&hash=xxxxxxx
   query_id=xxxxxxxxxx&user=xxxxxxfirst_namexxxxxlast_namexxxxxxxusernamexxxxxxxlanguage_codexxxxxxxallows_write_to_pmxxxxxxx&auth_date=xxxxxx&hash=xxxxxxx
   query_id=xxxxxxxxxx&user=xxxxxxfirst_namexxxxxlast_namexxxxxxxusernamexxxxxxxlanguage_codexxxxxxxallows_write_to_pmxxxxxxx&auth_date=xxxxxx&hash=xxxxxxx
   ```
Вместо query_id= может быть user=, разницы нету
# Как получить query_id:
Заходите в telegram web, открываете бота, жмете F12 или в десктопной версии нужно зайти в настройки, доп настройки, экспериментальные настройки и включить "Enable webview inspecting", тогда при нажатии F12 у вас откроется окно,переходите в Network. жмете старт в веб версии или обновляете страницу в десктопной (на три точки нажать), ищете запрос с именем getMe, в правой колонке находите query_id=бла бла бла или user=

![photo_2024-08-31_15-51-38](https://github.com/user-attachments/assets/7403da86-b968-4d89-be95-72a80098d14c)

