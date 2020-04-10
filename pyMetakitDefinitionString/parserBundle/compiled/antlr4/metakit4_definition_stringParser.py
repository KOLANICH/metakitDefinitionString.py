# Generated from grammar.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,12,61,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,1,1,1,1,3,1,24,8,1,1,2,1,2,1,2,1,2,
        1,2,1,3,1,3,1,3,1,3,1,4,1,4,3,4,37,8,4,1,5,5,5,40,8,5,10,5,12,5,
        43,9,5,1,6,1,6,1,6,1,7,4,7,49,8,7,11,7,12,7,50,1,8,1,8,4,8,55,8,
        8,11,8,12,8,56,3,8,59,8,8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,0,57,
        0,18,1,0,0,0,2,23,1,0,0,0,4,25,1,0,0,0,6,30,1,0,0,0,8,36,1,0,0,0,
        10,41,1,0,0,0,12,44,1,0,0,0,14,48,1,0,0,0,16,58,1,0,0,0,18,19,3,
        2,1,0,19,20,3,10,5,0,20,1,1,0,0,0,21,24,3,6,3,0,22,24,3,4,2,0,23,
        21,1,0,0,0,23,22,1,0,0,0,24,3,1,0,0,0,25,26,3,14,7,0,26,27,5,1,0,
        0,27,28,3,8,4,0,28,29,5,2,0,0,29,5,1,0,0,0,30,31,3,14,7,0,31,32,
        5,3,0,0,32,33,5,10,0,0,33,7,1,0,0,0,34,37,3,0,0,0,35,37,5,5,0,0,
        36,34,1,0,0,0,36,35,1,0,0,0,37,9,1,0,0,0,38,40,3,12,6,0,39,38,1,
        0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,11,1,0,0,0,43,
        41,1,0,0,0,44,45,5,4,0,0,45,46,3,2,1,0,46,13,1,0,0,0,47,49,3,16,
        8,0,48,47,1,0,0,0,49,50,1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,15,
        1,0,0,0,52,59,5,10,0,0,53,55,5,6,0,0,54,53,1,0,0,0,55,56,1,0,0,0,
        56,54,1,0,0,0,56,57,1,0,0,0,57,59,1,0,0,0,58,52,1,0,0,0,58,54,1,
        0,0,0,59,17,1,0,0,0,6,23,36,41,50,56,58
    ]

