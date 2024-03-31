from abc import ABC, abstractmethod


class AbstractRepository(ABC):

    @abstractmethod
    def show_all_table(self):
        raise NotImplementedError

    @abstractmethod
    def found_one_or_none(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def insert_data(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def update_data(self):
        raise NotImplementedError

    @abstractmethod
    def delete_data(self, **kwargs):
        raise NotImplementedError
