
# _parser_Parser_parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEleftEXPrightUMINUSUPLUSCOMMA DIVIDE EXP FLOAT INTEGER LBRACKET LPAREN MINUS NAME PERIOD PLUS RBRACKET RPAREN STRING TIMESstatement : expression\n        expression : expression PLUS expression\n                   | expression MINUS expression\n                   | expression TIMES expression\n                   | expression DIVIDE expression\n                   | expression EXP expression\n        expression : MINUS expression %prec UMINUSexpression : PLUS expression %prec UPLUSexpression : term\n        term : atom\n             | attraccess\n             | functioncall\n             | indexing\n        \n        atom : INTEGER\n             | FLOAT\n             | STRING\n             | global\n             | group\n        global : NAMEgroup : LPAREN expression RPARENattraccess : atom PERIOD NAMEindexing : atom LBRACKET expression RBRACKET\n        functioncall : atom LPAREN RPAREN\n                     | atom LPAREN arglist RPAREN\n        \n        arglist : arglist COMMA expression\n                | expression\n        '
    
_lr_action_items = {'MINUS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,25,26,27,28,29,30,31,32,33,34,36,37,38,39,40,41,42,],[4,18,4,4,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,4,4,4,4,4,4,-8,-7,4,4,18,-2,-3,-4,-5,-6,-21,-23,18,18,-20,-24,4,-22,18,]),'PLUS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,25,26,27,28,29,30,31,32,33,34,36,37,38,39,40,41,42,],[3,17,3,3,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,3,3,3,3,3,3,-8,-7,3,3,17,-2,-3,-4,-5,-6,-21,-23,17,17,-20,-24,3,-22,17,]),'INTEGER':([0,3,4,16,17,18,19,20,21,25,26,40,],[10,10,10,10,10,10,10,10,10,10,10,10,]),'FLOAT':([0,3,4,16,17,18,19,20,21,25,26,40,],[11,11,11,11,11,11,11,11,11,11,11,11,]),'STRING':([0,3,4,16,17,18,19,20,21,25,26,40,],[12,12,12,12,12,12,12,12,12,12,12,12,]),'NAME':([0,3,4,16,17,18,19,20,21,24,25,26,40,],[15,15,15,15,15,15,15,15,15,33,15,15,15,]),'LPAREN':([0,3,4,6,10,11,12,13,14,15,16,17,18,19,20,21,25,26,38,40,],[16,16,16,25,-14,-15,-16,-17,-18,-19,16,16,16,16,16,16,16,16,-20,16,]),'$end':([1,2,5,6,7,8,9,10,11,12,13,14,15,22,23,28,29,30,31,32,33,34,38,39,41,],[0,-1,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-8,-7,-2,-3,-4,-5,-6,-21,-23,-20,-24,-22,]),'TIMES':([2,5,6,7,8,9,10,11,12,13,14,15,22,23,27,28,29,30,31,32,33,34,36,37,38,39,41,42,],[19,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-8,-7,19,19,19,-4,-5,-6,-21,-23,19,19,-20,-24,-22,19,]),'DIVIDE':([2,5,6,7,8,9,10,11,12,13,14,15,22,23,27,28,29,30,31,32,33,34,36,37,38,39,41,42,],[20,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-8,-7,20,20,20,-4,-5,-6,-21,-23,20,20,-20,-24,-22,20,]),'EXP':([2,5,6,7,8,9,10,11,12,13,14,15,22,23,27,28,29,30,31,32,33,34,36,37,38,39,41,42,],[21,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-8,-7,21,21,21,21,21,-6,-21,-23,21,21,-20,-24,-22,21,]),'RPAREN':([5,6,7,8,9,10,11,12,13,14,15,22,23,25,27,28,29,30,31,32,33,34,35,36,38,39,41,42,],[-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-8,-7,34,38,-2,-3,-4,-5,-6,-21,-23,39,-26,-20,-24,-22,-25,]),'COMMA':([5,6,7,8,9,10,11,12,13,14,15,22,23,28,29,30,31,32,33,34,35,36,38,39,41,42,],[-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-8,-7,-2,-3,-4,-5,-6,-21,-23,40,-26,-20,-24,-22,-25,]),'RBRACKET':([5,6,7,8,9,10,11,12,13,14,15,22,23,28,29,30,31,32,33,34,37,38,39,41,],[-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-8,-7,-2,-3,-4,-5,-6,-21,-23,41,-20,-24,-22,]),'PERIOD':([6,10,11,12,13,14,15,38,],[24,-14,-15,-16,-17,-18,-19,-20,]),'LBRACKET':([6,10,11,12,13,14,15,38,],[26,-14,-15,-16,-17,-18,-19,-20,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([0,3,4,16,17,18,19,20,21,25,26,40,],[2,22,23,27,28,29,30,31,32,36,37,42,]),'term':([0,3,4,16,17,18,19,20,21,25,26,40,],[5,5,5,5,5,5,5,5,5,5,5,5,]),'atom':([0,3,4,16,17,18,19,20,21,25,26,40,],[6,6,6,6,6,6,6,6,6,6,6,6,]),'attraccess':([0,3,4,16,17,18,19,20,21,25,26,40,],[7,7,7,7,7,7,7,7,7,7,7,7,]),'functioncall':([0,3,4,16,17,18,19,20,21,25,26,40,],[8,8,8,8,8,8,8,8,8,8,8,8,]),'indexing':([0,3,4,16,17,18,19,20,21,25,26,40,],[9,9,9,9,9,9,9,9,9,9,9,9,]),'global':([0,3,4,16,17,18,19,20,21,25,26,40,],[13,13,13,13,13,13,13,13,13,13,13,13,]),'group':([0,3,4,16,17,18,19,20,21,25,26,40,],[14,14,14,14,14,14,14,14,14,14,14,14,]),'arglist':([25,],[35,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> expression','statement',1,'p_statement_expr','_parser.py',118),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','_parser.py',123),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','_parser.py',124),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','_parser.py',125),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','_parser.py',126),
  ('expression -> expression EXP expression','expression',3,'p_expression_binop','_parser.py',127),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','_parser.py',142),
  ('expression -> PLUS expression','expression',2,'p_expression_uplus','_parser.py',146),
  ('expression -> term','expression',1,'p_expression_term','_parser.py',150),
  ('term -> atom','term',1,'p_term','_parser.py',155),
  ('term -> attraccess','term',1,'p_term','_parser.py',156),
  ('term -> functioncall','term',1,'p_term','_parser.py',157),
  ('term -> indexing','term',1,'p_term','_parser.py',158),
  ('atom -> INTEGER','atom',1,'p_atom','_parser.py',164),
  ('atom -> FLOAT','atom',1,'p_atom','_parser.py',165),
  ('atom -> STRING','atom',1,'p_atom','_parser.py',166),
  ('atom -> global','atom',1,'p_atom','_parser.py',167),
  ('atom -> group','atom',1,'p_atom','_parser.py',168),
  ('global -> NAME','global',1,'p_global','_parser.py',173),
  ('group -> LPAREN expression RPAREN','group',3,'p_group','_parser.py',177),
  ('attraccess -> atom PERIOD NAME','attraccess',3,'p_attraccess','_parser.py',181),
  ('indexing -> atom LBRACKET expression RBRACKET','indexing',4,'p_indexing','_parser.py',185),
  ('functioncall -> atom LPAREN RPAREN','functioncall',3,'p_functioncall','_parser.py',190),
  ('functioncall -> atom LPAREN arglist RPAREN','functioncall',4,'p_functioncall','_parser.py',191),
  ('arglist -> arglist COMMA expression','arglist',3,'p_arglist','_parser.py',202),
  ('arglist -> expression','arglist',1,'p_arglist','_parser.py',203),
]
