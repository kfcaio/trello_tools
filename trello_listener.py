from card_descriptor import set_description
from extractor import extract_infos_from_pdf
from flask import Flask
from flask import abort
from flask import request
from link_builder import get_wpp_url
from url_shortner import shorten_url


app = Flask(__name__)


@app.route('/listen', methods=['GET', 'POST'])
def listener():
    if request.method == 'GET':
        return 'OK, foi um GET', 200
    if request.method == 'HEAD':
        return '', 200
    if request.method == 'POST':
        if request.json['action']['type'] == 'addAttachmentToCard':
			card_id = request.json['action']['data']['card']['id']
			pdf_url = request.json['action']['data']['attachment']['url']
			pdf_info = extract_infos_from_pdf(pdf_url)
			wpp_url = get_zap_link(pdf_info)
			set_description(card_id, shortened_wpp_url)
		else:
			print('POST DIFERENTE')
        print(request.json)
        return '', 200


if __name__ == '__main__':
    app.run(debug=True)
