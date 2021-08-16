import ast
import ASTParser as Parser


# Generates the namespace hierarchy
def generate(tree):
    namespace, level, separator = {}, 0, '\t'
    _walk(namespace, tree, level, separator)
    return namespace


# Turns a AST into a namespace hierarchy.
def _walk(namespace, node, level=0, sep='\t'):
    print(level, ':', sep*level, node)

    # get the name and the position of the node
    name = Parser.get_name(node)
    position = Parser.get_position(node)

    # if the parser should be indexed, index and put the node into the NS
    if Parser.should_index(node):
        Parser.index(namespace, name, position)

    # if the parser is a type that will need a inner namespace, create the inner namespace and walk through it
    if Parser.should_create_namespace(node):
        namespace = Parser.create_namespace(namespace, name, position)

    # loop through the child nodes
    for n in ast.iter_child_nodes(node):
        _walk(namespace, n, level + 1)
