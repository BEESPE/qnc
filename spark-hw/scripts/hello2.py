from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder.appName("HelloWorld2").getOrCreate()
    print("Hello 2")
    spark.stop()
