
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'NOT AND OR START FINISH WORDS NUMBER LETTER PROCEDURE TOGGLE IF ENDIF DEFINE ENDDEFINE WHILE ENDWHILE ELSE BLOCKS ENDBLOCKS VARIABLES ENDVARIABLES PROGRAM ENDPROGRAM DISPLAY TRUE FALSE RETURN NONZEROINT GREATER LESSER EQUALITY ASSIGNATION PLUS MINUS MULTIPLICATION DIVISION NUMBERVALUE LETTERVALUE WORDSVALUE IDENTIFIER NEWLINE COMMA SEMICOLON OPARENTHESIS CPARENTHESIS OBRACKETS CBRACKETSsimple : PROGRAM program ENDPROGRAMempty :program : variables blocks mainvariables : VARIABLES declaration ENDVARIABLESvariables : emptydeclaration : variableType IDENTIFIER ASSIGNATION expression declarationExtra SEMICOLON declarationdeclaration : variableType IDENTIFIER OBRACKETS arrayIndexes CBRACKETS ASSIGNATION expression declarationExtra SEMICOLON declarationdeclaration : variableType IDENTIFIER declarationExtra SEMICOLON declarationdeclaration : emptydeclarationExtra : COMMA IDENTIFIER ASSIGNATION expression declarationExtradeclarationExtra : COMMA IDENTIFIER OBRACKETS arrayIndexes CBRACKETS ASSIGNATION expression declarationExtradeclarationExtra : COMMA IDENTIFIER declarationExtradeclarationExtra : COMMA IDENTIFIER OBRACKETS arrayIndexes CBRACKETS declarationExtradeclarationExtra : emptyarrayIndexes : NONZEROINT arrayIndexesExtraarrayIndexesExtra : COMMA NONZEROINT arrayIndexesExtraarrayIndexesExtra : emptyblocks : BLOCKS block ENDBLOCKSblocks : emptyblock : DEFINE blockType IDENTIFIER parameters variables statement ENDDEFINE blockblock : emptyblockType : PROCEDURE\n                  | variableTypevariableType : NUMBER \n                  | WORDS\n                  | LETTERparameters : OPARENTHESIS parameter CPARENTHESIS parameter : variableType IDENTIFIER parameterExtraparameter : emptyparameterExtra : COMMA variableType IDENTIFIER parameterExtraparameterExtra : emptystatement : emptyassign : location ASSIGNATION expressionlocation : IDENTIFIERlocation : expression OBRACKETS arrayIndexes CBRACKETScall : IDENTIFIER OPARENTHESIS actuals CPARENTHESISactuals : expression commaExpressionListcommaExpressionList : emptycommaExpression : COMMA expressionreturn : RETURN returnExpression SEMICOLONreturnExpression : expressionmain : START variables statement FINISH expression : expression PLUS termexpression : expression MINUS termexpression : termterm : term MULTIPLICATION factorterm : term DIVISION factorterm : factorfactor : NUMBERVALUE\n                  | NONZEROINT\n                  | WORDSVALUE\n                  | LETTERVALUEfactor : OPARENTHESIS expression CPARENTHESIS'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,7,],[0,-1,]),'VARIABLES':([2,18,50,81,],[5,5,5,-27,]),'BLOCKS':([2,4,6,22,],[-2,9,-5,-4,]),'START':([2,4,6,8,10,22,25,],[-2,-2,-5,18,-19,-4,-18,]),'ENDPROGRAM':([3,17,49,],[7,-3,-42,]),'NUMBER':([5,20,45,51,70,90,97,],[14,14,14,14,14,14,14,]),'WORDS':([5,20,45,51,70,90,97,],[15,15,15,15,15,15,15,]),'LETTER':([5,20,45,51,70,90,97,],[16,16,16,16,16,16,16,]),'ENDVARIABLES':([5,11,13,45,58,70,83,97,100,],[-2,22,-9,-2,-8,-2,-6,-2,-7,]),'FINISH':([6,18,22,24,34,35,],[-5,-2,-4,-2,49,-32,]),'ENDDEFINE':([6,22,35,50,66,80,81,],[-5,-4,-32,-2,-2,88,-27,]),'DEFINE':([9,88,],[20,20,]),'ENDBLOCKS':([9,19,21,88,95,],[-2,25,-21,-2,-20,]),'IDENTIFIER':([12,14,15,16,26,27,28,32,68,96,],[23,-24,-25,-26,36,-22,-23,48,82,99,]),'PROCEDURE':([20,],[27,]),'ASSIGNATION':([23,48,59,87,],[29,63,76,93,]),'OBRACKETS':([23,48,],[31,65,]),'COMMA':([23,37,38,39,40,41,42,43,47,48,71,72,73,74,75,77,78,82,84,87,98,99,],[32,32,-45,-48,-49,-50,-51,-52,61,32,-43,-44,-46,-47,-53,61,32,90,32,32,32,90,]),'SEMICOLON':([23,30,33,37,38,39,40,41,42,43,48,52,64,71,72,73,74,75,78,84,86,87,92,94,98,101,],[-2,45,-14,-2,-45,-48,-49,-50,-51,-52,-2,70,-12,-43,-44,-46,-47,-53,-2,-2,-10,-2,97,-13,-2,-11,]),'NUMBERVALUE':([29,44,53,54,55,56,63,76,93,],[40,40,40,40,40,40,40,40,40,]),'NONZEROINT':([29,31,44,53,54,55,56,61,63,65,76,93,],[41,47,41,41,41,41,41,77,41,47,41,41,]),'WORDSVALUE':([29,44,53,54,55,56,63,76,93,],[42,42,42,42,42,42,42,42,42,]),'LETTERVALUE':([29,44,53,54,55,56,63,76,93,],[43,43,43,43,43,43,43,43,43,]),'OPARENTHESIS':([29,36,44,53,54,55,56,63,76,93,],[44,51,44,44,44,44,44,44,44,44,]),'PLUS':([37,38,39,40,41,42,43,57,71,72,73,74,75,78,84,98,],[53,-45,-48,-49,-50,-51,-52,53,-43,-44,-46,-47,-53,53,53,53,]),'MINUS':([37,38,39,40,41,42,43,57,71,72,73,74,75,78,84,98,],[54,-45,-48,-49,-50,-51,-52,54,-43,-44,-46,-47,-53,54,54,54,]),'CPARENTHESIS':([38,39,40,41,42,43,51,57,67,69,71,72,73,74,75,82,89,91,99,102,],[-45,-48,-49,-50,-51,-52,-2,75,81,-29,-43,-44,-46,-47,-53,-2,-28,-31,-2,-30,]),'MULTIPLICATION':([38,39,40,41,42,43,71,72,73,74,75,],[55,-48,-49,-50,-51,-52,55,55,-46,-47,-53,]),'DIVISION':([38,39,40,41,42,43,71,72,73,74,75,],[56,-48,-49,-50,-51,-52,56,56,-46,-47,-53,]),'CBRACKETS':([46,47,60,62,77,79,85,],[59,-2,-15,-17,-2,87,-16,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'simple':([0,],[1,]),'program':([2,],[3,]),'variables':([2,18,50,],[4,24,66,]),'empty':([2,4,5,9,18,23,24,37,45,47,48,50,51,66,70,77,78,82,84,87,88,97,98,99,],[6,10,13,21,6,33,35,33,13,62,33,6,69,35,13,62,33,91,33,33,21,13,33,91,]),'blocks':([4,],[8,]),'declaration':([5,45,70,97,],[11,58,83,100,]),'variableType':([5,20,45,51,70,90,97,],[12,28,12,68,12,96,12,]),'main':([8,],[17,]),'block':([9,88,],[19,95,]),'blockType':([20,],[26,]),'declarationExtra':([23,37,48,78,84,87,98,],[30,52,64,86,92,94,101,]),'statement':([24,66,],[34,80,]),'expression':([29,44,63,76,93,],[37,57,78,84,98,]),'term':([29,44,53,54,63,76,93,],[38,38,71,72,38,38,38,]),'factor':([29,44,53,54,55,56,63,76,93,],[39,39,39,39,73,74,39,39,39,]),'arrayIndexes':([31,65,],[46,79,]),'parameters':([36,],[50,]),'arrayIndexesExtra':([47,77,],[60,85,]),'parameter':([51,],[67,]),'parameterExtra':([82,99,],[89,102,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> simple","S'",1,None,None,None),
  ('simple -> PROGRAM program ENDPROGRAM','simple',3,'p_simple','simpleParser.py',11),
  ('empty -> <empty>','empty',0,'p_empty','simpleParser.py',15),
  ('program -> variables blocks main','program',3,'p_program','simpleParser.py',19),
  ('variables -> VARIABLES declaration ENDVARIABLES','variables',3,'p_variables','simpleParser.py',23),
  ('variables -> empty','variables',1,'p_emptyVariables','simpleParser.py',27),
  ('declaration -> variableType IDENTIFIER ASSIGNATION expression declarationExtra SEMICOLON declaration','declaration',7,'p_declaration','simpleParser.py',31),
  ('declaration -> variableType IDENTIFIER OBRACKETS arrayIndexes CBRACKETS ASSIGNATION expression declarationExtra SEMICOLON declaration','declaration',10,'p_arrayDeclaration','simpleParser.py',35),
  ('declaration -> variableType IDENTIFIER declarationExtra SEMICOLON declaration','declaration',5,'p_nullDeclaration','simpleParser.py',39),
  ('declaration -> empty','declaration',1,'p_emptyDeclaration','simpleParser.py',43),
  ('declarationExtra -> COMMA IDENTIFIER ASSIGNATION expression declarationExtra','declarationExtra',5,'p_declarationExtra','simpleParser.py',47),
  ('declarationExtra -> COMMA IDENTIFIER OBRACKETS arrayIndexes CBRACKETS ASSIGNATION expression declarationExtra','declarationExtra',8,'p_arrayDeclarationExtra','simpleParser.py',51),
  ('declarationExtra -> COMMA IDENTIFIER declarationExtra','declarationExtra',3,'p_nullDeclarationExtra','simpleParser.py',55),
  ('declarationExtra -> COMMA IDENTIFIER OBRACKETS arrayIndexes CBRACKETS declarationExtra','declarationExtra',6,'p_array_nullDeclarationExtra','simpleParser.py',59),
  ('declarationExtra -> empty','declarationExtra',1,'p_emptyDeclarationExtra','simpleParser.py',63),
  ('arrayIndexes -> NONZEROINT arrayIndexesExtra','arrayIndexes',2,'p_arrayIndexes','simpleParser.py',67),
  ('arrayIndexesExtra -> COMMA NONZEROINT arrayIndexesExtra','arrayIndexesExtra',3,'p_arrayIndexesExtra','simpleParser.py',71),
  ('arrayIndexesExtra -> empty','arrayIndexesExtra',1,'p_emptyArrayIndexesExtra','simpleParser.py',75),
  ('blocks -> BLOCKS block ENDBLOCKS','blocks',3,'p_blocks','simpleParser.py',79),
  ('blocks -> empty','blocks',1,'p_emptyBlocks','simpleParser.py',83),
  ('block -> DEFINE blockType IDENTIFIER parameters variables statement ENDDEFINE block','block',8,'p_block','simpleParser.py',87),
  ('block -> empty','block',1,'p_emptyBlock','simpleParser.py',91),
  ('blockType -> PROCEDURE','blockType',1,'p_blockType','simpleParser.py',96),
  ('blockType -> variableType','blockType',1,'p_blockType','simpleParser.py',97),
  ('variableType -> NUMBER','variableType',1,'p_variableType','simpleParser.py',101),
  ('variableType -> WORDS','variableType',1,'p_variableType','simpleParser.py',102),
  ('variableType -> LETTER','variableType',1,'p_variableType','simpleParser.py',103),
  ('parameters -> OPARENTHESIS parameter CPARENTHESIS','parameters',3,'p_parameters','simpleParser.py',107),
  ('parameter -> variableType IDENTIFIER parameterExtra','parameter',3,'p_parameter','simpleParser.py',111),
  ('parameter -> empty','parameter',1,'p_emptyParameter','simpleParser.py',115),
  ('parameterExtra -> COMMA variableType IDENTIFIER parameterExtra','parameterExtra',4,'p_parameterExtra','simpleParser.py',119),
  ('parameterExtra -> empty','parameterExtra',1,'p_emptyParameterExtra','simpleParser.py',123),
  ('statement -> empty','statement',1,'p_statement','simpleParser.py',127),
  ('assign -> location ASSIGNATION expression','assign',3,'p_assign','simpleParser.py',137),
  ('location -> IDENTIFIER','location',1,'p_location','simpleParser.py',140),
  ('location -> expression OBRACKETS arrayIndexes CBRACKETS','location',4,'p_locationBracket','simpleParser.py',143),
  ('call -> IDENTIFIER OPARENTHESIS actuals CPARENTHESIS','call',4,'p_call','simpleParser.py',146),
  ('actuals -> expression commaExpressionList','actuals',2,'p_actuals','simpleParser.py',149),
  ('commaExpressionList -> empty','commaExpressionList',1,'p_commaExpressionList','simpleParser.py',155),
  ('commaExpression -> COMMA expression','commaExpression',2,'p_commaExpression','simpleParser.py',158),
  ('return -> RETURN returnExpression SEMICOLON','return',3,'p_return','simpleParser.py',161),
  ('returnExpression -> expression','returnExpression',1,'p_returnExpression','simpleParser.py',164),
  ('main -> START variables statement FINISH','main',4,'p_main','simpleParser.py',167),
  ('expression -> expression PLUS term','expression',3,'p_expressionPlus','simpleParser.py',171),
  ('expression -> expression MINUS term','expression',3,'p_expressionMinus','simpleParser.py',175),
  ('expression -> term','expression',1,'p_expressionTerm','simpleParser.py',179),
  ('term -> term MULTIPLICATION factor','term',3,'p_termTimes','simpleParser.py',183),
  ('term -> term DIVISION factor','term',3,'p_termDiv','simpleParser.py',187),
  ('term -> factor','term',1,'p_termFactor','simpleParser.py',191),
  ('factor -> NUMBERVALUE','factor',1,'p_factorNum','simpleParser.py',195),
  ('factor -> NONZEROINT','factor',1,'p_factorNum','simpleParser.py',196),
  ('factor -> WORDSVALUE','factor',1,'p_factorNum','simpleParser.py',197),
  ('factor -> LETTERVALUE','factor',1,'p_factorNum','simpleParser.py',198),
  ('factor -> OPARENTHESIS expression CPARENTHESIS','factor',3,'p_factorExpr','simpleParser.py',202),
]
