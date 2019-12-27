# coding: utf8

#Este .py contiene las clases que ayudan a construir de forma mas o menos semática redes neuronales
#

from .base import register_abstract_class
from .base import register_concrete_class
from .base import Algorithm, BaseObject, BaseAbstract

class Part_Of_NN:
    """ Esta clase representa lo que es común a un elemento de una red neuronal a nivel de código
    """
    def _build_model(self, model):
        raise NotImplementedError()


@register_abstract_class
class NN_Preprocesor(BaseAbstract, Part_Of_NN):
    """ Representa los posibles elementos para preprocesar los datos en una red neuronal
    """
    pass


@register_abstract_class
class NN_Reduction(BaseAbstract, Part_Of_NN):
    """ Representa los posibles elementos para reducir dimensiones en los datos ya preprocesados en una red neuronal
    """
    pass


@register_abstract_class
class NN_Abtract_Feautures(BaseAbstract, Part_Of_NN):
    """ Representa los posibles elementos para descubrir features de mas alto nivel(osea mas abstractos) en una red neuronal
    """
    pass


@register_abstract_class
class NN_Classifier(BaseAbstract, Part_Of_NN):
    """ Representa los posibles elementos para un clasificador o regresor en una red neuronal, esta tendría como salida el resultado
    que se está buscando.
    """
    pass
        

@register_concrete_class
class NeuralNetwork(BaseObject, Algorithm):
    """Representa a todas las posibles redes neuronales
    """
    def __init__(self, nn_preprocesor:NN_Preprocesor, nn_reduction:NN_Reduction, nn_abstract_features:NN_Abtract_Feautures, nn_clasifier:NN_Classifier):
        """Instancia una red neuronal basada en 4 componentes fundamentales:
        Preprocesamiento, Reductor de dimensiones, un componente para descubrir features de mas alto nivel(osea mas abstractos) y una componente
        que sería un clasificador o regresor.
        """
        self.nn_preprocesor = nn_preprocesor
        self.nn_reduction = nn_reduction
        self.nn_abstract_features = nn_abstract_features
        self.nn_clasifier = nn_clasifier

@register_abstract_class
class Basic_Clasifier(NN_Classifier):
    """
    Un sofmax o clasificador-regresor simple
    """
    
    pass

@register_concrete_class
class Compose_Clasifier(NN_Classifier):
    """Compone clases de capas densas y un sofmax o clasificador-regresor detras
    """

    def __init__(self, clasifier: Compose_Clasifier, basic_clasifier: Basic_Clasifier):
        self.clasifier = clasifier
        self.basic_clasifier = basic_clasifier


@register_concrete_class
class NN_None(BaseObject, NN_Preprocesor):
    """Representa un componente que se comporta como una capa pero devuelve por la salida lo mismo que le entra por la entrada.
    """
    def _build_model(self, model):
        return model
