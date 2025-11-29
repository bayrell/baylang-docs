# Installing BAYRELL Cloud OS on a Server

[![Installing BAYRELL Cloud OS on a Server](https://img.youtube.com/vi/TlzsL3pxKn4/0.jpg)](https://www.youtube.com/watch?v=TlzsL3pxKn4)

Instructions:

1) Install the applications

```
sudo apt-get install mc nano git
```

2) DNS Configuration

Execute
```
sudo rm /etc/resolv.conf
sudo nano /etc/resolv.conf
```

Specify the following settings

```
nameserver 127.0.0.53
options edns0 trust-ad
ndots:1
search .
```

3) Download the script

```
git clone https://github.com/bayrell-os/cloud_os
cd cloud_os
```

4) Execute

```
bash cloud_os.sh 0.5.1
```

Wait for the installation script to complete. It will also ask you to enter the administrator login, and at the end it will create and display it on the screen.

5) Add the cloud OS to autostart

Create a file via the command

```
sudo nano /etc/rc.local
```

Write the following commands in it:

```
#!/bin/bash

for i in $(seq 0 1); do
	sleep 10
	docker start cloud_os_standard
done
```

Set the execute flag for this file

```
sudo chmod +x /etc/rc.local
```

6) Add the ubuntu user to the docker group

```
sudo usermod -a -G docker ubuntu
```

7) Reboot the server

```
sudo init 6
```

8) Installation is complete!
