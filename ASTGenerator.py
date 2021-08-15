import ast
import ASTParser as parser



# generate the namespace hieracrhy
def generate(tree):
    namespace, level, seperator = {}, 0, '\t'
    walk(namespace, tree, level, seperator)
    return namespace


# Turns a AST into a namespace hiearchy.
def walk(namespace, node, level = 0, sep = '\t'):

    # get the name and the position
    name = parser.getName(node)
    position = parser.getPosition(node)

    # if the parser should be indexed, index and put the node into the NS
    if parser.shouldIndex(node):
        parser.index(namespace, name, position)

    # loop thru the child nodes
    for n in ast.iter_child_nodes(node):
        # if you should create a subNS create one, and add the node into the subNS
        if parser.shouldCreateNamespace(node):
            # create a new namespace
            ns = {}
            parser.createNamespace(namespace, ns, name, position)
            walk(ns, n, level + 1)
        # if you don't have to create a subNS, just walk thru the regular node
        else:
            walk(namespace, n, level + 1)