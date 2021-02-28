_author__ = "Tim Peisker"
__copyright__ = "None"
__license__ = "None"
__maintainer__ = "Tim Peisker"
__email__ = "tim.peisker@tum.de"
__status__ = "Development"
__descr__ = """
    generate shopping list
"""

from pathlib import Path

__package__ = str(Path(
    __file__).parent.parent)  # the best way I know of to make relative imports work when exectuting a sript that isn't located at the top level in the package

import time
import argparse
import utils.utils as ut
import numpy as np
import itertools
from classes.SimFile import InputFile
from anytree import Node, RenderTree
import json


def proc_input():


    parser = argparse.ArgumentParser(
        description=__descr__,
    )
    parser.add_argument("-i", "--inputFile",
                        help="input json file with tacoxdna location",
                        type=str
                        )
    parser.add_argument("-d", "--directory",
                        help="directory where to do the conversion",
                        type=str
                        )
    parser.add_argument("-c", "--confName",
                        help="name to store the .oxdna portions",
                        type=str,
                        default = "start.oxdna"
                        )
    parser.add_argument("-t", "--topName",
                        help="name to store the .top portions",
                        type=str,
                        default="top.top"
                        )

    args = parser.parse_args()
    with open(args.inputFile) as json_file:
        input = json.load(json_file)
    args.json = input
    return args


def main():
    starttime = time.time()

    input = proc_input()
    files = ut.findFiles(input.directory)
    for f in files:
        subdir = ut.make_directory(parent=input.directory, name=Path(f).stem, date=False)
        ut.json_to_oxdna_top_converter(json_file=f, dest_folder=subdir, tacoxDNA=input.json["tacoxDNA"])  # TODO: add sequence file support, add start.oxdna and top.top name variation
        f.rename(Path(subdir)/ str(Path(f).name))


    print('That took {} seconds'.format(time.time() - starttime))


if __name__ == "__main__":
    main()
