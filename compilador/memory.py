class Memory:
	def __init__(self):
		self.memory = {
			'dir_global' : {
				# variables globales
				'int': 1000,
				'float': 2000,
				'char': 3000
			},
			'global_temp' : {
		 #temporales utilizadas en operaciones
				'int': 4000,
				'float': 5000,
				'char': 6000,
				'bool': 7000
		 },
			'dir_local': {
				'int': 8000,
				'float': 9000,
				'char': 10000
		 },
		 #temporales t1, t2, t3, etc
			'local_temp' :{
				'int': 11000,
				'float': 12000,
				'char': 13000,
				'bool': 14000
			},
			#direcciones para constantes
			#solo aqui hay string para poner letreros para estatuto escritura, checar para agregar nuevo tipo...
			'global_constant':{
				'int' : 15000,
				'float': 16000,
				'char': 17000,
				'string': 18000
			}
		}

###########################################
#Agregar un nuevo entero global
	def add_int_global(self):
		if self.memory['dir_global']['int'] < 2000:
			self.memory['dir_global']['int'] += 1
			return self.memory['dir_global']['int']
		else:
			raise Exception("ERROR: No hay memoria para enteros globales")
#Agregar un nuevo flotante global
	def add_float_global(self):
		if self.memory['dir_global']['float'] < 3000:
			self.memory['dir_global']['float'] += 1
			return self.memory['dir_global']['float'] 
		else:
			raise Exception("ERROR: No hay memoria para flotantes globales")
#Agregar un nuevo char global
	def add_char_global(self):
		if self.memory['dir_global']['char'] < 4000:
			self.memory['dir_global']['char'] += 1
			return self.memory['dir_global']['char'] 
		else:
			raise Exception("ERROR: No hay memoria para chars globales")

###########################################
#Agregar un nuevo entero temporal
	def add_int_temp(self):
		if self.memory['global_temp']['int'] < 5000:
			self.memory['global_temp']['int'] += 1
			return self.memory['global_temp']['int']
		else:
			raise Exception("ERROR: No hay memoria para temporales enteros globales")

#Agregar un nuevo flotante temporal
	def add_float_temp(self):
		if self.memory['global_temp']['float'] < 6000:
			self.memory['global_temp']['float'] += 1
			return self.memory['global_temp']['float']
		else:
			raise Exception("ERROR: No hay memoria para flotantes temporales globales")

#Agregar un nuevo char temporal
	def add_char_temp(self):
		if self.memory['global_temp']['char'] < 7000:
			self.memory['global_temp']['char'] += 1
			return self.memory['global_temp']['char']
		else:
			raise Exception("ERROR: No hay memoria para chars temporales globales")

#Agregar un nuevo bool temporal
	def add_bool_temp(self):
		if self.memory['global_temp']['bool'] < 8000:
			self.memory['global_temp']['bool'] += 1
			return self.memory['global_temp']['bool']
		else:
			raise Exception("ERROR: No hay memoria para booleanos temporales globales")

###########################################
#Agregar un nuevo entero local
	def add_int_local(self):
		if self.memory['dir_local']['int'] < 9000:
			self.memory['dir_local']['int'] += 1
			return self.memory['dir_local']['int']
		else:
			raise Exception("ERROR: No hay memoria para enteros locales")

#Agregar un nuevo flotante local
	def add_float_local(self):
		if self.memory['dir_local']['float'] < 10000:
			self.memory['dir_local']['float'] += 1
			return self.memory['dir_local']['float']
		else:
			raise Exception("ERROR: No hay memoria para flotantes locales")

#Agregar un nuevo char local
	def add_char_local(self):
		if self.memory['dir_local']['char'] < 11000:
			self.memory['dir_local']['char'] += 1
			return self.memory['dir_local']['char']
		else:
			raise Exception("ERROR: No hay memoria para chars locales")

###########################################
#Agregar un nuevo entero local temporal
	def add_int_local_temp(self):
		if self.memory['local_temp']['int'] < 12000:
			self.memory['local_temp']['int'] += 1
			return self.memory['local_temp']['int']
		else:
			raise Exception("ERROR: No hay memoria para enteros locales temporales")

#Agregar un nuevo flotante localtemporal
	def add_float_local_temp(self):
		if self.memory['local_temp']['float'] < 13000:
			self.memory['local_temp']['float'] += 1
			return self.memory['local_temp']['float']
		else:
			raise Exception("ERROR: No hay memoria para flotantes locales temporales")

#Agregar un nuevo char local temporal
	def add_char_local_temp(self):
		if self.memory['local_temp']['char'] < 14000:
			self.memory['local_temp']['char'] += 1
			return self.memory['local_temp']['char']
		else:
			raise Exception("ERROR: No hay memoria para chars locales temporales")

#Agregar un nuevo bool local temporal
	def add_bool_local_temp(self):
		if self.memory['local_temp']['bool'] < 15000:
			self.memory['local_temp']['bool'] += 1
			return self.memory['local_temp']['bool']
		else:
			raise Exception("ERROR: No hay memoria para booleanos locales temporales")

###########################################
#Agregar un nuevo entero constante
	def add_int_constante(self):
		if self.memory['global_constant']['int'] < 16000:
				self.memory['global_constant']['int'] += 1
				return self.memory['global_constant']['int']
		else:
			raise Exception("ERROR: No hay memoria para enteros constantes globales")

