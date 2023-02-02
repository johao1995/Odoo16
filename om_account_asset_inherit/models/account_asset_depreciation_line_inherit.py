from odoo  import models,fields,api

class AccountAssetDepreciationLineInherit(models.Model):
    _inherit="account.asset.depreciation.line"

    name=fields.Char(string="Nombre de depreciación")
    amount=fields.Monetary(string="Depreciación actual ")
    sequence=fields.Integer(string="Secuencia")
    depreciation_date=fields.Date(string="Fecha de depreciación")
    move_id=fields.Many2one(string="Entrada de depreciación")
    depreciated_value=fields.Monetary(string="Depreciación acumulada")
    move_check =fields.Boolean(string="Enlazado")
    remaining_value=fields.Monetary(string="Próximo Período Depreciación")