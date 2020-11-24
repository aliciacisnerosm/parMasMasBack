class Semantics:
	def __init__(self):
		self._global = {
			'functions': {
				'func_names': set(), 
				'main': {
				'param_types': [],
				'param_count': 0,
				'init': 0,
				'var_count': 0,
				'var_types': [0,0,0], # 0 int, 1 float & 2 char
				'temp_count': 0,
				'temp_types': [0,0,0,0], # 0 int, 1 float, 2 char & 3 bool
				'return_type': 'void',
					'variables': {
						'name_var': set(),
					}
				}
			},
			'functions_id_return_values': dict()
		
	}

#Función para declarar una función en el directorio de funciones
# Recibe como parametro el nombre (id), tipo de retorno y el número
# del cuádruplo donde inicia la función		
	def declare_function(self, name, return_type, init_val):
		if name not in self._global['functions']['func_names']:
			self._global['functions']['func_names'].add(name)
			self._global['functions'][name] = {
				'param_types': [],
				'param_count': 0,
				'var_count': 0,
				'init': init_val, 
				'temp_count': 0,
				'return_type': return_type,
				'temp_types': [0, 0, 0, 0],
				'var_types': [0,0,0],
				'variables': {
					'name_var': set()
				},
			}
#Función que obtiene el valor de inicio de la función	
	def get_init_function(self, name):
		return self._global['functions'][name]['init']

#Función que verifica que exista la función dentro del directorio de funciones
	def verify_function_id(self, name):
		return name in self._global['functions']['func_names']
		
#Función que declara variable dentro de la tabla de variables. Recibe el tipo de retorno, scope, kind,
#nombre de la variable, valor, direccion de memoria, dimension, y dimension de Array.
	def declare_variables(self, return_type, scope, kind, name, value, memory_dir, dimension, array_dimension=None):
		if scope == 'global':
			if name not in self._global['global_var']['global_var_names']:
				self._global['global_var']['global_var_names'].add(name)
				self._global['global_var'][memory_dir] = {
					'name': name,
					'return_type': return_type,
					'scope': scope,
					'kind': kind,
					'value': value,
					'memory_dir': memory_dir,
					'dimension': dimension,
					'array_dimension': array_dimension
				}
				
				if kind != 'param_types':
					if return_type == 1:
						self._global['global_count']['var_types'][0] += 1
					elif return_type == 2:
						self._global['global_count']['var_types'][1] += 1
					elif return_type == 3:
						self._global['global_count']['var_types'][2] += 1
				self._global['global_count']['var_count'] += 1
				
			else: 
				return ("Error: Variable ya declarada", name, return_type)
		else: 
			if name not in self._global['functions'][scope]['variables']['name_var']:
				self._global['functions'][scope]['variables']['name_var'].add(name)
				self._global['functions'][scope]['variables'][memory_dir] = {
					'name': name,
					'return_type': return_type,
					'scope': scope,
					'kind': kind,
					'value': value,
					'memory_dir': memory_dir,
					'dimension': dimension

				}
			if kind != 'param_types' and scope != 'global':
				if return_type == 1:
					self._global['functions'][scope]['var_types'][0] += 1
				elif return_type == 2:
					self._global['functions'][scope]['var_types'][1] += 1
				elif return_type == 3:
					self._global['functions'][scope]['var_types'][2] += 1

			else:
				return ("Error: Variable ya declarada", name, return_type)
		
		
		return ("exitoso", name, return_type)

#Asigna un valor de memoria a la variable de acuerdo al scope. Recibe como parametros el nombre y scope.
	def get_memory_dir(self, name, scope):
		if scope == "global":
			list_keys = list(self._global['global_var'].keys())
			for i in list_keys:
				if i != 'global_var_names':
					if self._global['global_var'][i]['name'] == name and name != None:
						return self._global['global_var'][i]['memory_dir']
		else:
			list_keys = list(self._global['functions'][scope]['variables'].keys())
			for i in list_keys:
				if i != 'name_var':
					if self._global['functions'][scope]['variables'][i]['name'] == name and name != None:
						return self._global['functions'][scope]['variables'][i]['memory_dir']
		
			list_keys = list(self._global['global_var'].keys())
			for i in list_keys:
				if i != 'global_var_names':
					if self._global['global_var'][i]['name'] == name and name != None:
						return self._global['global_var'][i]['memory_dir']
		
		return None

#Función que valida si una dirección de memoria corresponde a una función
# que espera valor de retorno. Recibe como parametro una dirección de memoria
	def memory_dir_is_function(self, memory_dir):
			if memory_dir in self._global['global_var']:
				print("is a function result", self._global['global_var'][memory_dir]['kind'] == 'function', memory_dir)
				return self._global['global_var'][memory_dir]['kind'] == 'function'

#Función que asigna un tipo de valor de retorno a una función.					
	def add_function_id_return_value(self, name, return_type):
		self._global['functions_id_return_values'][name] = return_type
#Función que agrega un valor de retorno a una función
	def add_function_return_value(self, name, value):
		self._global['functions_id_return_values'][name] = value
	
#Funcion que obtiene el tipo del valor de retorno de una función
	def get_function_return_type(self, name):
		print()
		return self._global['functions'][name]['return_type']
