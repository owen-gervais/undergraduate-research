## Formatting microSD card:

After plugging in your microSD card, type the below bash command to see the list of disks on your machine
```bash
diskutil list
```

In my case, the removable storage is on **/dev/disk2/**. Using the removable storage as your path, 
```bash
sudo diskutil eraseDisk FAT32 MYSD MBRFormat /dev/disk2
```


**Follow these steps to set up Ubuntu Server on "Tufts_Wireless"**
1. Connect to an Ethernet jack on Tufts Wifi (Snag one off a computer in Eaton Lab is the best place)  
2. Flash Ubuntu Server (64 Bit) from Raspberry Pi Imager to the formatted microSD
3. Connect keyboard and HDMI to the Pi.
4. Turn on the Pi, wait for the Pi to post and wait for the SSH keys to appear on the screen. Disregard if you are asked to put in the login and password, there is a bug that doesn't allow the user to put in the informatino until the SSH keys have been generated.
5. Login into the Pi, the username is **ubuntu** and the password is **ubuntu**
5. **Do not touch anything else after this!** When the Pi is installing and booting Ubuntu Server there are background updates that have to complete before you can do anything. Wait at least 15-20 mins depending on your internet speeds. 
6. After the updates have completed, you will need to switch the **renderer** for your Ubuntu install. Ubuntu desktop uses a renderer called **NetworkManager** which is vastly better than the stock **netplan** that comes with Ubuntu Server 20.04
7. First enter the below line into the terminal,
```bash
sudo apt-get install network-manager
```
to install **Network-Manager** on your machine
8. Now switch to the **netplan** folder on your machine by
```bash
cd /etc/netplan
```
You will see a file ending **.yaml**, edit this file using sudoedit.
```bash
sudoedit *.yaml
```
You will need to add one line to file under version:2, and it should follow the form
```bash
network:
  version: 2
  renderer: NetworkManager
```
Write out your changes to the file and exit. 
9. Last step is to connect everything together so you will need to issue these commands in order
```bash
sudo netplan --debug generate
```
```bash
sudo netplan apply
```
```bash
reboot
```
10. After issuing the last command and rebooting your system you should be able to type 
```bash
nmtui
``` 
into the terminal to bring up a graphical wifi selection screen. Select Tufts_Wireless and you should be all set to go!
