from flask import Flask, render_template, request, send_file
import qrcode

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    qrfile = None

    if request.method == 'POST':
        name = request.form.get('name')
        phone = int(request.form.get('phone'))
        email = request.form.get('email')
        link = request.form.get('link')
        data = f"Name: {name},\nPhone:{phone}, \nEmail:{email}, \nLink:{link}"

        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save('static/my_qr.png')
        qrfile = 'static/my_qr.png'

    if request.args.get('download'):
        image_path = 'static/my_qr.png'
        return send_file(image_path, as_attachment=True)

    return render_template('index.html', qrfile=qrfile)

if __name__ == '__main__':
    app.run(debug=True)
