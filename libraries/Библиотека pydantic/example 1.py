from pydantic import BaseModel


class City(BaseModel):
    city_id: int
    name: str
    population: int


intput_json = {
    'city_id': 1,
    'name': 'Moscow',
    'population': 16543222
}

intput_json2 = {
    'city_id': 2,
    'name': 'Moscows',
    'population': 1654322
}


city = City.parse_obj(intput_json)

print(city.city_id)
print(city.name)
print(city.population)