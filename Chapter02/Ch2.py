import pyspark
if not 'sc' in globals():
    sc = pyspark.SparkContext()
lines = sc.textFile("B09656_02 Spark Sample.ipynb")
lineLengths = lines.map(lambda s: len(s))
totalLengths = lineLengths.reduce(lambda a, b: a + b)
print(totalLengths)