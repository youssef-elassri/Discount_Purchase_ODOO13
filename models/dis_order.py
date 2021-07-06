from odoo import fields, models, api


class Dis_order_line(models.Model):

    _inherit = "purchase.order"

    discount = fields.Float("Discount")
    amount_after_dis = fields.Monetary("total after discount", compute='_amount_all')

    @api.depends('order_line.price_total')
    def _amount_all(self):
        for order in self:
            amount_untaxed = amount_tax = 0.0
            for line in order.order_line:
                line._compute_amount()
                amount_untaxed += line.price_subtotal
                amount_tax += line.price_tax
            amount_after_dis = amount_untaxed - order.discount
            order.update({
                'amount_untaxed': order.currency_id.round(amount_untaxed),
                'amount_after_dis': amount_untaxed - order.discount,
                'amount_tax': order.currency_id.round(amount_tax),
                'amount_total': amount_after_dis + amount_tax,
            })
