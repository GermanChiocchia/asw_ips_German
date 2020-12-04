# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions


class asw_alumno(models.Model):
    _name = 'asw.alumno'
    _description = 'Alumno'

    alu_nombre = fields.Char(
        string=u'Nombre',
    )

    alu_dni = fields.Char(
        string=u'D.N.I',
    )

    alu_legajo = fields.Integer(
        string=u'Legajo',
    )

    active = fields.Boolean(
        string=u'Esta activo?',
        default=True
    )

    sequence = fields.Integer(
        string=u'Secuencia',
    )

    anio_cursado_id = fields.Many2one(
        string=u'Año cursado',
        comodel_name='asw.anio_cursado',
        ondelete='set null',
        _rec_name='name_get()',
    )

    localidad_id = fields.Many2one(
        string=u'Localidad',
        comodel_name='asw.localidad',
        ondelete='set null',
        _rec_name='name_get()',
    )

    reportes_diarios_ids = fields.One2many(
        string=u'Reportes diarios',
        comodel_name='asw.reporte_diario',
        inverse_name='alumno_id',
    )

    curso_id = fields.Many2one(
        string=u'Curso',
        comodel_name='asw.curso',
        ondelete='set null',
        _rec_name='name_get()',
    )

    alu_horas_trabajadas = fields.Float(
        string =u'Horas trabajadas',
        compute = '_compute_alu_horas_trabajadas',
    )

    alu_porcentaje_hs_trabajadas = fields.Float(
        string =u'% sobre 200 hs trabajadas',
        compute = '_compute_porcentaje_hs_trabajadas',
    )

    @api.depends('reportes_diarios_ids')
    def _compute_alu_horas_trabajadas(self):
        for record in self:
            arr_horas = record.reportes_diarios_ids.mapped('rep_hs_trabajadas')
            suma_horas = sum(arr_horas)
            record.alu_horas_trabajadas = suma_horas

    @api.depends('alu_horas_trabajadas')
    def _compute_porcentaje_hs_trabajadas(self):
        for record in self:
            record.alu_porcentaje_hs_trabajadas = record.alu_horas_trabajadas / 2


    @api.depends('alu_nombre')
    def name_get(self):
        result = []
        for record in self:            
            name = record.alu_nombre
            result.append((record.id, name))
        return result
    
    @api.model
    def create(self, values):
        if ('alu_dni' in values and values['alu_dni'] != '' and values['alu_dni'] != '0'):
            cnt = self.env['asw.alumno'].search_count([('alu_dni', '=', values['alu_dni'])])
            if(cnt>0):
                raise exceptions.Warning('''Ya existe un alumno cargado con el dni ingresado, 
                por favor revise el numero de documento y vuelva a intentarlo''')
        result = super(asw_alumno, self).create(values)
        return result
    
    def write(self, values):
        if ('alu_dni' in values and values['alu_dni'] != '' and values['alu_dni'] != '0'):
            cnt = self.env['asw.alumno'].search_count([('alu_dni', '=', values['alu_dni']),('id', '!=', self.id)])
            if(cnt > 0):
                raise exceptions.Warning('''Ya existe un alumno cargado con el dni ingresado, 
                por favor revise el numero de documento y vuelva a intentarlo''')
        result = super(asw_alumno, self).write(values)
        return result

    @api.onchange('alu_dni')
    def onchange_dni(self):
        cnt = self.env['asw.alumno'].search_count([('alu_dni', '=', self.alu_dni)])
        if(cnt > 0):
            raise exceptions.Warning('''Ya existe un alumno cargado con el dni ingresado, 
            por favor revise el numero de documento y vuelva a intentarlo''')
    
    def unlink(self):
        for record in self:
            cnt = self.env['asw.reporte_diario'].search_count([('alumno_id', '=', record.id)])
            if(cnt!= 0):
                raise exceptions.UserError('''No puede eliminarse el registro del alumno
                %S ya que posee reportes diarios cargados''' % record.alu_nombre)
            result = super(asw_alumno, record).unlink()