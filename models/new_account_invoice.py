from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    global_discount = fields.Float('Discount', compute='cmp_totals')
    total_before_discount = fields.Float('Total avant remise', compute='cmp_totals')

    @api.model
    def cmp_totals(self):
        for move in self:
            total = total_dis = glob_dis = 0
            for line in move.line_ids:
                if line.price_unit > 0:
                    total += line.price_subtotal_d
                    total_dis += line.discount * 0.01 * line.price_subtotal_d
                    if line.purchase_line_id.order_id:
                        glob_dis = line.purchase_line_id.order_id.discount_valeur
            move.global_discount = glob_dis + total_dis
            move.total_before_discount = total
            move.amount_untaxed = move.total_before_discount - move.global_discount
            move.amount_total = move.amount_tax + move.amount_untaxed
            move.amount_total_signed = abs(move.amount_total) if move.type == 'entry' else -move.amount_total
            move.amount_untaxed_signed = abs(move.amount_untaxed) if move.type == 'entry' else -move.amount_untaxed


