
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightASSIGNATIONleftORleftANDleftEQUALITYleftGREATERLESSERleftPLUSMINUSleftMULTIPLICATIONDIVISIONMODULUSrightNOTNOT AND OR START FINISH WORDS NUMBER MANYNUMBERS LETTER PROCEDURE FLAG IF ENDIF DEFINE ENDDEFINE WHILE ENDWHILE ELSE BLOCKS ENDBLOCKS VARIABLES ENDVARIABLES PROGRAM ENDPROGRAM DISPLAY RETURN GREATER LESSER EQUALITY ASSIGNATION PLUS MINUS MULTIPLICATION DIVISION MODULUS NUMBERVALUE FLAGVALUE LETTERVALUE WORDSVALUE IDENTIFIER NEWLINE COMMA SEMICOLON OPARENTHESIS CPARENTHESIS OBRACKETS CBRACKETSsimple : PROGRAM program ENDPROGRAMempty :program : variables blocks mainvariables : VARIABLES declarationList ENDVARIABLESvariables : emptydeclarationList : declaration declarationListdeclarationList : emptydeclaration : variableType IDENTIFIER ASSIGNATION expression declarationExtra SEMICOLONdeclaration : arrayType IDENTIFIER OBRACKETS arrayIndexes CBRACKETS ASSIGNATION expression arrayDeclarationExtra SEMICOLONdeclaration : variableType IDENTIFIER declarationExtra SEMICOLONdeclaration : arrayType IDENTIFIER OBRACKETS arrayIndexes CBRACKETS arrayDeclarationExtra SEMICOLONdeclaration : emptydeclarationExtra : COMMA IDENTIFIER ASSIGNATION expression declarationExtraarrayDeclarationExtra : COMMA IDENTIFIER OBRACKETS arrayIndexes CBRACKETS ASSIGNATION expression arrayDeclarationExtradeclarationExtra : COMMA IDENTIFIER declarationExtraarrayDeclarationExtra : COMMA IDENTIFIER OBRACKETS arrayIndexes CBRACKETS arrayDeclarationExtradeclarationExtra : emptyarrayDeclarationExtra : emptyarrayIndexes : NUMBERVALUE arrayIndexesExtraarrayIndexesExtra : COMMA NUMBERVALUE arrayIndexesExtraarrayIndexesExtra : emptyblocks : BLOCKS blockList ENDBLOCKSblocks : emptyblockList : block blockListblockList : emptyblock : DEFINE blockType IDENTIFIER parameters variables statementPoint ENDDEFINEblock : emptyblockType : PROCEDURE\n                  | variableType\n                  | arrayTypevariableType : NUMBER \n                  | WORDS\n                  | LETTER\n                  | FLAGarrayType : MANYNUMBERSparameters : OPARENTHESIS parameter CPARENTHESISparameter : variableType IDENTIFIER parameterExtraparameter : emptyparameterExtra : COMMA variableType IDENTIFIER parameterExtraparameterExtra : emptystatementPoint : statementListstatementList : statement statementListstatementList : emptystatement : assign SEMICOLON \n                   | call SEMICOLON \n                   | return  empty \n                   | ifStatement empty \n                   | whileStatement emptystatement : emptyassign : location ASSIGNATION expression location : IDENTIFIERlocation : IDENTIFIER OBRACKETS arrayIndexes CBRACKETSlocation : callcall : IDENTIFIER OPARENTHESIS actuals CPARENTHESISactuals : expression commaExpressionListcommaExpressionList : commaExpression commaExpressionListcommaExpressionList : emptycommaExpression : COMMA expressionreturn : RETURN returnExpression SEMICOLONreturnExpression : expressionreturnExpression : emptyifStatement : IF OPARENTHESIS expression CPARENTHESIS statementPoint elseStatement ENDIFelseStatement : ELSE statementPointelseStatement : emptywhileStatement : WHILE OPARENTHESIS expression CPARENTHESIS statementPoint ENDWHILEmain : START variables statementPoint FINISH expression : locationexpression : unaryExpressionexpression : binaryExpressionexpression : FLAGVALUE\n                  | NUMBERVALUE\n                  | WORDSVALUE\n                  | LETTERVALUEexpression : OPARENTHESIS expression CPARENTHESISbinaryExpression : expression OR expressionbinaryExpression : expression AND expressionbinaryExpression : expression LESSER expressionbinaryExpression : expression GREATER expressionbinaryExpression : expression EQUALITY expressionbinaryExpression : expression PLUS expressionbinaryExpression : expression MINUS expressionbinaryExpression : expression MULTIPLICATION expressionbinaryExpression : expression DIVISION expressionbinaryExpression : expression MODULUS expressionunaryExpression : NOT expression'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,7,],[0,-1,]),'VARIABLES':([2,22,89,148,],[5,5,5,-36,]),'BLOCKS':([2,4,6,27,],[-2,9,-5,-4,]),'START':([2,4,6,8,10,27,32,],[-2,-2,-5,22,-23,-4,-22,]),'ENDPROGRAM':([3,21,74,],[7,-3,-66,]),'ENDVARIABLES':([5,11,12,13,28,70,121,152,170,],[-2,27,-2,-7,-6,-10,-8,-11,-9,]),'NUMBER':([5,12,13,26,70,90,121,152,161,170,],[16,16,-12,16,-10,16,-8,-11,16,-9,]),'WORDS':([5,12,13,26,70,90,121,152,161,170,],[17,17,-12,17,-10,17,-8,-11,17,-9,]),'LETTER':([5,12,13,26,70,90,121,152,161,170,],[18,18,-12,18,-10,18,-8,-11,18,-9,]),'FLAG':([5,12,13,26,70,90,121,152,161,170,],[19,19,-12,19,-10,19,-8,-11,19,-9,]),'MANYNUMBERS':([5,12,13,26,70,121,152,170,],[20,20,-12,20,-10,-8,-11,-9,]),'IDENTIFIER':([6,14,15,16,17,18,19,20,22,27,31,34,35,36,37,38,40,45,46,49,50,51,54,67,69,76,77,78,79,80,81,82,87,88,89,92,93,94,95,96,97,98,99,100,101,104,114,117,119,134,136,143,145,146,148,166,168,169,172,177,],[-5,29,30,-31,-32,-33,-34,-35,-2,-4,53,57,-28,-29,-30,58,71,53,-49,-2,-2,-2,58,58,58,-44,-45,-46,-47,-48,58,58,58,58,-2,58,58,58,58,58,58,58,58,58,58,58,-59,53,149,58,153,58,53,53,-36,53,-65,174,-62,58,]),'RETURN':([6,22,27,31,45,46,49,50,51,76,77,78,79,80,89,114,117,145,146,148,166,168,172,],[-5,-2,-4,54,54,-49,-2,-2,-2,-44,-45,-46,-47,-48,-2,-59,54,54,54,-36,54,-65,-62,]),'IF':([6,22,27,31,45,46,49,50,51,76,77,78,79,80,89,114,117,145,146,148,166,168,172,],[-5,-2,-4,55,55,-49,-2,-2,-2,-44,-45,-46,-47,-48,-2,-59,55,55,55,-36,55,-65,-62,]),'WHILE':([6,22,27,31,45,46,49,50,51,76,77,78,79,80,89,114,117,145,146,148,166,168,172,],[-5,-2,-4,56,56,-49,-2,-2,-2,-44,-45,-46,-47,-48,-2,-59,56,56,56,-36,56,-65,-62,]),'FINISH':([6,22,27,31,43,44,45,46,49,50,51,75,76,77,78,79,80,114,168,172,],[-5,-2,-4,-2,74,-41,-2,-43,-2,-2,-2,-42,-44,-45,-46,-47,-48,-59,-65,-62,]),'ENDDEFINE':([6,27,44,45,46,49,50,51,75,76,77,78,79,80,89,114,117,147,148,168,172,],[-5,-4,-41,-2,-43,-2,-2,-2,-42,-44,-45,-46,-47,-48,-2,-59,-2,159,-36,-65,-62,]),'DEFINE':([9,24,25,159,],[26,26,-27,-26,]),'ENDBLOCKS':([9,23,24,25,33,159,],[-2,32,-2,-25,-24,-26,]),'PROCEDURE':([26,],[35,]),'ASSIGNATION':([29,48,52,53,71,106,139,144,175,],[38,-53,81,-51,104,134,-54,-52,177,]),'COMMA':([29,58,59,60,61,62,63,64,65,66,68,71,73,103,106,112,122,123,124,125,126,127,128,129,130,131,132,133,138,139,141,144,149,151,156,174,175,179,],[40,-51,40,-67,-68,-69,-70,-71,-72,-73,-53,40,108,-85,136,143,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-74,40,108,-54,143,-52,161,136,-58,161,136,136,]),'SEMICOLON':([29,39,41,47,48,54,58,59,60,61,62,63,64,65,66,68,71,84,85,86,91,103,105,106,110,122,123,124,125,126,127,128,129,130,131,132,133,135,137,139,144,150,151,163,175,178,179,180,],[-2,70,-17,76,77,-2,-51,-2,-67,-68,-69,-70,-71,-72,-73,-53,-2,114,-60,-61,121,-85,-15,-2,-50,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-74,-2,152,-18,-54,-52,-13,-2,170,-2,-16,-2,-14,]),'OBRACKETS':([30,53,58,153,],[42,83,83,164,]),'FLAGVALUE':([38,54,67,69,81,82,87,88,92,93,94,95,96,97,98,99,100,101,104,134,143,177,],[63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,]),'NUMBERVALUE':([38,42,54,67,69,81,82,83,87,88,92,93,94,95,96,97,98,99,100,101,104,108,134,143,164,177,],[64,73,64,64,64,64,64,73,64,64,64,64,64,64,64,64,64,64,64,64,64,138,64,64,73,64,]),'WORDSVALUE':([38,54,67,69,81,82,87,88,92,93,94,95,96,97,98,99,100,101,104,134,143,177,],[65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,]),'LETTERVALUE':([38,54,67,69,81,82,87,88,92,93,94,95,96,97,98,99,100,101,104,134,143,177,],[66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,]),'OPARENTHESIS':([38,53,54,55,56,57,58,67,69,81,82,87,88,92,93,94,95,96,97,98,99,100,101,104,134,143,177,],[67,82,67,87,88,90,82,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,]),'NOT':([38,54,67,69,81,82,87,88,92,93,94,95,96,97,98,99,100,101,104,134,143,177,],[69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,]),'ELSE':([44,45,46,49,50,51,75,76,77,78,79,80,114,145,157,168,172,],[-41,-2,-43,-2,-2,-2,-42,-44,-45,-46,-47,-48,-59,-2,166,-65,-62,]),'ENDIF':([44,45,46,49,50,51,75,76,77,78,79,80,114,145,157,165,166,167,168,172,173,],[-41,-2,-43,-2,-2,-2,-42,-44,-45,-46,-47,-48,-59,-2,-2,172,-2,-64,-65,-62,-63,]),'ENDWHILE':([44,45,46,49,50,51,75,76,77,78,79,80,114,146,158,168,172,],[-41,-2,-43,-2,-2,-2,-42,-44,-45,-46,-47,-48,-59,-2,168,-65,-62,]),'OR':([58,59,60,61,62,63,64,65,66,68,85,102,103,110,112,115,116,122,123,124,125,126,127,128,129,130,131,132,133,139,144,151,156,179,],[-51,92,-67,-68,-69,-70,-71,-72,-73,-53,92,92,-85,92,92,92,92,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-74,92,-54,-52,92,92,92,]),'AND':([58,59,60,61,62,63,64,65,66,68,85,102,103,110,112,115,116,122,123,124,125,126,127,128,129,130,131,132,133,139,144,151,156,179,],[-51,93,-67,-68,-69,-70,-71,-72,-73,-53,93,93,-85,93,93,93,93,93,-76,-77,-78,-79,-80,-81,-82,-83,-84,-74,93,-54,-52,93,93,93,]),'LESSER':([58,59,60,61,62,63,64,65,66,68,85,102,103,110,112,115,116,122,123,124,125,126,127,128,129,130,131,132,133,139,144,151,156,179,],[-51,94,-67,-68,-69,-70,-71,-72,-73,-53,94,94,-85,94,94,94,94,94,94,-77,-78,94,-80,-81,-82,-83,-84,-74,94,-54,-52,94,94,94,]),'GREATER':([58,59,60,61,62,63,64,65,66,68,85,102,103,110,112,115,116,122,123,124,125,126,127,128,129,130,131,132,133,139,144,151,156,179,],[-51,95,-67,-68,-69,-70,-71,-72,-73,-53,95,95,-85,95,95,95,95,95,95,-77,-78,95,-80,-81,-82,-83,-84,-74,95,-54,-52,95,95,95,]),'EQUALITY':([58,59,60,61,62,63,64,65,66,68,85,102,103,110,112,115,116,122,123,124,125,126,127,128,129,130,131,132,133,139,144,151,156,179,],[-51,96,-67,-68,-69,-70,-71,-72,-73,-53,96,96,-85,96,96,96,96,96,96,-77,-78,-79,-80,-81,-82,-83,-84,-74,96,-54,-52,96,96,96,]),'PLUS':([58,59,60,61,62,63,64,65,66,68,85,102,103,110,112,115,116,122,123,124,125,126,127,128,129,130,131,132,133,139,144,151,156,179,],[-51,97,-67,-68,-69,-70,-71,-72,-73,-53,97,97,-85,97,97,97,97,97,97,97,97,97,-80,-81,-82,-83,-84,-74,97,-54,-52,97,97,97,]),'MINUS':([58,59,60,61,62,63,64,65,66,68,85,102,103,110,112,115,116,122,123,124,125,126,127,128,129,130,131,132,133,139,144,151,156,179,],[-51,98,-67,-68,-69,-70,-71,-72,-73,-53,98,98,-85,98,98,98,98,98,98,98,98,98,-80,-81,-82,-83,-84,-74,98,-54,-52,98,98,98,]),'MULTIPLICATION':([58,59,60,61,62,63,64,65,66,68,85,102,103,110,112,115,116,122,123,124,125,126,127,128,129,130,131,132,133,139,144,151,156,179,],[-51,99,-67,-68,-69,-70,-71,-72,-73,-53,99,99,-85,99,99,99,99,99,99,99,99,99,99,99,-82,-83,-84,-74,99,-54,-52,99,99,99,]),'DIVISION':([58,59,60,61,62,63,64,65,66,68,85,102,103,110,112,115,116,122,123,124,125,126,127,128,129,130,131,132,133,139,144,151,156,179,],[-51,100,-67,-68,-69,-70,-71,-72,-73,-53,100,100,-85,100,100,100,100,100,100,100,100,100,100,100,-82,-83,-84,-74,100,-54,-52,100,100,100,]),'MODULUS':([58,59,60,61,62,63,64,65,66,68,85,102,103,110,112,115,116,122,123,124,125,126,127,128,129,130,131,132,133,139,144,151,156,179,],[-51,101,-67,-68,-69,-70,-71,-72,-73,-53,101,101,-85,101,101,101,101,101,101,101,101,101,101,101,-82,-83,-84,-74,101,-54,-52,101,101,101,]),'CPARENTHESIS':([58,60,61,62,63,64,65,66,68,90,102,103,111,112,115,116,118,120,122,123,124,125,126,127,128,129,130,131,132,139,140,141,142,144,149,155,156,160,162,174,176,],[-51,-67,-68,-69,-70,-71,-72,-73,-53,-2,132,-85,139,-2,145,146,148,-38,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-74,-54,-55,-2,-57,-52,-2,-56,-58,-37,-40,-2,-39,]),'CBRACKETS':([72,73,107,109,113,138,154,171,],[106,-2,-19,-21,144,-2,-20,175,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'simple':([0,],[1,]),'program':([2,],[3,]),'variables':([2,22,89,],[4,31,117,]),'empty':([2,4,5,9,12,22,24,29,31,45,49,50,51,54,59,71,73,89,90,106,112,117,133,138,141,145,146,149,151,157,166,174,175,179,],[6,10,13,25,13,6,25,41,46,46,78,79,80,86,41,41,109,6,120,137,142,46,41,109,142,46,46,162,137,167,46,162,137,137,]),'blocks':([4,],[8,]),'declarationList':([5,12,],[11,28,]),'declaration':([5,12,],[12,12,]),'variableType':([5,12,26,90,161,],[14,14,36,119,169,]),'arrayType':([5,12,26,],[15,15,37,]),'main':([8,],[21,]),'blockList':([9,24,],[23,33,]),'block':([9,24,],[24,24,]),'blockType':([26,],[34,]),'declarationExtra':([29,59,71,133,],[39,91,105,150,]),'statementPoint':([31,117,145,146,166,],[43,147,157,158,173,]),'statementList':([31,45,117,145,146,166,],[44,75,44,44,44,44,]),'statement':([31,45,117,145,146,166,],[45,45,45,45,45,45,]),'assign':([31,45,117,145,146,166,],[47,47,47,47,47,47,]),'call':([31,38,45,54,67,69,81,82,87,88,92,93,94,95,96,97,98,99,100,101,104,117,134,143,145,146,166,177,],[48,68,48,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,48,68,68,48,48,48,68,]),'return':([31,45,117,145,146,166,],[49,49,49,49,49,49,]),'ifStatement':([31,45,117,145,146,166,],[50,50,50,50,50,50,]),'whileStatement':([31,45,117,145,146,166,],[51,51,51,51,51,51,]),'location':([31,38,45,54,67,69,81,82,87,88,92,93,94,95,96,97,98,99,100,101,104,117,134,143,145,146,166,177,],[52,60,52,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,52,60,60,52,52,52,60,]),'expression':([38,54,67,69,81,82,87,88,92,93,94,95,96,97,98,99,100,101,104,134,143,177,],[59,85,102,103,110,112,115,116,122,123,124,125,126,127,128,129,130,131,133,151,156,179,]),'unaryExpression':([38,54,67,69,81,82,87,88,92,93,94,95,96,97,98,99,100,101,104,134,143,177,],[61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,]),'binaryExpression':([38,54,67,69,81,82,87,88,92,93,94,95,96,97,98,99,100,101,104,134,143,177,],[62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,]),'arrayIndexes':([42,83,164,],[72,113,171,]),'returnExpression':([54,],[84,]),'parameters':([57,],[89,]),'arrayIndexesExtra':([73,138,],[107,154,]),'actuals':([82,],[111,]),'parameter':([90,],[118,]),'arrayDeclarationExtra':([106,151,175,179,],[135,163,178,180,]),'commaExpressionList':([112,141,],[140,155,]),'commaExpression':([112,141,],[141,141,]),'parameterExtra':([149,174,],[160,176,]),'elseStatement':([157,],[165,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> simple","S'",1,None,None,None),
  ('simple -> PROGRAM program ENDPROGRAM','simple',3,'p_simple','simpleParser.py',32),
  ('empty -> <empty>','empty',0,'p_empty','simpleParser.py',37),
  ('program -> variables blocks main','program',3,'p_program','simpleParser.py',41),
  ('variables -> VARIABLES declarationList ENDVARIABLES','variables',3,'p_variables','simpleParser.py',47),
  ('variables -> empty','variables',1,'p_emptyVariables','simpleParser.py',54),
  ('declarationList -> declaration declarationList','declarationList',2,'p_declarationList','simpleParser.py',59),
  ('declarationList -> empty','declarationList',1,'p_emptyDeclarationList','simpleParser.py',64),
  ('declaration -> variableType IDENTIFIER ASSIGNATION expression declarationExtra SEMICOLON','declaration',6,'p_declaration','simpleParser.py',70),
  ('declaration -> arrayType IDENTIFIER OBRACKETS arrayIndexes CBRACKETS ASSIGNATION expression arrayDeclarationExtra SEMICOLON','declaration',9,'p_arrayDeclaration','simpleParser.py',84),
  ('declaration -> variableType IDENTIFIER declarationExtra SEMICOLON','declaration',4,'p_nullDeclaration','simpleParser.py',98),
  ('declaration -> arrayType IDENTIFIER OBRACKETS arrayIndexes CBRACKETS arrayDeclarationExtra SEMICOLON','declaration',7,'p_arrayNullDeclaration','simpleParser.py',109),
  ('declaration -> empty','declaration',1,'p_emptyDeclaration','simpleParser.py',123),
  ('declarationExtra -> COMMA IDENTIFIER ASSIGNATION expression declarationExtra','declarationExtra',5,'p_declarationExtra','simpleParser.py',128),
  ('arrayDeclarationExtra -> COMMA IDENTIFIER OBRACKETS arrayIndexes CBRACKETS ASSIGNATION expression arrayDeclarationExtra','arrayDeclarationExtra',8,'p_arrayDeclarationExtra','simpleParser.py',138),
  ('declarationExtra -> COMMA IDENTIFIER declarationExtra','declarationExtra',3,'p_nullDeclarationExtra','simpleParser.py',148),
  ('arrayDeclarationExtra -> COMMA IDENTIFIER OBRACKETS arrayIndexes CBRACKETS arrayDeclarationExtra','arrayDeclarationExtra',6,'p_arrayNullDeclarationExtra','simpleParser.py',159),
  ('declarationExtra -> empty','declarationExtra',1,'p_emptyDeclarationExtra','simpleParser.py',170),
  ('arrayDeclarationExtra -> empty','arrayDeclarationExtra',1,'p_emptyArrayDeclarationExtra','simpleParser.py',175),
  ('arrayIndexes -> NUMBERVALUE arrayIndexesExtra','arrayIndexes',2,'p_arrayIndexes','simpleParser.py',180),
  ('arrayIndexesExtra -> COMMA NUMBERVALUE arrayIndexesExtra','arrayIndexesExtra',3,'p_arrayIndexesExtra','simpleParser.py',185),
  ('arrayIndexesExtra -> empty','arrayIndexesExtra',1,'p_emptyArrayIndexesExtra','simpleParser.py',189),
  ('blocks -> BLOCKS blockList ENDBLOCKS','blocks',3,'p_blocks','simpleParser.py',194),
  ('blocks -> empty','blocks',1,'p_emptyBlocks','simpleParser.py',201),
  ('blockList -> block blockList','blockList',2,'p_blockList','simpleParser.py',206),
  ('blockList -> empty','blockList',1,'p_emptyBlockList','simpleParser.py',210),
  ('block -> DEFINE blockType IDENTIFIER parameters variables statementPoint ENDDEFINE','block',7,'p_block','simpleParser.py',214),
  ('block -> empty','block',1,'p_emptyBlock','simpleParser.py',222),
  ('blockType -> PROCEDURE','blockType',1,'p_blockType','simpleParser.py',228),
  ('blockType -> variableType','blockType',1,'p_blockType','simpleParser.py',229),
  ('blockType -> arrayType','blockType',1,'p_blockType','simpleParser.py',230),
  ('variableType -> NUMBER','variableType',1,'p_variableType','simpleParser.py',236),
  ('variableType -> WORDS','variableType',1,'p_variableType','simpleParser.py',237),
  ('variableType -> LETTER','variableType',1,'p_variableType','simpleParser.py',238),
  ('variableType -> FLAG','variableType',1,'p_variableType','simpleParser.py',239),
  ('arrayType -> MANYNUMBERS','arrayType',1,'p_arrayType','simpleParser.py',246),
  ('parameters -> OPARENTHESIS parameter CPARENTHESIS','parameters',3,'p_parameters','simpleParser.py',253),
  ('parameter -> variableType IDENTIFIER parameterExtra','parameter',3,'p_parameter','simpleParser.py',257),
  ('parameter -> empty','parameter',1,'p_emptyParameter','simpleParser.py',261),
  ('parameterExtra -> COMMA variableType IDENTIFIER parameterExtra','parameterExtra',4,'p_parameterExtra','simpleParser.py',266),
  ('parameterExtra -> empty','parameterExtra',1,'p_emptyParameterExtra','simpleParser.py',270),
  ('statementPoint -> statementList','statementPoint',1,'p_statementPoint','simpleParser.py',275),
  ('statementList -> statement statementList','statementList',2,'p_statementList','simpleParser.py',281),
  ('statementList -> empty','statementList',1,'p_emptyStatementList','simpleParser.py',284),
  ('statement -> assign SEMICOLON','statement',2,'p_statement','simpleParser.py',289),
  ('statement -> call SEMICOLON','statement',2,'p_statement','simpleParser.py',290),
  ('statement -> return empty','statement',2,'p_statement','simpleParser.py',291),
  ('statement -> ifStatement empty','statement',2,'p_statement','simpleParser.py',292),
  ('statement -> whileStatement empty','statement',2,'p_statement','simpleParser.py',293),
  ('statement -> empty','statement',1,'p_emptyStatement','simpleParser.py',298),
  ('assign -> location ASSIGNATION expression','assign',3,'p_assign','simpleParser.py',303),
  ('location -> IDENTIFIER','location',1,'p_location','simpleParser.py',312),
  ('location -> IDENTIFIER OBRACKETS arrayIndexes CBRACKETS','location',4,'p_locationBracket','simpleParser.py',316),
  ('location -> call','location',1,'p_locationCall','simpleParser.py',320),
  ('call -> IDENTIFIER OPARENTHESIS actuals CPARENTHESIS','call',4,'p_call','simpleParser.py',324),
  ('actuals -> expression commaExpressionList','actuals',2,'p_actuals','simpleParser.py',328),
  ('commaExpressionList -> commaExpression commaExpressionList','commaExpressionList',2,'p_commaExpressionList','simpleParser.py',332),
  ('commaExpressionList -> empty','commaExpressionList',1,'p_emptyCommaExpressionList','simpleParser.py',336),
  ('commaExpression -> COMMA expression','commaExpression',2,'p_commaExpression','simpleParser.py',341),
  ('return -> RETURN returnExpression SEMICOLON','return',3,'p_return','simpleParser.py',345),
  ('returnExpression -> expression','returnExpression',1,'p_returnExpression','simpleParser.py',349),
  ('returnExpression -> empty','returnExpression',1,'p_emptyReturnExpression','simpleParser.py',353),
  ('ifStatement -> IF OPARENTHESIS expression CPARENTHESIS statementPoint elseStatement ENDIF','ifStatement',7,'p_ifStatement','simpleParser.py',358),
  ('elseStatement -> ELSE statementPoint','elseStatement',2,'p_elseStatement','simpleParser.py',365),
  ('elseStatement -> empty','elseStatement',1,'p_emptyElseStatement','simpleParser.py',374),
  ('whileStatement -> WHILE OPARENTHESIS expression CPARENTHESIS statementPoint ENDWHILE','whileStatement',6,'p_whileStatement','simpleParser.py',383),
  ('main -> START variables statementPoint FINISH','main',4,'p_main','simpleParser.py',387),
  ('expression -> location','expression',1,'p_expressionLocation','simpleParser.py',392),
  ('expression -> unaryExpression','expression',1,'p_expressionUnary','simpleParser.py',397),
  ('expression -> binaryExpression','expression',1,'p_expressionBinary','simpleParser.py',402),
  ('expression -> FLAGVALUE','expression',1,'p_expressionTokens','simpleParser.py',407),
  ('expression -> NUMBERVALUE','expression',1,'p_expressionTokens','simpleParser.py',408),
  ('expression -> WORDSVALUE','expression',1,'p_expressionTokens','simpleParser.py',409),
  ('expression -> LETTERVALUE','expression',1,'p_expressionTokens','simpleParser.py',410),
  ('expression -> OPARENTHESIS expression CPARENTHESIS','expression',3,'p_parentesisExpression','simpleParser.py',415),
  ('binaryExpression -> expression OR expression','binaryExpression',3,'p_binaryExpressionOr','simpleParser.py',419),
  ('binaryExpression -> expression AND expression','binaryExpression',3,'p_binaryExpressionAnd','simpleParser.py',423),
  ('binaryExpression -> expression LESSER expression','binaryExpression',3,'p_binaryExpressionLessThan','simpleParser.py',427),
  ('binaryExpression -> expression GREATER expression','binaryExpression',3,'p_binaryExpressionGreaterThan','simpleParser.py',431),
  ('binaryExpression -> expression EQUALITY expression','binaryExpression',3,'p_binaryExpressionEquality','simpleParser.py',435),
  ('binaryExpression -> expression PLUS expression','binaryExpression',3,'p_binaryExpressionPlus','simpleParser.py',439),
  ('binaryExpression -> expression MINUS expression','binaryExpression',3,'p_binaryExpressionMinus','simpleParser.py',446),
  ('binaryExpression -> expression MULTIPLICATION expression','binaryExpression',3,'p_binaryExpressionMultiplication','simpleParser.py',450),
  ('binaryExpression -> expression DIVISION expression','binaryExpression',3,'p_binaryExpressionDivision','simpleParser.py',456),
  ('binaryExpression -> expression MODULUS expression','binaryExpression',3,'p_binaryExpressionModulus','simpleParser.py',460),
  ('unaryExpression -> NOT expression','unaryExpression',2,'p_unaryExpressionNOT','simpleParser.py',464),
]
