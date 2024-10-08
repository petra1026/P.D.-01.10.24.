class Prece:
    def __init__(self, nosaukums, kas, madeby, skaits=0, cena=0):
        self.name = nosaukums
        self.identity = kas
        self.izgatavotajs = madeby
        self.number = skaits
        self.cena = cena

    def get_identity_text(self):
        if self.identity == "p":
            return "programmatūra"
        elif self.identity == "d":
            return "detaļa"
        elif self.identity == "da":
            return "dators"
        else:
            return self.identity

    def pastastit_par_sevi(self):
        return "Produkts: {}, kas par produktu: {}, izgatavotājs: {}, skaits: {}, cena: {} EUR." .format(
            self.name, self.get_identity_text(), self.izgatavotajs, self.number, self.cena)

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
        elif self.identity == "da":
            teksts = "dators"
        else:
            teksts = self.identity
        print("Produkts: {}, kas par produktu: {}, izgatavotājs: {}, skaits: {}, cena: {} EUR." .format( self.name, self.get_identity_text(), self.izgatavotajs, self.number, self.cena))
        return "Produkts: {}, kas par produktu: {}, izgatavotājs: {}, skaits: {}, cena: {} EUR." .format( self.name, self.get_identity_text(), self.izgatavotajs, self.number, self.cena)

class Mātesplate(Prece):
    def __init__(self, nosaukums, skaits, kas):
        super().__init__(nosaukums, skaits, "d")
        self.info()
    def info(self):
        super().info()
        print(self.name,"detaļa.")

