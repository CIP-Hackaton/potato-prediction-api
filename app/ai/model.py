import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from scipy.spatial.distance import norm

class Model:

    distritos_to_vector_path = "app/ai/datasets/DistrToVectorNormal.csv"
    variedades_path = "app/ai/datasets/Variedad_a_Caracteristicas_28_numeric (1).csv"
    ruta_modelo_keras = "app/ai/models/Trained_model_VectorToVector.keras"

    def predict_automatic_mode(self, mes, departamento, provincia, distrito):
        """
        Calcula las normas de los vectores diferencia entre las predicciones ideales y los datos reales
        para cada variedad, dado un mes y una ubicación específica.

        Parámetros:
        distritos_to_vector_path (str): Ruta del primer CSV con las características necesarias.
        variedades_path (str): Ruta del segundo CSV con los vectores reales.
        ruta_modelo_keras (str): Ruta del modelo Keras.
        mes (str): Mes de referencia para la predicción (e.g., "Enero", "ENE").
        departamento (str): Nombre del departamento.
        provincia (str): Nombre de la provincia.
        distrito (str): Nombre del distrito.

        Retorna:
        List[float]: Lista de normas de vectores diferencia por cada variedad.
        """
        # Cargar el primer CSV y eliminar la columna UBIGEO
        df_csv_1 = pd.read_csv(self.distritos_to_vector_path)
        if 'UBIGEO' in df_csv_1.columns:
            df_csv_1 = df_csv_1.drop(columns=['UBIGEO'])

        # Filtrar por ubicación y mes
        df_filtrado = df_csv_1[(df_csv_1['NOMBDEP'] == departamento) &
                            (df_csv_1['NOMBPROV'] == provincia) &
                            (df_csv_1['NOMBDIST'] == distrito) &
                            (df_csv_1['MES'].str.upper() == mes.upper())]

        if df_filtrado.empty:
            raise ValueError("No se encontraron datos para la ubicación y mes especificados.")

        # Seleccionar las características necesarias para el modelo Keras
        input_features = ['TEMP_MAX', 'TIZON_PROMEDIO', 'TEMP_MIN', 'PRECIPITACION',
                        'NEVADA', 'EROSION_PROMEDIO','Clasificacion_Climatica']
        caracteristicas = df_filtrado[input_features].iloc[0].values.astype(float)

        # Cargar el modelo Keras
        modelo_keras = load_model(self.ruta_modelo_keras)

        # Predecir el vector ideal
        vector_ideal = modelo_keras.predict(caracteristicas.reshape(1, -1))

        # Cargar el segundo CSV y calcular las normas de diferencia
        variedades_df = pd.read_csv(self.variedades_path)
        output_features = [
            "Tizón tardío",
            "Materia Seca",
            "Periodo de crecimiento en altura",
            "Color crema predominante de la pulpa",
            "Color amarillo pálido predominante de la pulpa",
            "Forma: Ojos poco profundos",
            "Forma: Ojos ligeramente profundos"
        ]

        normas_diferencia = []

        for i, fila in variedades_df.iterrows():
            vector_real = fila[output_features].values.astype(float)
            norma = norm(vector_real - vector_ideal)
            normas_diferencia.append({
                'Variety': fila['Variety'],
                'Norma_Diferencia': norma
            })

        normas_diferencia.sort(key=lambda x: x["Norma_Diferencia"])
        normas_diferencia = normas_diferencia[:10]


        # Redondear el vector ideal y convertirlo a enteros, ignorando el segundo elemento
        dry_matter = vector_ideal[0][1]
        vector_ideal = np.round(vector_ideal)
        vector_ideal[0][1] = dry_matter

        return normas_diferencia, vector_ideal