from odoo import fields, models


class Coupon(models.Model):
    _inherit = "coupon.coupon"

    unconfirmed_sales_order_ids = fields.Many2many(
        "sale.order",
        help="The unconfirmed sales orders that may use this coupon",
        readonly=True,
    )
