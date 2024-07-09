## Этапы реализации

1) Базовый интерфейс - 2 часа
2) Создание графа пользователем - 4-5 часов
3) Сохранение и загрузка графов - 1-2 часа
4) Алгоритмы Дейкстры, Форда-Беллмана и Джонсона - по 2-3 часа (6-9 часов на все 3)
5) Алгоритм 1N-ON-AC-SI - 3-4 часа
6) Финальная доработка (к примеру, вынести какие-нибудь параметры в настройки) - 3 часа

19-25 часов + 30% (запас) => 25-33 часа

## Генерация exe-файла

```shell
pyinstaller --noconfirm --windowed --onefile --name "Path on graph" --add-data "../../resources/;resources/"  --distpath output/executable/ --specpath output/specification/ --workpath output/build/ main.py
```
