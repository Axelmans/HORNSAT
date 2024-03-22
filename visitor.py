from ast import *


# This is a base class, derived classes might have redefined visit functions.
# Upgrading the grammar means expanding the different Node objects, and allowing them to be visited.
class Visitor:

    def visitNodeVar(self, node: NodeVar):
        pass

    def visitNodeClause(self, node: NodeClause):
        pass

    def visitNodeFormula(self, node: NodeFormula):
        pass
