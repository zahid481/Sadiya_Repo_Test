#read data
df_read = spark.read.format('csv')\
                    .option('header', True)\
                    .saveAsTable('dbname.bronze_table')

df_read = df_read.select("name", "Id")