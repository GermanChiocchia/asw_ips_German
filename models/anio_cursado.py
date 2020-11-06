# -*- coding: utf-8 -*-
from odoo import models, fields, api

class asw_anio_cursado(models.Model):
    _name = 'asw.anio_cursado'
    _description = 'Año cursado'

    ani_periodo = fields.Char(
        string=u'Periodo',
    )

    ani_adeuda_materias = fields.Boolean(
        string=u'Adeuda materias?',
        default=False
    )

    @api.depends('ani_periodo')
    def name_get(self):
        result = []
        for record in self:            
            name = record.ani_periodo
            result.append((record.id, name))
        return result