# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class res_users(models.Model):
    _inherit = 'res.users'

    usr_alumno = fields.Many2one(
        string=u'Alumno',
        comodel_name='asw.alumno',
        ondelete='set null',
    )

    usr_supervisor = fields.Many2one(
        string=u'Supervisor',
        comodel_name='asw.supervisor',
        ondelete='set null',
    )

    usr_empresa = fields.Many2one(
        string=u'Empresa',
        comodel_name='asw.empresa',
        ondelete='set null',
    )