"""Запустить сканирование проекта из активного виртуального окружения."""

import argparse
import subprocess  # nosec B404 - запускаются фиксированные модули анализаторов
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MODULES = ["calculator.py", "operations.py", "main.py"]
TOOLS = {
    "flake8": (),
    "pylint": ("--score=no",),
    "bandit": ("-q",),
    "mypy": (),
    "black": ("--check", "--line-length=100"),
}


def main() -> int:
    """Вернуть ненулевой код, если хотя бы одна проверка завершилась ошибкой."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", metavar="FILE")
    options = parser.parse_args()
    allowed = [*MODULES, "analyze.py"]
    files = options.files or allowed
    if any(file not in allowed for file in files):
        parser.error("Укажите имя одного из модулей проекта.")
    return_codes = []
    for module, arguments in TOOLS.items():
        print(f"=== {module} ===", flush=True)
        command = [sys.executable, "-m", module, *arguments, *files]
        # Исполняемый файл и модули заданы программой, имена файлов проверены выше.
        result = subprocess.run(command, cwd=ROOT, check=False)  # nosec B603
        return_codes.append(result.returncode)
    return int(any(return_codes))


if __name__ == "__main__":
    raise SystemExit(main())
