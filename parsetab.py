
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'A BR CLIMB CONTENT CONTENT_STRING DIV DOC DOT H1 H2 H3 H4 H5 H6 HASH I IMG INT LI LINK L_PAREN META MULTIPLY P R_ANGLE R_CURLY R_PAREN SIBLING SPAN STRING TABLE TD TH TITLE TR UL\n    base :  expression \n         |  empty\n    \n    expression : expression MULTIPLY INT R_ANGLE expression\n    \n    expression : expression R_ANGLE expression\n               | expression SIBLING expression\n               | expression CLIMB expression\n               | expression DOT string\n               | expression HASH string\n               | expression CONTENT string\n               | expression MULTIPLY INT\n    \n    expression : DOT string\n               | HASH string\n    \n    expression : L_PAREN expression R_PAREN\n    \n    expression : NAME\n    \n    string : CONTENT_STRING\n            | STRING\n    \n    NAME : DIV\n        | SPAN\n        | P\n        | H1\n        | H2\n        | H3\n        | H4\n        | H5\n        | H6\n        | UL\n        | LI\n        | TABLE\n        | TH\n        | TD\n        | TR\n        | IMG\n        | BR\n        | LINK\n        | A\n        | META\n        | TITLE\n        | I\n        | DOC\n    \n    empty :\n    '
    
