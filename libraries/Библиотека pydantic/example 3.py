from pydantic import BaseModel, Field


class City(BaseModel):
    city_id: int
    name: str = Field(alias='cityFullName')


intput_json = {
    'city_id': 1,
    'cityFullName': 'Moscow',
}

city = City.parse_obj(intput_json)
print(city.json())
print(city.json(by_alias=True,
                exclude={'city_id'}))
