import os
from flask import Flask, render_template

app = Flask(__name__)

# Configuración con descripciones técnicas detalladas y rústicas
CONFIG = {
    'empresa': "MARCELO CAMARGO",
    'whatsapp': "59896424201", 
    'tagline': "CALIDAD QUE SE CONSTRUYE CON TÉCNICA",
    'meta_desc': "Especialista en revestimientos de alta gama, reformas integrales y terminaciones técnicas en Uruguay.",
    'servicios': [
        {
            'id': 'lavamanos',
            'titulo': 'LAVAMANOS',
            'sub': 'DISEÑO Y FUNCIONALIDAD',
            'img_principal': '/static/piletacasa.jpeg.jpeg',
            'fotos': [
                {'src': '/static/piletacasa.jpeg.jpeg', 't': 'Bacha de Apoyo Artesanal', 'd': 'Instalación técnica sobre mesada de madera maciza tratada con protector náutico. Se realizó un sellado perimetral con polímero elástico de alta resistencia para absorber las micro-vibraciones del mueble y anular cualquier filtración de humedad hacia el núcleo de la madera.'},
                {'src': '/static/pileta_espejo.jpeg.jpeg', 't': 'Iluminación y Espejos', 'd': 'Montaje de cristales de gran formato con sistemas de iluminación LED embutidos. El trabajo incluyó el fresado de la superficie para ocultar cableados y asegurar que el espejo quede perfectamente al ras, logrando un baño con profundidad y luz técnica.'},
                {'src': '/static/pileta2.jpeg.jpeg', 't': 'Grifería de Alta Gama', 'd': 'Colocación de monocomandos de diseño con ajuste de presión en base. Trabajamos la conexión hidráulica interna con selladores de rosca técnicos para garantizar cero goteo y un flujo de agua silencioso, cuidando la estética del metal cromado durante el apriete.'}
            ]
        },
        {
            'id': 'ducheros',
            'titulo': 'DUCHEROS',
            'sub': 'CONFORT E HIDRÁULICA',
            'img_principal': '/static/ducha1.jpeg.jpeg',
            'fotos': [
                {'src': '/static/ducha1.jpeg.jpeg', 't': 'Revestimiento con Junta Mínima', 'd': 'Colocación de cerámicas tipo Metro mediante replanteo previo para asegurar cortes simétricos en todas las esquinas. Utilizamos separadores de precisión de 1mm y pegamento impermeable reforzado, logrando una pared hermética y visualmente impecable.'},
                {'src': '/static/ducha2.jpeg.jpeg', 't': 'Ingeniería de Drenaje', 'd': 'Construcción de piso de ducha con pendiente técnica del 2% hacia la rejilla sifónica. Se aplicó una membrana cementicia impermeabilizante bajo el revestimiento para anular cualquier riesgo de filtración hacia los ambientes linderos o plantas inferiores.'}
            ]
        },
        {
            'id': 'piscinas',
            'titulo': 'PISCINAS',
            'sub': 'ESTRUCTURAS DE HORMIGÓN',
            'img_principal': '/static/piscina_obra_1.jpeg.jpeg',
            'fotos': [
                {'src': '/static/piscina_obra_1.jpeg.jpeg', 't': 'Construcción de Vaso', 'd': 'Ejecución de estructura reforzada con doble malla de hierro y un proceso de vibrado del hormigón para eliminar burbujas de aire y garantizar una cubeta 100% estanca y resistente a la presión hídrica.'},
                {'src': '/static/piscina_obra_2.jpeg.jpeg', 't': 'Finalización', 'd': 'Detalle de terminación en bordes y preparación de superficie para revestimientos técnicos de exterior.'}
            ]
        },
        {
            'id': 'banos_general',
            'titulo': 'BAÑOS EN GENERAL',
            'sub': 'REMODELACIÓN INTEGRAL',
            'img_principal': '/static/terminaciones1.jpeg.jpeg',
            'fotos': [
                {'src': '/static/terminaciones1.jpeg.jpeg', 't': 'Nivelación y Plomos', 'd': 'Preparación de muros mediante revoque hidrófugo y nivelación láser. Corregimos los falsos escuadres de la obra bruta para que las piezas de gran formato apoyen plano, evitando el "cejeo" entre placas y garantizando una superficie totalmente lisa.'},
                {'src': '/static/banocasa.jpeg.jpeg', 't': 'Sanitarios y Descargas', 'd': 'Instalación de loza sanitaria con fijaciones mecánicas ocultas. Se recalibraron las entradas de agua y las descargas de 110mm para asegurar un funcionamiento eficiente, sin ruidos molestos y con un sellado de base que previene olores y fugas.'},
                {'src': '/static/terminaciones2.jpeg.jpeg', 't': 'Cortes en Inglete (45°)', 'd': 'Ejecución de terminaciones premium mediante cortes a 45 grados en los encuentros de muros. Esta técnica manual elimina la necesidad de usar perfiles de terminación, dejando que el propio material sea el protagonista en cada esquina de la reforma.'}
            ]
        },
        {
            'id': 'parrillas',
            'titulo': 'PARRILLAS Y QUINCHOS',
            'sub': 'ALBAÑILERÍA TRADICIONAL',
            'img_principal': '/static/parrilla_obra.jpeg.jpeg',
            'fotos': [
                {'src': '/static/parrilla_obra.jpeg.jpeg', 't': 'Ladrillo Visto con Junta Rasada', 'd': 'Levantamiento de muros de ladrillo seleccionados, cuidando la horizontalidad de cada hilada. Se utilizó una mezcla con la proporción justa de cal para permitir la dilatación térmica de la estructura sin que aparezcan fisuras con el paso del tiempo.'},
                {'src': '/static/parrilla_Hormigon.jpeg.jpeg', 't': 'Vigas Reforzadas', 'd': 'Cálculo y ejecución de la estructura de apoyo para la campana de humos. Reforzamos los puntos críticos de carga para soportar el peso de la mampostería aérea, asegurando la estabilidad total de la construcción frente a vibraciones térmicas.'},
                {'src': '/static/parrilla_mezcla.jpeg.jpeg', 't': 'Encamisado Refractario', 'd': 'Revestimiento interno con tejuelas refractarias asentadas con ligante de alta temperatura. El diseño del "pulmón" se ajustó para garantizar un tiraje óptimo, evitando el retorno de humo y concentrando el calor de forma eficiente en el área de cocción.'}
            ]
        }
    ]
}

@app.route('/')
def trabajos():
    return render_template('index.html', info=CONFIG, pagina='trabajos')

@app.route('/presentacion')
def presentacion():
    todas_fotos = []
    for s in CONFIG['servicios']:
        for f in s['fotos']:
            todas_fotos.append(f['src'])
    return render_template('index.html', info=CONFIG, pagina='presentacion', fotos_cascada=todas_fotos)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)