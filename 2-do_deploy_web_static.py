#!/usr/bin/python3
"""(based on 1-pack_web_static.py) distributes an archive to web servers"""
from fabric.api import *
from os.path import exists
env.hosts = ['54.82.195.119', '54.90.96.25']


def do_deploy(archive_path):
    """Returns True if done correctly, otherwise False"""
    if exists(archive_path) is False:
        return False
    try:
        put(archive_path, "/tmp/")
        file_name = archive_path.split("/")[-1]
        no_extension = file_name.split(".")[0]
        uncompressfd = "/data/web_static/releases/{}/".format(no_extension)
        run("mkdir -p {}".format(uncompressfd))
        run("tar -zxvf /tmp/{} -C {}".format(file_name, uncompressfd))
        run("rm /tmp/{}".format(file_name))
        run("mv {}web_static/* {}/".format(uncompressfd, uncompressfd))
        run("rm -rf {}web_static".format(uncompressfd))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(uncompressfd))
        return True
    except Exception:
        return False
