import ASTGenerator as Generator
import ASTParser as Parser
import ast


if __name__ == '__main__':
    # converts it into a txt file
    with open("ToBeIndexed.py", "r") as source:
        text = source.read()

        # converts the txt file into a AST
        tree = Parser.parse(text)

        # converts the AST into a Namespace Hierarchy
        index = Generator.generate(tree)

    # Print of the namespace Hierarchy
    print(index)




