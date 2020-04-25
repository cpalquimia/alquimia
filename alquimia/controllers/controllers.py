# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class Alquimia(http.Controller):
    #Pide autenticación para entrar en zona privada entrenadores
    @http.route('/entrenadores', auth='user', website=True)
    def entrenadores(self, **kw):
        return request.render('website.entrenadores')
    #Pide autenticación para entrar en zona privada socios
    @http.route('/socios', auth='user', website=True)
    def socios(self, **kw):
        return request.render('website.socios')
    #La zona privada website del usuario la redirige a la principal
    @http.route('/my', auth='user', website=True)
    def my(self, **kw):
        return request.redirect('/')

    # @http.route('/zona-privada', auth='user', website=True)
    # def zonaPrivada(self, **kw):
    #     #Usuarios entrenador y socio
    #     entuser = request.env['res.users'].search([('name', 'ilike', 'entrenador')])
    #     socuser = request.env['res.users'].search([('name', 'ilike', 'socio')])
    #     entuid = entuser.id if entuser else -1
    #     socuid = socuser.id if socuser else -1

    #     #Blogs para entrenador y socio
    #     entblog = request.env['blog.blog'].search([('name', 'ilike', 'Entrenadores')])
    #     socblog = request.env['blog.blog'].search([('name', 'ilike', 'Socios')])
    #     entblogid = entblog.id if entblog else -1
    #     socblogid = socblog.id if socblog else -1

    #     if request.env.context.get('uid') == entuid:            
    #         #Invoca al template entrenadores_privada
    #         return request.render('alquimia.entrenadores_privada', {'blog_id':entblogid})           
            
    #     elif request.env.context.get('uid') == socuid:            
    #         #Invoca al template socios_privada
    #         return request.render('alquimia.socios_privada', {'blog_id':socblogid})            

#     @http.route('/alquimia/alquimia/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/alquimia/alquimia/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('alquimia.listing', {
#             'root': '/alquimia/alquimia',
#             'objects': http.request.env['alquimia.alquimia'].search([]),
#         })

#     @http.route('/alquimia/alquimia/objects/<model("alquimia.alquimia"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('alquimia.object', {
#             'object': obj
#         })
