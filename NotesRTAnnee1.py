
    """
Calcule des moyennes de chaque unitée d'enseignement de chaque semestre en première année de
    bachelor universitaire technologique en réseau et télécommunication

Copyright: bcbdjemel@gmail.com
    """
import statistics
import math

print('-----------------------------------------------------------------------------------------------------')
print('Bienvenue sur ce programme de calcule de moyenne de chaque UE de chaque semestre en RT1')
print(' ')
print('Entrez vos notes dans l\'ordre indiqué :')
print('-----------------------------------------------------------------------------------------------------')
print('Made by Djemel in 2022')
print('Contact me on bcbdjemel@gmail.com')
print('github : https://github.com/BEN-Djemel/')
print(' ')

global moy  # recuperation de la moyenne ue1.1 du semestre 1


def sem1_ue1():  # Fonction qui calcule la moyenne ue1.1 du semestre 1
    L1 = []
    # error = []
    R101 = float(input('veuillez saisir la moyenne de R101 en U.E 1.1 : '))
    L1.append(R101)
    R102 = float(input('veuillez saisir la moyenne de R102 en U.E 1.1 : '))
    L1.append(R102)
    R103 = float(input('veuillez saisir la moyenne de R103 en U.E 1.1 : '))
    L1.append(R103)
    R104 = float(input('veuillez saisir la moyenne de R104 en U.E 1.1 : '))
    L1.append(R104)
    R106 = float(input('veuillez saisir la moyenne de R106 en U.E 1.1 : '))
    L1.append(R106)
    R108 = float(input('veuillez saisir la moyenne de R108 en U.E 1.1 : '))
    L1.append(R108)
    R110 = float(input('veuillez saisir la moyenne de R110 en U.E 1.1 : '))
    L1.append(R110)
    R111 = float(input('veuillez saisir la moyenne de R111 en U.E 1.1 : '))
    L1.append(R111)
    R112 = float(input('veuillez saisir la moyenne de R112 en U.E 1.1 : '))
    L1.append(R112)
    R113 = float(input('veuillez saisir la moyenne de R113 en U.E 1.1 : '))
    L1.append(R113)
    R114 = float(input('veuillez saisir la moyenne de R114 en U.E 1.1 : '))
    L1.append(R114)
    SAE11 = float(input('veuillez saisir la moyenne de SAE11 en U.E 1.1 : '))
    L1.append(SAE11)
    SAE12 = float(input('veuillez saisir la moyenne de SAE12 en U.E 1.1 : '))
    L1.append(SAE12)

    z = len(L1)
    coeff = (16 + 33 + 12 + 12 + 8 + 8 + 10 + 6 + 3 + 3 + 2 + 5 + 4)
    global moy
    moy = (((L1[0] * 16) + (L1[1] * 33) + (L1[2] * 12) + (L1[3] * 12) + (L1[4] * 8) + (L1[5] * 8) + (L1[6] * 10) + (
            L1[7] * 6) + (L1[8] * 3) + (L1[9] * 3) + (L1[10] * 2) + (L1[11] * 5) + (L1[12] * 4)) / coeff)
    # print('Le nombre de notes entrée est de ', z)
    # print('votre liste est: ', L1)
    print('-----------------------------------------------------------------------------------------------------')
    return moy


global moy2  # recuperation de la moyenne ue1.2 du semestre 1


