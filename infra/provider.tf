provider "aws" {
    region = $var.region
}

terraform {
  backend "s3" {
    name = "value"
    bucket = "terraform-state-eduney-707008544288"
    key = "state/desafiomod1/terraform.tfstate"
  }
}
