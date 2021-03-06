import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo11-addons-oca-stock-logistics-workflow",
    description="Meta package for oca-stock-logistics-workflow Odoo addons",
    version=version,
    install_requires=[
        'odoo11-addon-stock_no_negative',
        'odoo11-addon-stock_pack_operation_auto_fill',
        'odoo11-addon-stock_picking_invoice_link',
        'odoo11-addon-stock_picking_show_backorder',
        'odoo11-addon-stock_picking_show_return',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
