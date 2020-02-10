#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
eblabs Package Manager Drag 'n Drop Installer

@2019 Eric Bates, eric@eric-bates.com

This is a quick installer for the eblabs Package Manager. This is a tool that manages the installing
and updating all of your eblabs tools.

"""

__author__ = "Eric Bates, eblabs.com"
__copyright__ = "Copyright (c)2019, Eric Bates"
__credits__ = ["Eric Bates"]
__maintainer__ = "Eric Bates"
__email__ = "info@eblabs.com"
__status__ = "Beta"
__version__ = '0.5.1'
__version_date__ = '2019-11-25'

import urllib2
import urllib
import tempfile
import os
import sys
import zipfile
import shutil
import traceback
import socket
import json
from functools import partial
from maya import cmds


class SummaryManager(object):
    summary_data = []

    @classmethod
    def reset(cls):
        cls.summary_data = []

    @classmethod
    def append_item(cls, item):
        if '\n' in item:
            buffer = item.split('/n')
            for b in buffer:
                cls.summary_data.append(b)
        else:
            cls.summary_data.append(item)

    @classmethod
    def print_summary(cls):
        summary = '''
       _      _         _          
      | |    | |       | |         
  ___ | |__  | |  __ _ | |__   ___ 
 / _ \| '_ \ | | / _` || '_ \ / __|
|  __/| |_) || || (_| || |_) |\__ \\
 \___||_.__/ |_| \__,_||_.__/ |___/
 
 Drag/Drop Package Manager Install Summary
 {0} {1}
        '''.format(__version__, __version_date__)
        print(summary)
        print_summary_items = ''
        if cls.summary_data:
            print_summary_items += '+----------------------------------------\n'
            for i in cls.summary_data:
                print_summary_items += '|' + i + '\n'
            print_summary_items += '+----------------------------------------\n'
        print(print_summary_items)

'''
launcher
'''

def onMayaDroppedPythonFile(*args, **kwargs):
    '''
    run installer
    '''
    Installer.run_installer()


class Status(object):
    Pre = 1
    Offline = 2
    Success = 3
    Error = 4

class Installer():
    Instance = False

    @classmethod
    def run_installer(cls):
        '''
        reset summary
        '''
        SummaryManager.reset()

        '''
        run installer
        '''
        cls.run_installer_exec()

        '''
        print summary
        '''
        SummaryManager.print_summary()

    @classmethod
    def run_installer_exec(cls):
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
            SummaryManager.append_item('Internet Check: Offline')
        else:
            try:
                '''
                attempt to install
                '''

                json_info_url = 'https://raw.githubusercontent.com/eblabs/eblabs_community/master/Installer/installer_info.json'
                info = Utils.read_json_from_url(json_info_url)
                # 'https://github.com/eblabs/eblabs_community/raw/master/Installer/eblabs_PackageManager_0.0.zip'

                package_url = info['installer_url']
                temp_filepath = Utils.download_file(url=package_url)
                if temp_filepath:
                    '''
                    woot, file downloaded
                    '''
                    success = Utils.install_package(filepath=temp_filepath)
                    if success:
                        status = Status.Success
                        SummaryManager.append_item('Install Package: Success')
                    else:
                        SummaryManager.append_item('Install Package: Error')
                        status = Status.Error
            except Exception as e:
                SummaryManager.append_item('Install Package: Fail: {0}, {1}'.format(Exception, e))
                SummaryManager.append_item('Install Package: Traceback: {0}'.format(traceback.format_exc()))
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

1. Download the Latest Offline Installer, it can be found here:
https://github.com/eblabs/eblabs_community/blob/master/Installer/versions/

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
        
        try:
            url = 'github.com'
            socket.create_connection((url, 80))
            return True
        except Exception as e:
            SummaryManager.append_item('Internet Check: Fail: {0}, {1}'.format(Exception, e))
            #print(184, Exception, e)
        return False

        # noinspection PyUnreachableCode
        '''
                try:
                    url = 'https://github.com'
                    urllib2.urlopen(url, timeout=1)
                    return True
                except urllib2.URLError as err:
                    return False
        '''
        '''
        try:
            url = 'https://github.com'
            urllib.urlopen(url, timeout=1)
            return True
        except urllib2.URLError as err:
            return False
        '''

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
                SummaryManager.append_item('Download Package: Success')
                #Debugging.debug_log(205, 'file download success')
                return temp_file
        except Exception as e:
            SummaryManager.append_item('Download Package: Fail: {0}, {1}'.format(Exception, e))
            #Debugging.debug_log(208, Exception, e)
            pass

        return False

    @classmethod
    def ask_user_for_package_file(cls):
        # get path
        filters = 'eblabs_PackageManager_*.zip (eblabs_PackageManager_*.zip)'
        path = cmds.fileDialog2(fileFilter=filters, dialogStyle=2, fileMode=1, okCaption='OK')
        if path:
            return str(path[0])
        else:
            return False

    @classmethod
    def read_json_from_url(cls, url=''):
        #https://stackoverflow.com/questions/1393324/in-python-given-a-url-to-a-text-file-what-is-the-simplest-way-to-read-the-cont
        try:
            url_string = urllib.urlopen(url).read()
            data = json.loads(url_string)
            return data
        except:
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
        SummaryManager.append_item('Install Package: Temp Folder: {0}'.format(temp_folder))
        if not temp_folder:
            return False

        '''
        unzip into install path
        '''
        try:
            with zipfile.ZipFile(filepath, 'r') as z:
                z.extractall(temp_folder)
            SummaryManager.append_item('Unzip: Success: {0}, {1}'.format(temp_folder, filepath))
        except Exception as e:
            SummaryManager.append_item('Unzip: Fail: {0}, {1}, {2}, {3}'.format(Exception, e, temp_folder, filepath))
        '''
        add init files
        '''
        init_files = []
        path = os.path.normpath(os.path.join(temp_folder, '__init__.py'))
        init_files.append(path)
        for f in init_files:
            if not os.path.isfile(f):
                cls.touch(f)
                SummaryManager.append_item('Adding Init Files')

        '''
        run installer command
        '''
        try:
            install_path = temp_folder
            with add_path(install_path):
                '''
                install
                '''
                import scripts.Utils.Misc as Misc
                Misc.Core.install_package(filepaths=[filepath])

                '''
                load UI
                '''
                import scripts.PackageManager as tool
                reload(tool)
                w = tool.Window()
                w.display()
            return True
        except Exception as e:
            SummaryManager.append_item('Install Failed: isFile: {0}, {1}'.format(os.path.isfile(filepath), filepath))
            SummaryManager.append_item('Install Failed: Exception: {0}, {1}'.format(Exception, e))
            SummaryManager.append_item('Install Failed: Traceback: {0}'.format(traceback.format_exc()))
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
                print(409, Exception, e)
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


class add_path(object):
    '''
    #https://stackoverflow.com/questions/17211078/how-to-temporarily-modify-sys-path-in-python

    with add_path('/path/to/dir'):
        mod = __import__('mymodule')
    '''
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        sys.path.insert(0, self.path)

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            sys.path.remove(self.path)
        except ValueError:
            pass
