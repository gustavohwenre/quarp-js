from abc import ABC, abstractmethod

class BaseModel(ABC):
    @abstractmethod
    def salvar(self):
        pass
