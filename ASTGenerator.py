import ast
import ASTParser as parser

# reads ToBeIndexed and parses it into a AST and then turns it into a namespace heiarchy and prints it out
def show_ast():
    with open("ToBeIndexed.py", "r") as source:
        text = source.read()
        tree = ast.parse(text)
        namespace = {}
        walk(namespace, tree)
        print(namespace)

# Turns a AST into a namespace heiarchy.
def walk(namespace, node, level = 0, sep = '\t'):
    name = parser.getName(node)
    position = parser.getPosition(node)

    if parser.shouldIndex(node):
        parser.index(namespace, name, position)

    for n in ast.iter_child_nodes(node):

        if parser.shouldCreateNamespace(node):
            ns = {}
            parser.createNamespace(namespace, ns, name, position)
            walk(ns, n, level + 1)
        else:
            walk(namespace, n, level + 1)