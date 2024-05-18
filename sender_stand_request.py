import Confic
import requests
import data


def post_new_order(body):
    return requests.post(Confic.URL_SERVICE + Confic.CREATE_ORDERS_PATH,
                         json=body,
                         headers=data.headers)

def get_order_from_track(track):
    return requests.get(Confic.URL_SERVICE + Confic.FIND_ORDER_FROM_TRACK_PATH + str(track),
                        headers=data.headers)

def assertion_code_200():
	response_new_order = post_new_order(data.order_body)
	track = response_new_order.json()["track"]
	return get_order_from_track(track).status_code


def test_get_order_from_track_code_200():
	assert assertion_code_200() == data.status_code_200

