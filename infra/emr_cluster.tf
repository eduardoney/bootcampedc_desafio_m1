resource "aws_emr_cluster" "cluster" {
  name          = "emr-edc-${var.numero_conta}"
  release_label = "emr-6.3.0"
  applications  = ["Spark", "Hadoop", "Hive", "JupyterHub", "JupyterEnterpriseGateway", "Hue", "Pig", "Livy"]

  termination_protection            = false
  keep_job_flow_alive_when_no_steps = true

  ec2_attributes {
    key_name  = "ec2-key-bootcamp-edc"
    subnet_id = aws_subnet.main.id
    #emr_managed_master_security_group = aws_security_group.sg.id
    #emr_managed_slave_security_group  = aws_security_group.sg.id
    instance_profile = aws_iam_instance_profile.emr_profile.arn
  }

  master_instance_group {
    instance_type  = "m4.large"
    instance_count = 1
    bid_price      = "0.20"
  }

  core_instance_group {
    instance_type  = "c4.large"
    instance_count = 1

    ebs_config {
      size                 = "40"
      type                 = "gp2"
      volumes_per_instance = 1
    }

    bid_price = "0.20"
  }

  ebs_root_volume_size = 50

  tags = {
    projeto = "bootcamp-edc"
  }

  service_role = aws_iam_role.iam_emr_service_role.arn
}