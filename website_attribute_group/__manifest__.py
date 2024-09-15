# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Website Product Attribute Group',
    'summary': 'Groups attributes by groups/category. (website attribute group | attribute category | product attribute category)',
    'description': 'Groups attributes by groups/category',
    'version': '16.0.1.0',
    'category': 'Website',
    'author': 'Visionee',
    'license': 'OPL-1',
    'depends': [
        'website_sale', 'stock',
    ],
    'data': [
        'templates/shop_product.xml',
        'views/product_attribute_value_views.xml',
        'views/attribute_value_group_views.xml',
        'data/website_attribute_image_data.xml',
        'security/ir.model.access.csv',
    ],
    'assets': {
        'web.assets_frontend': [
            'website_attribute_group/static/src/**/*',
        ],
    },
    'images': [
        'static/description/banner.gif',
    ],
    'price': 30,
    'currency': "EUR",
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
}
