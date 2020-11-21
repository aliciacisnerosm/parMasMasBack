import sys
import re

# from compilador.ply.lex import lex
# from compilador.ply.yacc import yacc

import compilador.ply.lex as lex
import compilador.ply.yacc as yacc
import compilador.semantic_var as semantic_var
from compilador.semantic_var import *
from compilador.quadruples import *
from compilador.memory import *
from compilador.types import *
from compilador.virtual_machine import *
from collections import deque
import os

error = False
semantic_var = None
memory = None
scope = 'global'
var_type = None # si tenemos tiempo, quitar global
arr_quadruples = []
cube = SemanticCube()
vControl = None
k = None
func_name = None
generator = None
is_array = False
array_info = {}
cont = 1


stack_operators = deque()
stack_operands = deque()
stack_type = deque()
stack_jumps = deque()
stack_dimensions = deque()


reserved = {
	'if': 'IF',
	'else': 'ELSE',
	'program': 'PROGRAM',
	'main': 'MAIN',
	'var': 'VAR',
	'int': 'INT',
	'char':'CHAR',
	'float': 'FLOAT',
	'write': 'WRITE',
	'while': 'WHILE',
	'do': 'DO',
	'for': 'FOR',
	'then': 'THEN',
	'read': 'READ',
	'vd': 'VD',
	'and': 'AND',
	'or': 'OR',
	'void': 'VOID',
	'func': 'FUNC',
	'to': 'TO',
	'return': 'RETURN'
}


tokens = [ 'ID', 'COLON','SEMICOLON', 'LEFT_PAR', 'RIGHT_PAR', 'LEFT_BR', 'RIGHT_BR', 'LEFT_CURL', 'RIGHT_CURL',
'COMMA', 'EQUALS', 'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'GREATER_THAN', 'LESS_THAN', 'DIFFERENT', 'GREATER_EQUAL','LESS_EQUAL','EQUAL','STR',
'CTE_I','CTE_CHAR', 'MORE', 'DOT',
] + list(reserved.values())

#EXPRESIONES REGULARES SIMPLES
t_STR = r'\"([^"]|\\")*"'
t_COLON = r'\:'
t_SEMICOLON = r'\;'
t_LEFT_PAR = r'\('
t_RIGHT_PAR = r'\)'
t_LEFT_BR = r'\['
t_RIGHT_BR = r'\]'
t_LEFT_CURL = r'\{'
t_RIGHT_CURL = r'\}'
t_COMMA = r'\,'
t_EQUALS = r'\='
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_GREATER_THAN = r'\>'
t_LESS_THAN = r'\<'
t_DIFFERENT = r'\<>'
t_EQUAL = r'\=='
t_GREATER_EQUAL = r'\>='
t_LESS_EQUAL = r'\<='
t_ignore = ' \t'
t_MORE = r'\&'
t_DOT = r'\.'

#EXPRESIONES REGULARES COMPLEJAS
def t_ID(t):
	r'[a-zA-Z_][a-zA-Z_0-9]*'
	t.type = reserved.get(t.value, 'ID')
	return t

