Activation is automatic, custom format mask is hard coded in ``models/custom_format_coupon.py`` for now.

Coupon codes are generated from this mask where 
``x`` is replaced with a random lowercase letter, 
``X`` is replaced with a random uppercase letter,
``0`` is replaced with a random digit. 
All other characters are left intact.
