# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Employee Attendance',
    'version': '1.1',
    'category': 'Human Resources',
    'sequence': 76,
    # 'summary': 'Jobs, Departments, Employees Details',
    'description': "",
    'website': 'https://www.odoo.com',
    'depends': [
        'hr'
    ],
    'data': [
        'views/attendance.xml',
        'views/emp_code_inherit.xml',
        'security/group.xml',
        'security/ir.model.access.csv',
        'security/record_rule.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
}