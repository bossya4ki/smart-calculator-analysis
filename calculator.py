"""Калькулятор с сохранением истории в UTF-8."""

from pathlib import Path

from operations import add, divide, multiply, subtract

OPERATIONS = {"+": add, "-": subtract, "*": multiply, "/": divide}


class Calculator:
    """Выполняет разрешённую операцию и запоминает результат."""

    def __init__(self) -> None:
        self.history: list[str] = []

    def calculate(self, a: float, b: float, operation: str) -> float:
        """Вычислить результат и добавить его в историю."""
        function = OPERATIONS.get(operation)
        if function is None:
            raise ValueError("Неизвестная операция.")
        result = function(a, b)
        self.history.append(f"{a:g} {operation} {b:g} = {result:g}")
        return result

    def clear_history(self) -> None:
        """Очистить историю текущего сеанса."""
        self.history.clear()

    def save_history(self, filename: Path) -> None:
        """Записать текущую историю в UTF-8."""
        with filename.open("w", encoding="utf-8") as stream:
            stream.writelines(f"{entry}\n" for entry in self.history)

    def load_history(self, filename: Path) -> None:
        """Восстановить историю, если файл сохранён ранее."""
        try:
            contents = filename.read_text(encoding="utf-8")
        except FileNotFoundError:
            return
        self.history = contents.splitlines()
