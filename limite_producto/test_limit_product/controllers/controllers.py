# -*- coding: utf-8 -*-
from odoo import http

# class TestLimitProduct(http.Controller):
#     @http.route('/test_limit_product/test_limit_product/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_limit_product/test_limit_product/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_limit_product.listing', {
#             'root': '/test_limit_product/test_limit_product',
#             'objects': http.request.env['test_limit_product.test_limit_product'].search([]),
#         })

#     @http.route('/test_limit_product/test_limit_product/objects/<model("test_limit_product.test_limit_product"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_limit_product.object', {
#             'object': obj
#         })