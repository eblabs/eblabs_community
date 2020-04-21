# Welcome to Screen Space Tools

<img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/ScreenSpaceTools/data/eblabs_screenSpace.png" alt="image" width="32px" />

**Advanced animation tools for manipulating animation relative to screen space, including the ability to switch spaces to/from local space and screen space for any control.**

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

# How does it work?
> <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/ScreenSpaceTools/data/ScreenSpace_Camera.gif" alt="image"/>

>Here is a simple scene where a space ship is flying past a moving camera.

> <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/ScreenSpaceTools/data/ScreenSpace_Edit2.gif" alt="image"/>

>Here you can see how the animation has been reconstructed in a simpler way relative to the camera. Horizontal, Vertical and Depth.

# UI Manual

## Main Areas
<img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/ScreenSpaceTools/data/ScreenSpace_Main_Breakdown.png" alt="image"/>

| # | Area | Description | 
| --- | --- |--- |
| **A** | Tabs | Access the Screen Space Tools tab as well as a Help quick start tab. |
| **B** | Create Tools | This is where you can create a new Screen Space control. |
| **C** | Bake Tools | From here you can easily bake your animation back to your original controls.  |
| **D** | Quick Undos | Speed up your Undos and Redos with these buttons. |

### Create Tools
<img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/ScreenSpaceTools/data/ScreenSpace_UI_Create.png" alt="image"/>

| Item | Description | 
| --- | --- |
| Cameras In Scene | This list will show all the cameras in the scene. Since screen space is relative to your point of view, you’ll need to pick a camera here to make a screen space rig.  | 
| + Include Orientation  | By default, Screen Space controls are made only with translations. Check here if you want to modify rotation in screenspace as well.  | 
| Create Screen Space Rig | Clicking this button will make a screen space rig for all of your selected controls, using the highlighted camera.  | 

### Bake Tools
<img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/ScreenSpaceTools/data/ScreenSpace_UI_Bake.png" alt="image"/>

| Item | Description | 
| --- | --- |
| Screen Space Rigs | You can either select the controls in the viewport, or using this list. This is mainly for making it easier to select controls, and to bake more than one control simultaneously.  | 
| Delete | If you change your mind, you can delete a screen space control by using this button or by deleting the entire rig group from the outliner. Your animation will go back to how it was previously, without any clutter left in your scene. |
| Smart Bake | This will bake out your animation using only your existing keyframes.|
| Full Bake | This will bake out every frame. |
| Refresh Lists	 | Click to update all the lists in the screen space UI. |


# Manual Installation (Advanced Users Only)

The Package Manager makes installing a simple process, but if you need to do this manually here's how. [Package Manager Getting Started](https://eblabs.com/package-manager-quick-install-beta/)

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
package_id = 'ScreenSpace'

import os
from maya import mel

melCommand = os.path.normpath(os.path.join(install_path, 'eblabs_hub', 'ScreenSpace', 'scripts', 'eblabs_screenSpace.mel'))
melCommand = melCommand.replace('\\','\\\\')
mel.eval('source \"{0}\"'.format(melCommand))
mel.eval('ebLabs_screenSpace;')
```


