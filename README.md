[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
![PyInstaller](https://img.shields.io/badge/-PyInstaller-464646?style=flat-square)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=flat-square&logo=pandas&logoColor=white)
# loadfromVK
Приложение собирает статистику всех обьявлений во всех рекламных компаниях клиента и преобразует ее в csv-файл. 
## Содержание
- [Актуальность](#актуальность)
- [Выгружаемые данные](#выгружаемые-данные)
- [Инструкция](#инструкция)

## Актуальность
 - Независимость от виртуального окружения. Доступность для широкой аудитории
 - Возможность получить статистику сразу по всем обьявлениям

## Выгружаемые данные
По умолчанию данные можно получить по дням за указанный период. 
В выгрузке вы найдете следующие поля:
- __campaign_id__ - ID рекламной компании
-  __ad_id__ - ID рекламного обьявления
- __impressions__ - просмотры
- __clicks__ - клики
- __spent__ - потраченные средства
- __date__ - дата
- __reach__ - охват
- __link_external_clicks__ - количество уникальных переходов по ссылкам
- __join_rate__ - вступления в группу

[Полный список полей, представленных методом ads.getStatistics](https://dev.vk.com/method/ads.getStatistics)

## Инструкция
1. Зарегистрируйте приложение в ВК.
   - Следуя [ссылке](https://vk.com/apps?act=manage), создайте приложение. ID этого приложения будет необходим для запросов
2. В папке запустите исполняемый файл(load_data.exe). Он автономен, его можно перенести в удобное вам место.
Заполните настройки личного кабинета ВК. Пример для заполнения доступен в файле [.env.example](https://github.com/number92/loadfromVK/blob/main/.env.example)
![Образец](https://github.com/number92/loadfromVK/blob/main/screenshots/1.png)
Получите и вставьте access_token
![Образец](https://github.com/number92/loadfromVK/blob/main/screenshots/2.png)
