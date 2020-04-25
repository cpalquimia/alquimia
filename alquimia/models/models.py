# -*- coding: utf-8 -*-

from odoo import models, fields, api

# Modelo que hereda blog.post. Añadimos el field para Incorporar una URL del vídeo en la entrada del blog
class Blog(models.Model):
    _inherit = 'blog.post'
   
    #Codigo iframe del visor
    iframe_code = fields.Char('Código iframe Visor Vídeo')

    # @api.depends('video_url')
    # def _compute_iframe_code(self):
    #     for post in self:
    #         iframe_text = "<iframe width=\"560\" height=\"315\" src=\"{URL}\" frameborder=\"0\" allow=\"accelerometer; autoplay;encrypted-media; gyroscope; picture-in-picture\" allowfullscreen=\"1\"></iframe>"
    #         post.iframe_code = iframe_text.format(URL=post.video_url)



# class alquimia(models.Model):
#     _name = 'alquimia.alquimia'
#     _description = 'alquimia.alquimia'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
