from collections import namedtuple
import json
import time

from itertools import groupby
from odoo import api, fields, models, _
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools.float_utils import float_compare, float_is_zero, float_round
from odoo.exceptions import UserError
from odoo.addons.stock.models.stock_move import PROCUREMENT_PRIORITIES
from operator import itemgetter

class limitProduct(models.Model):
	_inherit = 'stock.picking'
	
	@api.one
	def write(self, vals):
		self.ensure_one()
		result = super(limitProduct, self).write(vals)
		same_line = self.env['sale.order'].search([], limit=1)
		purc_line = self.env['purchase.order'].search([], limit=1)
		lista_order = [same_line]
		lista_purch = [purc_line]
		if vals:
			for lines in lista_order:
				for line in vals:
					if line not in lines:
						raise UserError(_('No puedes agregar productos del mismo tipo, diferente a la demanda inicial de la orden.'))

	@api.multi
	def button_validate(self):
		self.ensure_one()
		result = super(limitProduct, self).button_validate()
		res = self.env['sale.order'].search([], limit=1)
		puc = self.env['purchase.order'].search([], limit=1)

		for val in self:
			if val:
				for search_sale in res:
					for line in val.move_lines:
						if search_sale.product_id != line.product_id:
							raise UserError(_('No puede agregar nuevos productos que no se encuentre en la orden.'))	

				for line in val.move_lines:
					if line.quantity_done > 0:
						raise UserError(_('No puedes ingresar mas cantidad de productos, de la demanda inicial.'))

				#for search_purchase in puc:
				#	for line in val.move_lines:
				#		if search_purchase.product_id != line.product_id:
				#			raise UserError(_('No puede agregar nuevos productos, diferentes a la demanda inicial.'))	

