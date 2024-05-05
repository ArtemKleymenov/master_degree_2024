#!/usr/bin/env python3

import connexion
from threading import Thread
from facial_service import run_fr_service
from swagger_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    t = Thread(target=run_fr_service, daemon=True)
    t.start()
    app.add_api('swagger.yaml', arguments={'title': 'Face Recognition Service - OpenAPI 3.0'}, pythonic_params=True)
    app.run(port=8080)


if __name__ == '__main__':
    main()
