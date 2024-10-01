print("Hello!")
class Dators:
    def __init__(nosaukums, skaits, kas):
        self.name = nosaukums
        self.number = skaits
        self.identity = kas

    def pastastit_par_sevi(self):

        if self.identity == "p":
            teksts = "programmatūra"
        elif self.identity == "d":
            teksts = "detaļa"
        else:
            teksts = self.identity
        print("Produkts {}, skaits {}, kas par produktu {}." .format(self.name, self.number, teksts))
        return "Produkts {}, skaits {}, kas par produktu {}." .format(self.name, self.number, teksts)
    
class detaļa(Mātes plate):
    def __init__(nosaukums, skaits, kas):
        super().__init__(nosaukums, skaits, "d")
        self.info()
    def info(self):
        super().info()
        print(self.name,"detaļa.")

#lieta 1=Dators("Dell", 25, "p")
# programmatura.pastastit_par_sevi()

# lieta 2 = detaļa("Mātes plate", 79, "d")