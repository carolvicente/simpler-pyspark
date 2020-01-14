from pyspark.sql.functions import udf, lit, row_number, monotonically_increasing_id, unix_timestamp, lit
from pyspark.sql.types import *
from pyspark.sql import *




def replace_ocurrence_in_column(str: current_value, str: target_value, DataFrame: dataframe, str: column_name):

    res_udf = udf(lambda x: lit(x.replace(current_value, target_value)))
    return  dataframe.withColumn(column_name, res_udf(column_name))