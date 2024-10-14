from odoo import fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    bill_ref = fields.Char(string="Bill Ref")
    bill_count = fields.Integer(default=0)
    bill_id = fields.Integer()

    def action_create_bill(self):
        return {
            "name": "Create Bill",
            "type": "ir.actions.act_window",
            "res_model": "bill.wizard",
            "view_mode": "form",
            "target": "new",
            "context": {"default_picking_id": self.id}
        }

    def action_view_pick_bill(self):
        print("++++++++++++++++", self.bill_id)
        return {
            "name": "Created Bill",
            "type": "ir.actions.act_window",
            "res_model": "account.move",
            "view_mode": "form",
            "res_id": self.bill_id,
            "target": "current",
        }