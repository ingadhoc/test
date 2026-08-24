from odoo import fields, models


class ResUsers(models.Model):
    _inherit = "res.users"

    send_message_delay = fields.Integer(
        string="Send Message Delay",
        help="Seconds the composer waits before sending a message, so the author can still edit it.",
    )

    @property
    def SELF_READABLE_FIELDS(self):
        return super().SELF_READABLE_FIELDS + ["send_message_delay"]

    @property
    def SELF_WRITEABLE_FIELDS(self):
        return super().SELF_WRITEABLE_FIELDS + ["send_message_delay"]
