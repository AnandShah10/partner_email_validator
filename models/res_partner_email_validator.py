from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError
import re


class EmailValidator(models.Model):
    _inherit = 'res.partner'

    _sql_constraints = [
        ('unique_email', 'UNIQUE (email)', 'Email must be unique!')
    ]

    @api.constrains('email')
    def _validate_email(self):
        for i in self:
            if i.email:  # if Doctor email Field is not empty
                pd = re.fullmatch(r'^[a-zA-Z0-9]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', str(i.email))
                print(i.email)
                if pd is None:  # if Not Valid Email
                    raise ValidationError(_("Email is not valid!"))
