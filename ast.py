class Node:

    def __init__(self, node_type: str):
        self.type = node_type

    def accept(self, visitor):
        pass

    def name(self):
        return str(self)


class NodeVar(Node):

    def __init__(self, identifier: str, complement: bool):
        Node.__init__(self, "Variable")
        self.identifier = identifier
        self.neg = complement

    def accept(self, visitor):
        return visitor.visitNodeVar(self)


class NodeClause(Node):

    def __init__(self, variables):
        Node.__init__(self, "Clause")
        self.vars = variables

    def accept(self, visitor):
        return visitor.visitNodeClause(self)


class NodeFormula(Node):

    def __init__(self, clauses):
        Node.__init__(self, "Formula")
        self.clauses = clauses

    def accept(self, visitor):
        return visitor.visitNodeFormula(self)
