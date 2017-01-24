""" Programme visant à réaliser des simulations de comportements et d'organisation chez un insect social, la fourmis """

class Fourmis: # class définissant une fourmis, caractérisée par :

# son espèce
# sa colonie
# sa ponte
# son numéro de ponte
# son âge
# sa caste
# sa santé
# son intégrité
# son énergie
# son chargement
# sa position x, y et z

    compteur_numero_ponte = 0 # Le compteur vaut 0 au départ de l'année

    def __init__(self, espece, colonie): # méthode constructeur
        
        Fourmis.compteur_numero_ponte += 1 # À chaque fois que l'on crée une fourmis, on incrémente le compteur de 1

        self._espece = espece
        self._colonie = colonie
        self._ponte = 1
        self._numero_ponte = Fourmis.compteur_numero_ponte
        self._age = 0
        self._caste = "NA"
        self._sante = 0
        self._integrite = 100
        self._energie = 100
        self._chargement = 0
        self._positionX = 0
        self._positionY = 0
        self._positionZ = 0
        
#------ESPECE
    def _get_espece(self): # Getter ou Accesseur pour l'attribut privé _espece
        print("L'objet {} est une {}.\n".format(id(self), self._espece))
    def _set_espece(self, new_espece): # Setter ou Mutateur pour l'attribut privé _espece
        print ("Vous ne pouvez pas modifier l'espèce d'une fourmis ! O_o\n")
    espece = property(_get_espece, _set_espece) # espece est maitenant une propriété
#------COLONIE
    def _get_colonie(self): # Getter ou Accesseur pour l'attribut privé _colonie
        print("L'objet {} provient de la colonie {}.\n".format(id(self), self._colonie))
    def _set_colonie(self, new_colonie): # Setter ou Mutateur pour l'attribut privé _colonie
        print ("Vous ne pouvez pas modifier la colonie d'origine d'une fourmis ! O_o\n")
    colonie = property(_get_colonie, _set_colonie) # colonie est maitenant une propriété
#------PONTE
    def _get_ponte(self): # Getter ou Accesseur pour l'attribut privé _ponte
        print("L'objet {} est issu de la ponte n°{}.\n".format(id(self), self._ponte))
    def _set_ponte(self, new_ponte): # Setter ou Mutateur pour l'attribut privé _ponte
        print ("Vous ne pouvez pas modifier la ponte dont est issue une fourmis ! O_o\n")
    ponte = property(_get_ponte, _set_ponte) # ponte est maitenant une propriété
#------NUMERO_PONTE
    def _get_numero_ponte(self): # Getter ou Accesseur pour l'attribut privé _numero_ponte
        print("L'objet {} est la {}ème de sa ponte.\n".format(id(self), self._numero_ponte))
    def _set_numero_ponte(self, new_numero_ponte): # Setter ou Mutateur pour l'attribut privé _numero_ponte
        print ("Vous ne pouvez pas modifier l'ordre de naissance d'une fourmis ! O_o\n")
    numero_ponte = property(_get_numero_ponte, _set_numero_ponte) # numero_ponte est maitenant une propriété
#------AGE
    def _get_age(self): # Getter ou Accesseur pour l'attribut privé _age
        print("L'objet {} a {} jours.\n".format(id(self), self._age))
    def _set_age(self, new_age): # Setter ou Mutateur pour l'attribut privé _age
        print ("Vous ne pouvez pas modifier l'âge d'une fourmis ! O_o\n")
    age = property(_get_age, _set_age) # age est maitenant une propriété
#------CASTE
    def _get_caste(self): # Getter ou Accesseur pour l'attribut privé _caste
        print("L'objet {} fait partie de la caste des {}s.\n".format(id(self), self._caste))
    def _set_caste(self, new_caste): # Setter ou Mutateur pour l'attribut privé _caste
        print ("Attention !! \n L'objet {} n'est plus une {} ! \n Il fait maintenant partie de la caste des {}s !\n".format(id(self), self._caste, new_caste))
        self._caste = new_caste
    caste = property(_get_caste, _set_caste) # caste est maitenant une propriété
#------SANTE
    def _get_sante(self): # Getter ou Accesseur pour l'attribut privé _sante
        if self._sante == 0:
            print("L'objet {} est en bonne santée.\n".format(id(self)))
        if self._sante == 1:
            print("L'objet {} est malade.\n".format(id(self)))
    def _set_sante(self, new_sante): # Setter ou Mutateur pour l'attribut privé _sante
        if new_sante >= 1:
            new_sante = 1
        if new_sante < 1:
            new_sante = 0
        if new_sante == self._sante:
            print("Attention !! \n Vous n'avez pas changé l'état de santé de l'objet {}\n".format(id(self)))
        if new_sante > self._sante:
            print ("Attention !! \n L'objet {} n'est plus en bonne santé ! \n Il est maitenant malade !\n".format(id(self)))
        if new_sante < self._sante:
            print ("Attention !! \n L'objet {} n'est plus malade ! Il est maitenant en bonne sante !\n".format(id(self)))
        self._sante = new_sante
    sante = property(_get_sante, _set_sante) # sante est maitenant une propriété
