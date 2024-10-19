from jinja2 import Template

# Example 1
cities = [{'id': 1, 'city': 'Москва'},
          {'id': 5, 'city': 'Тверь'},
          {'id': 7, 'city': 'Минск'},
          {'id': 8, 'city': 'Смоленск'},
          {'id': 11, 'city': 'Калуга'}]

link = '''<select name="cities">
{% for i in c -%}
    <option value="{{i["id"]}}">{{i["city"]}}</option>
{% endfor -%}
</select>'''
# {% for i in c -%} если убрать - то добавятся пустые строчки
tm = Template(link)
msg = tm.render(c=cities)
print(msg)
print()
# Example 2

citiess = [{'id': 1, 'city': 'Москва'},
          {'id': 5, 'city': 'Тверь'},
          {'id': 7, 'city': 'Минск'},
          {'id': 8, 'city': 'Смоленск'},
          {'id': 11, 'city': 'Калуга'}]

link = '''<select name="cities">
{% for i in c -%}
{% if i.id > 6 -%}
    <option value="{{i["id"]}}">{{i["city"]}}</option>
{% elif i.city == "Москва" -%}
    <option>{{ i["city"] }}</option>
{% else -%}
    {{i["city"]}}
{% endif -%}
{% endfor -%}
</select>'''
# {% for i in c -%} если убрать - то добавятся пустые строчки
tmm = Template(link)
msgg = tmm.render(c=citiess)
print(msgg)