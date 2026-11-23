# Умный калькулятор

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python main.py 5 / 2
python analyze.py
python analyze.py calculator.py
```

В Windows PowerShell окружение активируется командой `.venv\Scripts\Activate.ps1`. Можно также запускать команды напрямую через `.venv\Scripts\python.exe`. Результат расчёта сохраняется в history.txt. Поддерживаются четыре арифметические операции.

В комплекте есть воспроизводимый отчёт статического анализа и конфигурация GitHub Actions. Примените те же правила локально и в CI. Обновляйте версии инструментов после проверки результатов на отдельной ветке. Для спорного предупреждения сначала подтвердите причину и документируйте узкое исключение при необходимости.
