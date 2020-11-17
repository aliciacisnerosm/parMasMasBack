from collections import deque
from copy import deepcopy,copy

class VirtualMachine:
	def __init__(self, arr_quadruples, general_dir):
		self.global_memory = MemoryMap(general_dir, 'global') # memory global - variables temporales & constantes 
		self.arr_quadruples = arr_quadruples 
		self.execution_stack = deque()
		self.local_memory = MemoryMap(None, 'local')
		self.stack_pointers = deque()
		self.general_dir = general_dir
		self.aux_memory = None


	def get_memory(self, memory_dir):
		if (memory_dir >= 1000 and memory_dir < 8000) or (memory_dir >= 15000 and memory_dir < 19000):
			return self.global_memory

		elif (memory_dir >= 8000 and memory_dir < 15000) and self.aux_memory == None :
			return self.local_memory
		else:
			if self.aux_memory.get_value(memory_dir) != None:
				return self.aux_memory
			else:
				return self.local_memory


	def process_quadruples(self):
		pointer = 0
		params = []
		counter = 1
		while (pointer < len(self.arr_quadruples)):
			print("CUADRUPLO ACTUAL ->>>", self.arr_quadruples[pointer])
			
			if self.arr_quadruples[pointer][0] == '+':
				left_value = self.get_memory(self.arr_quadruples[pointer][1]).get_value(self.arr_quadruples[pointer][1])
				right_value =  self.get_memory(self.arr_quadruples[pointer][2]).get_value(self.arr_quadruples[pointer][2])
				result = left_value + right_value
				self.get_memory(self.arr_quadruples[pointer][3]).set_value(self.arr_quadruples[pointer][3], result)
				pointer += 1
		
			elif self.arr_quadruples[pointer][0] == '-':
				left_value = self.get_memory(self.arr_quadruples[pointer][1]).get_value(self.arr_quadruples[pointer][1])
				right_value =  self.get_memory(self.arr_quadruples[pointer][2]).get_value(self.arr_quadruples[pointer][2])
				result = left_value - right_value
				self.get_memory(self.arr_quadruples[pointer][3]).set_value(self.arr_quadruples[pointer][3], result)
				pointer += 1
				
			elif self.arr_quadruples[pointer][0] == '=':
				value_memory = self.get_memory(self.arr_quadruples[pointer][1])
				value = value_memory.get_value(self.arr_quadruples[pointer][1])
				self.get_memory(self.arr_quadruples[pointer][3]).set_value(self.arr_quadruples[pointer][3], value)
				pointer += 1

			elif self.arr_quadruples[pointer][0] == '*':
				left_value = self.get_memory(self.arr_quadruples[pointer][1]).get_value(self.arr_quadruples[pointer][1])
				right_value =  self.get_memory(self.arr_quadruples[pointer][2]).get_value(self.arr_quadruples[pointer][2])
				result = left_value * right_value
				self.get_memory(self.arr_quadruples[pointer][3]).set_value(self.arr_quadruples[pointer][3], result)
				pointer += 1
				
			elif self.arr_quadruples[pointer][0] == '/':
				left_value = self.get_memory(self.arr_quadruples[pointer][1]).get_value(self.arr_quadruples[pointer][1])
				right_value =  self.get_memory(self.arr_quadruples[pointer][2]).get_value(self.arr_quadruples[pointer][2])
				result = left_value / right_value
				self.get_memory(self.arr_quadruples[pointer][3]).set_value(self.arr_quadruples[pointer][3], result)
				pointer += 1

			elif self.arr_quadruples[pointer][0] == 'read':
				value_memory = self.get_memory(self.arr_quadruples[pointer][3]).get_value(self.arr_quadruples[pointer][3])
				pointer += 1
				
			elif self.arr_quadruples[pointer][0]== 'write':
				value_memory = self.get_memory(self.arr_quadruples[pointer][3]).get_value(self.arr_quadruples[pointer][3])
				print("write", self.get_memory(self.arr_quadruples[pointer][3]).type_int)
				print("local_memory en write -> ", self.local_memory.type_int)
				if self.aux_memory != None:
					print("aux_memory en write -> ", self.aux_memory.type_int)
				print("memory que utiliza realmente ->", id(self.get_memory(self.arr_quadruples[pointer][3])))
				pointer += 1
				print(counter, value_memory)
				counter += 1

			elif self.arr_quadruples[pointer][0] == 'and':
				left_value = self.get_memory(self.arr_quadruples[pointer][1]).get_value(self.arr_quadruples[pointer][1])
				right_value =  self.get_memory(self.arr_quadruples[pointer][2]).get_value(self.arr_quadruples[pointer][2])
				result = left_value and right_value
				self.get_memory(self.arr_quadruples[pointer][3]).set_value(self.arr_quadruples[pointer][3], result)
				pointer += 1

			elif self.arr_quadruples[pointer][0] == 'or':
				left_value = self.get_memory(self.arr_quadruples[pointer][1]).get_value(self.arr_quadruples[pointer][1])
				right_value =  self.get_memory(self.arr_quadruples[pointer][2]).get_value(self.arr_quadruples[pointer][2])
				result = left_value or right_value
				self.get_memory(self.arr_quadruples[pointer][3]).set_value(self.arr_quadruples[pointer][3], result)
				pointer += 1

			elif self.arr_quadruples[pointer][0] == '>':
				left_value = self.get_memory(self.arr_quadruples[pointer][1]).get_value(self.arr_quadruples[pointer][1])
				right_value =  self.get_memory(self.arr_quadruples[pointer][2]).get_value(self.arr_quadruples[pointer][2])
				result = left_value > right_value
				self.get_memory(self.arr_quadruples[pointer][3]).set_value(self.arr_quadruples[pointer][3], result)
				pointer += 1

			elif self.arr_quadruples[pointer][0] == '<':
				left_value = self.get_memory(self.arr_quadruples[pointer][1]).get_value(self.arr_quadruples[pointer][1])
				right_value =  self.get_memory(self.arr_quadruples[pointer][2]).get_value(self.arr_quadruples[pointer][2])
				result = left_value < right_value
				self.get_memory(self.arr_quadruples[pointer][3]).set_value(self.arr_quadruples[pointer][3], result)
				pointer += 1

			elif self.arr_quadruples[pointer][0] == '>=':
				left_value = self.get_memory(self.arr_quadruples[pointer][1]).get_value(self.arr_quadruples[pointer][1])
				right_value =  self.get_memory(self.arr_quadruples[pointer][2]).get_value(self.arr_quadruples[pointer][2])
				result = left_value >= right_value
				self.get_memory(self.arr_quadruples[pointer][3]).set_value(self.arr_quadruples[pointer][3], result)
				pointer += 1
				
			elif self.arr_quadruples[pointer][0] == '<=':
				left_value = self.get_memory(self.arr_quadruples[pointer][1]).get_value(self.arr_quadruples[pointer][1])
				right_value =  self.get_memory(self.arr_quadruples[pointer][2]).get_value(self.arr_quadruples[pointer][2])
				result = left_value <= right_value
				self.get_memory(self.arr_quadruples[pointer][3]).set_value(self.arr_quadruples[pointer][3], result)
				pointer += 1
				
			elif self.arr_quadruples[pointer][0] == '<>':
				left_value = self.get_memory(self.arr_quadruples[pointer][1]).get_value(self.arr_quadruples[pointer][1])
				right_value =  self.get_memory(self.arr_quadruples[pointer][2]).get_value(self.arr_quadruples[pointer][2])
				result = left_value != right_value
				self.get_memory(self.arr_quadruples[pointer][3]).set_value(self.arr_quadruples[pointer][3], result)
				pointer += 1
				
			elif self.arr_quadruples[pointer][0] == '==':
				left_value = self.get_memory(self.arr_quadruples[pointer][1]).get_value(self.arr_quadruples[pointer][1])
				right_value =  self.get_memory(self.arr_quadruples[pointer][2]).get_value(self.arr_quadruples[pointer][2])
				result = left_value == right_value
				self.get_memory(self.arr_quadruples[pointer][3]).set_value(self.arr_quadruples[pointer][3], result)
				pointer += 1

			elif self.arr_quadruples[pointer][0] == 'GOTO':
				next_quadruple = self.arr_quadruples[pointer][3]
				pointer = next_quadruple

			elif self.arr_quadruples[pointer][0] == 'ERA':
				self.aux_memory = deepcopy(self.local_memory)
				self.local_memory = MemoryMap(self.general_dir, self.arr_quadruples[pointer][3])
				self.local_memory.get_local_values()
				pointer +=1
			elif self.arr_quadruples[pointer][0] == 'ENDFUNC':
				pointer = self.stack_pointers.pop()
				self.execution_stack.pop()
				if(len(self.execution_stack)!=0):
					self.local_memory=self.execution_stack[len(self.execution_stack)-1]
				print("--------------------------TERMINA----------------------------------")

			elif self.arr_quadruples[pointer][0] == 'GOTOF':
				left_value = self.get_memory(self.arr_quadruples[pointer][1]).get_value(self.arr_quadruples[pointer][1])
				print(left_value, "left_value")
				if left_value == False:
					pointer = self.arr_quadruples[pointer][3]
				else:
					pointer += 1
		
			elif self.arr_quadruples[pointer][0] == 'GOSUB':
				self.aux_memory = None
				self.stack_pointers.append(pointer + 1)		# cool
				pointer = self.arr_quadruples[pointer][3] # cool
				self.execution_stack.append(self.local_memory) 
				print("------------------------EMPIEZA------------------------------------")
				self.local_memory.add_params(params)
				params = []
				
			elif self.arr_quadruples[pointer][0] == 'PARAM':
				value_memory = self.get_memory(self.arr_quadruples[pointer][1])
				value = value_memory.get_value(self.arr_quadruples[pointer][1])
				params.append(value)
				pointer +=1
			elif self.arr_quadruples[pointer][0] == 'RETURN':
				value = self.get_memory(self.arr_quadruples[pointer][3]).get_value(self.arr_quadruples[pointer][3])
				self.global_memory.add_return_value(value, self.local_memory.return_type, self.local_memory.function_name)
				pointer += 1
				
				value_2 = self.get_memory(self.arr_quadruples[pointer][1]).get_value(self.arr_quadruples[pointer][1])
				self.get_memory(self.arr_quadruples[pointer][3]).set_value(self.arr_quadruples[pointer][3], value)
				pointer = self.stack_pointers.pop()
				self.execution_stack.pop()

				if(len(self.execution_stack)!=0):
					self.local_memory=self.execution_stack[len(self.execution_stack)-1]
				print("memoria - return", self.global_memory.type_int)
				
			else:
				pointer += 1

	def execute(self): 
		print("entra a execute")
		print(self.arr_quadruples)
		self.global_memory.init_global_memory()
		self.process_quadruples()
		print(self.execution_stack)


