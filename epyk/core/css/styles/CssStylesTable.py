"""
CSS Style module for the Table components
"""


from epyk.core.css.styles import CssStyle


class CssDataTable(CssStyle.CssCls):
  attrs = {'border-collapse': 'collapse !IMPORTANT'}

  def customize(self, style, eventsStyles):
    style.update({'border': "1px solid %s !IMPORTANT" % self.getColor('greys', 3)})
    eventsStyles['hover'].update({'border': "1px solid %s !IMPORTANT" % self.getColor('success', 1)})


class CssDataTableHeader(CssStyle.CssCls):
  cssId = {'child': 'thead'}

  def customize(self, style, eventsStyles):
    style.update({'color': self.getColor('greys', 0), "background": self.getColor('greys', -1), 'white-space': 'nowrap'})


class CssDataTableFooter(CssStyle.CssCls):
  @property
  def classname(self): return 'paginate_button'

  def customize(self, style, eventsStyles):
    style.update({"color": "red !IMPORTANT", 'background-color': "%s !IMPORTANT" % self.getColor("colors", 2)})


class CssDataTableEven(CssStyle.CssCls):
  cssId = {'child': 'tbody tr:nth-child(even)'}

  def customize(self, style, eventsStyles):
    style.update({'color': self.getColor('greys', -1), 'background-color': self.getColor('greys', 0), 'border-top': "1px solid %s !IMPORTANT" % self.getColor('greys', 0)})
    eventsStyles['hover'].update({'border': "1px solid %s !IMPORTANT" % self.getColor('success', 1), 'color': self.getColor('greys', -1), 'background-color': self.getColor('colors', 3)})


class CssDataTableOdd(CssStyle.CssCls):
  cssId = {'child': 'tbody tr:nth-child(odd)'}

  def customize(self, style, eventsStyles):
    style.update({'color': self.getColor('greys', -1), 'background-color': self.getColor('colors', 1), 'border-top': "1px solid %s !IMPORTANT" % self.getColor('colors', 1)})
    eventsStyles['hover'].update({'border': "1px solid %s !IMPORTANT" % self.getColor('success', 1), 'color': self.getColor('greys', -1), 'background-color': self.getColor('colors', 3)})


class CssTableBasic(CssStyle.CssCls):
  attrs = {'margin': '5px', 'border-collapse': 'collapse'}


class CssTableColumnSystem(CssStyle.CssCls):
  attrs = {'margin': '5px', 'text-align': 'left', 'font-weight': 'bold'}


class CssTableColumnFixed(CssStyle.CssCls):
  attrs = {'margin': '5px', 'text-align': 'left', 'font-weight': 'bold'}


class CssTableNewRow(CssStyle.CssCls):
  attrs = {'color': '#546472'}


class CssTableSelected(CssStyle.CssCls):
  attrs = {'background-color': '#AEDAF8!important'}


class CssCellComment(CssStyle.CssCls):
  attrs = {'margin': '0!important', 'padding': '2px 0 0 2px!important'}


class CssCellSave(CssStyle.CssCls):
  attrs = {'color': '#293846!important'}


class CssTdEditor(CssStyle.CssCls):
  attrs = {'border-width': '1px', 'border-style': 'solid', 'text-align': 'left', 'height': '30px', 'padding': '5px', 'vertical-align': 'middle'}

  def customize(self, style, eventsStyles):
    style.update({"color": self.getColor('colors', 5), 'border-color': self.getColor('greys', 5)})


class CssTdDetails(CssStyle.CssCls):
  before = {'content': "'\\f0fe'", 'font-family': "'Font Awesome 5 Free'", 'cursor': 'pointer', 'padding': '0 5px 0 0'}
  cssId = {'child': 'td'}


class CssTdDetailsShown(CssStyle.CssCls):
  before = {'content': "'\\f146'", 'font-family': "'Font Awesome 5 Free'", 'cursor': 'pointer', 'padding': '0 5px 0 0'}
  cssId = {'child': 'td'}
