# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
(
    ["1", "3", "0","-12"],
    ["","","","",
     "x1=-2 x2=2"],
    '''
    Revisa si pusiste todos los ( ) en la fórmula general
    Revisa si hiciste el import math
    Revisa si desplegaste las raices dentro de la función
    '''
),
(   ["1", "1", "-2","-1"],
    ["","","","",
     "x1=-0.41421356237309515 x2=2.414213562373095"],
    '''
    Revisa si pusiste todos los ( ) en la fórmula general
    Revisa si hiciste el import math
    Revisa si desplegaste las raices dentro de la función
    '''
),
(   ["1", "1", "1","2"],
    ["","","","",
     "None"],
    '''
    Revisa si revisaste que el determinante sea positivo
    Revisa si hiciste el import math
    Revisa si desplegaste las raices dentro de la función
    '''
),
(   ["2", "3", "25","26"],
    ["","","","",
     "area = 36.0"],
    '''
    opcion 2,  revisa que si leiste los valores como flotantes,
    revisa si la funcion regresa valor
    '''
),
(
    ["2", "10.0", "12.0","15.0"],
    ["","","","",
    "area = 59.81168364124187"],
    '''
    opcion 2,  revisa que si leiste los valores como flotantes,
    revisa si la funcion regresa valor
    '''
),
(
    ["2", "10", "20","25"],
    ["","","","",
    "area = 94.99177595981665"],
    '''
    revisa que si leiste los valores como flotantes,
    revisa si la funcion regresa valor
    '''
),
(   ["4"],
    [""],
    '''
    No debe desplegar nada el programa
    '''
),
(
    ["-1"],
    [""],
    '''
    No debe desplegar nada el programa
    '''
    )

]
