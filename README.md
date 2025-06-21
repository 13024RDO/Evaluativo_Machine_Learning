
# Predicción de Ventas Semanales de un Emprendimiento de Repostería

Este proyecto aplica técnicas de Machine Learning para predecir cuántas unidades de productos de repostería se venderán semanalmente en base a distintas condiciones como el sabor, el clima, promociones y la actividad en redes sociales.

## Objetivo

Desarrollar una aplicación completa que integre:
- Un modelo de regresión entrenado con al menos 500 registros.
- Un servidor Flask que exponga el modelo mediante una API REST.
- Una interfaz para enviar datos y visualizar predicciones.

---

##  Estructura del Proyecto

```
modelo-regresion-lineal/
│
├── demanda_reposteria.csv       # Dataset propio generado artificialmente
├── modelo_reposteria.pkl        # Modelo entrenado guardado con joblib
├── app.py                       # API desarrollada con Flask
├── entrenamiento.ipynb          # Notebook con el código de entrenamiento
└── README.md                    # Este archivo
```

---

## Modelo de Machine Learning

- **Tipo**: Regresión Lineal
- **Librería**: Scikit-Learn
- **Dataset**: 500 registros simulados
- **Variables usadas**:
  - `semana`: número de semana del año
  - `sabor_producto`: chocolate, vainilla, frutilla, limón, dulce de leche
  - `clima`: soleado, nublado, lluvioso
  - `feriado`: sí / no
  - `promocion`: sí / no
  - `redes_sociales`: sí / no
  - `unidades_vendidas`: (variable objetivo)

---

## Cómo ejecutar el proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/13024RDO/Evaluativo_Machine_Learning.git
cd modelo-regresion-lineal
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

>  Si no tenés el archivo, usá:
```bash
pip install pandas scikit-learn flask joblib
```

### 3. Ejecutar el servidor

```bash
python app.py
```

El servidor estará disponible en:  
`http://127.0.0.1:5000`

---

##  Endpoints disponibles

### `POST /predict`
Predice la cantidad de unidades a vender.

#### Ejemplo JSON de entrada:
```json
{
  "semana": 20,
  "sabor_producto": "vainilla",
  "clima": "soleado",
  "feriado": "no",
  "promocion": "sí",
  "redes_sociales": "sí"
}
```

#### Respuesta esperada:
```json
{
  "prediccion_unidades_vendidas": 34
}
```

---

### `GET /metrics`
Devuelve métricas del modelo.

```json
{
  "modelo": "Regresión Lineal",
  "r2_score": 0.86,
  "rmse": 4.2
}
```

---

## Trabajo práctico evaluativo

Este proyecto cumple con todos los criterios:
- Dataset propio y original
- Más de 500 registros
- Modelo funcional y evaluado
- API implementada con Flask
- Predicciones desde cliente (puede integrarse una interfaz visual)
- Buenas prácticas de estructura y código

---


## Autor

Leonardo Gomez  
Ezequiel Fleitas
Trabajo práctico para la materia *Machine Learning*
