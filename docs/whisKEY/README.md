# Welcome to whisKEY Pro

<img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/whisKEY/data/whiskey_icon.png" alt="image" width="64px" />

**The WhisKEY Pro Toolkit is an Animator’s swiss army knife of animation tools.**

# Key Features
> * Realtime in-between sliders.
> * Fully customizable UI.
> * Many widgets to choose from.
> * Lots of workflow and cleanup tools.
> <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/whisKEY/data/WhisKEYPro.jpg" alt="image" />


# How to install?
Use the Package Manager for quickly installing and updating tools, get it here:

[Package Manager Getting Started](https://eblabs.com/package-manager-quick-install-beta/)


# Customize your widgets
The whisKEY toolset is designed to work around you, pick and choose the widgets you like. Check the right click menu to add, remove or reorder your widgets.

> <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/whisKEY/data/MainMenu.png" alt="image" />


| # | Widget | Description | 
| --- | --- |--- |
| <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/whisKEY/data/Widget_Classic.jpg" alt="image" /> | Classic | A collection of basic animation tools. |
| <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/whisKEY/data/Widget_Inbetween.jpg" alt="image" /> | Inbetween | Basic inbetweening tools. |
| <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/whisKEY/data/Widget_WorldSpace.jpg" alt="image" /> | World Space | An inbetween tool to blend previous and next world space positions.  |
| <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/whisKEY/data/Widget_Extras.jpg" alt="image" /> | Extras | Multiply, PosePusher and In/Out tool. |
| <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/whisKEY/data/Widget_SnapShot.jpg" alt="image" /> | Snapshot | For capturing a pose and applying it at another time or another set of similarly named controls. |
| <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/whisKEY/data/Widget_Tools.jpg" alt="image" /> | Tools | Misc tools for rekeying, cleaning subframe keys or boring keys and baking. |
| <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/whisKEY/data/Widget_Options.jpg" alt="image" /> | Options | For setting the tangent types for your selection. Also sets the default type for new keys. |

## Here are some ways you can customize
| | | | |
|-|-|-|-|
|<img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/whisKEY/data/Customize_A.png" alt="image" width="200"/> | <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/whisKEY/data/Customize_B.png" alt="image" width="200"/> | <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/whisKEY/data/Customize_C.png" alt="image" width="200"/> | <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/whisKEY/data/Customize_D.png" alt="image" width="200"/> |


# Tips and Tricks

## How to - Inbetween Widget
> <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/whisKEY/data/inbetween.gif" alt="image" />

## How to - Multiply Widget
> <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/whisKEY/data/multiply.gif" alt="image" />

## How to - Capture Pose Widget
> <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/whisKEY/data/capturePose.gif" alt="image" />

## How to - World Space Widget
> <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/whisKEY/data/worldSpace2.gif" alt="image" />

## How to - In/Out Widget
> * You can adjust or reset the sensitivity of this widget through the right click menu or by ctrl+sliding.
> <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/whisKEY/data/inOut.gif" alt="image" />

## Expand and collapse
> <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/whisKEY/data/expandCollapse_v001.gif" alt="image" />

## Pin and Rename
> * Click the text to rename the widget.
> * The pin button will store the selection, so the widget will work with those objects regardless of what's selected
> <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/whisKEY/data/PinAndRename.gif" alt="image" />

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
install_path = 'E:/path/to/maya/scripts'
package_id = 'Whiskey'

import os
import sys
if not install_path in sys.path:
    sys.path.insert(0, install_path)

import eblabs_hub.Whiskey.scripts.WhiskeyPro as tool

tool.window.load()
```


