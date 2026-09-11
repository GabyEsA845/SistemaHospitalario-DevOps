# SistemaHospitalario-DevOps

Proyecto de práctica para la actividad "Portafolio DevOps". Simula un sistema
básico de gestión hospitalaria (pacientes, consultas y autenticación) usado
como evidencia de flujo de trabajo con Git, GitHub Flow, y CI/CD con GitHub Actions.

## Estructura
- `src/pacientes.py`: modelo de Paciente
- `src/consultas.py`: modelo de Consulta
- `src/auth.py`: módulo de autenticación (rama feature/login)
- `tests/`: pruebas unitarias con pytest

## Flujo de ramas
- `main`: rama estable
- `develop`: integración de nuevas funcionalidades
- `feature/login`: desarrollo del módulo de login, fusionado a develop vía PR

## Ejecutar pruebas
\`\`\`bash
pip install pytest
pytest
\`\`\`