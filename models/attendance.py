from odoo import fields, models, tools , api , exceptions

class Attendance (models.Model):
    _name="hr_attendance"
    _recname = "employee_id"
    _description = "Attendance"
    _order = "employee_id,date desc"

    employee_id = fields.Many2one(
        comodel_name='hr.employee',
        string='Employee',
        required=True)
    employee_code = fields.Char(string='Employee Code',readonly=True, related='employee_id.employee_code',store = True)
    department_id = fields.Many2one(
        comodel_name='hr.department',
        string='Department',readonly=True,
        required=False, store=True, related='employee_id.department_id')
    date = fields.Date(string='Date',required=True)
    checkin = fields.Float("Check in", required=True)
    checkout = fields.Float("Check out", required=True)
    total_hour = fields.Float("Total Hour",store=True , compute = 'total_hour_day')
    total_hour_late = fields.Float("Total Hour Late", store=True , compute = 'total_hour_day')
    total_hour_early = fields.Float("Total Hour Early", store=True , compute = 'total_hour_day')

    # @api.multi
    # def user_checks(self):
    #     self = self.env['hr_attendance'].search([('employee_code'),('date')])


    @api.depends('total_hour', 'total_hour_early', 'checkin', 'checkout', 'total_hour_late')
    def total_hour_day(self):
        for time in self:
            if  0 < time.checkout < time.checkin :
                raise exceptions.ValidationError("Check out > Check in")
            elif time.checkin or time.checkout < 0 :
                raise exceptions.ValidationError("Check in , check out >0")
            elif time.checkin == 0 and time.checkout == 0:
                time.total_hour_late = 0
                time.total_hour_early = 0
                time.total_hour = 0
            elif time.checkin <= 8.5 and 12 < time.checkout <= 13.25:
                time.total_hour_late = 0
                time.total_hour_early = 4.5
                time.total_hour = 3.5
            elif time.checkin > 8.5 and 12 < time.checkout <= 13.25:
                time.total_hour_late = time.checkin - 8.5
                time.total_hour_early = 4.5
                time.total_hour = 3.5 - time.total_hour_late
            elif 12 < time.checkin <= 13.25 and time.checkout < 17.75:
                time.total_hour_late = 3.5
                time.total_hour_early = 17.75 - time.checkout
                time.total_hour = 4.5 - time.total_hour_early
            elif 12 < time.checkin <= 13.25 and time.checkout >= 17.75:
                time.total_hour_late = 3.5
                time.total_hour_early = 0
                time.total_hour = 4.5
            elif time.checkin <= 8.5 and time.checkout <= 12:
                time.total_hour_late = 0
                time.total_hour_early = 4.5 + (12 - time.checkout)
                time.total_hour = time.checkout - 8.5
            elif time.checkin > 8.5 and time.checkout <= 12:
                time.total_hour_late = time.checkin - 8.5
                time.total_hour_early = 4.5 + (12 - time.checkout)
            elif time.checkin >= 13.25 and time.checkout >= 17.75:
                time.total_hour_late = time.checkin - 13.25
                time.total_hour_early = 0
                time.total_hour = 4.5 - time.total_hour_late
            elif time.checkin >= 13.25 and time.checkout < 17.75:
                time.total_hour_late = time.checkin - 13.25
                time.total_hour_early = 17.75 - time.checkout
                time.total_hour = 4.5 - (time.total_hour_late + time.total_hour_early)
            elif time.checkin <= 8.5 and time.checkout >= 17.75:
                time.total_hour_late = 0
                time.total_hour_early = 0
                time.total_hour = 8
            elif time.checkin <= 8.5 and time.checkout <= 17.75:
                time.total_hour_late = 0
                time.total_hour_early = 17.75 - time.checkout
                time.total_hour = 8 - (17.75 - time.checkout)
            elif time.checkin > 8.5 and time.checkout >= 17.75:
                time.total_hour_late = time.checkin - 8.5
                time.total_hour_early = 0
                time.total_hour = 8 - time.total_hour_late
            elif time.checkin > 8.5 and time.checkout < 17.75:
                time.total_hour_late = time.checkin - 8.5
                time.total_hour_early = 17.75 - time.checkout
                time.total_hour = 8 - (time.total_hour_late + time.total_hour_early)
















