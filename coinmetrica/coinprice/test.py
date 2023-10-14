from jinja2 import Template

name = 'ppp'

qqq = Template('hi {{ name.upper() }}').render(name=name)

print(qqq)