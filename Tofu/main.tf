terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.5"
    }
  }
}

variable "student_name" {
  type    = string
  default = "OpenTofu Learner"
}

resource "local_file" "hello" {
  filename = "${path.module}/hello.txt"
  content  = "Hello, ${var.student_name}! This file was created locally.\n"
}

output "test_file_path" {
  value = local_file.hello.filename
}   