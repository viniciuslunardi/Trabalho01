import pickle
from abc import ABC, abstractmethod


class DAO(ABC):
    __instance = None

    def __init__(self, datasource=""):
        self.__datasource = datasource
        self.__object_cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __new__(cls, *args, **kwargs):
        if DAO.__instance is None:
            DAO.__instance = object.__new__(cls)
            return DAO.__instance

    def __dump(self):
        pickle.dump(self.__object_cache, open(self.__datasource, "wb"))

    def __load(self):
        self.__object_cache = pickle.load(open(self.__datasource, "rb"))

    def add(self, key, obj):
        self.__object_cache[key] = obj
        self.__dump()

    def remove(self, key):
        try:
            self.__object_cache.pop(key)
            self.__dump()
        except KeyError:
            pass

    def get(self, key):
        try:
            return self.__object_cache[key]
        except KeyError:
            pass

    def get_all(self):
        return self.__object_cache.values()

