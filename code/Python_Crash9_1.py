class Restaurant():


	def __init__(self, restaurant_name, cuisine_type):

		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):

		print (self.restaurant_name)
		print (self.cuisine_type)

	def open_restaurant(self):

		print ('正在营业')

	def num_served_restaurant(self):
		print ('本月累积用餐顾客：' + str(self.number_served) + '人。')

	def set_number_served(self,peoples):
		"""设置就餐人数"""

		self.number_served = peoples

	def increment_number_served(self,people):
		"""设置每日递增就餐人数"""

		self.number_served += people


"""restaurant = Restaurant('restaurant','restaurant')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(200)
restaurant.increment_number_served(50)
restaurant.num_served_restaurant()"""

"""西北一霸 = Restaurant('西北一霸','兰州拉面')
西北一霸.describe_restaurant()
西北一霸.open_restaurant()

四川小霸王 = Restaurant('四川小霸王','四川小炒')
四川小霸王.describe_restaurant()
四川小霸王.open_restaurant()

包子孙二娘 = Restaurant('包子孙二娘','自助火锅')
包子孙二娘.describe_restaurant()
包子孙二娘.open_restaurant()
"""

class User():


	def __init__(self, first_name, last_name, age, telephone, email, qq):

		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.telephone = telephone
		self.email = email
		self.qq =  qq
		self.login_attempts = 100

	def describle_user(self):

		print ('名号：' + self.first_name + ' ' + self.last_name)
		print ('生辰:' + self.age)
		print ('电话:' + self.telephone)
		print ('邮箱:' + self.email)
		print ('QQ:' + self.qq)

	def greet_user(self):

		print (self.last_name + ', 大侠，早晨好！今日宇宙平安，万事如常！')

	def increment_login_attempts(self):
		"""将数量增加1"""

		self.login_attempts += 1

	def reset_login_attempts(self):
		"""将后台人数重置为0"""

		self.login_attempts = 0


"""Bob = User('Tony', 'Bob', '17', '0109999999', '898989', '000000')
for i in range(15):
	Bob.increment_login_attempts()

print ('Bob is :' + str(Bob.login_attempts))

Bob.reset_login_attempts()

print ('Now,Bob is :' + str(Bob.login_attempts))
"""


"""赵子龙 = User('常山小白龙枪王之王赵王爷','赵子龙','十八岁','13910000000','zhaoyun@shuhan.com','989898')
张飞 = User('长坂坡一夫当关万万军胆寒张翼德','张飞','二十八岁','13910098768','yide@shuhan.com','564789')
诸葛亮 = User('大梦谁先觉平生我自知卧龙先生诸葛孔明','小亮','二十五岁','13910000001','liangaiyueying@shuhan.com','111112')
关羽 = User('过五关斩六将武圣真君红牌全是杀关云长','关羽','三十岁','13910000002','xiaoyu@shuhan.com','989800')
周飞亮 = User('情痴为爱错吃毒丸成毒人不忘初心','周飞亮','十三岁','18820000022','feiliangxiaoyun@wudujiao.com','1234567')

赵子龙.describle_user()
赵子龙.greet_user()
张飞.describle_user()
张飞.greet_user()
诸葛亮.describle_user()
诸葛亮.greet_user()
关羽.describle_user()
关羽.greet_user()

周飞亮.describle_user()
周飞亮.greet_user()
"""

class IceCreamStand(Restaurant):
	"""冰淇凌小店"""

	def __init__(self, restaurant_name, cuisine_type):
		"""初始化父类的属性"""

		super().__init__(restaurant_name,cuisine_type)
		self.flavors = ['原味巧克力', '阿尔法奶油', "青春芒果"]

	def icecreams_flavors(self):
		"""各种口味冰淇凌列表"""

		print ("本店的冰淇凌口味有： " + str(self.flavors) + " 可供选择！")


一乐冰淇凌 = IceCreamStand("一乐冰屋", "休闲小店")
一乐冰淇凌.describe_restaurant()
一乐冰淇凌.open_restaurant()
一乐冰淇凌.icecreams_flavors()
