from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder.appName("HelloWorld").getOrCreate()
    print("Hello, World!")
    spark.stop()