"""Командная строка умного калькулятора."""

import argparse
from pathlib import Path

from calculator import Calculator


def main() -> int:
    """Обработать аргументы, выполнить расчёт и сохранить историю."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("a", type=float)
    parser.add_argument("operation", choices=["+", "-", "*", "/"])
    parser.add_argument("b", type=float)
    args = parser.parse_args()

    calculator = Calculator()
    history_file = Path("history.txt")
    try:
        calculator.load_history(history_file)
        result = calculator.calculate(args.a, args.b, args.operation)
        calculator.save_history(history_file)
    except (OSError, ValueError, ZeroDivisionError) as error:
        parser.exit(1, f"{error}\n")
    print(f"Результат: {result:g}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
