# cse594 Project: Maya plugin
## written by Seth Lemanek and Chris Bedoya

**October 22, 2017**
This project contains a maya plugin that creates creates a "hello world" command and creates a menu that links to a .py file that makes a GUI interface to execute the command.

### How to run this plugin
Open project with Visual Studio and click "Build Solution".
Open Maya then with "loadPlugin" command or pluin manager, open the directory (x64/Debug) that contains the .py file

**October 25, 2017**
Plugin redone to be an entirely Python plugin.  Nothing complicated.  It adds a hello and hellogui command and makes a menu for them.  hello just outputs "hello world" and hellogui creates a gui to run hello command.