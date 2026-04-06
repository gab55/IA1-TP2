\* Deux_Equipes *\
Maximize
scoreTotal: 88 x_Alice_A + 88 x_Alice_B + 91 x_Bob_A + 91 x_Bob_B
 + 84 x_Clara_A + 84 x_Clara_B + 93 x_David_A + 93 x_David_B + 79 x_Emma_A
 + 79 x_Emma_B + 87 x_Frank_A + 87 x_Frank_B + 85 x_Grace_A + 85 x_Grace_B
 + 89 x_Hugo_A + 89 x_Hugo_B
Subject To
PoidsTotal_A: 72 x_Alice_A + 85 x_Bob_A + 68 x_Clara_A + 90 x_David_A
 + 65 x_Emma_A + 95 x_Frank_A + 70 x_Grace_A + 80 x_Hugo_A <= 250
PoidsTotal_B: 72 x_Alice_B + 85 x_Bob_B + 68 x_Clara_B + 90 x_David_B
 + 65 x_Emma_B + 95 x_Frank_B + 70 x_Grace_B + 80 x_Hugo_B <= 250
SalaireTotal: 1200 x_Alice_A + 1200 x_Alice_B + 1800 x_Bob_A + 1800 x_Bob_B
 + 950 x_Clara_A + 950 x_Clara_B + 2100 x_David_A + 2100 x_David_B
 + 800 x_Emma_A + 800 x_Emma_B + 2400 x_Frank_A + 2400 x_Frank_B
 + 1050 x_Grace_A + 1050 x_Grace_B + 1600 x_Hugo_A + 1600 x_Hugo_B <= 8500
max1Equipe_Alice: x_Alice_A + x_Alice_B <= 1
max1Equipe_Bob: x_Bob_A + x_Bob_B <= 1
max1Equipe_Clara: x_Clara_A + x_Clara_B <= 1
max1Equipe_David: x_David_A + x_David_B <= 1
max1Equipe_Emma: x_Emma_A + x_Emma_B <= 1
max1Equipe_Frank: x_Frank_A + x_Frank_B <= 1
max1Equipe_Grace: x_Grace_A + x_Grace_B <= 1
max1Equipe_Hugo: x_Hugo_A + x_Hugo_B <= 1
nbJoueurEquipe_A: x_Alice_A + x_Bob_A + x_Clara_A + x_David_A + x_Emma_A
 + x_Frank_A + x_Grace_A + x_Hugo_A = 3
nbJoueurEquipe_B: x_Alice_B + x_Bob_B + x_Clara_B + x_David_B + x_Emma_B
 + x_Frank_B + x_Grace_B + x_Hugo_B = 3
Binaries
x_Alice_A
x_Alice_B
x_Bob_A
x_Bob_B
x_Clara_A
x_Clara_B
x_David_A
x_David_B
x_Emma_A
x_Emma_B
x_Frank_A
x_Frank_B
x_Grace_A
x_Grace_B
x_Hugo_A
x_Hugo_B
End
