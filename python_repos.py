import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#Call API and store response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r=requests.get(url)
print("Status code:", r.status_code)

#store API response
response_dict = r.json()

#print result
print("Total 111repo: ", response_dict['total_count'])

#explor repo
repo_dicts = response_dict['items']

names=[]
stars=[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

#visualisation
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-starred Python Projects on GitHub'
chart.x_labels=names

chart.add('',stars)
chart.render_to_file('asdfsdf.svg')

