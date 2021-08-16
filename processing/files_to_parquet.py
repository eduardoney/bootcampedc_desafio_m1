from pyspark.sql import SparkSession

# Create Spark Session
spark = (SparkSession
         .builder
         .appName("files_to_parquet")
         .getOrCreate())

file_list = ["docentes","escolas","gestor","matricula","turmas"]

for file in file_list:
    # read file csv
    df_data = (
        spark
        .read
        .format("csv")
        .option("delimiter", "|")
        .option("header", True)
        .option("inferSchema", True)
        .load(f"s3://datalake-eduardoney-707008544288/raw-data/microdados_educacao_basica_2020/{file}*.CSV")

    )
    (   # Save in parquet format
        df_data
        .write
        .mode("overwrite")
        .format("parquet")
        .partitionBy("NU_ANO_CENSO")
        .save(f"s3://datalake-eduardoney-707008544288/staging/microdados_educacao_basica/{file}")
    )
