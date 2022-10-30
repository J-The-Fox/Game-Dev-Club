# Game-Dev-Club
Game Develpment Club!

> Roses Are Red,
> Violets Are Blue,
> Unexpected '{' 
> On Line 32

## Projects
Make Sure To Add Your Project Under The 'projects' Folder And Title The Folder With Your Project Name + Creator + Any Contributers Sepperated By Dashes
Like This (Can Use GitHub Account Or Not): NewProject-J-The-Fox

You Can Also Use A `README.md` File In Your Project As Well To Add Extra Info

## Game Engines
Popular Game Engines To Use Are

- Unity
- Unreal Engine
- Godot

### Installation

## Map Making

Most Game Engines Support Their Own Map Making Tools In The Engine Themselves, However If You Would Like To Use External Tools, You Can Use Blender, or Twinmotion. To Help Make 3D Maps

### Texturing

Texturing Can Be Done Inside Most, If Not All Game Engines, However You Can Create Texures On Any Art App You Choose And Import Them Into Your Project A Great App Is Krita. It's Open Source And Availiable For All Platforms, However Use The App You Prefer

## Libraries And Frameworks

A List Of Popular Frameworks And Libraries:
- OpenGL
- SDL2
- DirectX
- .NET
- Mono Framework

### Installation Of Libraries And Frameworks

SDL2 Installation: 

> To Install SDL2, Go To https://github.com/libsdl-org/SDL/releases/tag/release-2.24.1 And Download The Correct Format For Your System.

On MacOSX Systems:
- Install The SDL Framework By Adding It The /Library/Frameworks Folder. If You Don't Have The Permissions, You Can Instead Install It To /Users/Your_User/Library/Frameworks Folder. If The Folder Does Not Exist, Add It And Then Move The SDL2 Folder There

You Can Alternatively Install It Via Homebrew If You Have It Installed By Using The Commands
```sh
brew install SDL2
brew install SDL2_image
brew install SDL2_ttf
```

On Windows Systems:

On Linux / Unix Systems:
For Debian With APT
```sh
sudo apt update
sudo apt upgrade
sudo apt install sdl2
```

For Arch With Pacman
```sh
sudo pacman -Syu
sudo pacman -S dotnet-runtime dotnet-sdk
```
More Information Can Be Found Here: 

For Fedora With DNF
```sh
sudo dnf install sdl2
```

OpenGL Installation:
For OpenGL, Make Sure Your Grapchics Card Supports OpenGL, It Should Come Preinstalled With The Driver For Your Graphics Card. The Webiste Is https://www.opengl.org/.

DirectX Installation:

.NET Installation:

On MacOSX Systems:
- Go To The [.NET Website](https://dotnet.microsoft.com/en-us/download) And Download The Selected Version
- Run The Package To Install It

On Windows Systems:
- Go To The [.NET Website](https://dotnet.microsoft.com/en-us/download) And Download The Selected Version
- Run The Installer To Install It

On Linux / Unix Systems:
Depending On Your Linux Distro And Pakage Manager
For Debian With APT
```sh
sudo apt update
sudo apt upgrade
sudo apt install dotnetVersion
```
(Replace The 'Version' With The Version Wanted. So For .NET6 It Would Be dotnet6)

For Arch With Pacman
```sh
sudo pacman -Syu
sudo pacman -S dotnet-runtime dotnet-sdk
```
More Information Can Be Found [Here](https://wiki.archlinux.org/title/.NET)

For Fedora With DNF
```sh
sudo dnf install dotnet
```

Mono Installation:

On MacOSX Systems:

On Windows Systems:

On Linux / Unix Systems:
Depending On Your Linux Distro And Pakage Manager
For Debian With APT
```sh
sudo apt updates
sudo apt upgrade
sudo apt install dirmngr gnupg apt-transport-https ca-certificates
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
sudo sh -c 'echo "deb https://download.mono-project.com/repo/ubuntu stable-bionic main" > /etc/apt/sources.list.d/mono-official-stable list'
sudo apt update
sudo apt install mono-complete
```

For Arch With Pacman
```sh
sudo pacman -Syu
sudo pacman -S mono
sudo pacman -S mono-complete
```

For Fedora With DNF
```sh
sudo dnf install mono-devel
```
