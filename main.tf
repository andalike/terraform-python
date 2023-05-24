resource "null_resource" "run_python" {
  provisioner "local-exec" {
    command = "python3 ./code-lookout.py"
  }
}