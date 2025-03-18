import pandas as pd
import jsonpickle

def read_excel_file(file_path, sheet_name):
    """Lee el archivo Excel y devuelve un DataFrame."""
    try:
        return pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')
    except Exception as e:
        print(f"Error al leer el archivo Excel: {e}")
        return None

def fill_missing_ends(df):
    """Rellena la columna 'Ends' con el valor de 'Start' si está vacía."""
    if 'Ends' in df.columns and 'Start' in df.columns:
        df['Ends'] = df.apply(lambda row: row['Start'] if pd.isna(row['Ends']) else row['Ends'], axis=1)
    return df

def remove_empty_columns(df):
    """Elimina las columnas vacías de cada fila."""
    return df.apply(lambda row: {k: v for k, v in row.items() if pd.notna(v)}, axis=1).to_list()

def filter_digital_no(df):
    """Filtra las filas donde la columna 'Digital' no sea 'No'."""
    return df[df['Digital'] != 'No']

def convert_day_to_int(df):
    """Convierte los valores de la columna 'Day' a enteros si es posible."""
    if 'Day' in df.columns:
        df['Day'] = df['Day'].apply(lambda x: int(x) if pd.notna(x) else x)
    return df

def save_to_js(data, output_file):
    """Guarda los datos en un archivo JS con export default."""
    json_data = jsonpickle.encode(data, unpicklable=False, indent=4)
    with open(output_file, 'w') as file:
        file.write('const schedule = ')
        file.write(json_data)
        file.write(';\nexport default schedule;')
    print(f"Archivo JS '{output_file}' creado exitosamente.")

def split_by_day(df, day1, day2):
    """Divide los eventos en dos días basándose en la columna 'Day'."""
    df_day1 = df[df['Day'] == day1]
    df_day2 = df[df['Day'] == day2]
    return df_day1, df_day2

def main():
    # Configuración
    file_path = 'schedule.xlsx'
    day1 = 3
    day2 = 4

    sheet_name = f'Day {day1}&{day2}'
    output_file_day1 = f'schedule_{day1}.js'
    output_file_day2 = f'schedule_{day2}.js'

    # Proceso
    df = read_excel_file(file_path, sheet_name)
    if df is not None:
        print("Datos leídos del archivo Excel:")
        print(df.head())  # Mostrar las primeras filas para verificar los datos

        df = filter_digital_no(df)
        print("Datos después de filtrar 'Digital' no 'No':")
        print(df.head())  # Verificar los datos después del filtrado

        df = fill_missing_ends(df)
        print("Datos después de rellenar 'Ends':")
        print(df.head())  # Verificar los datos después de rellenar 'Ends'

        df = convert_day_to_int(df)
        print("Datos después de convertir 'Day' a enteros:")
        print(df.head())  # Verificar los datos después de convertir 'Day'

        # Dividir los datos en dos días basándose en la columna 'Day'
        df_day1, df_day2 = split_by_day(df, day1, day2)
        print(f"Datos para el día {day1}:")
        print(df_day1.head())  # Verificar los datos para el día 1
        print(f"Datos para el día {day2}:")
        print(df_day2.head())  # Verificar los datos para el día 2

        # Eliminar columnas vacías y convertir a lista de diccionarios
        data_day1 = remove_empty_columns(df_day1)
        data_day2 = remove_empty_columns(df_day2)

        # Guardar en archivos JS separados
        save_to_js(data_day1, output_file_day1)
        save_to_js(data_day2, output_file_day2)

if __name__ == "__main__":
    main()