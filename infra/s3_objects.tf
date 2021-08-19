resource "aws_s3_bucket_object" "codigo_spark" {
  bucket = aws_s3_bucket.datalake.id #Busca o recurso pelo id do primeiro objeto criado.
  key    = "emr-code/pyspark/files_to_parquet.py"
  acl    = "private"
  source = "../processing/files_to_parquet.py"
  etag   = filemd5("../processing/files_to_parquet.py") #Faz a validação para n~ão subir se não tiver alteração.
}
