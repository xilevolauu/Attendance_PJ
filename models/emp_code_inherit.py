# -*- coding: utf-8 -*-
from odoo import fields, models, tools

class EmpCodeInherit (models.Model):
    _inherit = 'hr.employee'
    employee_code = fields.Char('Employee Code')

    _sql_constraints = [('nonono', 'UNIQUE(employee_code)', 'Code is not duplicate, re-enter')]
