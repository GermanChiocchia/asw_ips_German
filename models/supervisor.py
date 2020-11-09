# -*- coding: utf-8 -*-
from odoo import models, fields, api

class asw_supervisor(models.Model):
    _name = 'asw.supervisor'
    _description = 'Supervisor'

    sup_nombre = fields.Char(
        string=u'Nombre',
    )

    sup_dni = fields.Char(
        string=u'D.N.I.',
    )

    cur_sup_ids = fields.Many2many(
        comodel_name='asw.curso',
        relation='curso_supervisor',
        column1='sup_nombre',
        column2='cur_nombre',
        string=u'Cursos por supervisor',
    )