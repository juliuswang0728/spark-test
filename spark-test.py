import py4j
import pyspark
from pyspark.context import SparkContext

sc = SparkContext()
# Control our logLevel. This overrides any user-defined log settings.
# Valid log levels include: ALL, DEBUG, ERROR, FATAL, INFO, OFF, TRACE, WARN
sc.setLogLevel("FATAL")

text_file = sc.textFile(spark_home + "/README.md")
word_counts = text_file \
    .flatMap(lambda line: line.split()) \
    .map(lambda word: (word, 1)) \
    .reduceByKey(lambda a, b: a + b)
print word_counts.collect()
