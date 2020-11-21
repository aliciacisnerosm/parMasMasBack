
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'programAND CHAR COLON COMMA CTE_CHAR CTE_I DIFFERENT DIVIDE DO DOT ELSE EQUAL EQUALS FLOAT FOR FUNC GREATER_EQUAL GREATER_THAN ID IF INT LEFT_BR LEFT_CURL LEFT_PAR LESS_EQUAL LESS_THAN MAIN MINUS MORE MULTIPLY OR PLUS PROGRAM READ RETURN RIGHT_BR RIGHT_CURL RIGHT_PAR SEMICOLON STR THEN TO VAR VD VOID WHILE WRITE\n\tcte_f : CTE_I DOT CTE_I\n\t\n\t\n\tprogram : PROGRAM ID punto_program COLON main\n\t\t\t\t\t| PROGRAM ID punto_program COLON variables main\n\t\t\t\t\t| PROGRAM ID punto_program COLON variables funciones main\n\t\t\t\t\t| PROGRAM ID punto_program COLON funciones main  \n\t\n\tpunto_program : \n\t\n\tmain : MAIN LEFT_PAR RIGHT_PAR LEFT_CURL punto_goto_main main_aux RIGHT_CURL punto_generator\n\t\n\tpunto_generator :\n\t\n\tpunto_goto_main :\n\t\n\tmain_aux : estatutos_main_multiple\n\t\t\t\t\t | empty\n\t\n\tvariables : VAR punto_variables_1 SEMICOLON\n\t\t\t\t\t\t| VAR punto_variables_1 variables_aux SEMICOLON\n\t\n\tpunto_variables_1 :\n\t\n\tvariables_aux : tipo COLON declaracion_inicial\n\t\t\t\t\t\t\t\t| tipo COLON declaracion_inicial MORE variables_aux\n\t\n\ttipo : INT\n\t\t\t| FLOAT\n\t\t\t| CHAR\n\t\n\tdeclaracion_inicial : dec_varaux punto_dec_var_1 COMMA declaracion_inicial\n\t\t\t\t\t\t\t\t\t\t\t| dec_varaux punto_dec_var_1\n\t\n\tpunto_dec_var_1 :\n\t\n\tdec_varaux : ID \n\t\t\t\t\t\t | dec_var_dimension\n\t\t\t\t\t\t\t\n\t\n\tdec_var_dimension : ID LEFT_BR punto_is_array CTE_I punto_size RIGHT_BR \n\t\t\t\t\t\t| ID LEFT_BR punto_is_array CTE_I punto_size  RIGHT_BR LEFT_BR CTE_I punto_size RIGHT_BR\n\t\n\tpunto_is_array :\n\t\n\t\n\tpunto_size :\n\t\n\tpunto_dec_varaux_1 :\n\t\n\tdec_var : ID COMMA dec_var\n\t\t\t\t\t| ID\n\t\n\tdec_var_llamada : m_exp punto_verify_dec_param COMMA punto_mas_k dec_var_llamada\n\t\t\t\t\t\t\t\t\t| m_exp punto_verify_dec_param\n\t\n\tpunto_mas_k :\n\t\n\tpunto_verify_dec_param : \n\t\n\tfunciones : funciones_aux\n\t\t\t\t\t\t| funciones_aux funciones\n\t\n\t\n\t\tfunciones_aux : tipo FUNC ID punto_id_func punto_return_value LEFT_PAR not_params RIGHT_PAR LEFT_CURL not_variables estatutos RIGHT_CURL punto_end_function_return\n\t\t\t\t\t\t\t\t | VOID FUNC ID punto_id_func LEFT_PAR not_params RIGHT_PAR LEFT_CURL not_variables count_vars estatutos RIGHT_CURL end_func\n\t\n\tpunto_return_value :\n\t\n\tnot_variables : variables count_vars\n\t\t\t\t\t\t\t\t| empty\n\t\n\tnot_params : parametros count_params\n\t\t\t\t\t\t | empty\n\t\n\t\tpunto_end_function_return :\n\t\n\tpunto_id_func :\n\t\n\tparametros : dec_var_param COMMA parametros\n\t\t\t\t\t\t\t| dec_var_param\n\t\n\tdec_var_param : tipo ID punto_push_param\n\t\n\tpunto_push_param :\n\t\n\tcount_params :\n\t\n\tcount_vars :\n\t\n\tend_func :\n\t\n\t\texp_or : t_exp punto_pop_or t_exp_or_aux\n\t\t\t\t\t| t_exp punto_pop_or\n\t\n\t\tpunto_pop_or :\n\t\n\t\n\tt_exp_or_aux : OR punto_push_or exp_or\n\t\n\tpunto_push_or :\n\t\n\tt_exp : g_exp pop_and t_exp_aux\n\t\t\t\t| g_exp pop_and\n\t\n\tpop_and :\n\t\n\t\n\tt_exp_aux : AND punto_push_and t_exp\n\t\n\tpunto_push_and :\n\t\n\t\tg_exp : m_exp\n\t\t\t\t\t| m_exp relacionales punto_relacionales m_exp punto_pop_relacional\n\t\n\tpunto_relacionales :\n\t\n\tpunto_pop_relacional :\n\t\n\tm_exp : termino punto_mexp_pop\n\t\t\t\t| termino punto_mexp_pop m_exp_aux\n\t\n\tpunto_mexp_pop :\n\t\n\tm_exp_aux : PLUS punto_m_exp_push m_exp\n\t\t\t\t\t\t| MINUS punto_m_exp_push m_exp\n\t\n\tpunto_m_exp_push :\n\t\n\ttermino : factor punto_termino_pop\n\t\t\t\t\t| factor punto_termino_pop termino_aux\n\t\n\tpunto_termino_pop :\n\t\n  termino_aux : MULTIPLY punto_termino_aux termino\n              | DIVIDE punto_termino_aux termino\n  \n\tpunto_termino_aux :\n\t\n\tfactor : cte\n\t\t\t\t| LEFT_PAR punto_fondo_falso exp_or RIGHT_PAR punto_fin_fondo_falso\n\t\t\t\t| ID factor_push_operand\n\t\t\t\t| ID punto_verify_id LEFT_PAR punto_era RIGHT_PAR punto_end_llamada\n\t\t\t\t| ID punto_verify_id LEFT_PAR punto_era punto_fondo_falso dec_var_llamada RIGHT_PAR punto_saca_fondo_falso punto_verify_total_params punto_end_llamada\n\t\t\t\t| ID punto_asignacion_var punto_get_size LEFT_BR punto_fondo_falso m_exp punto_access_arr punto_verify_arr RIGHT_BR punto_direccion_arr \n\t\n\tpunto_saca_fondo_falso : \n\t\n\tpunto_fondo_falso :\n\t\n\tpunto_fin_fondo_falso :\n\t\n\trelacionales : LESS_THAN\n\t\t\t\t\t\t\t\t\t| GREATER_THAN\n\t\t\t\t\t\t\t\t\t| DIFFERENT\n\t\t\t\t\t\t\t\t\t| EQUAL\n\t\t\t\t\t\t\t\t\t| GREATER_EQUAL\n\t\t\t\t\t\t\t\t\t| LESS_EQUAL\n\t\n\testatutos : estatutos_main_aux \n\t\t\t\t\t\t| retorno SEMICOLON \n\t\n\testatutos_main : asignacion SEMICOLON\n\t\t\t\t\t\t\t\t\t| llamada SEMICOLON\n\t\t\t\t\t\t\t\t\t| lectura SEMICOLON\n\t\t\t\t\t\t\t\t\t| escritura SEMICOLON\n\t\t\t\t\t\t\t\t\t| decision SEMICOLON\n\t\t\t\t\t\t\t\t\t| repeticion SEMICOLON\n\t\n\testatutos_main_multiple : estatutos_main estatutos_main_multiple\n\t\t\t\t\t\t\t\t\t\t| estatutos_main\n\t\n\testatutos_main_aux : estatutos_main estatutos\n\t\t\t\t\t\t\t\t\t\t\t| estatutos_main\n\t\n\tasignacion : vars EQUALS punto_igual m_exp punto_asignacion\n\t\t\t\t\t\t\n\t\n\tvars : ID punto_asignacion_var\n\t\t\t | ID punto_asignacion_var punto_get_size LEFT_BR punto_fondo_falso m_exp punto_access_arr punto_verify_arr RIGHT_BR punto_direccion_arr \n\t\t\t \n\t\n\tpunto_dimension_2 :\n\t\n\tpunto_get_size :\n\t\n\tpunto_access_arr :\n\t\n\tpunto_verify_arr :\n\t\n\tpunto_direccion_arr :\n\t\n\tpunto_asignacion_var : \n\t\n\tpunto_igual :\n\t\n\tpunto_asignacion : \n\t\n\t\tllamada : ID punto_verify_id LEFT_PAR punto_era RIGHT_PAR punto_end_llamada \n\t\t\t\t\t\t| ID punto_verify_id LEFT_PAR punto_era dec_var_llamada RIGHT_PAR punto_verify_total_params punto_end_llamada\n\t\t\t\t\t\t\n\t\n\tpunto_verify_id :\n\t\n\tpunto_verify_total_params :\n\t\n\tpunto_end_llamada :\n\t\n\tpunto_era :\n\t\n\t\tretorno : RETURN LEFT_PAR m_exp RIGHT_PAR punto_return\n\t\n\tpunto_return :\n\t\n\t\n\tpunto_read_stack : \n\t\n\tlectura : READ LEFT_PAR lectura_var RIGHT_PAR\n\t\n\tlectura_var : punto_read_stack ID punto_push_dec_var punto_add_read_operand COMMA lectura_var\n\t\t\t\t\t| punto_read_stack ID punto_push_dec_var punto_add_read_operand\n\t\n\tpunto_push_dec_var :\n\t\n\t\tpunto_add_read_operand : \n\t\n\tescritura : WRITE LEFT_PAR escritura_aux RIGHT_PAR\n\t\n\tescritura_aux : punto_write_stack STR punto_escritura_push punto_add_write_operand\n\t\t\t\t\t\t\t\t| punto_write_stack m_exp punto_escritura_push punto_add_write_operand\n\t\t\t\t\t\t\t\t| punto_write_stack STR punto_escritura_push punto_add_write_operand COMMA escritura_aux \n\t\t\t\t\t\t\t\t| punto_write_stack m_exp punto_escritura_push punto_add_write_operand COMMA escritura_aux\n\t\n\tpunto_escritura_push : \n\t\n\tpunto_write_stack :\n\t\n\tpunto_add_write_operand : \n\t\n\tdecision : IF LEFT_PAR exp_or RIGHT_PAR punto_if_exp LEFT_CURL estatutos RIGHT_CURL punto_end_if \n\t\t\t\t\t\t| IF LEFT_PAR exp_or RIGHT_PAR punto_if_exp  LEFT_CURL estatutos RIGHT_CURL ELSE punto_else LEFT_CURL estatutos RIGHT_CURL punto_end_if\n\t\n\tpunto_if_exp :\n\t\n\tpunto_else :\n\t\n\tpunto_end_if :\n\t\n\trepeticion : condicional\n\t\t\t\t\t\t\t| no_condicional\n\t\n\tno_condicional : FOR LEFT_PAR ID punto_for EQUALS m_exp punto_exp_for_inf TO m_exp punto_exp_for_sup RIGHT_PAR LEFT_CURL estatutos RIGHT_CURL punto_end_for\n\t\n\tpunto_for :\n\t\n\tpunto_exp_for_inf :\n\t\n\tpunto_exp_for_sup :\n\t\n\tpunto_end_for :\n\t\n\tcondicional : WHILE punto_while LEFT_PAR exp_or RIGHT_PAR punto_validar_exp LEFT_CURL estatutos RIGHT_CURL punto_end_while\n\t\n\tpunto_while :\n\t\n\tpunto_validar_exp :\n\t\n\tpunto_end_while :\n\t\n\tcte : CTE_I factor_int_push\n\t\t\t| cte_f factor_float_push\n\t\t\t| CTE_CHAR factor_char_push\n\t\n\tfactor_push_operand :\n\t\n\tfactor_float_push :\n\t\n\tfactor_int_push :\n\t\n\tfactor_char_push :\n\t\n\tempty : \n\t'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,6,17,19,25,72,96,],[0,-2,-3,-5,-4,-8,-7,]),'ID':([2,14,15,16,23,24,27,32,33,34,37,47,71,74,75,76,77,78,79,80,83,84,85,87,89,97,98,101,103,104,116,121,125,126,132,136,137,138,139,140,141,142,155,156,157,158,163,170,172,173,175,176,178,179,180,184,186,187,188,197,198,199,201,202,203,204,205,206,213,217,219,220,221,232,233,234,240,243,253,275,282,],[3,-17,-18,-19,30,31,-12,-9,-13,40,55,55,95,-97,-98,-99,-100,-101,-102,-116,-126,-138,112,117,40,112,-123,128,112,-87,112,-163,112,-87,112,-66,-89,-90,-91,-92,-93,-94,-163,-52,-52,-42,112,-58,-63,112,-73,-73,-79,-79,-123,112,55,55,-41,55,112,112,112,112,112,112,-87,-87,55,-34,-126,-138,-138,112,112,55,112,112,112,55,55,]),'COLON':([3,4,14,15,16,29,],[-6,5,-17,-18,-19,34,]),'MAIN':([5,7,8,11,18,22,27,33,237,241,255,257,],[9,9,9,-36,9,-37,-12,-13,-45,-53,-38,-39,]),'VAR':([5,121,155,],[10,10,10,]),'VOID':([5,7,11,27,33,237,241,255,257,],[13,13,13,-12,-13,-45,-53,-38,-39,]),'INT':([5,7,10,11,21,27,33,43,63,66,94,237,241,255,257,],[14,14,-14,14,14,-12,-13,14,14,14,14,-45,-53,-38,-39,]),'FLOAT':([5,7,10,11,21,27,33,43,63,66,94,237,241,255,257,],[15,15,-14,15,15,-12,-13,15,15,15,15,-45,-53,-38,-39,]),'CHAR':([5,7,10,11,21,27,33,43,63,66,94,237,241,255,257,],[16,16,-14,16,16,-12,-13,16,16,16,16,-45,-53,-38,-39,]),'LEFT_PAR':([9,30,31,35,36,42,55,56,57,58,61,62,80,81,84,85,86,97,98,103,104,112,116,125,126,132,136,137,138,139,140,141,142,146,163,170,172,173,175,176,178,179,180,184,198,199,201,202,203,204,205,206,214,217,220,221,232,233,240,243,253,],[20,-46,-46,-40,43,66,-120,83,84,85,-153,87,-116,98,-138,104,116,104,-123,104,-87,-120,104,104,-87,104,-66,-89,-90,-91,-92,-93,-94,180,104,-58,-63,104,-73,-73,-79,-79,-123,104,104,104,104,104,104,104,-87,-87,240,-34,-138,-138,104,104,104,104,104,]),'SEMICOLON':([10,21,28,38,39,40,41,48,49,50,51,52,53,59,60,64,88,109,110,111,112,113,114,115,118,124,127,129,143,144,145,148,150,151,159,160,174,177,182,185,189,190,196,212,216,222,227,228,229,230,231,242,248,249,260,262,264,266,267,270,272,274,276,277,280,281,283,285,286,287,],[-14,27,33,-15,-22,-23,-24,74,75,76,77,78,79,-145,-146,-21,-16,-70,-76,-80,-159,-161,-160,-162,-20,-117,-127,-132,-68,-74,-82,-156,-157,-158,-107,-122,-69,-75,-1,-25,-118,-121,-88,238,-122,-81,-71,-72,-77,-78,-122,-119,-144,-83,-140,-86,-155,-26,-125,-121,-152,-124,-122,-114,-84,-85,-144,-141,-151,-147,]),'FUNC':([12,13,14,15,16,],[23,24,-17,-18,-19,]),'RIGHT_PAR':([20,43,66,67,68,69,70,91,93,95,98,100,102,105,106,107,108,109,110,111,112,113,114,115,122,123,125,128,130,131,134,135,143,144,145,148,150,151,152,161,162,164,165,166,167,169,171,174,177,180,182,191,193,194,195,196,200,205,222,224,225,226,227,228,229,230,231,245,246,247,249,250,256,258,262,265,270,273,276,277,280,281,],[26,-163,-163,92,-51,-44,-48,120,-43,-50,-123,127,129,133,-56,-61,-64,-70,-76,-80,-159,-161,-160,-162,-47,-49,160,-130,-137,-137,-55,-60,-68,-74,-82,-156,-157,-158,183,190,-35,-131,-139,-139,196,-54,-59,-69,-75,-123,-1,-33,-129,-133,-134,-88,-67,231,-81,-57,-62,-65,-71,-72,-77,-78,-122,-128,-135,-136,-83,262,267,-32,-86,-150,-121,278,-122,-114,-84,-85,]),'LEFT_CURL':([26,92,120,133,168,183,207,261,269,278,],[32,121,155,-142,197,-154,234,-143,275,282,]),'RETURN':([27,33,74,75,76,77,78,79,121,155,156,157,158,186,187,188,197,213,234,275,282,],[-12,-13,-97,-98,-99,-100,-101,-102,-163,-163,-52,-52,-42,214,214,-41,214,214,214,214,214,]),'READ':([27,32,33,37,47,74,75,76,77,78,79,121,155,156,157,158,186,187,188,197,213,234,275,282,],[-12,-9,-13,56,56,-97,-98,-99,-100,-101,-102,-163,-163,-52,-52,-42,56,56,-41,56,56,56,56,56,]),'WRITE':([27,32,33,37,47,74,75,76,77,78,79,121,155,156,157,158,186,187,188,197,213,234,275,282,],[-12,-9,-13,57,57,-97,-98,-99,-100,-101,-102,-163,-163,-52,-52,-42,57,57,-41,57,57,57,57,57,]),'IF':([27,32,33,37,47,74,75,76,77,78,79,121,155,156,157,158,186,187,188,197,213,234,275,282,],[-12,-9,-13,58,58,-97,-98,-99,-100,-101,-102,-163,-163,-52,-52,-42,58,58,-41,58,58,58,58,58,]),'WHILE':([27,32,33,37,47,74,75,76,77,78,79,121,155,156,157,158,186,187,188,197,213,234,275,282,],[-12,-9,-13,61,61,-97,-98,-99,-100,-101,-102,-163,-163,-52,-52,-42,61,61,-41,61,61,61,61,61,]),'FOR':([27,32,33,37,47,74,75,76,77,78,79,121,155,156,157,158,186,187,188,197,213,234,275,282,],[-12,-9,-13,62,62,-97,-98,-99,-100,-101,-102,-163,-163,-52,-52,-42,62,62,-41,62,62,62,62,62,]),'RIGHT_CURL':([32,37,44,45,46,47,73,74,75,76,77,78,79,210,211,213,215,223,238,239,252,279,284,],[-9,-163,72,-10,-11,-104,-103,-97,-98,-99,-100,-101,-102,237,-95,-106,241,248,-96,-105,264,283,286,]),'MORE':([38,39,40,41,64,118,185,266,],[63,-22,-23,-24,-21,-20,-25,-26,]),'COMMA':([39,40,41,64,70,95,109,110,111,112,113,114,115,123,128,130,131,143,144,145,148,150,151,162,164,165,166,174,177,182,185,191,193,194,195,196,222,227,228,229,230,231,249,262,266,270,276,277,280,281,],[-22,-23,-24,89,94,-50,-70,-76,-80,-159,-161,-160,-162,-49,-130,-137,-137,-68,-74,-82,-156,-157,-158,-35,-131,-139,-139,-69,-75,-1,-25,217,219,220,221,-88,-81,-71,-72,-77,-78,-122,-83,-86,-26,-121,-122,-114,-84,-85,]),'LEFT_BR':([40,55,82,99,112,147,181,185,],[65,-115,-111,126,-115,-111,206,209,]),'EQUALS':([54,55,82,117,153,259,268,],[80,-115,-108,-148,184,-114,-109,]),'CTE_I':([65,80,84,85,90,97,98,103,104,116,125,126,132,136,137,138,139,140,141,142,149,163,170,172,173,175,176,178,179,180,184,198,199,201,202,203,204,205,206,209,217,220,221,232,233,240,243,253,],[-27,-116,-138,113,119,113,-123,113,-87,113,113,-87,113,-66,-89,-90,-91,-92,-93,-94,182,113,-58,-63,113,-73,-73,-79,-79,-123,113,113,113,113,113,113,113,-87,-87,236,-34,-138,-138,113,113,113,113,113,]),'CTE_CHAR':([80,84,85,97,98,103,104,116,125,126,132,136,137,138,139,140,141,142,163,170,172,173,175,176,178,179,180,184,198,199,201,202,203,204,205,206,217,220,221,232,233,240,243,253,],[-116,-138,115,115,-123,115,-87,115,115,-87,115,-66,-89,-90,-91,-92,-93,-94,115,-58,-63,115,-73,-73,-79,-79,-123,115,115,115,115,115,115,115,-87,-87,-34,-138,-138,115,115,115,115,115,]),'STR':([84,103,220,221,],[-138,130,-138,-138,]),'OR':([106,107,108,109,110,111,112,113,114,115,134,135,143,144,145,148,150,151,171,174,177,182,196,200,222,225,226,227,228,229,230,231,249,262,270,276,277,280,281,],[-56,-61,-64,-70,-76,-80,-159,-161,-160,-162,170,-60,-68,-74,-82,-156,-157,-158,-59,-69,-75,-1,-88,-67,-81,-62,-65,-71,-72,-77,-78,-122,-83,-86,-121,-122,-114,-84,-85,]),'AND':([107,108,109,110,111,112,113,114,115,135,143,144,145,148,150,151,174,177,182,196,200,222,226,227,228,229,230,231,249,262,270,276,277,280,281,],[-61,-64,-70,-76,-80,-159,-161,-160,-162,172,-68,-74,-82,-156,-157,-158,-69,-75,-1,-88,-67,-81,-65,-71,-72,-77,-78,-122,-83,-86,-121,-122,-114,-84,-85,]),'LESS_THAN':([108,109,110,111,112,113,114,115,143,144,145,148,150,151,174,177,182,196,222,227,228,229,230,231,249,262,270,276,277,280,281,],[137,-70,-76,-80,-159,-161,-160,-162,-68,-74,-82,-156,-157,-158,-69,-75,-1,-88,-81,-71,-72,-77,-78,-122,-83,-86,-121,-122,-114,-84,-85,]),'GREATER_THAN':([108,109,110,111,112,113,114,115,143,144,145,148,150,151,174,177,182,196,222,227,228,229,230,231,249,262,270,276,277,280,281,],[138,-70,-76,-80,-159,-161,-160,-162,-68,-74,-82,-156,-157,-158,-69,-75,-1,-88,-81,-71,-72,-77,-78,-122,-83,-86,-121,-122,-114,-84,-85,]),'DIFFERENT':([108,109,110,111,112,113,114,115,143,144,145,148,150,151,174,177,182,196,222,227,228,229,230,231,249,262,270,276,277,280,281,],[139,-70,-76,-80,-159,-161,-160,-162,-68,-74,-82,-156,-157,-158,-69,-75,-1,-88,-81,-71,-72,-77,-78,-122,-83,-86,-121,-122,-114,-84,-85,]),'EQUAL':([108,109,110,111,112,113,114,115,143,144,145,148,150,151,174,177,182,196,222,227,228,229,230,231,249,262,270,276,277,280,281,],[140,-70,-76,-80,-159,-161,-160,-162,-68,-74,-82,-156,-157,-158,-69,-75,-1,-88,-81,-71,-72,-77,-78,-122,-83,-86,-121,-122,-114,-84,-85,]),'GREATER_EQUAL':([108,109,110,111,112,113,114,115,143,144,145,148,150,151,174,177,182,196,222,227,228,229,230,231,249,262,270,276,277,280,281,],[141,-70,-76,-80,-159,-161,-160,-162,-68,-74,-82,-156,-157,-158,-69,-75,-1,-88,-81,-71,-72,-77,-78,-122,-83,-86,-121,-122,-114,-84,-85,]),'LESS_EQUAL':([108,109,110,111,112,113,114,115,143,144,145,148,150,151,174,177,182,196,222,227,228,229,230,231,249,262,270,276,277,280,281,],[142,-70,-76,-80,-159,-161,-160,-162,-68,-74,-82,-156,-157,-158,-69,-75,-1,-88,-81,-71,-72,-77,-78,-122,-83,-86,-121,-122,-114,-84,-85,]),'PLUS':([109,110,111,112,113,114,115,143,144,145,148,150,151,177,182,196,222,229,230,231,249,262,270,276,277,280,281,],[-70,-76,-80,-159,-161,-160,-162,175,-74,-82,-156,-157,-158,-75,-1,-88,-81,-77,-78,-122,-83,-86,-121,-122,-114,-84,-85,]),'MINUS':([109,110,111,112,113,114,115,143,144,145,148,150,151,177,182,196,222,229,230,231,249,262,270,276,277,280,281,],[-70,-76,-80,-159,-161,-160,-162,176,-74,-82,-156,-157,-158,-75,-1,-88,-81,-77,-78,-122,-83,-86,-121,-122,-114,-84,-85,]),'RIGHT_BR':([109,110,111,112,113,114,115,119,143,144,145,148,150,151,154,174,177,182,192,196,218,222,227,228,229,230,231,236,244,249,251,254,262,263,270,271,276,277,280,281,],[-70,-76,-80,-159,-161,-160,-162,-28,-68,-74,-82,-156,-157,-158,185,-69,-75,-1,-112,-88,-113,-81,-71,-72,-77,-78,-122,-28,259,-83,-112,266,-86,-113,-121,277,-122,-114,-84,-85,]),'TO':([109,110,111,112,113,114,115,143,144,145,148,150,151,174,177,182,196,208,222,227,228,229,230,231,235,249,262,270,276,277,280,281,],[-70,-76,-80,-159,-161,-160,-162,-68,-74,-82,-156,-157,-158,-69,-75,-1,-88,-149,-81,-71,-72,-77,-78,-122,253,-83,-86,-121,-122,-114,-84,-85,]),'MULTIPLY':([110,111,112,113,114,115,144,145,148,150,151,182,196,222,231,249,262,270,276,277,280,281,],[-76,-80,-159,-161,-160,-162,178,-82,-156,-157,-158,-1,-88,-81,-122,-83,-86,-121,-122,-114,-84,-85,]),'DIVIDE':([110,111,112,113,114,115,144,145,148,150,151,182,196,222,231,249,262,270,276,277,280,281,],[-76,-80,-159,-161,-160,-162,179,-82,-156,-157,-158,-1,-88,-81,-122,-83,-86,-121,-122,-114,-84,-85,]),'DOT':([113,],[149,]),'ELSE':([248,],[261,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'punto_program':([3,],[4,]),'main':([5,7,8,18,],[6,17,19,25,]),'variables':([5,121,155,],[7,157,157,]),'funciones':([5,7,11,],[8,18,22,]),'funciones_aux':([5,7,11,],[11,11,11,]),'tipo':([5,7,11,21,43,63,66,94,],[12,12,12,29,71,29,71,71,]),'punto_variables_1':([10,],[21,]),'variables_aux':([21,63,],[28,88,]),'punto_id_func':([30,31,],[35,36,]),'punto_goto_main':([32,],[37,]),'declaracion_inicial':([34,89,],[38,118,]),'dec_varaux':([34,89,],[39,39,]),'dec_var_dimension':([34,89,],[41,41,]),'punto_return_value':([35,],[42,]),'main_aux':([37,],[44,]),'estatutos_main_multiple':([37,47,],[45,73,]),'empty':([37,43,66,121,155,],[46,69,69,158,158,]),'estatutos_main':([37,47,186,187,197,213,234,275,282,],[47,47,213,213,213,213,213,213,213,]),'asignacion':([37,47,186,187,197,213,234,275,282,],[48,48,48,48,48,48,48,48,48,]),'llamada':([37,47,186,187,197,213,234,275,282,],[49,49,49,49,49,49,49,49,49,]),'lectura':([37,47,186,187,197,213,234,275,282,],[50,50,50,50,50,50,50,50,50,]),'escritura':([37,47,186,187,197,213,234,275,282,],[51,51,51,51,51,51,51,51,51,]),'decision':([37,47,186,187,197,213,234,275,282,],[52,52,52,52,52,52,52,52,52,]),'repeticion':([37,47,186,187,197,213,234,275,282,],[53,53,53,53,53,53,53,53,53,]),'vars':([37,47,186,187,197,213,234,275,282,],[54,54,54,54,54,54,54,54,54,]),'condicional':([37,47,186,187,197,213,234,275,282,],[59,59,59,59,59,59,59,59,59,]),'no_condicional':([37,47,186,187,197,213,234,275,282,],[60,60,60,60,60,60,60,60,60,]),'punto_dec_var_1':([39,],[64,]),'not_params':([43,66,],[67,91,]),'parametros':([43,66,94,],[68,68,122,]),'dec_var_param':([43,66,94,],[70,70,70,]),'punto_verify_id':([55,112,],[81,146,]),'punto_asignacion_var':([55,112,],[82,147,]),'punto_while':([61,],[86,]),'punto_is_array':([65,],[90,]),'count_params':([68,],[93,]),'punto_generator':([72,],[96,]),'punto_igual':([80,],[97,]),'punto_get_size':([82,147,],[99,181,]),'lectura_var':([83,219,],[100,245,]),'punto_read_stack':([83,219,],[101,101,]),'escritura_aux':([84,220,221,],[102,246,247,]),'punto_write_stack':([84,220,221,],[103,103,103,]),'exp_or':([85,116,132,198,],[105,152,167,224,]),'t_exp':([85,116,132,198,199,],[106,106,106,106,225,]),'g_exp':([85,116,132,198,199,],[107,107,107,107,107,]),'m_exp':([85,97,103,116,125,132,163,173,184,198,199,201,202,232,233,240,243,253,],[108,124,131,108,162,108,192,200,208,108,108,227,228,162,251,256,162,265,]),'termino':([85,97,103,116,125,132,163,173,184,198,199,201,202,203,204,232,233,240,243,253,],[109,109,109,109,109,109,109,109,109,109,109,109,109,229,230,109,109,109,109,109,]),'factor':([85,97,103,116,125,132,163,173,184,198,199,201,202,203,204,232,233,240,243,253,],[110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,]),'cte':([85,97,103,116,125,132,163,173,184,198,199,201,202,203,204,232,233,240,243,253,],[111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,]),'cte_f':([85,97,103,116,125,132,163,173,184,198,199,201,202,203,204,232,233,240,243,253,],[114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,]),'punto_push_param':([95,],[123,]),'punto_era':([98,180,],[125,205,]),'punto_fondo_falso':([104,126,205,206,],[132,163,232,233,]),'punto_pop_or':([106,],[134,]),'pop_and':([107,],[135,]),'relacionales':([108,],[136,]),'punto_mexp_pop':([109,],[143,]),'punto_termino_pop':([110,],[144,]),'factor_push_operand':([112,],[145,]),'factor_int_push':([113,],[148,]),'factor_float_push':([114,],[150,]),'factor_char_push':([115,],[151,]),'punto_for':([117,],[153,]),'punto_size':([119,236,],[154,254,]),'not_variables':([121,155,],[156,186,]),'punto_asignacion':([124,],[159,]),'dec_var_llamada':([125,232,243,],[161,250,258,]),'punto_push_dec_var':([128,],[164,]),'punto_escritura_push':([130,131,],[165,166,]),'punto_if_exp':([133,],[168,]),'t_exp_or_aux':([134,],[169,]),'t_exp_aux':([135,],[171,]),'punto_relacionales':([136,],[173,]),'m_exp_aux':([143,],[174,]),'termino_aux':([144,],[177,]),'count_vars':([156,157,],[187,188,]),'punto_end_llamada':([160,216,231,276,],[189,242,249,280,]),'punto_verify_dec_param':([162,],[191,]),'punto_add_read_operand':([164,],[193,]),'punto_add_write_operand':([165,166,],[194,195,]),'punto_push_or':([170,],[198,]),'punto_push_and':([172,],[199,]),'punto_m_exp_push':([175,176,],[201,202,]),'punto_termino_aux':([178,179,],[203,204,]),'punto_validar_exp':([183,],[207,]),'estatutos':([186,187,197,213,234,275,282,],[210,215,223,239,252,279,284,]),'estatutos_main_aux':([186,187,197,213,234,275,282,],[211,211,211,211,211,211,211,]),'retorno':([186,187,197,213,234,275,282,],[212,212,212,212,212,212,212,]),'punto_verify_total_params':([190,270,],[216,276,]),'punto_access_arr':([192,251,],[218,263,]),'punto_fin_fondo_falso':([196,],[222,]),'punto_pop_relacional':([200,],[226,]),'punto_exp_for_inf':([208,],[235,]),'punto_mas_k':([217,],[243,]),'punto_verify_arr':([218,263,],[244,271,]),'punto_end_function_return':([237,],[255,]),'end_func':([241,],[257,]),'punto_end_if':([248,283,],[260,285,]),'punto_direccion_arr':([259,277,],[268,281,]),'punto_else':([261,],[269,]),'punto_saca_fondo_falso':([262,],[270,]),'punto_end_while':([264,],[272,]),'punto_exp_for_sup':([265,],[273,]),'punto_return':([267,],[274,]),'punto_end_for':([286,],[287,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('cte_f -> CTE_I DOT CTE_I','cte_f',3,'p_cte_f','lexer.py',127),
  ('program -> PROGRAM ID punto_program COLON main','program',5,'p_program','lexer.py',139),
  ('program -> PROGRAM ID punto_program COLON variables main','program',6,'p_program','lexer.py',140),
  ('program -> PROGRAM ID punto_program COLON variables funciones main','program',7,'p_program','lexer.py',141),
  ('program -> PROGRAM ID punto_program COLON funciones main','program',6,'p_program','lexer.py',142),
  ('punto_program -> <empty>','punto_program',0,'p_punto_program','lexer.py',147),
  ('main -> MAIN LEFT_PAR RIGHT_PAR LEFT_CURL punto_goto_main main_aux RIGHT_CURL punto_generator','main',8,'p_main','lexer.py',166),
  ('punto_generator -> <empty>','punto_generator',0,'p_punto_generator','lexer.py',170),
  ('punto_goto_main -> <empty>','punto_goto_main',0,'p_punto_goto_main','lexer.py',188),
  ('main_aux -> estatutos_main_multiple','main_aux',1,'p_main_aux','lexer.py',196),
  ('main_aux -> empty','main_aux',1,'p_main_aux','lexer.py',197),
  ('variables -> VAR punto_variables_1 SEMICOLON','variables',3,'p_variables','lexer.py',202),
  ('variables -> VAR punto_variables_1 variables_aux SEMICOLON','variables',4,'p_variables','lexer.py',203),
  ('punto_variables_1 -> <empty>','punto_variables_1',0,'p_punto_variables_1','lexer.py',208),
  ('variables_aux -> tipo COLON declaracion_inicial','variables_aux',3,'p_variables_aux','lexer.py',214),
  ('variables_aux -> tipo COLON declaracion_inicial MORE variables_aux','variables_aux',5,'p_variables_aux','lexer.py',215),
  ('tipo -> INT','tipo',1,'p_tipo','lexer.py',220),
  ('tipo -> FLOAT','tipo',1,'p_tipo','lexer.py',221),
  ('tipo -> CHAR','tipo',1,'p_tipo','lexer.py',222),
  ('declaracion_inicial -> dec_varaux punto_dec_var_1 COMMA declaracion_inicial','declaracion_inicial',4,'p_declaracion_inicial','lexer.py',237),
  ('declaracion_inicial -> dec_varaux punto_dec_var_1','declaracion_inicial',2,'p_declaracion_inicial','lexer.py',238),
  ('punto_dec_var_1 -> <empty>','punto_dec_var_1',0,'p_punto_dec_var_1','lexer.py',244),
  ('dec_varaux -> ID','dec_varaux',1,'p_dec_varaux','lexer.py',263),
  ('dec_varaux -> dec_var_dimension','dec_varaux',1,'p_dec_varaux','lexer.py',264),
  ('dec_var_dimension -> ID LEFT_BR punto_is_array CTE_I punto_size RIGHT_BR','dec_var_dimension',6,'p_dec_var_dimension','lexer.py',271),
  ('dec_var_dimension -> ID LEFT_BR punto_is_array CTE_I punto_size RIGHT_BR LEFT_BR CTE_I punto_size RIGHT_BR','dec_var_dimension',10,'p_dec_var_dimension','lexer.py',272),
  ('punto_is_array -> <empty>','punto_is_array',0,'p_punto_is_array','lexer.py',278),
  ('punto_size -> <empty>','punto_size',0,'p_punto_size','lexer.py',286),
  ('punto_dec_varaux_1 -> <empty>','punto_dec_varaux_1',0,'p_punto_dec_varaux_1','lexer.py',300),
  ('dec_var -> ID COMMA dec_var','dec_var',3,'p_dec_var','lexer.py',305),
  ('dec_var -> ID','dec_var',1,'p_dec_var','lexer.py',306),
  ('dec_var_llamada -> m_exp punto_verify_dec_param COMMA punto_mas_k dec_var_llamada','dec_var_llamada',5,'p_dec_var_llamada','lexer.py',311),
  ('dec_var_llamada -> m_exp punto_verify_dec_param','dec_var_llamada',2,'p_dec_var_llamada','lexer.py',312),
  ('punto_mas_k -> <empty>','punto_mas_k',0,'p_punto_mas_k','lexer.py',316),
  ('punto_verify_dec_param -> <empty>','punto_verify_dec_param',0,'p_punto_verify_dec_param','lexer.py',323),
  ('funciones -> funciones_aux','funciones',1,'p_funciones','lexer.py',337),
  ('funciones -> funciones_aux funciones','funciones',2,'p_funciones','lexer.py',338),
  ('funciones_aux -> tipo FUNC ID punto_id_func punto_return_value LEFT_PAR not_params RIGHT_PAR LEFT_CURL not_variables estatutos RIGHT_CURL punto_end_function_return','funciones_aux',13,'p_funciones_aux','lexer.py',345),
  ('funciones_aux -> VOID FUNC ID punto_id_func LEFT_PAR not_params RIGHT_PAR LEFT_CURL not_variables count_vars estatutos RIGHT_CURL end_func','funciones_aux',13,'p_funciones_aux','lexer.py',346),
  ('punto_return_value -> <empty>','punto_return_value',0,'p_punto_return_value','lexer.py',350),
  ('not_variables -> variables count_vars','not_variables',2,'p_not_variables','lexer.py',366),
  ('not_variables -> empty','not_variables',1,'p_not_variables','lexer.py',367),
  ('not_params -> parametros count_params','not_params',2,'p_not_params','lexer.py',372),
  ('not_params -> empty','not_params',1,'p_not_params','lexer.py',373),
  ('punto_end_function_return -> <empty>','punto_end_function_return',0,'p_punto_end_function_return','lexer.py',378),
  ('punto_id_func -> <empty>','punto_id_func',0,'p_punto_id_func','lexer.py',395),
  ('parametros -> dec_var_param COMMA parametros','parametros',3,'p_parametros','lexer.py',412),
  ('parametros -> dec_var_param','parametros',1,'p_parametros','lexer.py',413),
  ('dec_var_param -> tipo ID punto_push_param','dec_var_param',3,'p_dec_var_param','lexer.py',418),
  ('punto_push_param -> <empty>','punto_push_param',0,'p_punto_push_param','lexer.py',423),
  ('count_params -> <empty>','count_params',0,'p_count_params','lexer.py',443),
  ('count_vars -> <empty>','count_vars',0,'p_count_vars','lexer.py',450),
  ('end_func -> <empty>','end_func',0,'p_end_func','lexer.py',458),
  ('exp_or -> t_exp punto_pop_or t_exp_or_aux','exp_or',3,'p_exp_or','lexer.py',472),
  ('exp_or -> t_exp punto_pop_or','exp_or',2,'p_exp_or','lexer.py',473),
  ('punto_pop_or -> <empty>','punto_pop_or',0,'p_punto_pop_or','lexer.py',477),
  ('t_exp_or_aux -> OR punto_push_or exp_or','t_exp_or_aux',3,'p_t_exp_or_aux','lexer.py',514),
  ('punto_push_or -> <empty>','punto_push_or',0,'p_punto_push_or','lexer.py',519),
  ('t_exp -> g_exp pop_and t_exp_aux','t_exp',3,'p_t_exp','lexer.py',527),
  ('t_exp -> g_exp pop_and','t_exp',2,'p_t_exp','lexer.py',528),
  ('pop_and -> <empty>','pop_and',0,'p_pop_and','lexer.py',532),
  ('t_exp_aux -> AND punto_push_and t_exp','t_exp_aux',3,'p_t_exp_aux','lexer.py',566),
  ('punto_push_and -> <empty>','punto_push_and',0,'p_punto_push_and','lexer.py',570),
  ('g_exp -> m_exp','g_exp',1,'p_g_exp','lexer.py',577),
  ('g_exp -> m_exp relacionales punto_relacionales m_exp punto_pop_relacional','g_exp',5,'p_g_exp','lexer.py',578),
  ('punto_relacionales -> <empty>','punto_relacionales',0,'p_punto_relacionales','lexer.py',582),
  ('punto_pop_relacional -> <empty>','punto_pop_relacional',0,'p_punto_pop_relacional','lexer.py',591),
  ('m_exp -> termino punto_mexp_pop','m_exp',2,'p_m_exp','lexer.py',618),
  ('m_exp -> termino punto_mexp_pop m_exp_aux','m_exp',3,'p_m_exp','lexer.py',619),
  ('punto_mexp_pop -> <empty>','punto_mexp_pop',0,'p_punto_mexp_pop','lexer.py',626),
  ('m_exp_aux -> PLUS punto_m_exp_push m_exp','m_exp_aux',3,'p_m_exp_aux','lexer.py',664),
  ('m_exp_aux -> MINUS punto_m_exp_push m_exp','m_exp_aux',3,'p_m_exp_aux','lexer.py',665),
  ('punto_m_exp_push -> <empty>','punto_m_exp_push',0,'p_punto_m_exp_push','lexer.py',669),
  ('termino -> factor punto_termino_pop','termino',2,'p_termino','lexer.py',679),
  ('termino -> factor punto_termino_pop termino_aux','termino',3,'p_termino','lexer.py',680),
  ('punto_termino_pop -> <empty>','punto_termino_pop',0,'p_punto_termino_pop','lexer.py',686),
  ('termino_aux -> MULTIPLY punto_termino_aux termino','termino_aux',3,'p_termino_aux','lexer.py',722),
  ('termino_aux -> DIVIDE punto_termino_aux termino','termino_aux',3,'p_termino_aux','lexer.py',723),
  ('punto_termino_aux -> <empty>','punto_termino_aux',0,'p_punto_termino_aux','lexer.py',728),
  ('factor -> cte','factor',1,'p_factor','lexer.py',736),
  ('factor -> LEFT_PAR punto_fondo_falso exp_or RIGHT_PAR punto_fin_fondo_falso','factor',5,'p_factor','lexer.py',737),
  ('factor -> ID factor_push_operand','factor',2,'p_factor','lexer.py',738),
  ('factor -> ID punto_verify_id LEFT_PAR punto_era RIGHT_PAR punto_end_llamada','factor',6,'p_factor','lexer.py',739),
  ('factor -> ID punto_verify_id LEFT_PAR punto_era punto_fondo_falso dec_var_llamada RIGHT_PAR punto_saca_fondo_falso punto_verify_total_params punto_end_llamada','factor',10,'p_factor','lexer.py',740),
  ('factor -> ID punto_asignacion_var punto_get_size LEFT_BR punto_fondo_falso m_exp punto_access_arr punto_verify_arr RIGHT_BR punto_direccion_arr','factor',10,'p_factor','lexer.py',741),
  ('punto_saca_fondo_falso -> <empty>','punto_saca_fondo_falso',0,'p_saca_fondo_falso','lexer.py',747),
  ('punto_fondo_falso -> <empty>','punto_fondo_falso',0,'p_punto_fondo_falso','lexer.py',754),
  ('punto_fin_fondo_falso -> <empty>','punto_fin_fondo_falso',0,'p_punto_fin_fondo_falso','lexer.py',762),
  ('relacionales -> LESS_THAN','relacionales',1,'p_relacionales','lexer.py',769),
  ('relacionales -> GREATER_THAN','relacionales',1,'p_relacionales','lexer.py',770),
  ('relacionales -> DIFFERENT','relacionales',1,'p_relacionales','lexer.py',771),
  ('relacionales -> EQUAL','relacionales',1,'p_relacionales','lexer.py',772),
  ('relacionales -> GREATER_EQUAL','relacionales',1,'p_relacionales','lexer.py',773),
  ('relacionales -> LESS_EQUAL','relacionales',1,'p_relacionales','lexer.py',774),
  ('estatutos -> estatutos_main_aux','estatutos',1,'p_estatutos','lexer.py',781),
  ('estatutos -> retorno SEMICOLON','estatutos',2,'p_estatutos','lexer.py',782),
  ('estatutos_main -> asignacion SEMICOLON','estatutos_main',2,'p_estatutos_main','lexer.py',787),
  ('estatutos_main -> llamada SEMICOLON','estatutos_main',2,'p_estatutos_main','lexer.py',788),
  ('estatutos_main -> lectura SEMICOLON','estatutos_main',2,'p_estatutos_main','lexer.py',789),
  ('estatutos_main -> escritura SEMICOLON','estatutos_main',2,'p_estatutos_main','lexer.py',790),
  ('estatutos_main -> decision SEMICOLON','estatutos_main',2,'p_estatutos_main','lexer.py',791),
  ('estatutos_main -> repeticion SEMICOLON','estatutos_main',2,'p_estatutos_main','lexer.py',792),
  ('estatutos_main_multiple -> estatutos_main estatutos_main_multiple','estatutos_main_multiple',2,'p_estatutos_main_multiple','lexer.py',797),
  ('estatutos_main_multiple -> estatutos_main','estatutos_main_multiple',1,'p_estatutos_main_multiple','lexer.py',798),
  ('estatutos_main_aux -> estatutos_main estatutos','estatutos_main_aux',2,'p_estatutos_main_aux','lexer.py',803),
  ('estatutos_main_aux -> estatutos_main','estatutos_main_aux',1,'p_estatutos_main_aux','lexer.py',804),
  ('asignacion -> vars EQUALS punto_igual m_exp punto_asignacion','asignacion',5,'p_asignacion','lexer.py',809),
  ('vars -> ID punto_asignacion_var','vars',2,'p_vars','lexer.py',814),
  ('vars -> ID punto_asignacion_var punto_get_size LEFT_BR punto_fondo_falso m_exp punto_access_arr punto_verify_arr RIGHT_BR punto_direccion_arr','vars',10,'p_vars','lexer.py',815),
  ('punto_dimension_2 -> <empty>','punto_dimension_2',0,'p_punto_dimension_2','lexer.py',847),
  ('punto_get_size -> <empty>','punto_get_size',0,'p_punto_get_size','lexer.py',855),
  ('punto_access_arr -> <empty>','punto_access_arr',0,'p_punto_access_arr','lexer.py',864),
  ('punto_verify_arr -> <empty>','punto_verify_arr',0,'p_punto_verify_arr','lexer.py',879),
  ('punto_direccion_arr -> <empty>','punto_direccion_arr',0,'p_punto_direccion_arr','lexer.py',905),
  ('punto_asignacion_var -> <empty>','punto_asignacion_var',0,'p_punto_asignacion_var','lexer.py',926),
  ('punto_igual -> <empty>','punto_igual',0,'p_punto_igual','lexer.py',941),
  ('punto_asignacion -> <empty>','punto_asignacion',0,'p_punto_asignacion','lexer.py',948),
  ('llamada -> ID punto_verify_id LEFT_PAR punto_era RIGHT_PAR punto_end_llamada','llamada',6,'p_llamada','lexer.py',974),
  ('llamada -> ID punto_verify_id LEFT_PAR punto_era dec_var_llamada RIGHT_PAR punto_verify_total_params punto_end_llamada','llamada',8,'p_llamada','lexer.py',975),
  ('punto_verify_id -> <empty>','punto_verify_id',0,'p_punto_verify_id','lexer.py',980),
  ('punto_verify_total_params -> <empty>','punto_verify_total_params',0,'p_punto_verify_total_params','lexer.py',988),
  ('punto_end_llamada -> <empty>','punto_end_llamada',0,'p_punto_end_llamada','lexer.py',997),
  ('punto_era -> <empty>','punto_era',0,'p_punto_era','lexer.py',1021),
  ('retorno -> RETURN LEFT_PAR m_exp RIGHT_PAR punto_return','retorno',5,'p_retorno','lexer.py',1045),
  ('punto_return -> <empty>','punto_return',0,'p_punto_return','lexer.py',1049),
  ('punto_read_stack -> <empty>','punto_read_stack',0,'p_punto_read_stack','lexer.py',1068),
  ('lectura -> READ LEFT_PAR lectura_var RIGHT_PAR','lectura',4,'p_lectura','lexer.py',1077),
  ('lectura_var -> punto_read_stack ID punto_push_dec_var punto_add_read_operand COMMA lectura_var','lectura_var',6,'p_lectura_var','lexer.py',1082),
  ('lectura_var -> punto_read_stack ID punto_push_dec_var punto_add_read_operand','lectura_var',4,'p_lectura_var','lexer.py',1083),
  ('punto_push_dec_var -> <empty>','punto_push_dec_var',0,'p_punto_push_dec_var','lexer.py',1089),
  ('punto_add_read_operand -> <empty>','punto_add_read_operand',0,'p_punto_add_read_operand','lexer.py',1105),
  ('escritura -> WRITE LEFT_PAR escritura_aux RIGHT_PAR','escritura',4,'p_escritura','lexer.py',1121),
  ('escritura_aux -> punto_write_stack STR punto_escritura_push punto_add_write_operand','escritura_aux',4,'p_escritura_aux','lexer.py',1126),
  ('escritura_aux -> punto_write_stack m_exp punto_escritura_push punto_add_write_operand','escritura_aux',4,'p_escritura_aux','lexer.py',1127),
  ('escritura_aux -> punto_write_stack STR punto_escritura_push punto_add_write_operand COMMA escritura_aux','escritura_aux',6,'p_escritura_aux','lexer.py',1128),
  ('escritura_aux -> punto_write_stack m_exp punto_escritura_push punto_add_write_operand COMMA escritura_aux','escritura_aux',6,'p_escritura_aux','lexer.py',1129),
  ('punto_escritura_push -> <empty>','punto_escritura_push',0,'p_punto_escritura_push','lexer.py',1133),
  ('punto_write_stack -> <empty>','punto_write_stack',0,'p_punto_write_stack','lexer.py',1151),
  ('punto_add_write_operand -> <empty>','punto_add_write_operand',0,'p_punto_add_write_operand','lexer.py',1158),
  ('decision -> IF LEFT_PAR exp_or RIGHT_PAR punto_if_exp LEFT_CURL estatutos RIGHT_CURL punto_end_if','decision',9,'p_decision','lexer.py',1170),
  ('decision -> IF LEFT_PAR exp_or RIGHT_PAR punto_if_exp LEFT_CURL estatutos RIGHT_CURL ELSE punto_else LEFT_CURL estatutos RIGHT_CURL punto_end_if','decision',14,'p_decision','lexer.py',1171),
  ('punto_if_exp -> <empty>','punto_if_exp',0,'p_punto_if_exp','lexer.py',1175),
  ('punto_else -> <empty>','punto_else',0,'p_punto_else','lexer.py',1189),
  ('punto_end_if -> <empty>','punto_end_if',0,'p_punto_end_if','lexer.py',1200),
  ('repeticion -> condicional','repeticion',1,'p_repeticion','lexer.py',1208),
  ('repeticion -> no_condicional','repeticion',1,'p_repeticion','lexer.py',1209),
  ('no_condicional -> FOR LEFT_PAR ID punto_for EQUALS m_exp punto_exp_for_inf TO m_exp punto_exp_for_sup RIGHT_PAR LEFT_CURL estatutos RIGHT_CURL punto_end_for','no_condicional',15,'p_no_condicional','lexer.py',1214),
  ('punto_for -> <empty>','punto_for',0,'p_punto_for','lexer.py',1219),
  ('punto_exp_for_inf -> <empty>','punto_exp_for_inf',0,'p_punto_exp_for_inf','lexer.py',1233),
  ('punto_exp_for_sup -> <empty>','punto_exp_for_sup',0,'p_punto_exp_for_sup','lexer.py',1253),
  ('punto_end_for -> <empty>','punto_end_for',0,'p_punto_end_for','lexer.py',1284),
  ('condicional -> WHILE punto_while LEFT_PAR exp_or RIGHT_PAR punto_validar_exp LEFT_CURL estatutos RIGHT_CURL punto_end_while','condicional',10,'p_condicional','lexer.py',1304),
  ('punto_while -> <empty>','punto_while',0,'p_punto_while','lexer.py',1309),
  ('punto_validar_exp -> <empty>','punto_validar_exp',0,'p_punto_validar_exp','lexer.py',1317),
  ('punto_end_while -> <empty>','punto_end_while',0,'p_punto_end_while','lexer.py',1333),
  ('cte -> CTE_I factor_int_push','cte',2,'p_cte','lexer.py',1349),
  ('cte -> cte_f factor_float_push','cte',2,'p_cte','lexer.py',1350),
  ('cte -> CTE_CHAR factor_char_push','cte',2,'p_cte','lexer.py',1351),
  ('factor_push_operand -> <empty>','factor_push_operand',0,'p_factor_push_operand','lexer.py',1357),
  ('factor_float_push -> <empty>','factor_float_push',0,'p_factor_float_push','lexer.py',1374),
  ('factor_int_push -> <empty>','factor_int_push',0,'p_factor_int_push','lexer.py',1385),
  ('factor_char_push -> <empty>','factor_char_push',0,'p_factor_char_push','lexer.py',1397),
  ('empty -> <empty>','empty',0,'p_empty','lexer.py',1413),
]
