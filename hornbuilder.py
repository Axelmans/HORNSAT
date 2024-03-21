from ANTLR4.HORNSATParser import *
from ANTLR4.HORNSATVisitor import *
from ast import *


class HornBuilder(HORNSATVisitor):

    def visitAllClauses(self, ctx: HORNSATParser.AllClausesContext):
        clauses = []
        for clause in ctx.clause():
            clauses.append(self.visit(clause))
        return NodeFormula(clauses)

    def visitSingleClause(self, ctx: HORNSATParser.SingleClauseContext):
        variables = []
        negation = False
        for char in ctx.getText():
            if char in ["(", ")", "|"]:
                continue
            elif char == "~":
                negation = True
            else:
                variables.append(NodeVar(char, negation))
                negation = False
        return NodeClause(variables)
