from flask import Flask, render_template, request

aplikasi = Flask(__name__)

@aplikasi.route("/")
def app():
    return render_template("persegipanjang.html")

@aplikasi.route("/send", methods=["POST"])
def send(sum=sum):
    if request.method == "POST":
        persegipanjang = request.form["persegipanjang"]
        persegipanjang2= request.form["persegipanjang2"]
        sum = float(persegipanjang) * 2
        sum2 = float(persegipanjang2) * 3
        return render_template("persegipanjang.html", sum=sum, sum2=sum2)
    else:
        return render_template("persegipanjang.html")

if __name__ == '__main__':
    aplikasi.run(debug=True)
