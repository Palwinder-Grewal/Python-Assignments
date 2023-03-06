flow_1 = {
    "intent": "product_info",
    "entities": [
        {"entity": "product", "prompt": "can you please enter what are you searching ?"},
        {"entity": "location", "prompt": "Please enter your location ?"}
    ],
    "api_data": {
        "url": "https://rasatest.free.beeceptor.com/"
    }
}
flow_2 = {
    "intent": "ask_price",
    "entities": [
        {"entity": "product", "prompt": "can you please enter what are you searching ?"},
        {"entity": "location", "prompt": "Please enter your location ?"}
    ],
    "api_data": {
        "url": "https://rasatest.free.beeceptor.com/"
    }
}

flow_3 = {
    "intent": "ask_price",
    "entities": [
        {"entity": "order_id", "prompt": "Please enter your order id ?"}
    ],
    "api_data": {
        "url": "https://rasatest.free.beeceptor.com/"
    }
}