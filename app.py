from flask import Flask, request, jsonify
from module import upload_decode_s3, insert_rds

app = Flask(__name__)


@app.route('/post', methods=['Post'])
def fun_main():
    info = request.get_json()

    info_1 = upload_decode_s3.fun_upload(info)
    info_2 = insert_rds.insert_rds(info_1)

    return jsonify(info_2)


if __name__ == '__main__':
    app.run(debug=True)

