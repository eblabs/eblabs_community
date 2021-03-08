
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

> Select all your controls (don't forget hidden IK or FK controls, etc)
> <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/Reflektor/data/UI_Register.png" alt="image" width="300" />
> Click the "Register" button (check below if you run into any issues)

## ...mirror my selection

> <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/Reflektor/data/UI_Mirror.png" alt="image" width="300" />
> Select your controls and click "Mirror"
> Your pose will be mirror to the other side.
> To mirror swap both sides, make sure to select both sides before clicking (check next tip).

## ...select both sides

> <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/Reflektor/data/UI_Select.png" alt="image" width="300" />
> Click "Select" to select the opposite side.
> To add the opposite side to your selection, use SHIFT + Click on the button.

## ...mirror pose using an arbitrary mirror plane

> <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/Reflektor/data/UI_SetMirrorPlane.png" alt="image" width="300" />
> First select the object that you would like to use as a mirror plane and click "Set Mirror Plane Reference". (currently mirroring will be done over the X axis)
> <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/Reflektor/data/UI_MirrorViaMirrorPlane.png" alt="image" width="300" />
> Next simply click "Mirror Via Reference Plane". (It's not reccomended to use this for ALL controls at once, its best used on as few controls as possible.)

# Examples and Tips

## How to troubleshoot registration problems
* Here's how

# UI Manual

## Main Areas
(breakdown image of main areas)

| # | Area | Description | 
| --- | --- |--- |
| **1** | Main Area | Here you can find various menus and options. |
| **2** | Area 1 | Do this kind of stuff from here. |
| **3** | Area 2 | Do this kind of stuff from here.  |
| **4** | Area 3 | Do this kind of stuff from here. |

### Main Area
(screen grab of area)

| Item | Description | 
| --- | --- |
| Function | If you click it, it does this  | 


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
package_id = 'RetimeTools'

import os
import sys
if not install_path in sys.path:
    sys.path.append(install_path)

import eblabs_hub.RetimeTools.scripts.RetimeTools as tool
reload(tool)
w = tool.Window()
w.display()
```