def sem1_ue2():  # Fonction qui calcule la moyenne ue1.2 du semestre 1
    L2 = []
    # errorr = []
    R101 = float(input('veuillez saisir la moyenne de R101 en U.E 1.2 : '))
    L2.append(R101)
    R103 = float(input('veuillez saisir la moyenne de R103 en U.E 1.2 : '))
    L2.append(R103)
    R104 = float(input('veuillez saisir la moyenne de R104 en U.E 1.2 : '))
    L2.append(R104)
    R105 = float(input('veuillez saisir la moyenne de R105 en U.E 1.2 : '))
    L2.append(R105)
    R110 = float(input('veuillez saisir la moyenne de R110 en U.E 1.2 : '))
    L2.append(R110)
    R111 = float(input('veuillez saisir la moyenne de R111 en U.E 1.2 : '))
    L2.append(R111)
    R112 = float(input('veuillez saisir la moyenne de R112 en U.E 1.2 : '))
    L2.append(R112)
    R113 = float(input('veuillez saisir la moyenne de R113 en U.E 1.2 : '))
    L2.append(R113)
    R114 = float(input('veuillez saisir la moyenne de R114 en U.E 1.2 : '))
    L2.append(R114)
    R115 = float(input('veuillez saisir la moyenne de R115 en U.E 1.2 : '))
    L2.append(R115)
    SAE13 = float(input('veuillez saisir la moyenne de SAE13 en U.E 1.2 : '))
    L2.append(SAE13)

    z2 = len(L2)
    coeff2 = (33 + 4 + 4 + 5 + 5 + 5 + 5 + 3 + 8 + 8 + 2)
    global moy2
    moy2 = (((L2[0] * 4) + (L2[1] * 4) + (L2[2] * 5) + (L2[3] * 5) + (L2[4] * 5) + (L2[5] * 5) + (L2[6] * 3) + (
            L2[7] * 8) + (L2[8] * 8) + (L2[9] * 2) + (L2[10] * 33)) / coeff2)
    # print('Le nombre de notes entrée est de ', z2)
    # print('votre liste est: ', L2)
    print('-----------------------------------------------------------------------------------------------------')
    return moy2


global moy3  # recuperation de la moyenne ue1.3 du semestre 1


def sem1_ue3():  # Fonction qui calcule la moyenne ue1.3 du semestre 1
    L3 = []
    # errorrr = []
    R101 = float(input('veuillez saisir la moyenne de R101 en U.E 1.3 : '))
    L3.append(R101)
    R107 = float(input('veuillez saisir la moyenne de R107 en U.E 1.3 : '))
    L3.append(R107)
    R108 = float(input('veuillez saisir la moyenne de R108 en U.E 1.3 : '))
    L3.append(R108)
    R109 = float(input('veuillez saisir la moyenne de R109 en U.E 1.3 : '))
    L3.append(R109)
    R110 = float(input('veuillez saisir la moyenne de R110 en U.E 1.3 : '))
    L3.append(R110)
    R111 = float(input('veuillez saisir la moyenne de R111 en U.E 1.3 : '))
    L3.append(R111)
    R112 = float(input('veuillez saisir la moyenne de R112 en U.E 1.3 : '))
    L3.append(R112)
    R115 = float(input('veuillez saisir la moyenne de R115 en U.E 1.3 : '))
    L3.append(R115)
    SAE14 = float(input('veuillez saisir la moyenne de SAE14 en U.E 1.3 : '))
    L3.append(SAE14)
    SAE15 = float(input('veuillez saisir la moyenne de SAE15 en U.E 1.3 : '))
    L3.append(SAE15)

    z3 = len(L3)
    coeff3 = (4 + 22 + 7 + 4 + 5 + 4 + 4 + 4 + 26 + 16)
    global moy3
    moy3 = (((L3[0] * 4) + (L3[1] * 22) + (L3[2] * 7) + (L3[3] * 4) + (L3[4] * 5) + (L3[5] * 4) + (L3[6] * 4) + (
            L3[7] * 4) + (L3[8] * 16) + (L3[9] * 26)) / coeff3)
    # print('Le nombre de notes entrée est de ', z3)
    # print('votre liste est: ', L3)
    print('-----------------------------------------------------------------------------------------------------')
    return moy3


global moyy  # recuperation de la moyenne ue2.1 du semestre 2


