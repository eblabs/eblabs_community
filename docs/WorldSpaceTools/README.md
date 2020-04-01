# Welcome to World Space Tools

<img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/WorldSpaceTools/data/eblabs_worldSpaceTools.png" alt="image" width="64px" />

**Advanced animation tools for manipulating animation and switching between local, world space, and other parent spaces.**

# Key Features
* Manipulate your animation in world, local or any other parent space.
* Really useful for fixing up foot sliding with cycled animation.
* Create mini rigs on the fly with existing animation.
* Animator friendly, can full bake or only use keyframes you the animator created.
* Effecient, can batch process multiple objects simulataneously. 
* Super flexible and can be used on nearly any type of animation control or rig.

<img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/WorldSpaceTools/data/WorldSpaceTools_MainUI.jpg" alt="image"/>

# How to install?
Use the Package Manager for quickly installing and updating tools, get it here:

[Package Manager Getting Started](https://eblabs.com/package-manager-quick-install-beta/)

# UI Manual

## Main Areas
<img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/WorldSpaceTools/data/WorldSpaceTools_MainUI_Areas.jpg" alt="image"/>

| # | Area | Description | 
| --- | --- |--- |
| **1** | Menu | Here you can find various menus and options. |
| **2** | Tabs | From here you can find all of the different modules. |
| **3** | Tools Area | Tools for each module can be found here.  |
| **4** | Quick Undos | Disables the viewport during undo and redo. |

### Spaces Tools Area
(screen grab of area)

| UI | Options | 
| --- | --- |
| <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/WorldSpaceTools/data/WorldSpaceTools_MainUI.jpg" alt="image"/> | <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/WorldSpaceTools/data/WorldSpaceTools_MainUI_Options.jpg" alt="image"/>  | 

| Item | Description | 
| --- | --- |
| Function | If you click it, it does this  | 


### Main Area
(screen grab of area)

| Item | Description | 
| --- | --- |
| Function | If you click it, it does this  | 


### Main Area
(screen grab of area)

| Item | Description | 
| --- | --- |
| Function | If you click it, it does this  | 


### Main Area
(screen grab of area)

| Item | Description | 
| --- | --- |
| Function | If you click it, it does this  | 


# Manual Installation (Advanced User)

The Package Manager makes installing a simple process, but if you need to do this manually here's how.

Tools should be installed to a common `eblabs_hub` folder. The `install path` should be one folder up from the `eblabs_hub` folder. Make sure that there are blank `__init__.py` files within all folders.

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


