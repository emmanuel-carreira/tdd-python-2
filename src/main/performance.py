from enum import Enum

class Performance(Enum):
    BELOW_EXPECTATIONS = 1
    GOOD = 2
    GREAT = 3

    @staticmethod
    def get_readjustment_percentage(performance: int) -> float:
        performance_strategy = {
            Performance.BELOW_EXPECTATIONS: 0.03,
            Performance.GOOD: 0.15,
            Performance.GREAT: 0.2
        }
        return performance_strategy.get(performance, 0)
