class MySingleAttributedClass:
    __slots__ = 'single_permitted_attribute'


instance = MySingleAttributedClass()
instance.single_permitted_attribute = 5
try:
    instance.x = 5
except:
    print('Forbidden attribute to get/set')
