# -*- coding: utf-8 -*-
# Copyright 2018 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
{
    "name": """REST API / Open API (Swagger)""",
    "summary": """Set up API and export OpenAPI specification file for integration with whatever system you need""",
    "category": "",
    "images": [],
    "version": "8.0.1.0.0",
    "application": False,

    "author": "IT-Projects LLC, Ivan Yelizariev",
    "support": "apps@it-projects.info",
    "website": "https://it-projects.info/team/yelizariev",
    "license": "LGPL-3",

    "depends": [
    ],
    "external_dependencies": {"python": ['bravado_core', 'swagger_spec_validator'], "bin": []},
    "data": [
        # "security/ir.model.access.csv",
        # "views/assets.xml",
        # "views/openapi_view.xml",
        # "views/res_users_view.xml",
        # "views/ir_model_view.xml",
    ],
    "demo": [
        # "views/assets_demo.xml",
        # "data/openapi_demo.xml",
    ],
    "qweb": [
    ],

    "auto_install": False,
    "installable": True,
}
