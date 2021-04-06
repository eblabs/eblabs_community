# Welcome to whisKEY Pro

<img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/whisKEY/data/whiskey_icon.png" alt="image" width="64px" />

**The WhisKEY Pro Toolkit is an Animator’s swiss army knife of animation tools.**

# Key Features
* Realtime in-between sliders.
* Fully customizable UI.
* Many widgets to choose from.
* Lots of workflow and cleanup tools.

<img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/whisKEY/data/WhisKEYPro.jpg" alt="image" />


# How to install?
Use the Package Manager for quickly installing and updating tools, get it here:

[Package Manager Getting Started](https://eblabs.com/package-manager-quick-install-beta/)


# Customize your widgets
The whisKEY toolset is designed to work around you. You can pick and choose your own widgets.

Here are the main widgets
| # | Widget | Description | 
| --- | --- |--- |
| <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/whisKEY/data/Widget_Classic.jpg" alt="image" /> | Classic | A collection of basic animation tools. |
| <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/whisKEY/data/Widget_Inbetween.jpg" alt="image" /> | Inbetween | Basic inbetweening tools. |
| <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/whisKEY/data/Widget_WorldSpace.jpg" alt="image" /> | World Space | An inbetween tool to blend previous and next world space positions.  |
| <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/whisKEY/data/Widget_Extras.jpg" alt="image" /> | Extras | Multiply, PosePusher and In/Out tool. |
| <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/whisKEY/data/Widget_SnapShot.jpg" alt="image" /> | Snapshot | For capturing a pose and applying it at another time or another set of similarly named controls. |
| <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/whisKEY/data/Widget_Tools.jpg" alt="image" /> | Tools | Misc tools for rekeying, cleaning subframe keys or boring keys and baking. |
| <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/whisKEY/data/Widget_Options.jpg" alt="image" /> | Options | For setting the tangent types for your selection. Also sets the default type for new keys. |
| <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/whisKEY/data/Widget_Principles.jpg" alt="image" /> | Animation Principles | Brush up on the basics here. |

## ...do something

> Here's how


# Examples and Tips

## Do this cool thing
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
install_path = 'E:/path/to/maya/scripts'
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


