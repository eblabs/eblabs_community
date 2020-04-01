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

<img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/WorldSpaceTools/data/WorldSpaceTools_MainUI.jpg" alt="image" width="600"/>

# How to install?
Use the Package Manager for quickly installing and updating tools, get it here:

[Package Manager Getting Started](https://eblabs.com/package-manager-quick-install-beta/)


# I want to...
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


