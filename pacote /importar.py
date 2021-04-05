class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def perimetro(self):
        """Essa função calcula o perimetro de um quadrado (isso é um doc str)"""
        return 4 * self.lado

    def area(self):
        return self.lado * self.lado


class Animal: 
    def __init__(self, name, age, sexo=None): 
         print(f'hi {name}') 
         print(f'hi {name}') 
         print(f'hi {name}') 
         print(f'hi {name}') 
         self.name = name 
         self.age = age 
         self.external_id = Animal.generate_external_id(self.name, age) 
         self.external_id2 = self.generate_external_id(name, age) 
  
    def show_name(self): 
         print(self.name) 
          
     @property 
    def year_of_birth(self): 
         return datetime.datetime.now().year - self.age 
  
     @classmethod 
    def generate_external_id(cls, name, age): 
         return f'{name} -- {age}'