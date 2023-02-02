from odoo import models,fields,api

class AccountAssetAssetInherit(models.Model):
    _inherit="account.asset.asset"
    #Sobreescribiendo el atributo selection
    state=fields.Selection(selection=[
        ('draft','Borrador'),
        ('open','Corriendo'),
        ('close','Cerrar')
    ])
    method=fields.Selection(selection=[
        ('linear','Lineal'),
        ('degressive','Decreciente')
    ])
    method_time=fields.Selection(selection=[
        ('number','Numero de entradas'),
        ('end','Fecha de finalizaión')
    ])