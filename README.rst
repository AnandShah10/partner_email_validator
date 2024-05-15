Partner Email Validation Module
===============================

Description
-----------

The Partner Email Validation module adds email validation functionality to the *res.partner* model in Odoo. It ensures that email addresses entered for partners adhere to standard email format validation rules. This enhancement helps maintain data integrity by preventing the storage of invalid or improperly formatted email addresses.

Installation
------------

1. Download the module from the repository.
2. Add the module to your Odoo addons directory.
3. Install the module from the Odoo Apps menu.
4. Restart the Odoo server if necessary.

Usage
-----

1. Navigate to the Contacts module and open a partner/contact record.
2. Enter an email address in the "Email" field.
3. If the entered email address does not adhere to standard email format validation rules, an error message will be displayed, prompting the user to correct the email address.
4. Once a valid email address is entered, it will be saved successfully.

Notes
-----

- This module improves data quality and reliability by enforcing email address validation for partner records.
- Users are guided to enter valid email addresses through informative error messages, enhancing the user experience.
- Administrators can customize email validation rules as needed to accommodate specific business requirements.

Contributing
------------

Contributions to this module are welcome. Please submit any bug reports, feature requests, or pull requests to the repository.

License
-------

This module is licensed under the GPL-3 license. See the LICENSE file for more details.
