#!/usr/bin/env python3

"""
This is a helper app for "UnRen" to collect, pack and embed different module files
into the main script.

Requirements: py 3.6+
Step 1:
Reads the content of RenPy script files and stores it temporary. Now are the
tool files collected by a dir walker, filepath and data are collected as pairs in
a dict. The dict is pickled (#1), base64 encoded (#2) and also stored.

The different data streams are now embedded in prepaired placeholder locations in
the main script.
#1 The encoder func needs `bytes-like`
#2 Output of compression algorythms would confuse python(error).

Step 2:
Embeds the previously prepaired python script into a Win command file.
"""


import _ur_vers


__title__ = 'UnRen builder'
__license__ = 'Apache-2'
__author__ = 'madeddy'
__status__ = 'Development'
__version__ = _ur_vers.__version__


import os
import sys
import argparse
from pathlib import Path as pt
import pickle
import base64


class UrBuild:
    """
    Constructs from raw base files and different code parts the final
    executable scripts.
    (Class acts more as wrapper for easier var sharing without global.)
    """

    name = 'UnRen builder'
    # config  # hm...absolute or relative paths?
    tools_pth = pt('ur_tools').resolve(strict=True)
    vers_plh = b'vers_placeholder'

    raw_py2 = pt('ur_raw_27.py').resolve(strict=True)
    raw_py3 = pt('ur_raw_36.py').resolve(strict=True)
    base_cmd = pt('ur_base.cmd').resolve(strict=True)

    cpl_py2 = pt('unren_py27.py').resolve()
    cpl_py3 = pt('unren_py36.py').resolve()
    dst_cmd2 = pt('unren_27.cmd').resolve()
    dst_cmd3 = pt('unren_36.cmd').resolve()

    def __init__(self):
        self.emb_fl_lst = []
        self.emb_stream = None
        self._tmp = None

    @staticmethod
    def write_outfile(dst_file, data):
        """Writes a new file with given content."""
        with dst_file.open('wb') as ofi:
            ofi.write(data)

    # Step 1a
    @staticmethod
    def read_rpy_cfg(src_rpy):
        """Reads the RenPy cfg data from a rpy file."""
        with pt(UrBuild.snipped_pth).joinpath(src_rpy).open('rb') as ofi:
            pre_lines = [8 * b' ' + line if line != b'\n' else
                         line for line in ofi.readlines()[4:]]
            pre_lines[:0] = [b'\n']
            cfg_txt = b''.join(pre_lines).rstrip()
        return cfg_txt

    def get_rpy_embeds(self):
        """Gets the cfg text from every listed file and embeds it in the target py."""
        for plh, src_rpy in UrBuild.embed_lib.items():
            self.embed_dct[plh] = self.read_rpy_cfg(src_rpy)

    # Step 1b; pack tools to py
    def stream_packer(self, plh, src_pth):
        """Packs the tools to a pickled and encoded stream."""
        store = {}
        for f_item in self.emb_fl_lst:
            with pt(f_item).open('rb') as ofi:
                d_chunk = ofi.read()

            rel_fp = pt(f_item).relative_to(UrBuild.tools_pth)
            store[str(rel_fp)] = d_chunk

        # NOTE: To reduce size of output a compressor(zlib, lzma...) can be
        # used between pickle and encoder; At the end it is NOT py-code safe
        self.toolstream = base64.b85encode(pickle.dumps(store))
        self.embed_dct[plh] = self.toolstream

    # Step 1a; find tools
    def path_search(self, search_path):
        """Walks the tools directory and collects a list of py files."""
        for entry in search_path.rglob('*.py'):
    # Step 1: Make py
    def build_py(self):
        """Constructs the tools stream and embeds it in the py file."""
        pydst_dct = {UrBuild.raw_py2: UrBuild.cpl_py2,
                     UrBuild.raw_py3: UrBuild.cpl_py3}

    def embed2py(self):
        """Embeds the rpy cfg snippeds in the py files.
        Constructs the tools stream and embeds it in the py file."""
        self.get_rpy_embeds()  # must be before `tools_packer`
        self.path_walker()
        self.tools_packer()

        for _key, _val in dict({UrBuild.raw_py2: UrBuild.dst_py2,
                                UrBuild.raw_py3: UrBuild.dst_py3}).items():
            raw_py, dst_py = pt(_key), pt(_val)
            self.read_filedata(raw_py)

            self.write_outfile(cpl_py, self._tmp)

    # Step 2: Make cmd  - optional (just for the win cmd)
    def build_cmd(self):
        """Constructs the py stream and embeds it in the cmd file."""
        cmddst_dct = {UrBuild.cpl_py2: UrBuild.dst_cmd2,
            self.write_outfile(dst_cmd, self._tmp)


def parse_args():
    """Provides argument parsing functionality on CLI. Obviously."""
    aps = argparse.ArgumentParser(
        description="Helper app to build the release versions of UnRen.",
        epilog="")
    switch = aps.add_mutually_exclusive_group(required=True)
    switch.add_argument('-p', '--makepy',
                        dest='task',
                        action='store_const',
                        const='part_1',
                        help="Executes step 1: embeds the tools into the raw Python scripts.")
    switch.add_argument('-c', '--makecmd',
                        dest='task',
                        action='store_const',
                        const='part_2',
                        help="Executes step 2: embeds the Python script into the cmd.")
    aps.add_argument('--version',
                     action='version',
                     version=f"%(prog)s : { __title__} {__version__}")
    args = aps.parse_args()
    return args


def build_main(cfg):
    """This executes all program steps."""
    if not sys.version_info[:2] >= (3, 6):
        raise Exception("Must be executed in Python 3.6 or later.\n"
                        "You are running {}".format(sys.version))

    urb = UrBuild()
    # Step 1 embed rpy cfg & tools in the raw py files
    if cfg.task == 'part_1':
        urb.build_py()
        print("\nUnRen builder:>> Embed `tools in py` task completed!\n")
    # Step 2 - embed py files in the cmd file
    elif cfg.task == 'part_2':
        urb.build_cmd()
        print("\nUnRen builder:>> Embed `py in cmd` task completed!\n")


if __name__ == '__main__':
    build_main(parse_args())
