from odoo import fields, models


class BillWizard(models.TransientModel):
    _name = "bill.wizard"
    _description = "Create Bill Wizard"

    journal_id = fields.Many2one("account.journal", string="Journal")
    bill_date = fields.Date(string="Date Time")

    def action_create_bill(self):
        purchase_line = []
        pick = self.env.context.get("default_picking_id")
        picking = self.env["stock.picking"].browse(pick)
        for line in picking.move_ids:
            name = str(line.description_picking)
            purchase_line.append((0, 0, {
                "product_id": line.product_id.id,
                "name": name,
                "quantity": line.quantity,
                "price_unit": line.product_id.standard_price,
            }))
        new_bill = self.env["account.move"].create({
            "partner_id": picking.partner_id.id,
            "invoice_date": self.bill_date,
            "date": picking.scheduled_date,
            "move_type": "in_invoice",
            "journal_id": self.journal_id.id,
            "line_ids": purchase_line,
        })
        picking.bill_ref = new_bill.name
        picking.bill_id = new_bill.id
        picking.bill_count = picking.bill_count + 1

