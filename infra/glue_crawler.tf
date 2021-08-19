resource "aws_glue_catalog_database" "database" {
  name = var.database
}

resource "aws_glue_crawler" "docentes" {
  database_name = aws_glue_catalog_database.database.name
  name          = "docentes"
  role          = aws_iam_role.iam_glue_crawler_service_role.arn

  s3_target {
    path = "s3://${aws_s3_bucket.datalake.bucket}/staging/microdados_educacao_basica/docentes/"
  }
}


resource "aws_glue_crawler" "matricula" {
  database_name = aws_glue_catalog_database.database.name
  name          = "matricula"
  role          = aws_iam_role.iam_glue_crawler_service_role.arn

  s3_target {
    path = "s3://${aws_s3_bucket.datalake.bucket}/staging/microdados_educacao_basica/matricula/"
  }
}