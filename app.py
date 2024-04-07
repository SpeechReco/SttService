from flask import Flask
import assemblyai as aai

app = Flask(__name__)

aai.settings.api_key = "17d12fa0b5fd4ead94732c894bca89f8"


@app.route('/transcribe-recording')
def transcribe():
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe("https://storage.googleapis.com/speechrec-b38d7.appspot.com/4?GoogleAccessId=firebase-adminsdk-l42lb@speechrec-b38d7.iam.gserviceaccount.com&Expires=1722432175&Signature=BWPb1GB0uGm5sL4yPfq5eTVO3E4yfCFUgKN4agTkeKLMCvdqdyTJiwAvgqMFabewGVu9f20BuQ5oEkhTn0xem88QSwMorK9A6tlxTAgVh2D47thDUlmY%2BQZww37FjnlH4SEKJmCQ%2FOkm7OKD49No%2F7FWpAdpXOTU4GaKRoHN31f42dfR0I3CMhimaxyXEDJhoJJIMKEZU4SpHk7IBKU%2BgNtpGxaHap2zxnkh3kcK1cnLf%2FJpDDtbRxLdOXJvkK%2BTgwuyxgwSPkfed6hLCFuucrha1c7Q%2Fodh0L%2FXGy1%2BQzXUGWvce1vrFzkrk92WvYvUg4wD3xAw0h0dkYHhSZfKtw%3D%3D")
    return transcript.text

if __name__ == '__main__':
    app.run()
