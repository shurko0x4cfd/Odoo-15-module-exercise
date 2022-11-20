# -*- coding: utf-8 -*-

from odoo import models, fields, api
import random
from typing import Final


EMPTY_TOTAL: Final = 0.0
MAX_RANDOM: Final = 1000000000


class SaleOrder (models.Model):
    _inherit = 'sale.order'

    _description = 'Test description'
    active = True

    test = fields.Char('Test', readonly=True,
                       store=True,
                       compute='_test_field_compute',
                       recursive=True,
                       copy=True,
                       states={'draft': [('readonly', False)], })

    latest = fields.Monetary('Latest changed total', default=EMPTY_TOTAL)
    latest_valid = fields.Char('Latest valid test field', default='')
    state_total = fields.Char('State total', default='new')
    state_date = fields.Char('State date', default='new')
    state_test = fields.Char('State test', default='new')

    @api.depends('amount_total')
    def _test_field_compute(self):
        amount_total = self.amount_total

        if self.state_total == 'new':
            self.state_total = 'young'
            self.test = self.latest = random.randint(1, MAX_RANDOM)
            return

        if self.state_total == 'young':
            self.state_total = 'old'
            self.latest = amount_total

        if self.latest == amount_total:
            return

        self.latest = amount_total
        self.test = self.latest_valid = \
            str(amount_total) + ' - ' + str(self.date_order)

    @api.onchange('date_order')
    def _on_change_date_order(self):

        if self.state_date == 'new':
            self.state_date = 'old'
            return

        self.latest = self.amount_total
        self.test = self.latest_valid = \
            str(self.amount_total) + ' - ' + str(self.date_order)

    @api.onchange('test')
    def _on_change_test(self):

        if self.state_test == 'new':
            self.state_test = 'old'
            return

        if len(self.test) > 49:
            self.test = self.latest_valid
            return{
                'warning': {
                    'title': 'Неправильно заполнено поле',
                    'message': 'Длина текста должна быть меньше 50 символов!'
                }
            }

        self.latest = self.amount_total
        self.latest_valid = self.test


#
