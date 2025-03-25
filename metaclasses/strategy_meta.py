"""Регистрация подклассов — расширяемый шаблон стратегии"""

import abc
import inspect
from typing import Dict


class StrategyMeta(abc.ABCMeta):
    """Храним отображение внешне используемых имен в классы."""
    registry: Dict[str, 'Strategy'] = {}

    def __new__(cls, name, bases, namespace):
        new_cls = super().__new__(cls, name, bases, namespace)

        if not inspect.isabstract(new_cls):
            cls.registry[new_cls.name] = new_cls

        return new_cls


class Strategy(metaclass=StrategyMeta):
    @property
    @abc.abstractmethod
    def name(self):
        pass

    @abc.abstractmethod
    def validate_credentials(self, login: str, password: str) -> bool:
        pass

    @classmethod
    def for_name(cls, name: str) -> 'Strategy':
        """Используем реестр для создания новых классов"""
        return StrategyMeta.registry[name]()


class AlwaysOk(Strategy):
    name = 'always_ok'

    def validate_credentials(self, login: str, password: str) -> bool:
        return True


Strategy.for_name('always_ok').validate_credentials('john', 'x')
