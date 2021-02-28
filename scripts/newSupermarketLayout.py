_author__ = "Tim Peisker"
__copyright__ = "None"
__license__ = "None"
__maintainer__ = "Tim Peisker"
__email__ = "tim.peisker@tum.de"
__status__ = "Development"
__descr__ = """
    generate new supermarket layout
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
from graphviz import Digraph

def proc_input():  # TODO: implement correctly, maybe design a node-code UI for this task


    parser = argparse.ArgumentParser(
        description=__descr__,
    )
    parser.add_argument("-n", "--name",
                        help="input json file with tacoxdna location",
                        type=str
                        )
    parser.add_argument("-n", "--nodes",
                        help="sections of your supermarket",
                        type=str
                        )
    parser.add_argument("-e", "--edges",
                        help="which sections are connected",
                        type=str
                        )

    args = parser.parse_args()
    with open(args.inputFile) as json_file:
        input = json.load(json_file)
    args.json = input
    return args

def add_nodes(dot, nodes):
    for node in nodes():
        dot.node()  # TODO: complete this


def main():
    starttime = time.time()

    input = proc_input()
    dot = Digraph(name=input.name)
    add_nodes(dot, input.nodes)
    dot.edges(input.edges)
    dot.render('../SupermarketLayouts/{}.gv'.format(input.name), view=True)



    print('That took {} seconds'.format(time.time() - starttime))


if __name__ == "__main__":
    main()
