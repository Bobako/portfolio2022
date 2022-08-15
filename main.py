from sweater import app, config

if __name__ == '__main__':
    app.run(port=int(config["SITE"]["port"]))
