class Classtest:
    def instance_method(self):
        print(f"Called instanced_method of {self}")
    
    @classmethod
    def class_method(cls):
        print(f"Called class method of {cls}")

    #El estatic method no necesita un argumento
    @staticmethod
    def static_method():
        print(f"Called static method")

#Para llamara la clase hay dos formas

#1.-
# test = Classtest()
# test.instance_method()
# Classtest.instance_method(test)

Classtest.class_method()
Classtest.static_method()