# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1

(
[1, 1],
["","",
"1 I Am Not an Animal Animation",
"2 Chernobyl Drama",
"3 Rick and Morty Animation",
"4 Breaking Bad Drama",
"5 Hunter x Hunter Animation",
"6 Sherlock Crime",
"7 Planet Earth II Documentary"],
"Debe salir: lo que te indica el caso de prueba1"
),
(
[1, 2],
["","",
"Animation 3",
"Drama 2",
"Crime 1",
"Documentary 1",
],
"Debe salir: lo que te indica el caso de prueba2"
),
(
[1, 3],
["","",
"Promedio 1: 8.64",
"Promedio 2: 1183.43"],
"Debe salir: lo que te indica el caso de prueba3"
),
 # Test case 2
(
 [2, 1],
 ["","",
"1 Jose ITC",
"2 Nodal INE",
"3 Andres IFI",
"4 Ana Victoria IRS",
"5 Alexa IFI",
"6 Sofia ITC",
"7 Ada ITC"],
"Debe salir: lo que te indica el caso de prueba4"
),
(
 [2,2],
 ["","",
"ITC 3",
"INE 1",
"IFI 2",
"IRS 1"],
"Debe salir: lo que te indica el caso de prueba5"
,
(
 [2,3],
 ["","",
"Promedio 1: 112.57",
"Promedio 2: 2514.29"],
"Debe salir: lo que te indica el caso de prueba6"
)
]
