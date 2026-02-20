# Шаблоны и модификаторы

Деплой приложений в BAYRELL Cloud OS осуществляется через веб интерфейс. Основная идея, что пользователю не нужно создавать yaml файлы.

При запуске приложения, пользователь указывает какое приложение нужно запустить, и его необходимые настройки.

Например для запуска сервера MySQL указывается версия БД, root password и хост на котором запустить базу. Для сервера PHP указывается папка с проектом и хост где будет запущено приложение.

YAML файл генерируется автоматически. При сборке докер контейнера создается xml template с инструкциями как запускать это приложения. Поэтому создавать yaml файл не нужно. Он создается автоматически на основе xml шаблона и тех настройек что указал пользователь.

<center>
	<img src="ru/images/konczepcziya-oblachnoj-os-modifikatory-i-shablony.drawio.png"></img>
</center>


## Шаблон приложения

```
<?xml version="1.0" encoding="UTF-8" ?>
<template>
	<uid>org.bayrell.blank</uid>
	<name>Blank Template</name>
	<version>1.0</version>
    <type>default</type>
    <branch>main</branch>
    <arch>amd64</arch>
    <arch>arm64v8</arch>
	<maintainer>Ildar &lt;ildar@bayrell.org&gt;</maintainer>
	<marketplace>https://cloud_os.bayrell.org/</marketplace>
    <link name="Source code">https://github.com/bayrell-os/marketplace</link>
	<link name="Marketplace">https://cloud.bayrell.org/ru/marketplace/app/org.bayrell.blank</link>
	<xml name="bayrell.org" priority="20">https://cloud.bayrell.org/marketplace/org.bayrell.blank.xml</xml>
	<xml name="github.com" priority="10">https://raw.githubusercontent.com/bayrell-os/marketplace/main/org.bayrell.blank.xml</xml>
	<date>2022-05-14T18:37:00+06:00</date>
	<changelog>First template</changelog>
	<yaml>
		<services>
			<_var_app_name_>
				<image>bayrell/example:1.0</image>
				<environment>
				</environment>
			</_var_app_name_>
		</services>
		<volumes>
		</volumes>
	</yaml>
	<variables>
	</variables>
	<modificators>
		<li>org.bayrell.modificator.cloud_os</li>
		<li>org.bayrell.modificator.deploy_hostname</li>
	</modificators>
	<patch>
		<name>Template patch</name>
		<operations>
		</operations>
	</patch>
</template>
```

- uid - уникальный идентификатор шаблона
- name - название шаблона
- version - версия шаблона приложения
- maintainer - кто обслуживает данные шаблон
- type - тип шаблона. Возможны следующие типы:
  - default - тип по умолчанию
  - admin - шаблон с админ панелью. Для <type>admin</type> должен использоваться 81 порт.
  - vspace - шаблон для запуска в виртуальных пространствах
  - modificator - модификатор
- branch - ветка шаблона. Примеры: main, dev, test, version_1.0, и т.п.
- arch - возможные архитектуры
- marketplace - ссылка на маркетплей, откуда был скачан шаблон
- link - дополнительные ссылки
- xml - ссылка на xml шаблон для обновления и поиска новых версий. Атрибут priority означает приоритет шаблона. Сначала будут скачиваться шаблоны с высоким приоритетом (Чем больше число, тем выше приоритет). Затем, если шаблон, с высоким приоритетом недоступен, то скачиваться с низким.
- changelog - список изменений в данной версии
- date - дата выпуска xml шаблона
- yaml - содержимое yaml файла
- variables - Список переменных шаблона
- modificators - модификаторы по умолчанию, которые будут добавлены при создания приложения
- patch - патч шаблона


## Модификаторы приложений

Модификаторы предназначены для модификации основного шаблона.

Пример, данный модификатор добавляет dns сервер в шаблон.

```
<?xml version="1.1" encoding="UTF-8" ?>
<modificator>
	<uid>org.bayrell.modificator.dns.172.30.0.1</uid>
	<name>DNS 172.30.0.1</name>
	<version>1.0</version>
	<maintainer>Ildar &lt;ildar@bayrell.org&gt;</maintainer>
	<marketplace>https://cloud_os.bayrell.org/</marketplace>
	<xml name="bayrell.org" priority="20">https://cloud.bayrell.org/marketplace/org.bayrell.modificator.dns.172.30.0.1.xml</xml>
	<date>2022-10-20T18:37:00+06:00</date>
	<changelog>First template</changelog>
	<priority>-1000</priority>
	<operations>
		<operation type="replace">
			<path>/template/yaml/services/*/dns</path>
			<value>
				<dns>172.30.0.1</dns>
			</value>
		</operation>
	</operations>
</modificator>
```

В разделе operations указываются список модификаций шаблона. Основная идея: на основе xpath делать патч шаблона.

priority - Приоритет операций. Патчи с меньшим числом будут выполнены первыми.


## Примеры патчей


### Добавление ноды

Данный патч добавляет hostname во все ветки по адресу /template/yaml/services/*. При этом, перед добавлением, проверяет существует ли элемент или нет.

```
<operation type="add">
	<path>/template/yaml/services/*</path>
	<notExists>/template/yaml/services/*/hostname</notExists>
	<value>
		<hostname>{{.Service.Name}}.{{.Task.ID}}.local</hostname>
	</value>
</operation>
```


### Удаление ноды

Удаляет все вхождения по адресу /template/yaml/services/*/deploy/placement

```
<operation type="remove">
	<path>/template/yaml/services/*/deploy/placement</path>
</operation>
```


### Изменение ноды

Поменять значение по адресу /template/yaml/services/*/dns

```
<operation type="replace">
	<path>/template/yaml/services/*/dns</path>
	<value>
		<dns>172.30.0.1</dns>
	</value>
</operation>
```


### Добавление атрибута

```
<operation type="addAttribute" priority="1000">
	<path>/template/yaml/services/*/volumes</path>
	<name>type</name>
	<value>array</value>
</operation>
```

### Изменение и удаление атрибута

Еще не реализовано


## Формирование Yaml файла

Yaml формируется из xml шаблона после выполнения всех модификаторов. Содержимое /template/yaml превращается в yaml файл. При этом все переменные будут заменены соотвествующими значениями.


## Типы данных

### type="array"

Тип массив. xml будет превращен в массив.

```
<yaml>
	<services>
		<_var_app_name_>
			<volumes type="array">_var_app_name_:/data</volumes>
			<volumes type="array">/var/run/docker.sock:/var/run/docker.sock:ro</volumes>
		<_var_app_name_>
	</services>
</yaml>
```

В данном случае все значения _var_app_name_ будут заменены на code_server.

_var_app_name_ это системная переменная означает название приложение. Оно меняется при создании или редактировании приложения.

YAML:

```
services:
  code_server:
    volumes:
	  - 'code_server:/data'
	  - '/var/run/docker.sock:/var/run/docker.sock:ro'
```


### type="int"

```
<deploy>
	<replicas type="int">1</replicas>
</deploy>
```

Говорит, что значение replicas должно быть конвертировано в число.

```
deploy:
  replicas: 1
```


### type="boolean"

```
<cloud_network>
	<external type="boolean">true</external>
</cloud_network>
```

Говорит, что значение replicas должно быть конвертировано в логическую переменную.

```
cloud_network:
	external: true
```

### type="map"

```
<volumes type="map">
	<_var_app_name_ type="map" />
</volumes>
```

Определяет что содержимое является объектом

```
volumes:
	code_server: {  }
```
