import mysql.connector as mysqlcon

class Base_donnee():

    def __init__ (self):
        self.host = 'localhost'
        self.port = 8081
        self.user = 'root'
        self.mdp = 'root'
        self.nom = 'jo'
        self.conn = None
        self.curseur = None 

    #############
    # CONNEXION #
    #############

    #Générer la connexion:
    def gen_connexion (self):

        #On teste si la connexion à la bdd n'existe pas :
        if self.conn == None:
            #Si pas de connexion, on en crée une à la bdd souhaitée en paramètre de la méthode :
            connexion = mysqlcon.connect(port = self.port,
                                        host = self.host,
                                        user = self.user,
                                        password = self.mdp,
                                        database = self.nom)

            setattr(self, "conn", connexion)       
    
    def fermer_connexion (self):
        self.conn.close()


    ###########
    # CURSEUR #
    ###########

    def creer_curseur (self):
        self.curseur = self.conn.cursor(buffered=True)

    def fermer_curseur (self):
        self.curseur.close()


    ############
    # REQUÊTES #
    ############

    def injecter_nocs(self, var):    
        sql = "INSERT INTO nocs (id_noc, noc, region, note) VALUES (NULL,%s,%s,%s);"
        self.curseur.executemany(sql, var)
        self.conn.commit()

    def injecter_equipes(self, var):
        """
        Insertion des équipes en base.
        """
        sql = "INSERT INTO equipes (id_equipe, equipe, id_noc) VALUES (NULL, %s, (SELECT nocs.id_noc FROM nocs WHERE nocs.noc =%s));"
        self.curseur.executemany(sql, var)
        self.conn.commit()

    def injecter_athletes(self, var):
        """
        Insertion des athlètes en base.
        """
        sql = "INSERT INTO athletes (id_athlete, nom, sexe) VALUES (%s, %s, %s);"
        self.curseur.executemany(sql, var)
        self.conn.commit()

    def injecter_jeux(self, var):
        """
        Insertion des jeux en base.
        """
        sql = """INSERT INTO jeux (id_jeu, jeu, annee, saison) VALUES (NULL, %s, %s, %s);"""
        self.curseur.executemany(sql, var)
        self.conn.commit()

    def injecter_sports(self, var):
        """
        Insertion des sports en base.
        """
        sql = """INSERT INTO sports (id_sport, sport) VALUES (NULL, %s);"""
        self.curseur.executemany(sql, var)
        self.conn.commit()

    def injecter_epreuves(self, var):
        """
        Insertion des epreuves en base.
        """
        sql = """INSERT INTO epreuves (id_epreuve, epreuve, id_sport) VALUES (NULL, %s, (SELECT sports.id_sport FROM sports WHERE sports.sport =%s));"""
        self.curseur.executemany(sql, var)
        self.conn.commit()

    def injecter_epreuves_jeux(self, var):
        """
        Remplissage de la table intermédiaire epreuves_jeux en base.
        """
        sql = """INSERT INTO epreuves_jeux (id_epreuve, id_jeu) VALUES ((SELECT epreuves.id_epreuve FROM epreuves WHERE epreuves.epreuve =%s), (SELECT jeux.id_jeu FROM jeux WHERE jeux.jeu =%s AND jeux.annee =%s AND jeux.saison =%s));"""
        self.curseur.executemany(sql, var)
        self.conn.commit()

    def injecter_athletes_epreuves(self, var):
        """
        Remplissage de la table intermédiaire athletes_epreuves en base.
        """
        sql = """INSERT INTO athletes_epreuves (id_athlete, id_epreuve, medaille, age, poids, taille) VALUES (%s, (SELECT epreuves.id_epreuve FROM epreuves WHERE epreuves.epreuve =%s), %s, %s, %s, %s);"""
        self.curseur.executemany(sql, var)
        self.conn.commit()

    def injecter_villes(self, var):
        """
        Remplissage de la table villes en base.
        """
        sql = """INSERT INTO villes (id_ville, ville) VALUES (NULL, %s);"""
        self.curseur.executemany(sql, var)
        self.conn.commit()

    def injecter_jeux_villes(self, var):
        """
        Remplissage de la table intermédiaire jeux_villes en base.
        """
        sql = """INSERT INTO jeux_villes (id_jeu, id_ville) VALUES ((SELECT jeux.id_jeu FROM jeux WHERE jeux.jeu = %s AND jeux.annee = %s AND jeux.saison = %s), (SELECT villes.id_ville FROM villes WHERE villes.ville = %s));"""
        self.curseur.executemany(sql, var)
        self.conn.commit()



    def injecter_equipes_athletes(self, var):
        """
        Remplissage de la table intermédiaire equipes_athletes en base.
        """ 

        # select id_equipe from equipes, nocs where nocs.id_noc=equipes.id_noc and nocs.noc="FRA" and equipes.equipe="Martha-1"

        sql = """INSERT INTO equipes_athletes (id_athlete, id_equipe) VALUES (%s, (SELECT equipes.id_equipe FROM equipes, nocs WHERE equipes.equipe = %s AND nocs.noc = %s AND nocs.id_noc = equipes.id_noc));"""
        self.curseur.executemany(sql, var)
        self.conn.commit()

        
    def injecter_athletes_sports(self, var):
        """
        Remplissage de la table intermédiaire athletes_sports en base.
        """ 

        sql = """INSERT INTO athletes_sports (id_athlete, id_sport) VALUES (%s, (SELECT sports.id_sport FROM sports WHERE sports.sport = %s));"""
        self.curseur.executemany(sql, var)
        self.conn.commit()