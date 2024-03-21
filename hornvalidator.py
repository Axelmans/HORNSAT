from visitor import *


class HornValidator(Visitor):

    def visitNodeVar(self, node: NodeVar):
        return not node.neg

    def visitNodeClause(self, node: NodeClause):
        positive_var_found = False
        for var in node.vars:
            var_result = var.accept(self)
            if not positive_var_found and var_result:
                positive_var_found = True
            elif positive_var_found and var_result:
                return False
        return True

    def visitNodeFormula(self, node: NodeFormula):
        for clause in node.clauses:
            if not clause.accept(self):
                raise RuntimeError("Invalid Clause in formula: make sure each one has at most one positive variable.")
        return True
