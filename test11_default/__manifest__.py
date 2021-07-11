# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2021 jeo Software  (http://www.jeosoft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'test11',
    'version': '11.0.1.0.0',
    'category': 'Tools',
    'summary': "Test for v11 CE",
    'author': "jeo Software",
    'website': 'http://github.com/jobiols/module-repo',
    'license': 'AGPL-3',
    'depends': [
        # basic applications
        'standard_depends_ce',
    ],
    'data': [
    ],
    'installable': True,
    'application': False,

    # Here begins odoo-env manifest configuration
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # manifest version, if omitted it is backward compatible but
    # oe will show a deprecation warning
    'env-ver': '2',

    # Configuration data for odoo.conf
    'config': [
    ],

    # Default to CE, can be ommited
    'odoo-license': 'CE',

    # Port where odoo docker image starts serving pages.
    'port': '8069',

    # repositories to be installed in sources/ dir
    # syntax: the same as git clone
    'git-repos': [
        'https://github.com/jobiols/cl-test.git',

        'git@github.com:jobiols/odoo-uml.git',

        'https://github.com/jobiols/odoo-addons.git',
        'https://github.com/jobiols/odoo-custom.git',

        'https://github.com/ingadhoc/odoo-argentina.git',
        'https://github.com/ingadhoc/account-financial-tools.git',
        'https://github.com/ingadhoc/account-payment.git',
        'https://github.com/ingadhoc/miscellaneous.git',
        'https://github.com/ingadhoc/argentina-reporting.git',
        'https://github.com/ingadhoc/reporting-engine.git',
        'https://github.com/ingadhoc/aeroo_reports.git',
        'https://github.com/ingadhoc/sale.git',
        'https://github.com/ingadhoc/product.git',
        'https://github.com/ingadhoc/account-invoicing.git',
        'https://github.com/ingadhoc/stock.git',
        'https://github.com/ingadhoc/argentina-sale.git',
        'https://github.com/oca/partner-contact.git',
        'https://github.com/oca/web.git',
        'https://github.com/oca/server-tools.git',
        'https://github.com/oca/social.git',
        'https://github.com/oca/server-ux.git',
        'https://github.com/oca/server-brand.git',
        'https://github.com/oca/manufacture.git',
        'https://github.com/oca/manufacture-reporting.git',
        'https://github.com/oca/management-system.git',
        'https://github.com/oca/sale-workflow.git',
        'https://github.com/oca/stock-logistics-warehouse.git',
        'https://github.com/oca/stock-logistics-workflow.git'
    ],

    # Docker images to be used in this deployment
    # syntax: name url
    'docker-images': [
        'odoo jobiols/odoo-jeo:11.0',
        'postgres postgres:10.1-alpine',
        'aeroo adhoc/aeroo-docs'
    ]
}
