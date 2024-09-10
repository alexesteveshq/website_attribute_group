# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProductAttribute(models.Model):
    _inherit = "product.attribute"

    show_images = fields.Boolean(string='Show images')
    group_values = fields.Boolean(string='Group values')

    def write(self, vals):
        res = super(ProductAttribute, self).write(vals)
        if vals and ('show_images' in vals or 'group_values' in vals):
            self.env['ir.qweb'].clear_caches()
        return res

class ProductAttributeValue(models.Model):
    _inherit = "product.attribute.value"

    website_product_detail_image = fields.Binary(
        string="Website detail image",
        attachment=True,
        help="Image of the attribute value for shop online product detail.",
    )
    group_id = fields.Many2one('attribute.value.group', string='Group')
    default_selected = fields.Boolean(string='Default selected')
