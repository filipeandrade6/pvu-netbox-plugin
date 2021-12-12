### JUMPSTART

1. construa essa imagem docker
1. faça uma cópia do netbox versão docker
1. altere o arquivo *docker-compose.yml* do netbox (altere *image: netboxcommunity/net...* por *image: netbox-custom* )
1. altere o arquivo *configuration/configuration.py* e adicione *pvu_netbox_plugin* dentro da lista PLUGINS (px. linha 190)
1. inicie a aplicação