"""Базовые арифметические операции."""


def add(a: float, b: float) -> float:
    """Сложить два числа."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Вычесть второе число из первого."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Перемножить два числа."""
    return a * b


def divide(a: float, b: float) -> float:
    """Разделить первое число на второе."""
    if b == 0:
        raise ZeroDivisionError("Деление на ноль.")
    return a / b
