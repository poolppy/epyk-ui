"""
Module dedicated to wrap the Javascript Array

https://www.w3schools.com/jsref/jsref_obj_array.asp
"""

from epyk.core.js.primitives import JsObject
from epyk.core.js.fncs import JsFncs

from epyk.core.js import JsUtils


class JsArray(JsObject.JsObject):
  _jsClass = "Array"

  @property
  def length(self):
    """
    The length property of an array returns the length of an array (the number of array elements).

    Documentation:
    https://www.w3schools.com/JS/js_arrays.asp

    :return: A python Javascript Number
    """
    from epyk.core.js.primitives import JsNumber
    return JsNumber.JsNumber("%s.length" % self.varId, isPyData=False)


  # ------------------------------------------------------------------
  #                     ARRAY TRANSFORMATION FUNCTIONS
  #
  def some(self, jsFnc):
    """
    The some() method checks if any of the elements in an array pass a test (provided as a function).

    Example

    Documentation
    https://www.w3schools.com/jsref/jsref_some.asp

    :param jsFnc: function(currentValue, index, arr)	Required. A function to be run for each element in the array.

    :return: A Javascript Boolean
    """
    from epyk.core.js.primitives import JsBoolean

    return JsBoolean.JsBoolean("%s.some(%s)" % (self.varId, jsFnc), isPyData=False)

  def every(self, jsFncs, jsValue=None):
    """
    The every() method checks if all elements in an array pass a test (provided as a function).
    Data Structure used in this method is like obj(val, index, arra)

    Example

    Documentation
    https://www.w3schools.com/jsref/jsref_every.asp

    :param jsFncs: A function to be run for each element in the array
    :param jsValue: Optional. A value to be passed to the function to be used as its "this" value.

    :return: None
    """
    jsFncs = JsUtils.jsConvertFncs(jsFncs)
    if jsValue is None:
      return JsFncs.JsFunction("%s.every(function(val, index, arr){%s})" % (self.varId, ";".join(jsFncs)))

    return JsFncs.JsFunction("%s.every(function(val, index, arr){%s}, %s)" % (self.varId, ";".join(jsFncs), jsValue))

  def filter(self, jsFncs, jsValue=None):
    """
    The filter() method creates an array filled with all array elements that pass a test (provided as a function)

    Example

    Documentation
    https://www.w3schools.com/jsref/jsref_filter.asp

    :param jsFncs: A function to be run for each element in the array
    :param jsValue: Optional. A value to be passed to the function to be used as its "this" value.

    :return: None
    """
    jsFncs = JsUtils.jsConvertFncs(jsFncs)
    if jsValue is None:
      return JsFncs.JsFunction("%s.filter(function(val, index, arr){%s))" % (self.varId, ";".join(jsFncs)))

    return JsFncs.JsFunction("%s.filter(function(val, index, arr){%s), %s)" % (self.varId, ";".join(jsFncs), jsValue))

  def find(self, jsFnc):
    """
    The find() method returns the value of the first element in an array that pass a test (provided as a function)

    Example

    Documentation
    https://www.w3schools.com/jsref/jsref_find.asp

    :param jsFnc: function(currentValue, index, arr)	Required. A function to be run for each element in the array.

    :return: Returns the array element value if any of the elements in the array pass the test, otherwise it returns undefined
    """
    return "%s.find(%s)" % (self.varId, jsFnc)

  def findIndex(self, jsFnc):
    """
    The find() method returns the value of the first element in an array that pass a test (provided as a function)

    Example
    jsObj.console.log(jsObj.objects.array.get("MyArray").findIndex([
      jsObj.if_(jsObj.data.loop.val <= 0, [jsObj.return_(jsObj.objects.true)]),
      jsObj.return_(jsObj.objects.false)
    ]))

    Documentation
    https://www.w3schools.com/jsref/jsref_findindex.asp

    :param jsFnc: function(currentValue, index, arr)	Required. A function to be run for each element in the array.

    :return: Returns the array element index if any of the elements in the array pass the test, otherwise it returns -1
    """
    jsFnc = JsUtils.jsConvertFncs(jsFnc)
    return JsFncs.JsFunction("%s.findIndex(function(value, index, arr){%s})" % (self.varId, ";".join(jsFnc)))

  def forEach(self, jsFnc):
    """
    The forEach() method calls a provided function once for each element in an array, in order.

    Example
    jsObj.objects.get("MyObject").keys().forEach([
      jsObj.console.log(jsObj.data.loop.val)])

    Documentation
    https://www.w3schools.com/jsref/jsref_foreach.asp

    :param jsFnc: function(currentValue, index, arr)	Required. A function to be run for each element in the array.

    :return: Void, The Javascript String
    """
    jsFnc = JsUtils.jsConvertFncs(jsFnc)
    return JsFncs.JsFunction("%s.forEach(function(value, index, arr){%s})" % (self.varId, ";".join(jsFnc)))

  def map(self, jsFnc):
    """
    The map() method creates a new array with the results of calling a function for every array element.

    Example
    jsObj.console.log(jsObj.objects.array.get("MyArray").map([
      jsObj.data.loop.val * jsObj.math.max(jsObj.data.loop.arr.toArgs()),
      jsObj.return_(jsObj.data.loop.val)]))

    Documentation
    https://www.w3schools.com/jsref/jsref_map.asp

    :param jsFnc: function(currentValue, index, arr)	Required. A function to be run for each element in the array.

    :return: An Array containing the results of calling the provided function for each element in the original array.
    """
    jsFnc = JsUtils.jsConvertFncs(jsFnc)
    if self.varName is not None:
      return JsArray("%s = %s" % (self.varId, JsArray("%s.map(function(value, index, arr){%s; return value})" % (self.varId, ";".join(jsFnc)), isPyData=False)), isPyData=False)

    return JsArray("%s.map(function(value, index, arr){%s})" % (self.varId, ";".join(jsFnc)), isPyData=False)

  def sort(self, jsFnc=None):
    """
    The sort() method sorts an array alphabetically:

    Example
    jsObj.console.log(jsObj.objects.array.new([2, 5, 12, -3], "MyArray").shift()),
    jsObj.objects.array.get("MyArray").sort()

    Documentation
    https://www.w3schools.com/js/js_array_sort.asp

    :return: An Array object, representing the joined array
    """
    if jsFnc is not None:
      return JsArray("%s.sort(function(a, b){%s})" % (self.varId, jsFnc))

    return JsArray("%s.sort()" % self.varId, isPyData=False)

  def reduce(self, jsFnc):
    """
    The reduce() method reduces the array to a single value.

    Example
    jsObj.console.log(jsObj.objects.array.get("MyArray").reduce([
        jsObj.data.reduce.val + jsObj.data.reduce.rVal,
        jsObj.return_(jsObj.data.reduce.val)]))

    Documentation
    https://www.w3schools.com/jsref/jsref_reduce.asp

    :param jsFnc: The Javascript function used by the reduce method

    :return: A Python / Javascript Number
    """
    from epyk.core.js.primitives import JsNumber

    jsFnc = JsUtils.jsConvertFncs(jsFnc)
    return JsNumber.JsNumber("%s.reduce(function (r, o, i){%s})" % (self.varId, ";".join(jsFnc)))


  #------------------------------------------------------------------
  #             ARRAY TRANSFORMATION ON DATA
  #
  def shift(self):
    """
    The shift() method removes the first item of an array.

    Example
    jsObj.console.log(jsObj.objects.array.new([2, 5, 12, -3], "MyArray").shift()),
    jsObj.console.log(jsObj.objects.array.get("MyArray")),

    Documentation
    https://www.w3schools.com/jsref/jsref_shift.asp

    :return: Any type*, representing the removed array item. *An array item can be a string, a number, an array, a boolean, or any other object types that are allowed in an array.
    """
    return JsObject.JsObject("%s.shift()" % self.varId, isPyData=False)

  def slice(self, start, end):
    """
    The numbers in the table specify the first browser version that fully supports the method

    Example
    jsObj.objects.array.new([2, 5, 12, -3], "MyArray")
    jsObj.objects.array.get("MyArray").slice(3, 5)

    Documentation
    https://www.w3schools.com/jsref/jsref_slice_array.asp

    :param start: The index number in the array
    :param end: The index number in the array

    :return: A new Array, containing the selected elements
    """
    start = JsUtils.jsConvertData(start, None)
    end = JsUtils.jsConvertData(end, None)
    return JsArray("%s.slice(%s, %s)" % (self.varId, start, end), isPyData=False)

  def pop(self):
    """
    The pop() method removes the last element of an array, and returns that element.

    Example
    jsObj.objects.array.new([2, 5, 12, -3], "MyArray")
    jsObj.objects.array.get("MyArray").pop()

    Documentation:
    https://www.w3schools.com/js/js_array_methods.asp

    :return: Any type*, representing the removed array item. *An array item can be a string, a number, an array, a boolean, or any other object types that are allowed in an array.
    """
    return JsObject.JsObject("%s.pop()" % self.varId, isPyData=False)

  def delete(self, jsNumber):
    """
    Since JavaScript arrays are objects, elements can be deleted by using the JavaScript operator
    Using delete may leave undefined holes in the array. Use pop() or shift() instead.

    Example
    jsObj.objects.array.new([2, 5, 12, -3], "MyArray")
    jsObj.objects.array.get("MyArray").delete(2)

    Documentation:
    https://www.w3schools.com/js/js_array_methods.asp

    :param jsNumber: The index of the value in the array to be removed

    :return: Void, The Javascript String
    """
    jsNumber = JsUtils.jsConvertData(jsNumber, None)
    return JsFncs.JsFunction("delete %s[%s]" % (self.varId, jsNumber))

  def join(self, sep):
    """
    The join() method joins the elements of an array into a string, and returns the string.

    Example
    rptObj.js.array(varName="newUrl").join("&")

    Documentation
    https://www.w3schools.com/jsref/jsref_join.asp

    :param sep: Optional. The separator to be used. If omitted, the elements are separated with a comma
    :return: A String, representing the array values, separated by the specified separator
    """
    from epyk.core.js.primitives import JsString

    sep = JsUtils.jsConvertData(sep, None)
    return JsString.JsString("%s.join(%s)" % (self.varId, JsUtils.jsConvertData(sep, None)), isPyData=False)

  def copyWithin(self, start=0, end=None):
    """
    The copyWithin() method copies array elements within the array, to and from specified positions.

    Example
    jsObj.objects.array.new([2, 5, 12, -3], "MyArray")

    Documentation
    https://www.w3schools.com/jsref/jsref_copywithin.asp

    :param start: Optional. The index position to start copying elements from  (default is 0)
    :param end: Optional. The index position to stop copying elements from (default is array.length)

    :return: An Array, the changed array
    """
    if end is None:
      end = self.length
    return JsArray("%s.copyWithin(%s, %s)" % (self.varId, start, end), setVar=True, isPyData=False)

  def fill(self, jsData, start=0, end=None, jsFnc=None, jsObj=None):
    """
    The fill() method fills the specified elements in an array with a static value.
    The fill() method is not supported in Internet Explorer 11 and earlier versions.

    Example
    jsObj.objects.array.new([2, 5, 12, -3], "MyArray")
    jsObj.objects.array.get("MyArray").fill("test", 0, 2)

    Documentation
    https://www.w3schools.com/jsref/jsref_fill.asp

    :param jsData: Required. The value to fill the array with
    :param start: Optional. The index to start filling the array (default is 0)
    :param end: Optional. The index to stop filling the array (default is array.length)
    :param jsFnc:
    :param jsObj: Optional, The base Python Javascript object to add the polyfill

    :return: An Array, the changed array
    """
    if jsObj is not None:
      # Add a polyfill to ensure the browser compatibility
      jsObj._addImport("babel-polyfill")
    jsData = JsUtils.jsConvertData(jsData, jsFnc)
    if start is not None:
      start = JsUtils.jsConvertData(start, None)
      if end is not None:
        end = JsUtils.jsConvertData(end, None)
        return JsArray("%s.fill(%s, %s, %s)" % (self.varId, jsData, start, end), isPyData=False)
      else:
        return JsArray("%s.fill(%s, %s)" % (self.varId, jsData, start), isPyData=False)

    return JsArray("%s.fill(%s)" % (self.varId, jsData), isPyData=False)

  def concat(self, *args):
    """
    The concat() method is used to join two or more arrays.
    This method does not change the existing arrays, but returns a new array, containing the values of the joined arrays.

    Example
    jsObj.objects.array.new([2, 5, 12, -3], "MyArray"),
    jsObj.objects.array.new([3, -9, 2, -6], "MyArray2"),
    jsObj.objects.array.new([], "MyArray3"),
    jsObj.console.log(jsObj.objects.array.get("MyArray3").concat(jsObj.objects.array.get("MyArray"), jsObj.objects.array.get("MyArray2"))),

    Documentation
    https://www.w3schools.com/jsref/jsref_concat_array.asp

    :param args: Existing Javascript Arrays

    :return: An Array object, representing the joined array
    """
    return JsArray("%s.concat(%s)" % (self.varId, ", ".join([str(JsUtils.jsConvertData(a, None)) for a in args])), isPyData=False)

  def append(self, jsObj, val):
    """
    Equivalent to the append Python function for the Javascript

    Example
    jsObj.objects.array.new([2, 5, 12, -3], "MyArray")
    jsObj.objects.array.get("MyArray").append(jsObj, 34).append(jsObj, -47)

    Documentation
    https://www.w3schools.com/js/js_array_methods.asp
    https://www.w3schools.com/python/ref_list_append.asp

    :param jsObj: The Python Javascript base object
    :param val: The value to be added

    :return: The Python / Javascript Array
    """
    jsObj.extendProto(self, "append", [
      jsObj.objects.array.get("this").push(jsObj.objects.get("val")),
      jsObj.return_(jsObj.objects.array.get("this"))], pmts=["val"])
    return JsArray("%s.append(%s)" % (self.varId, JsUtils.jsConvertData(val, None)), isPyData=False)

  def push(self, *args):
    """
    The push() method adds new items to the end of an array, and returns the new length.

    Example
    jsObj.objects.array.new([2, 5, 12, -3], "MyArray")
    jsObj.objects.array.get("MyArray").push(55, -17)

    Documentation:
    https://www.w3schools.com/js/js_array_methods.asp

    :param args: A list of object to be added to the JsArray object

    :return: A Number, representing the new length of the array
    """
    from epyk.core.js.primitives import JsNumber

    return JsNumber.JsNumber("%s.push(%s)" % (self.varId, ", ".join([str(JsUtils.jsConvertData(a, None)) for a in args])), isPyData=False)

  def reverse(self):
    """
    The reverse() method reverses the elements in an array.

    Example
    jsObj.objects.array.new([2, 5, 12, -3], "MyArray")
    jsObj.objects.array.get("MyArray").reverse()

    Documentation:
    https://www.w3schools.com/js/js_array_sort.asp

    :return: An Array, representing the array after it has been reversed
    """
    return JsArray("%s.reverse()" % self.varId, isPyData=False)

  def unshift(self, *args):
    """
    The unshift() method adds a new element to an array (at the beginning), and "unshifts" older elements

    Example
    jsObj.objects.array.new([2, 5, 12, -3], "MyArray")
    jsObj.objects.array.get("MyArray").unshift(22)

    Documentation:
    https://www.w3schools.com/js/js_array_methods.asp

    :param args: Required. The item(s) to add to the beginning of the array

    :return: A Number, representing the new length of the array
    """
    return JsArray("%s.unshift(%s)" % (self.varId, ", ".join([str(JsUtils.jsConvertData(a, None)) for a in args])))

  def splice(self, i, j, jsData, jsFnc=None):
    """
    The splice() method can be used to add new items to an array
    With clever parameter setting, you can use splice() to remove elements without leaving "holes" in the array

    Example

    Documentation:
    https://www.w3schools.com/js/js_array_methods.asp

    :param i: Required. An integer that specifies at what position to add/remove items, Use negative values to specify the position from the end of the array
    :param j: Optional. The number of items to be removed. If set to 0, no items will be removed
    :param jsData: Optional. The new item(s) to be added to the array

    :return: A new Array, containing the removed items (if any)
    """
    jsData = JsUtils.jsConvert(jsData, jsFnc)
    return JsArray("%s.splice(%s, %s, %s)" % (self.varId, i, j, jsData))

  def __getitem__(self, index):
    return JsObject.JsObject("%s[%s]" % (self.varId, index))

  def unique(self, jsObj):
    """
    Prototype Extension

    Example
    jsObj.objects.array.new([2, 2, -3, -3], "MyArray")
    jsObj.objects.array.get("MyArray").unique()

    :param jsObj: The Python Javascript base object

    :return: A new Python Javascript Array with unique values
    """
    jsObj.extendProto(self, "unique", '''
      var arrayResult = [];this.forEach(function(item){
      if(arrayResult.indexOf(item) < 0){arrayResult.push(item)}}); return arrayResult''')
    return JsArray("%s.unique()" % self.varId)

  def contains(self, jsObj, data):
    """
    Prototype Extension

    Alternative to the includes function and compatible with all the browsers

    Example
    jsObj.objects.array.new([2, 2, -3, -3], "MyArray")
    jsObj.objects.array.get("MyArray").contains(2)

    :param jsObj: The Python Javascript base object
    :param data: The object to look for in the array

    :return: A Python Javascript boolean
    """
    from epyk.core.js.primitives import JsBoolean

    jsObj.extendProto(self, "contains", '''
      var i = this.length; while (i--){if (this[i] === obj){return true}}; return false
      ''', pmts=["data"])
    return JsBoolean.JsBoolean("%s.contains(%s)" % (self.varId, JsUtils.jsConvertData(data, None)), isPyData=False)

  def toArgs(self):
    return JsObject.JsObject("...%s" % self.varId)
