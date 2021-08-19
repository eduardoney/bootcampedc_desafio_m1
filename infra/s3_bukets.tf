resource "aws_s3_bucket" "datalake" {
  #bucket = "my-tf-test-bucket"
  bucket = "${var.base_bucket_name}-${var.numero_conta}"
  acl    = "private"

  tags = {
    projeto = "bootcamp-edc"
  }

  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }
}