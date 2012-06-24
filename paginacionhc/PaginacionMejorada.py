#-*- coding: UTF-8 -*-
"""
    accesos_directos_rango(actual, total, numero_accesos)
        Un ejemplo de uso seria:
            ant_pag, pos_pag = accesos_directos_rango(20, 100, 5)
        Y podriamos, si por ejemplo lo usamos para paginar articulos de
        un blog, usar este código en la plantilla:
            {% block paginacion %}
              {% if articulos.has_other_pages %}
              <div class="paginacion">
                {% if articulos.has_previous %}
                  <a href="?pagina=1">primera</a>
                  <a href="?pagina={{ articulos.previous_page_number }}">
                    &lt;
                  </a>
                  {% for anterior in ant_pag %}
                    <a href="?pagina={{ anterior }}">{{ anterior }}</a>
                  {% endfor %}
                {% endif %}
                <span class="pagina-actual">
                  {{ articulos.number }}
                </span>
                {% if articulos.has_next %}
                  {% for posterior in pos_pag %}
                    <a href="?pagina={{ posterior }}">{{ posterior }}</a>
                  {% endfor %}
                  <a href="?pagina={{ articulos.next_page_number }}">
                    &gt;
                  </a>
                  <a href="?pagina={{ articulos.paginator.num_pages }}">
                    ultima
                  </a>
                {% endif %}
              </div>
              {% endif %}
            {% endblock %}
        Y podemos quitar el subrayado de los enlaces con el CSS:
            .paginacion a
              {
                text-decoration:none;
              }
"""


def accesos_directos_rango(actual, total, numero_accesos):
    if numero_accesos < 1:
        return [[], []]
    inicial = actual - numero_accesos
    if inicial < 1:
        inicial = 1
    final = actual + numero_accesos
    if final > total:
        final = total
    return [range(inicial, actual), range(actual + 1, final + 1)]
