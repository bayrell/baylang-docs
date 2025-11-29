# Installing BAYRELL Cloud OS on Desktop

This is a thin client for managing the Cloud OS.

It should be installed locally on a computer, not on a server.

## Installation on Linux

1) Install Python 3.6

2) Install Cloud OS

```
pip3 install --upgrade cloud-os-desktop
```

3) Run Cloud OS from the console with the command

```
cloud_os_desktop
```

If an error occurs when starting

```
undefined symbol:_ZNSt12out_of_rangeC1EPKc, version Qt_5
```

you need to do:

```
sudo apt install python3-qtpy
```

## Installation on Windows

1) Download Python 3.10 from the website https://www.python.org/downloads/

2) Run the installer. Click on the Customize installation button

![screenshot_20221016_182140](https://blog.bayrell.org/wp-content/uploads/2022/10/screenshot_20221016_182140.png?_=1665924472000)

![screenshot_20221016_182205](https://blog.bayrell.org/wp-content/uploads/2022/10/screenshot_20221016_182205.png?_=1665924473000)

Check the Add environment to PATH box.

Install to the folder C:\Python310

![screenshot_20221016_182232](https://blog.bayrell.org/wp-content/uploads/2022/10/screenshot_20221016_182232.png?_=1665924472000)

3) Open the command line as administrator and run the command

```
pip install --upgrade cloud-os-desktop
```

4) Create a Shortcut named “Cloud OS” on the desktop with the following command

```
C:\Python310\pythonw.exe -c "from cloud_os_desktop.app import run; run()"
```

5) Run the shortcut