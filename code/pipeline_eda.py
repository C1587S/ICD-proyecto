# importar módulos propios
import load_data as ld
import clean_data as cd
import transform_data as td
import geda as geda
import pandas as pd

# 1 Leer la base de datos
# ----------------------------------------
df = ld.read_data("consumo-agua.csv", sep=";")
# resumen tabla
geda.resumen_tabla(df)
# Tipo de variables incorporadas
geda.tipos_variables(df)

# 2 Limpiar base de datos
# ----------------------------------------
df = cd.clean_column_names(df)
df = cd.eliminar_col(df,"geo_shape")
df = cd.split_column(df, "geo_point", "latitude", "longitude", del_col=True)
# 3 Transformar base de datos
# ----------------------------------------
df = td.to_lowercase(df, cols=["nomgeo", "alcaldia", "colonia", "indice_des"])
df = td.switch_type(df, "longitude", "numeric")
df = td.switch_type(df, "latitude", "numeric")
df = td.switch_type(df, "bimestre", "category")
df = td.switch_type(df, "gid", "category")
df = td.remove_special_char(df, col_name = "alcaldia")
df = td.remove_special_char(df, col_name = "nomgeo")

df.head()
# tabla resumen
geda.resumen_tabla(df)


# Realizar el GEDA
# ----------------------------------------

# Para variables numéricas
df_numerico = geda.df_numerico(df)

for col in df_numerico.columns:
    if df_numerico[col].dtypes == ("float64" or "int64"):
        print("\033[1m"+ "Análisis para la variable numérica: " f"{col}" )
       # muestra tabla de resúmen con estadísticos relevantes:
        summary = df[col].describe()
        df_summary = pd.DataFrame(summary)
        display(df_summary)
        # tabla con valores faltantes
        geda.missing_values(df, col)
        # histograma
        geda.histograma_plot(df, col)

# analisis de correlaciones
geda.heatmap_corr_pearson(df)


# Para variables categóricas
df_categorico = geda.df_categorico(df)

for col in df_categorico.columns:
    if df_categorico[col].dtypes == ("O"):
        print("\033[1m"+ "Análisis para la variable categórica: " f"{col}" )
        if col == "colonia":
             # muestra tabla de resúmen con estadísticos relevantes
            summary = df[col].describe(include = 'category')
            df_summary = pd.DataFrame(summary)
            display(df_summary)
            # mostrar datos faltantes
            geda.missing_values(df, col)
        else:
            summary = df[col].describe(include = 'category')
            df_summary = pd.DataFrame(summary)
            display(df_summary)

            geda.missing_values(df, col)
            geda.bar_plot(df, col)

    else:
        continue

# Análisis combinado

geda.boxplot_category("consumo_prom", "alcaldia", df)
geda.boxplot_category("consumo_total", "alcaldia", df)
geda.boxplot_category("consumo_prom", "indice_des", df )
geda.boxplot_category("consumo_total", "indice_des", df )


geda.plot_three_cat("consumo_prom", "alcaldia", "indice_des", df)
geda.plot_three_cat("consumo_total", "alcaldia", "indice_des", df)

geda.boxplot_category("consumo_prom", "bimestre", df )
geda.boxplot_category("consumo_total", "bimestre", df )

geda.plot_three_cat("consumo_prom", "alcaldia", "bimestre", df)
geda.plot_three_cat("consumo_total", "alcaldia", "bimestre", df)

geda.plot_three_cat("consumo_prom", "indice_des", "bimestre", df)
geda.plot_three_cat("consumo_total", "indice_des", "bimestre", df)

geda.boxplot_category("consumo_total_dom", "alcaldia", df)
geda.boxplot_category("consumo_prom_dom", "alcaldia", df)

geda.boxplot_category("consumo_total_no_dom", "alcaldia", df)
geda.boxplot_category("consumo_prom_no_dom", "alcaldia", df)

geda.boxplot_category("consumo_total_mixto", "alcaldia", df)
geda.boxplot_category("consumo_prom_mixto", "alcaldia", df)

geda.boxplot_category("consumo_total_dom", "indice_des", df)
geda.boxplot_category("consumo_prom_dom", "indice_des", df)

geda.boxplot_category("consumo_total_no_dom", "indice_des", df)
geda.boxplot_category("consumo_prom_no_dom", "indice_des", df)
geda.boxplot_category("consumo_total_mixto", "indice_des", df)
geda.boxplot_category("consumo_prom_mixto", "indice_des", df)

geda.boxplot_category("consumo_total_dom", "bimestre", df)
geda.boxplot_category("consumo_prom_dom", "bimestre", df)

geda.boxplot_category("consumo_total_no_dom", "bimestre", df)
geda.boxplot_category("consumo_prom_no_dom", "bimestre", df)

geda.boxplot_category("consumo_total_mixto", "bimestre", df)
geda.boxplot_category("consumo_prom_mixto", "bimestre", df)
# Combinación de variables categóricas y numéricas
