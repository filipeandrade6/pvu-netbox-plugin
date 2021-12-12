from extras.plugins import PluginConfig

class PvuConfig(PluginConfig):
    name = 'pvu_netbox_plugin'
    verbose_name = 'Projeto de Videomonitoramento Urbano'
    description = 'A plugin of Projeto de Videomonitoramento Urbano for Netbox.'
    version = '0.1'
    author = 'Filipe Andrade'
    author_email = 'filipe.engenharia42@gmail.com'
    base_url = 'pvu'
    required_settings = []
    default_settings = {
        'loud': False
    }

config = PvuConfig