_lr_action_items = {'H1':([0,11,36,37,41,51,],[1,1,1,1,1,1,]),'H2':([0,11,36,37,41,51,],[2,2,2,2,2,2,]),'H3':([0,11,36,37,41,51,],[3,3,3,3,3,3,]),'H4':([0,11,36,37,41,51,],[4,4,4,4,4,4,]),'H5':([0,11,36,37,41,51,],[5,5,5,5,5,5,]),'H6':([0,11,36,37,41,51,],[17,17,17,17,17,17,]),'CONTENT_STRING':([21,23,38,39,42,],[32,32,32,32,32,]),'CONTENT':([1,2,3,4,5,6,8,9,10,12,13,14,15,17,18,19,20,22,24,25,26,27,28,29,30,31,32,33,34,35,43,44,45,46,47,48,49,50,52,],[-20,-21,-22,-23,-24,-18,-39,-36,-34,-17,-33,-37,-19,-25,-31,-32,-28,-35,-30,-27,-14,-38,-26,-29,38,38,-15,-16,-11,-12,-13,38,38,-9,-8,-10,38,-7,38,]),'LINK':([0,11,36,37,41,51,],[10,10,10,10,10,10,]),'DIV':([0,11,36,37,41,51,],[12,12,12,12,12,12,]),'IMG':([0,11,36,37,41,51,],[19,19,19,19,19,19,]),'STRING':([21,23,38,39,42,],[33,33,33,33,33,]),'L_PAREN':([0,11,36,37,41,51,],[11,11,11,11,11,11,]),'BR':([0,11,36,37,41,51,],[13,13,13,13,13,13,]),'R_ANGLE':([1,2,3,4,5,6,8,9,10,12,13,14,15,17,18,19,20,22,24,25,26,27,28,29,30,31,32,33,34,35,43,44,45,46,47,48,49,50,52,],[-20,-21,-22,-23,-24,-18,-39,-36,-34,-17,-33,-37,-19,-25,-31,-32,-28,-35,-30,-27,-14,-38,-26,-29,41,41,-15,-16,-11,-12,-13,41,41,-9,-8,51,41,-7,41,]),'TITLE':([0,11,36,37,41,51,],[14,14,14,14,14,14,]),'CLIMB':([1,2,3,4,5,6,8,9,10,12,13,14,15,17,18,19,20,22,24,25,26,27,28,29,30,31,32,33,34,35,43,44,45,46,47,48,49,50,52,],[-20,-21,-22,-23,-24,-18,-39,-36,-34,-17,-33,-37,-19,-25,-31,-32,-28,-35,-30,-27,-14,-38,-26,-29,36,36,-15,-16,-11,-12,-13,36,36,-9,-8,-10,36,-7,36,]),'P':([0,11,36,37,41,51,],[15,15,15,15,15,15,]),'SPAN':([0,11,36,37,41,51,],[6,6,6,6,6,6,]),'TR':([0,11,36,37,41,51,],[18,18,18,18,18,18,]),'META':([0,11,36,37,41,51,],[9,9,9,9,9,9,]),'MULTIPLY':([1,2,3,4,5,6,8,9,10,12,13,14,15,17,18,19,20,22,24,25,26,27,28,29,30,31,32,33,34,35,43,44,45,46,47,48,49,50,52,],[-20,-21,-22,-23,-24,-18,-39,-36,-34,-17,-33,-37,-19,-25,-31,-32,-28,-35,-30,-27,-14,-38,-26,-29,40,40,-15,-16,-11,-12,-13,40,40,-9,-8,-10,40,-7,40,]),'TABLE':([0,11,36,37,41,51,],[20,20,20,20,20,20,]),'DOT':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,17,18,19,20,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,41,43,44,45,46,47,48,49,50,51,52,],[21,-20,-21,-22,-23,-24,-18,-39,-36,-34,21,-17,-33,-37,-19,-25,-31,-32,-28,-35,-30,-27,-14,-38,-26,-29,42,42,-15,-16,-11,-12,21,21,21,-13,42,42,-9,-8,-10,42,-7,21,42,]),'R_PAREN':([1,2,3,4,5,6,8,9,10,12,13,14,15,17,18,19,20,22,24,25,26,27,28,29,31,32,33,34,35,43,44,45,46,47,48,49,50,52,],[-20,-21,-22,-23,-24,-18,-39,-36,-34,-17,-33,-37,-19,-25,-31,-32,-28,-35,-30,-27,-14,-38,-26,-29,43,-15,-16,-11,-12,-13,-6,-5,-9,-8,-10,-4,-7,-3,]),'HASH':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,17,18,19,20,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,41,43,44,45,46,47,48,49,50,51,52,],[23,-20,-21,-22,-23,-24,-18,-39,-36,-34,23,-17,-33,-37,-19,-25,-31,-32,-28,-35,-30,-27,-14,-38,-26,-29,39,39,-15,-16,-11,-12,23,23,23,-13,39,39,-9,-8,-10,39,-7,23,39,]),'TD':([0,11,36,37,41,51,],[24,24,24,24,24,24,]),'A':([0,11,36,37,41,51,],[22,22,22,22,22,22,]),'UL':([0,11,36,37,41,51,],[28,28,28,28,28,28,]),'SIBLING':([1,2,3,4,5,6,8,9,10,12,13,14,15,17,18,19,20,22,24,25,26,27,28,29,30,31,32,33,34,35,43,44,45,46,47,48,49,50,52,],[-20,-21,-22,-23,-24,-18,-39,-36,-34,-17,-33,-37,-19,-25,-31,-32,-28,-35,-30,-27,-14,-38,-26,-29,37,37,-15,-16,-11,-12,-13,37,37,-9,-8,-10,37,-7,37,]),'$end':([0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,22,24,25,26,27,28,29,30,32,33,34,35,43,44,45,46,47,48,49,50,52,],[-40,-20,-21,-22,-23,-24,-18,0,-39,-36,-34,-17,-33,-37,-19,-2,-25,-31,-32,-28,-35,-30,-27,-14,-38,-26,-29,-1,-15,-16,-11,-12,-13,-6,-5,-9,-8,-10,-4,-7,-3,]),'I':([0,11,36,37,41,51,],[27,27,27,27,27,27,]),'DOC':([0,11,36,37,41,51,],[8,8,8,8,8,8,]),'TH':([0,11,36,37,41,51,],[29,29,29,29,29,29,]),'INT':([40,],[48,]),'LI':([0,11,36,37,41,51,],[25,25,25,25,25,25,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'base':([0,],[7,]),'string':([21,23,38,39,42,],[34,35,46,47,50,]),'empty':([0,],[16,]),'expression':([0,11,36,37,41,51,],[30,31,44,45,49,52,]),'NAME':([0,11,36,37,41,51,],[26,26,26,26,26,26,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> base","S'",1,None,None,None),
  ('base -> expression','base',1,'p_base','plyparseCopy.py',15),
  ('base -> empty','base',1,'p_base','plyparseCopy.py',16),
  ('expression -> expression MULTIPLY INT R_ANGLE expression','expression',5,'p_special','plyparseCopy.py',26),
  ('expression -> expression R_ANGLE expression','expression',3,'p_expression_nonterminal','plyparseCopy.py',34),
  ('expression -> expression SIBLING expression','expression',3,'p_expression_nonterminal','plyparseCopy.py',35),
  ('expression -> expression CLIMB expression','expression',3,'p_expression_nonterminal','plyparseCopy.py',36),
  ('expression -> expression DOT string','expression',3,'p_expression_nonterminal','plyparseCopy.py',37),
  ('expression -> expression HASH string','expression',3,'p_expression_nonterminal','plyparseCopy.py',38),
  ('expression -> expression CONTENT string','expression',3,'p_expression_nonterminal','plyparseCopy.py',39),
  ('expression -> expression MULTIPLY INT','expression',3,'p_expression_nonterminal','plyparseCopy.py',40),
  ('expression -> DOT string','expression',2,'p_expression_onlyProperty','plyparseCopy.py',46),
  ('expression -> HASH string','expression',2,'p_expression_onlyProperty','plyparseCopy.py',47),
  ('expression -> L_PAREN expression R_PAREN','expression',3,'p_grouping','plyparseCopy.py',53),
  ('expression -> NAME','expression',1,'p_temp','plyparseCopy.py',59),
  ('string -> CONTENT_STRING','string',1,'p_string','plyparseCopy.py',65),
  ('string -> STRING','string',1,'p_string','plyparseCopy.py',66),
  ('NAME -> DIV','NAME',1,'p_expression_terminal','plyparseCopy.py',72),
  ('NAME -> SPAN','NAME',1,'p_expression_terminal','plyparseCopy.py',73),
  ('NAME -> P','NAME',1,'p_expression_terminal','plyparseCopy.py',74),
  ('NAME -> H1','NAME',1,'p_expression_terminal','plyparseCopy.py',75),
  ('NAME -> H2','NAME',1,'p_expression_terminal','plyparseCopy.py',76),
  ('NAME -> H3','NAME',1,'p_expression_terminal','plyparseCopy.py',77),
  ('NAME -> H4','NAME',1,'p_expression_terminal','plyparseCopy.py',78),
  ('NAME -> H5','NAME',1,'p_expression_terminal','plyparseCopy.py',79),
  ('NAME -> H6','NAME',1,'p_expression_terminal','plyparseCopy.py',80),
  ('NAME -> UL','NAME',1,'p_expression_terminal','plyparseCopy.py',81),
  ('NAME -> LI','NAME',1,'p_expression_terminal','plyparseCopy.py',82),
  ('NAME -> TABLE','NAME',1,'p_expression_terminal','plyparseCopy.py',83),
  ('NAME -> TH','NAME',1,'p_expression_terminal','plyparseCopy.py',84),
  ('NAME -> TD','NAME',1,'p_expression_terminal','plyparseCopy.py',85),
  ('NAME -> TR','NAME',1,'p_expression_terminal','plyparseCopy.py',86),
  ('NAME -> IMG','NAME',1,'p_expression_terminal','plyparseCopy.py',87),
  ('NAME -> BR','NAME',1,'p_expression_terminal','plyparseCopy.py',88),
  ('NAME -> LINK','NAME',1,'p_expression_terminal','plyparseCopy.py',89),
  ('NAME -> A','NAME',1,'p_expression_terminal','plyparseCopy.py',90),
  ('NAME -> META','NAME',1,'p_expression_terminal','plyparseCopy.py',91),
  ('NAME -> TITLE','NAME',1,'p_expression_terminal','plyparseCopy.py',92),
  ('NAME -> I','NAME',1,'p_expression_terminal','plyparseCopy.py',93),
  ('NAME -> DOC','NAME',1,'p_expression_terminal','plyparseCopy.py',94),
  ('empty -> <empty>','empty',0,'p_empty','plyparseCopy.py',101),
]
