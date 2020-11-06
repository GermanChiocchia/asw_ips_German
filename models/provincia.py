# -*- coding: utf-8 -*-
from odoo import models, fields, api

class asw_provincia(models.Model):
    _name = 'asw.provincia'
    _description = 'Provincia'

    pro_nombre = fields.Char(
        string=u'Nombre provincia',
    )

    pro_codigo = fields.Char(
        string=u'Codigo provincia',
    )

    localidades_ids = fields.One2many(
        string=u'Localidades',
        comodel_name='asw.localidad',
        inverse_name='provincia_id',
    )

    @api.depends('pro_nombre')
    def name_get(self):
        result = []
        for record in self:            
            name = record.pro_nombre
            result.append((record.id, name))
        return result