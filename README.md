# OneApp v1.0.0

OneApp es una aplicación que permite convertir videos de YouTube a archivos MP3 de manera fácil y rápida. Este proyecto ha sido desarrollado utilizando Flask para el backend y HTML, CSS y JavaScript para el frontend.

## Tabla de Contenidos

- [Características](#características)
- [Instalación](#instalación)
- [Uso](#uso)
- [Contribuir](#contribuir)
- [Licencia](#licencia)
- [Contacto](#contacto)

## Características

- **Conversión de YouTube a MP3**: Convierte videos de YouTube a archivos MP3 con solo unos pocos clics.
- **Interfaz Amigable**: Diseño sencillo e intuitivo para una fácil navegación.
- **Rápida Conversión**: Procesamiento rápido y eficiente de las conversiones.

## Instalación

Para ejecutar OneApp en tu máquina local, sigue estos pasos:

1. **Clonar el repositorio**:

    ```bash
    git clone https://github.com/tlacaelel666/OneApp.git
    cd OneApp
    ```

2. **Crear un entorno virtual** (opcional pero recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. **Instalar las dependencias**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Configurar las variables de entorno**:

    Crea un archivo `.env` en el directorio raíz del proyecto y añade las siguientes variables:

    ```env
    FLASK_APP=app
    FLASK_ENV=development
    ```

5. **Ejecutar la aplicación**:

    ```bash
    flask run
    ```

6. **Acceder a la aplicación**:

    Abre tu navegador web y visita `http://127.0.0.1:5000`.

## Uso

1. **Convertir un video**:

    - Ingresa la URL del video de YouTube que deseas convertir.
    - Haz clic en el botón "Convertir".
    - Espera a que la conversión se complete y descarga el archivo MP3.

## Contribuir

¡Contribuciones son bienvenidas! Si deseas mejorar OneApp, sigue estos pasos:

1. **Hacer un fork del repositorio**.
2. **Crear una rama nueva** para tu funcionalidad (`git checkout -b feature/nueva-funcionalidad`).
3. **Realizar los cambios necesarios** y confirmar los cambios (`git commit -m 'Agregar nueva funcionalidad'`).
4. **Enviar los cambios a tu repositorio fork** (`git push origin feature/nueva-funcionalidad`).
5. **Crear una Pull Request** en el repositorio original.

## Licencia

Este proyecto está bajo la Licencia MIT. Puedes ver el archivo [LICENSE](LICENSE) para más detalles.

## Contacto

Para cualquier consulta o sugerencia, puedes contactar a:

- **Nombre**: Jacobo Mina
- **Email**: [jakocrazykings@gmail.comj
