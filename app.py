from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

# 🔥 Level 1: Open Redirect using next parameter
@app.route('/level1')
def level1():
    next_url = request.args.get('next', '/')
    if 'evil.com' in next_url:
        return "🚫 Bypassing Failed! 'evil.com' is blocked."
    return redirect(next_url)

# 🔥 Level 2: Open Redirect with :// restriction
@app.route('/level2')
def level2():
    next_url = request.args.get('next', '/')
    if '://' in next_url:
        return "🚫 Bypassing Failed! '://' is blocked."
    return redirect(f"https://example.com/{next_url}")

# 🔥 Level 3: Open Redirect with http and https restrictions
@app.route('/level3')
def level3():
    next_url = request.args.get('next', '/')
    if next_url.startswith('http') or '://' in next_url:
        return "🚫 Bypassing Failed! 'http' & 'https' are blocked."
    return redirect(next_url)

# 🔥 Level 4: Open Redirect with .com restriction
@app.route('/level4')
def level4():
    next_url = request.args.get('next', '/')
    if '.com' in next_url:
        return "🚫 Bypassing Failed! '.com' is blocked."
    return redirect(f"https://example{next_url}")

# 🔥 Level 5: Open Redirect in OAuth using redirect_uri
@app.route('/level5')
def level5():
    redirect_uri = request.args.get('redirect_uri', '/')
    if not redirect_uri.startswith('https://trusted-site.com'):
        return "🚫 Bypassing Failed! Only 'trusted-site.com' is allowed."
    return redirect(redirect_uri)

# 🛠 Help Page with Notion Reference
@app.route('/help')
def help_page():
    return render_template_string("""
        <h1>🛠 Open Redirect Challenge Help</h1>
        <p>Want to learn more about Open Redirect vulnerabilities and how to exploit or prevent them?</p>
        <p>Check out this guide: <a href="https://www.notion.so/Open-redirect-148abcd05dff80b9bedede0a616614d6?pvs=4#1acabcd05dff80009a7af5b3540dd8f9" target="_blank">Open Redirect Guide</a></p>
        <p>Return to the <a href="/">challenge menu</a>.</p>
    """)

# 🛠 Home Page (Challenge Menu)
@app.route('/')
def home():
    return render_template_string("""
        <h1>🔥 Open Redirect Challenge 🔥</h1>
        <p>Find a way to bypass the Open Redirect filters in each level!</p>
        <ul>
            <li><a href='/level1?next=https://evil.com'>Level 1</a></li>
            <li><a href='/level2?next=https%3A%2F%2Fevil.com'>Level 2</a></li>
            <li><a href='/level3?next=http://evil.com'>Level 3</a></li>
            <li><a href='/level4?next=/evil.com'>Level 4</a></li>
            <li><a href='/level5?redirect_uri=https://evil.com'>Level 5 (OAuth)</a></li>
        </ul>
        <p>🚀 Try to bypass them using different techniques!</p>
        <p>Need help? Check out the <a href="/help">Open Redirect Guide</a>.</p>
    """)

if __name__ == '__main__':
    app.run(debug=True)
