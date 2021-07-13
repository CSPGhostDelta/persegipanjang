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
        sum = float(persegipanjang)
        sum2 = float(persegipanjang2)
        sum3 = sum * sum2
        sum4 = 2 * (sum + sum2)
        return render_template("persegipanjang.html", sum=sum3, sum2=sum4)
    else:
        return render_template("persegipanjang.html")

if __name__ == '__main__':
    aplikasi.run(debug=True)
