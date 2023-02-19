from odoo import models, fields


class Meeting(models.Model):
    _inherit = 'calendar.event'

    mandatory_partner_ids = fields.Many2many(
        'res.partner', 'calendar_event_mand_res_partner_rel', string='Mandatory attendees'
    )
