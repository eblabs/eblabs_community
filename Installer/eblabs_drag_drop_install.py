#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
eblabs Package Manager Drag 'n Drop Installer

@2019 Eric Bates, eric@eric-bates.com

This is a quick installer for the eblabs Package Manager. This is a tool that manages the installing
and updating all of your eblabs tools.

"""

import urllib2
import urllib
import tempfile
import os
import sys
import zipfile
import shutil
from functools import partial
from maya import cmds

'''
launcher
'''
def onMayaDroppedPythonFile(*args, **kwargs):
    Installer.run_installer()


class Status(object):
    Pre = 1
    Offline = 2
    Success = 3
    Error = 4


class Debugging():

    display_logging = True

    @classmethod
    def debug_log(cls, *args, **kwargs):
        '''
        No Logging
        '''
        if not cls.display_logging:
            return False

        '''
        Logging
        '''
        print("""DEBUGGING LOG""")
        if args:
            for i, a in enumerate(args):
                print(i, a)

class Installer():
    Instance = False

    @classmethod
    def run_installer(cls):
        '''
        1. check if online
        2. get package, via online or local
        3. install local
        4. build shelf + button
        5. Congrats, info popup
        '''
        status = Status.Pre

        '''
        auto run stages
        '''
        is_online = Utils.internet_on()
        if not is_online:
            status = Status.Offline
        else:
            try:
                '''
                attempt to install
                '''
                url = 'https://github.com/eblabs/eblabs_docs/raw/master/Installer/eblabs_PackageManager_0.0.zip'
                temp_filepath = Utils.download_file(url=url)
                if temp_filepath:
                    '''
                    woot, file downloaded
                    '''
                    success = Utils.install_package(filepath=temp_filepath)
                    if success:
                        status = Status.Success
                    else:
                        Debugging.debug_log(94, 'Error')
                        status = Status.Error
            except Exception as e:
                Debugging.debug_log(97, Exception, e)
                status = Status.Error

        '''
        message
        '''
        if status == Status.Success:
            cls.success_popup()
        else:
            cls.fail_popup()

    @classmethod
    def success_popup(cls):
        text = '''
The eblabs Package Manager was installed Successfully!

It can be accessed from the eblabs shelf. Give it a try
to manage and update all your eblabs tools.

Check out eblabs.com for more info.

Happy Animating!

        '''

        cmds.confirmDialog(title='eblabs Successfully Installed', message=text, button=['Amazing'], defaultButton='Yes',
                           cancelButton='No', dismissString='No', icon='information')

    @classmethod
    def fail_popup(cls):
        '''
        text
        '''
        text = '''
It wasn't possible to connect to the internet or possibly 
there is another issue. Please try the offline install method. 

For support use the contact page at eblabs.com.

1. Download the Offline Installer, it can be found here:
https://github.com/eblabs/eblabs_docs/blob/master/Installer/eblabs_PackageManager_0.0.zip

2. Click Install and select the installer file.

3. Happy Animating!
                        '''

        '''
        dialog
        '''
        return_string = cmds.confirmDialog(title='eblabs Offline Install', message=text, button=['Cancel', 'Install'], defaultButton='Install',
                           cancelButton='Cancel', dismissString='Cancel', icon='warning')

        '''
        install
        '''
        if return_string == 'Install':
            success = Utils.install_package()
            if success:
                status = Status.Success
            else:
                status = Status.Error
        else:
            return False

        '''
        message
        '''
        if status == Status.Success:
            cls.success_popup()
        else:
            cls.fail_popup()

class Utils():

    @classmethod
    def internet_on(cls):
        '''
        use github as an online check
        '''
        try:
            url = 'https://github.com'
            urllib2.urlopen(url, timeout=1)
            return True
        except urllib2.URLError as err:
            return False

    @classmethod
    def download_file(cls, url=''):
        '''
        check
        '''
        if not url:
            return False

        '''
        temp save dir
        '''
        temp_folder = tempfile.gettempdir()
        _, filename = os.path.split(url)
        temp_file = os.path.normpath(os.path.join(temp_folder, filename))

        '''
        download
        '''
        try:
            urllib.urlretrieve(url, filename=temp_file)
            if os.path.exists(temp_file):
                return temp_file
        except Exception as e:
            pass

        '''
        fallback
        '''
        return False

    @classmethod
    def ask_user_for_package_file(cls):
        # get path
        filters = 'eblabs_PackageManager_0.0.zip (eblabs_PackageManager_0.0.zip)'
        path = cmds.fileDialog2(fileFilter=filters, dialogStyle=2, fileMode=1, okCaption='OK')
        if path:
            return str(path[0])
        else:
            return False

    @classmethod
    def touch(cls, path):
        '''
        create folder
        '''
        basedir = os.path.dirname(path)
        if not os.path.exists(basedir):
            os.makedirs(basedir)
        '''
        create empty file
        '''
        with open(path, 'a'):
            os.utime(path, None)

    @classmethod
    def install_package(cls, filepath = False):
        '''
        ask user for package
        '''
        if not filepath:
            filepath = cls.ask_user_for_package_file()
        if not filepath:
            return False

        '''
        simple
        1. unzip to temp folder
        2. run installer with package file
        '''
        temp_folder = cls.get_clean_temp_folder()
        if not temp_folder:
            return False

        '''
        unzip into install path
        '''
        with zipfile.ZipFile(filepath, 'r') as z:
            z.extractall(temp_folder)

        '''
        add init files
        '''
        init_files = []
        path = os.path.normpath(os.path.join(temp_folder, '__init__.py'))
        init_files.append(path)
        for f in init_files:
            if not os.path.isfile(f):
                cls.touch(f)

        '''
        run installer command
        '''
        try:
            install_path = temp_folder
            if not install_path in sys.path:
                sys.path.append(install_path)
            import scripts.PackageManager as tool
            reload(tool)

            '''
            install package manager
            '''
            tool.Utils.install_package(filepaths=[filepath])

            '''
            run
            '''
            w = tool.Window()
            w.display()
            return True
        except Exception as e:
            Debugging.debug_log(998, 'Install Failed', Exception, e)
            return False

    @classmethod
    def get_clean_temp_folder(cls):
        '''
        get temp folder
        '''
        temp_folder = tempfile.gettempdir()
        clean_folder = os.path.normpath(os.path.join(temp_folder, 'eblabs_temp'))

        '''
        delete if it exists
        '''
        if os.path.exists(clean_folder):
            try:
                shutil.rmtree(clean_folder)
            except Exception as e:
                pass

        '''
        generate new folders
        '''
        try:
            if not os.path.exists(clean_folder):
                os.makedirs(clean_folder)
        except:
            pass

        '''
        
        '''
        if not os.path.exists(clean_folder):
            return False
        return clean_folder
