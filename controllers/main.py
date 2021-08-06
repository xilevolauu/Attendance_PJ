import odoo
import json
import logging

_logger = logging.getLogger(__name__)


class AttendanceAPI(odoo.http.Controller):
    @odoo.http.route('/foo', auth='public')
    def foo_handler(self):
        return "cao lòd"

    @odoo.http.route('/bar', auth='public')
    def bar_handler(self):
        return json.dumps({
            "content": "đây là api!"
        })
s