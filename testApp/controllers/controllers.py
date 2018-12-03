# -*- coding: utf-8 -*-
from odoo import http

# class Cardiologieb(http.Controller):
#     @http.route('/cardiologieb/cardiologieb/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cardiologieb/cardiologieb/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cardiologieb.listing', {
#             'root': '/cardiologieb/cardiologieb',
#             'objects': http.request.env['cardiologieb.cardiologieb'].search([]),
#         })

#     @http.route('/cardiologieb/cardiologieb/objects/<model("cardiologieb.cardiologieb"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cardiologieb.object', {
#             'object': obj
#         })