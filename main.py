from groq import Groq
from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

AI_KEY = "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"

client = Groq(api_key=AI_KEY)

def ai_call(year):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"berikan saya 1 fakta menarik seputar teknologi di tahun {year}",
                }
            ],
            model = "llama-3.2-1b-preview",
            stream = False
        )
        ai_output = chat_completion.choices[0].message.content
        return ai_output
    
    except Exception:
        return f"Maaf Lag"

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/usia', methods=['GET', 'POST'])
def cek_usia():
    if request.method == 'POST':
        # Ambil data dari form
        tahun_lahir = int(request.form['tahun_lahir'])
        tahun_sekarang = datetime.now().year
        usia = tahun_sekarang - tahun_lahir
        ai_output = ai_call(tahun_lahir)
        # print(ai_output)
        return render_template('cek_usia.html', usia=usia, tahun_lahir=tahun_lahir, ai_output=ai_output)
    return render_template('cek_usia.html', usia= None)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0')
