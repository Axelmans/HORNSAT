# Generated from HORNSAT.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .HORNSATParser import HORNSATParser
else:
    from HORNSATParser import HORNSATParser

# This class defines a complete generic visitor for a parse tree produced by HORNSATParser.

class HORNSATVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by HORNSATParser#AllClauses.
    def visitAllClauses(self, ctx:HORNSATParser.AllClausesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HORNSATParser#SingleClause.
    def visitSingleClause(self, ctx:HORNSATParser.SingleClauseContext):
        return self.visitChildren(ctx)



del HORNSATParser