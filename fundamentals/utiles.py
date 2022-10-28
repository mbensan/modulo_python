class Utiles:

    @staticmethod
    def promedio(lista):
        suma = sum(lista)
        return suma / len(lista)
    
    @staticmethod
    def variance(data):
        # Number of observations
        n = len(data)
        # Mean of the data
        mean = sum(data) / n
        # Square deviations
        deviations = [(x - mean) ** 2 for x in data]
        # Variance
        variance = sum(deviations) / n
        return variance
    
    @staticmethod
    def maximo(lista):
        return max(lista)
