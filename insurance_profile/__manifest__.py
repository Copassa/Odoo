# -*- coding: utf-8 -*-
##############################################################################
#
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
    'name': "Insurance Odoo Installation profile",
    'summary': """
        Insurance Odoo Installation profile.
    """,
    'Insurance': """
        Solar Odoo Installation profile.
    """,
    'author': 'Angel A. Guadarrama B.',
    'website': "http://aguadarrama.odoo.com",
    'category': 'Base Profile',
    'version': '0.1',
    'depends': [
        'crm', 'sale_subscription_dashboard',
        'partner_contact_personal_information_page',
        'partner_contact_birthdate',
        'partner_contact_gender'],
    'data': [],
    'qweb': [],
    'images': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
