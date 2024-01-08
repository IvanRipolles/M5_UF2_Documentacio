class arees:
    """clase que calcula arees de diferentes formes"""

    def areaCuadrat(lado):
        """Calcula l'area d'un cuadrat."""
        return "l'area del cuadrat es: " + str (lado*lado)
    def areaRectangle(base, altura):
        """Calcula l'area d'un rectangle."""
        return "l'area del rectangle es: " + str (base * altura)

    def areaTriangle(base, altura):
        """Calcula l'area d'un triangle."""
        return "l'area del triangle es: " + str ((base*altura)/2)
    
"""defineix els parametres i imprimeix en pantalla les arees"""
print(arees.areaCuadrat(2))
print(arees.areaRectangle(3,4))
print(arees.areaTriangle(7,4))
