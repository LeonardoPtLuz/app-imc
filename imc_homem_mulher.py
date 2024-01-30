

def imc_masculino(peso: float, altura: float):
        imc_masc = peso / (altura*altura)
        
        if imc_masc < 20.7:
                return(f"{imc_masc:.1f} Abaixo do peso!")
        elif imc_masc >= 20.7 and imc_masc <= 26.4:
                return(f"{imc_masc:.1f} Peso ideal!")
        elif imc_masc >= 26.5 and imc_masc <= 27.8:
                return(f"{imc_masc:.1f} Pouco acima do peso!")
        elif imc_masc >= 27.8 and imc_masc <= 31.1:
                return(f"{imc_masc:.1f} Acima do peso!")
        else:
                return(f"{imc_masc:.1f} Obesidade!")


def imc_feminino(peso: float, altura: float):
        imc_fem = peso / (altura*altura)

        if imc_fem < 19.1:
                return(f"{imc_fem:.1f} Abaixo do peso!")
        elif imc_fem > 19.1 and imc_fem <= 25.8:
                return(f"{imc_fem:.1f} Peso ideal!")
        elif imc_fem >= 25.9 and imc_fem <= 27.3:
                return(f"{imc_fem:.1f} Pouco acima do peso!")
        elif imc_fem >= 27.4 and imc_fem <= 32.3:
                return(f"{imc_fem:.1f} Acima do peso!")
        else:
                return(f"{imc_fem:.1f} Obesidade!")