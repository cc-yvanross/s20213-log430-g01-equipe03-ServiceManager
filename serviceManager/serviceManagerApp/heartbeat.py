import threading
import time
import requests

from . import resources
from . import constants

class HeartBeat:
    """
    Classe singleton encapsulant la logique d'envoi de HeartBeats.


    Attributes
    ----------
    delay_ms : int
        Délai en millisecondes entre chaque envoi de heartbeat.
    __instance : Heartbeat
        Instance unique du singleton.
    
    Methods
    ----------
    get_instance() : HeartBeat
        Accesseur de l'instance unique.
    
    __init__(self)
        Constructeur de la classe.
    
    start(self)
        Méthode pour démarrer le processus d'envoi de signaux heartbeat.
    
    send_heartbeat(self):
        Processus d'envoi de signaux heartbeat.

    """
    delay_ms = 1000    
    __instance = None

    @staticmethod 
    def get_instance():
        """
        Accesseur de l'instance unique. Crée l'instance si elle est inexistante.

        Returns
        -------
        HeartBeat
            Instance unique de la classe.
        """
        if HeartBeat.__instance == None:
            HeartBeat()
        return HeartBeat.__instance

    def __init__(self):
        """
        Constructeur de la classe.

        Raises
        ------
        Exception
            Lorsqu'une initialisation est tentée alors que la classe est déjà instanciée.
        """
        if HeartBeat.__instance != None:
            raise Exception("This class is a singleton")
        else:
            HeartBeat.__instance = self

        self.receiver = resources.HEARTBEAT_RECEIVER_URI
       
    def start(self):
        """
        Méthode pour démarrer le processus d'envoi de signaux heartbeat.
        """
        self.thread = threading.Thread(target=self.send_heartbeat)
        self.thread.start()

    def send_heartbeat(self):
        """
        Processus d'envoi de signaux heartbeat.
        """
        time.sleep(HeartBeat.delay_ms/constants.MS_PER_SEC)
        requests.post(url=self.receiver, params={})
        self.send_heartbeat()
        