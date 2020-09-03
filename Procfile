release: flask db upgrade
web: gunicorn flask_dash_template.app:create_app\(\) -b 0.0.0.0:$PORT -w 3
