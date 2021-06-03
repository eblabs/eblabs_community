# Package Manager
The package manager is a system for installing and managing all of your eblabs.com animation tools. 


<img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/PackageManager/eblabsPackageManager_UI.png" alt="image" width="50%"/>

# Getting Started

## Online Installation
|Steps||
|---|---|
|1. Download the drag/drop installer.|<ul><li>Be sure to right click and "Save Link/Target As"</li><li>[eblabs_drag_drop_install.py](https://raw.githubusercontent.com/eblabs/eblabs_community/master/Installer/eblabs_drag_drop_install.py)</li></ul>|
|2. Simply drag and drop the installer into Maya|<img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/PackageManager/eblabsPackageManager_installer.gif" alt="image"/>|
|3. High five! | <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/PackageManager/eblabsPackageManager_installer_success.png" alt="image"/> |

## Offline Installation
|Steps||
|---|---|
|3. If an Online Install isn't possible, you will see a slightly different popup. |<img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/PackageManager/eblabsPackageManager_installer_offline.png" alt="image"/>|
|4. Fear not, the actual installation files can be downloaded manually. Save the latest package to your computer from here.|[Get Latest Package Manager Version Here](https://github.com/eblabs/eblabs_community/raw/master/Installer/versions/eblabs_PackageManager_0.6.4.h.eblabs)<br/><br/>Be sure to right click and "Save Link/Target As".|
|5. From the popup click "Install" and locate the package that you just downloaded.|<img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/PackageManager/data/PackageManager_Docs_InstallButton.jpg" alt="image"/>|
|6. After these additional steps, High Five! | <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/PackageManager/eblabsPackageManager_installer_success.png" alt="image"/> |

# Package Manager Quick Start

## Shelf Button

The Package Manager can be found on the eblabs shelf.<br/>
![](https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/PackageManager/eblabsPackageManager_Shelf.png)

## Add New Tool
Once you have the Package Manager up and running, installing and updating new tools is quick and easy.
|Steps||
|---|---|
|1. Be sure to download the packages for tools you've purchased from your account.|[https://eblabs.com/my-account/downloads/](https://eblabs.com/my-account/downloads/) |
|2. Click on "Add Package" and locate the package you'd like to install.|<img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/PackageManager/eblabsPackageManager_addPackage.gif" alt="image"/> |

# Troubleshooting

## Pre-Maya 2017u5 Installation
We are working to improve the install process for older versions of Maya. Here is a work around to help when the drag and drop installer isn't recognized.

| Steps | |
| --- | --- |
|We can actually run the installation process manually from the script editor.<br/><br/>Copy/Paste the contents of the installer into a Python tab of the script editor.|[eblabs_drag_drop_install.py](https://raw.githubusercontent.com/eblabs/eblabs_community/master/Installer/eblabs_drag_drop_install.py)|
| ```onMayaDroppedPythonFile()``` <br/><br/> Add one additional line at the end. Make sure there aren't any tabs or spaces in front of this. | <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/PackageManager/data/Troubleshooting_pre2017Fix.jpg" alt="image"/> |
|Click Run|<img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/PackageManager/data/Troubleshooting_pre2017Fix_RunSmall.jpg" alt="image"/>|
|Voila|<img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/PackageManager/eblabsPackageManager_installer_success.png" alt="image"/><br/>This will launch the installer. <br/><br/>Note for Macs, from here you will need to follow the "Offline Install" method. </br>|
