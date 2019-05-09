import os
import urllib


def get_wpp_url(pdf_info):
	msg = os.environ['WPP_MSG'].format(pdf_info['full_name'], pdf_info['insurer'])
	msg = urllib.parse.quote(msg)
	link = 'https://api.whatsapp.com/send?phone={}&text={}'.format(pdf_info['tel'], msg)

	return link