# Databricks notebook source
# MAGIC %md
# MAGIC # Magic methods
# MAGIC ## some magic methods list
# MAGIC - fs
# MAGIC - sql
# MAGIC - scala
# MAGIC - python

# COMMAND ----------

# MAGIC %sql
# MAGIC select "hello"

# COMMAND ----------

# MAGIC %sh
# MAGIC ls -l

# COMMAND ----------

# MAGIC %fs
# MAGIC ls

# COMMAND ----------

ls /databricks-datasets/

# COMMAND ----------

dbutils.fs.ls("/")

# COMMAND ----------

dbutils.fs.ls("dbfs:/databricks-datasets/COVID")

# COMMAND ----------

for file in dbutils.fs.ls("dbfs:/databricks-datasets/COVID"):
    if file.name.endswith("/"):
        print(file.name)

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help("ls")

# COMMAND ----------


