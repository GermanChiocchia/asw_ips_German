# -*- coding: utf-8 -*-
from odoo import models, fields, api

class asw_localidad(models.Model):
    _name = 'asw.localidad'
    _description = 'Localidad'

    loc_nombre = fields.Char(
        string=u'Nombre localidad',
    )

    loc_codigo = fields.Char(
        string=u'Codigo postal',
    )

    provincia_id = fields.Many2one(
        string=u'Provincia',
        comodel_name = 'asw.provincia',
        ondelete = 'set null',
        _rec_name = 'name_get()',
    )

    @api.depends('loc_nombre')
    def name_get(self):
        result = []
        for record in self:            
            name = record.loc_nombre
            result.append((record.id, name))
        return result