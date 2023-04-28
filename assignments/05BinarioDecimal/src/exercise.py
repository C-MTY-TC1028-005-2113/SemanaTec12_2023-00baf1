"""

Nombre:                                  Matricula:

Fecha:                                 Carrera:

"""


def main():
    series = [['I Am Not an Animal', 'Animation',  'GB', '349', '10/05/04', '9.5'],
    ['Chernobyl', 'Drama',  'US', '595', '06/05/19', '8.5'],
    ['Rick and Morty', 'Animation',  'US', '1395', '02/12/13', '8.5'],
    ['Breaking Bad', 'Drama',  'US', '3560', '20/01/08', '8.5'],
    ['Hunter x Hunter', 'Animation',  'JP', '152', '02/10/11', '8.5'],
    ['Sherlock', 'Crime',  'GB', '1885', '25/07/10', '8.5'],
    ['Planet Earth II', 'Documentary',  'GB', '348', '06/11/16', '8.5']]

    alumnos =  [ ['Jose', 'ITC', 'MX', '300', '10/05/04', '99'],
    ['Nodal', 'INE', 'US', '500', '06/05/19', '200'],
    ['Andres', 'IFI',  'MX', '1200', '02/12/13', '100'],
    ['Ana Victoria', 'IRS', 'US', '5600', '20/01/08', '100'],
    ['Alexa', 'IFI',  'MX', '5000', '02/10/11', '100'],
    ['Sofia', 'ITC',  'MX', '4000', '25/07/10', '90'],
    ['Ada', 'ITC', 'MX', '1000', '06/11/16', '99']]

    # Leer  la matriz que va a utilizar
    m = int(input())
    
    # Selecciona la matriz que va a usar
    if m == 1 :
        matriz = series.copy( )
    else:
        matriz = alumnos.copy( )

    # leer la opcion que va a calcular  y/o desplegar
    opcion = int(input())

    # Añade las instrucciones de cada opcion, borra el pass
    if opcion == 1:
        pass
        

    elif opcion == 2:
        pass
        
    elif opcion == 3:
        pass
    
        print("Promedio 1:", round(promedio, 2))
        print("Promedio 2:", round(promedio_minutos, 2))


if __name__=='__main__':
    main()
