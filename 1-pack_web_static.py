#!/usr/bin/python3
"""generates a .tgz archive from the contents of the web_static folder"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """Return the archive path if correctly generated"""
    try:
        create_time = datetime.now().strftime("%Y%m%d%H%M%S")
        taz_path = "/versions/web_static_" + create_time + ".tgz"
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(taz_path))
        return taz_path
    except Exception:
        return None
