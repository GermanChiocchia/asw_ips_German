# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions

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

    @api.model
    def create(self, values):
        if ('ani_periodo' in values and values['ani_periodo'] != '' and values['ani_periodo'] != '0'):
            cnt = self.env['asw.anio_cursado'].search_count([('ani_periodo', '=', values['ani_periodo'])])
            if(cnt>0):
                raise exceptions.Warning('''Ya existe el año ingresado, 
                por favor reviselo y vuelva a intentarlo''')
        result = super(asw_anio_cursado, self).create(values)
        return result
    
    def write(self, values):
        if ('ani_periodo' in values and values['ani_periodo'] != '' and values['ani_periodo'] != '0'):
            cnt = self.env['asw.anio_cursado'].search_count([('ani_periodo', '=', values['ani_periodo']),('id', '!=', self.id)])
            if(cnt > 0):
                raise exceptions.Warning('''Ya existe el periodo ingresado, 
                por favor vuelva a intentarlo''')
        result = super(asw_anio_cursado, self).write(values)
        return result

    @api.onchange('ani_periodo')
    def onchange_dni(self):
        cnt = self.env['asw.anio_cursado'].search_count([('ani_periodo', '=', self.ani_periodo)])
        if(cnt > 0):
            raise exceptions.Warning('''Ya existe el epriodo ingresado, 
            por favor vuelva a intentarlo''')