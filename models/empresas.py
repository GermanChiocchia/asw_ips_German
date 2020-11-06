# -*- coding: utf-8 -*-
from odoo import models, fields, api

class asw_empresa(models.Model):
    _name = 'asw.empresa'
    _description = 'Empresa'

    emp_nombre = fields.Char(
        string=u'Nombre de la empresa',
    )

    emp_cuit = fields.Char(
        string=u'CUIL',
    )

    emp_direccion = fields.Char(
        string=u'Direccion',
    )

    emp_telefono = fields.Char(
        string=u'Telefono',
    )

    emp_nombre_contacto = fields.Char(
        string=u'Nombre de contacto',
    )

    localidad_id = fields.Many2one(
        string=u'Localidad',
        comodel_name='asw.localidad',
        ondelete='set null',
        _rec_name='name_get()',
    )

    contratos_ids = fields.One2many(
        string=u'´Contratos',
        comodel_name='asw.contrato',
        inverse_name='empresa_id',
    )

    @api.depends('emp_nombre')
    def name_get(self):
        result = []
        for record in self:            
            name = record.emp_nombre
            result.append((record.id, name))
        return result