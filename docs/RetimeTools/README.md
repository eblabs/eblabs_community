# Welcome to Retime Tools

A versitile toolset for retiming your animation. 

Some features include,
* Experiment with timing changes non-destructively.
* Any number of retimes in your scene.
* Full bake or "Shuffle" your existing keys based on the retime.

<img src="data/RetimeTools_MainWindow.jpg" alt="image" width="600"/>

# How to install?
Use the Package Manager for quickly installing and updating Tools, get it here:
[Package Manager Getting Started](https://eblabs.com/package-manager-quick-install-beta/)


# I want to...
## ...create a new Retime Object
## ...bake out my animation
## ...bake out my animation but perserve my keyframes
## ...clean up my subframe keys


# UI Manual

## Main Areas


# Manual Installation (Advanced User)
`
install_path = 'E:/Git/eblabs-hub/'
package_id = 'RetimeTools'

import os
import sys
if not install_path in sys.path:
    sys.path.append(install_path)

import eblabs_hub.RetimeTools.scripts.RetimeTools as tool
reload(tool)
w = tool.Window()
w.display()
`


