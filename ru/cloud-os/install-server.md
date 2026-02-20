# Установка BAYRELL Cloud OS на сервер

<iframe width="100%" height="500" src="https://www.youtube.com/embed/TlzsL3pxKn4?si=6eLQz2fnhVNqUEND&rel=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen="true"></iframe>

Инструкция:

1) Установите приложения

```
sudo apt-get install mc nano git
```

2) Настройка DNS

Выполните
```
sudo rm /etc/resolv.conf
sudo nano /etc/resolv.conf
```

Укажите следующие настройки

```
nameserver 127.0.0.53
options edns0 trust-ad
ndots:1
search .
```

3) Скачайте скрипт

```
git clone https://github.com/bayrell-os/cloud_os
cd cloud_os
```

4) Выполните

```
bash cloud_os.sh 0.5.1
```

Подождите пока выполнится скрипт установки. Он также вас попросит ввести логин администратора, и в конце создаст и выведет его на экран.

5) Добавьте в автозапуск облачную ОС

Создайте файл через команду

```
sudo nano /etc/rc.local
```

Пропишите в нем команды:

```
#!/bin/bash

for i in $(seq 0 1); do
	sleep 10
	docker start cloud_os_standard
done
```

Поставьте флаг выполнения для этого файла

```
sudo chmod +x /etc/rc.local
```

6) Добавьте пользователя ubuntu в группу docker

```
sudo usermod -a -G docker ubuntu
```

7) Перезагрузите сервер

```
sudo init 6
```

8) Установка завершена!
