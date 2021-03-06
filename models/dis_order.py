from odoo import fields, models, api


class Dis_order(models.Model):

    _inherit = "purchase.order"

    discount = fields.Float("Discount")
    discount_valeur = fields.Float("Discount")
    total_discount = fields.Float("Total Discount", compute='_amount_all')
    amount_after_dis = fields.Float("total after discount", compute='_amount_all')
    type_discount = fields.Selection(selection=[
        ('fixed', 'fixed'),
        ('percentage', 'percentage')
    ], String = 'Type de remise')

    @api.depends('order_line.price_total')
    def _amount_all(self):
        for order in self:
            discount_lines = amount_untaxed = amount_tax = 0.0
            for line in order.order_line:
                line._compute_amount()
                amount_untaxed += line.price_subtotal
                amount_tax += line.price_tax
                discount_lines += line.price_subtotal * line.discount * 0.01

                order.discount_valeur = (amount_untaxed - discount_lines) * order.discount * 0.01 if order.type_discount == 'percentage' else order.discount
            order.total_discount = discount_lines + order.discount_valeur
            amount_after_dis = amount_untaxed - order.total_discount
            order.update({
                'amount_untaxed': order.currency_id.round(amount_untaxed),
                'amount_after_dis': amount_untaxed - order.total_discount,
                'amount_tax': order.currency_id.round(amount_tax),
                'amount_total': amount_after_dis + amount_tax,
            })

