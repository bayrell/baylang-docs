# Установка BAYRELL Cloud OS на десктоп

Это тонкий клиент для управления Облачной ОС.

Устанавливать нужно локально на компьютер, а не на сервер.

## Установка на Linux

1) Установите Python 3.6

2) Установите Облачную ОС

```
pip3 install --upgrade cloud-os-desktop
```

3) Запустите Облачную ОС из консоли командой

```
cloud_os_desktop
```

Если возникает ошибка при запуске

```
undefined symbol:_ZNSt12out_of_rangeC1EPKc, version Qt_5
```

нужно сделать:

```
sudo apt install python3-qtpy
```

## Установка на Windows

1) Скачайте Python 3.10 с сайта https://www.python.org/downloads/

2) Запустите установщик. Нажмите на кнопку Customize installation

![screenshot_20221016_182140](https://blog.bayrell.org/wp-content/uploads/2022/10/screenshot_20221016_182140.png?_=1665924472000)

![screenshot_20221016_182205](https://blog.bayrell.org/wp-content/uploads/2022/10/screenshot_20221016_182205.png?_=1665924473000)

Нажмите на флажок Add environment to PATH.

Установите в папку C:\Python310

![screenshot_20221016_182232](https://blog.bayrell.org/wp-content/uploads/2022/10/screenshot_20221016_182232.png?_=1665924472000)

3) Откройте командную строку от администратора и выполните команду

```
pip install --upgrade cloud-os-desktop
```

4) Создайте Ярлык с названием "Cloud OS" на рабочем столе со следующей командой

```
C:\Python310\pythonw.exe -c "from cloud_os_desktop.app import run; run()"
```

5) Запустите ярлык