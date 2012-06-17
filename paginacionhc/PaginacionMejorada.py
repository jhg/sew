#-*- coding: UTF-8 -*-


def accesos_directos_rango(actual, total, numero_accesos):
    if numero_accesos < 1:
        numero_accesos = 1
    inicial = actual - numero_accesos
    if inicial < 1:
        inicial = 1
    final = actual + numero_accesos
    if final > total:
        final = total
    return [range(inicial, actual), range(actual + 1, final + 1)]
