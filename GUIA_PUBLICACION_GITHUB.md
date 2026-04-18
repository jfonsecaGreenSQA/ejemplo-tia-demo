# 📚 GUÍA COMPLETA: Publicar Proyecto TIA Demo en GitHub

Esta guía te llevará paso a paso para publicar el proyecto `ejemplo-tia-demo` en tu cuenta de GitHub y usarlo en la clase.

---

## 📋 PASOS RÁPIDOS (Resumen)

1. Crear repositorio en GitHub
2. Subir código
3. Ejecutar workflows
4. Usar en demo clase

**Tiempo total:** 10-15 minutos

---

## 🚀 PASO 1: Crear Repositorio en GitHub

### **Opción A: Desde GitHub Web (Recomendado)**

1. **Ir a GitHub:** https://github.com
2. **Login** con tu cuenta
3. **Click** en botón verde "New" (o ícono +)
4. **Completar:**
   - Repository name: `ejemplo-tia-demo`
   - Description: `Demo educativa Test Impact Analysis para Diplomado QA+IA`
   - Visibility: **Public** (para que estudiantes puedan verlo)
   - ✅ Initialize with README: **NO marcar** (ya lo tenemos)
   - Click **"Create repository"**

5. **Copiar URL:** Verás algo como:
   ```
   https://github.com/TU_USUARIO/ejemplo-tia-demo.git
   ```

---

## 📦 PASO 2: Subir Código al Repositorio

### **Desde tu computadora local:**

Abre terminal (PowerShell/CMD/Git Bash) y ejecuta:

```bash
# 1. Navegar a donde descargaste el proyecto
cd ruta/donde/descargaste/ejemplo-tia-demo

# 2. Inicializar Git (si no está inicializado)
git init

# 3. Agregar todos los archivos
git add .

# 4. Hacer commit inicial
git commit -m "Initial commit: TIA demo completo"

# 5. Conectar con tu repositorio GitHub
git remote add origin https://github.com/TU_USUARIO/ejemplo-tia-demo.git

# 6. Subir código
git branch -M main
git push -u origin main
```

**IMPORTANTE:** Reemplaza `TU_USUARIO` con tu usuario de GitHub.

---

## ✅ PASO 3: Verificar Subida Exitosa

1. **Ir a:** `https://github.com/TU_USUARIO/ejemplo-tia-demo`
2. **Deberías ver:**
   - ✅ README.md con descripción completa
   - ✅ Carpeta `src/` con 4 archivos Python
   - ✅ Carpeta `tests/` con 4 archivos de tests
   - ✅ Carpeta `.github/workflows/` con 2 workflows

---

## ⚙️ PASO 4: Ejecutar Workflows (Para Demo)

### **4.1 Activar GitHub Actions**

1. Ve a tu repositorio en GitHub
2. Click tab **"Actions"**
3. Si aparece mensaje "Enable Actions", click en **"I understand my workflows, go ahead and enable them"**

### **4.2 Ejecutar Workflow SIN TIA**

1. En tab Actions, click workflow **"CI Full (Sin TIA)"**
2. Click botón **"Run workflow"** (derecha)
3. Select branch: **main**
4. Click **"Run workflow"** verde
5. Espera ~1 minuto - verás ejecución en progreso
6. Click en la ejecución para ver detalles
7. **CAPTURA DE PANTALLA** para mostrar en clase

**Resultado esperado:**
```
✅ 30 tests ejecutados
⏱️  Tiempo: ~1-2 minutos
```

### **4.3 Ejecutar Workflow CON TIA**

1. **PRIMERO:** Haz un pequeño cambio en código
   - Edita `src/payment.py` en GitHub (botón lápiz)
   - Cambia línea 10: agrega un comentario `# Versión 1.1`
   - Commit changes

2. En tab Actions, ve workflow **"CI con TIA (Simulado)"**
3. Verás que se ejecutó automáticamente
4. Click para ver detalles
5. **CAPTURA DE PANTALLA**

**Resultado esperado:**
```
✓ Detectado cambio en payment.py
→ Ejecutar solo test_payment.py (15 tests)
✅ 15 tests ejecutados
⏱️  Tiempo: ~30 segundos
📊 AHORRO: 50% vs todos los tests
```

---

## 🎓 PASO 5: Usar en la Clase (Demo en Vivo)

### **Preparación Antes de Clase:**

1. **Tener repositorio listo** con ambos workflows ejecutados
2. **Tener capturas de pantalla** de ambas ejecuciones
3. **Marcar como favorito** el repositorio en navegador

### **Durante la Clase:**

**SLIDE 9: Demo GitHub Actions**

