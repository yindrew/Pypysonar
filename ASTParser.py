import ast


#returns the name of the node
def getName(node):
    if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
        return node.name
    elif isinstance(node, ast.arg):
        return node.arg
    elif isinstance(node, ast.Name):
        return getNameNodeId(node)
    else:
        return None

# if the node is part of builtin, dont return it
def getNameNodeId(node):
    if isBuiltin(node.id):
        return None
    return node.id

# return whether or not the name is part of builtin
def isBuiltin(name):
    return name in ["print"]

# get the position of the node
def getPosition(node):
    if shouldIndex(node):
        startPointOffset = getStartPointOffset(node)
        startRow = node.lineno
        startCol = node.col_offset + startPointOffset
        endRow = startRow
        endCol = startCol + len(getName(node))
        return startRow, startCol, endRow, endCol
    else:
        return None

# get the start offset of the node
def getStartPointOffset(node):
    if isinstance(node, ast.FunctionDef):
        return 4
    if isinstance(node, ast.ClassDef):
        return 6
    else:
        return 0


#return whether or not the node should be indexed
def shouldIndex(node):
    #validNodeType = isinstance(node, (ast.FunctionDef, ast.arg, ast.Name))
    return getName(node) is not None


#create a namespace for a node with the name as the key and the position as the value. If the key is already in, append the position on the end.
def index(namespace, name, position):
    try:
        namespace[name].append(position)
    except:
        namespace[name] = [position]

# create a new sub ns for nodes that have sub-namespaces
def shouldCreateNamespace(node):
    return isinstance(node, (ast.FunctionDef, ast.ClassDef))

# create a new subNS with the properties of the node, and then add the subNS back into the overarching NS.
def createNamespace(namespace, newNS, name, position):
    newNS[name] = position
    namespace["NS" + name] = newNS
