"""
Theme module for the Blue styles

https://htmlcolorcodes.com/color-chart/material-design-color-chart/
"""


class ThemeBlue(object):
  name = "blue"
  charts = ['#293342', '#334D6B', '#aabbee', '#6677bb', '#8B98E8', '#005566', '#269493', '#66bbaa', '#bbeeee', '#4e1c72',
            '#bb88ff', '#d1b3ff', '#d15f32', '#ffccaa', '#ffeebb', '#485d8c']
  colors = ["#e3f2fd", '#bbdefb', '#90caf9', '#64b5f6', '#42a5f5', '#2196f3', '#1e88e5', '#1976d2', '#1565c0', '#0d47a1']
  greys = ['#FFFFFF', '#f5f5f5', '#eeeeee', '#e0e0e0', '#bdbdbd', '#9e9e9e', '#757575', '#616161', '#424242', '#212121', '#000000']
  warning, danger, success = ('#FFF3CD', '#e2ac00'), ("#F8D7DA", "#C00000"), ('#e8f2ef', '#3bb194')


class ThemeBlueGrey(object):
  name = "blue-grey"
  charts = [
    '#009999', '#336699', '#ffdcb9',
    '#cc99ff', '#b3d9ff', '#ffff99',
    '#000066', '#b2dfdb', '#80cbc4',
    '#e8f5e9', '#c8e6c9', '#a5d6a7', # green
    '#ffebee', '#ffcdd2', '#ef9a9a', # red
    '#f3e5f5', '#e1bee7', '#ce93d8', # purple
    '#ede7f6', '#d1c4e9', '#b39ddb', # deep purple
    '#e8eaf6', '#c5cae9', '#9fa8da', # indigo
    '#fffde7', '#fff9c4', '#fff59d', # yellow
    '#fff3e0', '#ffe0b2', '#ffcc80', # orange
    '#efebe9', '#d7ccc8', '#bcaaa4', # brown
  ]
  colors = ['#eceff1', '#cfd8dc', '#b0bec5', '#90a4ae', '#78909c', '#607d8b', '#546e7a', '#455a64', '#37474f', '#263238']
  greys = ['#FFFFFF', '#f5f5f5', '#eeeeee', '#e0e0e0', '#bdbdbd', '#9e9e9e', '#757575', '#616161', '#424242', '#212121', '#000000']
  warning, danger, success = ('#FFF3CD', '#e2ac00'), ("#F8D7DA", "#C00000"), ('#e8f2ef', '#3bb194')


class ThemeLightBlue(object):
  name = "light blue"
  charts = [
    '#009999', '#336699', '#ffdcb9',
    '#cc99ff', '#b3d9ff', '#ffff99',
    '#000066', '#b2dfdb', '#80cbc4',
    '#e8f5e9', '#c8e6c9', '#a5d6a7', # green
    '#ffebee', '#ffcdd2', '#ef9a9a', # red
    '#f3e5f5', '#e1bee7', '#ce93d8', # purple
    '#ede7f6', '#d1c4e9', '#b39ddb', # deep purple
    '#e8eaf6', '#c5cae9', '#9fa8da', # indigo
    '#fffde7', '#fff9c4', '#fff59d', # yellow
    '#fff3e0', '#ffe0b2', '#ffcc80', # orange
    '#efebe9', '#d7ccc8', '#bcaaa4', # brown
  ]
  colors = ['#E1F5FE', '#B3E5FC', '#81D4FA', '#4FC3F7', '#29B6F6', '#03A9F4', '#039BE5', '#0288D1', '#0277BD', '#01579B']
  greys = ['#FFFFFF', '#f5f5f5', '#eeeeee', '#e0e0e0', '#bdbdbd', '#9e9e9e', '#757575', '#616161', '#424242', '#212121', '#000000']
  warning, danger, success = ('#FFF3CD', '#e2ac00'), ("#F8D7DA", "#C00000"), ('#e8f2ef', '#3bb194')