class metakit4_definition_stringParser ( Parser ):

    grammarFileName = "grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "':'", "','", "'^'" ]

    symbolicNames = [ "<INVALID>", "SubFieldsStart", "SubFieldsEnd", "Colon", 
                      "OptionsSeparator", "IndirectMarker", "OtherWordChars", 
                      "OtherWordCharsOther", "OtherWordCharsUpper", "OtherWordCharsLower", 
                      "TypeSpecifier", "TypeSpecifierUpper", "TypeSpecifierLower" ]

    RULE_subFields = 0
    RULE_scalarOrView = 1
    RULE_view = 2
    RULE_scalar = 3
    RULE_body = 4
    RULE_rest_subFields_with_delF = 5
    RULE_rest_subField_with_delF = 6
    RULE_word = 7
    RULE_wordPiece = 8

    ruleNames =  [ "subFields", "scalarOrView", "view", "scalar", "body", 
                   "rest_subFields_with_delF", "rest_subField_with_delF", 
                   "word", "wordPiece" ]

    EOF = Token.EOF
    SubFieldsStart=1
    SubFieldsEnd=2
    Colon=3
    OptionsSeparator=4
    IndirectMarker=5
    OtherWordChars=6
    OtherWordCharsOther=7
    OtherWordCharsUpper=8
    OtherWordCharsLower=9
    TypeSpecifier=10
    TypeSpecifierUpper=11
    TypeSpecifierLower=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SubFieldsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.first_subField = None # ScalarOrViewContext
            self.rest_subFields_with_del = None # Rest_subFields_with_delFContext

        def scalarOrView(self):
            return self.getTypedRuleContext(metakit4_definition_stringParser.ScalarOrViewContext,0)


        def rest_subFields_with_delF(self):
            return self.getTypedRuleContext(metakit4_definition_stringParser.Rest_subFields_with_delFContext,0)


        def getRuleIndex(self):
            return metakit4_definition_stringParser.RULE_subFields

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubFields" ):
                listener.enterSubFields(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubFields" ):
                listener.exitSubFields(self)




    def subFields(self):

        localctx = metakit4_definition_stringParser.SubFieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_subFields)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            localctx.first_subField = self.scalarOrView()
            self.state = 19
            localctx.rest_subFields_with_del = self.rest_subFields_with_delF()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScalarOrViewContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.scalarF = None # ScalarContext
            self.viewF = None # ViewContext

        def scalar(self):
            return self.getTypedRuleContext(metakit4_definition_stringParser.ScalarContext,0)


        def view(self):
            return self.getTypedRuleContext(metakit4_definition_stringParser.ViewContext,0)


        def getRuleIndex(self):
            return metakit4_definition_stringParser.RULE_scalarOrView

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScalarOrView" ):
                listener.enterScalarOrView(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScalarOrView" ):
                listener.exitScalarOrView(self)




    def scalarOrView(self):

        localctx = metakit4_definition_stringParser.ScalarOrViewContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_scalarOrView)
        try:
            self.state = 23
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                localctx.scalarF = self.scalar()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                localctx.viewF = self.view()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ViewContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # WordContext
            self.bodyF = None # BodyContext

        def SubFieldsStart(self):
            return self.getToken(metakit4_definition_stringParser.SubFieldsStart, 0)

        def SubFieldsEnd(self):
            return self.getToken(metakit4_definition_stringParser.SubFieldsEnd, 0)

        def word(self):
            return self.getTypedRuleContext(metakit4_definition_stringParser.WordContext,0)


        def body(self):
            return self.getTypedRuleContext(metakit4_definition_stringParser.BodyContext,0)


        def getRuleIndex(self):
            return metakit4_definition_stringParser.RULE_view

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterView" ):
                listener.enterView(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitView" ):
                listener.exitView(self)




    def view(self):

        localctx = metakit4_definition_stringParser.ViewContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_view)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            localctx.name = self.word()
            self.state = 26
            self.match(metakit4_definition_stringParser.SubFieldsStart)
            self.state = 27
            localctx.bodyF = self.body()
            self.state = 28
            self.match(metakit4_definition_stringParser.SubFieldsEnd)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScalarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # WordContext
            self.typeF = None # Token

        def Colon(self):
            return self.getToken(metakit4_definition_stringParser.Colon, 0)

        def word(self):
            return self.getTypedRuleContext(metakit4_definition_stringParser.WordContext,0)


        def TypeSpecifier(self):
            return self.getToken(metakit4_definition_stringParser.TypeSpecifier, 0)

        def getRuleIndex(self):
            return metakit4_definition_stringParser.RULE_scalar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScalar" ):
                listener.enterScalar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScalar" ):
                listener.exitScalar(self)




    def scalar(self):

        localctx = metakit4_definition_stringParser.ScalarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_scalar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            localctx.name = self.word()
            self.state = 31
            self.match(metakit4_definition_stringParser.Colon)
            self.state = 32
            localctx.typeF = self.match(metakit4_definition_stringParser.TypeSpecifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.subFieldsF = None # SubFieldsContext
            self.selfF = None # Token

        def subFields(self):
            return self.getTypedRuleContext(metakit4_definition_stringParser.SubFieldsContext,0)


        def IndirectMarker(self):
            return self.getToken(metakit4_definition_stringParser.IndirectMarker, 0)

        def getRuleIndex(self):
            return metakit4_definition_stringParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)




    def body(self):

        localctx = metakit4_definition_stringParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_body)
        try:
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                localctx.subFieldsF = self.subFields()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                localctx.selfF = self.match(metakit4_definition_stringParser.IndirectMarker)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rest_subFields_with_delFContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rest_subField_with_delF(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(metakit4_definition_stringParser.Rest_subField_with_delFContext)
            else:
                return self.getTypedRuleContext(metakit4_definition_stringParser.Rest_subField_with_delFContext,i)


        def getRuleIndex(self):
            return metakit4_definition_stringParser.RULE_rest_subFields_with_delF

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRest_subFields_with_delF" ):
                listener.enterRest_subFields_with_delF(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRest_subFields_with_delF" ):
                listener.exitRest_subFields_with_delF(self)




    def rest_subFields_with_delF(self):

        localctx = metakit4_definition_stringParser.Rest_subFields_with_delFContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_rest_subFields_with_delF)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 38
                self.rest_subField_with_delF()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rest_subField_with_delFContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.rest_subField = None # ScalarOrViewContext

        def OptionsSeparator(self):
            return self.getToken(metakit4_definition_stringParser.OptionsSeparator, 0)

        def scalarOrView(self):
            return self.getTypedRuleContext(metakit4_definition_stringParser.ScalarOrViewContext,0)


        def getRuleIndex(self):
            return metakit4_definition_stringParser.RULE_rest_subField_with_delF

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRest_subField_with_delF" ):
                listener.enterRest_subField_with_delF(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRest_subField_with_delF" ):
                listener.exitRest_subField_with_delF(self)




    def rest_subField_with_delF(self):

        localctx = metakit4_definition_stringParser.Rest_subField_with_delFContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_rest_subField_with_delF)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(metakit4_definition_stringParser.OptionsSeparator)
            self.state = 45
            localctx.rest_subField = self.scalarOrView()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def wordPiece(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(metakit4_definition_stringParser.WordPieceContext)
            else:
                return self.getTypedRuleContext(metakit4_definition_stringParser.WordPieceContext,i)


        def getRuleIndex(self):
            return metakit4_definition_stringParser.RULE_word

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWord" ):
                listener.enterWord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWord" ):
                listener.exitWord(self)




    def word(self):

        localctx = metakit4_definition_stringParser.WordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_word)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 47
                self.wordPiece()
                self.state = 50 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==6 or _la==10):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WordPieceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TypeSpecifier(self):
            return self.getToken(metakit4_definition_stringParser.TypeSpecifier, 0)

        def OtherWordChars(self, i:int=None):
            if i is None:
                return self.getTokens(metakit4_definition_stringParser.OtherWordChars)
            else:
                return self.getToken(metakit4_definition_stringParser.OtherWordChars, i)

        def getRuleIndex(self):
            return metakit4_definition_stringParser.RULE_wordPiece

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWordPiece" ):
                listener.enterWordPiece(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWordPiece" ):
                listener.exitWordPiece(self)




    def wordPiece(self):

        localctx = metakit4_definition_stringParser.WordPieceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_wordPiece)
        try:
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.match(metakit4_definition_stringParser.TypeSpecifier)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 54 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 53
                        self.match(metakit4_definition_stringParser.OtherWordChars)

                    else:
                        raise NoViableAltException(self)
                    self.state = 56 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





