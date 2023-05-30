terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "3.57.0"
    }
  }
}

provider "azurerm" {
  # Configuration options
  subscription_id = var.subscription_id
  tenant_id = var.tenant_id 
  client_id = var.client_id
  client_secret = var.client_secret
  skip_provider_registration = "true"
  features {}
}

locals {
  resource_group_name="groupApp"
  location="East US"
}

resource "azurerm_resource_group" "groupapp" {
  name     = local.resource_group_name
  location = local.location
}

resource "azurerm_storage_account" "aldemostorage" {
  name                     = "aldemostorage"
  resource_group_name      = local.resource_group_name
  location                 = local.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  account_kind = "StorageV2"
  depends_on =  [
    azurerm_resource_group.groupapp
   ]
  tags = {
    environment = "staging"
  }
}
resource "azurerm_container_registry" "aldemoreg" {
  name                = "aldemoreg"
  resource_group_name = local.resource_group_name
  location            = local.location
  sku                 = "Basic"
  admin_enabled       = true
  depends_on = [
    azurerm_storage_account.aldemostorage
  ]
}
resource "azurerm_kubernetes_cluster" "akscluster" {
  name                = "AKSCluster"
  location            = local.location
  resource_group_name = local.resource_group_name
  dns_prefix          = "AKSCluster"

  default_node_pool {
    name       = "default"
    node_count = 2
    vm_size    = "Standard_D2_v2"
  }

  identity {
    type = "SystemAssigned"
  }

  tags = {
    Environment = "Staging"
  }
}

output "client_certificate" {
  value     = azurerm_kubernetes_cluster.akscluster.kube_config.0.client_certificate
  sensitive = true
}

output "kube_config" {
  value = azurerm_kubernetes_cluster.akscluster.kube_config_raw

  sensitive = true
}