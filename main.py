from flask import Flask, request, render_template, url_for
from playwright.sync_api import sync_playwright

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/examples")
def examples():
    return render_template('examples.html')


@app.route("/render")
def render():
    url = request.args.get('url')
    print(url)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        content = page.content()
        data = {
            "info": url,
            "html": content,
        }
        browser.close()
    return data


if __name__ == "__main__":
    app.run('0.0.0.0', 8080, debug=True)
