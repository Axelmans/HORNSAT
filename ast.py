# Node base class for usage in AST class
class Node:

    def __init__(self, node_type: str):
        self.type = node_type

    # visitor must be some form of Visitor object.
    def accept(self, visitor):
        pass

    def name(self):
        return str(self)


class NodeVar(Node):

    def __init__(self, identifier: str, complement: bool):
        Node.__init__(self, "Variable")
        # Name of Variable.
        self.identifier = identifier
        # Variable is complement if set to True
        self.neg = complement

    def accept(self, visitor):
        return visitor.visitNodeVar(self)


class NodeClause(Node):

    def __init__(self, variables: list):
        Node.__init__(self, "Clause")
        # Keep Variables inside Clause as list.
        self.vars = variables

    def accept(self, visitor):
        return visitor.visitNodeClause(self)


class NodeFormula(Node):

    def __init__(self, clauses):
        Node.__init__(self, "Formula")
        # Keep Clauses inside Formula as list.
        self.clauses = clauses

    def accept(self, visitor):
        return visitor.visitNodeFormula(self)
