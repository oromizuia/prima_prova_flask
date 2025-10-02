from flask import Flask, request, render_template_string
from flask_cors import CORS
import smtplib
import ssl
from email.message import EmailMessage
import os

app = Flask(__name__)
CORS(app)

HTML_FORM = """
<form method="post">
  <label>Nome e Cognome</label>
  <input type="text" name="nome" required><br>
  <label>Email</label>
  <input type="email" name="email" required><br>
  <label>Messaggio</label>
  <textarea name="messaggio" required></textarea><br>
  <button type="submit">Invia</button>
</form>
"""

@app.route('/', methods=['GET', 'POST'])
def send_mail():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        messaggio = request.form['messaggio']

        msg = EmailMessage()
        msg['Subject'] = 'Nuovo messaggio dal sito'
        msg['From'] = 'tuoindirizzo@email.it'
        msg['To'] = 'olivieri.giulio.b@gmail.com'
        msg.set_content(f"Nome: {nome}\nEmail: {email}\nMessaggio:\n{messaggio}")

        # Configura il server SMTP (esempio con Gmail)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            
            smtp.login("ernesto.romita@gmail.com", "zrqc dvgs sswq aygi")
            smtp.send_message(msg)
        return "Email inviata!"
    return render_template_string(HTML_FORM)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