def sem2_ue1():  # Fonction qui calcule la moyenne ue2.1 du semestre 2
    L4 = []
    # error = []
    R201 = float(input('veuillez saisir la moyenne de R201 en U.E 2.1 : '))
    L4.append(R201)
    R202 = float(input('veuillez saisir la moyenne de R202 en U.E 2.1 : '))
    L4.append(R202)
    R203 = float(input('veuillez saisir la moyenne de R203 en U.E 2.1 : '))
    L4.append(R203)
    R204 = float(input('veuillez saisir la moyenne de R204 en U.E 2.1 : '))
    L4.append(R204)
    R205 = float(input('veuillez saisir la moyenne de R205 en U.E 2.1 : '))
    L4.append(R205)
    R209 = float(input('veuillez saisir la moyenne de R209 en U.E 2.1 : '))
    L4.append(R209)
    R210 = float(input('veuillez saisir la moyenne de R210 en U.E 2.1 : '))
    L4.append(R210)
    R211 = float(input('veuillez saisir la moyenne de R211 en U.E 2.1 : '))
    L4.append(R211)
    R212 = float(input('veuillez saisir la moyenne de R212 en U.E 2.1 : '))
    L4.append(R212)
    R213 = float(input('veuillez saisir la moyenne de R213 en U.E 2.1 : '))
    L4.append(R213)
    R214 = float(input('veuillez saisir la moyenne de R214 en U.E 2.1 : '))
    L4.append(R214)
    SAE21 = float(input('veuillez saisir la moyenne de SAE21 en U.E 2.1 : '))
    L4.append(SAE21)
    SAE24 = float(input('veuillez saisir la moyenne de SAE24 en U.E 2.1 : '))
    L4.append(SAE24)
    SAE25 = float(input('veuillez saisir la moyenne de SAE25 en U.E 2.1 : '))
    L4.append(SAE25)

    z4 = len(L4)
    coeff4 = (19 + 12 + 12 + 8 + 2 + 2 + 3 + 3 + 2 + 3 + 3 + 23 + 22 + 1)
    global moyy
    moyy = (((L4[0] * 19) + (L4[1] * 12) + (L4[2] * 12) + (L4[3] * 8) + (L4[4] * 2) + (L4[5] * 2) + (L4[6] * 3) + (
            L4[7] * 3) + (L4[8] * 2) + (L4[9] * 3) + (L4[10] * 3) + (L4[11] * 23) + (L4[12] * 22) + (
                         L4[13] * 1)) / coeff4)
    # print('Le nombre de notes entrée est de ', z4)
    # print('votre liste est: ', L4)
    print('-----------------------------------------------------------------------------------------------------')
    return moyy


global moyy2  # recuperation de la moyenne ue2.2 du semestre 2


def sem2_ue2():  # Fonction qui calcule la moyenne ue2.2 du semestre 2
    L5 = []
    # error = []
    R201 = float(input('veuillez saisir la moyenne de R201 en U.E 2.2 : '))
    L5.append(R201)
    R204 = float(input('veuillez saisir la moyenne de R204 en U.E 2.2 : '))
    L5.append(R204)
    R205 = float(input('veuillez saisir la moyenne de R205 en U.E 2.2 : '))
    L5.append(R205)
    R206 = float(input('veuillez saisir la moyenne de R206 en U.E 2.2 : '))
    L5.append(R206)
    R210 = float(input('veuillez saisir la moyenne de R210 en U.E 2.2 : '))
    L5.append(R210)
    R211 = float(input('veuillez saisir la moyenne de R211 en U.E 2.2 : '))
    L5.append(R211)
    R212 = float(input('veuillez saisir la moyenne de R212 en U.E 2.2 : '))
    L5.append(R212)
    R213 = float(input('veuillez saisir la moyenne de R213 en U.E 2.2 : '))
    L5.append(R213)
    R214 = float(input('veuillez saisir la moyenne de R214 en U.E 2.2 : '))
    L5.append(R214)
    SAE22 = float(input('veuillez saisir la moyenne de SAE22 en U.E 2.2 : '))
    L5.append(SAE22)
    SAE24 = float(input('veuillez saisir la moyenne de SAE24 en U.E 2.2 : '))
    L5.append(SAE24)
    SAE25 = float(input('veuillez saisir la moyenne de SAE25 en U.E 2.2 : '))
    L5.append(SAE25)

    z5 = len(L5)
    coeff_5 = (4 + 4 + 12 + 10 + 8 + 4 + 2 + 5 + 8 + 19 + 18 + 1)
    global moyy2
    moyy2 = (((L5[0] * 4) + (L5[1] * 4) + (L5[2] * 12) + (L5[3] * 10) + (L5[4] * 8) + (L5[5] * 4) + (L5[6] * 2) + (
            L5[7] * 5) + (L5[8] * 8) + (L5[9] * 19) + (L5[10] * 18) + (L5[11] * 1)) / coeff_5)
    # print('Le nombre de notes entrée est de ', z5)
    # print('votre liste est: ', L5)
    print('-----------------------------------------------------------------------------------------------------')
    return moyy2


