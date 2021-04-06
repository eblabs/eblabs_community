# Welcome to Group Move Tool

<img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/GroupMoveTool/data/eblabs_groupMoveTool.png" alt="image" width="64px" />

**Easily transform many objects at once, as a group.**
> <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/GroupMoveTool/data/eblabs_groupMoveToolCompare.gif" alt="image" width="600"/>

# Key Features
> * Translate and rotate your selected objects.
> * Works with complex heirarchies. 
> * Relocate pivots on the fly.

# How to install?
Use the Package Manager for quickly installing and updating tools, get it here:

[Package Manager Getting Started](https://eblabs.com/package-manager-quick-install-beta/)


# Quick Start Guide
| # | Area | Description | 
| --- | --- |--- |
| **1** | Select | Select all the controls or objects you'd like to manipulate. |
| **2** | Click | Activate the **Group Move Tool** by clicking on the button. |
| **3** | Move/Rotate/Scale | Move your objects, when you release the objects will update their positions.  |
| **4** | Finish | Deselect the Group Move node to exit the tool. |

# Tips and Tricks

## Change the Pivots
* Hit the *Insert* key when the tool is active to move the pivot point.

## Try scale!
* Using scale will move objects closer or farther apart. 

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
package_id = 'GroupMoveTool'

import os
import sys
if not install_path in sys.path:
    sys.path.insert(0, install_path)

import eblabs_hub.GroupMoveTool.scripts.GroupMoveTool as tool
tool.GroupMove()
```


