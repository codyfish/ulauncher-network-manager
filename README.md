# ulauncher-network-manager

A simple ulauncher plugin controlling NetworkManager and tlp-rdw (A utility disabling and enabling radio devices on laptops)


## Installation
This extension is only available for Python 3 ulauncher (ulauncher 5/Api 2) 

Install this extension using ulaunchers extension menu.
Install the dependencies using pip (python 3) or your systems package manager

### Dependencies

* python-networkmanager

##Usage

| command |  | action |
|---------|----------|--------|
| `nm nme` | | enable devices controlled by NetworkManager |
| `nm nmd` | | disable devices controlled by NetworkManager |
| `nm rdwe` | | enable networking hardware using tlp-rdw |
| `nm rdwd` | | disable networking hardware using tlp-rdw |
| `nm <id>` | | enable connection <id> |

##Icons

Icons from https://github.com/horst3180/arc-icon-theme

##Disclaimer

This is an extension I made for myself, at the moment it still might be very buggy or not work in the expected way.