global moyy3  # recuperation de la moyenne ue2.2 du semestre 2


def sem2_ue3():  # Fonction qui calcule la moyenne ue2.2 du semestre 2
    L6 = []
    # error = []
    R202 = float(input('veuillez saisir la moyenne de R202 en U.E 2.3 : '))
    L6.append(R202)
    R207 = float(input('veuillez saisir la moyenne de R207 en U.E 2.3 : '))
    L6.append(R207)
    R208 = float(input('veuillez saisir la moyenne de R208 en U.E 2.3 : '))
    L6.append(R208)
    R209 = float(input('veuillez saisir la moyenne de R209 en U.E 2.3 : '))
    L6.append(R209)
    R210 = float(input('veuillez saisir la moyenne de R210 en U.E 2.3 : '))
    L6.append(R210)
    R211 = float(input('veuillez saisir la moyenne de R211 en U.E 2.3 : '))
    L6.append(R211)
    R212 = float(input('veuillez saisir la moyenne de R212 en U.E 2.3 : '))
    L6.append(R212)
    R213 = float(input('veuillez saisir la moyenne de R213 en U.E 2.3 : '))
    L6.append(R213)
    SAE23 = float(input('veuillez saisir la moyenne de SAE23 en U.E 2.3 : '))
    L6.append(SAE23)
    SAE24 = float(input('veuillez saisir la moyenne de SAE24 en U.E 2.3 : '))
    L6.append(SAE24)
    SAE25 = float(input('veuillez saisir la moyenne de SAE25 en U.E 2.3 : '))
    L6.append(SAE25)

    z6 = len(L6)
    coeff6 = (4 + 10 + 10 + 10 + 8 + 5 + 2 + 5 + 18 + 17 + 1)
    global moyy3
    moyy3 = (((L6[0] * 4) + (L6[1] * 10) + (L6[2] * 10) + (L6[3] * 10) + (L6[4] * 8) + (L6[5] * 5) + (L6[6] * 2) + (
            L6[7] * 5) + (L6[8] * 18) + (L6[9] * 17) + (L6[10] * 1)) / coeff6)
    print('-----------------------------------------------------------------------------------------------------')
    # print('Le nombre de notes entrées est de ', z6)
    # print('votre liste est: ', L6)
    return moyy3


print('-----------------------------------------------------------------------------------------------------')
# sem est la contraction de semestre
sem = int(input('tapez 1 pour SEMESTRE 1 ; tapez 2 pour SEMESTRE 2 ; tapez 3 pour les deux semestres (l\'année) : '))
if sem == 1:
    print('-----------------------------------------------------------------------------------------------------')
    ue = int(
        input('tapez 1 pour UE 1.1 ; tapez 2 pour UE 1.2 ; tapez 3 pour UE 1.3 ; tapez 4 pour tout le SEMESTRE 1 : '))
    if ue == 1:
        print('-----------------------------------------------------------------------------------------------------')
        print('La moyenne des notes de l\'ue 1.1 est de ', format(sem1_ue1(), '.2f'), '/20')
    elif ue == 2:
        print('-----------------------------------------------------------------------------------------------------')
        print('La moyenne des notes de l\'ue 1.2 est de ', format(sem1_ue2(), '.2f'), '/20')
    elif ue == 3:
        print('-----------------------------------------------------------------------------------------------------')
        print('La moyenne des notes de l\'ue 1.3 est de ', format(sem1_ue3(), '.2f'), '/20')
    elif ue == 4:
        sem1_ue1()
        print('-----------------------------------------------------------------------------------------------------')
        sem1_ue2()
        print('-----------------------------------------------------------------------------------------------------')
        sem1_ue3()
        print('-----------------------------------------------------------------------------------------------------')
        print('La moyenne des notes de l\'ue 1.1 est de ', format(moy, '.2f'), '/20')
        print('La moyenne des notes de l\'ue 1.2 est de ', format(moy2, '.2f'), '/20')
        print('La moyenne des notes de l\'ue 1.3 est de ', format(moy3, '.2f'), '/20')
        if moy + moy2 + moy3 >= 28:
            print(
                '-----------------------------------------------------------------------------------------------------')
            print('Felicitation, le premier semestre est validé!')
        else:
            print('Redouble d\'efforts au second semestre. Ce semestre 1 n\'est pas validé...')
    else:
        print('erreur')
