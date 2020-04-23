- [Package Manager](#package-manager)
  * [Getting Started](#getting-started)
    + [Online Installation](#online-installation)
    + [Offline Installation](#offline-installation)
  * [Package Manager Quick Start](#package-manager-quick-start)
    + [Shelf Button](#shelf-button)
    + [Add New Tool](#add-new-tool)

# Package Manager
The package manager is a system for installing and managing all of your eblabs.com animation tools. 

## Required Maya Version
The Package Manager is currently supporting Maya 2017u5 and newer. Please contact support for integration with older versions of Maya.
https://eblabs.com/contact/

## Getting Started

### Online Installation

1. Download Drag and Drop installer. 
    - [here](https://raw.githubusercontent.com/eblabs/eblabs_community/master/Installer/eblabs_drag_drop_install.py)<br/>
2. Simply Drag and Drop the file into Maya. This will run the installer, from here you can manage all of your eblabs tools. <br/>
    - ![Drag and Drop](https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/PackageManager/eblabsPackageManager_installer.gif)
3. Congrats, you've successfully installed the Package Manager. <br/> 
    - ![](https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/PackageManager/eblabsPackageManager_installer_success.png)


### Offline Installation
1. Download offline installer files here:
    - [download drag and drop installer here](https://raw.githubusercontent.com/eblabs/eblabs_community/master/Installer/eblabs_drag_drop_install.py)
    - [download Package Manager here](https://github.com/eblabs/eblabs_community/raw/master/Installer/versions/eblabs_PackageManager_0.5.6_compiled.zip)
2. Drag the installer into Maya.
3. From here a popup will appear where you can manually select the Package Manager file. <br/> ![](https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/PackageManager/eblabsPackageManager_installer_offline.png)

## Package Manager Quick Start

### Shelf Button

The Package Manager can be found on the eblabs shelf.<br/>
![](https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/PackageManager/eblabsPackageManager_Shelf.png)

### Add New Tool
![](https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/PackageManager/eblabsPackageManager_UI.png)
1. From the main UI, click "Add Package" to locate the zip package that you've downloaded from your eblabs.com MyAccount page. <br/>
    - ![](https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/PackageManager/eblabsPackageManager_addPackage.gif)
    - [https://eblabs.com/my-account/downloads/](https://eblabs.com/my-account/downloads/)    


## Troubleshooting

### Pre-Maya 2017u5 Installation
We are working to improve the install process for older versions of Maya. Here is a work around to help when the drag and drop installer isnt recognized.

| Steps | Info  |
| --- | --- |
|Copy the contents of the installer into a Python tab of the script editor.|[eblabs_drag_drop_install.py](https://raw.githubusercontent.com/eblabs/eblabs_community/master/Installer/eblabs_drag_drop_install.py)|
| ```onMayaDroppedPythonFile()``` <br/> Add one additional line at the end. Make sure there aren't any tabs or spaces in front of this. | <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/PackageManager/data/Troubleshooting_pre2017Fix.jpg" alt="image"/> |
|Click Run|<img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/PackageManager/data/Troubleshooting_pre2017Fix_RunSmall.jpg" alt="image"/>|
