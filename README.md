# Game-Dev-Club
Game Development Club

## Projects
Make Sure To Add Your Project Under The 'projects' Folder And Title The Folder With Your Project Name + Creator + Any Contributers Sepperated By Dashes
Like This (Can Use GitHub Account Or Not): NewProject-J-The-Fox

You Can Also Use A README.md File In Your Project As Well To Add Extra Info

### For Python Projects:
The requirements.txt File Holds A List Of Useful Python Packages That Could be Used In General, 
You Do Not Have To Use This File. However If You Choose To Add A Python Project, It Is Helpful 
To Create A requirements.txt File If You Use Non-Built-In Packages.

To Get Packages From This File, Simply Run These Two Commands:
On Windows:
-> cd DriveLetter:/Path/To/requirements.txt
-> python3 -m pip install -r requirements.txt

On Linux / Unix / MacOS:
Externel Drives Should Have The /Volumes Added To The Start For MacOS. 
For Linux / Unix, Use /home/YourUser/DriveName Instead
-> cd /Path/To/requirements.txt 
-> python3 -m pip install -r requirements.txt

The setup.py Is Another Python File That Is Helpful To Have But Not Required.
setup.py Holds Information Such As version, aurthor, packages (Folders), description, name, Among Other Things.
You Can Run It Directly Or Run This Command:

On Windows:
-> python3 DriveLetter:/Path/To/requirements.txt

On Linux / Unix / MacOS:
Externel Drives Should Have The /Volumes Added To The Start For MacOS. 
For Linux / Unix, Use /home/YourUser/DriveName Instead
-> python3 Path/To/requirements.txt 

### For C++ / C / QT Creator Projects
Make Sure To Include A Makefile File Or CMake File Within The Root Folder Of Your Project, This Will Allow Anyone To Compile Your Project Into An Executable Program

When You Are Ready To Run The Project, (Or Clone It From GitHub), Run The Makefile / Cmake File By Running:

For Makefile
On Windows:
-> cd DriveLetter:/Path/To/Makefile.mk
-> make

On Linux / Unix / MacOS:
Externel Drives Should Have The /Volumes Added To The Start For MacOS. 
For Linux / Unix, Use /home/YourUser/DriveName Instead
-> cd /Path/To/Makefile.mk
-> make

For Cmake
On Windows:
-> cd DriveLetter:/Path/To/NameOfCmakeFile.cmake
-> cmake

On Linux / Unix / MacOS:
Externel Drives Should Have The /Volumes Added To The Start For MacOS. 
For Linux / Unix, Use /home/YourUser/DriveName Instead
-> cd /Path/To/NameOfCmakeFile.cmake
-> cmake





##  Building Files

Cmake and Makefile Are Helpful For Building And Creating An Excecutable Game

## Libraries And Frameworks

A List Of Popular Frameworks And Libraries:
OpenGL
SDL2
DirectX
.NET
Mono Framework

### Instalation Of Libraries And Frameworks

SDL2 Installation: 
To Install SDL2, Go To https://github.com/libsdl-org/SDL/releases/tag/release-2.24.1 And Download The Correct Format For Your System.

On MacOSX Systems:
Install The SDL Framework By Adding It The /Library/Frameworks Folder. If You Don't Have The Permissions, You Can Instead Install It To /Users/Your_User/Library/Frameworks Folder. If The Folder Does Not Exist, Add It And Then Move The SDL2 Folder There

You Can Alrernitlvy Install It Via Homebrew If You Have It Installed By Using The Commands
-> brew install SDL2
-> brew install SDL2_image
-> brew install SDL2_ttf

On Windows Systems:

On Linux / Unix Systems:
For Debian With APT
-> sudo apt update
-> sudo apt upgrade
-> sudo apt install sdl2
(Replace The 'Version' With The Version Wanted. So For .NET6 It Would Be dotnet6)

For Arch With Pacman
-> sudo pacman -Syu
-> sudo pacman -S dotnet-runtime dotnet-sdk
More Information Can Be Found Here: 

For Fedora With DNF
-> sudo dnf install sdl2

OpenGL Installation:
For OpenGL, Make Sure Your Grapchics Card Supports OpenGL, It Should Come Preinstalled With The Driver For Your Graphics Card. The Webiste Is https://www.opengl.org/.

DirectX Installation:

.NET Installation:

On MacOSX Systems:
Go To https://dotnet.microsoft.com/en-us/download And Download The Selected Version
Run The Package To Install It

On Windows Systems:
Go To https://dotnet.microsoft.com/en-us/download And Download The Selected Version
Run The Installer To Install It

On Linux / Unix Systems:
Depending On Your Linux Distro And Pakage Manager
For Debian With APT
-> sudo apt update
-> sudo apt upgrade
-> sudo apt install dotnetVersion
(Replace The 'Version' With The Version Wanted. So For .NET6 It Would Be dotnet6)

For Arch With Pacman
-> sudo pacman -Syu
-> sudo pacman -S dotnet-runtime dotnet-sdk
More Information Can Be Found Here: https://wiki.archlinux.org/title/.NET

For Fedora With DNF
-> sudo dnf install dotnet

Mono Installation:

On MacOSX Systems:

On Windows Systems:

On Linux / Unix Systems:
Depending On Your Linux Distro And Pakage Manager
For Debian With APT
-> sudo apt update
-> sudo apt upgrade
-> sudo apt install dirmngr gnupg apt-transport-https ca-certificates
-> sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
sudo sh -c 'echo "deb https://download.mono-project.com/repo/ubuntu stable-bionic main" > /etc/apt/sources.list.d/mono-official-stable list'
-> sudo apt update
-> sudo apt install mono-complete
(Replace The 'Version' With The Version Wanted. So For .NET6 It Would Be dotnet6)

For Arch With Pacman
-> sudo pacman -Syu
-> sudo pacman -S mono
-> sudo pacman -S mono-complete

For Fedora With DNF
-> sudo dnf install mono-devel