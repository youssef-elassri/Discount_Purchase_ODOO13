from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    global_discount = fields.Float('Discount', compute='_cmp_totals')
    total_before_discount = fields.Float('Total avant remise', compute='_cmp_totals')


    @api.model
    def _cmp_totals(self):
        for move in self:
            total = total_dis = 0
            for line in move.line_ids:
                if line.price_unit > 0:
                    total += line.price_subtotal_d
                    print(total)
                    total_dis += (line.discount * 0.01) * line.price_subtotal_d
            move.global_discount = total_dis # + discount order
            move.total_before_discount = total
            move.amount_untaxed = move.total_before_discount - move.global_discount


