# Templates and Modifiers

Application deployment in BAYRELL Cloud OS is done through the web interface. The main idea is that users don’t need to create YAML files.

When launching an application, the user specifies which application needs to be run and its required settings.

For example, to launch a MySQL server, the database version, root password, and host on which to run the database are specified. For a PHP server, the project folder and the host where the application will be launched are specified.

The YAML file is generated automatically. During docker container assembly, an XML template is created with instructions on how to launch this application. Therefore, there’s no need to create a YAML file. It is automatically created based on the XML template and the settings provided by the user.

![Templates and modifiers](https://blog.bayrell.org/wp-content/uploads/2022/10/konczepcziya-oblachnoj-os-modifikatory-i-shablony.drawio.png?_=1666251653000)


## Application Template

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

- uid - unique template identifier
- name - template name
- version - application template version
- maintainer - who maintains this template
- type - template type. Possible types:
  - default - default type
  - admin - template with admin panel. For <type>admin</type>, port 81 must be used.
  - vspace - template for running in virtual spaces
  - modificator - modifier
- branch - template branch. Examples: main, dev, test, version_1.0, etc.
- arch - supported architectures
- marketplace - link to the marketplace from which the template was downloaded
- link - additional links
- xml - link to the XML template for updates and searching new versions. The priority attribute indicates the template priority. First, templates with high priority will be downloaded (the higher the number, the higher the priority). Then, if the high-priority template is unavailable, it will be downloaded with low priority.
- changelog - list of changes in this version
- date - date of XML template release
- yaml - YAML file contents
- variables - List of template variables
- modificators - default modifiers that will be added when creating an application
- patch - template patch


## Application Modifiers

Modifiers are designed to modify the main template.

Example: This modifier adds a DNS server to the template.

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

In the operations section, a list of template modifications is specified. Main idea: patch template using XPath.

priority - Operation priority. Patches with lower numbers will be executed first.


## Patch Examples


### Node Addition

This patch adds hostname to all branches at path /template/yaml/services/*. Moreover, before addition, it checks whether the element exists or not.

```
<operation type="add">
	<path>/template/yaml/services/*</path>
	<notExists>/template/yaml/services/*/hostname</notExists>
	<value>
		<hostname>{{.Service.Name}}.{{.Task.ID}}.local</hostname>
	</value>
</operation>
```


### Node Removal

Deletes all matches at path /template/yaml/services/*/deploy/placement

```
<operation type="remove">
	<path>/template/yaml/services/*/deploy/placement</path>
</operation>
```


### Node Modification

Change the value at path /template/yaml/services/*/dns

```
<operation type="replace">
	<path>/template/yaml/services/*/dns</path>
	<value>
		<dns>172.30.0.1</dns>
	</value>
</operation>
```


### Attribute Addition

```
<operation type="addAttribute" priority="1000">
	<path>/template/yaml/services/*/volumes</path>
	<name>type</name>
	<value>array</value>
</operation>
```

### Attribute Modification and Deletion

Not yet implemented


## YAML File Generation

YAML is generated from the XML template after executing all modifiers. Contents of /template/yaml turn into YAML file. At the same time, all variables will be replaced with corresponding values.


## Data Types

### type="array"

Array type. XML will be transformed into an array.

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

In this case, all values of var_app_name will be replaced with code_server.

var_app_name is a system variable meaning the application name. It changes during creating or editing an application.

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

It says that the replicas value should be converted to a number.

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

It says that the value should be converted to a logical variable.

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

Defines that the content is an object

```
volumes:
	code_server: {  }
```
