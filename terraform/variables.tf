variable "cluster" {
  default = "akscluster"
}
variable "app" {
  type        = string
  description = "aldemo"
  default     = "aldemo"
}
variable "zone" {
  default = "east-us"
}
variable "docker-image" {
  type        = string
  description = "app"
  default     = "dexdv/aks:latest"
}