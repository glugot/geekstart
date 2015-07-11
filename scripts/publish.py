#!/usr/bin/env python


import os
import shutil
import subprocess

from distutils.dir_util import copy_tree


GIT_REPO = "https://github.com/glugot/geekstart.git"
DEST_DIR = "/home/stylesen/geekstart.git"
WEB_ROOT_DEST = "/home/stylesen/public_html/geekstart"


def publish():
    if os.path.exists(DEST_DIR):
        pwd = os.getcwd()
        os.chdir(DEST_DIR)
        try:
            subprocess.check_call(["git", "pull"])
            print "Updated local clone on %s" % DEST_DIR
        except subprocess.CalledProcessError:
            print "git pull failed on %s" % DEST_DIR
            raise
    else:
        try:
            subprocess.check_call(["git", "clone",
                                   "https://github.com/glugot/geekstart.git",
                                   DEST_DIR])
        except subprocess.CalledProcessError:
            print "git clone failed" % DEST_DIR
            raise

    pwd = os.getcwd()
    os.chdir(DEST_DIR)
    try:
        subprocess.check_call(["make", "clean"])
        subprocess.check_call(["make", "publish"])
    except subprocess.CalledProcessError:
        print "make failed"
        raise

    if os.path.exists(WEB_ROOT_DEST):
        shutil.rmtree(WEB_ROOT_DEST)

    os.mkdir(WEB_ROOT_DEST)
    copy_tree(os.path.join(DEST_DIR, "output"), WEB_ROOT_DEST)


def main():
    publish()

if __name__ == '__main__':
    main()