#Agregar un nuevo flotante constante
	def add_float_constante(self):
		if self.memory['global_constant']['float'] < 17000:
			self.memory['global_constant']['float'] += 1
			return self.memory['global_constant']['float']
		else:
			raise Exception("ERROR: No hay memoria para flotantes constantes globales")

#Agregar un nuevo char constante
	def add_char_constante(self):
		if self.memory['global_constant']['char'] < 18000:
			self.memory['global_constant']['char'] += 1
			return self.memory['global_constant']['char']
		else:
			raise Exception("ERROR: No hay memoria para chars constantes globales")

#Agregar un nuevo string constante			
	def add_string_constante(self):
		if self.memory['global_constant']['string'] < 19000:
			self.memory['global_constant']['string'] += 1
			return self.memory['global_constant']['string']
		else:
			raise Exception("ERROR: No hay memoria para string constantes globales")
		

##########################################
#Resetea las direcciones locales
	def reset_dir_local(self):
		self.memory['dir_local'] = {
			'int': 8000,
			'float': 9000,
			'char': 10000
		}
#Resetea las direcciones locales temporales
	def reset_local_temp(self):
		self.memory['local_temp'] = {
			'int': 11000,
			'float': 12000,
			'char': 13000,
			'bool': 14000
		}
#Resetea las direcciones globales temporales
	def reset_global_temp(self):
		 self.memory['global_temp'] = {
			'int': 4000,
			'float': 5000,
			'char': 6000,
			'bool': 7000
		}

#Función que genera una dirección de memoria, recibe como parámetro el tipo de retorno,
#scope, un booleano si es temporal, y un booleano si es constante
	def get_value_memory(self, return_type, scope, temp, const):
		if return_type == 1:
			if const:
				return self.add_int_constante()
			if scope == "global":
				if temp == True:
					return self.add_int_temp()
				else:
					return self.add_int_global()
			else:
				if temp == False:
					return self.add_int_local()
				else:
					return self.add_int_local_temp()
			

		elif return_type == 2:
			if const:
				return self.add_float_constante()
			if scope == "global":
				if temp == True:
					return self.add_float_temp()
				else:
					return self.add_float_global()
			else:
				if temp == False:
					return self.add_float_local()
				else:
					return self.add_float_local_temp()
		elif return_type == 3:
			if const:
				return self.add_char_constante()
			if scope == "global":
				if temp == True:
					return self.add_char_temp()
				else:
					 return self.add_char_global()
			else:
				if temp == False:
					return self.add_char_local()
				else:
					return self.add_char_local_temp()
					
		elif return_type == 4:
			if scope != "global":
				return self.add_bool_local_temp()
			else:
				return self.add_bool_temp()
		
		elif return_type == 6:
			if const:
				return self.add_string_constante()
		
#Función que genera una dirección de memoria para elementos dimensionados 
#dejando el espacio suficiente para todos los elementos del arreglo
#Recibe como parametro el tipo de retorno, scope, un booleano  si es temporal,
#un booleano si es constante y el espacio a dejar.
	def value_memory_array(self, return_type, scope, temp, const, space):
		if return_type == 1:
			if const:
				value = self.add_int_constante() 
				for i in range(space - 1):
					self.add_int_constante()
				print(self.memory)
				return value
					
			if scope == "global":
				if temp == True:
					value = self.add_int_temp()
					for i in range(space - 1):
						self.add_int_temp()
					print(self.memory)
					return value

				else:
					value = self.add_int_global()
					for i in range(space - 1):
						self.add_int_global()
					print(self.memory)
					return value
			else:
				if temp == False:
					value = self.add_int_local()
					for i in range (space-1):
						self.add_int_local()
					print(self.memory)
					return value
				else:
					value = self.add_int_local_temp()
					for i in range (space -1):
						self.add_int_local_temp()
					print(self.memory)
					return value
				
		elif return_type == 2:
			if const:
				value = self.add_float_constante()
				for i in range(space - 1):
					self.add_float_constante()
				return value
			if scope == "global":
				if temp == True:
					value= self.add_float_temp()
					for i in range(space-1):
						self.add_float_temp()
					return value
				else:
					value = self.add_float_global()
					for i in range(space - 1):
						self.add_float_global()
					return value
			else:
				if temp == False:
					value = self.add_float_local()
					for i  in range (space-1):
						self.add_float_local()
					return value
				else:
					value  = self.add_float_local_temp()
					for i in range(space-1):
						self.add_float_local_temp()
					return value
		elif return_type == 3:
			if const:
				value = self.add_char_constante()
				for i in range(space-1):
					self.add_char_constante()
				return value

			if scope == "global":
				if temp == True:
						value =self.add_char_temp()
						for i in range(space-1):
							self.add_char_temp()
						return value
				else:
					value =self.add_char_global()
					for i in range(space-1):
						self.add_char_global()
					return value
			else:
				if temp == False:
					value = self.add_char_local()
					for i in range(space-1):
						self.add_char_local()
					return value
				else:
					value = self.add_char_local_temp()
					for i in range(space-1):
						self.add_char_local_temp()
					return value
						
		elif return_type == 4:
			if scope != "global":
				value = self.add_bool_local_temp()
				for i in range(space-1):
					self.add_bool_local_temp()
				return value
			else:
				value = self.add_bool_temp()
				for i in range(space-1):
					self.add_bool_temp()
				return value
				
		elif return_type == 6:
			if const:
				value = self.add_string_constante()
				for i in range(space-1):
					self.add_string_constante()
				return value

				


