from django.contrib import admin

from campanha.models import Campanha, Composicao, DadosCadastrais, Doador, DuracaoCampanha, EntidadeOrganizadora, Meta

admin.site.register(DadosCadastrais)
admin.site.register(Doador)
admin.site.register(EntidadeOrganizadora)
admin.site.register(Campanha)
admin.site.register(DuracaoCampanha)
admin.site.register(Meta)
admin.site.register(Composicao)
