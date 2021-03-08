
# Welcome to Reflektor Beta

<img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/Reflektor/data/eblabs_reflektor.png" alt="image" width="64px" />

A simple yet versitile tool for mirroring poses and selections.

# Key Features
* Auto registration your character
* Mirror Poses along local axis or an arbitrary mirror plane
* Mirror Selections as well

<img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/Reflektor/data/UI_Main.jpg" alt="image" width="300" />

# How to install?
Use the Package Manager for quickly installing and updating tools, get it here:

[Package Manager Getting Started](https://eblabs.com/package-manager-quick-install-beta/)


# I want to...
## ...start using the tool with my character

> First you will need to Register your character under the "Setup Character" tab.  
> Select all your controls (don't forget hidden IK or FK controls, etc)  
> <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/Reflektor/data/UI_Register.png" alt="image" width="300" />  
> Click the "Register" button (check below if you run into any issues)  

## ...mirror my selection

> Select your controls and click "Mirror"
> <div style="clear:both;"><img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/Reflektor/data/UI_Mirror.png" alt="image" width="300"> </div>
> > Your pose will be mirror to the other side.
> To mirror swap both sides, make sure to select both sides before clicking (check next tip).

## ...select both sides

> Click "Select" to select the opposite side.  
> <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/Reflektor/data/UI_Select.png" alt="image" width="300" />  
> To add the opposite side to your selection, use SHIFT + Click on the button.  

## ...mirror pose using an arbitrary mirror plane

> First select the object that you would like to use as a mirror plane and click "Set Mirror Plane Reference". (currently mirroring will be done over the X axis)  
> <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/Reflektor/data/UI_SetMirrorPlane.png" alt="image" width="300" />  
> Next simply click "Mirror Via Reference Plane". (It's not reccomended to use this for ALL controls at once, its best used on as few controls as possible.)  
> <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/Reflektor/data/UI_MirrorViaMirrorPlane.png" alt="image" width="300" />  

# Examples and Tips

## How to troubleshoot registration problems
* For the most part you can just make your selection and click "Register".
* If you do run into problems, you can go through the steps manually in the "Character Setup" tab. More details about this below.
<img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/Reflektor/data/HowTo_RegisterCharacterManually.gif" alt="image" width="600" />  

# UI Manual

## Main Areas
<img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/Reflektor/data/UI_Overview.gif" alt="image" width="300" />  

| # | Area | Description | 
| --- | --- |--- |
| **1** | Tools Menu | Here you can find additional tools and info. |
| **2** | Main Tab | All of the main tools. |
| **3** | Character Setup | You can registere a new charater here.  |
| **4** | Edit Controls | For modifying the mirroring data if needed. |

### Tools
| Item | Description | 
| --- | --- |
| Manually Register Left Right Pair | If your rig has some naming inconsistencies, you can use this to force register a Left/Right pair. Just select a left and right control, and click this to register a pair even if their naming isn't correct.  | 

### Main
| Item | Description | 
| --- | --- |
| Mirror | Click here to mirror your selected controls to the other side. FYI, selecting both left and right before clicking this will "mirror swap" both sides. | 
| Select | Click to select the other side. Shift + Click to add the other side to your selection. | 
| Set Mirror Plane Reference | It's also possible to mirror your pose based on a mirror plane that you can define. Select your object and click to register this Mirror Plane. Keep in mind that the X axis will be used for mirroring. | 
| Mirror via Reference Plane | With your controls selected, click here to mirror your pose using the Mirror Plane that you created. | 

### Setup Character
| Item | Description | 
| --- | --- |
| Add Controls | Add controls to the list of objects to be registered. | 
| Clear | Resets the list of objects to be registered. | 
| Character ID | This will show you what the data will be saved as. | 
| Keywords | The tool will attempt to find out the best Left and Right keywords. You can click on these to change the keywords if you like. <br />Using an "^" at the start tells the tool that the keyword is at the start of the name. "$" can be used to tell the tool that the name ends with the keyword. <br/>For example "^L_" means that the name starts with "L_". | 
| Mirror Axis | Currently only local X mirroring is supported. | 
| Control List | Here you can check to see if the pairing went correctly. You can see by the "C" Center, "L" Left and "R" Right, that the controls are grouped properly. | 

### Edit Controls

| Item | Description | 
| --- | --- |
| Editor | Coming soon, from here you will be able to modify the mirroring data and make any adjustments. | 


# Manual Installation (Advanced Users Only)

The Package Manager makes installing a simple process, [Package Manager Getting Started](https://eblabs.com/package-manager-quick-install-beta/)
Although, if you still need to do this manually here's how. 

Tools should be installed to a common `eblabs_hub` folder. The `install path` should be one folder up from the `eblabs_hub` folder. Make sure that there are blank `__init__.py` files within all folders.

## Folder Structure
```
.
├── eblabs_hub
└── __init__.py
    └── package_id
        ├── __init__.py
        └── unzip package contents here
```

## Manual Command
```python
install_path = 'E:/path/to/tools/folder/'
package_id = 'Reflektor'

import os
import sys
if not install_path in sys.path:
    sys.path.append(install_path)

import eblabs_hub.Reflektor.scripts.MainModule as tool
reload(tool)

tool.MainWindow.launch()
```

