# Code-Generation-Refactoring

Este repositorio contiene varios scripts de Python para propósitos educativos y de demostración.

## Estructura del proyecto

- [`calculator.py`](calculator.py): Calculadora básica con operaciones aritméticas.
- [`calculator_test.py`](calculator_test.py): Pruebas unitarias para la calculadora.
- [`sum_elements.py`](sum_elements.py): Suma una lista de números introducidos por el usuario.
- [`card_draw.py`](card_draw.py): Simula el sorteo de cartas de una baraja (contiene errores intencionales).
- [`hello.py`](hello.py): Imprime "Hola Mundo".
- [`weather_script.py`](weather_script.py): Consulta el clima de una ciudad usando la API de OpenWeatherMap.

## Requisitos

- Python 3.x
- [`requests`](https://pypi.org/project/requests/) para `weather_script.py`
- [`pytest`](https://pytest.org/) para ejecutar pruebas (opcional)

## Uso

### Calculadora

```sh
python calculator.py
```

### Suma de elementos

```sh
python sum_elements.py
```

### Consulta de clima

1. Obtén una API key de [OpenWeatherMap](https://openweathermap.org/api).
2. Reemplaza `"YOUR_API_KEY"` en [`weather_script.py`](weather_script.py) por tu clave.
3. Ejecuta:

```sh
python weather_script.py
```

### Pruebas

```sh
pytest calculator_test.py
```

## Notas

- El archivo [`card_draw.py`](card_draw.py) contiene errores intencionales para fines de práctica.
- Configuración de pruebas en [`.vscode/settings.json`](.vscode/settings.json).
