# -*- coding: utf-8 -*-

from odoo import fields, models


class AttributeValueGroup(models.Model):
    _name = "attribute.value.group"
    _description = "Attribute value group"

    name = fields.Char(string='Name', translate=True)
    image = fields.Binary(string='Image')
    is_none = fields.Boolean(string='Is none')
