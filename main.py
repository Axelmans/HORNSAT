from hornbuilder import *
from hornvalidator import *
from hornsolver import *
from ANTLR4.HORNSATLexer import HORNSATLexer, InputStream, CommonTokenStream

lexer = HORNSATLexer(InputStream(open("test.txt", "r").read()))
stream = CommonTokenStream(lexer)
parser = HORNSATParser(stream)
tree = parser.formula()
builder = HornBuilder()
ast = builder.visit(tree)
validator = HornValidator()
ast.accept(validator)
solver = HornSolver()
assignment = ast.accept(solver)
print(assignment)
fei = "fei"

