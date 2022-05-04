# Rounding

## Motivación

Un ejercicio para entender por qué algunas veces las formas ordinarias de desarrollo y testing con ejemplos no son las herramientas adecuadas para resolver un problema.

## Introducción

Supongamos que tenemos un sistema que invierte la plata de sus usuarios en diferentes portafolios. Los portafolios tienen diferentes activos con un % de cada uno, por ejemplo, podemos tener un portafolio que es 50% acciones de YPF y 50% bitcoin.

El objeto portafolio contiene el activo como clave y el valor total del activo como valor en un diccionario:

```python
    {
        "YPF": 500,
        "BTC": 500,
    }
```

## Problema

Queremos mostrar a nuestros usuarios el % de cada activo en su portafolio. Para eso tenemos que transformar nuestro diccionario de valores en un diccionario de porcentajes:

```python
    {
        "YPF": "50%",
        "BTC": "50%",
    }
```

La dificultad del ejercicio (o lo interesante) radica en mostrar estos datos para valores arbitrarios y garantizar que:

1. Los porcentajes siempre van a sumar 100%
2. Ningún porcentaje es 0%
3. Deberíamos validar de alguna forma que (1) y (2) se cumplen siempre, tratando de cubrir tantos edge cases como sea posible
