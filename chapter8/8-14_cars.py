def car_info_creator(manufacturer, model, **keywords):
    car_info = {}
    car_info["manufacturer"] = manufacturer
    car_info["model"] = model
    for key, value in keywords.items():
        car_info[key] = value
    return car_info

my_car = car_info_creator("bentley", "continental GT", color="dark gray", tow_package=True)
print(my_car)