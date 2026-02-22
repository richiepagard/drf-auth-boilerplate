SPECTACULAR_SETTINGS = {
    'TITLE': 'Django REST Framework Auth Boilerplate',
    'DESCRIPTION': 'A boilerplate for authentication in Django Rest Framework with JWT support.',
    # Version configs
    'VERSION': '1.7.4',

    'SERVE_INCLUDE_SCHEMA': False,
    # Contact options
    'CONTACT': {
        'name': 'Richie Pagard',
        'email': 'richiepagard@gmail.com',
        'url': 'https://github.com/richiepagard'
    },

    # Customize Swagger UI
    "SWAGGER_UI_SETTINGS":
    """{
        deepLinking: true,
        displayOperationId: true,
        persistAuthorization: true,
        presets: [SwaggerUIBundle.presets.apis, SwaggerUIStandalonePreset],
        layout: "StandaloneLayout",
    }""",
}