```
[Compartir pantalla navegador]

1. Ir a: github.com/TU_USUARIO/ejemplo-tia-demo

2. Explicar estructura:
   "Tenemos 4 módulos Python: payment, auth, cart, search"
   "Cada uno con sus tests"

3. Click tab "Actions"

4. Mostrar "CI Full (Sin TIA)":
   - Click en última ejecución
   - Señalar: "30 tests ejecutados"
   - Señalar tiempo: "~1-2 minutos"

5. Explicar:
   "Este workflow ejecuta TODOS los tests"
   "No importa qué archivo cambié"
   "Como proyecto grande: 12 minutos, 420 tests"

6. Volver a Actions

7. Mostrar "CI con TIA":
   - Click en última ejecución
   - Señalar: "✓ Detectado cambio en payment.py"
   - Señalar: "Solo 15 tests ejecutados"
   - Señalar tiempo: "~30 segundos"

8. Explicar:
   "TIA detectó que solo cambié payment.py"
   "Ejecutó SOLO tests de payment"
   "50% de reducción en este caso"
   "En proyecto real: 99.6% reducción"

9. Comparar lado a lado (abrir ambas tabs)

10. Conclusión:
    "Esta es la magia de Test Impact Analysis"
```

---

## 📊 COMPARACIÓN PARA MOSTRAR EN CLASE

Prepara esta tabla en Excel/slide:

| Métrica | SIN TIA | CON TIA | Ahorro |
|---------|---------|---------|--------|
| Tests ejecutados | 30 | 15 | 50% |
| Tiempo | 1-2 min | 30 seg | 50-75% |
| En proyecto REAL (420 tests) | 12 min | 45 seg | 93.75% |
| Costo CI/CD | $2.40 | $0.15 | $2.25 |

---

## 🔧 TROUBLESHOOTING

### **Problema: Workflows no aparecen en Actions**

**Solución:**
```bash
# Verificar que carpeta .github existe
ls -la .github/workflows/

# Si no existe, crearla:
mkdir -p .github/workflows
# Copiar archivos ci-full.yml y ci-tia.yml

# Hacer commit y push:
git add .github/
git commit -m "Add workflows"
git push
```

### **Problema: Tests fallan**

**Solución:**
```bash
# Ejecutar tests localmente primero:
cd ejemplo-tia-demo
pip install pytest
pytest tests/ -v

# Si fallan, revisar imports en tests
```

### **Problema: TIA no detecta cambios**

**Solución:**
- Workflow TIA requiere al menos 2 commits en rama
- Primera ejecución siempre ejecuta todos los tests
- A partir de segunda ejecución detecta cambios

---

## 🎯 EJERCICIO PARA ESTUDIANTES

**Después de la demo, proponer:**

```
EJERCICIO OPCIONAL:

1. Fork el repositorio ejemplo-tia-demo
2. Modifica src/cart.py (cambia cualquier línea)
3. Haz commit y push
4. Ve a Actions y observa:
   - ¿Qué workflow se ejecutó?
   - ¿Cuántos tests corrió?
   - ¿Detectó que solo cart.py cambió?

5. Comparte captura en Slack
```

---

## 📝 CHECKLIST PRE-CLASE

**24 horas antes:**

- [ ] Repositorio publicado en GitHub
- [ ] Workflow "CI Full" ejecutado exitosamente
- [ ] Workflow "CI TIA" ejecutado exitosamente
- [ ] Capturas de pantalla guardadas
- [ ] URL repositorio marcada como favorita
- [ ] Tabla comparativa en slide

**1 hora antes:**

- [ ] Abrir repositorio en navegador
- [ ] Abrir tab Actions
- [ ] Verificar workflows recientes están verdes ✅
- [ ] Tener Excel comparativa lista

---

## 💡 TIPS PARA LA DEMO

1. **Preparar pestañas navegador:**
   - Tab 1: Repositorio main
   - Tab 2: Workflow SIN TIA
   - Tab 3: Workflow CON TIA
   - Tab 4: Excel comparativa

2. **Si internet falla:**
   - Tener capturas de pantalla backup
   - Mostrar capturas en vez de live

3. **Explicar concepto, no código:**
   - No entrar en detalles YAML
   - Enfocarse en RESULTADOS
   - Mostrar números grandes: 30→15, 2min→30seg

4. **Responder preguntas comunes:**
   - "¿Funciona con cualquier lenguaje?" → Sí
   - "¿Necesito Launchable?" → No obligatorio, hay alternativas
   - "¿Qué tan difícil es implementar?" → Setup inicial 2-4 semanas

---

## 🔗 RECURSOS ADICIONALES

**Para ti (instructor):**
- Documentación Launchable: https://www.launchableinc.com/docs
- GitHub Actions docs: https://docs.github.com/actions

**Para compartir con estudiantes:**
- Link repositorio: `https://github.com/TU_USUARIO/ejemplo-tia-demo`
- README del proyecto (ya explica todo)

---

## ✅ RESUMEN EJECUTIVO

**LO QUE NECESITAS HACER:**

1. ✅ Crear repo en GitHub (2 min)
2. ✅ Subir código (3 min)
3. ✅ Ejecutar workflows (5 min)
4. ✅ Tomar capturas (2 min)
5. ✅ Marcar favorito (1 min)

**TOTAL: ~15 minutos de preparación**

**EN CLASE:**
- Compartir pantalla GitHub
- Mostrar Actions
- Comparar workflows
- Explicar ahorro 93.75%

**RESULTADO:**
- Demo visual impactante
- Concepto TIA claro
- Estudiantes motivados

---

**¿Dudas o problemas?**

Contacto: jorge.fonseca@javerianacali.edu.co

---

**Creado para:** Diplomado QA + IA - Sesión 3  
**Fecha:** Abril 2026  
**Versión:** 1.0

