# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, date

# Add start and end time to tasks
class Task(models.Model):
    _inherit = 'account.analytic.line'

    start_time = fields.Float(string="Start time")
    end_time = fields.Float(string="End time")

    @api.onchange('start_time','end_time')
    def get_time(self):
        for time in self:
            if (time.end_time - time.start_time) < 0:
                time.unit_amount = 0

            elif (time.end_time - time.start_time) > 16:
                time.unit_amount = 0

            else:
                time.unit_amount = time.end_time - time.start_time
