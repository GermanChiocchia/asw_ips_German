# -*- coding: utf-8 -*-
from odoo import models, fields, api

class asw_curso(models.Model):
    _name = 'asw.curso'
    _description = 'Curso'

    cur_nombre = fields.Char(
        string=u'Nombre del curso',
    )

    cur_completado = fields.Boolean(
        string=u'Completado?',
        default=False
    )

    cur_sup_ids = fields.Many2many(
        comodel_name='asw.supervisor',
        relation='curso_supervisor',
        column1='cur_nombre',
        column2='sup_nombre',
        string=u'Supervisores por curso',
    )

    @api.depends('cur_nombre')
    def name_get(self):
        result = []
        for record in self:            
            name = record.cur_nombre
            result.append((record.id, name))
        return result