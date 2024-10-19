from pydantic import BaseModel


class Tag(BaseModel):
    id: int
    tag: str


class City(BaseModel):
    city_id: int
    name: str
    tags: list[Tag]


intput_json = {
    'city_id': 1,
    'name': 'Moscow',
    'tags': [
        {
            'id': 1, 'tag': 'capital'
        },
        {
            'id': 2, 'tag': 'big city'
        }
    ]
}

city = City.parse_obj(intput_json)

for i in city.tags:
    print(i.tag, i.id)
print()

print(city.tags[0].tag)
print(city.tags[1].tag)
print()

tag = city.tags[1]
print(tag.json())
