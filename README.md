#QuickShot
QuickShot is a simple python program that allows you to easily take screenshots(partial and full screen).  
The program was designed for *nix systems and depends on wxPython and xrectsel.

##Installation
Make sure you have all dependencies(use the package manage for your distribution)

    $ sudo pip install wxpython
Build and install xrectsel from https://github.com/lolilolicon/FFcast2/blob/master/xrectsel.c


Elevate

    $ sudo su
Clone repository  

    # cd /opt
    # git clone https://github.com/opsr/quickshot.git
Edit config file "path" and "prefix" to reflex your preferences.

    # vim quickshot/config
Set quickshot ownership to your user

    # chown -R user:user quickshot/
Create a link for quickshot

    # ln -s /opt/quickshot/quickshot.py /usr/bin/quickshot
Enjoy

    # exit
    $ quickshot