#Función que agrega variables  dentro de la tabla de variables. Recibe el tipo de retorno, scope,kind
#nombre  de la variable, valor, direccion de memoria, dimension, 
	def add_variables(self, return_type, scope, kind, name, value, memory_dir, dimension):
		if scope == 'global':
			self._global['global_var'][memory_dir] = {
					'name':name,
					'return_type': return_type,
					'scope': scope,
					'kind': kind,
					'value': value,
					'memory_dir': memory_dir,
					'dimension': dimension,
				}
		else:
			self._global['functions'][scope]['variables'][memory_dir] = {
					'name': name,
					'return_type': return_type,
					'scope': scope,
					'kind': kind,
					'value': value,
					'memory_dir': memory_dir,
					'dimension': dimension,
				}
			self._global['functions'][scope]['temp_count'] += 1
		
			if kind == 'temp_variable':
				if return_type == 1:
					self._global['functions'][scope]['temp_types'][0] += 1
				elif return_type == 2:
					self._global['functions'][scope]['temp_types'][1] += 1
				elif return_type == 3:
					self._global['functions'][scope]['temp_types'][2] += 1
				elif return_type == 4:
					self._global['functions'][scope]['temp_types'][3] += 1
#Función que agrega una variable  constante global. Recibe como parametro el valor de retorno, scope
#kind, valor, direccion de memoria, dimension.
	def add_constant_variables(self, return_type, scope, kind, value, memory_dir, dimension):
		self._global['global_var'][memory_dir] = {
				'return_type': return_type,
				'scope': scope,
				'kind': kind,
				'value': value,
				'memory_dir': memory_dir,
				'dimension': dimension,
				'name': None
			}
	
#Función que elimina una función local al ser terminada. Recibe el scope como parametro
	def remove_local_function(self, scope):
		if scope != 'global':
			del self._global['functions'][scope]['variables']

#Agrega tipos de dato para parametros de funciones. Recibe scope y tipo de retorno como parámetros.
	def add_parameter_type(self,scope,return_type):
		if scope != 'global':
			self._global['functions'][scope]['param_types'].append(return_type)
#Contabiliza los parametros de cada función para generar la firma de la función. Recibe scope como parámetro.			
	def count_params(self, scope):
		if scope != 'global':
			self._global['functions'][scope]['param_count'] = len(self._global['functions'][scope]['param_types']) 
#Contabiliza el total de variables utilizadas para generar firma de la función.
	def count_vars(self, scope):
		if scope != 'global':
			self._global['functions'][scope]['var_count'] = abs(len(self._global['functions'][scope]['variables']['name_var']) - len(self._global['functions'][scope]['param_types']) )
#Obtiene las tablas de variables
	def get_variables_sets(self, var, scope):
		if scope != 'global':
			return var in self._global['global_var']['global_var_names'] or var in self._global['functions'][scope]['variables']['name_var']
		else:
			return var in self._global['global_var']['global_var_names']
	
#Obtiene el tipo de retorno de las variables.Recibe scope y dirección de memoria como parámetro.	
	def get_return_type_variables(self, scope, memory_dir):

		if memory_dir in self._global['global_var']:
			return self._global['global_var'][memory_dir]['return_type']
		elif memory_dir in self._global['functions'][scope]['variables']:
			return self._global['functions'][scope]['variables'][memory_dir]['return_type']
#Obtiene el nombre de la variable. Recibe dirección de memoria y scope como parametro.
	def get_name_variable(self, memory_dir, scope):
		if memory_dir in self._global['global_var']:
			return self._global['global_var'][memory_dir]['name']
		elif memory_dir in self._global['functions'][scope]['variables']:
			print("variable local", scope)
			return self._global['functions'][scope]['variables'][memory_dir]['name']
#Obtiene el valor de la variable. Recibe scope y dirección de memoria como parámetros.			
	def get_value_variable(self, scope, memory_dir):
		if  memory_dir in self._global['global_var']:
			return self._global['global_var'][memory_dir]['value']
		elif memory_dir in self._global['functions'][scope]['variables']:
			return self._global['functions'][scope]['variables'][memory_dir]['value']
#Obtiene dimensión de la variable. Recibe scope y dirección de memoria como parámetros.			
	def get_dimension_variable(self, scope, memory_dir):
		if memory_dir in self._global['global_var']:
			print(self._global['global_var'][memory_dir]['dimension'], "dimension")
			return self._global['global_var'][memory_dir]['dimension']
		elif memory_dir in self._global['functions'][scope]['variables']:
			print(self._global['functions'][scope]['variables'][memory_dir]['dimension'], "dimension")
			return self._global['functions'][scope]['variables'][memory_dir]['dimension']
#Obtiene la dimensión del arreglo. Recibe scope y dirección de memoria como parámetros.
	def get_dimension_array(self, scope, memory_dir):
		if memory_dir in self._global['global_var']:
			return self._global['global_var'][memory_dir]['array_dimension']
		elif memory_dir in self._global['functions'][scope]['variables']:
			return self._global['functions'][scope]['variables'][memory_dir]['array_dimension']
#Asigna un valor a una dirección de memoria. Recibe dirección de memoria y valor como parámetros.
	def set_value(self, scope, memory_dir, value):
		if memory_dir in self._global['global_var']:
			self._global['global_var'][memory_dir]['value'] = value
		elif memory_dir in self._global['functions'][scope]['variables']:
			self._global['functions'][scope]['variables'][memory_dir]['value'] = value	
#Asigna el nombre a una variable. Recibe scope, dirección de memoria y nombre como parámetros.
	def add_variable_name(self, scope, memory_dir, name):
		if memory_dir in self._global['global_var']:
			self._global['global_var'][memory_dir]['name'] = name
		elif memory_dir in self._global['functions'][scope]['variables']:
			self._global['functions'][scope]['variables'][memory_dir]['name'] = name	
