from odoo import api, fields, models


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    price_subtotal_d = fields.Float('Subtotal', compute="_cmp_sub")

    @api.model
    def _cmp_sub(self):
        for line in self:
            line.price_subtotal_d = line.price_unit * line.quantity