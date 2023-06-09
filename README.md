# ASCII Art Editor
Данный проект представляет собой конвертер изображений в ASCII-арт.
Программа создана студентами 2 курса направления математика и компьютерные науки института математики и механики: Зубковым Владиславом и Новиковой Анастасией.
## Как это работает
ASCII-арт представляет собой изображение, состоящее из символов ASCII. Конвертер берет изображение, разбивает его на пиксели и заменяет каждый пиксель на соответствующий символ ASCII в зависимости от его яркости. Яркость каждого пикселя определяется как среднее значение его красного, зеленого и синего каналов. В результате получается ASCII-арт, который можно сохранить в виде текстового файла.

## Установка и использование
Для работы конвертера необходим Python 3.6 или выше. Для установки необходимых библиотек можно воспользоваться командой:

```
pip install -r requirements.txt
```

Для запуска конвертера нужно переместить необходимый JPG-файл в папку images и выполнить команду:

```
python main.py name width height
```

где name - имя JPG-файла, который нужно преобразовать в ASCII-арт
    width - ширина ASCII-арт
    height - высота ASCII-арт

