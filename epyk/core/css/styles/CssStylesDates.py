"""
CSS Style module for the Dates components
"""


from epyk.core.css.styles import CssStyle


class CssDatePickerUI(CssStyle.CssCls):
  cssId = {"reference": ".ui-datepicker"}

  def customize(self, style, eventsStyles):
    style.update({"background": self.getColor('colors', 0)})

  @property
  def classname(self):
    return '.ui-datepicker'


class CssDatePicker(CssStyle.CssCls):
  attrs = {'font-size': '12px', 'font-family': 'Calibri', 'border': 'none', 'cursor': 'pointer', 'margin': '0',
           'padding': '2px', 'display': 'inline', 'border-radius': '5px', 'text-align': 'center'}
  focus = {'outline': 0}

  def customize(self, style, eventsStyles):
    style.update({"background": self.getColor('colors', 0), "color": self.getColor('greys', -1), 'border': '1px solid %s' % self.getColor('colors', 0)})
    eventsStyles['hover'].update({'color': self.getColor('colors', -1)})


class CssDatesTimePicker(CssStyle.CssCls):
  def customize(self, style, eventsStyles):
    style.update({'color': self.getColor('greys', -1), "background": self.getColor('colors', 0)})
