# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions

class asw_reporte_diario(models.Model):
    _name = 'asw.reporte_diario'
    _description = 'Reporte diario'

    rep_fecha = fields.Date(
        string=u'Fecha',
    )

    rep_hora_ingreso = fields.Datetime(
        string=u'Horario de ingreso',
    )

    rep_hora_egreso = fields.Datetime(
        string=u'Horario de egreso',
    )

    rep_actividad = fields.Html(
        string=u'Actividad que realizó',
    )

    rep_obstaculos = fields.Html(
        string=u'Obstaculos',
    )

    rep_hs_trabajadas = fields.Integer(
        string=u'Horas trabajadas',
    )

    alumno_id = fields.Many2one(
        string=u'Alumno',
        comodel_name='asw.alumno',
        ondelete='set null',
        _rec_name='name_get()',
    )

    @api.model
    def create(self, values):
        if (values['rep_hora_ingreso'] > values['rep_hora_egreso']):
            raise exceptions.Warning('''La hora de egreso nunca puede ser menor a la de ingreso,
            por favor corrijalo''')
        result = super(asw_reporte_diario, self).create(values)
        return result
    
    def write(self, values):
        if (values['rep_hora_ingreso'] > values['rep_hora_egreso']):
            raise exceptions.Warning('''La hora de egreso nunca puede ser menor a la de ingreso,
            por favor corrijalo''')
        result = super(asw_reporte_diario, self).create(values)
        return result

    @api.onchange('rep_hora_ingreso')
    def onchange_rep(self):
        if (self.rep_hora_ingreso > self.rep_hora_egreso):
            raise exceptions.Warning('''La hora de egreso nunca puede ser menor a la de ingreso,
                por favor corrijalo''')