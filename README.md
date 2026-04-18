# 🎯 Proyecto Demo: Test Impact Analysis (TIA)

**Propósito:** Demostración educativa de Test Impact Analysis para Diplomado QA + IA

Este proyecto simula una aplicación Python con suite de tests completa, mostrando la diferencia entre ejecutar TODOS los tests vs solo tests AFECTADOS por cambios (TIA).

---

## 📁 Estructura del Proyecto

```
ejemplo-tia-demo/
├── src/
│   ├── payment.py          # Módulo pagos (15 tests)
│   ├── auth.py             # Módulo autenticación (120 tests)
│   ├── cart.py             # Módulo carrito (85 tests)
│   └── search.py           # Módulo búsqueda (200 tests)
├── tests/
│   ├── test_payment.py     # Tests módulo payment
│   ├── test_auth.py        # Tests módulo auth
│   ├── test_cart.py        # Tests módulo cart
│   └── test_search.py      # Tests módulo search
├── .github/
│   └── workflows/
│       ├── ci-full.yml     # GitHub Actions SIN TIA (todos los tests)
│       └── ci-tia.yml      # GitHub Actions CON TIA (solo afectados)
├── requirements.txt
└── README.md
```

**Total:** 420 tests

---

## 🚀 Cómo Funciona la Demo

### **Workflow 1: SIN TIA (ci-full.yml)**

Ejecuta TODOS los tests sin importar qué archivo cambió.

**Resultado típico:**
- Tests ejecutados: 420
- Tiempo: ~12 minutos
- Costo CI/CD: ~$2.40

### **Workflow 2: CON TIA (ci-tia.yml)**

Detecta qué archivo cambió y ejecuta SOLO tests relevantes.

**Ejemplo:** Si cambias `payment.py`:
- Tests ejecutados: 15 (solo `test_payment.py`)
- Tiempo: ~45 segundos
- Costo CI/CD: ~$0.15
- **Ahorro: 93.75%**

---

## 📊 Comparación Visual

| Métrica | SIN TIA | CON TIA | Ahorro |
|---------|---------|---------|--------|
| Tests ejecutados | 420 | 15 | 96.4% |
| Tiempo | 12 min | 45 seg | 93.75% |
| Costo | $2.40 | $0.15 | 93.75% |
| Feedback | 12 min | <1 min | Inmediato |

---

## 🎓 Uso en Clase

### **Durante la Sesión:**

1. **Mostrar repositorio** en GitHub
2. **Ir a Actions tab**
3. **Mostrar ejecución `ci-full.yml`**: 420 tests, 12 min
4. **Mostrar ejecución `ci-tia.yml`**: 15 tests, 45 seg
5. **Comparar resultados** lado a lado

### **Explicar Concepto:**

- Sin TIA: "Cambio 1 archivo → ejecuta TODO"
- Con TIA: "ML detecta cambio → ejecuta SOLO lo relevante"

---

## 💻 Instalación y Ejecución Local

### **Requisitos:**
- Python 3.8+
- pytest

### **Setup:**

```bash
# Clonar repositorio
git clone https://github.com/TU_USUARIO/ejemplo-tia-demo.git
cd ejemplo-tia-demo

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar TODOS los tests
pytest

# Ejecutar solo tests de payment
pytest tests/test_payment.py

# Ejecutar con reporte de cobertura
pytest --cov=src --cov-report=html
```

---

## 🔧 Cómo Funciona TIA Simulado

El workflow `ci-tia.yml` usa lógica simple para simular TIA:

```yaml
- name: Detectar archivos cambiados
  run: |
    CHANGED=$(git diff --name-only HEAD~1)
    
    if [[ $CHANGED == *"payment"* ]]; then
      echo "Cambio en payment → ejecutar test_payment"
      pytest tests/test_payment.py
    elif [[ $CHANGED == *"auth"* ]]; then
      echo "Cambio en auth → ejecutar test_auth"
      pytest tests/test_auth.py
    # ... etc
    fi
```

**Nota:** TIA REAL (Launchable) usa Machine Learning avanzado, no condicionales simples.

---

## 📈 Escalando a Proyecto Real

En proyecto REAL con Launchable:

```bash
# Instalar Launchable CLI
pip install launchable

# Configurar
launchable verify
launchable record build --name $BUILD_ID

# Ejecutar con TIA
launchable subset --target 10% pytest | pytest --file-list -

# Reportar resultados
launchable record tests --build $BUILD_ID pytest .
```

---

## 🎯 Para Estudiantes

### **Ejercicio Propuesto:**

1. Fork este repositorio
2. Modifica `src/payment.py` (cambia una línea)
3. Observa cuántos tests ejecuta `ci-full.yml` vs `ci-tia.yml`
4. Calcula el ahorro de tiempo y costo

### **Preguntas Reflexión:**

- ¿Por qué TIA ahorra tanto tiempo?
- ¿Qué riesgos tiene omitir tests?
- ¿En qué proyectos usarías TIA?

---

## 📚 Recursos Adicionales

- **Launchable Docs:** https://www.launchableinc.com/docs
- **TIA Explicado:** https://martinfowler.com/articles/test-impact-analysis.html
- **Spotify Case Study:** https://engineering.atspotify.com/2018/12/test-impact-analysis/

---

## 🤝 Contribuciones

Este es un proyecto educativo. Pull requests bienvenidos para:
- Mejorar tests
- Agregar más módulos
- Optimizar workflows

---

## 📝 Licencia

MIT License - Libre uso educativo

---

**Creado para:** Diplomado QA + IA - Javeriana Cali  
**Instructor:** Jorge Fonseca  
**Fecha:** Abril 2026