elif sem == 2:
    print('-----------------------------------------------------------------------------------------------------')
    ue2 = int(
        input('tapez 1 pour UE 2.1 ; tapez 2 pour UE 2.2 ; tapez 3 pour UE 2.3 ; tapez 4 pour tout le SEMESTRE 2 : '))
    if ue2 == 1:
        print('-----------------------------------------------------------------------------------------------------')
        print('La moyenne des notes de l\'ue 2.1 est de ', format(sem2_ue1(), '.2f'), '/20')
    elif ue2 == 2:
        print('-----------------------------------------------------------------------------------------------------')
        print('La moyenne des notes de l\'ue 2.2 est de ', format(sem2_ue2(), '.2f'), '/20')
    elif ue2 == 3:
        print('-----------------------------------------------------------------------------------------------------')
        print('La moyenne des notes de l\'ue 2.3 est de ', format(sem2_ue3(), '.2f'), '/20')
    elif ue2 == 4:
        sem2_ue1()
        print('-----------------------------------------------------------------------------------------------------')
        sem2_ue2()
        print('-----------------------------------------------------------------------------------------------------')
        sem2_ue3()
        print('-----------------------------------------------------------------------------------------------------')
        print('La moyenne des notes de l\'ue 2.1 est de ', format(moyy, '.2f'), '/20')
        print('La moyenne des notes de l\'ue 2.2 est de ', format(moyy2, '.2f'), '/20')
        print('La moyenne des notes de l\'ue 2.3 est de ', format(moyy3, '.2f'), '/20')
        if moyy + moyy2 + moyy3 >= 28:
            print(
                '-----------------------------------------------------------------------------------------------------')
            print('Le second semestre est validé!')
        else:
            print(
                '-----------------------------------------------------------------------------------------------------')
            print('Le second semestre n\'est pas validé.')
    else:
        print('erreur')
elif sem == 3:
    print('-----------------------------------------------------------------------------------------------------')
    print('Vous allez mettre vos notes du semestre 1.')
    sem1_ue1()
    print('-----------------------------------------------------------------------------------------------------')
    sem1_ue2()
    print('-----------------------------------------------------------------------------------------------------')
    sem1_ue3()
    print('-----------------------------------------------------------------------------------------------------')
    print('-----------------------------------------------------------------------------------------------------')
    print('Vous allez mettre vos notes du semestre 2.')
    sem2_ue1()
    print('-----------------------------------------------------------------------------------------------------')
    sem2_ue2()
    print('-----------------------------------------------------------------------------------------------------')
    sem2_ue3()
    print('-----------------------------------------------------------------------------------------------------')
    print('-----------------------------------------------------------------------------------------------------')
    print('La moyenne des notes de l\'ue 1.1 est de ', format(moy, '.2f'), '/20')
    print('La moyenne des notes de l\'ue 1.2 est de ', format(moy2, '.2f'), '/20')
    print('La moyenne des notes de l\'ue 1.3 est de ', format(moy3, '.2f'), '/20')
    print('La moyenne des notes de l\'ue 2.1 est de ', format(moyy, '.2f'), '/20')
    print('La moyenne des notes de l\'ue 2.2 est de ', format(moyy2, '.2f'), '/20')
    print('La moyenne des notes de l\'ue 2.3 est de ', format(moyy3, '.2f'), '/20')
    if moy + moy2 + moy3 + moyy + moyy2 + moyy3 >= 56:
        print('Ton année est validé!')
    else:
        print('Tu n\'as pas validé ton année...')
else:
    print('erreur')
print('-----------------------------------------------------------------------------------------------------')
print('Merci d\'avoir utilisé ce programme, au revoir !')
