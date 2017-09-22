class User():


	def __init__(self, first_name, last_name, age):

		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		
		self.login_attempts = 100

	def describle_user(self):

		print ('名号：' + self.first_name + ' ' + self.last_name)
		print ('年龄:' + self.age)
		

	def greet_user(self):

		print (self.last_name + ', 大侠，早晨好！今日宇宙平安，万事如常！')

	def increment_login_attempts(self):
		"""将数量增加1"""

		self.login_attempts += 1

	def reset_login_attempts(self):
		"""将后台人数重置为0"""

		self.login_attempts = 0

class Privileges():
	"""教主权限"""

	def __init__(self,privileges=[]):
		"""初始化权限"""
		self.privileges = ['任命长老', '学习乾坤大挪移神功', '掌握圣火令']

	def show_privileges(self):
		"""显示管理员的权限"""
		print ('管理员的权限有： ' + str(self.privileges) + ' .')



class Admin(User):
	"""管理员列表"""

	def __init__(self, first_name, last_name, age):
		"""初始化父类的属性"""
		super().__init__(first_name, last_name, age)
		self.privileges = Privileges()
		

	


阳顶天 = Admin('教主', '阳顶天', '不惑之年')
阳顶天.describle_user()
阳顶天.privileges.show_privileges()
