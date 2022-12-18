from enum import Enum
from typing import List


class ProblemType(Enum):
    MAX = "max"
    MIN = "min"


class LimitConditionType(Enum):
    LS = "ls"
    LE = "le"
    GT = "gt"
    GE = "ge"


class SimplexMethodSolver:

    def __init__(self, target, limit_conditions):
        self.__target = target
        self.__limit_conditions = limit_conditions

    def __to_canonical_form(self):
        pass

    def __build_simplex_table(self):
        pass

    def __evaluate_deltas(self) -> List[float]:
        pass

    def __check_deltas(self, deltas: List[float]) -> bool:
        check = True
        for delta in deltas:
            if delta < 0:
                check = False
        return check

    def __recalculate_simplex_table(self):
        pass

    def __get_answer_from_simplex_table(self):
        pass

    def solve(self):
        self.__to_canonical_form()
        self.__build_simplex_table()
        deltas = self.__evaluate_deltas()
        while not self.__check_deltas(deltas):
            self.__recalculate_simplex_table()
            deltas = self.__evaluate_deltas()
        return self.__get_answer_from_simplex_table()