def t_CTE_I(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_CTE_CHAR(t):
	r'[a-zA-Z]'
	t.value=str(t.value)
	return t


def t_error(t):
	print("Illegal characters", t)
	t.lexer.skip(1)

def t_newline(t):
		r'\n+'
		t.lexer.lineno += t.value.count("\n")

lexer = lex.lex()
start = 'program'

def p_cte_f(p):
	'''
	cte_f : CTE_I DOT CTE_I
	
	'''
	if p[1] == None:
		global error
		error = True
	
	float_var = str(p[1]) + p[2] + str(p[3])
	p[0] = float(float_var)

def p_program(p):
	'''
	program : PROGRAM ID punto_program COLON main
					| PROGRAM ID punto_program COLON variables main
					| PROGRAM ID punto_program COLON variables funciones main
					| PROGRAM ID punto_program COLON funciones main  
	''' 

def p_punto_program(p):
	'''
	punto_program : 
	'''
	global semantic_var, memory, arr_quadruples
	semantic_var = Semantics()
	memory = Memory()
	global_var = {
		'global_var_names': set(),
	}
	semantic_var._global['global_var'] = global_var
	semantic_var._global['global_count'] = {
		'var_count': 0,
		'var_types': [0,0,0] # 0 int, 1 float & 2 char
	}

	q = Quadruple('GOTO', None, None, None)
	arr_quadruples.append(q.get_quadruple())

def p_main(p):
	'''
	main : MAIN LEFT_PAR RIGHT_PAR LEFT_CURL punto_goto_main main_aux RIGHT_CURL punto_generator
	'''
def p_punto_generator(p):
	'''
	punto_generator :
	'''
	global arr_quadruples, semantic_var, scope
	scope = 'global'
	virtualMachine = VirtualMachine(arr_quadruples,semantic_var._global)
	virtualMachine.execute()
		
	for index, value in enumerate(arr_quadruples):
		print(index, value, file=open("output_quadruples-1.txt", "a"))
		
	semantic_var.remove_local_function(scope)
	memory.reset_local_temp()
	memory.reset_dir_local()
	arr_quadruples = []
	

def p_punto_goto_main(p):
	'''
	punto_goto_main :
	'''
	global arr_quadruples, scope
	scope = 'main'
	arr_quadruples[0]=('GOTO',None,None,len(arr_quadruples))

def p_main_aux(p):
	'''
	main_aux : estatutos_main_multiple
					 | empty
	'''      

def p_variables(p):
	'''
	variables : VAR punto_variables_1 SEMICOLON
						| VAR punto_variables_1 variables_aux SEMICOLON
	'''

def p_punto_variables_1(p):
	'''
	punto_variables_1 :
	'''


def p_variables_aux(p):
	'''
	variables_aux : tipo COLON declaracion_inicial
								| tipo COLON declaracion_inicial MORE variables_aux
	'''

def p_tipo(p):
	'''
	tipo : INT
			| FLOAT
			| CHAR
	'''
	p[0] = p[1]

	global var_type
	if p[1] == 'int':
		var_type = 1
	elif p[1] == 'float':
		var_type = 2
	elif p[1] == 'char':
		var_type = 3
	

def p_declaracion_inicial(p):
	'''
	declaracion_inicial : dec_varaux punto_dec_var_1 COMMA declaracion_inicial
											| dec_varaux punto_dec_var_1
	'''
	
	
def p_punto_dec_var_1(p):
	'''
	punto_dec_var_1 :
	'''
	global semantic_var, scope, var_type, is_array, array_info, cont
	
	if is_array:
		dimension = len(array_info)
		is_array = False
		cont = 1
		if dimension == 1:
			memory_dir_aux = memory.value_memory_array(var_type, scope, False, False, array_info[1]['valor'])
			semantic_var.declare_variables(var_type, scope, 'variable_name', p[-1], None, memory_dir_aux, array_info[1]['valor'], [array_info[1]['valor']])
		array_info = {}
	else:
		memory_dir_aux = memory.get_value_memory(var_type, scope, False, False)
		semantic_var.declare_variables(var_type, scope, 'variable_name', p[-1], None, memory_dir_aux, 0)

	
def p_dec_varaux(p):
	'''
	dec_varaux : ID 
						 | dec_var_dimension
							
	'''
	p[0] = p[1]

def p_dec_var_dimension(p):
	'''
	dec_var_dimension : ID LEFT_BR punto_is_array CTE_I punto_size RIGHT_BR 
						| ID LEFT_BR punto_is_array CTE_I punto_size  RIGHT_BR LEFT_BR CTE_I punto_size RIGHT_BR
	'''	
	p[0] = p[1]

def p_punto_is_array(p):
	'''
	punto_is_array :
	
	'''
	global is_array
	is_array = True

def p_punto_size(p):
	'''
	punto_size :
	'''
	global is_array, array_info, cont
	array_info[cont] = {
		'dimension': cont,
		'valor': p[-1]
	}
	cont += 1



#todo: agregar punto para las dimensiones (:
def p_punto_dec_varaux_1(p):
	'''
	punto_dec_varaux_1 :
	'''

def p_dec_var(p):
	'''
	dec_var : ID COMMA dec_var
					| ID
	'''

def p_dec_var_llamada(p):
	'''
	dec_var_llamada : m_exp punto_verify_dec_param COMMA punto_mas_k dec_var_llamada
									| m_exp punto_verify_dec_param
	'''
def p_punto_mas_k(p):
	'''
	punto_mas_k :
	'''
	global k
	k += 1

def p_punto_verify_dec_param(p):
	'''
	punto_verify_dec_param : 
	'''
	global stack_operands, stack_type, k, func_name, arr_quadruples
	param_type = semantic_var._global['functions'][func_name]['param_types'][k]
	param_1 = stack_operands.pop()
	param_1_type = stack_type.pop()
	if param_type != param_1_type:
		raise Exception("Error: el tipo de parametro no coinicide con el indicado")
	else:
		q = Quadruple('PARAM', param_1, None, k)
		arr_quadruples.append(q.get_quadruple())
	
def p_funciones(p):
	'''
	funciones : funciones_aux
						| funciones_aux funciones
	
	'''
	

def p_funciones_aux(p):
	'''
		funciones_aux : tipo FUNC ID punto_id_func punto_return_value LEFT_PAR not_params RIGHT_PAR LEFT_CURL not_variables estatutos RIGHT_CURL punto_end_function_return
								 | VOID FUNC ID punto_id_func LEFT_PAR not_params RIGHT_PAR LEFT_CURL not_variables count_vars estatutos RIGHT_CURL end_func
	'''
def p_punto_return_value(p):
	'''
	punto_return_value :
	'''
	global semantic_var # id - type
	semantic_var.add_function_id_return_value(p[-2], p[-4])
	return_type = None
	if p[-4] == 'int':
		return_type = 1
	elif p[-4] == 'float':
		return_type = 2
	elif [p-4] == 'char':
		return_type = 3

	memory_dir = memory.get_value_memory(return_type, 'global', False, False)	
	semantic_var.add_variables(return_type, 'global', 'function', p[-2], None, memory_dir, 0 )
def p_not_variables(p):
	'''
	not_variables : variables count_vars
								| empty
	'''

def p_not_params(p):
	'''
	not_params : parametros count_params
						 | empty
	'''

def p_punto_end_function_return(p):
	'''
		punto_end_function_return :
	'''
	global arr_quadruples, scope, semantic_var, memory
	
	q = Quadruple('ENDFUNC',None,None,None)
	arr_quadruples.append(q.get_quadruple())
	
	semantic_var.remove_local_function(scope)
	memory.reset_local_temp()
	memory.reset_dir_local()

	scope = 'global'
	


def p_punto_id_func(p):
	'''
	punto_id_func :
	'''
	global semantic_var, scope, arr_quadruples
	scope = p[-1]

	if p[-3] == 'void':
		semantic_var.declare_function(p[-1], None, len(arr_quadruples))
	elif p[-3] == 'int':
		semantic_var.declare_function(p[-1],1, len(arr_quadruples))
	elif p[-3] == 'char':
		semantic_var.declare_function(p[-1], 2, len(arr_quadruples))
	elif p[-3] == 'float':
		semantic_var.declare_function(p[-1], 3, len(arr_quadruples))
	
	
def p_parametros(p):
	'''
	parametros : dec_var_param COMMA parametros
							| dec_var_param
	'''

def p_dec_var_param(p): 
	'''
	dec_var_param : tipo ID punto_push_param
	'''
	
def p_punto_push_param(p):
	'''
	punto_push_param :
	'''

	global semantic_var
	param_type = -1

	if p[-2] == 'int':
		param_type = 1
	elif p[-2] == 'char':
		param_type = 2
	elif p[-2] == 'float':
		param_type = 3
	
	var_memory= memory.get_value_memory(param_type,scope,False,False)
	semantic_var.add_variables(param_type, scope, 'param',p[-1],None,var_memory,0)
	semantic_var.add_parameter_type(scope, param_type)
	semantic_var._global['functions'][scope]['variables']['name_var'].add(p[-1])

def p_count_params(p):
	'''
	count_params :
	'''
	global semantic_var
	semantic_var.count_params(scope)
	
def p_count_vars(p):
	'''
	count_vars :
	'''	
	global arr_quadruples, semantic_var
	semantic_var.count_vars(scope)
	semantic_var._global['functions'][scope]['arr_quadruples_count'] = len(arr_quadruples)	

def p_end_func(p):
	'''
	end_func :
	'''
	global arr_quadruples, scope, semantic_var
	
	q = Quadruple('ENDFUNC',None,None,None)
	arr_quadruples.append(q.get_quadruple())
	memory.reset_local_temp()
	memory.reset_dir_local()
	semantic_var.remove_local_function(scope)
	scope = 'global'


def p_exp_or(p):
	'''
		exp_or : t_exp punto_pop_or t_exp_or_aux
					| t_exp punto_pop_or
	'''
def p_punto_pop_or(p):
	'''
		punto_pop_or :
	
	'''
	global stack_operators, arr_quadruples, stack_operands, semantic_var, stack_type
	
	if len(stack_operators) != 0:
		top = stack_operators.pop()
		print("top en or", top)
		if top == 'or':
			op1 = stack_operands.pop() # memory dir
			op2 = stack_operands.pop()

			type_1 = stack_type.pop()
			type_2 = stack_type.pop()
			value_type = cube.get_type(type_1, type_2, top)

			if value_type != 5:
				# 1 memory dir : scope, 'bool', temp
				dir_memory_aux = memory.get_value_memory(4, scope, True, False)
		
				# 2 agregar esa direccion de memoria a _global variables temp 
				semantic_var.add_variables(4, scope, 'temp_variable', None, None, dir_memory_aux, 0)
				
				# 3 crear cuadruplo = (or false true memory_dir)

				q = Quadruple(top, op2, op1, dir_memory_aux)
				arr_quadruples.append(q.get_quadruple())
				stack_type.append(value_type)
				stack_operands.append(dir_memory_aux)
			else:
				raise Exception("error en or")
		else:
			stack_operators.append(top)


def p_t_exp_or_aux(p):
	'''
	t_exp_or_aux : OR punto_push_or exp_or
	'''

def p_punto_push_or(p):
	'''
	punto_push_or :
	'''
	global stack_operators
	stack_operators.append('or')


def p_t_exp(p):
	'''
	t_exp : g_exp pop_and t_exp_aux
				| g_exp pop_and
	'''
def p_pop_and(p):
	'''
	pop_and :
	
	'''
	global stack_operators, arr_quadruples, stack_operands,stack_type
	if len(stack_operators) != 0:
		top = stack_operators.pop()

		if top == 'and':
			op1 = stack_operands.pop() # memory dir
			op2 = stack_operands.pop()

			type_1 = stack_type.pop()
			type_2 = stack_type.pop()
			
			value_type = cube.get_type(type_1, type_2, top)
			#todo: checar tipos
			if value_type != 5:
				# 1 memory dir : scope, 'bool', temp
				dir_memory_aux = memory.get_value_memory(4, scope, True, False)

				# 3 agregar esa direccion de memoria a _global variables temp 
				semantic_var.add_variables(4, scope, 'temp_variable', None, None, dir_memory_aux, 0)
				
				q = Quadruple(top, op2, op1, dir_memory_aux)
				arr_quadruples.append(q.get_quadruple())
				stack_operands.append(dir_memory_aux)
				stack_type.append(4)
			else:
				raise Exception("error en and")
		else:
			stack_operators.append(top)

def p_t_exp_aux(p):
	'''
	t_exp_aux : AND punto_push_and t_exp
	'''
def p_punto_push_and(p):
	'''
	punto_push_and :
	'''
	global stack_operators
	stack_operators.append('and')
	
def p_g_exp(p):
	'''
		g_exp : m_exp
					| m_exp relacionales punto_relacionales m_exp punto_pop_relacional
	'''
def p_punto_relacionales(p):
	'''
	punto_relacionales :
	'''
	global stack_operators
	if p[-1] != None:
		stack_operators.append(p[-1])
	

def p_punto_pop_relacional(p):
	'''
	punto_pop_relacional :
	'''
	global stack_operators, arr_quadruples, stack_type,stack_operands
	top = stack_operators.pop()
	if top == '>' or top == '<' or top == '>=' or top == '<=' or top == '==' or top =='<>':

		op1 = stack_operands.pop() # 9 - dir
		op2 = stack_operands.pop() # aglobal - dir

		type_1 = stack_type.pop()
		type_2 = stack_type.pop()

		value_type = cube.get_type(type_1, type_2, top)

		if value_type != 5:
			dir_memory_aux = memory.get_value_memory(4, scope, True, False)
			semantic_var.add_variables(4, scope, 'temp_variable', None,  None, dir_memory_aux, 0)
				
			q = Quadruple(top, op2, op1, dir_memory_aux)
			arr_quadruples.append(q.get_quadruple())
			stack_operands.append(dir_memory_aux)
			stack_type.append(4)
		else:
			stack_operators.append(top)
			
def p_m_exp(p):
	'''
	m_exp : termino punto_mexp_pop
				| termino punto_mexp_pop m_exp_aux
	'''
	global stack_operands, stack_operators
	p[0] = p[1]

def p_punto_mexp_pop(p):
	'''
	punto_mexp_pop :
	'''
	global stack_operators, arr_quadruples, cube, stack_operands, stack_type

	if len(stack_operators) != 0:
		top = stack_operators.pop()

		if top == '+' or top == '-':
			value = None
			value_type = None
			
			op1 = stack_operands.pop()
			op2 = stack_operands.pop()

			type_aux_1 = stack_type.pop()
			type_aux_2 = stack_type.pop()
			
			value_type = cube.get_type(type_aux_1, type_aux_2, top)

			if value_type == 5:
				#todo: error
				raise Exception("error en tipo de suma & resta")
			else:
				dir_memory_aux = memory.get_value_memory(value_type, scope, True, False)
				
				semantic_var.add_variables(value_type, scope, 'temp_variable', None, None, dir_memory_aux, 0)

				q = Quadruple(top, op2, op1, dir_memory_aux )
				arr_quadruples.append(q.get_quadruple())
				stack_operands.append(dir_memory_aux)
				stack_type.append(value_type)

		else:
			stack_operators.append(top)


def p_m_exp_aux(p):
	'''
	m_exp_aux : PLUS punto_m_exp_push m_exp
						| MINUS punto_m_exp_push m_exp
	'''
def p_punto_m_exp_push(p):
	'''
	punto_m_exp_push :
	'''
	global stack_operators
	if p[-1] != None:
		stack_operators.append(p[-1])
		


def p_termino(p):
	'''
	termino : factor punto_termino_pop
					| factor punto_termino_pop termino_aux
	'''   
	p[0] = p[1]

def p_punto_termino_pop(p):
	'''
	punto_termino_pop :
	'''
	global stack_operators, arr_quadruples, cube, stack_operands, stack_type

	if len(stack_operators) != 0:
		top = stack_operators.pop()

		if top == '*' or top == '/':
			value = None
			value_type = None
			
			op1 = stack_operands.pop()
			op2 = stack_operands.pop()
			
			type_aux_1 = stack_type.pop()
			type_aux_2 = stack_type.pop()
			
			value_type = cube.get_type(type_aux_1, type_aux_2, top)

			if value_type == 5:
				#todo: error
				raise Exception("error en multiplicacion y división")
			else:
				dir_memory_aux = memory.get_value_memory(value_type, scope, True, False)
				semantic_var.add_variables(value_type, scope, 'temp_variable', None, None, dir_memory_aux, 0)

				q = Quadruple(top, op2, op1, dir_memory_aux )
				arr_quadruples.append(q.get_quadruple())
				stack_operands.append(dir_memory_aux)
				stack_type.append(value_type)

		else:
			stack_operators.append(top)

def p_termino_aux(p):
  '''
  termino_aux : MULTIPLY punto_termino_aux termino
              | DIVIDE punto_termino_aux termino
  '''

def p_punto_termino_aux(p):
	'''
	punto_termino_aux :
	'''
	global stack_operators
	if p[-1] != None:
		stack_operators.append(p[-1])

def p_factor(p):
	'''
	factor : cte
				| LEFT_PAR punto_fondo_falso exp_or RIGHT_PAR punto_fin_fondo_falso
				| ID factor_push_operand
				| ID punto_verify_id LEFT_PAR punto_era RIGHT_PAR punto_end_llamada
				| ID punto_verify_id LEFT_PAR punto_era punto_fondo_falso dec_var_llamada RIGHT_PAR punto_saca_fondo_falso punto_verify_total_params punto_end_llamada
				| ID punto_asignacion_var punto_get_size LEFT_BR punto_fondo_falso m_exp punto_access_arr punto_verify_arr RIGHT_BR punto_direccion_arr 
	'''
	p[0] = p[1]

def p_saca_fondo_falso(p):
	'''
	punto_saca_fondo_falso : 
	'''
	global stack_operators
	stack_operators.pop()
	
def p_punto_fondo_falso(p):
	'''
	punto_fondo_falso :
	'''
	global stack_operators
	stack_operators.append('(')


def p_punto_fin_fondo_falso(p):
	'''
	punto_fin_fondo_falso :
	'''
	global stack_operators
	stack_operators.pop()
	
def p_relacionales(p):
	'''
	relacionales : LESS_THAN
									| GREATER_THAN
									| DIFFERENT
									| EQUAL
									| GREATER_EQUAL
									| LESS_EQUAL
	'''
	p[0] = p[1]


def p_estatutos(p):
	'''
	estatutos : estatutos_main_aux 
						| retorno SEMICOLON 
	'''

def p_estatutos_main(p):
	'''
	estatutos_main : asignacion SEMICOLON
									| llamada SEMICOLON
									| lectura SEMICOLON
									| escritura SEMICOLON
									| decision SEMICOLON
									| repeticion SEMICOLON
	''' 
	
def p_estatutos_main_multiple(p):
	'''
	estatutos_main_multiple : estatutos_main estatutos_main_multiple
										| estatutos_main
	'''

def p_estatutos_main_aux(p):
	'''
	estatutos_main_aux : estatutos_main estatutos
											| estatutos_main
	'''

def p_asignacion(p):
	'''
	asignacion : vars EQUALS punto_igual m_exp punto_asignacion
						
	'''
def p_vars(p):
	'''
	vars : ID punto_asignacion_var
			 | ID punto_asignacion_var punto_get_size LEFT_BR punto_fondo_falso m_exp punto_access_arr punto_verify_arr RIGHT_BR punto_direccion_arr 
			 
	'''
	p[0] = p[1]
	print(p[0], "este  es p[0]")

# def p_punto_verify_matriz(p):
# 	'''
# 	punto_verify_matriz :
# 	'''
# 	global stack_operators, stack_dimensions, arr_quadruples, stack_operands
# 	stack_operators.pop() #sacar fondo falso
# 	value_2=stack_dimensions.pop() #dimension casilla 2 que quiero accesar
# 	value_1= stack_dimensions.pop()#dimension casilla 1 que quiero accesar
# 	total = stack_dimensions.pop()  #dimension total de la variable (24)
# 	dimension_array = semantic_var.get_dimension_array(scope, p[-13])
	
# 	if value_1 <= dimension_array[0] and value_2 <= dimension_array[1]:
# 		q1= Quadruple('Verify',value_1,None,dimension_array[0])
# 		arr_quadruples.append(q1.get_quadruple())
# 		q2=Quadruple('Verify',value_2,None,dimension_array[1])
# 		arr_quadruples.append(q2.get_quadruple())
# 		total = (value_1+1)*(value_2+1)
# 		final_dir = p[-13]+total
# 		qtotal =Quadruple('&',p[-13],total,final_dir )
# 		arr_quadruples.append(qtotal.get_quadruple())
# 		stack_operands.append(final_dir)
# 	else:
# 		print("ERROR: OUT OF BOUNDS")

def p_punto_dimension_2(p):
	'''
	punto_dimension_2 :
	'''
	global stack_operators
	stack_operators.pop()


def p_punto_get_size(p):
	'''
	punto_get_size :
	'''
	global semantic_var, stack_dimensions
	memory_dir = p[-1]
	dimension = semantic_var.get_dimension_variable(scope, memory_dir) #dimension total de la variable 
	stack_dimensions.append(dimension) # dimension total

def p_punto_access_arr(p):
	'''
	punto_access_arr :
	'''
	global stack_dimensions,semantic_var
	var_type = stack_type.pop()
	var = stack_operands.pop()
	
	if var_type == 1:
		stack_type.append(var_type)
		stack_operands.append(var)
		#elemento  al que  quiero accesar
	else:
		raise Exception("ERROR: SOLO SE ACEPTAN ENTEROS")
		
def p_punto_verify_arr(p):
	'''
	punto_verify_arr :
	'''
	global arr_quadruples, stack_dimensions, stack_operators, stack_operands, semantic_var, stack_pointers
	stack_operators.pop() # sacar fondo falso
	access =stack_operands[len(stack_operands) - 1]# direccion del que yo quiero accesar
	print("Esta es la  direcciond del que quiero accesar", access)
	total_size = stack_dimensions.pop() #dimension total del array
	print("este es total_size", total_size)

	value = semantic_var.get_value_variable(scope,access)
	print("este es value  en  punto_verify_arr", value)
	if (value <= total_size and value >=0):
		q =Quadruple('Verify',access,0,total_size) # verificar tamaño
		arr_quadruples.append(q.get_quadruple())
	
		# memory_val = memory.get_value_memory(1, scope,True, False)
		# q2 = Quadruple('&', p[-7], access, memory_val )
		# arr_quadruples.append(q2.get_quadruple())
		# stack_operands.append(memory_val)

	
	else:
		raise Exception("ERROR: OUT OF BOUNDS")
def p_punto_direccion_arr(p):
	'''
	punto_direccion_arr :
	'''
	global stack_operands, arr_quadruples
	value = stack_operands.pop() #aux1
	value_type = stack_type.pop()
	temp = memory.get_value_memory(value_type,scope,True,False)  #ti
	k= memory.get_value_memory(1, scope, False, True)# siempre 0
	semantic_var.add_constant_variables(1, scope, 'const_variable', 0, k, 0)

	q = Quadruple('+',value,k, temp)
	arr_quadruples.append(q.get_quadruple())

	temp_n= memory.get_value_memory(value_type,scope,True,False)

	q2= Quadruple('&', temp,p[-8], temp_n)
	arr_quadruples.append(q2.get_quadruple())
	stack_operands.append( '(' + str(temp_n) + ')')

	
def p_punto_asignacion_var(p):
	'''
	punto_asignacion_var : 
	'''
	global stack_operands, stack_type, semantic_var, stack_type
	var_id = semantic_var.get_memory_dir(p[-1], scope)
	type_id = semantic_var.get_return_type_variables(scope, var_id)

	if var_id != None:
		stack_operands.append(var_id)
		stack_type.append(type_id)

	print(stack_operands)
	p[0] = var_id

def p_punto_igual(p):
	'''
	punto_igual :
	'''
	global stack_operators
	stack_operators.append('=')
	
def p_punto_asignacion(p):
	'''
	punto_asignacion : 
	'''
	global stack_operators, stack_operands, arr_quadruples, scope, stack_type, semantic_var
	if p[-4] != None:
		name = semantic_var.get_name_variable(p[-4], scope)
		
		if not semantic_var.get_variables_sets(p[-4], scope):
			raise Exception("error en punto de asignacion")
		else:
			elem = stack_operands.pop()
			izq= stack_operands.pop()
			op = stack_operators.pop()

			ty1= stack_type.pop()
			ty2 = stack_type.pop()
			
			value_type = cube.get_type(ty1, ty2, op)
			
			if value_type == 5:
				print("error en asignacion, type mismatch")
			else:			
				q = Quadruple(op, elem, None, izq)
				arr_quadruples.append(q.get_quadruple())

def p_llamada(p):
	'''
		llamada : ID punto_verify_id LEFT_PAR punto_era RIGHT_PAR punto_end_llamada 
						| ID punto_verify_id LEFT_PAR punto_era dec_var_llamada RIGHT_PAR punto_verify_total_params punto_end_llamada
						
	'''
def p_punto_verify_id(p):
	'''
	punto_verify_id :
	'''
	global semantic_var, arr_quadruples
	if not semantic_var.verify_function_id(p[-1]):
		raise Exception("Error: esta función no existe", p[-1])

def p_punto_verify_total_params(p):
	'''
	punto_verify_total_params :
	'''
	global k, semantic_var
	total_params= len(semantic_var._global['functions'][func_name]['param_types'])
	if(k+1!=total_params):
		print("error no coincide cantidad de parametros")

def p_punto_end_llamada(p):
	'''
	punto_end_llamada :
	'''
	global arr_quadruples, func_name, semantic_var, stack_operands, stack_type
	q = Quadruple('GOSUB',func_name,None, semantic_var.get_init_function(func_name))
	arr_quadruples.append(q.get_quadruple())

	if len(stack_operands) != 0:
		memory_dir = stack_operands.pop()
		
		if semantic_var.memory_dir_is_function(memory_dir):
			return_type = stack_type.pop()
			memory_dir_2 = memory.get_value_memory(return_type, scope, True, False)
			q2 = Quadruple('=', memory_dir, None, memory_dir_2)
			stack_operands.append(memory_dir_2)
			stack_type.append(return_type)
			arr_quadruples.append(q2.get_quadruple())
		else:
			stack_operands.append(memory_dir)
	else:
		print("sigue funcion void")


def p_punto_era(p):
	'''
	punto_era :
	'''
	global k, arr_quadruples, func_name, semantic_var
	q = Quadruple('ERA', None,None,p[-3])
	arr_quadruples.append(q.get_quadruple())

	memory_dir = semantic_var.get_memory_dir(p[-3], 'global')

	if memory_dir == None:
		if p[-3] not in semantic_var._global['functions']['func_names']:
			raise Exception("ERROR: FUNCIÓN NO EXISTE")
		else:
			print("es una funcion void")
	else:
		return_type = semantic_var.get_return_type_variables('global', memory_dir)
		stack_type.append(return_type)
		stack_operands.append(memory_dir)

	k = 0
	func_name = p[-3]

	
def p_retorno(p):
	'''
		retorno : RETURN LEFT_PAR m_exp RIGHT_PAR punto_return
	'''
def p_punto_return(p):
	'''
	punto_return :
	
	'''
	global stack_operands, semantic_var, stack_type, arr_quadruples
	value = stack_operands.pop()
	semantic_var.add_function_return_value(scope, value)
	return_type=stack_type.pop()
	q = Quadruple('RETURN', None, None, value)
	arr_quadruples.append(q.get_quadruple())
	# funcion -> 
	memory_dir = semantic_var.get_memory_dir(scope, 'global')
	print("¿que esta retornando?", value, memory_dir, scope)
	#temp_return = memory.get_value_memory(return_type, scope, True, False)
	q2 = Quadruple('=', value, None, memory_dir)
	arr_quadruples.append(q2.get_quadruple())


def p_punto_read_stack(p):
	'''
	punto_read_stack : 
	'''
	global stack_operators
	stack_operators.append("read")
	


def p_lectura(p):
	'''
	lectura : READ LEFT_PAR lectura_var RIGHT_PAR
	'''

def p_lectura_var(p):
	'''
	lectura_var : punto_read_stack ID punto_push_dec_var punto_add_read_operand COMMA lectura_var
					| punto_read_stack ID punto_push_dec_var punto_add_read_operand
	'''
	p[0] = p[1]

def p_punto_push_dec_var(p):
	'''
	punto_push_dec_var :
	'''
	global stack_operands, stack_operators, stack_type

	var_id = semantic_var.get_memory_dir(p[-1], scope)
	type_id = semantic_var.get_return_type_variables(scope, var_id)

	if p[-1] != None:
		stack_operands.append(var_id)
		stack_type.append(type_id)

	p[0] = var_id
	

def p_punto_add_read_operand(p):
	'''
		punto_add_read_operand : 
	'''
	global arr_quadruples
	global stack_operators
	global stack_operands

	if not semantic_var.get_variables_sets(p[-2], scope):
		raise Exception("Error en punto de read")
	else:
		type1 = stack_type.pop()
		q = Quadruple(stack_operators.pop(), None, None, stack_operands.pop())
		arr_quadruples.append(q.get_quadruple())

#TO DO: ARREGLAR ESCRITURA MULTIPLES STRINGS
def p_escritura(p):
	'''
	escritura : WRITE LEFT_PAR escritura_aux RIGHT_PAR
	'''

def p_escritura_aux(p):
	'''
	escritura_aux : punto_write_stack STR punto_escritura_push punto_add_write_operand
								| punto_write_stack m_exp punto_escritura_push punto_add_write_operand
								| punto_write_stack STR punto_escritura_push punto_add_write_operand COMMA escritura_aux 
								| punto_write_stack m_exp punto_escritura_push punto_add_write_operand COMMA escritura_aux
	'''
def p_punto_escritura_push(p):
	'''
	punto_escritura_push : 
	'''
	global stack_operands, semantic_var, stack_operators, stack_type
	if type(p[-1]) == str:
		if not re.search("\".*\"", p[-1]):
			stack_operands.append(stack_operands.pop())
		else:
			memory_dir = memory.get_value_memory(6, scope, False, True)
			semantic_var.add_constant_variables(6, scope, 'const_variable', p[-1], memory_dir, 0)
			stack_operands.append(memory_dir)
			stack_type.append(6)

	else:
		stack_operands.append(stack_operands.pop())

		
def p_punto_write_stack(p):
	'''
	punto_write_stack :
	'''
	global stack_operators
	stack_operators.append("write")

def p_punto_add_write_operand(p):
	'''
	punto_add_write_operand : 
	'''
	global arr_quadruples, stack_operators, stack_operands, semantic_var,stack_type
	
	# checar q este ok 
	elemento = stack_operands.pop()
	type_elment = stack_type.pop()
	q = Quadruple(stack_operators.pop(), None, None, elemento)
	arr_quadruples.append(q.get_quadruple())

def p_decision(p):
	'''
	decision : IF LEFT_PAR exp_or RIGHT_PAR punto_if_exp LEFT_CURL estatutos RIGHT_CURL punto_end_if 
						| IF LEFT_PAR exp_or RIGHT_PAR punto_if_exp  LEFT_CURL estatutos RIGHT_CURL ELSE punto_else LEFT_CURL estatutos RIGHT_CURL punto_end_if
	'''
def p_punto_if_exp(p):
	'''
	punto_if_exp :
	'''
	global stack_type, stack_operands, arr_quadruples, stack_jumps
	exp_type = stack_type.pop()
	if(exp_type == 5):
		raise Exception("Error, type mismatch")
	else:
		result = stack_operands.pop()
		q = Quadruple('GOTOF', result, None, None) 
		arr_quadruples.append(q.get_quadruple())
		stack_jumps.append(len(arr_quadruples) - 1)
		
def p_punto_else(p):
	'''
	punto_else :
	'''
	global stack_jumps, arr_quadruples
	q = Quadruple('GOTO',None,None,None)
	arr_quadruples.append(q.get_quadruple())
	false= stack_jumps.pop()
	stack_jumps.append(len(arr_quadruples)-1)
	fill(false, len(arr_quadruples))

def p_punto_end_if(p):
	'''
	punto_end_if :
	'''
	global stack_jumps, arr_quadruples
	end = stack_jumps.pop()
	fill(end, len(arr_quadruples))

def p_repeticion(p):
	'''
	repeticion : condicional
							| no_condicional
	'''

def p_no_condicional(p):
	'''
	no_condicional : FOR LEFT_PAR ID punto_for EQUALS m_exp punto_exp_for_inf TO m_exp punto_exp_for_sup RIGHT_PAR LEFT_CURL estatutos RIGHT_CURL punto_end_for
	'''

def p_punto_for(p):
	'''
	punto_for :
	'''
	global stack_jumps, stack_operands, stack_type
	#checar que regresa dec_varaux
	memory_dir_p1 = semantic_var.get_memory_dir(p[-1], scope)
	return_type = semantic_var.get_return_type_variables(scope, memory_dir_p1)
	if return_type == 3 or return_type == 4 or return_type == 5:
		raise Exception("Error, el valor en el for no es numerico")
	else:
		stack_operands.append(memory_dir_p1) # id = j 
		stack_type.append(return_type)  # type - int

def p_punto_exp_for_inf(p):
	'''
	punto_exp_for_inf :
	'''
	global stack_jumps, stack_operands, stack_type, arr_quadruples, vControl
	return_type = stack_type.pop() # exp 1 - int o float 
	if return_type == 3 or return_type == 4 or return_type == 5:
		raise Exception("ERROR: Type mismatch")
	else:
		exp = stack_operands.pop() # 1
		vControl = stack_operands.pop() # j
		controlType = stack_type.pop() # int
		tipo_res= cube.get_type(controlType,return_type,'=')
		if tipo_res == 5:
			raise Exception("ERROR: Type mismatch")
		else :
			#falta el get dir memory para ultimo argumento
			q = Quadruple('=', exp, None, vControl)
			arr_quadruples.append(q.get_quadruple())

def p_punto_exp_for_sup(p):
	'''
	punto_exp_for_sup :
	'''
	global stack_jumps, stack_operands, stack_type, arr_quadruples, vControl
	return_type = stack_type.pop()
	if return_type == 3 or return_type == 4 or return_type == 5:
		raise Exception("Error: type mismatch")
	else:
		exp = stack_operands.pop()
		#checar memory dir
		vFinal = exp
		# imitar proceso de asignacion
		memory_dir_vfinal = None
		if return_type == 1:
			memory_dir_vfinal = memory.get_value_memory(1, scope, True, False)
		elif return_type == 2:
			memory_dir_vfinal = memory.get_value_memory(2, scope, True, False)

		q1= Quadruple('=', exp, None, memory_dir_vfinal)
		arr_quadruples.append(q1.get_quadruple())
		memory_dir = memory.get_value_memory(4, scope, True, False)
		
		q2 = Quadruple('<',vControl, memory_dir_vfinal, memory_dir)
		arr_quadruples.append(q2.get_quadruple())
		#checar para hacer push del contador
		stack_jumps.append(len(arr_quadruples) -1)
		goto = Quadruple('GOTOF', memory_dir, None, None)
		arr_quadruples.append(goto.get_quadruple())
		stack_jumps.append(len(arr_quadruples) -1)

def p_punto_end_for (p):
	'''
	punto_end_for :
	'''
	# imitar proceso 
	global stack_jumps, arr_quadruples
	
	memory_dir_p1 = memory.get_value_memory(1, scope, True, True)
	semantic_var.add_constant_variables(1, scope, 'const_variable', 1, memory_dir_p1, 0)
	q = Quadruple('+',vControl,memory_dir_p1,vControl)
	arr_quadruples.append(q.get_quadruple())
	
	end = stack_jumps.pop()
	ret = stack_jumps.pop()
	q = Quadruple('GOTO', None, None, ret)
	arr_quadruples.append(q.get_quadruple())
	
	fill(end,len(arr_quadruples))


def p_condicional(p):
	'''
	condicional : WHILE punto_while LEFT_PAR exp_or RIGHT_PAR punto_validar_exp LEFT_CURL estatutos RIGHT_CURL punto_end_while
	'''

def p_punto_while(p):
	'''
	punto_while :
	'''
	global stack_jumps, arr_quadruples
	#punto neuralgico para meter el numero del cuadruplo en la pila de saltos
	stack_jumps.append(len(arr_quadruples))

def p_punto_validar_exp(p):
	'''
	punto_validar_exp :
	'''
	global stack_type, stack_operands, arr_quadruples
	return_type = stack_type.pop()
	if return_type != 4:
		raise Exception("Error: type mismatch")
	else:
		result = stack_operands.pop()
		q = Quadruple('GOTOF', result,None,None)
		arr_quadruples.append(q.get_quadruple())
		stack_jumps.append(len(arr_quadruples) - 1)

		

def p_punto_end_while(p):
	'''
	punto_end_while :
	'''
	global stack_jumps, arr_quadruples
	end = stack_jumps.pop()
	goto_return = stack_jumps.pop()
	q = Quadruple('GOTO', None, None,goto_return)
	arr_quadruples.append(q.get_quadruple())
	fill(end,len(arr_quadruples))

def fill(end, cont):
	global arr_quadruples
	aux_q = arr_quadruples[end]
	arr_quadruples[end] = (aux_q[0], aux_q[1], aux_q[2], cont)

def p_cte(p):
	'''
	cte : CTE_I factor_int_push
			| cte_f factor_float_push
			| CTE_CHAR factor_char_push
	'''
	p[0] = p[1]
	
def p_factor_push_operand(p):
	'''
	factor_push_operand :
	'''
	global stack_operators
	if not semantic_var.get_variables_sets(p[-1], scope):
		raise Exception("Error en factor")
	else:
    # TO DO: CHECAR TIPOS PARA MANIPULAR MEMORIA Y TEMPORALES
		global stack_type, stack_operands
		memory_dir_p1 = semantic_var.get_memory_dir(p[-1], scope)
		type_aux_p1 = semantic_var.get_return_type_variables(scope,memory_dir_p1)
		if memory_dir_p1 != None:
			stack_operands.append(memory_dir_p1)
			stack_type.append(type_aux_p1)

#cambio de  add_variables a add_constant_variable y temp_variable a global_constant
def p_factor_float_push(p):
	'''
	factor_float_push :
	'''
	global stack_operands, stack_type
	if p[-1] != None:
		memory_dir_p1 = memory.get_value_memory(2, scope, True, True)
		semantic_var.add_constant_variables(2, scope, 'const_variable', p[-1], memory_dir_p1, 0)
		stack_operands.append(memory_dir_p1)
		stack_type.append(2)

def p_factor_int_push(p):
	'''
	factor_int_push :
	'''
	global stack_operands, scope
	if p[-1] != None:
		memory_dir_p1 = memory.get_value_memory(1, scope, True, True)
		semantic_var.add_constant_variables(1, scope, 'const_variable', p[-1], memory_dir_p1, 0)
		stack_operands.append(memory_dir_p1)
		stack_type.append(1)


def p_factor_char_push(p):
	'''
	factor_char_push :
	'''
	global stack_operands, stack_type
	if p[-1] != None:
		memory_dir_p1 = memory.get_value_memory(3, scope, True, True)
		semantic_var.add_constant_variables(3, 'global', 'const_variable', p[-1], memory_dir_p1, 0)
		stack_operands.append(memory_dir_p1)
		stack_type.append(3)

def p_error(p): 
	global error
	error = True
	raise Exception("ERROR {}".format(p))

def p_empty(p):
	'''
	empty : 
	'''
	p[0] = None

parser = yacc.yacc()


def parser():
	try:
		arch_name = 'fibo_recursivo.txt'
		this_folder = os.path.dirname(os.path.abspath(__file__))
		my_file = os.path.join(this_folder, arch_name)
		print(my_file)
		arch = open(my_file,'r')
		print("Nombre de archivo " + arch_name)
		archivo = arch.read()
		arch.close()
		yacc.parse(archivo)

		if error: 
			return "hay errores de sintaxis"
		else:
			global arr_quadruples, stack_operands, semantic_var, scope
			scope = 'global'
			return "apropiado"


	except EOFError:
		print(EOFError)

if __name__ == '__main__':
	parser()