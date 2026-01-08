from flask import Flask, request, jsonify
import enviar_email

app = Flask(__name__)


@app.route("/enviar", methods=["POST"])
def enviar():
    dados = request.get_json()

    if not dados or "email" not in dados:
        return jsonify({"erro": "Email não informado"}), 400

    try:
        enviar_email.enviar(dados["email"])
    except ValueError as erro:
        return jsonify({"erro": str(erro)}), 400
    except Exception:
        return jsonify({"erro": "Erro interno no servidor"}), 500

    return jsonify({"status": "Email enviado com sucesso!"}), 200


if __name__ == "__main__":
    app.run(debug=True)
