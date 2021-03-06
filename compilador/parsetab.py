
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'programAND CHAR COLON COMMA CTE_F CTE_I DIFFERENT DIVIDE DO ELSE EQUAL EQUALS FLOAT FOR FUNC GREATER_THAN ID IF INT LEFT_BR LEFT_CURL LEFT_PAR LESS_THAN MAIN MINUS MORE MULTIPLY OR PLUS PROGRAM READ RETURN RIGHT_BR RIGHT_CURL RIGHT_PAR SEMICOLON STR THEN TO VAR VD VOID WHILE WRITE\n  program : PROGRAM ID COLON main\n          | PROGRAM ID COLON variables main\n          | PROGRAM ID COLON variables funciones main\n          | PROGRAM ID COLON funciones main  \n  \n  main : MAIN LEFT_PAR RIGHT_PAR LEFT_CURL main_aux RIGHT_CURL\n\n  \n  main_aux : estatutos_main_multiple\n           | empty\n  \n  variables : VAR SEMICOLON\n            | VAR variables_aux SEMICOLON\n  \n  variables_aux : tipo COLON dec_var\n                | tipo COLON dec_var MORE variables_aux\n  \n  tipo : INT\n      | FLOAT\n      | CHAR\n  \n  dec_var : dec_varaux COMMA dec_var\n          | dec_varaux\n  \n  dec_varaux : ID\n              | ID LEFT_BR CTE_I RIGHT_BR\n              | ID LEFT_BR CTE_I RIGHT_BR LEFT_BR CTE_I RIGHT_BR\n  \n  funciones : funciones_aux\n            | funciones_aux funciones\n  \n  \n    funciones_aux : tipo FUNC ID LEFT_PAR parametros RIGHT_PAR LEFT_CURL variables estatutos RIGHT_CURL\n             | tipo FUNC ID LEFT_PAR RIGHT_PAR LEFT_CURL variables estatutos RIGHT_CURL\n             | VOID FUNC ID LEFT_PAR RIGHT_PAR LEFT_CURL variables estatutos RIGHT_CURL\n             | VOID FUNC ID LEFT_PAR parametros RIGHT_PAR LEFT_CURL variables estatutos RIGHT_CURL\n  \n  parametros : dec_var_param COMMA parametros\n              | dec_var_param\n\n  \n\tdec_var_param : tipo ID\n\t\n  expresion : exp\n              | exp relacionales expresion\n\t\t\t\t\t\t\t| exp logicos expresion\n              | LEFT_PAR expresion RIGHT_PAR \n              | LEFT_PAR expresion RIGHT_PAR relacionales expresion\n              | LEFT_PAR expresion RIGHT_PAR logicos expresion\n\n  \n  logicos : AND \n          | OR\n  \n  relacionales : LESS_THAN\n                  | GREATER_THAN\n                  | DIFFERENT\n                  | EQUAL\n  \n  estatutos : estatutos_main_aux \n            | retorno SEMICOLON \n\n  \n  estatutos_main : asignacion SEMICOLON\n                  | llamada SEMICOLON\n                  | lectura SEMICOLON\n                  | escritura SEMICOLON\n                  | decision SEMICOLON\n                  | repeticion SEMICOLON\n  \n  estatutos_main_multiple : estatutos_main estatutos_main_multiple\n                    | estatutos_main\n  \n  estatutos_main_aux : estatutos_main estatutos\n                      | estatutos_main\n\n  \n  asignacion : dec_varaux EQUALS exp\n  \n  exp : termino exp_aux \n      | termino\n  \n  exp_aux : PLUS exp\n          | MINUS exp\n  \n  termino : factor\n          | factor termino_aux\n  \n  termino_aux : MULTIPLY termino\n              | DIVIDE termino\n  \n  factor : cte\n          | LEFT_PAR exp RIGHT_PAR\n          | ID LEFT_PAR dec_var RIGHT_PAR\n          | ID LEFT_PAR RIGHT_PAR\n  \n    llamada : VD ID LEFT_PAR RIGHT_PAR\n            | VD ID LEFT_PAR dec_var RIGHT_PAR\n  \n    retorno : RETURN LEFT_PAR exp RIGHT_PAR\n  \n  lectura : READ LEFT_PAR dec_var RIGHT_PAR\n  \n  escritura : WRITE LEFT_PAR escritura_aux RIGHT_PAR\n  \n  escritura_aux : STR\n                | exp\n                | STR COMMA escritura_aux\n                | exp COMMA escritura_aux\n  \n  decision : IF LEFT_PAR expresion RIGHT_PAR THEN LEFT_CURL estatutos RIGHT_CURL \n            | IF LEFT_PAR expresion RIGHT_PAR THEN LEFT_CURL estatutos RIGHT_CURL ELSE LEFT_CURL estatutos RIGHT_CURL\n  \n  repeticion : condicional\n              | no_condicional\n  \n  no_condicional : FOR LEFT_PAR dec_varaux EQUALS exp TO exp RIGHT_PAR DO LEFT_CURL estatutos RIGHT_CURL\n  \n  condicional : WHILE LEFT_PAR expresion RIGHT_PAR DO LEFT_CURL estatutos RIGHT_CURL\n  \n  cte : ID \n      | CTE_I\n      | CTE_F \n  \n  empty : \n  '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,5,16,18,26,66,],[0,-1,-2,-4,-3,-5,]),'ID':([2,13,14,15,20,24,25,28,29,32,41,49,58,60,68,69,70,71,72,73,74,76,77,78,79,80,94,98,103,110,112,115,116,118,119,121,126,127,131,132,133,134,135,136,137,138,140,142,146,149,171,175,176,177,178,179,195,196,],[3,-12,-13,-14,-8,30,31,-9,35,35,35,75,35,84,-43,-44,-45,-46,-47,-48,95,35,95,95,95,35,95,35,95,35,35,95,95,95,95,35,95,95,95,95,-37,-38,-39,-40,-35,-36,95,35,35,35,95,95,95,35,35,95,35,35,]),'COLON':([3,13,14,15,22,],[4,-12,-13,-14,29,]),'MAIN':([4,6,7,10,17,20,23,28,168,172,181,183,],[8,8,8,-20,8,-8,-21,-9,-23,-24,-22,-25,]),'VAR':([4,86,88,109,113,],[9,9,9,9,9,]),'VOID':([4,6,10,20,28,168,172,181,183,],[12,12,12,-8,-9,-23,-24,-22,-25,]),'INT':([4,6,9,10,20,28,36,37,57,87,168,172,181,183,],[13,13,13,13,-8,-9,13,13,13,13,-23,-24,-22,-25,]),'FLOAT':([4,6,9,10,20,28,36,37,57,87,168,172,181,183,],[14,14,14,14,-8,-9,14,14,14,14,-23,-24,-22,-25,]),'CHAR':([4,6,9,10,20,28,36,37,57,87,168,172,181,183,],[15,15,15,15,-8,-9,15,15,15,15,-23,-24,-22,-25,]),'LEFT_PAR':([8,30,31,50,51,52,55,56,74,75,77,78,79,94,95,103,115,116,118,119,126,127,131,132,133,134,135,136,137,138,140,147,171,175,176,179,],[19,36,37,76,77,78,79,80,94,98,94,103,103,94,121,103,94,94,94,94,94,94,103,103,-37,-38,-39,-40,-35,-36,94,171,94,103,103,94,]),'SEMICOLON':([9,21,33,34,35,42,43,44,45,46,47,53,54,81,82,90,91,92,93,95,96,97,108,114,117,122,124,125,145,150,151,152,153,154,156,157,174,180,189,190,191,199,200,],[20,28,-10,-16,-17,68,69,70,71,72,73,-77,-78,-11,-15,-53,-55,-58,-62,-81,-82,-83,-18,-54,-59,-66,-69,-70,169,-56,-57,-60,-61,-63,-65,-67,-64,-19,-68,-75,-80,-76,-79,]),'FUNC':([11,12,13,14,15,],[24,25,-12,-13,-14,]),'RIGHT_PAR':([19,34,35,36,37,61,63,65,82,84,91,92,93,95,96,97,98,99,100,101,102,104,105,106,108,111,114,117,120,121,123,128,129,150,151,152,153,154,155,156,158,159,160,162,163,174,180,182,184,185,188,],[27,-16,-17,62,64,85,-27,89,-15,-28,-55,-58,-62,-81,-82,-83,122,124,125,-71,-72,130,-29,139,-18,-26,-54,-59,154,156,157,160,154,-56,-57,-60,-61,-63,174,-65,-73,-74,-32,-30,-31,-64,-19,189,-33,-34,192,]),'RETURN':([20,28,68,69,70,71,72,73,110,112,142,146,149,177,178,195,196,],[-8,-9,-43,-44,-45,-46,-47,-48,147,147,147,147,147,147,147,147,147,]),'VD':([20,28,32,41,68,69,70,71,72,73,110,112,142,146,149,177,178,195,196,],[-8,-9,49,49,-43,-44,-45,-46,-47,-48,49,49,49,49,49,49,49,49,49,]),'READ':([20,28,32,41,68,69,70,71,72,73,110,112,142,146,149,177,178,195,196,],[-8,-9,50,50,-43,-44,-45,-46,-47,-48,50,50,50,50,50,50,50,50,50,]),'WRITE':([20,28,32,41,68,69,70,71,72,73,110,112,142,146,149,177,178,195,196,],[-8,-9,51,51,-43,-44,-45,-46,-47,-48,51,51,51,51,51,51,51,51,51,]),'IF':([20,28,32,41,68,69,70,71,72,73,110,112,142,146,149,177,178,195,196,],[-8,-9,52,52,-43,-44,-45,-46,-47,-48,52,52,52,52,52,52,52,52,52,]),'WHILE':([20,28,32,41,68,69,70,71,72,73,110,112,142,146,149,177,178,195,196,],[-8,-9,55,55,-43,-44,-45,-46,-47,-48,55,55,55,55,55,55,55,55,55,]),'FOR':([20,28,32,41,68,69,70,71,72,73,110,112,142,146,149,177,178,195,196,],[-8,-9,56,56,-43,-44,-45,-46,-47,-48,56,56,56,56,56,56,56,56,56,]),'LEFT_CURL':([27,62,64,85,89,161,164,193,194,],[32,86,88,109,113,177,178,195,196,]),'RIGHT_CURL':([32,38,39,40,41,67,68,69,70,71,72,73,143,144,146,148,167,169,170,173,186,187,197,198,],[-84,66,-6,-7,-50,-49,-43,-44,-45,-46,-47,-48,168,-41,-52,172,181,-42,-51,183,190,191,199,200,]),'MORE':([33,34,35,82,108,180,],[57,-16,-17,-15,-18,-19,]),'COMMA':([34,35,63,84,91,92,93,95,96,97,101,102,108,114,117,150,151,152,153,154,156,174,180,],[58,-17,87,-28,-55,-58,-62,-81,-82,-83,126,127,-18,-54,-59,-56,-57,-60,-61,-63,-65,-64,-19,]),'EQUALS':([35,48,107,108,180,],[-17,74,140,-18,-19,]),'LEFT_BR':([35,108,],[59,141,]),'CTE_I':([59,74,77,78,79,94,103,115,116,118,119,126,127,131,132,133,134,135,136,137,138,140,141,171,175,176,179,],[83,96,96,96,96,96,96,96,96,96,96,96,96,96,96,-37,-38,-39,-40,-35,-36,96,166,96,96,96,96,]),'CTE_F':([74,77,78,79,94,103,115,116,118,119,126,127,131,132,133,134,135,136,137,138,140,171,175,176,179,],[97,97,97,97,97,97,97,97,97,97,97,97,97,97,-37,-38,-39,-40,-35,-36,97,97,97,97,97,]),'STR':([77,126,127,],[101,101,101,]),'RIGHT_BR':([83,166,],[108,180,]),'LESS_THAN':([91,92,93,95,96,97,105,114,117,129,150,151,152,153,154,156,160,174,],[-55,-58,-62,-81,-82,-83,133,-54,-59,133,-56,-57,-60,-61,-63,-65,133,-64,]),'GREATER_THAN':([91,92,93,95,96,97,105,114,117,129,150,151,152,153,154,156,160,174,],[-55,-58,-62,-81,-82,-83,134,-54,-59,134,-56,-57,-60,-61,-63,-65,134,-64,]),'DIFFERENT':([91,92,93,95,96,97,105,114,117,129,150,151,152,153,154,156,160,174,],[-55,-58,-62,-81,-82,-83,135,-54,-59,135,-56,-57,-60,-61,-63,-65,135,-64,]),'EQUAL':([91,92,93,95,96,97,105,114,117,129,150,151,152,153,154,156,160,174,],[-55,-58,-62,-81,-82,-83,136,-54,-59,136,-56,-57,-60,-61,-63,-65,136,-64,]),'AND':([91,92,93,95,96,97,105,114,117,129,150,151,152,153,154,156,160,174,],[-55,-58,-62,-81,-82,-83,137,-54,-59,137,-56,-57,-60,-61,-63,-65,137,-64,]),'OR':([91,92,93,95,96,97,105,114,117,129,150,151,152,153,154,156,160,174,],[-55,-58,-62,-81,-82,-83,138,-54,-59,138,-56,-57,-60,-61,-63,-65,138,-64,]),'TO':([91,92,93,95,96,97,114,117,150,151,152,153,154,156,165,174,],[-55,-58,-62,-81,-82,-83,-54,-59,-56,-57,-60,-61,-63,-65,179,-64,]),'PLUS':([91,92,93,95,96,97,117,152,153,154,156,174,],[115,-58,-62,-81,-82,-83,-59,-60,-61,-63,-65,-64,]),'MINUS':([91,92,93,95,96,97,117,152,153,154,156,174,],[116,-58,-62,-81,-82,-83,-59,-60,-61,-63,-65,-64,]),'MULTIPLY':([92,93,95,96,97,154,156,174,],[118,-62,-81,-82,-83,-63,-65,-64,]),'DIVIDE':([92,93,95,96,97,154,156,174,],[119,-62,-81,-82,-83,-63,-65,-64,]),'THEN':([130,],[161,]),'DO':([139,192,],[164,194,]),'ELSE':([190,],[193,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'main':([4,6,7,17,],[5,16,18,26,]),'variables':([4,86,88,109,113,],[6,110,112,142,149,]),'funciones':([4,6,10,],[7,17,23,]),'funciones_aux':([4,6,10,],[10,10,10,]),'tipo':([4,6,9,10,36,37,57,87,],[11,11,22,11,60,60,22,60,]),'variables_aux':([9,57,],[21,81,]),'dec_var':([29,58,76,98,121,],[33,82,99,123,155,]),'dec_varaux':([29,32,41,58,76,80,98,110,112,121,142,146,149,177,178,195,196,],[34,48,48,34,34,107,34,48,48,34,48,48,48,48,48,48,48,]),'main_aux':([32,],[38,]),'estatutos_main_multiple':([32,41,],[39,67,]),'empty':([32,],[40,]),'estatutos_main':([32,41,110,112,142,146,149,177,178,195,196,],[41,41,146,146,146,146,146,146,146,146,146,]),'asignacion':([32,41,110,112,142,146,149,177,178,195,196,],[42,42,42,42,42,42,42,42,42,42,42,]),'llamada':([32,41,110,112,142,146,149,177,178,195,196,],[43,43,43,43,43,43,43,43,43,43,43,]),'lectura':([32,41,110,112,142,146,149,177,178,195,196,],[44,44,44,44,44,44,44,44,44,44,44,]),'escritura':([32,41,110,112,142,146,149,177,178,195,196,],[45,45,45,45,45,45,45,45,45,45,45,]),'decision':([32,41,110,112,142,146,149,177,178,195,196,],[46,46,46,46,46,46,46,46,46,46,46,]),'repeticion':([32,41,110,112,142,146,149,177,178,195,196,],[47,47,47,47,47,47,47,47,47,47,47,]),'condicional':([32,41,110,112,142,146,149,177,178,195,196,],[53,53,53,53,53,53,53,53,53,53,53,]),'no_condicional':([32,41,110,112,142,146,149,177,178,195,196,],[54,54,54,54,54,54,54,54,54,54,54,]),'parametros':([36,37,87,],[61,65,111,]),'dec_var_param':([36,37,87,],[63,63,63,]),'exp':([74,77,78,79,94,103,115,116,126,127,131,132,140,171,175,176,179,],[90,102,105,105,120,129,150,151,102,102,105,105,165,182,105,105,188,]),'termino':([74,77,78,79,94,103,115,116,118,119,126,127,131,132,140,171,175,176,179,],[91,91,91,91,91,91,91,91,152,153,91,91,91,91,91,91,91,91,91,]),'factor':([74,77,78,79,94,103,115,116,118,119,126,127,131,132,140,171,175,176,179,],[92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,]),'cte':([74,77,78,79,94,103,115,116,118,119,126,127,131,132,140,171,175,176,179,],[93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,]),'escritura_aux':([77,126,127,],[100,158,159,]),'expresion':([78,79,103,131,132,175,176,],[104,106,128,162,163,184,185,]),'exp_aux':([91,],[114,]),'termino_aux':([92,],[117,]),'relacionales':([105,129,160,],[131,131,175,]),'logicos':([105,129,160,],[132,132,176,]),'estatutos':([110,112,142,146,149,177,178,195,196,],[143,148,167,170,173,186,187,197,198,]),'estatutos_main_aux':([110,112,142,146,149,177,178,195,196,],[144,144,144,144,144,144,144,144,144,]),'retorno':([110,112,142,146,149,177,178,195,196,],[145,145,145,145,145,145,145,145,145,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID COLON main','program',4,'p_program','lexer.py',88),
  ('program -> PROGRAM ID COLON variables main','program',5,'p_program','lexer.py',89),
  ('program -> PROGRAM ID COLON variables funciones main','program',6,'p_program','lexer.py',90),
  ('program -> PROGRAM ID COLON funciones main','program',5,'p_program','lexer.py',91),
  ('main -> MAIN LEFT_PAR RIGHT_PAR LEFT_CURL main_aux RIGHT_CURL','main',6,'p_main','lexer.py',97),
  ('main_aux -> estatutos_main_multiple','main_aux',1,'p_main_aux','lexer.py',103),
  ('main_aux -> empty','main_aux',1,'p_main_aux','lexer.py',104),
  ('variables -> VAR SEMICOLON','variables',2,'p_variables','lexer.py',109),
  ('variables -> VAR variables_aux SEMICOLON','variables',3,'p_variables','lexer.py',110),
  ('variables_aux -> tipo COLON dec_var','variables_aux',3,'p_variables_aux','lexer.py',115),
  ('variables_aux -> tipo COLON dec_var MORE variables_aux','variables_aux',5,'p_variables_aux','lexer.py',116),
  ('tipo -> INT','tipo',1,'p_tipo','lexer.py',121),
  ('tipo -> FLOAT','tipo',1,'p_tipo','lexer.py',122),
  ('tipo -> CHAR','tipo',1,'p_tipo','lexer.py',123),
  ('dec_var -> dec_varaux COMMA dec_var','dec_var',3,'p_dec_var','lexer.py',128),
  ('dec_var -> dec_varaux','dec_var',1,'p_dec_var','lexer.py',129),
  ('dec_varaux -> ID','dec_varaux',1,'p_dec_varaux','lexer.py',134),
  ('dec_varaux -> ID LEFT_BR CTE_I RIGHT_BR','dec_varaux',4,'p_dec_varaux','lexer.py',135),
  ('dec_varaux -> ID LEFT_BR CTE_I RIGHT_BR LEFT_BR CTE_I RIGHT_BR','dec_varaux',7,'p_dec_varaux','lexer.py',136),
  ('funciones -> funciones_aux','funciones',1,'p_funciones','lexer.py',141),
  ('funciones -> funciones_aux funciones','funciones',2,'p_funciones','lexer.py',142),
  ('funciones_aux -> tipo FUNC ID LEFT_PAR parametros RIGHT_PAR LEFT_CURL variables estatutos RIGHT_CURL','funciones_aux',10,'p_funciones_aux','lexer.py',148),
  ('funciones_aux -> tipo FUNC ID LEFT_PAR RIGHT_PAR LEFT_CURL variables estatutos RIGHT_CURL','funciones_aux',9,'p_funciones_aux','lexer.py',149),
  ('funciones_aux -> VOID FUNC ID LEFT_PAR RIGHT_PAR LEFT_CURL variables estatutos RIGHT_CURL','funciones_aux',9,'p_funciones_aux','lexer.py',150),
  ('funciones_aux -> VOID FUNC ID LEFT_PAR parametros RIGHT_PAR LEFT_CURL variables estatutos RIGHT_CURL','funciones_aux',10,'p_funciones_aux','lexer.py',151),
  ('parametros -> dec_var_param COMMA parametros','parametros',3,'p_parametros','lexer.py',156),
  ('parametros -> dec_var_param','parametros',1,'p_parametros','lexer.py',157),
  ('dec_var_param -> tipo ID','dec_var_param',2,'p_dec_var_param','lexer.py',163),
  ('expresion -> exp','expresion',1,'p_expresion','lexer.py',169),
  ('expresion -> exp relacionales expresion','expresion',3,'p_expresion','lexer.py',170),
  ('expresion -> exp logicos expresion','expresion',3,'p_expresion','lexer.py',171),
  ('expresion -> LEFT_PAR expresion RIGHT_PAR','expresion',3,'p_expresion','lexer.py',172),
  ('expresion -> LEFT_PAR expresion RIGHT_PAR relacionales expresion','expresion',5,'p_expresion','lexer.py',173),
  ('expresion -> LEFT_PAR expresion RIGHT_PAR logicos expresion','expresion',5,'p_expresion','lexer.py',174),
  ('logicos -> AND','logicos',1,'p_logicos','lexer.py',180),
  ('logicos -> OR','logicos',1,'p_logicos','lexer.py',181),
  ('relacionales -> LESS_THAN','relacionales',1,'p_relacionales','lexer.py',187),
  ('relacionales -> GREATER_THAN','relacionales',1,'p_relacionales','lexer.py',188),
  ('relacionales -> DIFFERENT','relacionales',1,'p_relacionales','lexer.py',189),
  ('relacionales -> EQUAL','relacionales',1,'p_relacionales','lexer.py',190),
  ('estatutos -> estatutos_main_aux','estatutos',1,'p_estatutos','lexer.py',195),
  ('estatutos -> retorno SEMICOLON','estatutos',2,'p_estatutos','lexer.py',196),
  ('estatutos_main -> asignacion SEMICOLON','estatutos_main',2,'p_estatutos_main','lexer.py',202),
  ('estatutos_main -> llamada SEMICOLON','estatutos_main',2,'p_estatutos_main','lexer.py',203),
  ('estatutos_main -> lectura SEMICOLON','estatutos_main',2,'p_estatutos_main','lexer.py',204),
  ('estatutos_main -> escritura SEMICOLON','estatutos_main',2,'p_estatutos_main','lexer.py',205),
  ('estatutos_main -> decision SEMICOLON','estatutos_main',2,'p_estatutos_main','lexer.py',206),
  ('estatutos_main -> repeticion SEMICOLON','estatutos_main',2,'p_estatutos_main','lexer.py',207),
  ('estatutos_main_multiple -> estatutos_main estatutos_main_multiple','estatutos_main_multiple',2,'p_estatutos_main_multiple','lexer.py',212),
  ('estatutos_main_multiple -> estatutos_main','estatutos_main_multiple',1,'p_estatutos_main_multiple','lexer.py',213),
  ('estatutos_main_aux -> estatutos_main estatutos','estatutos_main_aux',2,'p_estatutos_main_aux','lexer.py',218),
  ('estatutos_main_aux -> estatutos_main','estatutos_main_aux',1,'p_estatutos_main_aux','lexer.py',219),
  ('asignacion -> dec_varaux EQUALS exp','asignacion',3,'p_asignacion','lexer.py',225),
  ('exp -> termino exp_aux','exp',2,'p_exp','lexer.py',231),
  ('exp -> termino','exp',1,'p_exp','lexer.py',232),
  ('exp_aux -> PLUS exp','exp_aux',2,'p_exp_aux','lexer.py',237),
  ('exp_aux -> MINUS exp','exp_aux',2,'p_exp_aux','lexer.py',238),
  ('termino -> factor','termino',1,'p_termino','lexer.py',243),
  ('termino -> factor termino_aux','termino',2,'p_termino','lexer.py',244),
  ('termino_aux -> MULTIPLY termino','termino_aux',2,'p_termino_aux','lexer.py',249),
  ('termino_aux -> DIVIDE termino','termino_aux',2,'p_termino_aux','lexer.py',250),
  ('factor -> cte','factor',1,'p_factor','lexer.py',255),
  ('factor -> LEFT_PAR exp RIGHT_PAR','factor',3,'p_factor','lexer.py',256),
  ('factor -> ID LEFT_PAR dec_var RIGHT_PAR','factor',4,'p_factor','lexer.py',257),
  ('factor -> ID LEFT_PAR RIGHT_PAR','factor',3,'p_factor','lexer.py',258),
  ('llamada -> VD ID LEFT_PAR RIGHT_PAR','llamada',4,'p_llamada','lexer.py',263),
  ('llamada -> VD ID LEFT_PAR dec_var RIGHT_PAR','llamada',5,'p_llamada','lexer.py',264),
  ('retorno -> RETURN LEFT_PAR exp RIGHT_PAR','retorno',4,'p_retorno','lexer.py',269),
  ('lectura -> READ LEFT_PAR dec_var RIGHT_PAR','lectura',4,'p_lectura','lexer.py',274),
  ('escritura -> WRITE LEFT_PAR escritura_aux RIGHT_PAR','escritura',4,'p_escritura','lexer.py',279),
  ('escritura_aux -> STR','escritura_aux',1,'p_escritura_aux','lexer.py',284),
  ('escritura_aux -> exp','escritura_aux',1,'p_escritura_aux','lexer.py',285),
  ('escritura_aux -> STR COMMA escritura_aux','escritura_aux',3,'p_escritura_aux','lexer.py',286),
  ('escritura_aux -> exp COMMA escritura_aux','escritura_aux',3,'p_escritura_aux','lexer.py',287),
  ('decision -> IF LEFT_PAR expresion RIGHT_PAR THEN LEFT_CURL estatutos RIGHT_CURL','decision',8,'p_decision','lexer.py',292),
  ('decision -> IF LEFT_PAR expresion RIGHT_PAR THEN LEFT_CURL estatutos RIGHT_CURL ELSE LEFT_CURL estatutos RIGHT_CURL','decision',12,'p_decision','lexer.py',293),
  ('repeticion -> condicional','repeticion',1,'p_repeticion','lexer.py',298),
  ('repeticion -> no_condicional','repeticion',1,'p_repeticion','lexer.py',299),
  ('no_condicional -> FOR LEFT_PAR dec_varaux EQUALS exp TO exp RIGHT_PAR DO LEFT_CURL estatutos RIGHT_CURL','no_condicional',12,'p_no_condicional','lexer.py',304),
  ('condicional -> WHILE LEFT_PAR expresion RIGHT_PAR DO LEFT_CURL estatutos RIGHT_CURL','condicional',8,'p_condicional','lexer.py',309),
  ('cte -> ID','cte',1,'p_cte','lexer.py',313),
  ('cte -> CTE_I','cte',1,'p_cte','lexer.py',314),
  ('cte -> CTE_F','cte',1,'p_cte','lexer.py',315),
  ('empty -> <empty>','empty',0,'p_empty','lexer.py',324),
]
