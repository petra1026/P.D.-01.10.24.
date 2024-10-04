print("Hello!")
class Prece:
    def __init__(self, nosaukums, kas, madeby, skaits = 0):
        self.name = nosaukums
        self.identity = kas
        self.izgatavotajs = madeby
        self.number = skaits
        
       

    def pastastit_par_sevi(self):

        if self.identity == "p":
            teksts = "programmatūra"
        elif self.identity == "d":
            teksts = "detaļa"
        else:
            teksts = self.identity
        print("Produkts: {}, kas par produktu: {}, izgatavotājs: {}, skaits: {}." .format(self.name, teksts, self.izgatavotajs, self.number))
        return "Produkts: {}, kas par produktu: {}, izgatavotājs: {}, skaits: {}." .format(self.name, teksts, self.izgatavotajs, self.number)
    
class Dators(Prece):
    def __init__(self, nosaukums, kas, madeby, skaits = 0):
        self.name = nosaukums
        self.identity = kas
        self.izgatavotajs = madeby
        self.number = skaits
        

    def pastastit_par_sevi(self):

        if self.identity == "p":
            teksts = "programmatūra"
        elif self.identity == "d":
            teksts = "detaļa"
        else:
            teksts = self.identity
        print("Produkts: {}, kas par produktu: {}, izgatavotājs: {}, skaits: {}." .format(self.name, teksts, self.izgatavotajs, self.number))
        return "Produkts: {}, kas par produktu: {}, izgatavotājs: {}, skaits: {}." .format(self.name, teksts, self.izgatavotajs, self.number)
    

class Mātesplate(Prece):
    def __init__(self, nosaukums, skaits, kas):
        super().__init__(nosaukums, skaits, "d")
        self.info()
    def info(self):
        super().info()
        print(self.name,"detaļa.")

#lieta 1= programmatūra("Windows11", "p", 25)
# programmatura.pastastit_par_sevi()

# lieta 2 = detaļa("Mātes plate", "d", 79)