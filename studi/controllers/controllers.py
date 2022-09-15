# -*- coding: utf-8 -*-
# from odoo import http


# class Studi(http.Controller):
#     @http.route('/studi/studi', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/studi/studi/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('studi.listing', {
#             'root': '/studi/studi',
#             'objects': http.request.env['studi.studi'].search([]),
#         })

#     @http.route('/studi/studi/objects/<model("studi.studi"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('studi.object', {
#             'object': obj
#         })
