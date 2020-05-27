# -*- encoding: utf-8 -*-

# Odoo, Open Source Management Solution
# Copyright (C) 2014-2015  Grupo ESOC <www.grupoesoc.es>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from openerp import fields, models


class PartnerInsuranceHistory(models.Model):
    """Partners insurance history."""
    _inherit = "res.partner"

    note_1 = fields.Text(string='Notes 1')
    note_2 = fields.Text(string='Notes 1')
    policy_number = fields.Char(string='Policy number')
    company = fields.Char(string='Company')
    plan = fields.Char(string='Plan')
    effective_date = fields.Char(string='Effective Date')
    p_date = fields.Char(string='P. Type')
