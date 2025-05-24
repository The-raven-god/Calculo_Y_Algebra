---

# 🧮 Transformación de Integrales Dobles con Jacobiano

**Autor:** Ing. Santiago Rueda Quintero
**Autor:** Ing. Lisandro Rueda Thomas
**Autor:** Ing. Jimmer Mario Cortez
**Lenguaje:** Python 3
**Interfaz gráfica:** Tkinter
**Propósito:** Visualizar, transformar y analizar integrales dobles usando cambios de variable con cálculo del Jacobiano.

---

## 📋 Descripción

Este software educativo e interactivo permite:

* Introducir una función $f(x, y)$ a integrar.
* Definir límites de integración en $x$ y $y$.
* Especificar un cambio de variables (ej. coordenadas polares).
* Calcular el nuevo integrando aplicando el Jacobiano.
* Visualizar gráficamente la región original de integración.

Está diseñado para estudiantes y docentes que deseen comprender y aplicar el cambio de variables en integrales dobles de forma visual y dinámica.

---

## 📦 Requisitos del Sistema

Antes de ejecutar el programa, asegúrate de tener instalado lo siguiente:

### Lenguaje y Entorno

* Python 3.8 o superior

### Librerías necesarias

Puedes instalar todas las dependencias usando `pip`:

```bash
pip install sympy numpy matplotlib
```

Estas son las principales bibliotecas utilizadas:

| Biblioteca   | Función                   |
| ------------ | ------------------------- |
| `tkinter`    | Interfaz gráfica          |
| `sympy`      | Manipulación simbólica    |
| `numpy`      | Cálculo numérico          |
| `matplotlib` | Visualización de gráficos |

---

## 🚀 Ejecución del Programa

1. Asegúrate de tener el archivo `Software.py` en tu equipo.
2. Abre una terminal o consola en la carpeta donde se encuentra el archivo.
3. Ejecuta el programa con:

```bash
python Software.py
```

Esto abrirá una ventana con la interfaz gráfica del programa.

---

## 🛠️ Uso del Programa

### 1. **Función f(x,y)**

Introduce la función a integrar.
Ejemplos válidos:

* `x**2 + y**2`
* `sqrt(x**2 + y**2)`

### 2. **Límites de integración**

* **x desde**: límite inferior de $x$
* **x hasta**: límite superior de $x$
* **y desde** y **hasta**: pueden depender de $x$ (ej. `sqrt(1 - x**2)`)

### 3. **Cambio de variable**

Especifica el cambio de variable.
Ejemplo para coordenadas polares:

* `x = r*cos(theta)`
* `y = r*sin(theta)`

### 4. **Botones disponibles**

* `Calcular`: Aplica el cambio de variable, calcula el Jacobiano y muestra los resultados.
* `Limpiar`: Limpia los campos y reinicia con valores de ejemplo.
* `Ayuda`: Muestra instrucciones rápidas de uso.

---

## 📊 Resultados

* **Texto**: Se muestra el desarrollo simbólico del cambio de variables, Jacobiano, y nuevo integrando.
* **Gráfico**: Visualiza la región original de integración en coordenadas cartesianas.

---

## 🧪 Ejemplo de Entrada

```text
f(x,y) = x**2 + y**2  
x: desde 0 hasta 1  
y: desde 0 hasta sqrt(1 - x**2)  
Cambio de variable:
x = r*cos(theta)
y = r*sin(theta)
```

Este cambio representa una transformación a coordenadas polares para una región en forma de cuarto de círculo.

---

## 📎 Notas adicionales

* El programa acepta expresiones simbólicas en formato Python (`**`, `sqrt()`, `sin()`, `cos()`).
* No es necesario escribir `math.` o importar funciones manualmente.
* El Jacobiano se calcula automáticamente dependiendo del tipo de variables utilizadas (polares o lineales).

---

## ❓ Problemas Comunes

* **Expresión vacía**: Asegúrate de no dejar campos vacíos.
* **Sintaxis incorrecta**: Usa `**` para potencias, y `*` para multiplicaciones.
* **No se grafica la región**: Revisa los límites, especialmente si dependen de $x$.

---

## 📬 Contacto

Para dudas o sugerencias, puedes contactar a:

**Ing. Santiago**
Email: \[[tu-email@ejemplo.com](mailto:tu-email@ejemplo.com)] *(modificar si es necesario)*

---

