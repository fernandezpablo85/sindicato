[![License: WTFPL](https://img.shields.io/badge/License-WTFPL-brightgreen.svg)](http://www.wtfpl.net/about/)

# El Sindicato Del Software - V1.0.0

Software, economía, política y bardo salteño.

[Stream on Twitch](https://www.twitch.tv/elsindicatodelsoftware)

# Run Length Encoding

## Definición

Run Length Encoding es una forma simple de compresión de datos lossless, o sea, que no piede información (es posible reconstruir los datos originales desde la versión comprimida). Para más información ver [RLE en wikipedia](https://en.wikipedia.org/wiki/Run-length_encoding).

### Ejercicios Simples

- Implementar la funcion `rle` en el archivo `main.ts`.
- Los tests deberían correr y pasar: `npm test`.
- La solución óptima es O(n)
- Opcional: se te ocurre una solución menos eficiente pero más legible?

### Property Based Testing

- Este proyecto incluye un property-based test usando el framework `fast-check`, agregar adicionales que ejerciten la función `rle`.
