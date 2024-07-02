import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366', base_style=LCS) 
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False) 
chart.title = 'Python Projects' 
chart.x_labels = ['public-apis', 'system-design-primer', 'awesome-python']
plot_dicts = [{'value': 297115, 'label': 'Description of public-apis.'}, 
              {'value': 262416, 'label': 'Description of system-design-primer.'}, 
              {'value': 211224, 'label': 'Description of awesome-python.'}, ]
chart.add('', plot_dicts) 
chart.render_in_browser()