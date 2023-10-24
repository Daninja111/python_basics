#En este modulo tendremos los generadores y los decoradores

#Sector Perfumeria P - num
def turno_perfumeria(funcion):
    def interior():
        print("Su turno es: /n")
        funcion()
        print("/n Aguarde su turno")
    return interior

def gen_perfum():
    num = 0
    while True:
        yield num
        num += 1
perfumeria = gen_perfum()
print(f"P - {next(perfumeria)}")
deco_perfumeria = turno_perfumeria(gen_perfum)

#Sector Medicamentos M - num
def turno_medicamentos():
    def gen_meds():
        num = 0
        while True:
            yield num
            num += 1

    medicamentos = gen_meds()
    print(f"M - {next(medicamentos)}")



#Sector Cosmetica C - num
def turno_cosmetica():
    def gen_cosmetics():
        num = 0
        while True:
            yield num
            num += 1

    cosmetica = gen_cosmetics()
    print(f"C - {next(cosmetica)}")