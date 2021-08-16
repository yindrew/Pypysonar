import ast


def parse(code):
    return ast.parse(code)


# returns the name of the node
def get_name(node):
    if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
        return node.name
    elif isinstance(node, ast.arg):
        return node.arg
    elif isinstance(node, ast.Name):
        return get_name_node_id(node)
    else:
        return None


# if the node is part of builtin, don't return it
def get_name_node_id(node):
    if is_built_in(node.id):
        return None
    return node.id


# return whether or not the name is part of builtin
def is_built_in(name):
    return name in ["print"]


# get the position of the node
def get_position(node):
    if should_index(node):
        start_point_offset = get_start_point_offset(node)
        start_row = node.lineno
        start_col = node.col_offset + start_point_offset
        end_row = start_row
        end_col = start_col + len(get_name(node))
        return start_row, start_col, end_row, end_col
    else:
        return None


# get the start offset of the node
def get_start_point_offset(node):
    if isinstance(node, ast.FunctionDef):
        return 4
    if isinstance(node, ast.ClassDef):
        return 6
    else:
        return 0


# return whether or not the node should be indexed
def should_index(node):
    return get_name(node) is not None


# create a namespace for a node with the name as the key and the position as the value. If the key is already in, append
# the position on the end.
def index(namespace, name, position):
    try:
        namespace[name].append(position)
    except KeyError:
        namespace[name] = [position]


# create a new sub ns for nodes that have sub-namespaces
def should_create_namespace(node):
    return isinstance(node, (ast.FunctionDef, ast.ClassDef))


# create a new subNS with the properties of the node, and then add the subNS back into the overarching NS.
def create_namespace(namespace, name, position):
    new_namespace = {name: position}
    namespace["NS_" + name] = new_namespace
    return new_namespace
