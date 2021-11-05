from collections import defaultdict, OrderedDict
from csv import reader
from itertools import chain, combinations
from optparse import OptionParser
from fpgrowth_py.utils import *

itemSetList = [['eggs', 'bacon', 'soup'],
                ['eggs', 'bacon', 'apple'],
                ['soup', 'bacon', 'banana'],
               ['soup','banana']]

frequency = [1 for i in range(len(itemSetList))]


headerTable = defaultdict(int)
# Counting frequency and create header table
#
for idx, itemSet in enumerate(itemSetList):
    for item in itemSet:
        headerTable[item] += frequency[idx]

#headerTable = dict((item, sup) for item, sup in headerTable.items() if sup >= minSup)
for item, sup in headerTable.items():
    if sup >= 2:
        headerTable[item]=sup


if(len(headerTable) == 0):
    print('no fp tree,no headertable')

for item in headerTable:
    headerTable[item] = [headerTable[item], None]



# Init Null head node
fpTree = Node('Null', 1, None)
# Update FP tree for each cleaned and sorted itemSet
for idx, itemSet in enumerate(itemSetList):
    itemSet = [item for item in itemSet if item in headerTable]
    itemSet.sort(key=lambda item: headerTable[item][0], reverse=True)
    print(itemSet)
    # Traverse from root to leaf, update tree with given item
    currentNode = fpTree
    print(currentNode)
    i=0
    for item in itemSet:
        #currentNode = updateTree(item, currentNode, headerTable, frequency[idx])
        i+=1
        if item in currentNode.children:
            # If the item already exists, increment the count
            currentNode.children[item].increment(frequency)
            print(currentNode.children[item])
        else:
            i=1
            # Create a new branch
            newItemNode = Node(item, frequency, currentNode)
            currentNode.children[item] = newItemNode
            print(currentNode.children[item])
            # Link the new branch to header table
            updateHeaderTable(item, newItemNode, headerTable)