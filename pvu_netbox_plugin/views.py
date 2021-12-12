from django.shortcuts import render
from django.views.generic import View
from dcim.models import Device, Site

#!./venv/bin/python
# ^estava no topo...

class PontosView(View):
    """
    Display pontos de captura.
    """ 
    def get(self, request):

        table = {}

        # dispositivos = Devices.objects.all()
        # if not dispositivos:
        #     return # não é assim...

        pontos = Site.objects.all()
        print(pontos)

        if not pontos:
            return # não é assim...
        
        for ponto in pontos:
            table[ponto.name] = {
                "ponto": ponto.name,
                "cidade": ponto.region,
                "geo": str(ponto.latitude) + ", " + str(ponto.longitude),
                "endereco": ponto.description,
                # ADICIONAR CAMPOS CUSTOM - CEB ID e TIPO DE PORTE
            }
            # dispositivosPonto = dispositivos["site"][ponto.name]

        print(table)
        
        return render(request, 'pvu_netbox_plugin/pontos.html', {"pontos": table})