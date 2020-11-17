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
#TO DO: HANDLE ERRORS
###########################################
	def add_int_global(self):
		if self.memory['dir_global']['int'] < 2000:
			self.memory['dir_global']['int'] += 1
			return self.memory['dir_global']['int']
		else:
			return "error"

	def add_float_global(self):
		if self.memory['dir_global']['float'] < 3000:
			self.memory['dir_global']['float'] += 1
			return self.memory['dir_global']['float'] 
		else:
			return "error"

	def add_char_global(self):
		if self.memory['dir_global']['char'] < 4000:
			self.memory['dir_global']['char'] += 1
			return self.memory['dir_global']['char'] 
		else:
			return "error"

###########################################
# temp global
	def add_int_temp(self):
		if self.memory['global_temp']['int'] < 5000:
			self.memory['global_temp']['int'] += 1
			return self.memory['global_temp']['int']
		else:
			return "error"


	def add_float_temp(self):
		if self.memory['global_temp']['float'] < 6000:
			self.memory['global_temp']['float'] += 1
			return self.memory['global_temp']['float']
		else:
			return "error"

	def add_char_temp(self):
		if self.memory['global_temp']['char'] < 7000:
			self.memory['global_temp']['char'] += 1
			return self.memory['global_temp']['char']
		else:
			return "error"

	def add_bool_temp(self):
		if self.memory['global_temp']['bool'] < 8000:
			self.memory['global_temp']['bool'] += 1
			return self.memory['global_temp']['bool']
		else:
			return "error"

###########################################

	def add_int_local(self):
		if self.memory['dir_local']['int'] < 9000:
			self.memory['dir_local']['int'] += 1
			return self.memory['dir_local']['int']
		else:
			return "error"

	def add_float_local(self):
		if self.memory['dir_local']['float'] < 10000:
			self.memory['dir_local']['float'] += 1
			return self.memory['dir_local']['float']
		else:
			return "error"

	def add_char_local(self):
		if self.memory['dir_local']['char'] < 11000:
			self.memory['dir_local']['char'] += 1
			return self.memory['dir_local']['char']
		else:
			return "error"

###########################################
# local temp
	def add_int_local_temp(self):
		if self.memory['local_temp']['int'] < 12000:
			self.memory['local_temp']['int'] += 1
			return self.memory['local_temp']['int']
		else:
			return "error"

	def add_float_local_temp(self):
		if self.memory['local_temp']['float'] < 13000:
			self.memory['local_temp']['float'] += 1
			return self.memory['local_temp']['float']
		else:
			return "error"

	def add_char_local_temp(self):
		if self.memory['local_temp']['char'] < 14000:
			self.memory['local_temp']['char'] += 1
			return self.memory['local_temp']['char']
		else:
			return "error"


	def add_bool_local_temp(self):
		if self.memory['local_temp']['bool'] < 15000:
			self.memory['local_temp']['bool'] += 1
			return self.memory['local_temp']['bool']
		else:
			return "error"

###########################################
#global constantes
	def add_int_constante(self):
		if self.memory['global_constant']['int'] < 16000:
				self.memory['global_constant']['int'] += 1
				return self.memory['global_constant']['int']
		else:
			return "error"
	
	def add_float_constante(self):
		if self.memory['global_constant']['float'] < 17000:
			self.memory['global_constant']['float'] += 1
			return self.memory['global_constant']['float']
		else:
			return "error"

	def add_char_constante(self):
		if self.memory['global_constant']['char'] < 18000:
			self.memory['global_constant']['char'] += 1
			return self.memory['global_constant']['char']
		else:
			return "error"
		#checar este	
	def add_string_constante(self):
		if self.memory['global_constant']['string'] < 19000:
			self.memory['global_constant']['string'] += 1
			return self.memory['global_constant']['string']
		else:
			return "error"
		

##########################################
	def reset_dir_local(self):
		self.memory['dir_local'] = {
			'int': 8000,
			'float': 9000,
			'char': 10000
		}

	def reset_local_temp(self):
		self.memory['local_temp'] = {
			'int': 11000,
			'float': 12000,
			'char': 13000,
			'bool': 14000
		}

	def reset_global_temp(self):
		 self.memory['global_temp'] = {
			'int': 4000,
			'float': 5000,
			'char': 6000,
			'bool': 7000
		}
#falta get value_memory de las constantes

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
				


