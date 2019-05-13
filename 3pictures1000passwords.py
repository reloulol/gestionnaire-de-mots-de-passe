# -*- coding: utf8 -*-
from tkinter import font
import os.path
import random
from tkinter import *
from tkinter import Menu
from inspect import signature


img_liste = []
mauvais_contenu = [] 
dat = []
mdp = []
choix=[]
mdp_choisi_random=[]

nom1 = ''
nom = ''
entree_liste = []

fen1=Tk()

log1=Toplevel()
log1.withdraw()
log2=Toplevel()
log2.withdraw()
log3=Toplevel()
log3.withdraw()
log4=Toplevel()
log4.withdraw()
log5=Toplevel()
log5.withdraw()
log6=Toplevel()
log6.withdraw()
log7=Toplevel()
log7.withdraw()
log8=Toplevel()
log8.withdraw()


Con1=Toplevel()
Con1.withdraw()
Con2=Toplevel()
Con2.withdraw()
Con3=Toplevel()
Con3.withdraw()
Con4=Toplevel()
Con4.withdraw()
Con5=Toplevel()
Con5.withdraw()

fen2=Toplevel()
fen2.withdraw()
fen3=Toplevel()
fen3.withdraw()
fen4=Toplevel()
fen4.withdraw()
fen5=Toplevel()
fen5.withdraw()


