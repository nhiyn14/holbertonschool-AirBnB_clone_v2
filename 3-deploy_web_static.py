#!/usr/bin/python3
"""
(based on 2-do_deploy_web_static.py)
creates and distributes an archive to your web servers
"""

from fabric.api import *
from os.path import exists
from datetime import datetime
env.hosts = ['54.82.195.119', '54.90.96.25']


def do_pack():
    """Create an archive. Return the archive path"""
    try:
        create_time = datetime.now().strftime("%Y%m%d%H%M%S")
        taz_path = "versions/web_static_{}.tgz".format(create_time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(taz_path))
        return taz_path
    except Exception:
        return None


def do_deploy(archive_path):
    """Distribute an archive to web server. Returns True"""
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


def deploy():
    """Combine do_pack and do_deploy(archive_path)"""
    archive_path = do_pack()
    return do_deploy(archive_path)
