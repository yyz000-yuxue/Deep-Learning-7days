
class Cat(object):
    """
    猫科动物类
    """
    # 类的属性
    tag = 'Cat base'

    def __init__(self, name):
        # 实例化后的属性
        self.name = name
        pass

    def eat(self):
        """
        吃
        :return:
        """
        pass

class Tiger(Cat):
    pass