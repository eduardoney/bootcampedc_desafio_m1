variable "base_bucket_name" {
  type        = string
  default     = "datalake-eduardoney"
  description = "Bucket base do projeto"
}

variable "numero_conta" {
  type        = string
  default     = "707008544288"
  description = "Numero da conta na aws"
}

variable "aws_region" {
  type        = string
  default     = "us-east-1"
  description = "Região default do aws"
}

variable "database" {
  type        = string
  default     = "datalake_edc"
  description = "Nome da base de dados para consumo do athena"
}