#------INTEGRITE
    def _get_integrite(self): # Getter ou Accesseur pour l'attribut privé _integrite
        print("L'objet {} est intègre à {}%.\n".format(id(self), self._integrite))
    def _set_integrite(self, new_integrite): # Setter ou Mutateur pour l'attribut privé _integrite
        if new_integrite < self._integrite:
            print ("Attention !! \n L'objet {} c'est détérioré ! \n Il est maintenant intègre à {}% !\n".format(\
            id(self), self._integrite, new_integrite))
            self._integrite = new_integrite
        if new_integrite >= self._integrite:
            print ("Attention !! \n Vous ne pouvez pas rendre l'intégrité à une fourmis ! O_o")
    integrite = property(_get_integrite, _set_integrite) # integrite est maitenant une propriété
#------ENERGIE
    def _get_energie(self): # Getter ou Accesseur pour l'attribut privé _energie
        print("L'objet {} est à {}% de son énergie.\n".format(id(self), self._energie))
    def _set_energie(self, new_energie): # Setter ou Mutateur pour l'attribut privé _energie
        if new_energie >= 100:
            new_energie = 100
        if new_energie <= 0:
            new_energie = 0
        print ("Attention !! \n L'objet {} n'est plus à {}% de son énergie ! \n Il est maintenant à {}% !\n".format(\
            id(self), self._energie, new_energie))
        self._energie = new_energie
    energie = property(_get_energie, _set_energie) # energie est maitenant une propriété
#------CHARGEMENT
    def _get_chargement(self): # Getter ou Accesseur pour l'attribut privé _chargement
        if self._chargement == 0:
            print("L'objet {} n'est pas chargé.\n".format(id(self), self._chargement))
        if self._chargement == 1:
            print ("L'objet {} transporte actuellement un(e) QUELQUECHOSE.\n".format(id(self), self._chargement))
    def _set_chargement(self, new_chargement): # Setter ou Mutateur pour l'attribut privé _chargement
        if new_chargement >= 1:
            new_chargement = 1
        if new_chargement < 1:
            new_chargement = 0
        if new_chargement == self._chargement:
            print("Attention !! \n Vous n'avez pas changé l'état de chargement de l'objet {}\n".format(id(self)))
        if new_chargement > self._chargement:
            print ("Attention !! \n L'objet {} est maintenant chargé !\n Il transporte actuellement un(e) QUELQUECHOSE !\n".format(id(self)))
        if new_chargement < self._chargement:
            print ("Attention !! \n L'objet {} n'est plus chargé ! Il ne transporte rien actuellement !\n".format(id(self)))
        self._chargement = new_chargement
    chargement = property(_get_chargement, _set_chargement) # chargement est maitenant une propriété
#------POSITION-X
    def _get_positionX(self): # Getter ou Accesseur pour l'attribut privé _positionX
        print("L'objet {} est en position X = {}.\n".format(id(self), self._positionX))
    def _set_positionX(self, new_positionX): # Setter ou Mutateur pour l'attribut privé _positionX
        print ("Attention !! \n L'objet {} n'est plus en position X = {} ! \n Il c'est déplacé en position X = {} !\n".format(\
            id(self), self._positionX, new_positionX))
        self._positionX = new_positionX
    positionX = property(_get_positionX, _set_positionX) # positionX est maitenant une propriété
#------POSITION-Y
    def _get_positionY(self): # Getter ou Accesseur pour l'attribut privé _positionY
        print("L'objet {} est en position Y = {}.\n".format(id(self), self._positionY))
    def _set_positionY(self, new_positionY): # Setter ou Mutateur pour l'attribut privé _positionY
        print ("Attention !! \n L'objet {} n'est plus en position Y = {} ! \n Il c'est déplacé en position Y = {} !\n".format(\
            id(self), self._positionY, new_positionY))
        self._positionY = new_positionY
    positionY = property(_get_positionY, _set_positionY) # positionY est maitenant une propriété
#------POSITION-Z
    def _get_positionZ(self): # Getter ou Accesseur pour l'attribut privé _positionZ
        print("L'objet {} est en position Z = {}.\n".format(id(self), self._positionZ))
    def _set_positionZ(self, new_positionZ): # Setter ou Mutateur pour l'attribut privé _positionZ
        print ("Attention !! \n L'objet {} n'est plus en position Z = {} ! \n Il c'est déplacé en position Z = {} !\n".format(\
            id(self), self._positionZ, new_positionZ))
        self._positionZ = new_positionZ
    positionZ = property(_get_positionZ, _set_positionZ) # positionZ est maitenant une propriété
#------

class Gyne(Fourmis): # class définissant une gyne, héritant de la class Fourmis
    pass

class Oeuf(Fourmis): # class définissant un oeuf, héritant de la class Fourmis
    pass


def attributs(objet):
    
        objet.espece
        objet.colonie
        objet.ponte
        objet.numero_ponte
        objet.age
        objet.caste
        objet.sante
        objet.integrite
        objet.energie
        objet.chargement
        objet.positionX
        objet.positionY
        objet.positionZ

def ponte():
    oeuf = Oeuf("Messor_barbarus", 1)
    at_fourmis(oeuf)
    oeuf = Oeuf("Messor_barbarus", 1)
    at_fourmis(oeuf)
    
def multi_ponte(x):
    for i in range (0, x, 1):
        ponte()
        at_fourmis(oeuf)

def info_fourmis(x, y, z):
    for i in range (x, y, z):
        at_fourmis(["fourmis"+str(i)]())







