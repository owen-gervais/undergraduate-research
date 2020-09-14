
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


