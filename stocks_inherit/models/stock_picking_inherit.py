from odoo import models,fields,api

class StockPickingInherit(models.Model):
    _inherit="stock.picking"

    state=fields.Selection(selection=[
        ('draft','Borrador'),
        ('waiting','Esperando otra operaacion'),
        ('confirmed','Esperando'),
        ('assigned','Pendiente'),
        ('done','Recibido'),
        ('cancel','Cancelado')
    ])