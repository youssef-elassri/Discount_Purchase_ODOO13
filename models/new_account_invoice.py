from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    global_discount = fields.Float('Discount', compute='_cmp_totals')
    total_before_discount = fields.Float('Total avant remise', compute='_cmp_totals')


    @api.model
    def _cmp_totals(self):
        for move in self:
            total = glob_dis = 0
            for line in move.line_ids:
                if line.price_unit > 0:
                    total = line.purchase_line_id.order_id.amount_untaxed
                    glob_dis = line.purchase_line_id.order_id.total_discount
            move.global_discount = glob_dis
            move.total_before_discount = total
            move.amount_untaxed = move.total_before_discount - move.global_discount


