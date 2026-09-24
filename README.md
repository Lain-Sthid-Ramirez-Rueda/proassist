# ⚡ ProAssist — Personal Productivity Assistant

Chatbot web bilingüe (español/inglés) de productividad personal impulsado por IA.
Gratis, seguro y optimizado con alto rendimiento.

## 🚀 Demo en vivo

- [ProAssist en Render](https://proassist-r1q6.onrender.com)
- Integrado directamente en el portafolio: [lainramirez.vercel.app](https://lainramirez.vercel.app)

> ⚠️ El servicio usa el plan gratuito de Render.
> Si lleva un rato inactivo, la primera carga puede tardar ~30-50 segundos mientras se reactiva el contenedor.

## 🛠 Stack Tecnológico

- **Backend:** Python 3.11 · Flask · Gunicorn (multihilo con locks thread-safe)
- **IA:** Groq API (`qwen/qwen3.8-27b`) con latencia ultra baja
- **Frontend:** HTML5 · CSS3 (Material & Syne font) · Marked.js · DOMPurify
- **Despliegue & Contenedores:** Docker · Render

## ✨ Funcionalidades y Mejoras de Calidad

- **Bilingüe inteligente:** Conversación natural en español e inglés según el idioma del usuario.
- **Aislamiento de sesiones:** Sesiones independientes por usuario (`sessionId`) en memoria con expiración automática (TTL).
- **Formato Markdown enriquecido:** Renderizado automático de negritas, encabezados estilizados, viñetas y bloques de código con botón de copiado rápido.
- **Copiar respuestas:** Botón para copiar al portapapeles cualquier mensaje o bloque de código con un solo clic.
- **Seguridad robusta:**
  - Rate limiting (límite anti-abuso de peticiones por IP).
  - Sanitización anti-XSS con DOMPurify.
  - Cabeceras HTTP de seguridad y Content Security Policy (`frame-ancestors` restrictivo).
  - Protección de prompts e instrucciones contra inyecciones adversarias.
- **Monitoreo & Keep-Alive:** Endpoint `/health` para chequeos de salud y servicios de uptime.

## ⚙️ Variables de Entorno

| Variable | Descripción | Valor por defecto |
|---|---|---|
| `GROQ_API_KEY` | Clave de API de Groq | *(Requerida)* |
| `GROQ_MODEL` | Identificador del modelo de Groq | `qwen/qwen3.8-27b` |
| `MAX_TOKENS` | Límite de tokens de salida | `700` |
| `PORT` | Puerto de escucha del servidor | `8080` |

## 👤 Autor

**Lain Sthid Ramírez Rueda**  
Analista y Desarrollador de Software · SENA  
[LinkedIn](https://linkedin.com/in/lain-sthid-ramirez-rueda) · [GitHub](https://github.com/Lain-ramirez18) · lainramirez18@gmail.com
