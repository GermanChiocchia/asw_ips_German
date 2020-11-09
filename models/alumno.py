# -*- coding: utf-8 -*-
from odoo import models, fields, api


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
        deafult=True
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