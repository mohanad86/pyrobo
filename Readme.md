#Starting with Python3 codes	
- Here you will find simple and complex python codes for two wheels robot 

- python codes 

![alt text](https://github.com/mohanad86/pyrobo/blob/master/images/install-python-3-mac-21894_630x210.jpg)
### Arduino
![alt text](https://github.com/mohanad86/pyrobo/blob/master/images/50450-IMG_5222.jpg)
### Arduino program
![alt text](https://github.com/mohanad86/pyrobo/blob/master/images/Screenshot%20from%202016-03-27%20217-47-29.jpg)
### Select the right board to install
![alt text](https://github.com/mohanad86/pyrobo/blob/master/images/ToolsMenu.png)

### First you need to take a look for PyRobovision wiki page 
- [To know how to install Firmata] (https://wiki.itcollege.ee/index.php/PyRobovision)

- [Get to the Firamta page to see some examples] (https://wiki.itcollege.ee/index.php/Firmata)
  
- [git clone here PyMata] (https://github.com/MrYsLab/PyMata)
### If you want to install pygame with python3 follow the instructions
- Get Pygame source code. So you need to download the last source code from the trunk, hopping it's not broken at this moment:
```
$ sudo apt-get install mercurial
$ hg clone https://bitbucket.org/pygame/pygame
$ cd pygame
```
- You also need to download the build dependency
```
$ sudo apt-get build-dep pygame
$ sudo apt-get install python3-dev
$ sudo apt-get install python3-numpy
```
- This will install dependency used by the version of pygame available on your package depot. Newer version maybe need other dependency! We also need to specify python3-dev and python3-numpy because, well, build-dep will install python2 version of this packages
```
$ python3 setup.py build
$ sudo python3 setup.py install
```
```
$ cd Pymata 
$ sudo python3 setup.py install
```
### Don't also forget to take a look for examples here
- [Firmata Examples] (https://github.com/firmata/arduino)
 
### If you are using Unbntu platform
 
- Install python withing the follow commands
- Install git into you Machine to pull and push from the server
- Install gedit to edit the file that you will put your code on it

```
$ sudo apt-get install python3
$ sudo apt-get install git
$ sudo apt-get install gedit
```
#Follow this instructions to clone to my Repo
- Clone to the my repository from terminal
``` 
$ git clone https://github.com/mohanad86/pyrobo.git
$ git pull 
- You will pull the python codes in your PC
$ ls
-To navigate to the folder 
$ cd pyrobot
- Then you are in :)
``` 


    Author: Mohanad Aly 

License
----
Licensed under the Apache License

http://www.apache.org/licenses/LICENSE-2.0
