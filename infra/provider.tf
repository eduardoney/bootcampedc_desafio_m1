provider "aws" {
  region = var.aws_region
}

terraform {
  backend "s3" {
    bucket = "terraform-state-eduney-707008544288"
    key    = "state/desafiomod1/terraform.tfstate"
  }
}
