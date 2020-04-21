# Welcome to Screen Space Tools

<img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/ScreenSpaceTools/data/eblabs_screenSpace.png" alt="image" width="32px" />

**Advanced animation tools for manipulating animation relative to screen space, including the ability to switch spaces to/from local space and screen space for almost any control.**

# Key Features
* Quickly edit your animation in screen space.
* Animation becomes relative to the camera, horizontal, vertical and depth-(distance to camera) curves.
* Great for animating flying objects, or finding depth bumps in object tracks.
* Animator friendly, have the choice to use only your existing keyframes.
* Matchmove friendly, have the choice to bake all keys.
* Can be used in many more creative ways.

<img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/ScreenSpaceTools/data/screenSpace_mainUI1.jpg" alt="image"/>

# How to install?
Use the Package Manager for quickly installing and updating tools, get it here:

[Package Manager Getting Started](https://eblabs.com/package-manager-quick-install-beta/)

# Examples and Tips

## How does it work?
| Scene | GIF | 
| --- | --- |
| Here is a simple scene where a space ship is flying past a moving camera. | <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/ScreenSpaceTools/data/ScreenSpace_Camera.gif" alt="image"/> | 
| Here you can see how the animation has been reconstructed in a simpler way relative to the camera. Horizontal, Vertical and Depth. | <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/ScreenSpaceTools/data/ScreenSpace_Edit2.gif" alt="image"/> | 


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
package_id = 'ScreenSpace'

import os
from maya import mel

melCommand = os.path.normpath(os.path.join(install_path, 'eblabs_hub', 'ScreenSpace', 'scripts', 'eblabs_screenSpace.mel'))
melCommand = melCommand.replace('\\','\\\\')
mel.eval('source \"{0}\"'.format(melCommand))
mel.eval('ebLabs_screenSpace;')
```


