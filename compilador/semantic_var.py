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
	
	def get_init_function(self, name):
		return self._global['functions'][name]['init']

	def verify_function_id(self, name):
		return name in self._global['functions']['func_names']
		
	#declara variables 
	def declare_variables(self, return_type, scope, kind, name, value, memory_dir, dimension):
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
					'dimension': dimension
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
		
		return "error en memory dir"

	def add_function_id_return_value(self, name, return_type):
		self._global['functions_id_return_values'][name] = return_type
	
	def add_function_return_value(self, name, value):
		self._global['functions_id_return_values'][name] = value
	# agrega variables temporales

	def get_function_return_type(self, name):
		print()
		return self._global['functions'][name]['return_type']
		

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

	def remove_local_function(self, scope):
		if scope != 'global':
			del self._global['functions'][scope]['variables']

	#agrega tipos de dato para parametros de funciones
	def add_parameter_type(self,scope,return_type):
		if scope != 'global':
			self._global['functions'][scope]['param_types'].append(return_type)
			
	def count_params(self, scope):
		if scope != 'global':
			self._global['functions'][scope]['param_count'] = len(self._global['functions'][scope]['param_types']) 

	def count_vars(self, scope):
		if scope != 'global':
			self._global['functions'][scope]['var_count'] = abs(len(self._global['functions'][scope]['variables']['name_var']) - len(self._global['functions'][scope]['param_types']) )

	def get_variables_sets(self, var, scope):
		if scope != 'global':
			return var in self._global['global_var']['global_var_names'] or var in self._global['functions'][scope]['variables']['name_var']
		else:
			return var in self._global['global_var']['global_var_names']
	
	def get_return_type_variables(self, scope, memory_dir):

		if memory_dir in self._global['global_var']:
			return self._global['global_var'][memory_dir]['return_type']
		elif memory_dir in self._global['functions'][scope]['variables']:
			return self._global['functions'][scope]['variables'][memory_dir]['return_type']

	def get_name_variable(self, memory_dir, scope):	
		if memory_dir in self._global['global_var']:
			return self._global['global_var'][memory_dir]['name']
		elif memory_dir in self._global['functions'][scope]['variables']:
			return self._global['functions'][scope]['variables'][memory_dir]['name']
			
	def get_value_variable(self, scope, memory_dir):
		if  memory_dir in self._global['global_var']:
			return self._global['global_var'][memory_dir]['value']
		elif memory_dir in self._global['functions'][scope]['variables']:
			return self._global['functions'][scope]['variables'][memory_dir]['value']
			
	def set_value(self, scope, memory_dir, value):
		if memory_dir in self._global['global_var']:
			self._global['global_var'][memory_dir]['value'] = value
		elif memory_dir in self._global['functions'][scope]['variables']:
			self._global['functions'][scope]['variables'][memory_dir]['value'] = value	

	def add_variable_name(self, scope, memory_dir, name):
		if memory_dir in self._global['global_var']:
			self._global['global_var'][memory_dir]['name'] = name
		elif memory_dir in self._global['functions'][scope]['variables']:
			self._global['functions'][scope]['variables'][memory_dir]['name'] = name	

	#hacer funcion get param_types de la funcion