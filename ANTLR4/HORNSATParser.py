# Generated from HORNSAT.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\t")
        buf.write(" \4\2\t\2\4\3\t\3\3\2\3\2\3\2\7\2\n\n\2\f\2\16\2\r\13")
        buf.write("\2\3\3\3\3\5\3\21\n\3\3\3\3\3\3\3\5\3\26\n\3\3\3\7\3\31")
        buf.write("\n\3\f\3\16\3\34\13\3\3\3\3\3\3\3\2\2\4\2\4\2\2\2!\2\6")
        buf.write("\3\2\2\2\4\16\3\2\2\2\6\13\5\4\3\2\7\b\7\3\2\2\b\n\5\4")
        buf.write("\3\2\t\7\3\2\2\2\n\r\3\2\2\2\13\t\3\2\2\2\13\f\3\2\2\2")
        buf.write("\f\3\3\2\2\2\r\13\3\2\2\2\16\20\7\4\2\2\17\21\7\7\2\2")
        buf.write("\20\17\3\2\2\2\20\21\3\2\2\2\21\22\3\2\2\2\22\32\7\6\2")
        buf.write("\2\23\25\7\b\2\2\24\26\7\7\2\2\25\24\3\2\2\2\25\26\3\2")
        buf.write("\2\2\26\27\3\2\2\2\27\31\7\6\2\2\30\23\3\2\2\2\31\34\3")
        buf.write("\2\2\2\32\30\3\2\2\2\32\33\3\2\2\2\33\35\3\2\2\2\34\32")
        buf.write("\3\2\2\2\35\36\7\5\2\2\36\5\3\2\2\2\6\13\20\25\32")
        return buf.getvalue()


class HORNSATParser ( Parser ):

    grammarFileName = "HORNSAT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'&&'", "'('", "')'", "<INVALID>", "'~'", 
                     "'||'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "VAR", "NEGATION", "DISJUNCTION", "WS" ]

    RULE_formula = 0
    RULE_clause = 1

    ruleNames =  [ "formula", "clause" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    VAR=4
    NEGATION=5
    DISJUNCTION=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class FormulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HORNSATParser.RULE_formula

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AllClausesContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HORNSATParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def clause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HORNSATParser.ClauseContext)
            else:
                return self.getTypedRuleContext(HORNSATParser.ClauseContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAllClauses" ):
                listener.enterAllClauses(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAllClauses" ):
                listener.exitAllClauses(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAllClauses" ):
                return visitor.visitAllClauses(self)
            else:
                return visitor.visitChildren(self)



    def formula(self):

        localctx = HORNSATParser.FormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_formula)
        self._la = 0 # Token type
        try:
            localctx = HORNSATParser.AllClausesContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.clause()
            self.state = 9
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HORNSATParser.T__0:
                self.state = 5
                self.match(HORNSATParser.T__0)
                self.state = 6
                self.clause()
                self.state = 11
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HORNSATParser.RULE_clause

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SingleClauseContext(ClauseContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HORNSATParser.ClauseContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self, i:int=None):
            if i is None:
                return self.getTokens(HORNSATParser.VAR)
            else:
                return self.getToken(HORNSATParser.VAR, i)
        def NEGATION(self, i:int=None):
            if i is None:
                return self.getTokens(HORNSATParser.NEGATION)
            else:
                return self.getToken(HORNSATParser.NEGATION, i)
        def DISJUNCTION(self, i:int=None):
            if i is None:
                return self.getTokens(HORNSATParser.DISJUNCTION)
            else:
                return self.getToken(HORNSATParser.DISJUNCTION, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleClause" ):
                listener.enterSingleClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleClause" ):
                listener.exitSingleClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleClause" ):
                return visitor.visitSingleClause(self)
            else:
                return visitor.visitChildren(self)



    def clause(self):

        localctx = HORNSATParser.ClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_clause)
        self._la = 0 # Token type
        try:
            localctx = HORNSATParser.SingleClauseContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.match(HORNSATParser.T__1)
            self.state = 14
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HORNSATParser.NEGATION:
                self.state = 13
                self.match(HORNSATParser.NEGATION)


            self.state = 16
            self.match(HORNSATParser.VAR)
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HORNSATParser.DISJUNCTION:
                self.state = 17
                self.match(HORNSATParser.DISJUNCTION)
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HORNSATParser.NEGATION:
                    self.state = 18
                    self.match(HORNSATParser.NEGATION)


                self.state = 21
                self.match(HORNSATParser.VAR)
                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 27
            self.match(HORNSATParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





