import zeep
# URL del WSDL
wsdl = "http://www.dneonline.com/calculator.asmx?WSDL"
# Crear un cliente SOAP
client = zeep.Client(wsdl=wsdl)
# Suma
try:
    resultado_suma = client.service.Add(intA=5, intB=3)
    print(f"El resultado de la suma es: {resultado_suma}")
except Exception as e:
    print(f"Error en la operación de suma: {e}")
# Multiplicación
try:
    resultado_multiplicacion = client.service.Multiply(intA=5, intB=5)
    print(f"El resultado de la multiplicación es: {resultado_multiplicacion}")
except Exception as e:
    print(f"Error en la operación de multiplicación: {e}")
# Resta
try:
    resultado_resta = client.service.Subtract(intA=5, intB=5)
    print(f"El resultado de la resta es: {resultado_resta}")
except Exception as e:
    print(f"Error en la operación de resta: {e}")
# División
try:
    resultado_division = client.service.Divide(intA=10, intB=5)
    print(f"El resultado de la división es: {resultado_division}")
except Exception as e:
    print(f"Error en la operación de división: {e}")