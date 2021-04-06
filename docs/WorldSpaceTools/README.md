# Welcome to World Space Tools

<img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/WorldSpaceTools/data/eblabs_worldSpaceTools.png" alt="image" width="64px" />


**Advanced animation tools for manipulating animation and switching between local, world space, and other parent spaces.**

# Key Features
* Manipulate your animation in world, local or any other parent space.
* Really useful for fixing up foot sliding with cycled animation.
* Create mini rigs on the fly with existing animation.
* Animator friendly, can full bake or only use keyframes you the animator created.
* Efficient, can batch process multiple objects simultaneously. 
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
| **1** | Menu | Menus and options. |
| **2** | Tabs | From here you can find all of the different modules. |
| **3** | Tools Area | Tools for each module can be found here.  |
| **4** | Quick Undos | Disables the viewport during undo and redo. |

### Spaces Tools Area
| UI | Options | 
| --- | --- |
| <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/WorldSpaceTools/data/WorldSpaceTools_MainUI.jpg" alt="image"/> | <img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/WorldSpaceTools/data/WorldSpaceTools_MainUI_Options.jpg" alt="image"/>  | 


| Item | Description | 
| --- | --- |
| To World Space | <ul><li>Select rig controls and click.</li><li>Temporary controls will be created.</li></ul>  | 
| To Parent Space | <ul><li>Select rig controls first and select your parent last then click.</li><li>Temporary controls will be created.</li></ul>  | 
| To Local Space | <ul><li>Select your world space controls and click.</li><li>Animation will be transfered back to your original objects.</li></ul>   | 

| Options | Description | 
| --- | --- |
| Translates + Rotates | Use these options to select what specific channels are included. |
| On Keys | Select whether the tool uses your existing key frames, or is baked out for a specific frame range. <br>Highighting a range on the timeline also works to set a time range. |


### Extras Tools Area
<img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/WorldSpaceTools/data/WorldSpaceTools_Extras.jpg" alt="image"/>


| Item | Description | 
| --- | --- |
| Add Child COG | Select a world space control and click to create an extra child offset control. | 
| Add Parent COG | Select a world space control and click to create an extra parent offset control.  | 
| Check Gimbal Flipping | Select any animated control and click here to see an analysys of gimble flipping for the current animation. <br><img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/WorldSpaceTools/data/WorldSpaceTools_GimbalScreen.jpg" alt="image"/><br>Look for the lowest % for the least flipping rotate order. | 


### Copy Tools Area
<img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/WorldSpaceTools/data/WorldSpaceTools_Copy.jpg" alt="image"/>


| Item | Description | 
| --- | --- |
| On Keys | Toggle between smart baking on keys or full baking for a time range.  | 
| Maintain Offset | When copying animation you can choose to maintain the current offset. Leaving this will copy animation as is.  | 
| Copy Anim A to B(s) | <ul><li>Select the objects that you'd like to copy animation FROM first.</li><li>Lastly, select one or more objects that you'd like to copy the animation TO and click.</li></ul> | 
| Copy Anim (Single Frame) A to B | Click to copy the current position and rotation. | 


### Path Tools Area
<img src="https://raw.githubusercontent.com/eblabs/eblabs_community/master/docs/WorldSpaceTools/data/WorldSpaceTools_Path.jpg" alt="image"/>


| Item | Description | 
| --- | --- |
| Create Paths For Selected | Click here to create nurbs curve paths that matches your animation. | 
| Rebuild Slider | Use this to simplify the nurbs curve. Set the number of CVs with the slider and click to rebuild the curve.  | 
| Animate Locator | <ul><li>Select the nurbs path followed by the animated control, then click.</li><li>This will create a locator that is attached to the path and animated to closely match the original control. </li></ul>  | 
| To Path Space | Select your animation controls and then click. <br><ul><li>This will create a path space control that preserves the existing animation although now driven through animation along a nurbs path.</li></ul> | 


# Manual Installation (Advanced User)

The Package Manager makes installing a simple process, but if you need to do this manually here's how.

A great place to install these tools is in the maya/script folder, please see the folder structure below to setup your tools in the simplest way. Tools should be installed to a common `eblabs_hub` folder. The `install path` should be one folder up from the `eblabs_hub` folder. Make sure that there are blank `__init__.py` files within all folders.

## Folder Structure
```
.
├── eblabs_hub
└── __init__.py
    └── package_id
        ├── __init__.py
        └── unzip package contents here
```

## Reminder on Install Path
Make sure to reference the parent folder of your /eblabs_hub folder.

Bad: 
```python
install_path = 'E:/path/to/maya/scripts/eblabs_hub'
```

Good: 
```python
install_path = 'E:/path/to/maya/scripts'
```

## Launch Command
```python
install_path = 'E:/path/to/maya/script/'
package_id = 'WorldSpaceTools'

import os
import sys
if not install_path in sys.path:
    sys.path.append(install_path)

import eblabs_hub.WorldSpaceTools.scripts.worldspace as tool

tool.window.load()
```