class MemoryMap:
	def __init__(self, general_dir, function_name):				
		self.general_dir = general_dir
		self.type_int = dict()
		self.type_float = dict()
		self.type_char = dict()
		self.type_bool = dict()
		self.type_str = dict() 
		self.function_name = function_name
		self.init = None
		self.param_types = None 
		self.param_count = None
		self.var_count = None
		self.var_types = None
		self.temp_count = None
		self.return_type = None
		self.temp_types = None
		self.counter_int = 11001
		self.counter_float = 12001
		self.counter_char = 13001

	def get_local_values(self):
		if self.function_name != 'global':
			self.init = self.general_dir['functions'][self.function_name]['init']
			self.param_types = self.general_dir['functions'].get(self.function_name).get('param_types') 
			self.param_count = self.general_dir['functions'].get(self.function_name).get('param_count') 
			self.var_count = self.general_dir['functions'].get(self.function_name).get('var_count') 
			self.var_types = self.general_dir['functions'].get(self.function_name).get('var_types') 
			self.temp_count = self.general_dir['functions'].get(self.function_name).get('temp_count') 
			self.return_type = self.general_dir['functions'].get(self.function_name).get('return_type') 
			self.temp_types = self.general_dir['functions'].get(self.function_name).get('temp_types')

	def init_global_memory(self):
		if self.function_name == 'global':
			
			for i in self.general_dir['global_var']:
				if i != 'global_var_names':
					# int
					if (i >= 1000 and i < 2000) or (i >= 4000 and i < 5000) or (i >= 15000 and i < 16000):
						self.type_int[i] = {
							'value': self.general_dir['global_var'][i]['value']
						}
					# float
					elif (i >= 2000 and i < 3000) or (i >= 5000 and i < 6000) or (i >= 16000 and i < 17000):
						self.type_float[i] = {
							'value': self.general_dir['global_var'][i]['value']
						}
					#char
					elif (i >= 4000 and i < 5000) or (i >= 6000 and i < 7000) or (i >= 17000 and i < 18000):
						self.type_char[i] = {
							'value': self.general_dir['global_var'][i]['value']
						}
					#strings
					elif i >= 18000 and i < 19000:
						self.type_str[i] = {
							'value': self.general_dir['global_var'][i]['value']
						}

			print(1, self.type_int, file=open("output_global_int.txt", "w"))
			print(2, self.type_float,file=open("output_global_float.txt", "w"))
			print(3, self.type_char, file=open("output_global_char.txt", "w"))
			print(4, self.type_str, file=open("output_global_string.txt", "w"))

	def add_return_value(self, value, return_type, function_name):
		if return_type == 1:
			self.type_int[function_name] = {
				'value': value
			}
			print("entra a return value",self.type_int[function_name], "int")
		elif return_type == 2:
			self.type_float[function_name] = {
				'value': value
			}
			print("entra a return value",self.type_float[function_name], "float")
		elif return_type == 3:
			self.type_char[function_name] = {
				'value': value
			}
			print("entra a return value",self.type_char[function_name], "char")


	def get_value(self, memory_dir):
		if (memory_dir >= 8000 and memory_dir < 9000) or (memory_dir >= 11000 and memory_dir < 12000)	or (memory_dir >= 1000 and memory_dir < 2000) or (memory_dir >= 4000 and memory_dir < 5000) or (memory_dir >= 15000 and memory_dir < 16000):
			if memory_dir in self.type_int:
				return self.type_int[memory_dir]['value']
			else:
				return self.new_int(memory_dir)
		elif (memory_dir >= 2000 and memory_dir < 3000) or (memory_dir >= 5000 and memory_dir < 6000) or (memory_dir >= 9000 and memory_dir < 10000) or (memory_dir >= 12000 and memory_dir < 13000) or (memory_dir >= 16000 and memory_dir < 17000):
			if memory_dir in self.type_float:
				return self.type_float[memory_dir]['value']
			else:
				return self.new_float(memory_dir)
		elif (memory_dir >= 10000 and memory_dir < 11000) or (memory_dir >= 13000 and memory_dir < 14000) or ( memory_dir >= 17000 and memory_dir < 18000) or (memory_dir >= 3000 and memory_dir < 4000) or (memory_dir >= 6000 and memory_dir < 7000):
			if memory_dir in self.type_char:
				return self.type_char[memory_dir]['value']
			else:
				return self.new_char(memory_dir)
		elif (memory_dir>=14000 and memory_dir < 15000):
			if memory_dir in self.type_bool:
				return self.type_bool[memory_dir]['value']
			else:
				return self.new_bool(memory_dir)
		elif (memory_dir>= 18000 and memory_dir<19000):
			if memory_dir in self.type_str:
				return self.type_str[memory_dir]['value']
			else:
				return self.new_str(memory_dir)

	def new_int(self, memory_dir):
		self.type_int[memory_dir] = {
			'value': None
				}
		return self.type_int[memory_dir]['value']

	def new_float(self, memory_dir):
		self.type_float[memory_dir] = {
			'value': None
		}
		return self.type_float[memory_dir]['value']

	def new_char(self, memory_dir):
		self.type_char[memory_dir] = {
			'value': None
		}
		return self.type_char[memory_dir]['value']

	def new_bool(self, memory_dir):
		self.type_bool[memory_dir] = {
			'value': None
		}
		print(self.type_bool[memory_dir]['value'], "este es bool - crea")
		return self.type_bool[memory_dir]['value']

	def new_str(self, memory_dir):
		self.type_str[memory_dir] = {
			'value': None
		}
		return self.type_str[memory_dir]['value']
	
	def set_value(self, memory_dir, value):
		if (memory_dir >= 8000 and memory_dir < 9000) or (memory_dir >= 11000 and memory_dir < 12000)	or (memory_dir >= 1000 and memory_dir < 2000) or (memory_dir >= 4000 and memory_dir < 5000) or (memory_dir >= 15000 and memory_dir < 16000):
			if memory_dir not in self.type_int:
				self.type_int[memory_dir] = {
					'value': value
				}
				print(self.type_int[memory_dir], "setttt")
			else:
				self.type_int[memory_dir]['value'] = value
				print(self.type_int[memory_dir])

		elif (memory_dir >= 2000 and memory_dir < 3000) or (memory_dir >= 5000 and memory_dir < 6000) or (memory_dir >= 9000 and memory_dir < 10000) or (memory_dir >= 12000 and memory_dir < 13000) or (memory_dir >= 16000 and memory_dir < 17000):
			if memory_dir not in self.type_int:
				self.type_float[memory_dir] = {
					'value': value
				}
				print(self.type_float[memory_dir], "setttt")
			else:
				self.type_float[memory_dir]['value'] = value
				print(self.type_float[memory_dir])

		elif (memory_dir >= 10000 and memory_dir < 11000) or (memory_dir >= 13000 and memory_dir < 14000) or ( memory_dir >= 17000 and memory_dir < 18000) or (memory_dir >= 3000 and memory_dir < 4000) or (memory_dir >= 6000 and memory_dir < 7000):
			if memory_dir not in self.type_char:
				self.type_char[memory_dir] = {
					'value': value
				}
			else:
				self.type_char[memory_dir]['value'] = value
				print(self.type_char[memory_dir])

		elif (memory_dir>=14000 and memory_dir < 15000):
			if memory_dir not in self.type_bool:
				self.type_bool[memory_dir] = {
					'value': value
				}
			else:
				self.type_bool[memory_dir]['value'] = value
				print(self.type_bool[memory_dir])

		elif (memory_dir >= 18000 and memory_dir < 19000):
			if memory_dir not in self.type_str:
				self.type_str[memory_dir] = {
					'value': value
				}
			else:
				self.type_str[memory_dir]['value'] = value
				print(self.type_str[memory_dir])
	
	def add_params(self, params):
		for index, value in enumerate(params):
			if type(value) is int:
				if self.param_types[index] != 0:
					self.type_int[self.counter_int] = {
						'value': value
					}
					self.counter_int += 1
				else:
					print("Error - parametro #", index +1, "en", self.function_name, "esta incorrecto")
			elif type(value) is float:
				if self.param_types[index] != 1:
					self.type_float[self.counter_float] = {
						'value': value
					}
					self.counter_int += 1
				else:
					print("Error - parametro #", index +1, "en", self.function_name, "esta incorrecto")
			else:
				if self.param_types[index] != 2:
					self.type_char[self.counter_char] = {
						'value': value
					}
					self.counter_int += 1
				else:
					print("Error - parametro #", index +1, "en", self.function_name, "esta incorrecto")
	







