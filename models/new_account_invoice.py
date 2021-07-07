from odoo import api, fields, models, _


class AccountMove(models.Model):
    _inherit = 'account.move'

    global_discount = fields.Float('Discount')
    total_apres_discount = fields.Float('Total Apres Remise')



