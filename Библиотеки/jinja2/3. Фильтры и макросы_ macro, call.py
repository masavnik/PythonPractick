from jinja2 import Template

# "sum" - Остальные фильтры можно найти в документации jinja
documentation = 'https://jinja.palletsprojects.com/en/2.11.x/templates/'


class Example:
    def __init__(self):
        self.cars = [
            {'model': 'Ауди', 'price': 23000},
            {'model': 'Шкода', 'price': 17300},
            {'model': 'Вольво', 'price': 44300},
            {'model': 'Вольксваген', 'price': 21300},
        ]

        self.person = [
            {'name': 'Алексей', 'old': 18, 'weight': 78.5},
            {'name': 'Николай', 'old': 28, 'weight': 82.3},
            {'name': 'Иван', 'old': 33, 'weight': 84.0},
        ]

    def conclusion_cars(self):
        tpl = "Суммарная сумма автомобилей {{ cs | sum(attribute='price') }}"
        tm = Template(tpl)
        msg = tm.render(cs=self.cars)
        return msg

    def conclusion_person(self):
        tpl = '''{%- for u in users -%}
                 {% filter upper %}{{u.name}}{% endfilter %}
                 {% endfor -%}'''
        tm = Template(tpl)
        msg = tm.render(users=self.person)
        return msg


ex = Example()
print(ex.conclusion_cars())
print(ex.conclusion_person())