##Fonction qui fait apparaitre une fenêtre tkinter, en fonction des paramètres(nom, taille, arriére plan, plein écran).
def createfen(nom, taille, bg, full):
    ##La fenêtre réapparait 
    nom.deiconify()
    ##Mise en place du nom
    nom.title("5 pictures 1000 passwords")
    ##Mise en place de la taille
    nom.geometry('{}'.format(taille))
    ##Centrage de la fenêtre sur l'écran source : https://stackoverflow.com/questions/3352918/how-to-center-a-window-on-the-screen-in-tkinter de Wayne Werner
    nom.update_idletasks()
    width = nom.winfo_width()
    height = nom.winfo_height()
    x = (nom.winfo_screenwidth() // 2) - (width // 2)
    y = (nom.winfo_screenheight() // 2) - (height // 2)
    nom.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    
    ## Full écran source: https://stackoverflow.com/questions/15981000/tkinter-python-maximize-window de A. Rodas. 
    if full=="1": 
        w, h = nom.winfo_screenwidth(), nom.winfo_screenheight()
        nom.geometry("%dx%d+0+0" % (w, h))
        
    ##Mise en place de l'arriére plan
    nom.configure(bg='{}'.format(bg))

    ##la fonction renvoie le nom de la fenêtre.
    return nom

##Fonction qui lit, tous les noms d'utilisateurs du ficher data.txt et qui les renvoie dans la liste usernames.
def readuser():
    n=0
    usernames=[]
    ## Si le ficher data.txt existe, le programme lit le ficher
    try:
        with open("data.txt", "r") as data:
            
            for i in data:
                n=n+1
                ##Une fois que n est égal à 7. Celui-ci prend la valeur 1 afin, de prendre en compte les données de l'utilisateur suivant. 
                if (n== 7):
                    n=1

                ## A chaque fois que le programme atteint la ligne 4, il ajoute le contenu de cette ligne dans la liste username
                if (n == 4):
                    username=data.readline()
                    username = username.replace("\n", "")
                    usernames.append(username)
                    
    ##Si le ficher n'existe pas la liste usernames renvoie liste vide.    
    except:
        usernames=[]

        
    return usernames

##Fonction qui lit, le mot de passe d'un utilisateur, et qui le renvoie, dans la liste mot_de_passe.
def readpassword(index): 
    mot_de_passe=[]
    lire_ligne1=[]
    index=index+1
    n=1

    ##En fonction de l'index de l'utilisateur, dans la liste username, le programme lit les lignes qui correspondent à son index
    if index == 1: 
        index=((index)*8)
    else:
        index= (index * 7)+1 
    ##La liste lire_ligne1 dispose des lignes que la boucle doit lire pour récupérer le mot de passe de l'utilisateur.
    lire_ligne1.append((index-2))
    lire_ligne1.append((index-1))
    lire_ligne1.append((index))
    
    with open("data.txt", "r") as data:
        for line in data:
            ## Retire le saut de ligne
            line = line.strip('\n')
            password=str(line.split(","))
            ## Retire les crochets, afin d'obtenir uniquement des nombres entiers. 
            password = password.replace("['", "")
            password = password.replace("']", "")

            ##Ajoute à la liste mot_de_passe les lignes correspondantes.
            if n == lire_ligne1[0]:
                mot_de_passe.append(password)
                
            elif n == lire_ligne1[1]:
                mot_de_passe.append(password)
                
            elif n == lire_ligne1[2]:
               
                mot_de_passe.append(password)
            n=n+1
        ##Transformation de cette liste en liste de nombre entier.     
        mot_de_passe= list (map (int, mot_de_passe))

        
        return mot_de_passe

            
 
## Cette fonction choisit, 15 images pour le diaporama lors de la connexion.   
def login(password, nombre):
    
    image_diapo_password=[]
    ##Choix d'un nombre au hasard entre 1 et 4. 
    numb_image_password = random.randint(1, 4)

    ##Si le nombre choisi au hasard est égal à 2 ou à 4 et que le nombre d'images déja choisies correspondant au mot de passe n'est pas inférieur à 2.
    if numb_image_password % 2 == 0 and nombre<2:
        
        ##Une image du mot de passe de l'utilisateur sera choisie.  
        nombre=+1
        
        ##Un nombre choisi au hasard entre 0 et 2.
        randompassword =  random.randint(0, 2)
        
        ##Choix de l'image au hasard
        image_pass=(password[randompassword])
        
        ##Ajout dans la liste d'images, pour le diaporama
        image_diapo_password.append(image_pass)
        
        ##Ajout dans une liste qui contient les images choisies pour la connexion(réutilisée lors de la vérification du mot de passe).
        mdp_choisi_random.append(image_pass)
        
        ##Choix de 14 autres images au hasard.
        for j in range(14):
            number = random.randint(1, 19)
            
            while number in image_diapo_password or number in password:
                number = random.randint(1, 19)
            image_diapo_password.append(number)
            
    ## Si le nombre choisi au hasard est égal à 3 et que le nombre d'images déja choisies correspondant aux mots de passe est nul.   


    elif numb_image_password ==3 and nombre<1:
        ## Deux images du mot de passe de l'utilisateur seront choisies.
        nombre=+2
        for j in range(2):
            
            ##Un nombre chosi au hasard entre 0 et 2.
            randompassword =  random.randint(0, 2)
            
            ##On vérifie que cette image n'a pas déjà été choisie, pour ce diaporama.
            while password[randompassword] in image_diapo_password:
                randompassword =  random.randint(0, 2)
                
            ##Ajout dans une liste qui contient les images choisies pour la connexion (réutilisée lors de la vérification du mot de passe).
            mdp_choisi_random.append(password[randompassword])
            
            ##Ajout dans la liste d'images, pour le diaporama
            image_diapo_password.append(password[randompassword])
            
        ##Choix de 13 autres images au hasard.
        for j in range(13):
            number = random.randint(1, 19)
            
            while number in image_diapo_password or number in password:
                number = random.randint(1, 19)
            image_diapo_password.append(number)


            
    ##Sinon, si le nombre choisi au hasard est égal à 0, ou que déjà 2 images du mot de passe ont été choisies. Dans ce cas, aucune image ne correspond au mot de passe.     
    else:
        for j in range(15):
            number = random.randint(1, 19)
            
            while number in image_diapo_password or number in password:
                number = random.randint(1, 19)
            image_diapo_password.append(number)
            
    ##Mélange des images pour éviter que les images qui correspondent au mot de passe soient en premiére position.
    random.shuffle(image_diapo_password)
    
    return image_diapo_password, nombre


## Obtenir le nom de l'image lors d'un clic. 
def get_name(num_img, label, info):
    path = num_img

    ##La variable info permet de changer la façon de donner le nom de l'image.
    ##Pour la connexion le numéro de l'image suffit.
    
    if info == "Connexion":
        choix.append(path)

    ##Pour l'inscription, il faut prévoir les messages d'erreurs, et guider l'utilisateur.
    else:
        ##Police d'écriture
        my_font = font.Font(fen2, ('Helvetica', 12, 'bold'))
        
        ##Vérification que l'utilisateur ne choisit pas la même image. 
        if path in mdp and len(mdp) < 4:
            error="Vous avez déjà  choisi cette image!"
            
        ##Vérification que l'utilisateur ne choisit pas plus de trois images. 
        elif len(mdp)==3:
            error="Vous avez déjà  choisi 3 images !"
            
        ##Si tout se passe bien, le nombre est ajouté dans la liste mdp et le label précédent est détruit pour en afficher un nouveau.    
        else:
            mdp.append(path)
            label.destroy()
            error=""
            if 3-len(mdp)==2:
                texte = ("Vous devez encore choisir {0} images").format(3-len(mdp))
            elif 3-len(mdp)==1:
                texte = ("Vous devez encore choisir {0} image").format(3-len(mdp))
            else:
                texte = "Cliquez sur valider pour continuer l'inscription"
                
            ##Label avec le nombre d'image(s) restante(s) à choisir. 
            label = Label(fen4, text=texte, background='grey', font=my_font, wraplength=500, anchor=W, justify=LEFT)
            label.place(x=20, y=560, width=650, height=40)
            
        ##Label avec une potentielle erreur.  
        label2 = Label(fen4, text=error, background='grey', font=my_font, wraplength=500, anchor=W, justify=LEFT)
        label2.place(x=20, y=600, width=650, height=40)
            
## Cette fonction crée un bouton unique avec différents paramétres. 
def MyButton(master, path_images,j, label, info):
    button = Button(master, image=img_liste[j], command=lambda:get_name(path_images, label, info) )
    return button

## Affiche le diaporama d'images dans des boutons. 
def image_button(fen ,nombre, liste_img, label, info): 
    deplacement=0
    hauteur=50
    fen.withdraw()
    for j in range(nombre):
        ##Ajout du suffixe .png
        myimg = str(liste_img[j]) + '.png'
        ##Recherche dans le dossier images. 
        path=os.path.join("images", myimg)
        num_image = str(liste_img[j])
        im = PhotoImage(file=path)
        ##Ajout de l'image dans la liste img_liste
        img_liste.append(im)
        ##Recadrage de l'image
        img_liste[j] = im.subsample(5, 5)
        ##Le programme affiche les boutons avec les images en déplaçant le curseur en hauteur et en largeur.
        if j != 0:
            deplacement = deplacement + 270
        if j % 5 == 0 and j != 0:
            hauteur = hauteur + 160
            deplacement = 0
        ##Utilisation de la fonction MyButton et placement des boutons.
        button = MyButton(fen, num_image, j, label, info)
        button.place(x=deplacement, y=hauteur)
    fen.deiconify()

def createfen1(nom1, taille, bg):
    nom1 = Tk()
    nom1.title("5 pictures 1000 passwords")
    nom1.geometry('{}'.format(taille))
    nom1.configure(bg='{}'.format(bg))
    # nom1.withdraw()
    return nom1
    
def Menu1(detruit):

    if detruit != "":
        detruit.withdraw()
    createfen(fen1, "1000x600", "grey", "0")

    ##Canvas avec image

    
    myimg = "cadena.png"
    ##Recherche dans le dossier images.
    path=os.path.join("images", myimg)
    can=Canvas(fen1, width =587, height =310, bg ='white')
    im = can.img1= PhotoImage(file = path)
    item = can.create_image(0, 0, image =im, anchor=NW)
    can.place(x=80, y=70)

    
    ##Font
    my_font = font.Font(fen1, ('Helvetica', 15, 'bold'))


    ##Label
    texte="Bienvenue, pour commencer à utiliser le gestionnaire de mot de passe, inscrivez-vous.\nSinon, connectez-vous pour avoir accès à vos mots de passe."
    label = Label(fen1, text=texte, background='grey', font=my_font, anchor=W, justify=LEFT)
    label.place(x=20, y=450, width=5000, height=100)
   
    ##Bouton Connexion

    bouton_connexion = Button(fen1, text="Connexion", command=lambda:Connexion1(fen1, ""))
    bouton_connexion.place(relx=0.750, rely=0.250)
    bouton_connexion.config(foreground="black", background="red")

    ##Bouton Inscription

    bouton_inscription = Button(fen1, text="Inscription", command=lambda:Inscription1(fen1, ""))
    bouton_inscription.place(relx=0.750, rely=0.500)
    bouton_inscription.config(foreground="black", background="red")

    
def Connexion1(detruit, error):
    
    createfen(Con1, "700x220", "grey","0")
    detruit.withdraw()

    ##Font
    my_font = font.Font(Con1, ('Helvetica', 12, 'bold'))

    ##Label username
    
    username = Label(Con1, text="Nom d'utilisateur", font=my_font, width=25, height=3, bg="grey", fg="white")
    username.place(x=20, y=50)

    ##Entrée pour le texte
    entry = Entry(Con1)
    entry.place(x=220, y=71, width=150)


    ##Label
    label = Label(Con1, text=error + "\nSi vous n'êtes pas encore inscrit cliquez sur inscription." , background='grey', font=my_font, wraplength=500, anchor=W, justify=LEFT)
    label.place(x=20, y=120, width=500, height=70)

    ##Bouton valider
    bouton = Button(Con1, text="   Suivant   ", background='red' , justify=LEFT, command=lambda:Connexion2(Con1, entry, ""))
    bouton.place(x=630, y=50)

    ##Bouton inscription
    bouton2 = Button(Con1, text="Inscription", background='red' , command=lambda:Inscription1(Con1, ""))
    bouton2.place(x=630, y=120)


def Connexion2(detruit, entry, error):
    ##Fonction readuser
    pseudos = readuser()

    ##En cas d'échec du mot de passe. 
    if detruit == Con1:
        ##Obtenir l'entrée
        nom = str(entry.get())
    else:
        mdp_choisi_random[:] = []
        choix[:] = []
        nom = entry

    ##Vérification que le nom existe
    if nom in pseudos:

        createfen(Con2, "1000x400", "grey", "0")
        detruit.withdraw()
        detruit.withdraw()

        ##Indexation du nom d'utilisateur
        index = pseudos.index(nom)

        ##Obtention du mot de passe de l'utilisateur
        motpasse = readpassword(index)

        ##Font
        my_font = font.Font(Con2, ('Helvetica', 15, 'bold'))

        ## String texte qui contient le message à afficher sur l'écran
        texte = (
                    error + "{0}, pour pouvoir vous connecter il faut que vous retrouviez les images qui correspondent à votre" +
                    " mot de passe à partir d'un diaporama de 15 images. Il y en aura zéro, une ou deux qui correspondront" +
                    " aux images que vous avez choisies lors de votre inscription ! ").format(nom)

        ## Placement du label texte qui est justifié vers la gauche
        label = Label(Con2, text=texte, background='grey', font=my_font, wraplength=500, anchor=W, justify=LEFT)
        label.place(x=20, y=50, width=500, height=200)

        ##Bouton
        bouton = Button(Con2, text="Suivant", background='red', command=lambda: Connexion3(Con2, motpasse, nom))
        bouton.place(x=900, y=112)

    ##Si le nom d'utilisateur n'existe pas.
    else:
        error = "Le nom d'utilisateur n'existe pas !"
        Connexion1(fen1, error)


def Connexion3(detruit, mdp, nom):

    createfen(Con3, "1200x600", "grey", "1")
    detruit.withdraw()
    nombre=0

    ##Execution de la fonction login
    numimage, nombre= login(mdp, nombre)

    ##Affichage du diaporama
    image_button(Con3,15, numimage,"", "Connexion")

    ##Font 
    my_font = font.Font(Con3, ('Helvetica', 15, 'bold'))

    ##Texte
    texte = "Choisissez 0, 1 ou 2 image(s) qui corresponde(nt) à votre mot de passe puis cliquez sur suivant"

    ##Label
    label = Label(Con3, text=texte, background='grey', font=my_font, wraplength=500, anchor=W, justify=LEFT)
    label.place(x=20, y=560, width=500, height=49)

    ##Bouton
    bouton = Button(Con3, text="Suivant", background='red' ,command=lambda:Connexion4(Con3, mdp, nombre, nom))
    bouton.place(x=800, y=565)


def Connexion4(detruit, mdp, nombre, nom):
    
    createfen(Con4, "1200x600", "grey", "1")
    detruit.withdraw()
    
    ##Execution de la fonction login
    numimage, nombre= login(mdp, nombre)

    ##Affichage du diaporama
    image_button(Con4,15, numimage,"", "Connexion")

    ##Font 
    my_font = font.Font(Con4, ('Helvetica', 15, 'bold'))

    ##Texte
    texte = "Choisissez 0, 1 ou 2 image(s) qui corresponde(nt) à votre mot de passe puis cliquez sur suivant"

    ##Label
    label = Label(Con4, text=texte, background='grey', font=my_font, wraplength=500, anchor=W, justify=LEFT)
    label.place(x=20, y=560, width=500, height=49)

    ##Bouton
    bouton = Button(Con4, text="Suivant", background='red' ,command=lambda:Connexion5(Con4, mdp, nombre, nom))
    bouton.place(x=800, y=560)

def Connexion5(detruit, mdp, nombre, nom):

    createfen(Con5, "1200x600", "grey", "1")
    detruit.withdraw()

    ##Execution de la fonction login
    numimage, nombre= login(mdp, nombre)
    
    ##Affichage du diaporama
    image_button(Con5,15, numimage,"", "Connexion")

    ##Font
    my_font = font.Font(Con5, ('Helvetica', 15, 'bold'))

    ##Texte
    texte = "Choisissez 0, 1 ou 2 image(s) qui corresponde(nt) à votre mot de passe puis cliquez sur suivant"

    ##Label
    label = Label(Con5, text=texte, background='grey', font=my_font, wraplength=500, anchor=W, justify=LEFT)
    label.place(x=20, y=560, width=500, height=49)

    ##Bouton   
    bouton = Button(Con5, text="Suivant",background='red', command=lambda:start(Con5, nom))
    bouton.place(x=800, y=560)

def start(detruit, nom):
    
    detruit.withdraw()

    ##Transformation de la liste en Integer
    choix2= list (map (int, choix))
    
    ##Rangement par odre croissant des deux listes.
    mdp_choisi_random.sort()
    choix2.sort()
    
    if mdp_choisi_random==choix2:
        createfen(log1, "1280x700", "grey","0")
        menu_bar(log1)
        my_font = font.Font(log1, ('Helvetica', 12, 'bold'))
        pseudo = read_pseudos()
        #Si le pseudo n'est pas enregistré
        if not nom in pseudo:
            bouton_1erefois = Button(log1, text="Tutoriel", command=lambda:themes(log1,nom))
            bouton_1erefois.place(x=580, y=280)
            bouton_1erefois.configure(background="red", foreground="black")
        else:
            bouton_connexion = Button(log1, text="Connexion", command=lambda: gestion_1(log1,nom))
            bouton_connexion.place(x=580, y=280)
            bouton_connexion.configure(background="red", foreground="black")

    else:
        error="Mot de passe incorrect ! "
        Connexion2(Con5, nom, error)
def themes(detruit,nom):
    #globaliser pour ne pas encombrer les paramètres de la fonction
    global E1
    global E2
    global E3
    detruit.withdraw()
    createfen(log2, "1280x700", "grey", "0")
    my_font = font.Font(log2, ('Helvetica', 12, 'bold'))
    menu_bar(log2)

    themes1 = Label(log2, text="Nommer ci-dessous les thèmes de mots de passe choisies:", background='grey', font=my_font, wraplength=500, anchor=W, justify=LEFT)
    themes1.config(width=80, height=4)
    themes1.place(x=200, y=30)

    E1 = Entry(log2)
    E1.place(x=540, y=120, width=150)
    E2 = Entry(log2)
    E2.place(x=540, y=195, width=150)
    E3 = Entry(log2)
    E3.place(x=540, y=270, width=150)
    bouton_valider = Button(log2, text='Valider',background='red',  command=lambda:categories(log2,nom))
    bouton_valider.place(relx=0.80, rely=0.6)


def categories(detruit, nom):
    #globaliser pour ne pas encombrer les paramètres de la fonction
    global G1
    global G2
    global G3
    global C1_1
    global C2_1
    global C3_1
    global C1_2
    global C2_2
    global C3_2
    G1 = str(E1.get())
    entree_liste.append(G1)
    G2 = str(E2.get())
    entree_liste.append(G2)
    G3 = str(E3.get())
    entree_liste.append(G3)
    detruit.withdraw()
    createfen(log3, "1280x700", "grey", "0")
    menu_bar(log3)
    my_font = font.Font(log3, ('Helvetica', 12, 'bold'))
    categorie1 = Label(log3, text="Nommer les catégories pour le thème {}:".format(entree_liste[0]), background='grey', font=my_font, wraplength=500, anchor=W, justify=LEFT)
    categorie1.place(x=150, y=30)
    #Place les entrées des catégories
    C1_1 = Entry(log3)
    C1_1.place(x=360, y=120, width=150)
    C2_1 = Entry(log3)
    C2_1.place(x=360, y=195, width=150)
    C3_1 = Entry(log3)
    C3_1.place(x=360, y=270, width=150)
    categorie2 = Label(log3, text="Nommer les catégories pour le thème {}:".format(entree_liste[1]),
                       background='grey', font=my_font, wraplength=500, anchor=W, justify=LEFT)
    categorie2.place(x=400, y=30)
    C1_2 = Entry(log3)
    C1_2.place(x=540, y=120, width=150)
    C2_2 = Entry(log3)
    C2_2.place(x=540, y=195, width=150)
    C3_2 = Entry(log3)
    C3_2.place(x=540, y=270, width=150)
    bouton_valider = Button(log3, text='Valider',background='red', command=lambda:gestion_1(log3,nom))
    bouton_valider.place(relx=0.80, rely=0.6)

def read_pseudos():
    n = 0
    liste_pseudos = []
    # Création du fichier
    open("mdps.txt", 'w').close()
    ## Si le ficher data.txt existe, le programme lit le ficher
    with open("mdps.txt", "r") as mdps:
        for mdp in mdps:
            n = n + 1
            if (n == 33):
                n = 1
            if (n == 0):
                pseudo = mdps.readline()
                pseudo = pseudo.replace("\n", "")
                liste_pseudos.append(pseudo)
            else:
                pass
    return liste_pseudos
def save_noms(nom):
    T1_1 = str(C1_1.get())
    entree_liste.append(T1_1)
    T2_1 = str(C2_1.get())
    entree_liste.append(T2_1)
    T3_1 = str(C3_1.get())
    entree_liste.append(T3_1)
    T1_2 = str(C1_2.get())
    entree_liste.append(T1_2)
    T2_2 = str(C2_2.get())
    entree_liste.append(T2_2)
    T3_2 = str(C3_2.get())
    entree_liste.append(T3_2)

    # Tri de la liste entree_liste:
    liste_triee = [entree_liste[0], entree_liste[3], entree_liste[4], entree_liste[5], entree_liste[1],
                   entree_liste[6], entree_liste[7], entree_liste[8], entree_liste[2]]
    #Ecrit dans le fichier
    with open("mdps.txt", "a+") as mdps:
            for i in range(33):
                if i == 0:
                    mdps.write("{}\n".format(nom))
                elif i == 1:
                    mdps.write("Thème 1 : {}\n".format(liste_triee[0]))
                elif i == 2:
                    mdps.write("Catégorie 1 : {} \n".format(liste_triee[1]))
                elif i == 6:
                    mdps.write("Catégorie 2 : {} \n".format(liste_triee[2]))
                elif i == 10:
                    mdps.write("Catégorie 3 : {} \n".format(liste_triee[3]))
                elif i == 14:
                    mdps.write("Thème 2 : {} \n".format(liste_triee[4]))
                elif i == 15:
                    mdps.write("Catégorie 1 : {} \n".format(liste_triee[5]))
                elif i == 19:
                    mdps.write("Catégorie 2 : {} \n".format(liste_triee[6]))
                elif i == 23:
                    mdps.write("Catégorie 3 : {} \n".format(liste_triee[7]))
                elif i == 27:
                    mdps.write("Thème 3 : {} \n".format(liste_triee[8]))
                else:
                    # Obliger de mettre un 0 pour que la string ne soit pas vide afin de pouvoir la transformer en int
                    mdps.write("0\n")

def gestion_1(detruit,nom):
    save_noms(nom)
    detruit.withdraw()
    createfen(log4, "1280x700", "grey", "0")
    menu_bar(log4)
    identites = []
    w_or_e = []
    #Mod permet de savoir la ligne précisement
    with open("mdps.txt", "r+") as mdps:
        for i in range(1):
            mdps.seek(0)
            all_lines = mdps.readlines()
            all_lines = [lines.rstrip("\n") for lines in all_lines]
        mod = all_lines[len(entree_liste) % 33]
        mod = int(mod)
        while mod <= len(all_lines):
            mod += 1
            if mod == 0 and mod != nom:
                break
            elif mod == 1:
                bouton_genre1 = Button(log4, text=all_lines[mod],background='red', command=lambda:[select_button(bouton_genre1,identites),gestion2(log4, mod, identites, nom,w_or_e)])
                bouton_genre1.place(x=400, y=280)
                continue

            elif mod == 14:
                bouton_genre2 = Button(log4, text=all_lines[mod],background='red', command=lambda: [select_button(bouton_genre2,identites),gestion2(log4, mod, identites, nom,w_or_e)])
                bouton_genre2.place(x=560, y=280)
                continue
            elif mod == 27:
                bouton_genre3 = Button(log4, text=all_lines[mod],background='red', command=lambda: [select_button(bouton_genre3,identites),gestion2(log4, mod, identites, nom,w_or_e)])
                bouton_genre3.place(x=720, y=280)
                break
            else:
                continue
def select_button(button,liste):
    liste.insert(0, str(button))

def gestion2(detruit,mod,identites,nom,w_or_e):
    detruit.withdraw()
    createfen(log5, "1280x700", "grey","0")
    menu_bar(log5)
    texte = Text()
    # Mod permet de savoir la ligne précisement
    with open("mdps.txt", "r+") as mdps:
        if mod == 0:
            pass
        else:
            for i in range(1):
                mdps.seek(0)
                all_lines = mdps.readlines()
                all_lines = [lines.rstrip("\n") for lines in all_lines]
            mod = all_lines[len(entree_liste) % 33]
            mod = int(mod)
        categories_liste = []
        #Ces 6 conditions permettent de savoir quel bouton a été cliqué
        if ".!toplevel4.!button" == identites[0]:
            while mod <= len(all_lines):
                mod += 1
                if mod == 0 and mod != nom:
                    break
                elif mod == 2:
                    bouton_cat1 = Button(log5, text=all_lines[mod],background='red', command=lambda:[select_button(bouton_cat1,categories_liste), gestion3(log5,nom,categories_liste,w_or_e,texte)])
                    bouton_cat1.place(x=400, y=280)
                    continue

                elif mod == 6:
                    bouton_cat2 = Button(log5, text=all_lines[mod],background='red', command=lambda: [select_button(bouton_cat2,categories_liste), gestion3(log5,nom,categories_liste,w_or_e,texte)])
                    bouton_cat2.place(x=560, y=280)
                    continue
                elif mod == 10:
                    bouton_cat3 = Button(log5, text=all_lines[mod],background='red', command=lambda: [select_button(bouton_cat3,categories_liste), gestion3(log5,nom,categories_liste,w_or_e,texte)])
                    bouton_cat3.place(x=720, y=280)
                    break
                else:
                    continue
        if ".!toplevel4.!button2" == identites[0]:
            while mod <= len(all_lines):
                mod += 1
                if mod == 0 and mod != nom:
                    break
                elif mod == 15:
                    bouton_cat4 = Button(log5, text=all_lines[mod],background='red', command=lambda: [select_button(bouton_cat4,categories_liste), gestion3(log5,nom,categories_liste,w_or_e,texte)])
                    bouton_cat4.place(x=400, y=280)
                    continue

                elif mod == 19:
                    bouton_cat5 = Button(log5, text=all_lines[mod],background='red', command=lambda: [select_button(bouton_cat5,categories_liste), gestion3(log5,nom,categories_liste,w_or_e,texte)])
                    bouton_cat5.place(x=560, y=280)
                    continue
                elif mod == 23:
                    bouton_cat6 = Button(log5, text=all_lines[mod],background='red', command=lambda: [select_button(bouton_cat6,categories_liste), gestion3(log5,nom,categories_liste,w_or_e,texte)])
                    bouton_cat6.place(x=720, y=280)
                    break
                else:
                    continue
        if ".!toplevel4.!button3" == identites[0]:
            log5.withdraw()
            createfen(log6, "1280x700", "grey", "0")
            no_categorie = []
            menu_barv2(log6, nom, no_categorie, w_or_e)
            my_font = font.Font(fen2, ('Helvetica', 12, 'bold'))
            labelnocat1 = Label()
            labelnocat2 = Label()
            labelnocat3 = Label()
            stringnocat = 'Mot de passe '
            with open("mdps.txt", "r+") as mdps:

                for i in range(1):
                    mdps.seek(0)
                    all_lines = mdps.readlines()
                    all_lines = [lines.rstrip("\n") for lines in all_lines]
                mod = all_lines[len(entree_liste) % 33]
                mod = int(mod)
                while mod <= len(all_lines):
                    mod += 1
                    if mod == 0 and mod != nom:
                        break
                    elif mod == 29:
                        lire_ligne("mdps.txt", mod, no_categorie)
                        continue
                    elif mod == 30:
                        lire_ligne("mdps.txt", mod, no_categorie)
                        continue
                    elif mod == 31:
                        lire_ligne("mdps.txt", mod, no_categorie)
                        break
                    elif mod == 32:
                        lire_ligne("mdps.txt", mod, no_categorie)
                        continue
                    elif mod == 33:
                        lire_ligne("mdps.txt", mod, no_categorie)
                        break
                    else:
                        continue

            if labelnocat1.winfo_exists() == True:
                labelnocat1.configure(log8, text='',background='grey', font=my_font, wraplength=500, anchor=W, justify=LEFT)
                labelnocat1.pack()
            if labelnocat2.winfo_exists() == True:
                labelnocat2.configure(log8, text='',background='grey', font=my_font, wraplength=500, anchor=W, justify=LEFT)
                labelnocat2.pack()
            if labelnocat3.winfo_exists() == True:
                labelnocat3.configure(log8, text='',background='grey', font=my_font, wraplength=500, anchor=W, justify=LEFT)
                labelnocat3.pack()
            for i in range(1):
                jk = stringnocat + " : {} ".format(no_categorie[i])
                jk2 = stringnocat + " : {} ".format(no_categorie[i + 1])
                jk3 = stringnocat + " : {} ".format(no_categorie[+2])
                labelnocat1.configure(text=jk)
                labelnocat2.configure(text=jk2)
                labelnocat3.configure(text=jk3)

def menu_bar(fenetre):
    #Barre de menu pour tout ce qui est en dehors du gestionnaire en lui-même
    menu = Menu(fenetre)
    menu.add_command(label="Retour menu", command=lambda: Menu1(fenetre))
    menu.add_command(label="Quit", command=quit)
    fenetre.config(menu=menu)

def menu_barv2(fenetre,nom,categories_liste,w_or_e):
    menu_bar(fenetre)
    menu = Menu(fenetre)
    #Barre de menu pour le gestionnaire
    if categories_liste != []:
        menu.add_command(label="New", command=lambda: afficher_mdps(menu,"New",nom,categories_liste,w_or_e))
        menu.add_command(label="Edit", command=lambda: afficher_mdps(menu,"Edit",nom,categories_liste,w_or_e))
        menu.add_command(label="Retour menu", command=lambda: Menu1(fenetre))
        menu.add_command(label="Quit", command=quit)
        fenetre.config(menu=menu)
    else:
        menu.add_command(label="New", command=lambda: afficher_mdpsv2(menu, "New", nom, categories_liste,w_or_e))
        menu.add_command(label="Edit", command=lambda: afficher_mdpsv2(menu, "Edit", nom, categories_liste,w_or_e))
        menu.add_command(label="Retour menu", command=lambda: Menu1(fenetre))
        menu.add_command(label="Quit", command=quit)
        fenetre.config(menu=menu)


def afficher_texte(line_num1,widget,item2):
    #Permet d'afficher le texte
    lines = open("mdps.txt", 'r').readlines()
    if item2 == "3mdps":
        texte = lines[line_num1]
        line_num1 = (line_num1 % 3)+1
        line_num1 = str(line_num1)
        line_num1 = line_num1 + ".0"
        line_num1 = float(line_num1)
        widget.insert(str(line_num1), texte)
    if item2 == "5mdps":
        texte = lines[line_num1]
        line_num1 = (line_num1 % 5)+1
        line_num1 = str(line_num1)
        line_num1 = line_num1 + ".0"
        line_num1 = float(line_num1)
        widget.insert(str(line_num1), texte)


def afficher_mdps(menu,item,nom,categories_liste,w_or_e):
    #Permet d'afficher pour les 3 mots de passe
    new = menu.entrycget(1, "label")
    edit = menu.entrycget(2, "label")
    createfen(log7, "1280x700", "grey", "0")
    menu_bar(log7)
    my_font = font.Font(fen2, ('Helvetica', 12, 'bold'))
    w_or_e.append(["0"])
    if new == item:
        information1 = Label(log7,
                            text="Ecrivez vos 3 mots de passes tout en respectant la règle d'un mot de passe par ligne ",background='grey', font=my_font, wraplength=500, anchor=W, justify=LEFT)
        information1.place(x=200, y=100)
        texte = Text(log7, height=3, width=20)
        texte.place(x=500, y=200)
        buttonSave1 = Button(log7, text="Valider", background='red',command=lambda: [select_button(buttonSave1,w_or_e), save_mdps(nom,categories_liste,w_or_e,texte),gestion3(log7,nom,categories_liste,w_or_e,texte)])
        buttonSave1.place(x=630, y=112)
    if edit == item:
        information2 = Label(log7,
                            text="Modifiez vos 3 mots de passes tout en respectant la règle d'un mot de passe par ligne ",background='grey', font=my_font, wraplength=500, anchor=W, justify=LEFT)
        information2.place(x=200, y=100)
        texte = Text(log7, height=3, width=20)
        texte.place(x=500, y=200)
        b1, b2, b3, b4, b5, b6 = save_mdps(nom, categories_liste,w_or_e,texte)
        with open("mdps.txt", "r+") as mdps:
            for i in range(1):
                mdps.seek(0)
                all_lines = mdps.readlines()
                all_lines = [lines.rstrip("\n") for lines in all_lines]
            mod = all_lines[len(entree_liste) % 33]
            mod = int(mod)
        if b1 == categories_liste[0]:
            while mod <= len(all_lines):
                mod += 1
                if mod == 0 and mod != nom:
                    break
                elif mod == 3:
                    afficher_texte(mod, texte,"3mdps")
                    continue
                elif mod == 4:
                    afficher_texte(mod, texte,"3mdps")
                    continue
                elif mod == 5:
                    afficher_texte(mod, texte,"3mdps")
                    break
                else:
                    continue
        elif b2 == categories_liste[0]:
            while mod <= len(all_lines):
                mod += 1
                if mod == 0 and mod != nom:
                    break
                elif mod == 7:
                    afficher_texte(mod, texte,"3mdps")
                    continue
                elif mod == 8:
                    afficher_texte(mod, texte,"3mdps")
                    continue
                elif mod == 9:
                    afficher_texte(mod, texte,"3mdps")
                    break
                else:
                    continue
        elif b3 == categories_liste[0]:
            while mod <= len(all_lines):
                mod += 1
                if mod == 0 and mod != nom:
                    break
                elif mod == 11:
                    afficher_texte(mod, texte,"3mdps")
                    continue
                elif mod == 12:
                    afficher_texte(mod, texte,"3mdps")
                    continue
                elif mod == 13:
                    afficher_texte(mod, texte,"3mdps")
                    break
                else:
                    continue
        elif b4 == categories_liste[0]:
            while mod <= len(all_lines):
                mod += 1
                if mod == 0 and mod != nom:
                    break
                elif mod == 16:
                    afficher_texte(mod, texte,"3mdps")
                    continue
                elif mod == 17:
                    afficher_texte(mod, texte,"3mdps")
                    continue
                elif mod == 18:
                    afficher_texte(mod, texte,"3mdps")
                    break
                else:
                    continue
        elif b5 == categories_liste[0]:
            while mod <= len(all_lines):
                mod += 1
                if mod == 0 and mod != nom:
                    break
                elif mod == 20:
                    afficher_texte(mod, texte,"3mdps")
                    continue
                elif mod == 21:
                    afficher_texte(mod, texte,"3mdps")
                    continue
                elif mod == 22:
                    afficher_texte(mod, texte,"3mdps")
                    break
                else:
                    continue
        elif b6 == categories_liste[0]:
            while mod <= len(all_lines):
                mod += 1
                if mod == 0 and mod != nom:
                    break
                elif mod == 24:
                    afficher_texte(mod, texte,"3mdps")
                    continue
                elif mod == 25:
                    afficher_texte(mod, texte,"3mdps")
                    continue
                elif mod == 26:
                    afficher_texte(mod, texte,"3mdps")
                    break
                else:
                    continue
        buttonSave2 = Button(log7, text="Valider",background='red', command=lambda: [save_mdps(nom,categories_liste,w_or_e,texte),gestion3(log7,nom,categories_liste,w_or_e,texte)])
        buttonSave2.place(x=630, y=112)

def afficher_mdpsv2(menu,item,nom,categories_liste,w_or_e):
    #Permet d'afficher pour les 5 mots de passe

    new = menu.entrycget(1, "label")
    edit = menu.entrycget(2, "label")
    createfen(log7, "1280x700", "grey", "0")
    menu_barv2(log7,nom,categories_liste,w_or_e)
    my_font = font.Font(fen2, ('Helvetica', 12, 'bold'))
    w_or_e.append(["1"])
    if new == item:

        information1 = Label(log7,
                             text="Ecrivez vos 5 mots de passes tout en respectant la règle d'un mot de passe par ligne ",background='grey', font=my_font, wraplength=500, anchor=W, justify=LEFT)
        information1.place(x=200, y=100)
        texte = Text(log7, height=5, width=20)
        texte.place(x=500, y=200)
        buttonSave1 = Button(log7, text="Valider",background='red', command=lambda: [select_button(buttonSave1, w_or_e),
                                                                    save_mdps(nom, categories_liste,w_or_e,texte),
                                                                    gestion3(log7, nom, categories_liste,w_or_e,texte)])
        buttonSave1.place(x=630, y=112)
    if edit == item:
        information2 = Label(log7,
                             text="Modifiez vos 5 mots de passes tout en respectant la règle d'un mot de passe par ligne ",background='grey', font=my_font, wraplength=500, anchor=W, justify=LEFT)
        information2.place(x=200, y=100)
        texte = Text(log7, height=5, width=20)
        texte.place(x=500, y=200)
        with open("mdps.txt", "r+") as mdps:
            for i in range(1):
                mdps.seek(0)
                all_lines = mdps.readlines()
                all_lines = [lines.rstrip("\n") for lines in all_lines]
            mod = all_lines[len(entree_liste) % 33]
            mod = int(mod)
        while mod <= len(all_lines):
            mod += 1
            if mod == 0 and mod != nom:
                break
            elif mod == 29:
                afficher_texte(mod, texte,"5mdps")
                continue
            elif mod == 30:
                afficher_texte(mod, texte,"5mdps")
                continue
            elif mod == 31:
                afficher_texte(mod, texte,"5mdps")
                continue
            elif mod == 32:
                afficher_texte(mod, texte,"5mdps")
                continue
            elif mod == 33:
                afficher_texte(mod, texte,"5mdps")
                break
            else:
                continue

        buttonSave2 = Button(log7, text="Valider",background='red', command=lambda: [save_mdps(nom, categories_liste,texte),
                                                                    gestion3(log7, nom, categories_liste,w_or_e,texte)])
        buttonSave2.place(x=630, y=112)
def replace_line(file_name, line_num, text):
    #Permet de remplacer les lignes
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()
def save_mdps(nom,categories_liste,w_or_e,texte):
    #Permet de sauvegarder les mots de passe dnas le ficier texte
    valeurs = []
    bouton_categorie1 = '.!toplevel5.!button'
    bouton_categorie2 = '.!toplevel5.!button2'
    bouton_categorie3 = '.!toplevel5.!button3'
    bouton_categorie4 = '.!toplevel5.!button4'
    bouton_categorie5 = '.!toplevel5.!button5'
    bouton_categorie6 = '.!toplevel5.!button6'
    with open("mdps.txt", "r+") as mdps:
        for i in range(1):
            mdps.seek(0)
            all_lines = mdps.readlines()
            all_lines = [lines.rstrip("\n") for lines in all_lines]
        mod = all_lines[len(entree_liste) % 33]
        mod = int(mod)

    if w_or_e[0] == "0":
        for i in range(3):
            i += 1
            i = str(i)
            i = i + ".0"
            i = float(i)
            valeur_user = texte.get(str(i), str(i + 1))
            valeurs.append(valeur_user)
        if bouton_categorie1 == categories_liste[0]:
            while mod <= len(all_lines):
                mod += 1
                if mod == 0 and mod != nom:
                    break
                elif mod == 4:
                    replace_line("mdps.txt",mod,valeurs[0])
                    continue
                elif mod == 5:
                    replace_line("mdps.txt", mod, valeurs[1])
                    continue
                elif mod == 6:
                    replace_line("mdps.txt", mod, valeurs[2])
                    break
                else:
                    continue
        if bouton_categorie2 == categories_liste[0]:
            while mod <= len(all_lines):
                mod += 1
                if mod == 0 and mod != nom:
                    break
                elif mod == 8:
                    replace_line("mdps.txt",mod,valeurs[0])
                    continue
                elif mod == 9:
                    replace_line("mdps.txt", mod, valeurs[1])
                    continue
                elif mod == 10:
                    replace_line("mdps.txt", mod, valeurs[2])
                    break
                else:
                    continue
        if bouton_categorie3 == categories_liste[0]:
            while mod <= len(all_lines):
                mod += 1
                if mod == 0 and mod != nom:
                    break
                elif mod == 12:
                    replace_line("mdps.txt",mod,valeurs[0])
                    continue
                elif mod == 13:
                    replace_line("mdps.txt", mod, valeurs[1])
                    continue
                elif mod == 14:
                    replace_line("mdps.txt", mod, valeurs[2])
                    break
                else:
                    continue
        if bouton_categorie4 == categories_liste[0]:
            while mod <= len(all_lines):
                mod += 1
                if mod == 0 and mod != nom:
                    break
                elif mod == 17:
                    replace_line("mdps.txt",mod,valeurs[0])
                    continue
                elif mod == 18:
                    replace_line("mdps.txt", mod, valeurs[1])
                    continue
                elif mod == 19:
                    replace_line("mdps.txt", mod, valeurs[2])
                    break
                else:
                    continue
        if bouton_categorie5 == categories_liste[0]:
            while mod <= len(all_lines):
                mod += 1
                if mod == 0 and mod != nom:
                    break
                elif mod == 21:
                    replace_line("mdps.txt",mod,valeurs[0])
                    continue
                elif mod == 22:
                    replace_line("mdps.txt", mod, valeurs[1])
                    continue
                elif mod == 23:
                    replace_line("mdps.txt", mod, valeurs[2])
                    break
                else:
                    continue
        if bouton_categorie6 == categories_liste[0]:
            while mod <= len(all_lines):
                mod += 1
                if mod == 0 and mod != nom:
                    break
                elif mod == 25:
                    replace_line("mdps.txt",mod,valeurs[0])
                    continue
                elif mod == 26:
                    replace_line("mdps.txt", mod, valeurs[1])
                    continue
                elif mod == 27:
                    replace_line("mdps.txt", mod, valeurs[2])
                    break
                else:
                    continue


    elif w_or_e[0] == "1":
        valeurs.seek(0)
        for i in range(5):
            i+=1
            i = str(i)
            i = i + ".0"
            i = float(i)
            valeur_user = texte.get(str(i), str(i+1))
            valeurs.append(valeur_user)
        while mod <= len(all_lines):
            mod += 1
            if mod == 0 and mod != nom:
                break
            elif mod == 29:
                replace_line("mdps.txt", mod, valeurs[0])
                continue
            elif mod == 30:
                replace_line("mdps.txt", mod, valeurs[1])
                continue
            elif mod == 31:
                replace_line("mdps.txt", mod, valeurs[2])
                continue
            elif mod == 32:
                replace_line("mdps.txt", mod, valeurs[3])
                continue
            elif mod == 33:
                replace_line("mdps.txt", mod, valeurs[4])
                break
            else:
                continue
    return bouton_categorie1,bouton_categorie2,bouton_categorie3,bouton_categorie4,bouton_categorie5,bouton_categorie6

def lire_ligne(file,index_ligne,liste_mdps):
    #Permet de lire une ligne grâce au mod
    with open(file, "r") as f:
        if len(liste_mdps) >= 4:
            liste_mdps[:] = []
        for i in range(index_ligne):
            ligne = f.readline()
            liste_mdps.append(ligne)
def gestion3(detruit,nom,categories_liste,w_or_e,texte):
    #Affiche les mots de passe dans des labels
    detruit.withdraw()
    createfen(log8, "1280x700", "grey", "0")
    menu_barv2(log8,nom,categories_liste,w_or_e)
    my_font = font.Font(fen2, ('Helvetica', 12, 'bold'))
    w_or_e.append("0")
    b1, b2, b3, b4, b5, b6 = save_mdps(nom, categories_liste,w_or_e,texte)
    string = 'Mot de passe '
    labels = []
    liste_mdps = []
    label1 = Label()
    label2 = Label()
    label3 = Label()
    with open("mdps.txt", "r+") as mdps:
        for i in range(1):
            mdps.seek(0)
            all_lines = mdps.readlines()
            all_lines = [lines.rstrip("\n") for lines in all_lines]
        mod = all_lines[len(entree_liste) % 33]
        mod = int(mod)
        if b1 == categories_liste[0]:
            while mod <= len(all_lines):
                mod += 1
                if mod == 0 and mod != nom:
                    break
                elif mod == 3:
                    lire_ligne("mdps.txt",mod,liste_mdps)
                    continue
                elif mod == 4:
                    lire_ligne("mdps.txt",mod,liste_mdps)
                    continue
                elif mod == 5:
                    lire_ligne("mdps.txt",mod,liste_mdps)
                    break
                else:
                    continue
        if b2 == categories_liste[0]:
            while mod <= len(all_lines):
                mod += 1
                if mod == 0 and mod != nom:
                    break
                elif mod == 7:
                    lire_ligne("mdps.txt", mod,liste_mdps)
                    continue
                elif mod == 8:
                    lire_ligne("mdps.txt", mod,liste_mdps)
                    continue
                elif mod == 9:
                    lire_ligne("mdps.txt", mod,liste_mdps)
                    break
                else:
                    continue
        if b3 == categories_liste[0]:
            while mod <= len(all_lines):
                mod += 1
                if mod == 0 and mod != nom:
                    break
                elif mod == 11:
                    lire_ligne("mdps.txt", mod,liste_mdps)
                    continue
                elif mod == 12:
                    lire_ligne("mdps.txt", mod,liste_mdps)
                    continue
                elif mod == 13:
                    lire_ligne("mdps.txt", mod,liste_mdps)
                    break
                else:
                    continue
        if b4 == categories_liste[0]:
            while mod <= len(all_lines):
                mod += 1
                if mod == 0 and mod != nom:
                    break
                elif mod == 16:
                    lire_ligne("mdps.txt", mod,liste_mdps)
                    continue
                elif mod == 17:
                    lire_ligne("mdps.txt", mod,liste_mdps)
                    continue
                elif mod == 18:
                    lire_ligne("mdps.txt", mod,liste_mdps)
                    break
                else:
                    continue
        if b5 == categories_liste[0]:
            while mod <= len(all_lines):
                mod += 1
                if mod == 0 and mod != nom:
                    break
                elif mod == 20:
                    lire_ligne("mdps.txt", mod, liste_mdps)
                    continue
                elif mod == 21:
                    lire_ligne("mdps.txt", mod, liste_mdps)
                    continue
                elif mod == 22:
                    lire_ligne("mdps.txt", mod, liste_mdps)
                    break
                else:
                    continue
        if b6 == categories_liste[0]:
            while mod <= len(all_lines):
                mod += 1
                if mod == 0 and mod != nom:
                    break
                elif mod == 24:
                    lire_ligne("mdps.txt", mod, liste_mdps)
                    continue
                elif mod == 25:
                    lire_ligne("mdps.txt", mod, liste_mdps)
                    continue
                elif mod == 26:
                    lire_ligne("mdps.txt", mod, liste_mdps)
                    break
                else:
                    continue

    if label1.winfo_exists() == True:
        label1.configure(log8, text='',background='grey', font=my_font, wraplength=500, anchor=W, justify=LEFT)
        label1.pack()
    if label2.winfo_exists() == True:
        label2.configure(log8, text='',background='grey', font=my_font, wraplength=500, anchor=W, justify=LEFT)
        label2.pack()
    if label3.winfo_exists() == True:
        label3.configure(log8, text='',background='grey', font=my_font, wraplength=500, anchor=W, justify=LEFT)
        label3.pack()
    for i in range(1):
        jk = string + " : {} ".format(liste_mdps[i])
        jk2 = string + " : {} ".format(liste_mdps[i+1])
        jk3 = string + " : {} ".format(liste_mdps[+2])
        label1.configure(text=jk)
        label2.configure(text=jk2)
        label3.configure(text=jk3)


def Inscription1(detruit, erreur):

    img_liste[:] = []
    createfen(fen2, "1000x400", "grey","0")
    detruit.withdraw()

    ##Font
    my_font = font.Font(fen2, ('Helvetica', 12, 'bold'))

    ##Label prénom
    prenom = Label(fen2, text="Nom", width=25, height=3, bg="grey", fg="white", font=my_font)
    prenom.place(x=20, y=50)

    ## Label nom

    name = Label(fen2, text="Prénom", width=25, height=3, bg="grey", fg="white", font=my_font)
    name.place(x=20, y=125)

    ## Label âge

    age = Label(fen2, text="Âge", width=25, height=3, bg="grey", fg="white", font=my_font)
    age.place(x=20, y=200)

    ## Label pseudonyme

    username = Label(fen2, text="Nom d'utilisateur", width=25, height=3, bg="grey", fg="white", font=my_font)
    username.place(x=20, y=275)

    ##Entrée du nom
    C1 = Entry(fen2)
    C1.place(x=220, y=140, width=150)

    ##Entrée du prénom
    C2 = Entry(fen2)
    C2.place(x=220, y=65, width=150)

    ##Entrée de l'âge
    C3 = Entry(fen2)
    C3.place(x=220, y=215, width=150)

    ##Entrée du nom d'utilisateur
    C4 = Entry(fen2)
    C4.place(x=220, y=295, width=150)

    
    ## Si la variable erreur n'est pas nulle les entrées sont remplies avec les données de l'Inscription2. 
    if erreur != "":
        C1.insert(END, mauvais_contenu[0])
        C2.insert(END, mauvais_contenu[1])
        C3.insert(END, mauvais_contenu[2])
        C4.insert(END, mauvais_contenu[3])
        mauvais_contenu[:] = []

    texte = erreur
    
    
    ## Placement du label texte qui est justifé vers la gauche
    label = Label(fen2, text=texte, background='grey', font=my_font, wraplength=500, anchor=W, justify=LEFT)
    label.place(x=20, y=350, width=650, height=40)

    ##Bouton valider
    bouton = Button(fen2, text="Valider", background='red' , command=lambda:Inscription2(fen2,C1,C2,C3,C4, "", label))
    bouton.place(x=630, y=112)

    ##Bouton retour
    bouton2 = Button(fen2, text="Retour", background='red' ,command=lambda:Menu1(fen2))
    bouton2.place(x=630, y=200)

  

def Inscription2(detruit, C1,C2,C3,C4, erreur,label):
    
    label.destroy()
    
    ##Données de l'entrée du prénom
    E1 = str(C1.get())

    ##Si la taille du prénom est inférieure à 3
    if len(E1)<3:
        erreur="Le prénom doit comporter au moins trois caractères !"
    ##Si la taille du prénom est supérieure à 16
    elif len(E1)>16 and  len(erreur) == 0:
        erreur="Le prénom ne peut dépasser seize caractères !"
    ##Sinon ajout de la donnée dans dat
    else:
        dat.append(E1)


    ##Données de l'entrée du nom
    E2 = str(C2.get())

    ##Si la taille du nom est inférieure à 3
    if len(E2)<3 and len(erreur) == 0:
        erreur="Le nom doit comporter au moins trois caractères !"
    ##Si la taille du prénom est supérieure à 16
    elif len(E2)>16 and len(erreur) == 0!="" :
        erreur="Le nom ne peut dépasser seize caractères !"
    elif E2=="" and  len(erreur) == 0:
        erreur= "Veillez entrer une information au nom !"
    ##Sinon ajout de la donnée dans dat    
    else:
        dat.append(E2)

        
    ##Données de l'entrée de l'âge    
    E3 = str(C3.get())

    E3str=str(C3.get())
    ##Vérification que l'entrée est bien un integer.
    try:
        E3=int(E3)
    except ValueError:
        if len(erreur) == 0:
            erreur="L'âge doit être un nombre !"

            
    if  len(erreur) == 0:
        ##Vérification de la réalité de l'âge
        if 12<=E3<=120:
            dat.append(E3)
        elif E3 <12:
            erreur= "Il faut avoir 12 ans pour s'inscrire !"
        
        else :
            erreur= "Il ne faut pas être immortel pour s'inscrire !"

    ##Obtention de la liste des utilisateurs
    users=readuser()
    ##Données de l'entrée du nom d'utilisateur 
    E4 = str(C4.get())

    ##Si la taille du pseudo est inférieure à 3
    if len(E4)<3 and  len(erreur) == 0:
        erreur="Le pseudo doit comporter au moins trois caractères !"
    ##Si la taille du pseudo est supérieure à 16
    elif len(E4)>16 and len(erreur) == 0:
        erreur="Le pseudo ne peut dépasser seize caractères !"
    ##Si le nom d'utilisateur est déjà utilisé
    elif E4 in users and  len(erreur) == 0:
        erreur= "Nom d'utilisateur déjà  utilisé !"
    ##Si le nom d'utilisateur posséde des espaces
    elif E4.find(" ")>0 and  len(erreur) == 0: 
        erreur="Pas d'espace dans le nom d'utilisateur !"
    ##Sinon la donnée est ajoutée
    else:
        dat.append(E4)        
  

    ##Si il y a une erreur, le mauvais contenu est enregistré dans des variables.
    if erreur != "" :
        if len(E1)!=0:
            mauvais_contenu.append(E1)
        else:
            mauvais_contenu.append("")
        if len(E2)!=0:
            mauvais_contenu.append(E2)
        else:
            mauvais_contenu.append("")
        if len(E3str)!=0:
            mauvais_contenu.append(E3)
        else:
            mauvais_contenu.append("")
        if len(E4)!=0:
            mauvais_contenu.append(E4)
        else:
            mauvais_contenu.append("")
            
     ##L'utilisateur est renvoyé sur la page d'inscription        
        dat[:] = []
        Inscription1(fen1, erreur)

        
    ##Si il n'y a pas d'erreur le programme continu.   
    else:

        
        detruit.withdraw()
        createfen(fen3, "1000x400", "grey","0")

        ##Création de la police
        my_font = font.Font(fen3, ('Helvetica', 15, 'bold'))

        ##String texte qui contient le message à afficher sur l'écran
        texte = ("Bienvenue {0}, pour pouvoir finaliser l'inscription vous allez devoir mémoriser 3 images qui correspondront à votre mot de passe. Il sera nécessaire de les retenir !").format(E1)

        ##Placement du label texte qui est justifé vers la gauche
        label = Label(fen3, text=texte, background='grey', font=my_font, wraplength=500, anchor=W, justify=LEFT)
        label.place(x=20, y=50, width=500, height=200)

        ##Bouton valider
        valider = Button(fen3, text="Valider",background='red' , command=lambda:Inscription3(fen3))
        valider.place(x=900, y=112)


def Inscription3(detruit):
    image=[]
    ##Vérification que la fonction n'est pas utilisée aprés une erreur. 
    if detruit != fen4:
        detruit.withdraw()
        createfen(fen4, "1200x600", "grey", "1")
    else:
        img_liste[:] = []


    ##Choix des images pour le diaparama
    for i in range(15):
        
        number = random.randint(1, 19)
        while number in image:
                number = random.randint(1, 19)
        image.append(number)

    ##Font 
    my_font = font.Font(fen2, ('Helvetica', 12, 'bold'))

    ##String texte qui contient le message à afficher sur l'écran
    texte = "Vous devez encore choisir 3 images"

    ##Placement du label texte qui est justifé vers la gauche
    label = Label(fen4, text=texte, background='grey', font=my_font, wraplength=500, anchor=W, justify=LEFT)
    label.place(x=20, y=560, width=500, height=40)

    
    image_button(fen4 ,15, image, label, "Inscription")
        
    
    ##Bouton valider qui fait appel à la fonction save data
    valider = Button(fen4, text="Valider", background='red' ,command=lambda:Inscription4(fen4))
    valider.place(x=800, y=560)


def save_data():
    donnees=[]
    ##Si le fichier existe le programme lit ce qu'il y a l'intéreur pour l'ajouter dans la liste données
    try:
        with open("data.txt", "r") as data:
            for i in range(1):
                readuser = data.readline()
                readuser = int(readuser)
            for i in range(1, readuser * 8):
                infos = data.readline()
                donnees.append(infos)
    ##Sinon, il fabrique un fichier texte et rentre des informations pour lancer correctement la suite de la fonction. 
    except IOError:
        readuser = 0
        with open("data.txt", "w") as data:
            for i in range(8):
                if i == 0:
                    data.write("0\n")

                elif i == 1:
                    data.write("Prénom\n")
                elif i == 2:
                    data.write("nom\n")
                elif i == 3:
                    data.write("17\n")
                elif i == 4:
                    data.write("username\n")
                elif i == 5:
                    data.write("8\n")
                elif i == 6:
                    data.write("9\n")
                else:
                    data.write("10\n")

    ##Ajout des données de l'utilisateur qui s'inscrit dans la liste données pour l'écrire dans le fichier texte.
    for i in range(7):
        realdata = "{}\n".format(dat[i])
        donnees.append(realdata)
       
    with open("data.txt", "w") as data:

        ##Ecriture des données sur le fichier data.txt
        for i in range(len(donnees) + 1):

            if i == 0:
                if readuser == "":
                    data.write("1\n")
                else:
                    readuser = int(readuser)
                    readuser += 1
                    data.write(str(readuser) + "\n")
            else:
                data.write("{}".format(donnees[i - 1]))


##Cette fonction exécute save_data et affiche les images correpondantes à celles choisies par l'utilisateur pour son mot de passe.
def Inscription4(detruit):
    
    deplacement=0
    hauteur=50
    ##Condition qui vérifie que l'utilisateur a bien choisi 3 images    
    if(len(mdp)!=3):
        mdp[:] = []
        Inscription3(fen4)
    ##Sinon, ajout des données dans la variable dat 
    else:
        for i in range(3):
            dat.append(mdp[i])

    createfen(fen5, "750x400", "grey", "0")
    detruit.withdraw()
    fen5.withdraw()

   ##Execution de save_data
    save_data()

    ##Affichage des Canvas
    for j in range(4, 7):
        ##Image des données
        number1 = dat[j]
        ##Ajout du préfixe
        myimg1 = str(number1) + '.png'
        ##Utilisation du dossier
        path=os.path.join("images", myimg1)
        im1 = PhotoImage(file=path)
        ##Recadrage de l'image
        im1 = im1.subsample(5, 5)
        img_liste.append(im1)
        ##Déplacement pour placer les images 
        if (j - 4) != 0:
            deplacement = deplacement + 250
        if (j - 4) % 5 == 0 and (j - 4) != 0:
            hauteur = hauteur + 220
            deplacement = 0

        #Creation du widget contenant l'image
        canvas = Canvas(fen5,width=195, height=130, bg='white')
        canvas.create_image(80, 75, image=im1)
        canvas.place(x=deplacement, y=hauteur)

        
    fen5.deiconify()

    ##Texte 
    texte = ("Félicitations ! Votre inscription est terminée. Mémoriser une dernière fois, les images qui correspondent à votre mot de passe!")

    ##Font
    police = font.Font(fen5, ('Helvetica', 15, 'bold'))

    ##Label
    label = Label(fen5, text=texte, background='grey', font=police, wraplength=500, anchor=W, justify=LEFT)
    label.place(x=0, y=270, width=500, height=100)

    ##Bouton valider 
    valider = Button(fen5, text="Terminer l'inscription", background='red' , command=lambda:Menu1(fen5))
    valider.place(x=510, y=270)

    ##Remise des variables à zéro
 
    mauvais_contenu[:] = []
    dat[:] = []
    mdp[:] = []
    erreur=""


## Execution du programme.
if __name__ == '__main__':
    Menu1("")
    fen1.mainloop()
