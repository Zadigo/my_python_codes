from collections import deque
import math

heights = [195, 182, 185]


class Height:
    def __init__(self, iterable, func=None):
        self._heights = iterable

        if func:
            if callable(func):
                for i in range(0, len(self._heights)):
                    result = func(self._heights[i])
                    self._heights[i] =  result or self._heights[i]

    def __iter__(self):
        yield self._iter(self._heights)
    
    def __add__(self, value):
        for height in self._heights:
            yield height + value

    def __sub__(self, value):
        for height in self._heights:
            yield height - value

    def __str__(self):
        return '%s' % self._heights

    def _append(self, value):
        self._heights.append(value)
        return self

    def _average(self):
        total = 0
        for value in self._heights:
            total += value
        avg = total / len(self._heights)
        return [round(avg, 1)]

    def _min(self):
        return [min(self._heights)]

    def _max(self):
        return [max(self._heights)]

    @staticmethod
    def _iter(values):
        for value in values:
            return value

    @property
    def _convert(self):
        for v in self._heights:
            yield round(v / 30.48, 1)
