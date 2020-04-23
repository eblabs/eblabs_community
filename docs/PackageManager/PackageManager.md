# Package Manager
The package manager is a system for installing and managing all of your eblabs.com animation tools. 

## Getting Started

### Online Installation
|Online Installation|Info|
|---|---|
|1. Download the drag/drop installer.|[eblabs_drag_drop_install.py](https://raw.githubusercontent.com/eblabs/eblabs_community/master/Installer/eblabs_drag_drop_install.py)<br/><br/>Be sure to right click and "Save Link As".|
|2. Simply drag and drop the installer into Maya|<img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/PackageManager/eblabsPackageManager_installer.gif" alt="image"/>|
|3. High five! | <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/PackageManager/eblabsPackageManager_installer_success.png" alt="image"/> |

### Offline Installation
|Offline Installation|Info|
|---|---|
|3. In the case of Offline Installs, you will see a slightly different popup. |<img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/PackageManager/eblabsPackageManager_installer_offline.png" alt="image"/>|
|4. But fear not, the actual instalation files can be downloaded manually. Save the latest package to your computer.|[latest Package Manager version](https://github.com/eblabs/eblabs_community/raw/master/Installer/versions/eblabs_PackageManager_0.5.6_compiled.zip)|
|5. From the popup click "Install" and select the latest package that you saved to your local computer in step #4.||
|6. A few more steps and High five! | <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/PackageManager/eblabsPackageManager_installer_success.png" alt="image"/> |

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
|Copy/Paste the contents of the installer into a Python tab of the script editor.|[eblabs_drag_drop_install.py](https://raw.githubusercontent.com/eblabs/eblabs_community/master/Installer/eblabs_drag_drop_install.py)|
| ```onMayaDroppedPythonFile()``` <br/><br/> Add one additional line at the end. Make sure there aren't any tabs or spaces in front of this. | <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/PackageManager/data/Troubleshooting_pre2017Fix.jpg" alt="image"/> |
|Click Run|<img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/PackageManager/data/Troubleshooting_pre2017Fix_RunSmall.jpg" alt="image"/>|
|Voila|<img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/PackageManager/eblabsPackageManager_installer_success.png" alt="image"/><br/>This will launch the installer. <br/><br/>Note for Macs, from here you will need to follow the "Offline Install" method. </br>|
