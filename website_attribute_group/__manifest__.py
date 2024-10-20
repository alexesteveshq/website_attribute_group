# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Website Product Attribute Group',
    'summary': 'Groups attributes by groups/category. (website attribute group | attribute category |'
               ' product attribute category | attribute subcategory)',
    'description': 'Groups attributes by groups/category',
    'version': '17.0.1.0',
    'category': 'Website',
    'author': 'Visionee',
    'license': 'OPL-1',
    'depends': [
        'website_sale', 'stock',
    ],
    'data': [
        'templates/shop_product.xml',
        'views/product_attribute_value_views.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'website_attribute_image/static/src/**/*',
        ],
    },
    'images': [
        'static/description/example_2.png',
    ],
    'price': 30,
    'currency': "EUR",
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
}
