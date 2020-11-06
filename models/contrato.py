# -*- coding: utf-8 -*-
from odoo import models, fields, api

class asw_contrato(models.Model):
    _name = 'asw.contrato'
    _description = 'Contrato'

    con_fecha = fields.Date(
        string=u'Fecha contrato',
    )

    con_activo = fields.Boolean(
        string=u'Sigue activo?',
        default=False
    )

    alumno_id = fields.Many2one(
        string=u'Alumno',
        comodel_name='asw.alumno',
        nodelete='set null',
        _rec_name='name_get()',
    )

    empresa_id = fields.Many2one(
        string=u'Empresa',
        comodel_name='asw.empresa',
        nodelete='set null',
        _rec_name='name_get()',
    )