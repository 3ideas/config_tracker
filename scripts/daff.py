#!/usr/bin/env python
import sys

import math as python_lib_Math
import math as Math
from os import path as python_lib_os_Path
import inspect as python_lib_Inspect
import sys as python_lib_Sys
import builtins as python_lib_Builtins
import functools as python_lib_Functools
import json as python_lib_Json
import os as python_lib_Os
import subprocess as python_lib_Subprocess
import traceback as python_lib_Traceback
from datetime import datetime as python_lib_datetime_Datetime
from datetime import timezone as python_lib_datetime_Timezone
from io import StringIO as python_lib_io_StringIO


class _hx_AnonObject:
    _hx_disable_getattr = False
    def __init__(self, fields):
        self.__dict__ = fields
    def __repr__(self):
        return repr(self.__dict__)
    def __contains__(self, item):
        return item in self.__dict__
    def __getitem__(self, item):
        return self.__dict__[item]
    def __getattr__(self, name):
        if (self._hx_disable_getattr):
            raise AttributeError('field does not exist')
        else:
            return None
    def _hx_hasattr(self,field):
        self._hx_disable_getattr = True
        try:
            getattr(self, field)
            self._hx_disable_getattr = False
            return True
        except AttributeError:
            self._hx_disable_getattr = False
            return False



class Enum:
    _hx_class_name = "Enum"
    __slots__ = ("tag", "index", "params")
    _hx_fields = ["tag", "index", "params"]
    _hx_methods = ["__str__"]

    def __init__(self,tag,index,params):
        self.tag = tag
        self.index = index
        self.params = params

    def __str__(self):
        if (self.params is None):
            return self.tag
        else:
            return self.tag + '(' + (', '.join(str(v) for v in self.params)) + ')'

Enum._hx_class = Enum


class Alignment:
    _hx_class_name = "Alignment"
    __slots__ = ("map_a2b", "map_b2a", "ha", "hb", "ta", "tb", "ia", "ib", "map_count", "order_cache", "order_cache_has_reference", "index_columns", "marked_as_identical", "reference", "meta", "comp", "has_addition", "has_removal")
    _hx_fields = ["map_a2b", "map_b2a", "ha", "hb", "ta", "tb", "ia", "ib", "map_count", "order_cache", "order_cache_has_reference", "index_columns", "marked_as_identical", "reference", "meta", "comp", "has_addition", "has_removal"]
    _hx_methods = ["range", "tables", "headers", "setRowlike", "link", "addIndexColumns", "getIndexColumns", "a2b", "b2a", "count", "toString", "toOrder", "addToOrder", "getSource", "getTarget", "getSourceHeader", "getTargetHeader", "toOrder3", "markIdentical", "isMarkedAsIdentical"]

    def __init__(self):
        self.has_removal = None
        self.has_addition = None
        self.index_columns = None
        self.order_cache = None
        self.tb = None
        self.ta = None
        self.map_a2b = haxe_ds_IntMap()
        self.map_b2a = haxe_ds_IntMap()
        def _hx_local_0():
            self.hb = 0
            return self.hb
        self.ha = _hx_local_0()
        self.map_count = 0
        self.reference = None
        self.meta = None
        self.comp = None
        self.order_cache_has_reference = False
        self.ia = -1
        self.ib = -1
        self.marked_as_identical = False

    def range(self,ha,hb):
        self.ha = ha
        self.hb = hb

    def tables(self,ta,tb):
        self.ta = ta
        self.tb = tb

    def headers(self,ia,ib):
        self.ia = ia
        self.ib = ib

    def setRowlike(self,flag):
        pass

    def link(self,a,b):
        if (a != -1):
            self.map_a2b.set(a,b)
        else:
            self.has_addition = True
        if (b != -1):
            self.map_b2a.set(b,a)
        else:
            self.has_removal = True
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0.map_count
        _hx_local_0.map_count = (_hx_local_1 + 1)
        _hx_local_1

    def addIndexColumns(self,unit):
        if (self.index_columns is None):
            self.index_columns = list()
        _this = self.index_columns
        _this.append(unit)

    def getIndexColumns(self):
        return self.index_columns

    def a2b(self,a):
        return self.map_a2b.h.get(a,None)

    def b2a(self,b):
        return self.map_b2a.h.get(b,None)

    def count(self):
        return self.map_count

    def toString(self):
        result = ((("" + HxOverrides.stringOrNull((("null" if ((self.map_a2b is None)) else self.map_a2b.toString())))) + " // ") + HxOverrides.stringOrNull((("null" if ((self.map_b2a is None)) else self.map_b2a.toString()))))
        if (self.reference is not None):
            result = (("null" if result is None else result) + (((" (" + Std.string(self.reference)) + ")")))
        return result

    def toOrder(self):
        if (self.order_cache is not None):
            if (self.reference is not None):
                if (not self.order_cache_has_reference):
                    self.order_cache = None
        if (self.order_cache is None):
            self.order_cache = self.toOrder3()
        if (self.reference is not None):
            self.order_cache_has_reference = True
        return self.order_cache

    def addToOrder(self,l,r,p = None):
        if (p is None):
            p = -2
        if (self.order_cache is None):
            self.order_cache = Ordering()
        self.order_cache.add(l,r,p)
        self.order_cache_has_reference = (p != -2)

    def getSource(self):
        return self.ta

    def getTarget(self):
        return self.tb

    def getSourceHeader(self):
        return self.ia

    def getTargetHeader(self):
        return self.ib

    def toOrder3(self):
        order = list()
        if (self.reference is None):
            k = self.map_a2b.keys()
            while k.hasNext():
                k1 = k.next()
                unit = Unit()
                unit.l = k1
                unit.r = self.a2b(k1)
                order.append(unit)
            k = self.map_b2a.keys()
            while k.hasNext():
                k1 = k.next()
                if (self.b2a(k1) == -1):
                    unit = Unit()
                    unit.l = -1
                    unit.r = k1
                    order.append(unit)
        else:
            k = self.map_a2b.keys()
            while k.hasNext():
                k1 = k.next()
                unit = Unit()
                unit.p = k1
                unit.l = self.reference.a2b(k1)
                unit.r = self.a2b(k1)
                order.append(unit)
            k = self.reference.map_b2a.keys()
            while k.hasNext():
                k1 = k.next()
                if (self.reference.b2a(k1) == -1):
                    unit = Unit()
                    unit.p = -1
                    unit.l = k1
                    unit.r = -1
                    order.append(unit)
            k = self.map_b2a.keys()
            while k.hasNext():
                k1 = k.next()
                if (self.b2a(k1) == -1):
                    unit = Unit()
                    unit.p = -1
                    unit.l = -1
                    unit.r = k1
                    order.append(unit)
        top = len(order)
        remotes = list()
        locals = list()
        _g = 0
        _g1 = top
        while (_g < _g1):
            o = _g
            _g = (_g + 1)
            if ((order[o] if o >= 0 and o < len(order) else None).r >= 0):
                remotes.append(o)
            else:
                locals.append(o)
        def _hx_local_0(a,b):
            return ((order[a] if a >= 0 and a < len(order) else None).r - (order[b] if b >= 0 and b < len(order) else None).r)
        remote_sort = _hx_local_0
        def _hx_local_1(a,b):
            if (a == b):
                return 0
            if (((order[a] if a >= 0 and a < len(order) else None).l >= 0) and (((order[b] if b >= 0 and b < len(order) else None).l >= 0))):
                return ((order[a] if a >= 0 and a < len(order) else None).l - (order[b] if b >= 0 and b < len(order) else None).l)
            if ((order[a] if a >= 0 and a < len(order) else None).l >= 0):
                return 1
            if ((order[b] if b >= 0 and b < len(order) else None).l >= 0):
                return -1
            return (a - b)
        local_sort = _hx_local_1
        if (self.reference is not None):
            def _hx_local_2(a,b):
                if (a == b):
                    return 0
                o1 = ((order[a] if a >= 0 and a < len(order) else None).r - (order[b] if b >= 0 and b < len(order) else None).r)
                if (((order[a] if a >= 0 and a < len(order) else None).p >= 0) and (((order[b] if b >= 0 and b < len(order) else None).p >= 0))):
                    o2 = ((order[a] if a >= 0 and a < len(order) else None).p - (order[b] if b >= 0 and b < len(order) else None).p)
                    if ((o1 * o2) < 0):
                        return o1
                    o3 = ((order[a] if a >= 0 and a < len(order) else None).l - (order[b] if b >= 0 and b < len(order) else None).l)
                    return o3
                return o1
            remote_sort = _hx_local_2
            def _hx_local_3(a,b):
                if (a == b):
                    return 0
                if (((order[a] if a >= 0 and a < len(order) else None).l >= 0) and (((order[b] if b >= 0 and b < len(order) else None).l >= 0))):
                    o1 = ((order[a] if a >= 0 and a < len(order) else None).l - (order[b] if b >= 0 and b < len(order) else None).l)
                    if (((order[a] if a >= 0 and a < len(order) else None).p >= 0) and (((order[b] if b >= 0 and b < len(order) else None).p >= 0))):
                        o2 = ((order[a] if a >= 0 and a < len(order) else None).p - (order[b] if b >= 0 and b < len(order) else None).p)
                        if ((o1 * o2) < 0):
                            return o1
                        return o2
                if ((order[a] if a >= 0 and a < len(order) else None).l >= 0):
                    return 1
                if ((order[b] if b >= 0 and b < len(order) else None).l >= 0):
                    return -1
                return (a - b)
            local_sort = _hx_local_3
        remotes.sort(key= python_lib_Functools.cmp_to_key(remote_sort))
        locals.sort(key= python_lib_Functools.cmp_to_key(local_sort))
        revised_order = list()
        at_r = 0
        at_l = 0
        _g = 0
        _g1 = top
        while (_g < _g1):
            o = _g
            _g = (_g + 1)
            if ((at_r < len(remotes)) and ((at_l < len(locals)))):
                ur = python_internal_ArrayImpl._get(order, (remotes[at_r] if at_r >= 0 and at_r < len(remotes) else None))
                ul = python_internal_ArrayImpl._get(order, (locals[at_l] if at_l >= 0 and at_l < len(locals) else None))
                if (((ul.l == -1) and ((ul.p >= 0))) and ((ur.p >= 0))):
                    if (ur.p > ul.p):
                        revised_order.append(ul)
                        at_l = (at_l + 1)
                        continue
                elif (ur.l > ul.l):
                    revised_order.append(ul)
                    at_l = (at_l + 1)
                    continue
                revised_order.append(ur)
                at_r = (at_r + 1)
                continue
            if (at_r < len(remotes)):
                ur1 = python_internal_ArrayImpl._get(order, (remotes[at_r] if at_r >= 0 and at_r < len(remotes) else None))
                revised_order.append(ur1)
                at_r = (at_r + 1)
                continue
            if (at_l < len(locals)):
                ul1 = python_internal_ArrayImpl._get(order, (locals[at_l] if at_l >= 0 and at_l < len(locals) else None))
                revised_order.append(ul1)
                at_l = (at_l + 1)
                continue
        order = revised_order
        result = Ordering()
        result.setList(order)
        if (self.reference is None):
            result.ignoreParent()
        return result

    def markIdentical(self):
        self.marked_as_identical = True

    def isMarkedAsIdentical(self):
        return self.marked_as_identical

Alignment._hx_class = Alignment


class CellBuilder:
    _hx_class_name = "CellBuilder"
    __slots__ = ()
    _hx_methods = ["needSeparator", "setSeparator", "setConflictSeparator", "setView", "update", "conflict", "marker", "links"]
CellBuilder._hx_class = CellBuilder


class CellInfo:
    _hx_class_name = "CellInfo"
    __slots__ = ("raw", "value", "pretty_value", "category", "category_given_tr", "separator", "pretty_separator", "updated", "conflicted", "pvalue", "lvalue", "rvalue", "meta")
    _hx_fields = ["raw", "value", "pretty_value", "category", "category_given_tr", "separator", "pretty_separator", "updated", "conflicted", "pvalue", "lvalue", "rvalue", "meta"]
    _hx_methods = ["toString"]

    def __init__(self):
        self.meta = None
        self.rvalue = None
        self.lvalue = None
        self.pvalue = None
        self.conflicted = None
        self.updated = None
        self.pretty_separator = None
        self.separator = None
        self.category_given_tr = None
        self.category = None
        self.pretty_value = None
        self.value = None
        self.raw = None

    def toString(self):
        if (not self.updated):
            return self.value
        if (not self.conflicted):
            return ((HxOverrides.stringOrNull(self.lvalue) + "::") + HxOverrides.stringOrNull(self.rvalue))
        return ((((HxOverrides.stringOrNull(self.pvalue) + "||") + HxOverrides.stringOrNull(self.lvalue)) + "::") + HxOverrides.stringOrNull(self.rvalue))

CellInfo._hx_class = CellInfo


class Class: pass


class ColumnChange:
    _hx_class_name = "ColumnChange"
    __slots__ = ("prevName", "name", "props")
    _hx_fields = ["prevName", "name", "props"]

    def __init__(self):
        self.props = None
        self.name = None
        self.prevName = None

ColumnChange._hx_class = ColumnChange


class Table:
    _hx_class_name = "Table"
    __slots__ = ()
    _hx_methods = ["getCell", "setCell", "getCellView", "isResizable", "resize", "clear", "insertOrDeleteRows", "insertOrDeleteColumns", "trimBlank", "get_width", "get_height", "getData", "clone", "create", "getMeta"]
Table._hx_class = Table


class CombinedTable:
    _hx_class_name = "CombinedTable"
    __slots__ = ("t", "body", "head", "dx", "dy", "core", "meta")
    _hx_fields = ["t", "body", "head", "dx", "dy", "core", "meta"]
    _hx_methods = ["all", "getTable", "get_width", "get_height", "getCell", "setCell", "toString", "getCellView", "isResizable", "resize", "clear", "insertOrDeleteRows", "insertOrDeleteColumns", "trimBlank", "getData", "clone", "create", "getMeta"]
    _hx_interfaces = [Table]

    def __init__(self,t):
        self.meta = None
        self.body = None
        self.t = t
        self.dx = 0
        self.dy = 0
        self.core = t
        self.head = None
        if ((t.get_width() < 1) or ((t.get_height() < 1))):
            return
        v = t.getCellView()
        if (v.toString(t.getCell(0,0)) != "@@"):
            return
        self.dx = 1
        self.dy = 0
        _g = 0
        _g1 = t.get_height()
        while (_g < _g1):
            y = _g
            _g = (_g + 1)
            txt = v.toString(t.getCell(0,y))
            if (((txt is None) or ((txt == ""))) or ((txt == "null"))):
                break
            _hx_local_0 = self
            _hx_local_1 = _hx_local_0.dy
            _hx_local_0.dy = (_hx_local_1 + 1)
            _hx_local_1
        self.head = CombinedTableHead(self,self.dx,self.dy)
        self.body = CombinedTableBody(self,self.dx,self.dy)
        self.core = self.body
        self.meta = SimpleMeta(self.head)

    def all(self):
        return self.t

    def getTable(self):
        return self

    def get_width(self):
        return self.core.get_width()

    def get_height(self):
        return self.core.get_height()

    def getCell(self,x,y):
        return self.core.getCell(x,y)

    def setCell(self,x,y,c):
        self.core.setCell(x,y,c)

    def toString(self):
        return SimpleTable.tableToString(self)

    def getCellView(self):
        return self.t.getCellView()

    def isResizable(self):
        return self.core.isResizable()

    def resize(self,w,h):
        return self.core.resize(h,w)

    def clear(self):
        self.core.clear()

    def insertOrDeleteRows(self,fate,hfate):
        return self.core.insertOrDeleteRows(fate,hfate)

    def insertOrDeleteColumns(self,fate,wfate):
        return self.core.insertOrDeleteColumns(fate,wfate)

    def trimBlank(self):
        return self.core.trimBlank()

    def getData(self):
        return None

    def clone(self):
        return self.core.clone()

    def create(self):
        return self.t.create()

    def getMeta(self):
        return self.meta

CombinedTable._hx_class = CombinedTable


class CombinedTableBody:
    _hx_class_name = "CombinedTableBody"
    __slots__ = ("parent", "dx", "dy", "all", "meta")
    _hx_fields = ["parent", "dx", "dy", "all", "meta"]
    _hx_methods = ["getTable", "get_width", "get_height", "getCell", "setCell", "toString", "getCellView", "isResizable", "resize", "clear", "insertOrDeleteRows", "insertOrDeleteColumns", "trimBlank", "getData", "clone", "create", "getMeta"]
    _hx_interfaces = [Table]

    def __init__(self,parent,dx,dy):
        self.meta = None
        self.parent = parent
        self.dx = dx
        self.dy = dy
        self.all = parent.all()

    def getTable(self):
        return self

    def get_width(self):
        return (self.all.get_width() - 1)

    def get_height(self):
        return ((self.all.get_height() - self.dy) + 1)

    def getCell(self,x,y):
        if (y == 0):
            if (self.meta is None):
                self.meta = self.parent.getMeta().asTable()
            return self.meta.getCell((x + self.dx),0)
        return self.all.getCell((x + self.dx),((y + self.dy) - 1))

    def setCell(self,x,y,c):
        if (y == 0):
            self.all.setCell((x + self.dx),0,c)
            return
        self.all.setCell((x + self.dx),((y + self.dy) - 1),c)

    def toString(self):
        return SimpleTable.tableToString(self)

    def getCellView(self):
        return self.all.getCellView()

    def isResizable(self):
        return self.all.isResizable()

    def resize(self,w,h):
        return self.all.resize((w + 1),(h + self.dy))

    def clear(self):
        self.all.clear()
        self.dx = 0
        self.dy = 0

    def insertOrDeleteRows(self,fate,hfate):
        fate2 = list()
        _g = 0
        _g1 = self.dy
        while (_g < _g1):
            y = _g
            _g = (_g + 1)
            fate2.append(y)
        hdr = True
        _g = 0
        while (_g < len(fate)):
            f = (fate[_g] if _g >= 0 and _g < len(fate) else None)
            _g = (_g + 1)
            if hdr:
                hdr = False
                continue
            x = (((f + self.dy) - 1) if ((f >= 0)) else f)
            fate2.append(x)
        return self.all.insertOrDeleteRows(fate2,((hfate + self.dy) - 1))

    def insertOrDeleteColumns(self,fate,wfate):
        fate2 = list()
        _g = 0
        _g1 = (self.dx + 1)
        while (_g < _g1):
            x = _g
            _g = (_g + 1)
            fate2.append(x)
        _g = 0
        while (_g < len(fate)):
            f = (fate[_g] if _g >= 0 and _g < len(fate) else None)
            _g = (_g + 1)
            x = (((f + self.dx) + 1) if ((f >= 0)) else f)
            fate2.append(x)
        return self.all.insertOrDeleteColumns(fate2,(wfate + self.dx))

    def trimBlank(self):
        return self.all.trimBlank()

    def getData(self):
        return None

    def clone(self):
        return CombinedTable(self.all.clone())

    def create(self):
        return CombinedTable(self.all.create())

    def getMeta(self):
        return self.parent.getMeta()

CombinedTableBody._hx_class = CombinedTableBody


class CombinedTableHead:
    _hx_class_name = "CombinedTableHead"
    __slots__ = ("parent", "dx", "dy", "all")
    _hx_fields = ["parent", "dx", "dy", "all"]
    _hx_methods = ["getTable", "get_width", "get_height", "getCell", "setCell", "toString", "getCellView", "isResizable", "resize", "clear", "insertOrDeleteRows", "insertOrDeleteColumns", "trimBlank", "getData", "clone", "create", "getMeta"]
    _hx_interfaces = [Table]

    def __init__(self,parent,dx,dy):
        self.parent = parent
        self.dx = dx
        self.dy = dy
        self.all = parent.all()

    def getTable(self):
        return self

    def get_width(self):
        return self.all.get_width()

    def get_height(self):
        return self.dy

    def getCell(self,x,y):
        if (x == 0):
            v = self.getCellView()
            txt = v.toString(self.all.getCell(x,y))
            if ((("" if ((0 >= len(txt))) else txt[0])) == "@"):
                return HxString.substr(txt,1,len(txt))
        return self.all.getCell(x,y)

    def setCell(self,x,y,c):
        self.all.setCell(x,y,c)

    def toString(self):
        return SimpleTable.tableToString(self)

    def getCellView(self):
        return self.all.getCellView()

    def isResizable(self):
        return False

    def resize(self,w,h):
        return False

    def clear(self):
        pass

    def insertOrDeleteRows(self,fate,hfate):
        return False

    def insertOrDeleteColumns(self,fate,wfate):
        return self.all.insertOrDeleteColumns(fate,wfate)

    def trimBlank(self):
        return False

    def getData(self):
        return None

    def clone(self):
        return None

    def create(self):
        return None

    def getMeta(self):
        return None

CombinedTableHead._hx_class = CombinedTableHead


class CompareFlags:
    _hx_class_name = "CompareFlags"
    __slots__ = ("ordered", "show_unchanged", "unchanged_context", "always_show_order", "never_show_order", "show_unchanged_columns", "unchanged_column_context", "always_show_header", "acts", "ids", "columns_to_ignore", "tables", "allow_nested_cells", "warnings", "diff_strategy", "padding_strategy", "show_meta", "show_unchanged_meta", "parent", "count_like_a_spreadsheet", "ignore_whitespace", "ignore_case", "ignore_epsilon", "terminal_format", "use_glyphs", "quote_html")
    _hx_fields = ["ordered", "show_unchanged", "unchanged_context", "always_show_order", "never_show_order", "show_unchanged_columns", "unchanged_column_context", "always_show_header", "acts", "ids", "columns_to_ignore", "tables", "allow_nested_cells", "warnings", "diff_strategy", "padding_strategy", "show_meta", "show_unchanged_meta", "parent", "count_like_a_spreadsheet", "ignore_whitespace", "ignore_case", "ignore_epsilon", "terminal_format", "use_glyphs", "quote_html"]
    _hx_methods = ["filter", "allowUpdate", "allowInsert", "allowDelete", "allowColumn", "getIgnoredColumns", "addPrimaryKey", "ignoreColumn", "addTable", "addWarning", "getWarning", "getNameByRole", "getCanonicalName", "getIdsByRole"]

    def __init__(self):
        self.padding_strategy = None
        self.ordered = True
        self.show_unchanged = False
        self.unchanged_context = 1
        self.always_show_order = False
        self.never_show_order = True
        self.show_unchanged_columns = False
        self.unchanged_column_context = 1
        self.always_show_header = True
        self.acts = None
        self.ids = None
        self.columns_to_ignore = None
        self.allow_nested_cells = False
        self.warnings = None
        self.diff_strategy = None
        self.show_meta = True
        self.show_unchanged_meta = False
        self.tables = None
        self.parent = None
        self.count_like_a_spreadsheet = True
        self.ignore_whitespace = False
        self.ignore_case = False
        self.ignore_epsilon = -1
        self.terminal_format = None
        self.use_glyphs = True
        self.quote_html = True

    def filter(self,act,allow):
        if (self.acts is None):
            self.acts = haxe_ds_StringMap()
            self.acts.h["update"] = (not allow)
            self.acts.h["insert"] = (not allow)
            self.acts.h["delete"] = (not allow)
            self.acts.h["column"] = (not allow)
        if (not (act in self.acts.h)):
            return False
        self.acts.h[act] = allow
        return True

    def allowUpdate(self):
        if (self.acts is None):
            return True
        if ("update" in self.acts.h):
            return self.acts.h.get("update",None)
        else:
            return False

    def allowInsert(self):
        if (self.acts is None):
            return True
        if ("insert" in self.acts.h):
            return self.acts.h.get("insert",None)
        else:
            return False

    def allowDelete(self):
        if (self.acts is None):
            return True
        if ("delete" in self.acts.h):
            return self.acts.h.get("delete",None)
        else:
            return False

    def allowColumn(self):
        if (self.acts is None):
            return True
        if ("column" in self.acts.h):
            return self.acts.h.get("column",None)
        else:
            return False

    def getIgnoredColumns(self):
        if (self.columns_to_ignore is None):
            return None
        ignore = haxe_ds_StringMap()
        _g = 0
        _g1 = len(self.columns_to_ignore)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            ignore.h[(self.columns_to_ignore[i] if i >= 0 and i < len(self.columns_to_ignore) else None)] = True
        return ignore

    def addPrimaryKey(self,column):
        if (self.ids is None):
            self.ids = list()
        _this = self.ids
        _this.append(column)

    def ignoreColumn(self,column):
        if (self.columns_to_ignore is None):
            self.columns_to_ignore = list()
        _this = self.columns_to_ignore
        _this.append(column)

    def addTable(self,table):
        if (self.tables is None):
            self.tables = list()
        _this = self.tables
        _this.append(table)

    def addWarning(self,warn):
        if (self.warnings is None):
            self.warnings = list()
        _this = self.warnings
        _this.append(warn)

    def getWarning(self):
        _this = self.warnings
        return "\n".join([python_Boot.toString1(x1,'') for x1 in _this])

    def getNameByRole(self,name,role):
        parts = name.split(":")
        if (len(parts) <= 1):
            return name
        if (role == "parent"):
            return (parts[0] if 0 < len(parts) else None)
        if (role == "local"):
            return python_internal_ArrayImpl._get(parts, (len(parts) - 2))
        return python_internal_ArrayImpl._get(parts, (len(parts) - 1))

    def getCanonicalName(self,name):
        return self.getNameByRole(name,"local")

    def getIdsByRole(self,role):
        result = list()
        if (self.ids is None):
            return result
        _g = 0
        _g1 = self.ids
        while (_g < len(_g1)):
            name = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            x = self.getNameByRole(name,role)
            result.append(x)
        return result

CompareFlags._hx_class = CompareFlags


class CompareTable:
    _hx_class_name = "CompareTable"
    __slots__ = ("comp", "indexes")
    _hx_fields = ["comp", "indexes"]
    _hx_methods = ["run", "align", "getComparisonState", "alignCore", "alignCore2", "alignColumns", "testHasSameColumns", "hasSameColumns2", "testIsEqual", "isEqual2", "compareCore", "storeIndexes", "getIndexes", "useSql"]

    def __init__(self,comp):
        self.indexes = None
        self.comp = comp
        if (comp.compare_flags is not None):
            if (comp.compare_flags.parent is not None):
                comp.p = comp.compare_flags.parent

    def run(self):
        if self.useSql():
            self.comp.completed = True
            return False
        more = self.compareCore()
        while (more and self.comp.run_to_completion):
            more = self.compareCore()
        return (not more)

    def align(self):
        while (not self.comp.completed):
            self.run()
        alignment = Alignment()
        self.alignCore(alignment)
        alignment.comp = self.comp
        self.comp.alignment = alignment
        return alignment

    def getComparisonState(self):
        return self.comp

    def alignCore(self,align):
        if self.useSql():
            tab1 = None
            tab2 = None
            tab3 = None
            if (self.comp.p is None):
                tab1 = self.comp.a
                tab2 = self.comp.b
            else:
                align.reference = Alignment()
                tab1 = self.comp.p
                tab2 = self.comp.b
                tab3 = self.comp.a
            db = None
            if (tab1 is not None):
                db = tab1.getDatabase()
            if ((db is None) and ((tab2 is not None))):
                db = tab2.getDatabase()
            if ((db is None) and ((tab3 is not None))):
                db = tab3.getDatabase()
            sc = SqlCompare(db,tab1,tab2,tab3,align,self.comp.compare_flags)
            sc.apply()
            if (self.comp.p is not None):
                align.meta.reference = align.reference.meta
            return
        if (self.comp.p is None):
            self.alignCore2(align,self.comp.a,self.comp.b)
            return
        align.reference = Alignment()
        self.alignCore2(align,self.comp.p,self.comp.b)
        self.alignCore2(align.reference,self.comp.p,self.comp.a)
        align.meta.reference = align.reference.meta

    def alignCore2(self,align,a,b):
        if (align.meta is None):
            align.meta = Alignment()
        self.alignColumns(align.meta,a,b)
        column_order = align.meta.toOrder()
        align.range(a.get_height(),b.get_height())
        align.tables(a,b)
        align.setRowlike(True)
        w = a.get_width()
        ha = a.get_height()
        hb = b.get_height()
        av = a.getCellView()
        ids = None
        ignore = None
        ordered = True
        if (self.comp.compare_flags is not None):
            ids = self.comp.compare_flags.ids
            ignore = self.comp.compare_flags.getIgnoredColumns()
            ordered = self.comp.compare_flags.ordered
        common_units = list()
        ra_header = align.getSourceHeader()
        rb_header = align.getSourceHeader()
        _g = 0
        _g1 = column_order.getList()
        while (_g < len(_g1)):
            unit = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            if (((unit.l >= 0) and ((unit.r >= 0))) and ((unit.p != -1))):
                if (ignore is not None):
                    if (((unit.l >= 0) and ((ra_header >= 0))) and ((ra_header < a.get_height()))):
                        name = av.toString(a.getCell(unit.l,ra_header))
                        if (name in ignore.h):
                            continue
                    if (((unit.r >= 0) and ((rb_header >= 0))) and ((rb_header < b.get_height()))):
                        name1 = av.toString(b.getCell(unit.r,rb_header))
                        if (name1 in ignore.h):
                            continue
                common_units.append(unit)
        index_top = None
        pending_ct = ha
        reverse_pending_ct = hb
        used = haxe_ds_IntMap()
        used_reverse = haxe_ds_IntMap()
        if (ids is not None):
            index_top = IndexPair(self.comp.compare_flags)
            ids_as_map = haxe_ds_StringMap()
            _g = 0
            while (_g < len(ids)):
                id = (ids[_g] if _g >= 0 and _g < len(ids) else None)
                _g = (_g + 1)
                ids_as_map.h[id] = True
            _g = 0
            while (_g < len(common_units)):
                unit = (common_units[_g] if _g >= 0 and _g < len(common_units) else None)
                _g = (_g + 1)
                na = av.toString(a.getCell(unit.l,0))
                nb = av.toString(b.getCell(unit.r,0))
                if ((na in ids_as_map.h) or (nb in ids_as_map.h)):
                    index_top.addColumns(unit.l,unit.r)
                    align.addIndexColumns(unit)
            index_top.indexTables(a,b,1)
            if (self.indexes is not None):
                _this = self.indexes
                _this.append(index_top)
            _g = 0
            _g1 = ha
            while (_g < _g1):
                j = _g
                _g = (_g + 1)
                cross = index_top.queryLocal(j)
                spot_a = cross.spot_a
                spot_b = cross.spot_b
                if ((spot_a != 1) or ((spot_b != 1))):
                    continue
                jb = python_internal_ArrayImpl._get(cross.item_b.lst, 0)
                align.link(j,jb)
                used.set(jb,1)
                if (not (j in used_reverse.h)):
                    reverse_pending_ct = (reverse_pending_ct - 1)
                used_reverse.set(j,1)
        else:
            N = 5
            columns = list()
            if (len(common_units) > N):
                columns_eval = list()
                _g = 0
                _g1 = len(common_units)
                while (_g < _g1):
                    i = _g
                    _g = (_g + 1)
                    ct = 0
                    mem = haxe_ds_StringMap()
                    mem2 = haxe_ds_StringMap()
                    ca = (common_units[i] if i >= 0 and i < len(common_units) else None).l
                    cb = (common_units[i] if i >= 0 and i < len(common_units) else None).r
                    _g2 = 0
                    _g3 = ha
                    while (_g2 < _g3):
                        j = _g2
                        _g2 = (_g2 + 1)
                        key = av.toString(a.getCell(ca,j))
                        if (not (key in mem.h)):
                            mem.h[key] = 1
                            ct = (ct + 1)
                    _g4 = 0
                    _g5 = hb
                    while (_g4 < _g5):
                        j1 = _g4
                        _g4 = (_g4 + 1)
                        key1 = av.toString(b.getCell(cb,j1))
                        if (not (key1 in mem2.h)):
                            mem2.h[key1] = 1
                            ct = (ct + 1)
                    columns_eval.append([i, ct])
                def _hx_local_6(a,b):
                    if ((a[1] if 1 < len(a) else None) < (b[1] if 1 < len(b) else None)):
                        return 1
                    if ((a[1] if 1 < len(a) else None) > (b[1] if 1 < len(b) else None)):
                        return -1
                    if ((a[0] if 0 < len(a) else None) > (b[0] if 0 < len(b) else None)):
                        return 1
                    if ((a[0] if 0 < len(a) else None) < (b[0] if 0 < len(b) else None)):
                        return -1
                    return 0
                sorter = _hx_local_6
                columns_eval.sort(key= python_lib_Functools.cmp_to_key(sorter))
                _g = []
                _g_current = 0
                _g_array = columns_eval
                while (_g_current < len(_g_array)):
                    x = _g_current
                    _g_current = (_g_current + 1)
                    x1 = (_g_array[x] if x >= 0 and x < len(_g_array) else None)
                    x2 = (x1[0] if 0 < len(x1) else None)
                    _g.append(x2)
                columns = Lambda.array(_g)
                columns = columns[0:N]
            else:
                _g = 0
                _g1 = len(common_units)
                while (_g < _g1):
                    i = _g
                    _g = (_g + 1)
                    columns.append(i)
            top = Math.floor((Math.pow(2,len(columns)) + 0.5))
            pending = haxe_ds_IntMap()
            _g = 0
            _g1 = ha
            while (_g < _g1):
                j = _g
                _g = (_g + 1)
                pending.set(j,j)
            added_columns = haxe_ds_IntMap()
            index_ct = 0
            _g = 0
            _g1 = top
            while (_g < _g1):
                k = _g
                _g = (_g + 1)
                if (k == 0):
                    continue
                if (pending_ct == 0):
                    break
                active_columns = list()
                kk = k
                at = 0
                while (kk > 0):
                    if (HxOverrides.mod(kk, 2) == 1):
                        active_columns.append((columns[at] if at >= 0 and at < len(columns) else None))
                    kk = (kk >> 1)
                    at = (at + 1)
                index = IndexPair(self.comp.compare_flags)
                _g2 = 0
                _g3 = len(active_columns)
                while (_g2 < _g3):
                    k1 = _g2
                    _g2 = (_g2 + 1)
                    col = (active_columns[k1] if k1 >= 0 and k1 < len(active_columns) else None)
                    unit = (common_units[col] if col >= 0 and col < len(common_units) else None)
                    index.addColumns(unit.l,unit.r)
                    if (not (col in added_columns.h)):
                        align.addIndexColumns(unit)
                        added_columns.set(col,True)
                index.indexTables(a,b,1)
                if (k == ((top - 1))):
                    index_top = index
                h = a.get_height()
                if (b.get_height() > h):
                    h = b.get_height()
                if (h < 1):
                    h = 1
                wide_top_freq = index.getTopFreq()
                ratio = wide_top_freq
                ratio = (ratio / ((h + 20)))
                if (ratio >= 0.1):
                    if ((index_ct > 0) or ((k < ((top - 1))))):
                        continue
                index_ct = (index_ct + 1)
                if (self.indexes is not None):
                    _this = self.indexes
                    _this.append(index)
                fixed = list()
                j = pending.keys()
                while j.hasNext():
                    j1 = j.next()
                    cross = index.queryLocal(j1)
                    spot_a = cross.spot_a
                    spot_b = cross.spot_b
                    if ((spot_a != 1) or ((spot_b != 1))):
                        continue
                    val = python_internal_ArrayImpl._get(cross.item_b.lst, 0)
                    if (not (val in used.h)):
                        fixed.append(j1)
                        align.link(j1,val)
                        used.set(val,1)
                        if (not (j1 in used_reverse.h)):
                            reverse_pending_ct = (reverse_pending_ct - 1)
                        used_reverse.set(j1,1)
                _g4 = 0
                _g5 = len(fixed)
                while (_g4 < _g5):
                    j2 = _g4
                    _g4 = (_g4 + 1)
                    pending.remove((fixed[j2] if j2 >= 0 and j2 < len(fixed) else None))
                    pending_ct = (pending_ct - 1)
        if (index_top is not None):
            offset = 0
            scale = 1
            _g = 0
            while (_g < 2):
                sgn = _g
                _g = (_g + 1)
                if (pending_ct > 0):
                    xb = None
                    if ((scale == -1) and ((hb > 0))):
                        xb = (hb - 1)
                    _g1 = 0
                    _g2 = ha
                    while (_g1 < _g2):
                        xa0 = _g1
                        _g1 = (_g1 + 1)
                        xa = ((xa0 * scale) + offset)
                        xb2 = align.a2b(xa)
                        if (xb2 is not None):
                            xb = (xb2 + scale)
                            if ((xb >= hb) or ((xb < 0))):
                                break
                            continue
                        if (xb is None):
                            continue
                        ka = index_top.localKey(xa)
                        kb = index_top.remoteKey(xb)
                        if (ka != kb):
                            continue
                        if (xb in used.h):
                            continue
                        align.link(xa,xb)
                        used.set(xb,1)
                        used_reverse.set(xa,1)
                        pending_ct = (pending_ct - 1)
                        xb = (xb + scale)
                        if ((xb >= hb) or ((xb < 0))):
                            break
                        if (pending_ct == 0):
                            break
                offset = (ha - 1)
                scale = -1
            offset = 0
            scale = 1
            _g = 0
            while (_g < 2):
                sgn = _g
                _g = (_g + 1)
                if (reverse_pending_ct > 0):
                    xa = None
                    if ((scale == -1) and ((ha > 0))):
                        xa = (ha - 1)
                    _g1 = 0
                    _g2 = hb
                    while (_g1 < _g2):
                        xb0 = _g1
                        _g1 = (_g1 + 1)
                        xb = ((xb0 * scale) + offset)
                        xa2 = align.b2a(xb)
                        if (xa2 is not None):
                            xa = (xa2 + scale)
                            if ((xa >= ha) or ((xa < 0))):
                                break
                            continue
                        if (xa is None):
                            continue
                        ka = index_top.localKey(xa)
                        kb = index_top.remoteKey(xb)
                        if (ka != kb):
                            continue
                        if (xa in used_reverse.h):
                            continue
                        align.link(xa,xb)
                        used.set(xb,1)
                        used_reverse.set(xa,1)
                        reverse_pending_ct = (reverse_pending_ct - 1)
                        xa = (xa + scale)
                        if ((xa >= ha) or ((xa < 0))):
                            break
                        if (reverse_pending_ct == 0):
                            break
                offset = (hb - 1)
                scale = -1
        _g = 1
        _g1 = ha
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            if (not (i in used_reverse.h)):
                align.link(i,-1)
        _g = 1
        _g1 = hb
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            if (not (i in used.h)):
                align.link(-1,i)
        if ((ha > 0) and ((hb > 0))):
            align.link(0,0)
            align.headers(0,0)

    def alignColumns(self,align,a,b):
        align.range(a.get_width(),b.get_width())
        align.tables(a,b)
        align.setRowlike(False)
        slop = 5
        va = a.getCellView()
        vb = b.getCellView()
        ra_best = 0
        rb_best = 0
        ct_best = -1
        ma_best = None
        mb_best = None
        ra_header = 0
        rb_header = 0
        ra_uniques = 0
        rb_uniques = 0
        _g = 0
        _g1 = slop
        while (_g < _g1):
            ra = _g
            _g = (_g + 1)
            _g2 = 0
            _g3 = slop
            while (_g2 < _g3):
                rb = _g2
                _g2 = (_g2 + 1)
                ma = haxe_ds_StringMap()
                mb = haxe_ds_StringMap()
                ct = 0
                uniques = 0
                if (ra < a.get_height()):
                    _g4 = 0
                    _g5 = a.get_width()
                    while (_g4 < _g5):
                        ca = _g4
                        _g4 = (_g4 + 1)
                        key = va.toString(a.getCell(ca,ra))
                        if (key in ma.h):
                            ma.h[key] = -1
                            uniques = (uniques - 1)
                        else:
                            ma.h[key] = ca
                            uniques = (uniques + 1)
                    if (uniques > ra_uniques):
                        ra_header = ra
                        ra_uniques = uniques
                uniques = 0
                if (rb < b.get_height()):
                    _g6 = 0
                    _g7 = b.get_width()
                    while (_g6 < _g7):
                        cb = _g6
                        _g6 = (_g6 + 1)
                        key1 = vb.toString(b.getCell(cb,rb))
                        if (key1 in mb.h):
                            mb.h[key1] = -1
                            uniques = (uniques - 1)
                        else:
                            mb.h[key1] = cb
                            uniques = (uniques + 1)
                    if (uniques > rb_uniques):
                        rb_header = rb
                        rb_uniques = uniques
                key2 = ma.keys()
                while key2.hasNext():
                    key3 = key2.next()
                    i0 = ma.h.get(key3,None)
                    i1 = mb.h.get(key3,None)
                    if (i1 is not None):
                        if ((i1 >= 0) and ((i0 >= 0))):
                            ct = (ct + 1)
                if (ct > ct_best):
                    ct_best = ct
                    ma_best = ma
                    mb_best = mb
                    ra_best = ra
                    rb_best = rb
        if (ma_best is None):
            if ((a.get_height() > 0) and ((b.get_height() == 0))):
                align.headers(0,-1)
            elif ((a.get_height() == 0) and ((b.get_height() > 0))):
                align.headers(-1,0)
            return
        key = ma_best.keys()
        while key.hasNext():
            key1 = key.next()
            i0 = ma_best.h.get(key1,None)
            i1 = mb_best.h.get(key1,None)
            if ((i0 is not None) and ((i1 is not None))):
                align.link(i0,i1)
            elif (i0 is not None):
                align.link(i0,-1)
            elif (i1 is not None):
                align.link(-1,i1)
        key = mb_best.keys()
        while key.hasNext():
            key1 = key.next()
            i0 = ma_best.h.get(key1,None)
            i1 = mb_best.h.get(key1,None)
            if ((i0 is None) and ((i1 is not None))):
                align.link(-1,i1)
        align.headers(ra_header,rb_header)

    def testHasSameColumns(self):
        p = self.comp.p
        a = self.comp.a
        b = self.comp.b
        eq = self.hasSameColumns2(a,b)
        if (eq and ((p is not None))):
            eq = self.hasSameColumns2(p,a)
        self.comp.has_same_columns = eq
        self.comp.has_same_columns_known = True
        return True

    def hasSameColumns2(self,a,b):
        if (a.get_width() != b.get_width()):
            return False
        if ((a.get_height() == 0) or ((b.get_height() == 0))):
            return True
        av = a.getCellView()
        _g = 0
        _g1 = a.get_width()
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            _g2 = (i + 1)
            _g3 = a.get_width()
            while (_g2 < _g3):
                j = _g2
                _g2 = (_g2 + 1)
                if av.equals(a.getCell(i,0),a.getCell(j,0)):
                    return False
            if (not av.equals(a.getCell(i,0),b.getCell(i,0))):
                return False
        return True

    def testIsEqual(self):
        p = self.comp.p
        a = self.comp.a
        b = self.comp.b
        self.comp.getMeta()
        nested = False
        if (self.comp.p_meta is not None):
            if self.comp.p_meta.isNested():
                nested = True
        if (self.comp.a_meta is not None):
            if self.comp.a_meta.isNested():
                nested = True
        if (self.comp.b_meta is not None):
            if self.comp.b_meta.isNested():
                nested = True
        if nested:
            self.comp.is_equal = False
            self.comp.is_equal_known = True
            return True
        eq = self.isEqual2(a,b)
        if (eq and ((p is not None))):
            eq = self.isEqual2(p,a)
        self.comp.is_equal = eq
        self.comp.is_equal_known = True
        return True

    def isEqual2(self,a,b):
        if ((a.get_width() != b.get_width()) or ((a.get_height() != b.get_height()))):
            return False
        av = a.getCellView()
        _g = 0
        _g1 = a.get_height()
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            _g2 = 0
            _g3 = a.get_width()
            while (_g2 < _g3):
                j = _g2
                _g2 = (_g2 + 1)
                if (not av.equals(a.getCell(j,i),b.getCell(j,i))):
                    return False
        return True

    def compareCore(self):
        if self.comp.completed:
            return False
        if (not self.comp.is_equal_known):
            return self.testIsEqual()
        if (not self.comp.has_same_columns_known):
            return self.testHasSameColumns()
        self.comp.completed = True
        return False

    def storeIndexes(self):
        self.indexes = list()

    def getIndexes(self):
        return self.indexes

    def useSql(self):
        if (self.comp.compare_flags is None):
            return False
        self.comp.getMeta()
        sql = True
        if (self.comp.p_meta is not None):
            if (not self.comp.p_meta.isSql()):
                sql = False
        if (self.comp.a_meta is not None):
            if (not self.comp.a_meta.isSql()):
                sql = False
        if (self.comp.b_meta is not None):
            if (not self.comp.b_meta.isSql()):
                sql = False
        if ((self.comp.p is not None) and ((self.comp.p_meta is None))):
            sql = False
        if ((self.comp.a is not None) and ((self.comp.a_meta is None))):
            sql = False
        if ((self.comp.b is not None) and ((self.comp.b_meta is None))):
            sql = False
        return sql

CompareTable._hx_class = CompareTable


class ConflictInfo:
    _hx_class_name = "ConflictInfo"
    __slots__ = ("row", "col", "pvalue", "lvalue", "rvalue")
    _hx_fields = ["row", "col", "pvalue", "lvalue", "rvalue"]

    def __init__(self,row,col,pvalue,lvalue,rvalue):
        self.row = row
        self.col = col
        self.pvalue = pvalue
        self.lvalue = lvalue
        self.rvalue = rvalue

ConflictInfo._hx_class = ConflictInfo


class Coopy:
    _hx_class_name = "Coopy"
    __slots__ = ("format_preference", "delim_preference", "csv_eol_preference", "extern_preference", "output_format", "output_format_set", "nested_output", "order_set", "order_preference", "io", "strategy", "css_output", "fragment", "flags", "cache_txt", "fail_if_diff", "diffs_found", "mv", "status", "daff_cmd")
    _hx_fields = ["format_preference", "delim_preference", "csv_eol_preference", "extern_preference", "output_format", "output_format_set", "nested_output", "order_set", "order_preference", "io", "strategy", "css_output", "fragment", "flags", "cache_txt", "fail_if_diff", "diffs_found", "mv", "status", "daff_cmd"]
    _hx_methods = ["init", "checkFormat", "setFormat", "getRenderer", "applyRenderer", "renderTable", "renderTables", "saveTable", "encodeTable", "saveTables", "saveText", "jsonToTables", "jsonToTable", "useColor", "runDiff", "loadTable", "command", "installGitDriver", "run", "coopyhx"]
    _hx_statics = ["VERSION", "diffAsHtml", "diffAsAnsi", "diff", "getBlankTable", "align", "patch", "compareTables", "compareTables3", "keepAround", "cellFor", "main", "show", "jsonify", "tablify"]

    def __init__(self,io = None):
        self.daff_cmd = None
        self.status = None
        self.mv = None
        self.diffs_found = None
        self.fail_if_diff = None
        self.cache_txt = None
        self.flags = None
        self.fragment = None
        self.css_output = None
        self.strategy = None
        self.io = None
        self.order_preference = None
        self.order_set = None
        self.nested_output = None
        self.output_format_set = None
        self.output_format = None
        self.extern_preference = None
        self.csv_eol_preference = None
        self.delim_preference = None
        self.format_preference = None
        self.init()
        self.io = io

    def init(self):
        self.extern_preference = False
        self.format_preference = None
        self.delim_preference = None
        self.csv_eol_preference = None
        self.output_format = "copy"
        self.output_format_set = False
        self.nested_output = False
        self.order_set = False
        self.order_preference = False
        self.strategy = None
        self.css_output = None
        self.fragment = False
        self.flags = None
        self.cache_txt = None
        self.fail_if_diff = False
        self.diffs_found = False

    def checkFormat(self,name):
        if self.extern_preference:
            return self.format_preference
        ext = ""
        if (name is not None):
            startIndex = None
            pt = None
            if (startIndex is None):
                pt = name.rfind(".", 0, len(name))
            else:
                i = name.rfind(".", 0, (startIndex + 1))
                startLeft = (max(0,((startIndex + 1) - len("."))) if ((i == -1)) else (i + 1))
                check = name.find(".", startLeft, len(name))
                pt = (check if (((check > i) and ((check <= startIndex)))) else i)
            if (pt >= 0):
                ext = HxString.substr(name,(pt + 1),None).lower()
                ext1 = ext
                _hx_local_0 = len(ext1)
                if (_hx_local_0 == 4):
                    if (ext1 == "html"):
                        self.format_preference = "html"
                    elif (ext1 == "json"):
                        self.format_preference = "json"
                    else:
                        ext = ""
                elif (_hx_local_0 == 3):
                    if (ext1 == "csv"):
                        self.format_preference = "csv"
                        self.delim_preference = ","
                    elif (ext1 == "htm"):
                        self.format_preference = "html"
                    elif (ext1 == "psv"):
                        self.format_preference = "csv"
                        self.delim_preference = "".join(map(chr,[128169]))
                    elif (ext1 == "ssv"):
                        self.format_preference = "csv"
                        self.delim_preference = ";"
                        self.format_preference = "csv"
                    elif (ext1 == "tsv"):
                        self.format_preference = "csv"
                        self.delim_preference = "\t"
                    elif (ext1 == "www"):
                        self.format_preference = "www"
                    else:
                        ext = ""
                elif (_hx_local_0 == 7):
                    if (ext1 == "sqlite3"):
                        self.format_preference = "sqlite"
                    else:
                        ext = ""
                elif (_hx_local_0 == 6):
                    if (ext1 == "ndjson"):
                        self.format_preference = "ndjson"
                    elif (ext1 == "sqlite"):
                        self.format_preference = "sqlite"
                    else:
                        ext = ""
                else:
                    ext = ""
        self.nested_output = ((self.format_preference == "json") or ((self.format_preference == "ndjson")))
        self.order_preference = (not self.nested_output)
        return ext

    def setFormat(self,name):
        self.extern_preference = False
        self.checkFormat(("." + ("null" if name is None else name)))
        self.extern_preference = True

    def getRenderer(self):
        renderer = DiffRender()
        renderer.usePrettyArrows(self.flags.use_glyphs)
        renderer.quoteHtml(self.flags.quote_html)
        return renderer

    def applyRenderer(self,name,renderer):
        if (not self.fragment):
            renderer.completeHtml()
        if (self.format_preference == "www"):
            self.io.sendToBrowser(renderer.html())
        else:
            self.saveText(name,renderer.html())
        if (self.css_output is not None):
            self.saveText(self.css_output,renderer.sampleCss())
        return True

    def renderTable(self,name,t):
        renderer = self.getRenderer()
        renderer.render(t)
        return self.applyRenderer(name,renderer)

    def renderTables(self,name,t):
        renderer = self.getRenderer()
        renderer.renderTables(t)
        return self.applyRenderer(name,renderer)

    def saveTable(self,name,t,render = None):
        txt = self.encodeTable(name,t,render)
        if (txt is None):
            return True
        return self.saveText(name,txt)

    def encodeTable(self,name,t,render = None):
        if (self.output_format != "copy"):
            self.setFormat(self.output_format)
        txt = ""
        self.checkFormat(name)
        if ((self.format_preference == "sqlite") and (not self.extern_preference)):
            self.format_preference = "csv"
        if (render is None):
            if (self.format_preference == "csv"):
                csv = Csv(self.delim_preference,self.csv_eol_preference)
                txt = csv.renderTable(t)
            elif (self.format_preference == "ndjson"):
                txt = Ndjson(t).render()
            elif ((self.format_preference == "html") or ((self.format_preference == "www"))):
                self.renderTable(name,t)
                return None
            elif (self.format_preference == "sqlite"):
                self.io.writeStderr("! Cannot yet output to sqlite, aborting\n")
                return ""
            else:
                txt = haxe_format_JsonPrinter.print(Coopy.jsonify(t),None,"  ")
        else:
            txt = render.render(t)
        return txt

    def saveTables(self,name,os,use_color,is_diff):
        if (self.output_format != "copy"):
            self.setFormat(self.output_format)
        txt = ""
        self.checkFormat(name)
        render = None
        if use_color:
            render = TerminalDiffRender(self.flags,self.delim_preference,is_diff)
        order = os.getOrder()
        if (len(order) == 1):
            return self.saveTable(name,os.one(),render)
        if ((self.format_preference == "html") or ((self.format_preference == "www"))):
            return self.renderTables(name,os)
        need_blank = False
        if ((len(order) == 0) or os.hasInsDel()):
            txt = (("null" if txt is None else txt) + HxOverrides.stringOrNull(self.encodeTable(name,os.one(),render)))
            need_blank = True
        if (len(order) > 1):
            _g = 1
            _g1 = len(order)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                t = os.get((order[i] if i >= 0 and i < len(order) else None))
                if (t is not None):
                    if need_blank:
                        txt = (("null" if txt is None else txt) + "\n")
                    need_blank = True
                    txt = (("null" if txt is None else txt) + HxOverrides.stringOrNull(((HxOverrides.stringOrNull((order[i] if i >= 0 and i < len(order) else None)) + "\n"))))
                    line = ""
                    _g2 = 0
                    _g3 = len((order[i] if i >= 0 and i < len(order) else None))
                    while (_g2 < _g3):
                        i1 = _g2
                        _g2 = (_g2 + 1)
                        line = (("null" if line is None else line) + "=")
                    txt = (("null" if txt is None else txt) + HxOverrides.stringOrNull(((("null" if line is None else line) + "\n"))))
                    txt = (("null" if txt is None else txt) + HxOverrides.stringOrNull(self.encodeTable(name,os.get((order[i] if i >= 0 and i < len(order) else None)),render)))
        return self.saveText(name,txt)

    def saveText(self,name,txt):
        if (name is None):
            _hx_local_0 = self
            _hx_local_1 = _hx_local_0.cache_txt
            _hx_local_0.cache_txt = (("null" if _hx_local_1 is None else _hx_local_1) + ("null" if txt is None else txt))
            _hx_local_0.cache_txt
        elif (name != "-"):
            self.io.saveContent(name,txt)
        else:
            self.io.writeStdout(txt)
        return True

    def jsonToTables(self,json):
        tables = Reflect.field(json,"tables")
        if (tables is None):
            return self.jsonToTable(json)
        return JsonTables(json,self.flags)

    def jsonToTable(self,json):
        output = None
        _g = 0
        _g1 = python_Boot.fields(json)
        while (_g < len(_g1)):
            name = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            t = Reflect.field(json,name)
            columns = Reflect.field(t,"columns")
            if (columns is None):
                continue
            rows = Reflect.field(t,"rows")
            if (rows is None):
                continue
            output = SimpleTable(len(columns),len(rows))
            has_hash = False
            has_hash_known = False
            _g2 = 0
            _g3 = len(rows)
            while (_g2 < _g3):
                i = _g2
                _g2 = (_g2 + 1)
                row = (rows[i] if i >= 0 and i < len(rows) else None)
                if (not has_hash_known):
                    if (len(python_Boot.fields(row)) == len(columns)):
                        has_hash = True
                    has_hash_known = True
                if (not has_hash):
                    lst = row
                    _g4 = 0
                    _g5 = len(columns)
                    while (_g4 < _g5):
                        j = _g4
                        _g4 = (_g4 + 1)
                        val = (lst[j] if j >= 0 and j < len(lst) else None)
                        output.setCell(j,i,Coopy.cellFor(val))
                else:
                    _g6 = 0
                    _g7 = len(columns)
                    while (_g6 < _g7):
                        j1 = _g6
                        _g6 = (_g6 + 1)
                        val1 = Reflect.field(row,(columns[j1] if j1 >= 0 and j1 < len(columns) else None))
                        output.setCell(j1,i,Coopy.cellFor(val1))
        if (output is not None):
            output.trimBlank()
        return output

    def useColor(self,flags,output):
        use_color = (flags.terminal_format == "ansi")
        if (flags.terminal_format is None):
            if ((((output is None) or ((output == "-")))) and ((((self.output_format == "copy") or ((self.output_format == "csv"))) or ((self.output_format == "psv"))))):
                if (self.io is not None):
                    if self.io.isTtyKnown():
                        use_color = self.io.isTty()
        return use_color

    def runDiff(self,parent,a,b,flags,output):
        ct = Coopy.compareTables3(parent,a,b,flags)
        align = ct.align()
        td = TableDiff(align,flags)
        o = SimpleTable(0,0)
        os = Tables(o)
        td.hiliteWithNesting(os)
        use_color = self.useColor(flags,output)
        self.saveTables(output,os,use_color,True)
        if self.fail_if_diff:
            summary = td.getSummary()
            if summary.different:
                self.diffs_found = True

    def loadTable(self,name,role):
        ext = self.checkFormat(name)
        if (ext == "sqlite"):
            sql = self.io.openSqliteDatabase(name)
            if (sql is None):
                self.io.writeStderr("! Cannot open database, aborting\n")
                return None
            tab = SqlTables(sql,self.flags,role)
            return tab
        txt = self.io.getContent(name)
        if (ext == "ndjson"):
            t = SimpleTable(0,0)
            ndjson = Ndjson(t)
            ndjson.parse(txt)
            return t
        if ((ext == "json") or ((ext == ""))):
            try:
                json = python_lib_Json.loads(txt,**python__KwArgs_KwArgs_Impl_.fromT(_hx_AnonObject({'object_hook': python_Lib.dictToAnon})))
                self.format_preference = "json"
                t = self.jsonToTables(json)
                if (t is None):
                    raise haxe_Exception.thrown("JSON failed")
                return t
            except BaseException as _g:
                None
                e = haxe_Exception.caught(_g).unwrap()
                if (ext == "json"):
                    raise haxe_Exception.thrown(e)
        self.format_preference = "csv"
        csv = Csv(self.delim_preference)
        output = SimpleTable(0,0)
        csv.parseTable(txt,output)
        if (self.csv_eol_preference is None):
            self.csv_eol_preference = csv.getDiscoveredEol()
        if (output is not None):
            output.trimBlank()
        return output

    def command(self,io,cmd,args):
        r = 0
        if io.hasAsync():
            r = io.command(cmd,args)
        if (r != 999):
            io.writeStdout(("$ " + ("null" if cmd is None else cmd)))
            _g = 0
            while (_g < len(args)):
                arg = (args[_g] if _g >= 0 and _g < len(args) else None)
                _g = (_g + 1)
                io.writeStdout(" ")
                startIndex = None
                spaced = (((arg.find(" ") if ((startIndex is None)) else HxString.indexOfImpl(arg," ",startIndex))) >= 0)
                if spaced:
                    io.writeStdout("\"")
                io.writeStdout(arg)
                if spaced:
                    io.writeStdout("\"")
            io.writeStdout("\n")
        if (not io.hasAsync()):
            r = io.command(cmd,args)
        return r

    def installGitDriver(self,io,formats):
        r = 0
        if (self.status is None):
            self.status = haxe_ds_StringMap()
            self.daff_cmd = ""
        key = "hello"
        if (not (key in self.status.h)):
            io.writeStdout("Setting up git to use daff on")
            _g = 0
            while (_g < len(formats)):
                format = (formats[_g] if _g >= 0 and _g < len(formats) else None)
                _g = (_g + 1)
                io.writeStdout((" *." + ("null" if format is None else format)))
            io.writeStdout(" files\n")
            self.status.h[key] = r
        key = "can_run_git"
        if (not (key in self.status.h)):
            r = self.command(io,"git",["--version"])
            if (r == 999):
                return r
            self.status.h[key] = r
            if (r != 0):
                io.writeStderr("! Cannot run git, aborting\n")
                return 1
            io.writeStdout("- Can run git\n")
        daffs = ["daff", "daff.rb", "daff.py"]
        if (self.daff_cmd == ""):
            _g = 0
            while (_g < len(daffs)):
                daff = (daffs[_g] if _g >= 0 and _g < len(daffs) else None)
                _g = (_g + 1)
                key1 = ("can_run_" + ("null" if daff is None else daff))
                if (not (key1 in self.status.h)):
                    r = self.command(io,daff,["version"])
                    if (r == 999):
                        return r
                    self.status.h[key1] = r
                    if (r == 0):
                        self.daff_cmd = daff
                        io.writeStdout((((("- Can run " + ("null" if daff is None else daff)) + " as \"") + ("null" if daff is None else daff)) + "\"\n"))
                        break
            if (self.daff_cmd == ""):
                io.writeStderr("! Cannot find daff, is it in your path?\n")
                return 1
        _g = 0
        while (_g < len(formats)):
            format = (formats[_g] if _g >= 0 and _g < len(formats) else None)
            _g = (_g + 1)
            key = ("have_diff_driver_" + ("null" if format is None else format))
            if (not (key in self.status.h)):
                r = self.command(io,"git",["config", "--global", "--get", (("diff.daff-" + ("null" if format is None else format)) + ".command")])
                if (r == 999):
                    return r
                self.status.h[key] = r
            have_diff_driver = (self.status.h.get(key,None) == 0)
            key = ("add_diff_driver_" + ("null" if format is None else format))
            if (not (key in self.status.h)):
                r = self.command(io,"git",["config", "--global", (("diff.daff-" + ("null" if format is None else format)) + ".command"), (HxOverrides.stringOrNull(self.daff_cmd) + " diff --git")])
                if (r == 999):
                    return r
                if have_diff_driver:
                    io.writeStdout((("- Cleared existing daff diff driver for " + ("null" if format is None else format)) + "\n"))
                io.writeStdout((("- Added diff driver for " + ("null" if format is None else format)) + "\n"))
                self.status.h[key] = r
            key = ("have_merge_driver_" + ("null" if format is None else format))
            if (not (key in self.status.h)):
                r = self.command(io,"git",["config", "--global", "--get", (("merge.daff-" + ("null" if format is None else format)) + ".driver")])
                if (r == 999):
                    return r
                self.status.h[key] = r
            have_merge_driver = (self.status.h.get(key,None) == 0)
            key = ("name_merge_driver_" + ("null" if format is None else format))
            if (not (key in self.status.h)):
                if (not have_merge_driver):
                    r = self.command(io,"git",["config", "--global", (("merge.daff-" + ("null" if format is None else format)) + ".name"), (("daff tabular " + ("null" if format is None else format)) + " merge")])
                    if (r == 999):
                        return r
                else:
                    r = 0
                self.status.h[key] = r
            key = ("add_merge_driver_" + ("null" if format is None else format))
            if (not (key in self.status.h)):
                r = self.command(io,"git",["config", "--global", (("merge.daff-" + ("null" if format is None else format)) + ".driver"), (HxOverrides.stringOrNull(self.daff_cmd) + " merge --output %A %O %A %B")])
                if (r == 999):
                    return r
                if have_merge_driver:
                    io.writeStdout((("- Cleared existing daff merge driver for " + ("null" if format is None else format)) + "\n"))
                io.writeStdout((("- Added merge driver for " + ("null" if format is None else format)) + "\n"))
                self.status.h[key] = r
        if (not io.exists(".git/config")):
            io.writeStderr("! This next part needs to happen in a git repository.\n")
            io.writeStderr("! Please run again from the root of a git repository.\n")
            return 1
        attr = ".gitattributes"
        txt = ""
        post = ""
        if (not io.exists(attr)):
            io.writeStdout("- No .gitattributes file\n")
        else:
            io.writeStdout("- You have a .gitattributes file\n")
            txt = io.getContent(attr)
        need_update = False
        _g = 0
        while (_g < len(formats)):
            format = (formats[_g] if _g >= 0 and _g < len(formats) else None)
            _g = (_g + 1)
            _hx_str = ("*." + ("null" if format is None else format))
            startIndex = None
            if (((txt.find(_hx_str) if ((startIndex is None)) else HxString.indexOfImpl(txt,_hx_str,startIndex))) >= 0):
                io.writeStderr((("- Your .gitattributes file already mentions *." + ("null" if format is None else format)) + "\n"))
            else:
                post = (("null" if post is None else post) + HxOverrides.stringOrNull(((((("*." + ("null" if format is None else format)) + " diff=daff-") + ("null" if format is None else format)) + "\n"))))
                post = (("null" if post is None else post) + HxOverrides.stringOrNull(((((("*." + ("null" if format is None else format)) + " merge=daff-") + ("null" if format is None else format)) + "\n"))))
                io.writeStdout("- Placing the following lines in .gitattributes:\n")
                io.writeStdout(post)
                if ((txt != "") and (not need_update)):
                    txt = (("null" if txt is None else txt) + "\n")
                txt = (("null" if txt is None else txt) + ("null" if post is None else post))
                need_update = True
        if need_update:
            io.saveContent(attr,txt)
        io.writeStdout("- Done!\n")
        return 0

    def run(self,args,io = None):
        if (io is None):
            io = TableIO()
        if (io is None):
            print("No system interface available")
            return 1
        self.init()
        self.io = io
        more = True
        output = None
        inplace = False
        git = False
        help = False
        self.flags = CompareFlags()
        self.flags.always_show_header = True
        while more:
            more = False
            _g = 0
            _g1 = len(args)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                tag = (args[i] if i >= 0 and i < len(args) else None)
                if (tag == "--output"):
                    more = True
                    output = python_internal_ArrayImpl._get(args, (i + 1))
                    pos = i
                    if (pos < 0):
                        pos = (len(args) + pos)
                    if (pos < 0):
                        pos = 0
                    res = args[pos:(pos + 2)]
                    del args[pos:(pos + 2)]
                    break
                elif (tag == "--css"):
                    more = True
                    self.fragment = True
                    self.css_output = python_internal_ArrayImpl._get(args, (i + 1))
                    pos1 = i
                    if (pos1 < 0):
                        pos1 = (len(args) + pos1)
                    if (pos1 < 0):
                        pos1 = 0
                    res1 = args[pos1:(pos1 + 2)]
                    del args[pos1:(pos1 + 2)]
                    break
                elif (tag == "--fragment"):
                    more = True
                    self.fragment = True
                    pos2 = i
                    if (pos2 < 0):
                        pos2 = (len(args) + pos2)
                    if (pos2 < 0):
                        pos2 = 0
                    res2 = args[pos2:(pos2 + 1)]
                    del args[pos2:(pos2 + 1)]
                    break
                elif (tag == "--plain"):
                    more = True
                    self.flags.use_glyphs = False
                    pos3 = i
                    if (pos3 < 0):
                        pos3 = (len(args) + pos3)
                    if (pos3 < 0):
                        pos3 = 0
                    res3 = args[pos3:(pos3 + 1)]
                    del args[pos3:(pos3 + 1)]
                    break
                elif (tag == "--unquote"):
                    more = True
                    self.flags.quote_html = False
                    pos4 = i
                    if (pos4 < 0):
                        pos4 = (len(args) + pos4)
                    if (pos4 < 0):
                        pos4 = 0
                    res4 = args[pos4:(pos4 + 1)]
                    del args[pos4:(pos4 + 1)]
                    break
                elif (tag == "--all"):
                    more = True
                    self.flags.show_unchanged = True
                    self.flags.show_unchanged_columns = True
                    pos5 = i
                    if (pos5 < 0):
                        pos5 = (len(args) + pos5)
                    if (pos5 < 0):
                        pos5 = 0
                    res5 = args[pos5:(pos5 + 1)]
                    del args[pos5:(pos5 + 1)]
                    break
                elif (tag == "--all-rows"):
                    more = True
                    self.flags.show_unchanged = True
                    pos6 = i
                    if (pos6 < 0):
                        pos6 = (len(args) + pos6)
                    if (pos6 < 0):
                        pos6 = 0
                    res6 = args[pos6:(pos6 + 1)]
                    del args[pos6:(pos6 + 1)]
                    break
                elif (tag == "--all-columns"):
                    more = True
                    self.flags.show_unchanged_columns = True
                    pos7 = i
                    if (pos7 < 0):
                        pos7 = (len(args) + pos7)
                    if (pos7 < 0):
                        pos7 = 0
                    res7 = args[pos7:(pos7 + 1)]
                    del args[pos7:(pos7 + 1)]
                    break
                elif (tag == "--act"):
                    more = True
                    if (self.flags.acts is None):
                        self.flags.acts = haxe_ds_StringMap()
                    self.flags.acts.h[python_internal_ArrayImpl._get(args, (i + 1))] = True
                    pos8 = i
                    if (pos8 < 0):
                        pos8 = (len(args) + pos8)
                    if (pos8 < 0):
                        pos8 = 0
                    res8 = args[pos8:(pos8 + 2)]
                    del args[pos8:(pos8 + 2)]
                    break
                elif (tag == "--context"):
                    more = True
                    context = Std.parseInt(python_internal_ArrayImpl._get(args, (i + 1)))
                    if (context >= 0):
                        self.flags.unchanged_context = context
                    pos9 = i
                    if (pos9 < 0):
                        pos9 = (len(args) + pos9)
                    if (pos9 < 0):
                        pos9 = 0
                    res9 = args[pos9:(pos9 + 2)]
                    del args[pos9:(pos9 + 2)]
                    break
                elif (tag == "--context-columns"):
                    more = True
                    context1 = Std.parseInt(python_internal_ArrayImpl._get(args, (i + 1)))
                    if (context1 >= 0):
                        self.flags.unchanged_column_context = context1
                    pos10 = i
                    if (pos10 < 0):
                        pos10 = (len(args) + pos10)
                    if (pos10 < 0):
                        pos10 = 0
                    res10 = args[pos10:(pos10 + 2)]
                    del args[pos10:(pos10 + 2)]
                    break
                elif (tag == "--inplace"):
                    more = True
                    inplace = True
                    pos11 = i
                    if (pos11 < 0):
                        pos11 = (len(args) + pos11)
                    if (pos11 < 0):
                        pos11 = 0
                    res11 = args[pos11:(pos11 + 1)]
                    del args[pos11:(pos11 + 1)]
                    break
                elif (tag == "--git"):
                    more = True
                    git = True
                    pos12 = i
                    if (pos12 < 0):
                        pos12 = (len(args) + pos12)
                    if (pos12 < 0):
                        pos12 = 0
                    res12 = args[pos12:(pos12 + 1)]
                    del args[pos12:(pos12 + 1)]
                    break
                elif (tag == "--unordered"):
                    more = True
                    self.flags.ordered = False
                    self.flags.unchanged_context = 0
                    self.order_set = True
                    pos13 = i
                    if (pos13 < 0):
                        pos13 = (len(args) + pos13)
                    if (pos13 < 0):
                        pos13 = 0
                    res13 = args[pos13:(pos13 + 1)]
                    del args[pos13:(pos13 + 1)]
                    break
                elif (tag == "--ordered"):
                    more = True
                    self.flags.ordered = True
                    self.order_set = True
                    pos14 = i
                    if (pos14 < 0):
                        pos14 = (len(args) + pos14)
                    if (pos14 < 0):
                        pos14 = 0
                    res14 = args[pos14:(pos14 + 1)]
                    del args[pos14:(pos14 + 1)]
                    break
                elif (tag == "--color"):
                    more = True
                    self.flags.terminal_format = "ansi"
                    pos15 = i
                    if (pos15 < 0):
                        pos15 = (len(args) + pos15)
                    if (pos15 < 0):
                        pos15 = 0
                    res15 = args[pos15:(pos15 + 1)]
                    del args[pos15:(pos15 + 1)]
                    break
                elif (tag == "--no-color"):
                    more = True
                    self.flags.terminal_format = "plain"
                    pos16 = i
                    if (pos16 < 0):
                        pos16 = (len(args) + pos16)
                    if (pos16 < 0):
                        pos16 = 0
                    res16 = args[pos16:(pos16 + 1)]
                    del args[pos16:(pos16 + 1)]
                    break
                elif (tag == "--input-format"):
                    more = True
                    self.setFormat(python_internal_ArrayImpl._get(args, (i + 1)))
                    pos17 = i
                    if (pos17 < 0):
                        pos17 = (len(args) + pos17)
                    if (pos17 < 0):
                        pos17 = 0
                    res17 = args[pos17:(pos17 + 2)]
                    del args[pos17:(pos17 + 2)]
                    break
                elif (tag == "--output-format"):
                    more = True
                    self.output_format = python_internal_ArrayImpl._get(args, (i + 1))
                    self.output_format_set = True
                    pos18 = i
                    if (pos18 < 0):
                        pos18 = (len(args) + pos18)
                    if (pos18 < 0):
                        pos18 = 0
                    res18 = args[pos18:(pos18 + 2)]
                    del args[pos18:(pos18 + 2)]
                    break
                elif (tag == "--id"):
                    more = True
                    if (self.flags.ids is None):
                        self.flags.ids = list()
                    _this = self.flags.ids
                    _this.append(python_internal_ArrayImpl._get(args, (i + 1)))
                    pos19 = i
                    if (pos19 < 0):
                        pos19 = (len(args) + pos19)
                    if (pos19 < 0):
                        pos19 = 0
                    res19 = args[pos19:(pos19 + 2)]
                    del args[pos19:(pos19 + 2)]
                    break
                elif (tag == "--ignore"):
                    more = True
                    self.flags.ignoreColumn(python_internal_ArrayImpl._get(args, (i + 1)))
                    pos20 = i
                    if (pos20 < 0):
                        pos20 = (len(args) + pos20)
                    if (pos20 < 0):
                        pos20 = 0
                    res20 = args[pos20:(pos20 + 2)]
                    del args[pos20:(pos20 + 2)]
                    break
                elif (tag == "--index"):
                    more = True
                    self.flags.always_show_order = True
                    self.flags.never_show_order = False
                    pos21 = i
                    if (pos21 < 0):
                        pos21 = (len(args) + pos21)
                    if (pos21 < 0):
                        pos21 = 0
                    res21 = args[pos21:(pos21 + 1)]
                    del args[pos21:(pos21 + 1)]
                    break
                elif (tag == "--www"):
                    more = True
                    self.output_format = "www"
                    self.output_format_set = True
                    pos22 = i
                    if (pos22 < 0):
                        pos22 = (len(args) + pos22)
                    if (pos22 < 0):
                        pos22 = 0
                    res22 = args[pos22:(pos22 + 1)]
                    del args[pos22:(pos22 + 1)]
                elif (tag == "--table"):
                    more = True
                    self.flags.addTable(python_internal_ArrayImpl._get(args, (i + 1)))
                    pos23 = i
                    if (pos23 < 0):
                        pos23 = (len(args) + pos23)
                    if (pos23 < 0):
                        pos23 = 0
                    res23 = args[pos23:(pos23 + 2)]
                    del args[pos23:(pos23 + 2)]
                    break
                elif ((tag == "-w") or ((tag == "--ignore-whitespace"))):
                    more = True
                    self.flags.ignore_whitespace = True
                    pos24 = i
                    if (pos24 < 0):
                        pos24 = (len(args) + pos24)
                    if (pos24 < 0):
                        pos24 = 0
                    res24 = args[pos24:(pos24 + 1)]
                    del args[pos24:(pos24 + 1)]
                    break
                elif ((tag == "-i") or ((tag == "--ignore-case"))):
                    more = True
                    self.flags.ignore_case = True
                    pos25 = i
                    if (pos25 < 0):
                        pos25 = (len(args) + pos25)
                    if (pos25 < 0):
                        pos25 = 0
                    res25 = args[pos25:(pos25 + 1)]
                    del args[pos25:(pos25 + 1)]
                    break
                elif ((tag == "-d") or ((tag == "--ignore-epsilon"))):
                    more = True
                    eps = python_internal_ArrayImpl._get(args, (i + 1))
                    self.flags.ignore_epsilon = Std.parseFloat(eps)
                    if python_lib_Math.isnan(self.flags.ignore_epsilon):
                        io.writeStderr("Epsilon for numeric comparison must be numeric\n")
                        return 1
                    pos26 = i
                    if (pos26 < 0):
                        pos26 = (len(args) + pos26)
                    if (pos26 < 0):
                        pos26 = 0
                    res26 = args[pos26:(pos26 + 2)]
                    del args[pos26:(pos26 + 2)]
                    break
                elif (tag == "--padding"):
                    more = True
                    self.flags.padding_strategy = python_internal_ArrayImpl._get(args, (i + 1))
                    pos27 = i
                    if (pos27 < 0):
                        pos27 = (len(args) + pos27)
                    if (pos27 < 0):
                        pos27 = 0
                    res27 = args[pos27:(pos27 + 2)]
                    del args[pos27:(pos27 + 2)]
                    break
                elif ((tag == "-e") or ((tag == "--eol"))):
                    more = True
                    ending = python_internal_ArrayImpl._get(args, (i + 1))
                    if (ending == "crlf"):
                        ending = "\r\n"
                    elif (ending == "lf"):
                        ending = "\n"
                    elif (ending == "cr"):
                        ending = "\r"
                    elif (ending == "auto"):
                        ending = None
                    else:
                        io.writeStderr((("Expected line ending of either 'crlf' or 'lf' but got " + ("null" if ending is None else ending)) + "\n"))
                        return 1
                    self.csv_eol_preference = ending
                    pos28 = i
                    if (pos28 < 0):
                        pos28 = (len(args) + pos28)
                    if (pos28 < 0):
                        pos28 = 0
                    res28 = args[pos28:(pos28 + 2)]
                    del args[pos28:(pos28 + 2)]
                    break
                elif (tag == "--fail-if-diff"):
                    more = True
                    self.fail_if_diff = True
                    pos29 = i
                    if (pos29 < 0):
                        pos29 = (len(args) + pos29)
                    if (pos29 < 0):
                        pos29 = 0
                    res29 = args[pos29:(pos29 + 1)]
                    del args[pos29:(pos29 + 1)]
                    break
                elif (((tag == "help") or ((tag == "-h"))) or ((tag == "--help"))):
                    more = True
                    pos30 = i
                    if (pos30 < 0):
                        pos30 = (len(args) + pos30)
                    if (pos30 < 0):
                        pos30 = 0
                    res30 = args[pos30:(pos30 + 1)]
                    del args[pos30:(pos30 + 1)]
                    help = True
                    break
        cmd = (args[0] if 0 < len(args) else None)
        ok = True
        if help:
            cmd = ""
            args = []
        try:
            if (len(args) < 2):
                if (cmd == "version"):
                    io.writeStdout((HxOverrides.stringOrNull(Coopy.VERSION) + "\n"))
                    return 0
                if (cmd == "git"):
                    io.writeStdout("You can use daff to improve git's handling of csv files, by using it as a\ndiff driver (for showing what has changed) and as a merge driver (for merging\nchanges between multiple versions).\n")
                    io.writeStdout("\n")
                    io.writeStdout("Automatic setup\n")
                    io.writeStdout("---------------\n\n")
                    io.writeStdout("Run:\n")
                    io.writeStdout("  daff git csv\n")
                    io.writeStdout("\n")
                    io.writeStdout("Manual setup\n")
                    io.writeStdout("------------\n\n")
                    io.writeStdout("Create and add a file called .gitattributes in the root directory of your\nrepository, containing:\n\n")
                    io.writeStdout("  *.csv diff=daff-csv\n")
                    io.writeStdout("  *.csv merge=daff-csv\n")
                    io.writeStdout("\nCreate a file called .gitconfig in your home directory (or alternatively\nopen .git/config for a particular repository) and add:\n\n")
                    io.writeStdout("  [diff \"daff-csv\"]\n")
                    io.writeStdout("  command = daff diff --git\n")
                    io.writeStderr("\n")
                    io.writeStdout("  [merge \"daff-csv\"]\n")
                    io.writeStdout("  name = daff tabular merge\n")
                    io.writeStdout("  driver = daff merge --output %A %O %A %B\n\n")
                    io.writeStderr("Make sure you can run daff from the command-line as just \"daff\" - if not,\nreplace \"daff\" in the driver and command lines above with the correct way\nto call it. Add --no-color if your terminal does not support ANSI colors.")
                    io.writeStderr("\n")
                    return 0
                if (len(args) < 1):
                    io.writeStderr("daff can produce and apply tabular diffs.\n")
                    io.writeStderr("Call as:\n")
                    io.writeStderr("  daff a.csv b.csv\n")
                    io.writeStderr("  daff [--color] [--no-color] [--output OUTPUT.csv] a.csv b.csv\n")
                    io.writeStderr("  daff [--output OUTPUT.html] a.csv b.csv\n")
                    io.writeStderr("  daff [--www] a.csv b.csv\n")
                    io.writeStderr("  daff parent.csv a.csv b.csv\n")
                    io.writeStderr("  daff --input-format sqlite a.db b.db\n")
                    io.writeStderr("  daff patch [--inplace] a.csv patch.csv\n")
                    io.writeStderr("  daff merge [--inplace] parent.csv a.csv b.csv\n")
                    io.writeStderr("  daff trim [--output OUTPUT.csv] source.csv\n")
                    io.writeStderr("  daff render [--output OUTPUT.html] diff.csv\n")
                    io.writeStderr("  daff copy in.csv out.tsv\n")
                    io.writeStderr("  daff in.csv\n")
                    io.writeStderr("  daff git\n")
                    io.writeStderr("  daff version\n")
                    io.writeStderr("\n")
                    io.writeStderr("The --inplace option to patch and merge will result in modification of a.csv.\n")
                    io.writeStderr("\n")
                    io.writeStderr("If you need more control, here is the full list of flags:\n")
                    io.writeStderr("  daff diff [--output OUTPUT.csv] [--context NUM] [--all] [--act ACT] a.csv b.csv\n")
                    io.writeStderr("     --act ACT:     show only a certain kind of change (update, insert, delete, column)\n")
                    io.writeStderr("     --all:         do not prune unchanged rows or columns\n")
                    io.writeStderr("     --all-rows:    do not prune unchanged rows\n")
                    io.writeStderr("     --all-columns: do not prune unchanged columns\n")
                    io.writeStderr("     --color:       highlight changes with terminal colors (default in terminals)\n")
                    io.writeStderr("     --context NUM: show NUM rows of context (0=none)\n")
                    io.writeStderr("     --context-columns NUM: show NUM columns of context (0=none)\n")
                    io.writeStderr("     --fail-if-diff: return status is 0 if equal, 1 if different, 2 if problem\n")
                    io.writeStderr("     --id:          specify column name to use as primary key (repeat for multi-column key)\n")
                    io.writeStderr("     --ignore:      specify column name to ignore completely (can repeat)\n")
                    io.writeStderr("     --index:       include row/columns numbers from original tables\n")
                    io.writeStderr("     --input-format [csv|tsv|ssv|psv|json|sqlite]: set format to expect for input\n")
                    io.writeStderr("     --eol [crlf|lf|cr|auto]: separator between rows of csv output.\n")
                    io.writeStderr("     --no-color:    make sure terminal colors are not used\n")
                    io.writeStderr("     --ordered:     assume row order is meaningful (default for CSV)\n")
                    io.writeStderr("     --output-format [csv|tsv|ssv|psv|json|copy|html]: set format for output\n")
                    io.writeStderr("     --padding [dense|sparse|smart]: set padding method for aligning columns\n")
                    io.writeStderr("     --table NAME:  compare the named table, used with SQL sources. If name changes, use 'n1:n2'\n")
                    io.writeStderr("     --unordered:   assume row order is meaningless (default for json formats)\n")
                    io.writeStderr("     -w / --ignore-whitespace: ignore changes in leading/trailing whitespace\n")
                    io.writeStderr("     -i / --ignore-case: ignore differences in case\n")
                    io.writeStderr("     -d EPS / --ignore-epsilon EPS: ignore small floating point differences\n")
                    io.writeStderr("\n")
                    io.writeStderr("  daff render [--output OUTPUT.html] [--css CSS.css] [--fragment] [--plain] diff.csv\n")
                    io.writeStderr("     --css CSS.css: generate a suitable css file to go with the html\n")
                    io.writeStderr("     --fragment:    generate just a html fragment rather than a page\n")
                    io.writeStderr("     --plain:       do not use fancy utf8 characters to make arrows prettier\n")
                    io.writeStderr("     --unquote:     do not quote html characters in html diffs\n")
                    io.writeStderr("     --www:         send output to a browser\n")
                    return 1
            cmd = (args[0] if 0 < len(args) else None)
            offset = 1
            if (not Lambda.has(["diff", "patch", "merge", "trim", "render", "git", "version", "copy"],cmd)):
                startIndex = None
                if (((cmd.find("--") if ((startIndex is None)) else HxString.indexOfImpl(cmd,"--",startIndex))) == 0):
                    cmd = "diff"
                    offset = 0
                else:
                    startIndex = None
                    if (((cmd.find(".") if ((startIndex is None)) else HxString.indexOfImpl(cmd,".",startIndex))) != -1):
                        if (len(args) == 2):
                            cmd = "diff"
                            offset = 0
                        elif (len(args) == 1):
                            cmd = "copy"
                            offset = 0
            if (cmd == "git"):
                _hx_len = (len(args) - offset)
                pos = offset
                if (pos < 0):
                    pos = (len(args) + pos)
                if (pos < 0):
                    pos = 0
                res = args[pos:(pos + _hx_len)]
                del args[pos:(pos + _hx_len)]
                types = res
                return self.installGitDriver(io,types)
            if git:
                ct = (len(args) - offset)
                if ((ct != 7) and ((ct != 9))):
                    io.writeStderr((("Expected 7 or 9 parameters from git, but got " + Std.string(ct)) + "\n"))
                    return 1
                pos = offset
                if (pos < 0):
                    pos = (len(args) + pos)
                if (pos < 0):
                    pos = 0
                res = args[pos:(pos + ct)]
                del args[pos:(pos + ct)]
                git_args = res
                _hx_len = len(args)
                pos = 0
                if (pos < 0):
                    pos = (len(args) + pos)
                if (pos < 0):
                    pos = 0
                res = args[pos:(pos + _hx_len)]
                del args[pos:(pos + _hx_len)]
                offset = 0
                old_display_path = (git_args[0] if 0 < len(git_args) else None)
                new_display_path = (git_args[0] if 0 < len(git_args) else None)
                old_file = (git_args[1] if 1 < len(git_args) else None)
                new_file = (git_args[4] if 4 < len(git_args) else None)
                if (ct == 9):
                    io.writeStdout((git_args[8] if 8 < len(git_args) else None))
                    new_display_path = (git_args[7] if 7 < len(git_args) else None)
                io.writeStdout((("--- a/" + ("null" if old_display_path is None else old_display_path)) + "\n"))
                io.writeStdout((("+++ b/" + ("null" if new_display_path is None else new_display_path)) + "\n"))
                args.append(old_file)
                args.append(new_file)
            parent = None
            if ((len(args) - offset) >= 3):
                parent = self.loadTable((args[offset] if offset >= 0 and offset < len(args) else None),"parent")
                offset = (offset + 1)
            aname = (args[offset] if offset >= 0 and offset < len(args) else None)
            a = self.loadTable(aname,"local")
            b = None
            if ((len(args) - offset) >= 2):
                if (cmd != "copy"):
                    b = self.loadTable(python_internal_ArrayImpl._get(args, (1 + offset)),"remote")
                else:
                    output = python_internal_ArrayImpl._get(args, (1 + offset))
            self.flags.diff_strategy = self.strategy
            if inplace:
                if (output is not None):
                    io.writeStderr("Please do not use --inplace when specifying an output.\n")
                output = aname
                return 1
            if (output is None):
                output = "-"
            if (cmd == "diff"):
                if (not self.order_set):
                    self.flags.ordered = self.order_preference
                    if (not self.flags.ordered):
                        self.flags.unchanged_context = 0
                self.flags.allow_nested_cells = self.nested_output
                if self.fail_if_diff:
                    try:
                        self.runDiff(parent,a,b,self.flags,output)
                    except BaseException as _g:
                        None
                        return 2
                    if self.diffs_found:
                        return 1
                else:
                    self.runDiff(parent,a,b,self.flags,output)
            elif (cmd == "patch"):
                patcher = HighlightPatch(a,b)
                patcher.apply()
                self.saveTable(output,a)
            elif (cmd == "merge"):
                merger = Merger(parent,a,b,self.flags)
                conflicts = merger.apply()
                ok = (conflicts == 0)
                if (conflicts > 0):
                    io.writeStderr((((Std.string(conflicts) + " conflict") + HxOverrides.stringOrNull((("s" if ((conflicts > 1)) else "")))) + "\n"))
                self.saveTable(output,a)
            elif (cmd == "trim"):
                self.saveTable(output,a)
            elif (cmd == "render"):
                self.renderTable(output,a)
            elif (cmd == "copy"):
                os = Tables(a)
                os.add("untitled")
                self.saveTables(output,os,self.useColor(self.flags,output),False)
        except BaseException as _g:
            None
            e = haxe_Exception.caught(_g).unwrap()
            if (not self.fail_if_diff):
                raise haxe_Exception.thrown(e)
            return 2
        if ok:
            return 0
        elif self.fail_if_diff:
            return 2
        else:
            return 1

    def coopyhx(self,io):
        args = io.args()
        if ((args[0] if 0 < len(args) else None) == "--keep"):
            return Coopy.keepAround()
        return self.run(args,io)

    @staticmethod
    def diffAsHtml(local,remote,flags = None):
        comp = TableComparisonState()
        td = Coopy.align(local,remote,flags,comp)
        o = Coopy.getBlankTable(td,comp)
        if (comp.a is not None):
            o = comp.a.create()
        if ((o is None) and ((comp.b is not None))):
            o = comp.b.create()
        if (o is None):
            o = SimpleTable(0,0)
        os = Tables(o)
        td.hiliteWithNesting(os)
        render = DiffRender()
        return render.renderTables(os).html()

    @staticmethod
    def diffAsAnsi(local,remote,flags = None):
        tool = Coopy(TableIO())
        tool.cache_txt = ""
        if (flags is None):
            flags = CompareFlags()
        tool.output_format = "csv"
        tool.runDiff(flags.parent,local,remote,flags,None)
        return tool.cache_txt

    @staticmethod
    def diff(local,remote,flags = None):
        comp = TableComparisonState()
        td = Coopy.align(local,remote,flags,comp)
        o = Coopy.getBlankTable(td,comp)
        if (comp.a is not None):
            o = comp.a.create()
        if ((o is None) and ((comp.b is not None))):
            o = comp.b.create()
        if (o is None):
            o = SimpleTable(0,0)
        td.hilite(o)
        return o

    @staticmethod
    def getBlankTable(td,comp):
        o = None
        if (comp.a is not None):
            o = comp.a.create()
        if ((o is None) and ((comp.b is not None))):
            o = comp.b.create()
        if (o is None):
            o = SimpleTable(0,0)
        return o

    @staticmethod
    def align(local,remote,flags,comp):
        comp.a = Coopy.tablify(local)
        comp.b = Coopy.tablify(remote)
        if (flags is None):
            flags = CompareFlags()
        comp.compare_flags = flags
        ct = CompareTable(comp)
        align = ct.align()
        td = TableDiff(align,flags)
        return td

    @staticmethod
    def patch(local,patch,flags = None):
        patcher = HighlightPatch(Coopy.tablify(local),Coopy.tablify(patch))
        return patcher.apply()

    @staticmethod
    def compareTables(local,remote,flags = None):
        comp = TableComparisonState()
        comp.a = Coopy.tablify(local)
        comp.b = Coopy.tablify(remote)
        comp.compare_flags = flags
        ct = CompareTable(comp)
        return ct

    @staticmethod
    def compareTables3(parent,local,remote,flags = None):
        comp = TableComparisonState()
        comp.p = Coopy.tablify(parent)
        comp.a = Coopy.tablify(local)
        comp.b = Coopy.tablify(remote)
        comp.compare_flags = flags
        ct = CompareTable(comp)
        return ct

    @staticmethod
    def keepAround():
        st = SimpleTable(1,1)
        v = Viterbi()
        td = TableDiff(None,None)
        cf = CompareFlags()
        idx = Index(cf)
        dr = DiffRender()
        hp = HighlightPatch(None,None)
        csv = Csv()
        tm = TableModifier(None)
        sc = SqlCompare(None,None,None,None,None)
        sq = SqliteHelper()
        sm = SimpleMeta(None)
        ct = CombinedTable(None)
        return 0

    @staticmethod
    def cellFor(x):
        return x

    @staticmethod
    def main():
        io = TableIO()
        coopy = Coopy()
        ret = coopy.coopyhx(io)
        if (ret != 0):
            Sys.exit(ret)

    @staticmethod
    def show(t):
        w = t.get_width()
        h = t.get_height()
        txt = ""
        _g = 0
        _g1 = h
        while (_g < _g1):
            y = _g
            _g = (_g + 1)
            _g2 = 0
            _g3 = w
            while (_g2 < _g3):
                x = _g2
                _g2 = (_g2 + 1)
                txt = (("null" if txt is None else txt) + Std.string(t.getCell(x,y)))
                txt = (("null" if txt is None else txt) + " ")
            txt = (("null" if txt is None else txt) + "\n")
        print(str(txt))

    @staticmethod
    def jsonify(t):
        workbook = haxe_ds_StringMap()
        sheet = list()
        w = t.get_width()
        h = t.get_height()
        txt = ""
        _g = 0
        _g1 = h
        while (_g < _g1):
            y = _g
            _g = (_g + 1)
            row = list()
            _g2 = 0
            _g3 = w
            while (_g2 < _g3):
                x = _g2
                _g2 = (_g2 + 1)
                v = t.getCell(x,y)
                row.append(v)
            sheet.append(row)
        workbook.h["sheet"] = sheet
        return workbook

    @staticmethod
    def tablify(data):
        if (data is None):
            return data
        get_cell_view = Reflect.field(data,"getCellView")
        if (get_cell_view is not None):
            return data
        daff = __import__('daff')
        return daff.PythonTableView(data)

Coopy._hx_class = Coopy


class CrossMatch:
    _hx_class_name = "CrossMatch"
    __slots__ = ("spot_a", "spot_b", "item_a", "item_b")
    _hx_fields = ["spot_a", "spot_b", "item_a", "item_b"]

    def __init__(self):
        self.item_b = None
        self.item_a = None
        self.spot_b = None
        self.spot_a = None

CrossMatch._hx_class = CrossMatch


class Csv:
    _hx_class_name = "Csv"
    __slots__ = ("cursor", "row_ended", "has_structure", "delim", "discovered_eol", "preferred_eol")
    _hx_fields = ["cursor", "row_ended", "has_structure", "delim", "discovered_eol", "preferred_eol"]
    _hx_methods = ["renderTable", "renderCell", "parseTable", "makeTable", "parseCellPart", "parseCell", "getDiscoveredEol", "setPreferredEol"]

    def __init__(self,delim = None,eol = None):
        if (delim is None):
            delim = ","
        self.has_structure = None
        self.cursor = 0
        self.row_ended = False
        self.delim = ("," if ((delim is None)) else delim)
        self.discovered_eol = None
        self.preferred_eol = eol

    def renderTable(self,t):
        eol = self.preferred_eol
        if (eol is None):
            eol = "\r\n"
        result = ""
        v = t.getCellView()
        stream = TableStream(t)
        w = stream.width()
        txts = list()
        while stream.fetch():
            _g = 0
            _g1 = w
            while (_g < _g1):
                x = _g
                _g = (_g + 1)
                if (x > 0):
                    x1 = self.delim
                    txts.append(x1)
                x2 = self.renderCell(v,stream.getCell(x))
                txts.append(x2)
            txts.append(eol)
        return "".join([python_Boot.toString1(x1,'') for x1 in txts])

    def renderCell(self,v,d,force_quote = None):
        if (force_quote is None):
            force_quote = False
        if (d is None):
            return "NULL"
        _hx_str = v.toString(d)
        need_quote = force_quote
        if (not need_quote):
            if (len(_hx_str) > 0):
                tmp = None
                if ((("" if ((0 >= len(_hx_str))) else _hx_str[0])) != " "):
                    index = (len(_hx_str) - 1)
                    tmp = ((("" if (((index < 0) or ((index >= len(_hx_str))))) else _hx_str[index])) == " ")
                else:
                    tmp = True
                if tmp:
                    need_quote = True
        if (not need_quote):
            _g = 0
            _g1 = len(_hx_str)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                ch = ("" if (((i < 0) or ((i >= len(_hx_str))))) else _hx_str[i])
                if ((((ch == "\"") or ((ch == "\r"))) or ((ch == "\n"))) or ((ch == "\t"))):
                    need_quote = True
                    break
                _this = self.delim
                if (ch == (("" if ((0 >= len(_this))) else _this[0]))):
                    if (len(self.delim) == 1):
                        need_quote = True
                        break
                    if ((i + len(self.delim)) <= len(_hx_str)):
                        match = True
                        _g2 = 1
                        _g3 = len(self.delim)
                        while (_g2 < _g3):
                            j = _g2
                            _g2 = (_g2 + 1)
                            index = (i + j)
                            tmp = ("" if (((index < 0) or ((index >= len(_hx_str))))) else _hx_str[index])
                            _this1 = self.delim
                            if (tmp != (("" if (((j < 0) or ((j >= len(_this1))))) else _this1[j]))):
                                match = False
                                break
                        if match:
                            need_quote = True
                            break
        result = ""
        if need_quote:
            result = (("null" if result is None else result) + "\"")
        line_buf = ""
        _g = 0
        _g1 = len(_hx_str)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            ch = ("" if (((i < 0) or ((i >= len(_hx_str))))) else _hx_str[i])
            if (ch == "\""):
                result = (("null" if result is None else result) + "\"")
            if ((ch != "\r") and ((ch != "\n"))):
                if (len(line_buf) > 0):
                    result = (("null" if result is None else result) + ("null" if line_buf is None else line_buf))
                    line_buf = ""
                result = (("null" if result is None else result) + ("null" if ch is None else ch))
            else:
                line_buf = (("null" if line_buf is None else line_buf) + ("null" if ch is None else ch))
        if (len(line_buf) > 0):
            result = (("null" if result is None else result) + ("null" if line_buf is None else line_buf))
        if need_quote:
            result = (("null" if result is None else result) + "\"")
        return result

    def parseTable(self,txt,tab):
        if (not tab.isResizable()):
            return False
        self.cursor = 0
        self.row_ended = False
        self.has_structure = True
        tab.resize(0,0)
        w = 0
        h = 0
        at = 0
        yat = 0
        while (self.cursor < len(txt)):
            cell = self.parseCellPart(txt)
            if (yat >= h):
                h = (yat + 1)
                tab.resize(w,h)
            if (at >= w):
                if (yat > 0):
                    if ((cell != "") and ((cell is not None))):
                        context = ""
                        _g = 0
                        _g1 = w
                        while (_g < _g1):
                            i = _g
                            _g = (_g + 1)
                            if (i > 0):
                                context = (("null" if context is None else context) + ",")
                            context = (("null" if context is None else context) + Std.string(tab.getCell(i,yat)))
                        print(str(((((("Ignored overflowing row " + Std.string(yat)) + " with cell '") + ("null" if cell is None else cell)) + "' after: ") + ("null" if context is None else context))))
                else:
                    w = (at + 1)
                    tab.resize(w,h)
            tab.setCell(at,(h - 1),cell)
            at = (at + 1)
            if self.row_ended:
                at = 0
                yat = (yat + 1)
            _hx_local_4 = self
            _hx_local_5 = _hx_local_4.cursor
            _hx_local_4.cursor = (_hx_local_5 + 1)
            _hx_local_5
        return True

    def makeTable(self,txt):
        tab = SimpleTable(0,0)
        self.parseTable(txt,tab)
        return tab

    def parseCellPart(self,txt):
        if (txt is None):
            return None
        self.row_ended = False
        first_non_underscore = len(txt)
        last_processed = 0
        quoting = False
        quote = 0
        result = ""
        start = self.cursor
        _g = self.cursor
        _g1 = len(txt)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            ch = HxString.charCodeAt(txt,i)
            last_processed = i
            if ((ch != 95) and ((i < first_non_underscore))):
                first_non_underscore = i
            if self.has_structure:
                if (not quoting):
                    if (ch == HxString.charCodeAt(self.delim,0)):
                        if (len(self.delim) == 1):
                            break
                        if ((i + len(self.delim)) <= len(txt)):
                            match = True
                            _g2 = 1
                            _g3 = len(self.delim)
                            while (_g2 < _g3):
                                j = _g2
                                _g2 = (_g2 + 1)
                                index = (i + j)
                                tmp = ("" if (((index < 0) or ((index >= len(txt))))) else txt[index])
                                _this = self.delim
                                if (tmp != (("" if (((j < 0) or ((j >= len(_this))))) else _this[j]))):
                                    match = False
                                    break
                            if match:
                                last_processed = (last_processed + ((len(self.delim) - 1)))
                                break
                    if ((ch == 13) or ((ch == 10))):
                        ch2 = HxString.charCodeAt(txt,(i + 1))
                        if (ch2 is not None):
                            if (ch2 != ch):
                                if ((ch2 == 13) or ((ch2 == 10))):
                                    if (self.discovered_eol is None):
                                        self.discovered_eol = (HxOverrides.stringOrNull("".join(map(chr,[ch]))) + HxOverrides.stringOrNull("".join(map(chr,[ch2]))))
                                    last_processed = (last_processed + 1)
                        if (self.discovered_eol is None):
                            self.discovered_eol = "".join(map(chr,[ch]))
                        self.row_ended = True
                        break
                    if (ch == 34):
                        if (i == self.cursor):
                            quoting = True
                            quote = ch
                            if (i != start):
                                result = (("null" if result is None else result) + HxOverrides.stringOrNull("".join(map(chr,[ch]))))
                            continue
                        elif (ch == quote):
                            quoting = True
                    result = (("null" if result is None else result) + HxOverrides.stringOrNull("".join(map(chr,[ch]))))
                    continue
                if (ch == quote):
                    quoting = False
                    continue
            result = (("null" if result is None else result) + HxOverrides.stringOrNull("".join(map(chr,[ch]))))
        self.cursor = last_processed
        if (quote == 0):
            if (result == "NULL"):
                return None
            if (first_non_underscore > start):
                _hx_del = (first_non_underscore - start)
                if (HxString.substr(result,_hx_del,None) == "NULL"):
                    return HxString.substr(result,1,None)
        return result

    def parseCell(self,txt):
        self.cursor = 0
        self.row_ended = False
        self.has_structure = False
        return self.parseCellPart(txt)

    def getDiscoveredEol(self):
        return self.discovered_eol

    def setPreferredEol(self,eol):
        self.preferred_eol = eol

Csv._hx_class = Csv


class Date:
    _hx_class_name = "Date"
    __slots__ = ("date", "dateUTC")
    _hx_fields = ["date", "dateUTC"]
    _hx_methods = ["toString"]
    _hx_statics = ["makeLocal"]

    def __init__(self,year,month,day,hour,_hx_min,sec):
        self.dateUTC = None
        if (year < python_lib_datetime_Datetime.min.year):
            year = python_lib_datetime_Datetime.min.year
        if (day == 0):
            day = 1
        self.date = Date.makeLocal(python_lib_datetime_Datetime(year,(month + 1),day,hour,_hx_min,sec,0))
        self.dateUTC = self.date.astimezone(python_lib_datetime_Timezone.utc)

    def toString(self):
        return self.date.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def makeLocal(date):
        try:
            return date.astimezone()
        except BaseException as _g:
            None
            tzinfo = python_lib_datetime_Datetime.now(python_lib_datetime_Timezone.utc).astimezone().tzinfo
            return date.replace(**python__KwArgs_KwArgs_Impl_.fromT(_hx_AnonObject({'tzinfo': tzinfo})))

Date._hx_class = Date


class DiffRender:
    _hx_class_name = "DiffRender"
    __slots__ = ("text_to_insert", "td_open", "td_close", "open", "pretty_arrows", "quote_html", "section")
    _hx_fields = ["text_to_insert", "td_open", "td_close", "open", "pretty_arrows", "quote_html", "section"]
    _hx_methods = ["usePrettyArrows", "quoteHtml", "insert", "beginTable", "setSection", "beginRow", "insertCell", "endRow", "endTable", "html", "toString", "render", "renderTables", "sampleCss", "completeHtml"]
    _hx_statics = ["examineCell", "markSpaces", "renderCell"]

    def __init__(self):
        self.section = None
        self.td_close = None
        self.td_open = None
        self.text_to_insert = list()
        self.open = False
        self.pretty_arrows = True
        self.quote_html = True

    def usePrettyArrows(self,flag):
        self.pretty_arrows = flag

    def quoteHtml(self,flag):
        self.quote_html = flag

    def insert(self,_hx_str):
        _this = self.text_to_insert
        _this.append(_hx_str)

    def beginTable(self):
        self.insert("<table>\n")
        self.section = None

    def setSection(self,_hx_str):
        if (_hx_str == self.section):
            return
        if (self.section is not None):
            self.insert("</t")
            self.insert(self.section)
            self.insert(">\n")
        self.section = _hx_str
        if (self.section is not None):
            self.insert("<t")
            self.insert(self.section)
            self.insert(">\n")

    def beginRow(self,mode):
        self.td_open = "<td"
        self.td_close = "</td>"
        row_class = ""
        if (mode == "header"):
            self.td_open = "<th"
            self.td_close = "</th>"
        row_class = mode
        tr = "<tr>"
        if (row_class != ""):
            tr = (("<tr class=\"" + ("null" if row_class is None else row_class)) + "\">")
        self.insert(tr)

    def insertCell(self,txt,mode):
        cell_decorate = ""
        if (mode != ""):
            cell_decorate = ((" class=\"" + ("null" if mode is None else mode)) + "\"")
        self.insert(((HxOverrides.stringOrNull(self.td_open) + ("null" if cell_decorate is None else cell_decorate)) + ">"))
        if (txt is not None):
            self.insert(txt)
        else:
            self.insert("null")
        self.insert(self.td_close)

    def endRow(self):
        self.insert("</tr>\n")

    def endTable(self):
        self.setSection(None)
        self.insert("</table>\n")

    def html(self):
        _this = self.text_to_insert
        return "".join([python_Boot.toString1(x1,'') for x1 in _this])

    def toString(self):
        return self.html()

    def render(self,tab):
        tab = Coopy.tablify(tab)
        if ((tab.get_width() == 0) or ((tab.get_height() == 0))):
            return self
        render = self
        render.beginTable()
        change_row = -1
        cell = CellInfo()
        view = tab.getCellView()
        corner = view.toString(tab.getCell(0,0))
        off = (1 if ((corner == "@:@")) else 0)
        if (off > 0):
            if ((tab.get_width() <= 1) or ((tab.get_height() <= 1))):
                return self
        _g = 0
        _g1 = tab.get_height()
        while (_g < _g1):
            row = _g
            _g = (_g + 1)
            open = False
            txt = view.toString(tab.getCell(off,row))
            if (txt is None):
                txt = ""
            DiffRender.examineCell(off,row,view,txt,"",txt,corner,cell,off)
            row_mode = cell.category
            if (row_mode == "spec"):
                change_row = row
            if ((((row_mode == "header") or ((row_mode == "spec"))) or ((row_mode == "index"))) or ((row_mode == "meta"))):
                self.setSection("head")
            else:
                self.setSection("body")
            render.beginRow(row_mode)
            _g2 = 0
            _g3 = tab.get_width()
            while (_g2 < _g3):
                c = _g2
                _g2 = (_g2 + 1)
                DiffRender.examineCell(c,row,view,tab.getCell(c,row),(view.toString(tab.getCell(c,change_row)) if ((change_row >= 0)) else ""),txt,corner,cell,off)
                val = (cell.pretty_value if (self.pretty_arrows) else cell.value)
                if self.quote_html:
                    val = StringTools.htmlEscape(view.toString(val))
                render.insertCell(val,cell.category_given_tr)
            render.endRow()
        render.endTable()
        return self

    def renderTables(self,tabs):
        order = tabs.getOrder()
        start = 0
        if ((len(order) <= 1) or tabs.hasInsDel()):
            self.render(tabs.one())
            start = 1
        _g = start
        _g1 = len(order)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            name = (order[i] if i >= 0 and i < len(order) else None)
            tab = tabs.get(name)
            if (tab.get_height() <= 1):
                continue
            self.insert("<h3>")
            self.insert(name)
            self.insert("</h3>\n")
            self.render(tab)
        return self

    def sampleCss(self):
        return ".highlighter .add { \n  background-color: #7fff7f;\n}\n\n.highlighter .remove { \n  background-color: #ff7f7f;\n}\n\n.highlighter td.modify { \n  background-color: #7f7fff;\n}\n\n.highlighter td.conflict { \n  background-color: #f00;\n}\n\n.highlighter .spec { \n  background-color: #aaa;\n}\n\n.highlighter .move { \n  background-color: #ffa;\n}\n\n.highlighter .null { \n  color: #888;\n}\n\n.highlighter table { \n  border-collapse:collapse;\n}\n\n.highlighter td, .highlighter th {\n  border: 1px solid #2D4068;\n  padding: 3px 7px 2px;\n}\n\n.highlighter th, .highlighter .header, .highlighter .meta {\n  background-color: #aaf;\n  font-weight: bold;\n  padding-bottom: 4px;\n  padding-top: 5px;\n  text-align:left;\n}\n\n.highlighter tr.header th {\n  border-bottom: 2px solid black;\n}\n\n.highlighter tr.index td, .highlighter .index, .highlighter tr.header th.index {\n  background-color: white;\n  border: none;\n}\n\n.highlighter .gap {\n  color: #888;\n}\n\n.highlighter td {\n  empty-cells: show;\n  white-space: pre-wrap;\n}\n"

    def completeHtml(self):
        self.text_to_insert.insert(0, "<!DOCTYPE html>\n<html>\n<head>\n<meta charset='utf-8'>\n<style TYPE='text/css'>\n")
        _this = self.text_to_insert
        x = self.sampleCss()
        _this.insert(1, x)
        self.text_to_insert.insert(2, "</style>\n</head>\n<body>\n<div class='highlighter'>\n")
        _this = self.text_to_insert
        _this.append("</div>\n</body>\n</html>\n")

    @staticmethod
    def examineCell(x,y,view,raw,vcol,vrow,vcorner,cell,offset = None):
        if (offset is None):
            offset = 0
        nested = view.isHash(raw)
        cell.category = ""
        cell.category_given_tr = ""
        cell.separator = ""
        cell.pretty_separator = ""
        cell.conflicted = False
        cell.updated = False
        def _hx_local_2():
            def _hx_local_1():
                def _hx_local_0():
                    cell.rvalue = None
                    return cell.rvalue
                cell.lvalue = _hx_local_0()
                return cell.lvalue
            cell.pvalue = _hx_local_1()
            return cell.pvalue
        cell.meta = _hx_local_2()
        cell.value = raw
        cell.pretty_value = cell.value
        if (vrow is None):
            vrow = ""
        if (vcol is None):
            vcol = ""
        if (((len(vrow) >= 3) and (((("" if ((0 >= len(vrow))) else vrow[0])) == "@"))) and (((("" if ((1 >= len(vrow))) else vrow[1])) != "@"))):
            idx = HxString.indexOfImpl(vrow,"@",1)
            if (idx >= 0):
                cell.meta = HxString.substr(vrow,1,(idx - 1))
                vrow = HxString.substr(vrow,(idx + 1),len(vrow))
                cell.category = "meta"
        removed_column = False
        if (vrow == ":"):
            cell.category = "move"
        if (((vrow == "") and ((offset == 1))) and ((y == 0))):
            cell.category = "index"
        startIndex = None
        if (((vcol.find("+++") if ((startIndex is None)) else HxString.indexOfImpl(vcol,"+++",startIndex))) >= 0):
            def _hx_local_3():
                cell.category = "add"
                return cell.category
            cell.category_given_tr = _hx_local_3()
        else:
            startIndex = None
            if (((vcol.find("---") if ((startIndex is None)) else HxString.indexOfImpl(vcol,"---",startIndex))) >= 0):
                def _hx_local_4():
                    cell.category = "remove"
                    return cell.category
                cell.category_given_tr = _hx_local_4()
                removed_column = True
        if (vrow == "!"):
            cell.category = "spec"
        elif (vrow == "@@"):
            cell.category = "header"
        elif (vrow == "..."):
            cell.category = "gap"
        elif (vrow == "+++"):
            if (not removed_column):
                cell.category = "add"
        elif (vrow == "---"):
            cell.category = "remove"
        else:
            startIndex = None
            if (((vrow.find("->") if ((startIndex is None)) else HxString.indexOfImpl(vrow,"->",startIndex))) >= 0):
                if (not removed_column):
                    tokens = vrow.split("!")
                    full = vrow
                    part = (tokens[1] if 1 < len(tokens) else None)
                    if (part is None):
                        part = full
                    _hx_str = view.toString(cell.value)
                    if (_hx_str is None):
                        _hx_str = ""
                    tmp = None
                    if (not nested):
                        startIndex = None
                        tmp = (((_hx_str.find(part) if ((startIndex is None)) else HxString.indexOfImpl(_hx_str,part,startIndex))) >= 0)
                    else:
                        tmp = True
                    if tmp:
                        cat = "modify"
                        div = part
                        if (part != full):
                            if nested:
                                cell.conflicted = view.hashExists(raw,"theirs")
                            else:
                                startIndex = None
                                cell.conflicted = (((_hx_str.find(full) if ((startIndex is None)) else HxString.indexOfImpl(_hx_str,full,startIndex))) >= 0)
                            if cell.conflicted:
                                div = full
                                cat = "conflict"
                        cell.updated = True
                        cell.separator = div
                        cell.pretty_separator = div
                        if nested:
                            if cell.conflicted:
                                tokens = [view.hashGet(raw,"before"), view.hashGet(raw,"ours"), view.hashGet(raw,"theirs")]
                            else:
                                tokens = [view.hashGet(raw,"before"), view.hashGet(raw,"after")]
                        else:
                            cell.pretty_value = view.toString(cell.pretty_value)
                            if (cell.pretty_value is None):
                                cell.pretty_value = ""
                            if (cell.pretty_value == div):
                                tokens = ["", ""]
                            else:
                                _this = cell.pretty_value
                                tokens = (list(_this) if ((div == "")) else _this.split(div))
                        pretty_tokens = tokens
                        if (len(tokens) >= 2):
                            python_internal_ArrayImpl._set(pretty_tokens, 0, DiffRender.markSpaces((tokens[0] if 0 < len(tokens) else None),(tokens[1] if 1 < len(tokens) else None)))
                            python_internal_ArrayImpl._set(pretty_tokens, 1, DiffRender.markSpaces((tokens[1] if 1 < len(tokens) else None),(tokens[0] if 0 < len(tokens) else None)))
                        if (len(tokens) >= 3):
                            ref = (pretty_tokens[0] if 0 < len(pretty_tokens) else None)
                            python_internal_ArrayImpl._set(pretty_tokens, 0, DiffRender.markSpaces(ref,(tokens[2] if 2 < len(tokens) else None)))
                            python_internal_ArrayImpl._set(pretty_tokens, 2, DiffRender.markSpaces((tokens[2] if 2 < len(tokens) else None),ref))
                        cell.pretty_separator = "".join(map(chr,[8594]))
                        cell.pretty_value = cell.pretty_separator.join([python_Boot.toString1(x1,'') for x1 in pretty_tokens])
                        def _hx_local_5():
                            cell.category = cat
                            return cell.category
                        cell.category_given_tr = _hx_local_5()
                        offset1 = (1 if (cell.conflicted) else 0)
                        cell.lvalue = (tokens[offset1] if offset1 >= 0 and offset1 < len(tokens) else None)
                        cell.rvalue = python_internal_ArrayImpl._get(tokens, (offset1 + 1))
                        if cell.conflicted:
                            cell.pvalue = (tokens[0] if 0 < len(tokens) else None)
        if ((x == 0) and ((offset > 0))):
            def _hx_local_6():
                cell.category = "index"
                return cell.category
            cell.category_given_tr = _hx_local_6()

    @staticmethod
    def markSpaces(sl,sr):
        if (sl == sr):
            return sl
        if ((sl is None) or ((sr is None))):
            return sl
        slc = StringTools.replace(sl," ","")
        src = StringTools.replace(sr," ","")
        if (slc != src):
            return sl
        slo = str("")
        il = 0
        ir = 0
        while (il < len(sl)):
            cl = ("" if (((il < 0) or ((il >= len(sl))))) else sl[il])
            cr = ""
            if (ir < len(sr)):
                cr = ("" if (((ir < 0) or ((ir >= len(sr))))) else sr[ir])
            if (cl == cr):
                slo = (("null" if slo is None else slo) + ("null" if cl is None else cl))
                il = (il + 1)
                ir = (ir + 1)
            elif (cr == " "):
                ir = (ir + 1)
            else:
                slo = (("null" if slo is None else slo) + HxOverrides.stringOrNull("".join(map(chr,[9251]))))
                il = (il + 1)
        return slo

    @staticmethod
    def renderCell(tab,view,x,y):
        cell = CellInfo()
        corner = view.toString(tab.getCell(0,0))
        off = (1 if ((corner == "@:@")) else 0)
        DiffRender.examineCell(x,y,view,tab.getCell(x,y),view.toString(tab.getCell(x,off)),view.toString(tab.getCell(off,y)),corner,cell,off)
        return cell

DiffRender._hx_class = DiffRender


class DiffSummary:
    _hx_class_name = "DiffSummary"
    __slots__ = ("row_deletes", "row_inserts", "row_updates", "row_reorders", "col_deletes", "col_inserts", "col_updates", "col_renames", "col_reorders", "row_count_initial_with_header", "row_count_final_with_header", "row_count_initial", "row_count_final", "col_count_initial", "col_count_final", "different")
    _hx_fields = ["row_deletes", "row_inserts", "row_updates", "row_reorders", "col_deletes", "col_inserts", "col_updates", "col_renames", "col_reorders", "row_count_initial_with_header", "row_count_final_with_header", "row_count_initial", "row_count_final", "col_count_initial", "col_count_final", "different"]

    def __init__(self):
        self.different = None
        self.col_count_final = None
        self.col_count_initial = None
        self.row_count_final = None
        self.row_count_initial = None
        self.row_count_final_with_header = None
        self.row_count_initial_with_header = None
        self.col_reorders = None
        self.col_renames = None
        self.col_updates = None
        self.col_inserts = None
        self.col_deletes = None
        self.row_reorders = None
        self.row_updates = None
        self.row_inserts = None
        self.row_deletes = None

DiffSummary._hx_class = DiffSummary


class FlatCellBuilder:
    _hx_class_name = "FlatCellBuilder"
    __slots__ = ("view", "separator", "conflict_separator", "flags")
    _hx_fields = ["view", "separator", "conflict_separator", "flags"]
    _hx_methods = ["needSeparator", "setSeparator", "setConflictSeparator", "setView", "update", "conflict", "marker", "links"]
    _hx_statics = ["quoteForDiff"]
    _hx_interfaces = [CellBuilder]

    def __init__(self,flags):
        self.conflict_separator = None
        self.separator = None
        self.view = None
        self.flags = flags

    def needSeparator(self):
        return True

    def setSeparator(self,separator):
        self.separator = separator

    def setConflictSeparator(self,separator):
        self.conflict_separator = separator

    def setView(self,view):
        self.view = view

    def update(self,local,remote):
        return self.view.toDatum(((HxOverrides.stringOrNull(FlatCellBuilder.quoteForDiff(self.view,local)) + HxOverrides.stringOrNull(self.separator)) + HxOverrides.stringOrNull(FlatCellBuilder.quoteForDiff(self.view,remote))))

    def conflict(self,parent,local,remote):
        return ((((HxOverrides.stringOrNull(self.view.toString(parent)) + HxOverrides.stringOrNull(self.conflict_separator)) + HxOverrides.stringOrNull(self.view.toString(local))) + HxOverrides.stringOrNull(self.conflict_separator)) + HxOverrides.stringOrNull(self.view.toString(remote)))

    def marker(self,label):
        return self.view.toDatum(label)

    def links(self,unit,row_like):
        if (self.flags.count_like_a_spreadsheet and (not row_like)):
            return self.view.toDatum(unit.toBase26String())
        return self.view.toDatum(unit.toString())

    @staticmethod
    def quoteForDiff(v,d):
        nil = "NULL"
        if v.equals(d,None):
            return nil
        _hx_str = v.toString(d)
        score = 0
        _g = 0
        _g1 = len(_hx_str)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            if (HxString.charCodeAt(_hx_str,score) != 95):
                break
            score = (score + 1)
        if (HxString.substr(_hx_str,score,None) == nil):
            _hx_str = ("_" + ("null" if _hx_str is None else _hx_str))
        return _hx_str

FlatCellBuilder._hx_class = FlatCellBuilder


class Row:
    _hx_class_name = "Row"
    __slots__ = ()
    _hx_methods = ["getRowString", "isPreamble"]
Row._hx_class = Row


class HighlightPatch:
    _hx_class_name = "HighlightPatch"
    __slots__ = ("source", "patch", "view", "sourceView", "csv", "header", "headerPre", "headerPost", "headerRename", "headerMove", "modifier", "currentRow", "payloadCol", "payloadTop", "mods", "cmods", "rowInfo", "cellInfo", "rcOffset", "indexes", "sourceInPatchCol", "patchInSourceCol", "destInPatchCol", "patchInDestCol", "patchInSourceRow", "lastSourceRow", "actions", "rowPermutation", "rowPermutationRev", "colPermutation", "colPermutationRev", "haveDroppedColumns", "headerRow", "preambleRow", "flags", "meta_change", "process_meta", "prev_meta", "next_meta", "finished_columns", "meta")
    _hx_fields = ["source", "patch", "view", "sourceView", "csv", "header", "headerPre", "headerPost", "headerRename", "headerMove", "modifier", "currentRow", "payloadCol", "payloadTop", "mods", "cmods", "rowInfo", "cellInfo", "rcOffset", "indexes", "sourceInPatchCol", "patchInSourceCol", "destInPatchCol", "patchInDestCol", "patchInSourceRow", "lastSourceRow", "actions", "rowPermutation", "rowPermutationRev", "colPermutation", "colPermutationRev", "haveDroppedColumns", "headerRow", "preambleRow", "flags", "meta_change", "process_meta", "prev_meta", "next_meta", "finished_columns", "meta"]
    _hx_methods = ["reset", "processMeta", "apply", "needSourceColumns", "needDestColumns", "needSourceIndex", "setMetaProp", "applyMetaRow", "applyRow", "getDatum", "getString", "getStringNull", "applyMeta", "applyHeader", "lookUp", "applyActionExternal", "applyAction", "checkAct", "getPreString", "getRowString", "isPreamble", "sortMods", "processMods", "useMetaForColumnChanges", "useMetaForRowChanges", "computeOrdering", "permuteRows", "fillInNewColumns", "finishRows", "permuteColumns", "finishColumns"]
    _hx_interfaces = [Row]

    def __init__(self,source,patch,flags = None):
        self.finished_columns = None
        self.next_meta = None
        self.prev_meta = None
        self.process_meta = None
        self.meta_change = None
        self.preambleRow = None
        self.headerRow = None
        self.haveDroppedColumns = None
        self.colPermutationRev = None
        self.colPermutation = None
        self.rowPermutationRev = None
        self.rowPermutation = None
        self.actions = None
        self.lastSourceRow = None
        self.patchInSourceRow = None
        self.patchInDestCol = None
        self.destInPatchCol = None
        self.patchInSourceCol = None
        self.sourceInPatchCol = None
        self.indexes = None
        self.rcOffset = None
        self.cellInfo = None
        self.rowInfo = None
        self.cmods = None
        self.mods = None
        self.payloadTop = None
        self.payloadCol = None
        self.currentRow = None
        self.modifier = None
        self.headerMove = None
        self.headerRename = None
        self.headerPost = None
        self.headerPre = None
        self.header = None
        self.csv = None
        self.source = source
        self.patch = patch
        self.flags = flags
        if (flags is None):
            self.flags = CompareFlags()
        self.view = patch.getCellView()
        self.sourceView = source.getCellView()
        self.meta = source.getMeta()

    def reset(self):
        self.header = haxe_ds_IntMap()
        self.headerPre = haxe_ds_StringMap()
        self.headerPost = haxe_ds_StringMap()
        self.headerRename = haxe_ds_StringMap()
        self.headerMove = None
        self.modifier = haxe_ds_IntMap()
        self.mods = list()
        self.cmods = list()
        self.csv = Csv()
        self.rcOffset = 0
        self.currentRow = -1
        self.rowInfo = CellInfo()
        self.cellInfo = CellInfo()
        def _hx_local_1():
            def _hx_local_0():
                self.patchInDestCol = None
                return self.patchInDestCol
            self.patchInSourceCol = _hx_local_0()
            return self.patchInSourceCol
        self.sourceInPatchCol = _hx_local_1()
        self.patchInSourceRow = haxe_ds_IntMap()
        self.indexes = None
        self.lastSourceRow = -1
        self.actions = list()
        self.rowPermutation = None
        self.rowPermutationRev = None
        self.colPermutation = None
        self.colPermutationRev = None
        self.haveDroppedColumns = False
        self.headerRow = 0
        self.preambleRow = 0
        self.meta_change = False
        self.process_meta = False
        self.prev_meta = None
        self.next_meta = None
        self.finished_columns = False

    def processMeta(self):
        self.process_meta = True

    def apply(self):
        self.reset()
        if (self.patch.get_width() < 2):
            return True
        if (self.patch.get_height() < 1):
            return True
        self.payloadCol = (1 + self.rcOffset)
        self.payloadTop = self.patch.get_width()
        corner = self.patch.getCellView().toString(self.patch.getCell(0,0))
        self.rcOffset = (1 if ((corner == "@:@")) else 0)
        _g = 0
        _g1 = self.patch.get_height()
        while (_g < _g1):
            r = _g
            _g = (_g + 1)
            _hx_str = self.view.toString(self.patch.getCell(self.rcOffset,r))
            _this = self.actions
            _this.append((_hx_str if ((_hx_str is not None)) else ""))
        def _hx_local_0():
            self.headerRow = self.rcOffset
            return self.headerRow
        self.preambleRow = _hx_local_0()
        _g = 0
        _g1 = self.patch.get_height()
        while (_g < _g1):
            r = _g
            _g = (_g + 1)
            self.applyRow(r)
        self.finishColumns()
        self.finishRows()
        return True

    def needSourceColumns(self):
        if (self.sourceInPatchCol is not None):
            return
        self.sourceInPatchCol = haxe_ds_IntMap()
        self.patchInSourceCol = haxe_ds_IntMap()
        av = self.source.getCellView()
        _g = 0
        _g1 = self.source.get_width()
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            name = av.toString(self.source.getCell(i,0))
            at = self.headerPre.h.get(name,None)
            if (at is None):
                continue
            self.sourceInPatchCol.set(i,at)
            self.patchInSourceCol.set(at,i)

    def needDestColumns(self):
        if (self.patchInDestCol is not None):
            return
        self.patchInDestCol = haxe_ds_IntMap()
        self.destInPatchCol = haxe_ds_IntMap()
        _g = 0
        _g1 = self.cmods
        while (_g < len(_g1)):
            cmod = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            if (cmod.patchRow != -1):
                self.patchInDestCol.set(cmod.patchRow,cmod.destRow)
                self.destInPatchCol.set(cmod.destRow,cmod.patchRow)

    def needSourceIndex(self):
        if (self.indexes is not None):
            return
        state = TableComparisonState()
        state.a = self.source
        state.b = self.source
        comp = CompareTable(state)
        comp.storeIndexes()
        comp.run()
        comp.align()
        self.indexes = comp.getIndexes()
        self.needSourceColumns()

    def setMetaProp(self,target,column_name,prop_name,value):
        if (column_name is None):
            return
        if (prop_name is None):
            return
        if (not (column_name in target.h)):
            value1 = list()
            target.h[column_name] = value1
        change = PropertyChange()
        change.prevName = prop_name
        change.name = prop_name
        if (value == ""):
            value = None
        change.val = value
        _this = target.h.get(column_name,None)
        _this.append(change)

    def applyMetaRow(self,code):
        self.needSourceColumns()
        codes = code.split("@")
        prop_name = ""
        if (len(codes) > 1):
            prop_name = python_internal_ArrayImpl._get(codes, (len(codes) - 2))
        if (len(codes) > 0):
            code = python_internal_ArrayImpl._get(codes, (len(codes) - 1))
        if (self.prev_meta is None):
            self.prev_meta = haxe_ds_StringMap()
        if (self.next_meta is None):
            self.next_meta = haxe_ds_StringMap()
        _g = self.payloadCol
        _g1 = self.payloadTop
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            txt = self.getDatum(i)
            idx_patch = i
            idx_src = (self.patchInSourceCol.h.get(idx_patch,None) if ((idx_patch in self.patchInSourceCol.h)) else -1)
            prev_name = None
            name = None
            if (idx_src != -1):
                prev_name = self.source.getCell(idx_src,0)
            if (idx_patch in self.header.h):
                name = self.header.h.get(idx_patch,None)
            DiffRender.examineCell(0,0,self.view,txt,"",code,"",self.cellInfo)
            if self.cellInfo.updated:
                self.setMetaProp(self.prev_meta,prev_name,prop_name,self.cellInfo.lvalue)
                self.setMetaProp(self.next_meta,name,prop_name,self.cellInfo.rvalue)
            else:
                self.setMetaProp(self.prev_meta,prev_name,prop_name,self.cellInfo.value)
                self.setMetaProp(self.next_meta,name,prop_name,self.cellInfo.value)

    def applyRow(self,r):
        self.currentRow = r
        code = (self.actions[r] if r >= 0 and r < len(self.actions) else None)
        done = False
        if ((r == 0) and ((self.rcOffset > 0))):
            done = True
        elif (code == "@@"):
            def _hx_local_0():
                self.headerRow = r
                return self.headerRow
            self.preambleRow = _hx_local_0()
            self.applyHeader()
            self.applyAction("@@")
            done = True
        elif (code == "!"):
            def _hx_local_1():
                self.headerRow = r
                return self.headerRow
            self.preambleRow = _hx_local_1()
            self.applyMeta()
            done = True
        else:
            startIndex = None
            if (((code.find("@") if ((startIndex is None)) else HxString.indexOfImpl(code,"@",startIndex))) == 0):
                self.flags.addWarning((("cannot usefully apply diffs with metadata yet: '" + ("null" if code is None else code)) + "'"))
                self.preambleRow = r
                self.applyMetaRow(code)
                if self.process_meta:
                    codes = code.split("@")
                    if (len(codes) > 0):
                        code = python_internal_ArrayImpl._get(codes, (len(codes) - 1))
                else:
                    self.meta_change = True
                    done = True
                self.meta_change = True
                done = True
        if self.process_meta:
            return
        if (not done):
            self.finishColumns()
            if (code == "+++"):
                self.applyAction(code)
            elif (code == "---"):
                self.applyAction(code)
            elif ((code == "+") or ((code == ":"))):
                self.applyAction(code)
            else:
                startIndex = None
                if (((code.find("->") if ((startIndex is None)) else HxString.indexOfImpl(code,"->",startIndex))) >= 0):
                    self.applyAction("->")
                else:
                    self.lastSourceRow = -1

    def getDatum(self,c):
        return self.patch.getCell(c,self.currentRow)

    def getString(self,c):
        return self.view.toString(self.getDatum(c))

    def getStringNull(self,c):
        d = self.getDatum(c)
        if (d is None):
            return None
        return self.view.toString(d)

    def applyMeta(self):
        _g = self.payloadCol
        _g1 = self.payloadTop
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            name = self.getString(i)
            if (name == ""):
                continue
            self.modifier.set(i,name)

    def applyHeader(self):
        _g = self.payloadCol
        _g1 = self.payloadTop
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            name = self.getString(i)
            if (name == "..."):
                self.modifier.set(i,"...")
                self.haveDroppedColumns = True
                continue
            mod = self.modifier.h.get(i,None)
            move = False
            if (mod is not None):
                if (HxString.charCodeAt(mod,0) == 58):
                    move = True
                    mod = HxString.substr(mod,1,len(mod))
            self.header.set(i,name)
            if (mod is not None):
                if (HxString.charCodeAt(mod,0) == 40):
                    prev_name = HxString.substr(mod,1,(len(mod) - 2))
                    self.headerPre.h[prev_name] = i
                    self.headerPost.h[name] = i
                    self.headerRename.h[prev_name] = name
                    continue
            if (mod != "+++"):
                self.headerPre.h[name] = i
            if (mod != "---"):
                self.headerPost.h[name] = i
            if move:
                if (self.headerMove is None):
                    self.headerMove = haxe_ds_StringMap()
                self.headerMove.h[name] = 1
        if (not self.useMetaForRowChanges()):
            if (self.source.get_height() == 0):
                self.applyAction("+++")

    def lookUp(self,_hx_del = None):
        if (_hx_del is None):
            _hx_del = 0
        if ((self.currentRow + _hx_del) in self.patchInSourceRow.h):
            return self.patchInSourceRow.h.get((self.currentRow + _hx_del),None)
        result = -1
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0.currentRow
        _hx_local_0.currentRow = (_hx_local_1 + _hx_del)
        _hx_local_0.currentRow
        if ((self.currentRow >= 0) and ((self.currentRow < self.patch.get_height()))):
            _g = 0
            _g1 = self.indexes
            while (_g < len(_g1)):
                idx = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
                _g = (_g + 1)
                match = idx.queryByContent(self)
                if (match.spot_a == 0):
                    continue
                if (match.spot_a == 1):
                    result = python_internal_ArrayImpl._get(match.item_a.lst, 0)
                    break
                if (self.currentRow > 0):
                    prev = self.patchInSourceRow.h.get((self.currentRow - 1),None)
                    if (prev is not None):
                        lst = match.item_a.lst
                        _g2 = 0
                        while (_g2 < len(lst)):
                            row = (lst[_g2] if _g2 >= 0 and _g2 < len(lst) else None)
                            _g2 = (_g2 + 1)
                            if (row == ((prev + 1))):
                                result = row
                                break
        self.patchInSourceRow.set(self.currentRow,result)
        _hx_local_4 = self
        _hx_local_5 = _hx_local_4.currentRow
        _hx_local_4.currentRow = (_hx_local_5 - _hx_del)
        _hx_local_4.currentRow
        return result

    def applyActionExternal(self,code):
        if (code == "@@"):
            return
        rc = RowChange()
        rc.action = code
        self.checkAct()
        if (code != "+++"):
            rc.cond = haxe_ds_StringMap()
        if (code != "---"):
            rc.val = haxe_ds_StringMap()
        have_column = False
        _g = self.payloadCol
        _g1 = self.payloadTop
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            prev_name = self.header.h.get(i,None)
            name = prev_name
            if (prev_name in self.headerRename.h):
                name = self.headerRename.h.get(prev_name,None)
            cact = self.modifier.h.get(i,None)
            if (cact == "..."):
                continue
            if ((name is None) or ((name == ""))):
                continue
            txt = self.csv.parseCell(self.getStringNull(i))
            updated = False
            if self.rowInfo.updated:
                self.getPreString(txt)
                updated = self.cellInfo.updated
            if ((cact == "+++") and ((code != "---"))):
                if ((txt is not None) and ((txt != ""))):
                    if (rc.val is None):
                        rc.val = haxe_ds_StringMap()
                    rc.val.h[name] = txt
                    have_column = True
            if updated:
                this1 = rc.cond
                value = self.csv.parseCell(self.cellInfo.lvalue)
                this1.h[name] = value
                this2 = rc.val
                value1 = self.csv.parseCell(self.cellInfo.rvalue)
                this2.h[name] = value1
            elif (code == "+++"):
                if (cact != "---"):
                    rc.val.h[name] = txt
            elif ((cact != "+++") and ((cact != "---"))):
                rc.cond.h[name] = txt
        if (rc.action == "+"):
            if (not have_column):
                return
            rc.action = "->"
        self.meta.changeRow(rc)

    def applyAction(self,code):
        if self.useMetaForRowChanges():
            self.applyActionExternal(code)
            return
        mod = HighlightPatchUnit()
        mod.code = code
        mod.add = (code == "+++")
        mod.rem = (code == "---")
        mod.update = (code == "->")
        self.needSourceIndex()
        if (self.lastSourceRow == -1):
            self.lastSourceRow = self.lookUp(-1)
        mod.sourcePrevRow = self.lastSourceRow
        nextAct = python_internal_ArrayImpl._get(self.actions, (self.currentRow + 1))
        if ((nextAct != "+++") and ((nextAct != "..."))):
            mod.sourceNextRow = self.lookUp(1)
        if mod.add:
            if (python_internal_ArrayImpl._get(self.actions, (self.currentRow - 1)) != "+++"):
                if (python_internal_ArrayImpl._get(self.actions, (self.currentRow - 1)) == "@@"):
                    mod.sourcePrevRow = 0
                    self.lastSourceRow = 0
                else:
                    mod.sourcePrevRow = self.lookUp(-1)
            mod.sourceRow = mod.sourcePrevRow
            if (mod.sourceRow != -1):
                mod.sourceRowOffset = 1
        else:
            def _hx_local_0():
                self.lastSourceRow = self.lookUp()
                return self.lastSourceRow
            mod.sourceRow = _hx_local_0()
        if (python_internal_ArrayImpl._get(self.actions, (self.currentRow + 1)) == ""):
            self.lastSourceRow = mod.sourceNextRow
        mod.patchRow = self.currentRow
        if (code == "@@"):
            mod.sourceRow = 0
        _this = self.mods
        _this.append(mod)

    def checkAct(self):
        act = self.getString(self.rcOffset)
        if (self.rowInfo.value != act):
            DiffRender.examineCell(0,0,self.view,act,"",act,"",self.rowInfo)

    def getPreString(self,txt):
        self.checkAct()
        if (not self.rowInfo.updated):
            return txt
        DiffRender.examineCell(0,0,self.view,txt,"",self.rowInfo.value,"",self.cellInfo)
        if (not self.cellInfo.updated):
            return txt
        return self.cellInfo.lvalue

    def getRowString(self,c):
        at = self.sourceInPatchCol.h.get(c,None)
        if (at is None):
            return "NOT_FOUND"
        return self.getPreString(self.getString(at))

    def isPreamble(self):
        return (self.currentRow <= self.preambleRow)

    def sortMods(self,a,b):
        if ((b.code == "@@") and ((a.code != "@@"))):
            return 1
        if ((a.code == "@@") and ((b.code != "@@"))):
            return -1
        if (((a.sourceRow == -1) and (not a.add)) and ((b.sourceRow != -1))):
            return 1
        if (((a.sourceRow != -1) and (not b.add)) and ((b.sourceRow == -1))):
            return -1
        if ((a.sourceRow + a.sourceRowOffset) > ((b.sourceRow + b.sourceRowOffset))):
            return 1
        if ((a.sourceRow + a.sourceRowOffset) < ((b.sourceRow + b.sourceRowOffset))):
            return -1
        if (a.patchRow > b.patchRow):
            return 1
        if (a.patchRow < b.patchRow):
            return -1
        return 0

    def processMods(self,rmods,fate,_hx_len):
        rmods.sort(key= python_lib_Functools.cmp_to_key(self.sortMods))
        offset = 0
        last = -1
        target = 0
        if (len(rmods) > 0):
            if ((rmods[0] if 0 < len(rmods) else None).sourcePrevRow == -1):
                last = 0
        _g = 0
        while (_g < len(rmods)):
            mod = (rmods[_g] if _g >= 0 and _g < len(rmods) else None)
            _g = (_g + 1)
            if (last != -1):
                _g1 = last
                _g2 = (mod.sourceRow + mod.sourceRowOffset)
                while (_g1 < _g2):
                    i = _g1
                    _g1 = (_g1 + 1)
                    fate.append((i + offset))
                    target = (target + 1)
                    last = (last + 1)
            if mod.rem:
                fate.append(-1)
                offset = (offset - 1)
            elif mod.add:
                mod.destRow = target
                target = (target + 1)
                offset = (offset + 1)
            else:
                mod.destRow = target
            if (mod.sourceRow >= 0):
                last = (mod.sourceRow + mod.sourceRowOffset)
                if mod.rem:
                    last = (last + 1)
            elif (mod.add and ((mod.sourceNextRow != -1))):
                last = (mod.sourceNextRow + mod.sourceRowOffset)
            elif (mod.rem or mod.add):
                last = -1
        if (last != -1):
            _g = last
            _g1 = _hx_len
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                fate.append((i + offset))
                target = (target + 1)
                last = (last + 1)
        return (_hx_len + offset)

    def useMetaForColumnChanges(self):
        if (self.meta is None):
            return False
        return self.meta.useForColumnChanges()

    def useMetaForRowChanges(self):
        if (self.meta is None):
            return False
        return self.meta.useForRowChanges()

    def computeOrdering(self,mods,permutation,permutationRev,dim):
        to_unit = haxe_ds_IntMap()
        from_unit = haxe_ds_IntMap()
        meta_from_unit = haxe_ds_IntMap()
        ct = 0
        _g = 0
        while (_g < len(mods)):
            mod = (mods[_g] if _g >= 0 and _g < len(mods) else None)
            _g = (_g + 1)
            if (mod.add or mod.rem):
                continue
            if (mod.sourceRow < 0):
                continue
            if (mod.sourcePrevRow >= 0):
                v = mod.sourceRow
                to_unit.set(mod.sourcePrevRow,v)
                v1 = mod.sourcePrevRow
                from_unit.set(mod.sourceRow,v1)
                if ((mod.sourcePrevRow + 1) != mod.sourceRow):
                    ct = (ct + 1)
            if (mod.sourceNextRow >= 0):
                v2 = mod.sourceNextRow
                to_unit.set(mod.sourceRow,v2)
                v3 = mod.sourceRow
                from_unit.set(mod.sourceNextRow,v3)
                if ((mod.sourceRow + 1) != mod.sourceNextRow):
                    ct = (ct + 1)
        if (ct > 0):
            cursor = None
            logical = None
            starts = []
            _g = 0
            _g1 = dim
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                u = from_unit.h.get(i,None)
                if (u is not None):
                    meta_from_unit.set(u,i)
                else:
                    starts.append(i)
            used = haxe_ds_IntMap()
            _hx_len = 0
            _g = 0
            _g1 = dim
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                if ((logical is not None) and (logical in meta_from_unit.h)):
                    cursor = meta_from_unit.h.get(logical,None)
                else:
                    cursor = None
                if (cursor is None):
                    v = (None if ((len(starts) == 0)) else starts.pop(0))
                    cursor = v
                    logical = v
                if (cursor is None):
                    cursor = 0
                while (cursor in used.h):
                    cursor = HxOverrides.mod(((cursor + 1)), dim)
                logical = cursor
                permutationRev.append(cursor)
                used.set(cursor,1)
            _g = 0
            _g1 = len(permutationRev)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                python_internal_ArrayImpl._set(permutation, i, -1)
            _g = 0
            _g1 = len(permutation)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                python_internal_ArrayImpl._set(permutation, (permutationRev[i] if i >= 0 and i < len(permutationRev) else None), i)

    def permuteRows(self):
        self.rowPermutation = list()
        self.rowPermutationRev = list()
        self.computeOrdering(self.mods,self.rowPermutation,self.rowPermutationRev,self.source.get_height())

    def fillInNewColumns(self):
        _g = 0
        _g1 = self.cmods
        while (_g < len(_g1)):
            cmod = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            if (not cmod.rem):
                if cmod.add:
                    _g2 = 0
                    _g3 = self.mods
                    while (_g2 < len(_g3)):
                        mod = (_g3[_g2] if _g2 >= 0 and _g2 < len(_g3) else None)
                        _g2 = (_g2 + 1)
                        if ((mod.patchRow != -1) and ((mod.destRow != -1))):
                            d = self.patch.getCell(cmod.patchRow,mod.patchRow)
                            self.source.setCell(cmod.destRow,mod.destRow,d)
                    hdr = self.header.h.get(cmod.patchRow,None)
                    self.source.setCell(cmod.destRow,0,self.view.toDatum(hdr))

    def finishRows(self):
        if self.useMetaForRowChanges():
            return
        if (self.source.get_width() == 0):
            if (self.source.get_height() != 0):
                self.source.resize(0,0)
            return
        fate = list()
        self.permuteRows()
        if (len(self.rowPermutation) > 0):
            _g = 0
            _g1 = self.mods
            while (_g < len(_g1)):
                mod = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
                _g = (_g + 1)
                if (mod.sourceRow >= 0):
                    mod.sourceRow = python_internal_ArrayImpl._get(self.rowPermutation, mod.sourceRow)
        if (len(self.rowPermutation) > 0):
            self.source.insertOrDeleteRows(self.rowPermutation,len(self.rowPermutation))
        _hx_len = self.processMods(self.mods,fate,self.source.get_height())
        self.source.insertOrDeleteRows(fate,_hx_len)
        self.needDestColumns()
        _g = 0
        _g1 = self.mods
        while (_g < len(_g1)):
            mod = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            if (not mod.rem):
                if mod.add:
                    c = self.headerPost.iterator()
                    while c.hasNext():
                        c1 = c.next()
                        offset = self.patchInDestCol.h.get(c1,None)
                        if ((offset is not None) and ((offset >= 0))):
                            self.source.setCell(offset,mod.destRow,self.patch.getCell(c1,mod.patchRow))
                elif mod.update:
                    self.currentRow = mod.patchRow
                    self.checkAct()
                    if (not self.rowInfo.updated):
                        continue
                    c2 = self.headerPre.iterator()
                    while c2.hasNext():
                        c3 = c2.next()
                        txt = self.view.toString(self.patch.getCell(c3,mod.patchRow))
                        DiffRender.examineCell(0,0,self.view,txt,"",self.rowInfo.value,"",self.cellInfo)
                        if (not self.cellInfo.updated):
                            continue
                        if self.cellInfo.conflicted:
                            continue
                        d = self.view.toDatum(self.csv.parseCell(self.cellInfo.rvalue))
                        offset1 = self.patchInDestCol.h.get(c3,None)
                        if ((offset1 is not None) and ((offset1 >= 0))):
                            self.source.setCell(self.patchInDestCol.h.get(c3,None),mod.destRow,d)
        self.fillInNewColumns()
        _g = 0
        _g1 = self.source.get_width()
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            name = self.view.toString(self.source.getCell(i,0))
            next_name = self.headerRename.h.get(name,None)
            if (next_name is None):
                continue
            self.source.setCell(i,0,self.view.toDatum(next_name))

    def permuteColumns(self):
        if (self.headerMove is None):
            return
        self.colPermutation = list()
        self.colPermutationRev = list()
        self.computeOrdering(self.cmods,self.colPermutation,self.colPermutationRev,self.source.get_width())
        if (len(self.colPermutation) == 0):
            return

    def finishColumns(self):
        if self.finished_columns:
            return
        self.finished_columns = True
        self.needSourceColumns()
        _g = self.payloadCol
        _g1 = self.payloadTop
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            act = self.modifier.h.get(i,None)
            hdr = self.header.h.get(i,None)
            if (act is None):
                act = ""
            if (act == "---"):
                at = -1
                if (i in self.patchInSourceCol.h):
                    at = self.patchInSourceCol.h.get(i,None)
                mod = HighlightPatchUnit()
                mod.code = act
                mod.rem = True
                mod.sourceRow = at
                mod.patchRow = i
                _this = self.cmods
                _this.append(mod)
            elif (act == "+++"):
                mod1 = HighlightPatchUnit()
                mod1.code = act
                mod1.add = True
                prev = -1
                cont = False
                mod1.sourceRow = -1
                if (len(self.cmods) > 0):
                    mod1.sourceRow = python_internal_ArrayImpl._get(self.cmods, (len(self.cmods) - 1)).sourceRow
                if (mod1.sourceRow != -1):
                    mod1.sourceRowOffset = 1
                mod1.patchRow = i
                _this1 = self.cmods
                _this1.append(mod1)
            elif (act != "..."):
                at1 = -1
                if (i in self.patchInSourceCol.h):
                    at1 = self.patchInSourceCol.h.get(i,None)
                mod2 = HighlightPatchUnit()
                mod2.code = act
                mod2.patchRow = i
                mod2.sourceRow = at1
                _this2 = self.cmods
                _this2.append(mod2)
        at = -1
        rat = -1
        _g = 0
        _g1 = (len(self.cmods) - 1)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            icode = (self.cmods[i] if i >= 0 and i < len(self.cmods) else None).code
            if ((icode != "+++") and ((icode != "---"))):
                at = (self.cmods[i] if i >= 0 and i < len(self.cmods) else None).sourceRow
            python_internal_ArrayImpl._get(self.cmods, (i + 1)).sourcePrevRow = at
            j = ((len(self.cmods) - 1) - i)
            jcode = (self.cmods[j] if j >= 0 and j < len(self.cmods) else None).code
            if ((jcode != "+++") and ((jcode != "---"))):
                rat = (self.cmods[j] if j >= 0 and j < len(self.cmods) else None).sourceRow
            python_internal_ArrayImpl._get(self.cmods, (j - 1)).sourceNextRow = rat
        fate = list()
        self.permuteColumns()
        if (self.headerMove is not None):
            if (len(self.colPermutation) > 0):
                _g = 0
                _g1 = self.cmods
                while (_g < len(_g1)):
                    mod = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
                    _g = (_g + 1)
                    if (mod.sourceRow >= 0):
                        mod.sourceRow = python_internal_ArrayImpl._get(self.colPermutation, mod.sourceRow)
                if (not self.useMetaForColumnChanges()):
                    self.source.insertOrDeleteColumns(self.colPermutation,len(self.colPermutation))
        _hx_len = self.processMods(self.cmods,fate,self.source.get_width())
        if (not self.useMetaForColumnChanges()):
            self.source.insertOrDeleteColumns(fate,_hx_len)
            return
        changed = False
        _g = 0
        _g1 = self.cmods
        while (_g < len(_g1)):
            mod = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            if (mod.code != ""):
                changed = True
                break
        if (not changed):
            return
        columns = list()
        target = haxe_ds_IntMap()
        def _hx_local_2(x):
            if (x < 0):
                return x
            else:
                return (x + 1)
        inc = _hx_local_2
        _g = 0
        _g1 = len(fate)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            target.set(i,inc((fate[i] if i >= 0 and i < len(fate) else None)))
        self.needSourceColumns()
        self.needDestColumns()
        _g = 1
        _g1 = self.patch.get_width()
        while (_g < _g1):
            idx_patch = _g
            _g = (_g + 1)
            change = ColumnChange()
            idx_src = (self.patchInSourceCol.h.get(idx_patch,None) if ((idx_patch in self.patchInSourceCol.h)) else -1)
            prev_name = None
            name = None
            if (idx_src != -1):
                prev_name = self.source.getCell(idx_src,0)
            if (self.modifier.h.get(idx_patch,None) != "---"):
                if (idx_patch in self.header.h):
                    name = self.header.h.get(idx_patch,None)
            change.prevName = prev_name
            change.name = name
            if (self.next_meta is not None):
                if (name in self.next_meta.h):
                    change.props = self.next_meta.h.get(name,None)
            columns.append(change)
        self.meta.alterColumns(columns)

HighlightPatch._hx_class = HighlightPatch


class HighlightPatchUnit:
    _hx_class_name = "HighlightPatchUnit"
    __slots__ = ("add", "rem", "update", "code", "sourceRow", "sourceRowOffset", "sourcePrevRow", "sourceNextRow", "destRow", "patchRow")
    _hx_fields = ["add", "rem", "update", "code", "sourceRow", "sourceRowOffset", "sourcePrevRow", "sourceNextRow", "destRow", "patchRow"]
    _hx_methods = ["toString"]

    def __init__(self):
        self.add = False
        self.rem = False
        self.update = False
        self.sourceRow = -1
        self.sourceRowOffset = 0
        self.sourcePrevRow = -1
        self.sourceNextRow = -1
        self.destRow = -1
        self.patchRow = -1
        self.code = ""

    def toString(self):
        return (((((((((((((("(" + HxOverrides.stringOrNull(self.code)) + " patch ") + Std.string(self.patchRow)) + " source ") + Std.string(self.sourcePrevRow)) + ":") + Std.string(self.sourceRow)) + ":") + Std.string(self.sourceNextRow)) + "+") + Std.string(self.sourceRowOffset)) + " dest ") + Std.string(self.destRow)) + ")")

HighlightPatchUnit._hx_class = HighlightPatchUnit


class Index:
    _hx_class_name = "Index"
    __slots__ = ("items", "keys", "top_freq", "height", "cols", "v", "indexed_table", "hdr", "ignore_whitespace", "ignore_case")
    _hx_fields = ["items", "keys", "top_freq", "height", "cols", "v", "indexed_table", "hdr", "ignore_whitespace", "ignore_case"]
    _hx_methods = ["addColumn", "indexTable", "toKey", "toKeyByContent", "getTable"]

    def __init__(self,flags):
        self.indexed_table = None
        self.v = None
        self.items = haxe_ds_StringMap()
        self.cols = list()
        self.keys = list()
        self.top_freq = 0
        self.height = 0
        self.hdr = 0
        self.ignore_whitespace = False
        self.ignore_case = False
        if (flags is not None):
            self.ignore_whitespace = flags.ignore_whitespace
            self.ignore_case = flags.ignore_case

    def addColumn(self,i):
        _this = self.cols
        _this.append(i)

    def indexTable(self,t,hdr):
        self.indexed_table = t
        self.hdr = hdr
        if ((len(self.keys) != t.get_height()) and ((t.get_height() > 0))):
            python_internal_ArrayImpl._set(self.keys, (t.get_height() - 1), None)
        _g = 0
        _g1 = t.get_height()
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            key = (self.keys[i] if i >= 0 and i < len(self.keys) else None)
            if (key is None):
                key = self.toKey(t,i)
                python_internal_ArrayImpl._set(self.keys, i, key)
            item = self.items.h.get(key,None)
            if (item is None):
                item = IndexItem()
                self.items.h[key] = item
            if (item.lst is None):
                item.lst = list()
            _this = item.lst
            _this.append(i)
            ct = len(item.lst)
            if (ct > self.top_freq):
                self.top_freq = ct
        self.height = t.get_height()

    def toKey(self,t,i):
        wide = ("_" if ((i < self.hdr)) else "")
        if (self.v is None):
            self.v = t.getCellView()
        _g = 0
        _g1 = len(self.cols)
        while (_g < _g1):
            k = _g
            _g = (_g + 1)
            d = t.getCell((self.cols[k] if k >= 0 and k < len(self.cols) else None),i)
            txt = self.v.toString(d)
            if self.ignore_whitespace:
                txt = StringTools.trim(txt)
            if self.ignore_case:
                txt = txt.lower()
            if (k > 0):
                wide = (("null" if wide is None else wide) + " // ")
            if ((((txt is None) or ((txt == ""))) or ((txt == "null"))) or ((txt == "undefined"))):
                continue
            wide = (("null" if wide is None else wide) + ("null" if txt is None else txt))
        return wide

    def toKeyByContent(self,row):
        wide = ("_" if (row.isPreamble()) else "")
        _g = 0
        _g1 = len(self.cols)
        while (_g < _g1):
            k = _g
            _g = (_g + 1)
            txt = row.getRowString((self.cols[k] if k >= 0 and k < len(self.cols) else None))
            if self.ignore_whitespace:
                txt = StringTools.trim(txt)
            if self.ignore_case:
                txt = txt.lower()
            if (k > 0):
                wide = (("null" if wide is None else wide) + " // ")
            if ((((txt is None) or ((txt == ""))) or ((txt == "null"))) or ((txt == "undefined"))):
                continue
            wide = (("null" if wide is None else wide) + ("null" if txt is None else txt))
        return wide

    def getTable(self):
        return self.indexed_table

Index._hx_class = Index


class IndexItem:
    _hx_class_name = "IndexItem"
    __slots__ = ("lst",)
    _hx_fields = ["lst"]
    _hx_methods = ["add", "length", "value", "asList"]

    def __init__(self):
        self.lst = None

    def add(self,i):
        if (self.lst is None):
            self.lst = list()
        _this = self.lst
        _this.append(i)
        return len(self.lst)

    def length(self):
        return len(self.lst)

    def value(self):
        return (self.lst[0] if 0 < len(self.lst) else None)

    def asList(self):
        return self.lst

IndexItem._hx_class = IndexItem


class IndexPair:
    _hx_class_name = "IndexPair"
    __slots__ = ("ia", "ib", "hdr", "quality", "flags")
    _hx_fields = ["ia", "ib", "hdr", "quality", "flags"]
    _hx_methods = ["addColumns", "indexTables", "queryByKey", "queryByContent", "queryLocal", "localKey", "remoteKey", "getTopFreq", "getQuality"]

    def __init__(self,flags):
        self.flags = flags
        self.ia = Index(flags)
        self.ib = Index(flags)
        self.quality = 0
        self.hdr = 0

    def addColumns(self,ca,cb):
        self.ia.addColumn(ca)
        self.ib.addColumn(cb)

    def indexTables(self,a,b,hdr):
        self.ia.indexTable(a,hdr)
        self.ib.indexTable(b,hdr)
        self.hdr = hdr
        good = 0
        key = self.ia.items.keys()
        while key.hasNext():
            key1 = key.next()
            item_a = self.ia.items.h.get(key1,None)
            spot_a = len(item_a.lst)
            item_b = self.ib.items.h.get(key1,None)
            spot_b = 0
            if (item_b is not None):
                spot_b = len(item_b.lst)
            if ((spot_a == 1) and ((spot_b == 1))):
                good = (good + 1)
        b = a.get_height()
        self.quality = (good / ((1.0 if (python_lib_Math.isnan(1.0)) else (b if (python_lib_Math.isnan(b)) else max(1.0,b)))))

    def queryByKey(self,ka):
        result = CrossMatch()
        result.item_a = self.ia.items.h.get(ka,None)
        result.item_b = self.ib.items.h.get(ka,None)
        def _hx_local_0():
            result.spot_b = 0
            return result.spot_b
        result.spot_a = _hx_local_0()
        if (ka != ""):
            if (result.item_a is not None):
                result.spot_a = len(result.item_a.lst)
            if (result.item_b is not None):
                result.spot_b = len(result.item_b.lst)
        return result

    def queryByContent(self,row):
        result = CrossMatch()
        ka = self.ia.toKeyByContent(row)
        return self.queryByKey(ka)

    def queryLocal(self,row):
        ka = self.ia.toKey(self.ia.getTable(),row)
        return self.queryByKey(ka)

    def localKey(self,row):
        return self.ia.toKey(self.ia.getTable(),row)

    def remoteKey(self,row):
        return self.ib.toKey(self.ib.getTable(),row)

    def getTopFreq(self):
        if (self.ib.top_freq > self.ia.top_freq):
            return self.ib.top_freq
        return self.ia.top_freq

    def getQuality(self):
        return self.quality

IndexPair._hx_class = IndexPair


class Meta:
    _hx_class_name = "Meta"
    __slots__ = ()
    _hx_methods = ["alterColumns", "changeRow", "applyFlags", "asTable", "cloneMeta", "useForColumnChanges", "useForRowChanges", "getRowStream", "isNested", "isSql", "getName"]
Meta._hx_class = Meta


class JsonTable:
    _hx_class_name = "JsonTable"
    __slots__ = ("w", "h", "columns", "rows", "data", "idx2col", "name")
    _hx_fields = ["w", "h", "columns", "rows", "data", "idx2col", "name"]
    _hx_methods = ["getTable", "get_width", "get_height", "getCell", "setCell", "toString", "getCellView", "isResizable", "resize", "clear", "insertOrDeleteRows", "insertOrDeleteColumns", "trimBlank", "getData", "clone", "setMeta", "getMeta", "create", "alterColumns", "changeRow", "applyFlags", "asTable", "cloneMeta", "useForColumnChanges", "useForRowChanges", "getRowStream", "isNested", "isSql", "getName"]
    _hx_interfaces = [Meta, Table]

    def __init__(self,data,name):
        self.name = None
        self.idx2col = None
        self.h = None
        self.w = None
        self.data = data
        self.columns = Reflect.field(data,"columns")
        self.rows = Reflect.field(data,"rows")
        self.w = len(self.columns)
        self.h = len(self.rows)
        self.idx2col = haxe_ds_IntMap()
        _g = 0
        _g1 = len(self.columns)
        while (_g < _g1):
            idx = _g
            _g = (_g + 1)
            v = (self.columns[idx] if idx >= 0 and idx < len(self.columns) else None)
            self.idx2col.set(idx,v)
        self.name = name

    def getTable(self):
        return self

    def get_width(self):
        return self.w

    def get_height(self):
        return (self.h + 1)

    def getCell(self,x,y):
        if (y == 0):
            return self.idx2col.h.get(x,None)
        return Reflect.field(python_internal_ArrayImpl._get(self.rows, (y - 1)),self.idx2col.h.get(x,None))

    def setCell(self,x,y,c):
        print("JsonTable is read-only")

    def toString(self):
        return ""

    def getCellView(self):
        return SimpleView()

    def isResizable(self):
        return False

    def resize(self,w,h):
        return False

    def clear(self):
        pass

    def insertOrDeleteRows(self,fate,hfate):
        return False

    def insertOrDeleteColumns(self,fate,wfate):
        return False

    def trimBlank(self):
        return False

    def getData(self):
        return None

    def clone(self):
        return None

    def setMeta(self,meta):
        pass

    def getMeta(self):
        return self

    def create(self):
        return None

    def alterColumns(self,columns):
        return False

    def changeRow(self,rc):
        return False

    def applyFlags(self,flags):
        return False

    def asTable(self):
        return None

    def cloneMeta(self,table = None):
        return None

    def useForColumnChanges(self):
        return False

    def useForRowChanges(self):
        return False

    def getRowStream(self):
        return None

    def isNested(self):
        return False

    def isSql(self):
        return False

    def getName(self):
        return self.name

JsonTable._hx_class = JsonTable


class JsonTables:
    _hx_class_name = "JsonTables"
    __slots__ = ("db", "t", "flags")
    _hx_fields = ["db", "t", "flags"]
    _hx_methods = ["getCell", "setCell", "getCellView", "isResizable", "resize", "clear", "insertOrDeleteRows", "insertOrDeleteColumns", "trimBlank", "get_width", "get_height", "getData", "clone", "getMeta", "create"]
    _hx_interfaces = [Table]

    def __init__(self,json,flags):
        self.flags = None
        self.db = json
        names = Reflect.field(json,"names")
        allowed = None
        count = len(names)
        if ((flags is not None) and ((flags.tables is not None))):
            allowed = haxe_ds_StringMap()
            _g = 0
            _g1 = flags.tables
            while (_g < len(_g1)):
                name = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
                _g = (_g + 1)
                allowed.h[name] = True
            count = 0
            _g = 0
            while (_g < len(names)):
                name = (names[_g] if _g >= 0 and _g < len(names) else None)
                _g = (_g + 1)
                if (name in allowed.h):
                    count = (count + 1)
        self.t = SimpleTable(2,(count + 1))
        self.t.setCell(0,0,"name")
        self.t.setCell(1,0,"table")
        v = self.t.getCellView()
        at = 1
        _g = 0
        while (_g < len(names)):
            name = (names[_g] if _g >= 0 and _g < len(names) else None)
            _g = (_g + 1)
            if (allowed is not None):
                if (not (name in allowed.h)):
                    continue
            self.t.setCell(0,at,name)
            tab = Reflect.field(self.db,"tables")
            tab = Reflect.field(tab,name)
            self.t.setCell(1,at,v.wrapTable(JsonTable(tab,name)))
            at = (at + 1)

    def getCell(self,x,y):
        return self.t.getCell(x,y)

    def setCell(self,x,y,c):
        pass

    def getCellView(self):
        return self.t.getCellView()

    def isResizable(self):
        return False

    def resize(self,w,h):
        return False

    def clear(self):
        pass

    def insertOrDeleteRows(self,fate,hfate):
        return False

    def insertOrDeleteColumns(self,fate,wfate):
        return False

    def trimBlank(self):
        return False

    def get_width(self):
        return self.t.get_width()

    def get_height(self):
        return self.t.get_height()

    def getData(self):
        return None

    def clone(self):
        return None

    def getMeta(self):
        return SimpleMeta(self,True,True)

    def create(self):
        return None

JsonTables._hx_class = JsonTables


class Lambda:
    _hx_class_name = "Lambda"
    __slots__ = ()
    _hx_statics = ["array", "has"]

    @staticmethod
    def array(it):
        a = list()
        i = HxOverrides.iterator(it)
        while i.hasNext():
            i1 = i.next()
            a.append(i1)
        return a

    @staticmethod
    def has(it,elt):
        x = HxOverrides.iterator(it)
        while x.hasNext():
            x1 = x.next()
            if HxOverrides.eq(x1,elt):
                return True
        return False
Lambda._hx_class = Lambda


class Merger:
    _hx_class_name = "Merger"
    __slots__ = ("parent", "local", "remote", "flags", "order", "units", "column_order", "column_units", "row_mix_local", "row_mix_remote", "column_mix_local", "column_mix_remote", "conflicts", "conflict_infos")
    _hx_fields = ["parent", "local", "remote", "flags", "order", "units", "column_order", "column_units", "row_mix_local", "row_mix_remote", "column_mix_local", "column_mix_remote", "conflicts", "conflict_infos"]
    _hx_methods = ["shuffleDimension", "shuffleColumns", "shuffleRows", "apply", "getConflictInfos", "addConflictInfo"]
    _hx_statics = ["makeConflictedCell"]

    def __init__(self,parent,local,remote,flags):
        self.conflict_infos = None
        self.conflicts = None
        self.column_mix_remote = None
        self.column_mix_local = None
        self.row_mix_remote = None
        self.row_mix_local = None
        self.column_units = None
        self.column_order = None
        self.units = None
        self.order = None
        self.parent = parent
        self.local = local
        self.remote = remote
        self.flags = flags

    def shuffleDimension(self,dim_units,_hx_len,fate,cl,cr):
        at = 0
        _g = 0
        while (_g < len(dim_units)):
            cunit = (dim_units[_g] if _g >= 0 and _g < len(dim_units) else None)
            _g = (_g + 1)
            if (cunit.p < 0):
                if (cunit.l < 0):
                    if (cunit.r >= 0):
                        cr.set(cunit.r,at)
                        at = (at + 1)
                else:
                    cl.set(cunit.l,at)
                    at = (at + 1)
            elif (cunit.l >= 0):
                if (cunit.r >= 0):
                    cl.set(cunit.l,at)
                    at = (at + 1)
        _g = 0
        _g1 = _hx_len
        while (_g < _g1):
            x = _g
            _g = (_g + 1)
            idx = cl.h.get(x,None)
            if (idx is None):
                fate.append(-1)
            else:
                fate.append(idx)
        return at

    def shuffleColumns(self):
        self.column_mix_local = haxe_ds_IntMap()
        self.column_mix_remote = haxe_ds_IntMap()
        fate = list()
        wfate = self.shuffleDimension(self.column_units,self.local.get_width(),fate,self.column_mix_local,self.column_mix_remote)
        self.local.insertOrDeleteColumns(fate,wfate)

    def shuffleRows(self):
        self.row_mix_local = haxe_ds_IntMap()
        self.row_mix_remote = haxe_ds_IntMap()
        fate = list()
        hfate = self.shuffleDimension(self.units,self.local.get_height(),fate,self.row_mix_local,self.row_mix_remote)
        self.local.insertOrDeleteRows(fate,hfate)

    def apply(self):
        self.conflicts = 0
        self.conflict_infos = list()
        ct = Coopy.compareTables3(self.parent,self.local,self.remote)
        align = ct.align()
        self.order = align.toOrder()
        self.units = self.order.getList()
        self.column_order = align.meta.toOrder()
        self.column_units = self.column_order.getList()
        allow_insert = self.flags.allowInsert()
        allow_delete = self.flags.allowDelete()
        allow_update = self.flags.allowUpdate()
        view = self.parent.getCellView()
        _g = 0
        _g1 = self.units
        while (_g < len(_g1)):
            row = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            if (((row.l >= 0) and ((row.r >= 0))) and ((row.p >= 0))):
                _g2 = 0
                _g3 = self.column_units
                while (_g2 < len(_g3)):
                    col = (_g3[_g2] if _g2 >= 0 and _g2 < len(_g3) else None)
                    _g2 = (_g2 + 1)
                    if (((col.l >= 0) and ((col.r >= 0))) and ((col.p >= 0))):
                        pcell = self.parent.getCell(col.p,row.p)
                        rcell = self.remote.getCell(col.r,row.r)
                        if (not view.equals(pcell,rcell)):
                            lcell = self.local.getCell(col.l,row.l)
                            if view.equals(pcell,lcell):
                                self.local.setCell(col.l,row.l,rcell)
                            elif (not view.equals(rcell,lcell)):
                                self.local.setCell(col.l,row.l,Merger.makeConflictedCell(view,pcell,lcell,rcell))
                                _hx_local_2 = self
                                _hx_local_3 = _hx_local_2.conflicts
                                _hx_local_2.conflicts = (_hx_local_3 + 1)
                                _hx_local_3
                                self.addConflictInfo(row.l,col.l,view,pcell,lcell,rcell)
        self.shuffleColumns()
        self.shuffleRows()
        x = self.column_mix_remote.keys()
        while x.hasNext():
            x1 = x.next()
            x2 = self.column_mix_remote.h.get(x1,None)
            _g = 0
            _g1 = self.units
            while (_g < len(_g1)):
                unit = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
                _g = (_g + 1)
                if ((unit.l >= 0) and ((unit.r >= 0))):
                    self.local.setCell(x2,self.row_mix_local.h.get(unit.l,None),self.remote.getCell(x1,unit.r))
                elif ((unit.p < 0) and ((unit.r >= 0))):
                    self.local.setCell(x2,self.row_mix_remote.h.get(unit.r,None),self.remote.getCell(x1,unit.r))
        y = self.row_mix_remote.keys()
        while y.hasNext():
            y1 = y.next()
            y2 = self.row_mix_remote.h.get(y1,None)
            _g = 0
            _g1 = self.column_units
            while (_g < len(_g1)):
                unit = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
                _g = (_g + 1)
                if ((unit.l >= 0) and ((unit.r >= 0))):
                    self.local.setCell(self.column_mix_local.h.get(unit.l,None),y2,self.remote.getCell(unit.r,y1))
        return self.conflicts

    def getConflictInfos(self):
        return self.conflict_infos

    def addConflictInfo(self,row,col,view,pcell,lcell,rcell):
        _this = self.conflict_infos
        x = ConflictInfo(row,col,view.toString(pcell),view.toString(lcell),view.toString(rcell))
        _this.append(x)

    @staticmethod
    def makeConflictedCell(view,pcell,lcell,rcell):
        return view.toDatum(((((("((( " + HxOverrides.stringOrNull(view.toString(pcell))) + " ))) ") + HxOverrides.stringOrNull(view.toString(lcell))) + " /// ") + HxOverrides.stringOrNull(view.toString(rcell))))

Merger._hx_class = Merger


class Mover:
    _hx_class_name = "Mover"
    __slots__ = ()
    _hx_statics = ["moveUnits", "move", "moveWithoutExtras"]

    @staticmethod
    def moveUnits(units):
        isrc = list()
        idest = list()
        _hx_len = len(units)
        ltop = -1
        rtop = -1
        in_src = haxe_ds_IntMap()
        in_dest = haxe_ds_IntMap()
        _g = 0
        _g1 = _hx_len
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            unit = (units[i] if i >= 0 and i < len(units) else None)
            if ((unit.l >= 0) and ((unit.r >= 0))):
                if (ltop < unit.l):
                    ltop = unit.l
                if (rtop < unit.r):
                    rtop = unit.r
                in_src.set(unit.l,i)
                in_dest.set(unit.r,i)
        v = None
        _g = 0
        _g1 = (ltop + 1)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            v = in_src.h.get(i,None)
            if (v is not None):
                isrc.append(v)
        _g = 0
        _g1 = (rtop + 1)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            v = in_dest.h.get(i,None)
            if (v is not None):
                idest.append(v)
        return Mover.moveWithoutExtras(isrc,idest)

    @staticmethod
    def move(isrc,idest):
        _hx_len = len(isrc)
        len2 = len(idest)
        in_src = haxe_ds_IntMap()
        in_dest = haxe_ds_IntMap()
        _g = 0
        _g1 = _hx_len
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            in_src.set((isrc[i] if i >= 0 and i < len(isrc) else None),i)
        _g = 0
        _g1 = len2
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            in_dest.set((idest[i] if i >= 0 and i < len(idest) else None),i)
        src = list()
        dest = list()
        v = None
        _g = 0
        _g1 = _hx_len
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            v = (isrc[i] if i >= 0 and i < len(isrc) else None)
            if (v in in_dest.h):
                src.append(v)
        _g = 0
        _g1 = len2
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            v = (idest[i] if i >= 0 and i < len(idest) else None)
            if (v in in_src.h):
                dest.append(v)
        return Mover.moveWithoutExtras(src,dest)

    @staticmethod
    def moveWithoutExtras(src,dest):
        if (len(src) != len(dest)):
            return None
        if (len(src) <= 1):
            return []
        _hx_len = len(src)
        in_src = haxe_ds_IntMap()
        blk_len = haxe_ds_IntMap()
        blk_src_loc = haxe_ds_IntMap()
        blk_dest_loc = haxe_ds_IntMap()
        _g = 0
        _g1 = _hx_len
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            in_src.set((src[i] if i >= 0 and i < len(src) else None),i)
        ct = 0
        in_cursor = -2
        out_cursor = 0
        next = None
        blk = -1
        v = None
        while (out_cursor < _hx_len):
            v = (dest[out_cursor] if out_cursor >= 0 and out_cursor < len(dest) else None)
            next = in_src.h.get(v,None)
            if (next != ((in_cursor + 1))):
                blk = v
                ct = 1
                blk_src_loc.set(blk,next)
                blk_dest_loc.set(blk,out_cursor)
            else:
                ct = (ct + 1)
            blk_len.set(blk,ct)
            in_cursor = next
            out_cursor = (out_cursor + 1)
        blks = list()
        k = blk_len.keys()
        while k.hasNext():
            k1 = k.next()
            blks.append(k1)
        def _hx_local_2(a,b):
            diff = (blk_len.h.get(b,None) - blk_len.h.get(a,None))
            if (diff == 0):
                diff = (a - b)
            return diff
        blks.sort(key= python_lib_Functools.cmp_to_key(_hx_local_2))
        moved = list()
        while (len(blks) > 0):
            blk = (None if ((len(blks) == 0)) else blks.pop(0))
            blen = len(blks)
            ref_src_loc = blk_src_loc.h.get(blk,None)
            ref_dest_loc = blk_dest_loc.h.get(blk,None)
            i = (blen - 1)
            while (i >= 0):
                blki = (blks[i] if i >= 0 and i < len(blks) else None)
                blki_src_loc = blk_src_loc.h.get(blki,None)
                to_left_src = (blki_src_loc < ref_src_loc)
                to_left_dest = (blk_dest_loc.h.get(blki,None) < ref_dest_loc)
                if (to_left_src != to_left_dest):
                    ct = blk_len.h.get(blki,None)
                    _g = 0
                    _g1 = ct
                    while (_g < _g1):
                        j = _g
                        _g = (_g + 1)
                        moved.append((src[blki_src_loc] if blki_src_loc >= 0 and blki_src_loc < len(src) else None))
                        blki_src_loc = (blki_src_loc + 1)
                    pos = i
                    if (pos < 0):
                        pos = (len(blks) + pos)
                    if (pos < 0):
                        pos = 0
                    res = blks[pos:(pos + 1)]
                    del blks[pos:(pos + 1)]
                i = (i - 1)
        return moved
Mover._hx_class = Mover


class Ndjson:
    _hx_class_name = "Ndjson"
    __slots__ = ("tab", "view", "columns", "header_row")
    _hx_fields = ["tab", "view", "columns", "header_row"]
    _hx_methods = ["renderRow", "render", "addRow", "addHeaderRow", "parse"]

    def __init__(self,tab):
        self.columns = None
        self.tab = tab
        self.view = tab.getCellView()
        self.header_row = 0

    def renderRow(self,r):
        row = haxe_ds_StringMap()
        _g = 0
        _g1 = self.tab.get_width()
        while (_g < _g1):
            c = _g
            _g = (_g + 1)
            key = self.view.toString(self.tab.getCell(c,self.header_row))
            if ((c == 0) and ((self.header_row == 1))):
                key = "@:@"
            value = self.tab.getCell(c,r)
            row.h[key] = value
        return haxe_format_JsonPrinter.print(row,None,None)

    def render(self):
        txt = ""
        offset = 0
        if (self.tab.get_height() == 0):
            return txt
        if (self.tab.get_width() == 0):
            return txt
        if (self.tab.getCell(0,0) == "@:@"):
            offset = 1
        self.header_row = offset
        _g = (self.header_row + 1)
        _g1 = self.tab.get_height()
        while (_g < _g1):
            r = _g
            _g = (_g + 1)
            txt = (("null" if txt is None else txt) + HxOverrides.stringOrNull(self.renderRow(r)))
            txt = (("null" if txt is None else txt) + "\n")
        return txt

    def addRow(self,r,txt):
        json = python_lib_Json.loads(txt,**python__KwArgs_KwArgs_Impl_.fromT(_hx_AnonObject({'object_hook': python_Lib.dictToAnon})))
        if (self.columns is None):
            self.columns = haxe_ds_StringMap()
        w = self.tab.get_width()
        h = self.tab.get_height()
        resize = False
        _g = 0
        _g1 = python_Boot.fields(json)
        while (_g < len(_g1)):
            name = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            if (not (name in self.columns.h)):
                self.columns.h[name] = w
                w = (w + 1)
                resize = True
        if (r >= h):
            h = (r + 1)
            resize = True
        if resize:
            self.tab.resize(w,h)
        _g = 0
        _g1 = python_Boot.fields(json)
        while (_g < len(_g1)):
            name = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            v = Reflect.field(json,name)
            c = self.columns.h.get(name,None)
            self.tab.setCell(c,r,v)

    def addHeaderRow(self,r):
        names = self.columns.keys()
        n = names
        while n.hasNext():
            n1 = n.next()
            self.tab.setCell(self.columns.h.get(n1,None),r,self.view.toDatum(n1))

    def parse(self,txt):
        self.columns = None
        rows = txt.split("\n")
        h = len(rows)
        if (h == 0):
            self.tab.clear()
            return
        if (python_internal_ArrayImpl._get(rows, (h - 1)) == ""):
            h = (h - 1)
        _g = 0
        _g1 = h
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            at = ((h - i) - 1)
            self.addRow((at + 1),(rows[at] if at >= 0 and at < len(rows) else None))
        self.addHeaderRow(0)

Ndjson._hx_class = Ndjson


class NestedCellBuilder:
    _hx_class_name = "NestedCellBuilder"
    __slots__ = ("view",)
    _hx_fields = ["view"]
    _hx_methods = ["needSeparator", "setSeparator", "setConflictSeparator", "setView", "update", "conflict", "marker", "negToNull", "links"]
    _hx_interfaces = [CellBuilder]

    def __init__(self):
        self.view = None

    def needSeparator(self):
        return False

    def setSeparator(self,separator):
        pass

    def setConflictSeparator(self,separator):
        pass

    def setView(self,view):
        self.view = view

    def update(self,local,remote):
        h = self.view.makeHash()
        self.view.hashSet(h,"before",local)
        self.view.hashSet(h,"after",remote)
        return h

    def conflict(self,parent,local,remote):
        h = self.view.makeHash()
        self.view.hashSet(h,"before",parent)
        self.view.hashSet(h,"ours",local)
        self.view.hashSet(h,"theirs",remote)
        return h

    def marker(self,label):
        return self.view.toDatum(label)

    def negToNull(self,x):
        if (x < 0):
            return None
        return x

    def links(self,unit,row_like):
        h = self.view.makeHash()
        if (unit.p >= -1):
            self.view.hashSet(h,"before",self.negToNull(unit.p))
            self.view.hashSet(h,"ours",self.negToNull(unit.l))
            self.view.hashSet(h,"theirs",self.negToNull(unit.r))
            return h
        self.view.hashSet(h,"before",self.negToNull(unit.l))
        self.view.hashSet(h,"after",self.negToNull(unit.r))
        return h

NestedCellBuilder._hx_class = NestedCellBuilder


class Ordering:
    _hx_class_name = "Ordering"
    __slots__ = ("order", "ignore_parent")
    _hx_fields = ["order", "ignore_parent"]
    _hx_methods = ["add", "getList", "setList", "toString", "ignoreParent"]

    def __init__(self):
        self.order = list()
        self.ignore_parent = False

    def add(self,l,r,p = None):
        if (p is None):
            p = -2
        if self.ignore_parent:
            p = -2
        _this = self.order
        x = Unit(l,r,p)
        _this.append(x)

    def getList(self):
        return self.order

    def setList(self,lst):
        self.order = lst

    def toString(self):
        txt = ""
        _g = 0
        _g1 = len(self.order)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            if (i > 0):
                txt = (("null" if txt is None else txt) + ", ")
            txt = (("null" if txt is None else txt) + Std.string((self.order[i] if i >= 0 and i < len(self.order) else None)))
        return txt

    def ignoreParent(self):
        self.ignore_parent = True

Ordering._hx_class = Ordering


class PropertyChange:
    _hx_class_name = "PropertyChange"
    __slots__ = ("prevName", "name", "val")
    _hx_fields = ["prevName", "name", "val"]

    def __init__(self):
        self.val = None
        self.name = None
        self.prevName = None

PropertyChange._hx_class = PropertyChange


class Reflect:
    _hx_class_name = "Reflect"
    __slots__ = ()
    _hx_statics = ["field", "isFunction", "compare"]

    @staticmethod
    def field(o,field):
        return python_Boot.field(o,field)

    @staticmethod
    def isFunction(f):
        if (not ((python_lib_Inspect.isfunction(f) or python_lib_Inspect.ismethod(f)))):
            return python_Boot.hasField(f,"func_code")
        else:
            return True

    @staticmethod
    def compare(a,b):
        if ((a is None) and ((b is None))):
            return 0
        if (a is None):
            return 1
        elif (b is None):
            return -1
        elif HxOverrides.eq(a,b):
            return 0
        elif (a > b):
            return 1
        else:
            return -1
Reflect._hx_class = Reflect


class RowChange:
    _hx_class_name = "RowChange"
    __slots__ = ("cond", "val", "conflicting_val", "conflicting_parent_val", "conflicted", "is_key", "action")
    _hx_fields = ["cond", "val", "conflicting_val", "conflicting_parent_val", "conflicted", "is_key", "action"]
    _hx_methods = ["showMap", "toString"]

    def __init__(self):
        self.action = None
        self.is_key = None
        self.conflicted = None
        self.conflicting_parent_val = None
        self.conflicting_val = None
        self.val = None
        self.cond = None

    def showMap(self,m):
        if (m is None):
            return "{}"
        txt = ""
        k = m.keys()
        while k.hasNext():
            k1 = k.next()
            if (txt != ""):
                txt = (("null" if txt is None else txt) + ", ")
            v = m.h.get(k1,None)
            txt = (("null" if txt is None else txt) + HxOverrides.stringOrNull((((("null" if k1 is None else k1) + "=") + Std.string(v)))))
        return (("{ " + ("null" if txt is None else txt)) + " }")

    def toString(self):
        return ((((HxOverrides.stringOrNull(self.action) + " ") + HxOverrides.stringOrNull(self.showMap(self.cond))) + " : ") + HxOverrides.stringOrNull(self.showMap(self.val)))

RowChange._hx_class = RowChange


class RowStream:
    _hx_class_name = "RowStream"
    __slots__ = ()
    _hx_methods = ["fetchColumns", "fetchRow"]
RowStream._hx_class = RowStream


class SimpleMeta:
    _hx_class_name = "SimpleMeta"
    __slots__ = ("t", "name2row", "name2col", "has_properties", "metadata", "keys", "row_active", "row_change_cache", "may_be_nested")
    _hx_fields = ["t", "name2row", "name2col", "has_properties", "metadata", "keys", "row_active", "row_change_cache", "may_be_nested"]
    _hx_methods = ["storeRowChanges", "rowChange", "colChange", "col", "row", "alterColumns", "setCell", "addMetaData", "asTable", "cloneMeta", "useForColumnChanges", "useForRowChanges", "changeRow", "applyFlags", "getRowStream", "isNested", "isSql", "getName"]
    _hx_interfaces = [Meta]

    def __init__(self,t,has_properties = None,may_be_nested = None):
        if (has_properties is None):
            has_properties = True
        if (may_be_nested is None):
            may_be_nested = False
        self.may_be_nested = None
        self.row_change_cache = None
        self.row_active = None
        self.keys = None
        self.metadata = None
        self.has_properties = None
        self.name2col = None
        self.name2row = None
        self.t = t
        self.rowChange()
        self.colChange()
        self.has_properties = has_properties
        self.may_be_nested = may_be_nested
        self.metadata = None
        self.keys = None
        self.row_active = False
        self.row_change_cache = None

    def storeRowChanges(self,changes):
        self.row_change_cache = changes
        self.row_active = True

    def rowChange(self):
        self.name2row = None

    def colChange(self):
        self.name2col = None

    def col(self,key):
        if (self.t.get_height() < 1):
            return -1
        if (self.name2col is None):
            self.name2col = haxe_ds_StringMap()
            w = self.t.get_width()
            _g = 0
            _g1 = w
            while (_g < _g1):
                c = _g
                _g = (_g + 1)
                this1 = self.name2col
                key1 = self.t.getCell(c,0)
                this1.h[key1] = c
        if (not (key in self.name2col.h)):
            return -1
        return self.name2col.h.get(key,None)

    def row(self,key):
        if (self.t.get_width() < 1):
            return -1
        if (self.name2row is None):
            self.name2row = haxe_ds_StringMap()
            h = self.t.get_height()
            _g = 1
            _g1 = h
            while (_g < _g1):
                r = _g
                _g = (_g + 1)
                this1 = self.name2row
                key1 = self.t.getCell(0,r)
                this1.h[key1] = r
        if (not (key in self.name2row.h)):
            return -1
        return self.name2row.h.get(key,None)

    def alterColumns(self,columns):
        target = haxe_ds_StringMap()
        wfate = 0
        if self.has_properties:
            target.h["@"] = wfate
            wfate = (wfate + 1)
        _g = 0
        _g1 = len(columns)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            col = (columns[i] if i >= 0 and i < len(columns) else None)
            if (col.prevName is not None):
                target.h[col.prevName] = wfate
            if (col.name is not None):
                wfate = (wfate + 1)
        fate = list()
        _g = 0
        _g1 = self.t.get_width()
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            targeti = -1
            name = self.t.getCell(i,0)
            if (name in target.h):
                targeti = target.h.get(name,None)
            fate.append(targeti)
        self.t.insertOrDeleteColumns(fate,wfate)
        start = (1 if (self.has_properties) else 0)
        at = start
        _g = 0
        _g1 = len(columns)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            col = (columns[i] if i >= 0 and i < len(columns) else None)
            if (col.name is not None):
                if (col.name != col.prevName):
                    self.t.setCell(at,0,col.name)
            if (col.name is not None):
                at = (at + 1)
        if (not self.has_properties):
            return True
        self.colChange()
        at = start
        _g = 0
        _g1 = len(columns)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            col = (columns[i] if i >= 0 and i < len(columns) else None)
            if (col.name is not None):
                _g2 = 0
                _g3 = col.props
                while (_g2 < len(_g3)):
                    prop = (_g3[_g2] if _g2 >= 0 and _g2 < len(_g3) else None)
                    _g2 = (_g2 + 1)
                    self.setCell(col.name,prop.name,prop.val)
            if (col.name is not None):
                at = (at + 1)
        return True

    def setCell(self,c,r,val):
        ri = self.row(r)
        if (ri == -1):
            return False
        ci = self.col(c)
        if (ci == -1):
            return False
        self.t.setCell(ci,ri,val)
        return True

    def addMetaData(self,column,property,val):
        if (self.metadata is None):
            self.metadata = haxe_ds_StringMap()
            self.keys = haxe_ds_StringMap()
        if (not (column in self.metadata.h)):
            this1 = self.metadata
            value = haxe_ds_StringMap()
            this1.h[column] = value
        props = self.metadata.h.get(column,None)
        props.h[property] = val
        self.keys.h[property] = True

    def asTable(self):
        if (self.has_properties and ((self.metadata is None))):
            return self.t
        if (self.metadata is None):
            return None
        w = self.t.get_width()
        props = list()
        k = self.keys.keys()
        while k.hasNext():
            k1 = k.next()
            props.append(k1)
        props.sort(key= python_lib_Functools.cmp_to_key(Reflect.compare))
        mt = SimpleTable((w + 1),(len(props) + 1))
        mt.setCell(0,0,"@")
        _g = 0
        _g1 = w
        while (_g < _g1):
            x = _g
            _g = (_g + 1)
            name = self.t.getCell(x,0)
            mt.setCell((1 + x),0,name)
            if (not (name in self.metadata.h)):
                continue
            vals = self.metadata.h.get(name,None)
            _g2 = 0
            _g3 = len(props)
            while (_g2 < _g3):
                i = _g2
                _g2 = (_g2 + 1)
                if ((props[i] if i >= 0 and i < len(props) else None) in vals.h):
                    mt.setCell((1 + x),(i + 1),vals.h.get((props[i] if i >= 0 and i < len(props) else None),None))
        _g = 0
        _g1 = len(props)
        while (_g < _g1):
            y = _g
            _g = (_g + 1)
            mt.setCell(0,(y + 1),(props[y] if y >= 0 and y < len(props) else None))
        return mt

    def cloneMeta(self,table = None):
        result = SimpleMeta(table)
        if (self.metadata is not None):
            result.keys = haxe_ds_StringMap()
            k = self.keys.keys()
            while k.hasNext():
                k1 = k.next()
                result.keys.h[k1] = True
            result.metadata = haxe_ds_StringMap()
            k = self.metadata.keys()
            while k.hasNext():
                k1 = k.next()
                if (not (k1 in self.metadata.h)):
                    continue
                vals = self.metadata.h.get(k1,None)
                nvals = haxe_ds_StringMap()
                p = vals.keys()
                while p.hasNext():
                    p1 = p.next()
                    value = vals.h.get(p1,None)
                    nvals.h[p1] = value
                result.metadata.h[k1] = nvals
        return result

    def useForColumnChanges(self):
        return True

    def useForRowChanges(self):
        return self.row_active

    def changeRow(self,rc):
        _this = self.row_change_cache
        _this.append(rc)
        return False

    def applyFlags(self,flags):
        return False

    def getRowStream(self):
        return TableStream(self.t)

    def isNested(self):
        return self.may_be_nested

    def isSql(self):
        return False

    def getName(self):
        return None

SimpleMeta._hx_class = SimpleMeta


class SimpleTable:
    _hx_class_name = "SimpleTable"
    __slots__ = ("data", "w", "h", "meta")
    _hx_fields = ["data", "w", "h", "meta"]
    _hx_methods = ["getTable", "get_width", "get_height", "getCell", "setCell", "toString", "getCellView", "isResizable", "resize", "clear", "insertOrDeleteRows", "insertOrDeleteColumns", "trimBlank", "getData", "clone", "create", "setMeta", "getMeta"]
    _hx_statics = ["tableToString", "tableIsSimilar"]
    _hx_interfaces = [Table]

    def __init__(self,w,h):
        self.data = haxe_ds_IntMap()
        self.w = w
        self.h = h
        self.meta = None

    def getTable(self):
        return self

    def get_width(self):
        return self.w

    def get_height(self):
        return self.h

    def getCell(self,x,y):
        return self.data.h.get((x + ((y * self.w))),None)

    def setCell(self,x,y,c):
        self.data.set((x + ((y * self.w))),c)

    def toString(self):
        return SimpleTable.tableToString(self)

    def getCellView(self):
        return SimpleView()

    def isResizable(self):
        return True

    def resize(self,w,h):
        self.w = w
        self.h = h
        return True

    def clear(self):
        self.data = haxe_ds_IntMap()

    def insertOrDeleteRows(self,fate,hfate):
        data2 = haxe_ds_IntMap()
        _g = 0
        _g1 = len(fate)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            j = (fate[i] if i >= 0 and i < len(fate) else None)
            if (j != -1):
                _g2 = 0
                _g3 = self.w
                while (_g2 < _g3):
                    c = _g2
                    _g2 = (_g2 + 1)
                    idx = ((i * self.w) + c)
                    if (idx in self.data.h):
                        data2.set(((j * self.w) + c),self.data.h.get(idx,None))
        self.h = hfate
        self.data = data2
        return True

    def insertOrDeleteColumns(self,fate,wfate):
        data2 = haxe_ds_IntMap()
        _g = 0
        _g1 = len(fate)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            j = (fate[i] if i >= 0 and i < len(fate) else None)
            if (j != -1):
                _g2 = 0
                _g3 = self.h
                while (_g2 < _g3):
                    r = _g2
                    _g2 = (_g2 + 1)
                    idx = ((r * self.w) + i)
                    if (idx in self.data.h):
                        data2.set(((r * wfate) + j),self.data.h.get(idx,None))
        self.w = wfate
        self.data = data2
        return True

    def trimBlank(self):
        if (self.h == 0):
            return True
        h_test = self.h
        if (h_test >= 3):
            h_test = 3
        view = self.getCellView()
        space = view.toDatum("")
        more = True
        while more:
            _g = 0
            _g1 = self.get_width()
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                c = self.getCell(i,(self.h - 1))
                if (not ((view.equals(c,space) or ((c is None))))):
                    more = False
                    break
            if more:
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.h
                _hx_local_0.h = (_hx_local_1 - 1)
                _hx_local_1
        more = True
        nw = self.w
        while more:
            if (self.w == 0):
                break
            _g = 0
            _g1 = h_test
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                c = self.getCell((nw - 1),i)
                if (not ((view.equals(c,space) or ((c is None))))):
                    more = False
                    break
            if more:
                nw = (nw - 1)
        if (nw == self.w):
            return True
        data2 = haxe_ds_IntMap()
        _g = 0
        _g1 = nw
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            _g2 = 0
            _g3 = self.h
            while (_g2 < _g3):
                r = _g2
                _g2 = (_g2 + 1)
                idx = ((r * self.w) + i)
                if (idx in self.data.h):
                    data2.set(((r * nw) + i),self.data.h.get(idx,None))
        self.w = nw
        self.data = data2
        return True

    def getData(self):
        return None

    def clone(self):
        result = SimpleTable(self.get_width(),self.get_height())
        _g = 0
        _g1 = self.get_height()
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            _g2 = 0
            _g3 = self.get_width()
            while (_g2 < _g3):
                j = _g2
                _g2 = (_g2 + 1)
                result.setCell(j,i,self.getCell(j,i))
        if (self.meta is not None):
            result.meta = self.meta.cloneMeta(result)
        return result

    def create(self):
        return SimpleTable(self.get_width(),self.get_height())

    def setMeta(self,meta):
        self.meta = meta

    def getMeta(self):
        return self.meta

    @staticmethod
    def tableToString(tab):
        meta = tab.getMeta()
        if (meta is not None):
            stream = meta.getRowStream()
            if (stream is not None):
                x = ""
                cols = stream.fetchColumns()
                _g = 0
                _g1 = len(cols)
                while (_g < _g1):
                    i = _g
                    _g = (_g + 1)
                    if (i > 0):
                        x = (("null" if x is None else x) + ",")
                    x = (("null" if x is None else x) + HxOverrides.stringOrNull((cols[i] if i >= 0 and i < len(cols) else None)))
                x = (("null" if x is None else x) + "\n")
                row = stream.fetchRow()
                while (row is not None):
                    _g = 0
                    _g1 = len(cols)
                    while (_g < _g1):
                        i = _g
                        _g = (_g + 1)
                        if (i > 0):
                            x = (("null" if x is None else x) + ",")
                        x = (("null" if x is None else x) + Std.string(row.h.get((cols[i] if i >= 0 and i < len(cols) else None),None)))
                    x = (("null" if x is None else x) + "\n")
                    row = stream.fetchRow()
                return x
        x = ""
        _g = 0
        _g1 = tab.get_height()
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            _g2 = 0
            _g3 = tab.get_width()
            while (_g2 < _g3):
                j = _g2
                _g2 = (_g2 + 1)
                if (j > 0):
                    x = (("null" if x is None else x) + ",")
                x = (("null" if x is None else x) + Std.string(tab.getCell(j,i)))
            x = (("null" if x is None else x) + "\n")
        return x

    @staticmethod
    def tableIsSimilar(tab1,tab2):
        if ((tab1.get_height() == -1) or ((tab2.get_height() == -1))):
            txt1 = SimpleTable.tableToString(tab1)
            txt2 = SimpleTable.tableToString(tab2)
            return (txt1 == txt2)
        if (tab1.get_width() != tab2.get_width()):
            return False
        if (tab1.get_height() != tab2.get_height()):
            return False
        v = tab1.getCellView()
        _g = 0
        _g1 = tab1.get_height()
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            _g2 = 0
            _g3 = tab1.get_width()
            while (_g2 < _g3):
                j = _g2
                _g2 = (_g2 + 1)
                if (not v.equals(tab1.getCell(j,i),tab2.getCell(j,i))):
                    return False
        return True

SimpleTable._hx_class = SimpleTable


class View:
    _hx_class_name = "View"
    __slots__ = ()
    _hx_methods = ["toString", "equals", "toDatum", "makeHash", "hashSet", "isHash", "hashExists", "hashGet", "isTable", "getTable", "wrapTable"]
View._hx_class = View


class SimpleView:
    _hx_class_name = "SimpleView"
    __slots__ = ()
    _hx_methods = ["toString", "equals", "toDatum", "makeHash", "hashSet", "hashExists", "hashGet", "isHash", "isTable", "getTable", "wrapTable"]
    _hx_interfaces = [View]

    def __init__(self):
        pass

    def toString(self,d):
        if (d is None):
            return ""
        return ("" + Std.string(d))

    def equals(self,d1,d2):
        if ((d1 is None) and ((d2 is None))):
            return True
        if ((d1 is None) or ((d2 is None))):
            return False
        return (("" + Std.string(d1)) == (("" + Std.string(d2))))

    def toDatum(self,x):
        return x

    def makeHash(self):
        return haxe_ds_StringMap()

    def hashSet(self,h,_hx_str,d):
        hh = h
        hh.h[_hx_str] = d

    def hashExists(self,h,_hx_str):
        hh = h
        return (_hx_str in hh.h)

    def hashGet(self,h,_hx_str):
        hh = h
        return hh.h.get(_hx_str,None)

    def isHash(self,h):
        return Std.isOfType(h,haxe_ds_StringMap)

    def isTable(self,t):
        return Std.isOfType(t,Table)

    def getTable(self,t):
        return t

    def wrapTable(self,t):
        return t

SimpleView._hx_class = SimpleView


class SparseSheet:
    _hx_class_name = "SparseSheet"
    __slots__ = ("h", "w", "row", "zero")
    _hx_fields = ["h", "w", "row", "zero"]
    _hx_methods = ["resize", "nonDestructiveResize", "get", "set"]

    def __init__(self):
        self.zero = None
        self.row = None
        def _hx_local_0():
            self.w = 0
            return self.w
        self.h = _hx_local_0()

    def resize(self,w,h,zero):
        self.row = haxe_ds_IntMap()
        self.nonDestructiveResize(w,h,zero)

    def nonDestructiveResize(self,w,h,zero):
        self.w = w
        self.h = h
        self.zero = zero

    def get(self,x,y):
        cursor = self.row.h.get(y,None)
        if (cursor is None):
            return self.zero
        val = cursor.h.get(x,None)
        if (val is None):
            return self.zero
        return val

    def set(self,x,y,val):
        cursor = self.row.h.get(y,None)
        if (cursor is None):
            cursor = haxe_ds_IntMap()
            self.row.set(y,cursor)
        cursor.set(x,val)

SparseSheet._hx_class = SparseSheet


class SqlColumn:
    _hx_class_name = "SqlColumn"
    __slots__ = ("name", "primary", "type_value", "type_family")
    _hx_fields = ["name", "primary", "type_value", "type_family"]
    _hx_methods = ["setName", "setPrimaryKey", "setType", "getName", "isPrimaryKey", "toString"]

    def __init__(self):
        self.name = ""
        self.primary = False
        self.type_value = None
        self.type_family = None

    def setName(self,name):
        self.name = name

    def setPrimaryKey(self,primary):
        self.primary = primary

    def setType(self,value,family):
        self.type_value = value
        self.type_family = family

    def getName(self):
        return self.name

    def isPrimaryKey(self):
        return self.primary

    def toString(self):
        return (HxOverrides.stringOrNull((("*" if (self.primary) else ""))) + HxOverrides.stringOrNull(self.name))

SqlColumn._hx_class = SqlColumn


class SqlCompare:
    _hx_class_name = "SqlCompare"
    __slots__ = ("db", "local", "remote", "alt", "at0", "at1", "at2", "diff_ct", "align", "peered", "alt_peered", "needed", "flags")
    _hx_fields = ["db", "local", "remote", "alt", "at0", "at1", "at2", "diff_ct", "align", "peered", "alt_peered", "needed", "flags"]
    _hx_methods = ["equalArray", "validateSchema", "denull", "link", "linkQuery", "where", "scanColumns", "apply"]

    def __init__(self,db,local,remote,alt,align = None,flags = None):
        self.needed = None
        self.alt_peered = None
        self.peered = None
        self.diff_ct = None
        self.at2 = None
        self.at1 = None
        self.at0 = None
        self.db = db
        self.local = local
        self.remote = remote
        self.alt = alt
        self.align = align
        self.flags = flags
        if (self.flags is None):
            self.flags = CompareFlags()
        self.peered = False
        self.alt_peered = False
        if ((local is not None) and ((remote is not None))):
            if (self.remote.getDatabase().getNameForAttachment() is not None):
                if (self.remote.getDatabase().getNameForAttachment() != self.local.getDatabase().getNameForAttachment()):
                    local.getDatabase().getHelper().attach(db,"__peer__",self.remote.getDatabase().getNameForAttachment())
                    self.peered = True
        if ((self.alt is not None) and ((local is not None))):
            if (self.alt.getDatabase().getNameForAttachment() is not None):
                if (self.alt.getDatabase().getNameForAttachment() != self.local.getDatabase().getNameForAttachment()):
                    local.getDatabase().getHelper().attach(db,"__alt__",self.alt.getDatabase().getNameForAttachment())
                    self.alt_peered = True

    def equalArray(self,a1,a2):
        if (len(a1) != len(a2)):
            return False
        _g = 0
        _g1 = len(a1)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            if ((a1[i] if i >= 0 and i < len(a1) else None) != (a2[i] if i >= 0 and i < len(a2) else None)):
                return False
        return True

    def validateSchema(self):
        all_cols1 = []
        key_cols1 = []
        access_error = False
        pk_missing = False
        if (self.local is not None):
            all_cols1 = self.local.getColumnNames()
            key_cols1 = self.local.getPrimaryKey()
            if (len(all_cols1) == 0):
                access_error = True
            if (self.flags.ids is not None):
                key_cols1 = self.flags.getIdsByRole("local")
            if (len(key_cols1) == 0):
                pk_missing = True
        all_cols2 = []
        key_cols2 = []
        if (self.remote is not None):
            all_cols2 = self.remote.getColumnNames()
            key_cols2 = self.remote.getPrimaryKey()
            if (len(all_cols2) == 0):
                access_error = True
            if (self.flags.ids is not None):
                key_cols2 = self.flags.getIdsByRole("remote")
            if (len(key_cols2) == 0):
                pk_missing = True
        all_cols3 = all_cols2
        key_cols3 = key_cols2
        if (self.alt is not None):
            all_cols3 = self.alt.getColumnNames()
            key_cols3 = self.alt.getPrimaryKey()
            if (len(all_cols3) == 0):
                access_error = True
            if (self.flags.ids is not None):
                key_cols3 = self.flags.getIdsByRole("parent")
            if (len(key_cols3) == 0):
                pk_missing = True
        if access_error:
            raise haxe_Exception.thrown("Error accessing SQL table")
        if pk_missing:
            raise haxe_Exception.thrown("sql diff not possible when primary key not available")
        pk_change = False
        if ((self.local is not None) and ((self.remote is not None))):
            if (not self.equalArray(key_cols1,key_cols2)):
                pk_change = True
        if ((self.local is not None) and ((self.alt is not None))):
            if (not self.equalArray(key_cols1,key_cols3)):
                pk_change = True
        if pk_change:
            raise haxe_Exception.thrown(("sql diff not possible when primary key changes: " + Std.string([key_cols1, key_cols2, key_cols3])))
        return True

    def denull(self,x):
        if (x is None):
            return -1
        return x

    def link(self):
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0.diff_ct
        _hx_local_0.diff_ct = (_hx_local_1 + 1)
        _hx_local_1
        mode = self.db.get(0)
        i0 = self.denull(self.db.get(1))
        i1 = self.denull(self.db.get(2))
        i2 = self.denull(self.db.get(3))
        if (i0 == -3):
            i0 = self.at0
            _hx_local_2 = self
            _hx_local_3 = _hx_local_2.at0
            _hx_local_2.at0 = (_hx_local_3 + 1)
            _hx_local_3
        if (i1 == -3):
            i1 = self.at1
            _hx_local_4 = self
            _hx_local_5 = _hx_local_4.at1
            _hx_local_4.at1 = (_hx_local_5 + 1)
            _hx_local_5
        if (i2 == -3):
            i2 = self.at2
            _hx_local_6 = self
            _hx_local_7 = _hx_local_6.at2
            _hx_local_6.at2 = (_hx_local_7 + 1)
            _hx_local_7
        offset = 4
        if (i0 >= 0):
            _g = 0
            _g1 = self.local.get_width()
            while (_g < _g1):
                x = _g
                _g = (_g + 1)
                self.local.setCellCache(x,i0,self.db.get((x + offset)))
            offset = (offset + self.local.get_width())
        if (i1 >= 0):
            _g = 0
            _g1 = self.remote.get_width()
            while (_g < _g1):
                x = _g
                _g = (_g + 1)
                self.remote.setCellCache(x,i1,self.db.get((x + offset)))
            offset = (offset + self.remote.get_width())
        if (i2 >= 0):
            _g = 0
            _g1 = self.alt.get_width()
            while (_g < _g1):
                x = _g
                _g = (_g + 1)
                self.alt.setCellCache(x,i2,self.db.get((x + offset)))
        if ((mode == 0) or ((mode == 2))):
            self.align.link(i0,i1)
            self.align.addToOrder(i0,i1)
        if (self.alt is not None):
            if ((mode == 1) or ((mode == 2))):
                self.align.reference.link(i0,i2)
                self.align.reference.addToOrder(i0,i2)

    def linkQuery(self,query,order):
        if self.db.begin(query,None,order):
            while self.db.read():
                self.link()
            self.db.end()

    def where(self,txt):
        if (txt == ""):
            return " WHERE 1 = 0"
        return (" WHERE " + ("null" if txt is None else txt))

    def scanColumns(self,all_cols1,all_cols2,key_cols,present1,present2,align):
        align.meta = Alignment()
        _g = 0
        _g1 = len(all_cols1)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            key = (all_cols1[i] if i >= 0 and i < len(all_cols1) else None)
            if (key in present2.h):
                align.meta.link(i,present2.h.get(key,None))
            else:
                align.meta.link(i,-1)
        _g = 0
        _g1 = len(all_cols2)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            key = (all_cols2[i] if i >= 0 and i < len(all_cols2) else None)
            if (not (key in present1.h)):
                align.meta.link(-1,i)
        align.meta.range(len(all_cols1),len(all_cols2))
        _g = 0
        while (_g < len(key_cols)):
            key = (key_cols[_g] if _g >= 0 and _g < len(key_cols) else None)
            _g = (_g + 1)
            unit = Unit(present1.h.get(key,None),present2.h.get(key,None))
            align.addIndexColumns(unit)

    def apply(self):
        if (self.db is None):
            return None
        if (self.align is None):
            self.align = Alignment()
        if (not self.validateSchema()):
            return None
        rowid_name = self.db.rowid()
        key_cols = []
        data_cols = []
        all_cols = []
        all_cols1 = []
        all_cols2 = []
        all_cols3 = []
        common = self.local
        if (self.local is not None):
            key_cols = self.local.getPrimaryKey()
            data_cols = self.local.getAllButPrimaryKey()
            all_cols = self.local.getColumnNames()
            all_cols1 = self.local.getColumnNames()
            if (self.flags.ids is not None):
                key_cols = self.flags.getIdsByRole("local")
                data_cols = list()
                pks = haxe_ds_StringMap()
                _g = 0
                while (_g < len(key_cols)):
                    col = (key_cols[_g] if _g >= 0 and _g < len(key_cols) else None)
                    _g = (_g + 1)
                    pks.h[col] = True
                _g = 0
                while (_g < len(all_cols)):
                    col = (all_cols[_g] if _g >= 0 and _g < len(all_cols) else None)
                    _g = (_g + 1)
                    if (not (col in pks.h)):
                        data_cols.append(col)
        if (self.remote is not None):
            all_cols2 = self.remote.getColumnNames()
            if (common is None):
                common = self.remote
        if (self.alt is not None):
            all_cols3 = self.alt.getColumnNames()
            if (common is None):
                common = self.alt
        else:
            all_cols3 = all_cols2
        all_common_cols = list()
        data_common_cols = list()
        present1 = haxe_ds_StringMap()
        present2 = haxe_ds_StringMap()
        present3 = haxe_ds_StringMap()
        present_primary = haxe_ds_StringMap()
        has_column_add = False
        _g = 0
        _g1 = len(key_cols)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            present_primary.h[(key_cols[i] if i >= 0 and i < len(key_cols) else None)] = i
        _g = 0
        _g1 = len(all_cols1)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            key = (all_cols1[i] if i >= 0 and i < len(all_cols1) else None)
            present1.h[key] = i
        _g = 0
        _g1 = len(all_cols2)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            key = (all_cols2[i] if i >= 0 and i < len(all_cols2) else None)
            if (not (key in present1.h)):
                has_column_add = True
            present2.h[key] = i
        _g = 0
        _g1 = len(all_cols3)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            key = (all_cols3[i] if i >= 0 and i < len(all_cols3) else None)
            if (not (key in present1.h)):
                has_column_add = True
            present3.h[key] = i
            if (key in present1.h):
                if (key in present2.h):
                    all_common_cols.append(key)
                    if (not (key in present_primary.h)):
                        data_common_cols.append(key)
        self.align.meta = Alignment()
        _g = 0
        _g1 = len(all_cols1)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            key = (all_cols1[i] if i >= 0 and i < len(all_cols1) else None)
            if (key in present2.h):
                self.align.meta.link(i,present2.h.get(key,None))
            else:
                self.align.meta.link(i,-1)
        _g = 0
        _g1 = len(all_cols2)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            key = (all_cols2[i] if i >= 0 and i < len(all_cols2) else None)
            if (not (key in present1.h)):
                self.align.meta.link(-1,i)
        self.scanColumns(all_cols1,all_cols2,key_cols,present1,present2,self.align)
        self.align.tables(self.local,self.remote)
        if (self.alt is not None):
            self.scanColumns(all_cols1,all_cols3,key_cols,present1,present3,self.align.reference)
            self.align.reference.tables(self.local,self.alt)
        sql_table1 = ""
        sql_table2 = ""
        sql_table3 = ""
        if (self.local is not None):
            sql_table1 = self.local.getQuotedTableName()
        if (self.remote is not None):
            sql_table2 = self.remote.getQuotedTableName()
        if (self.alt is not None):
            sql_table3 = self.alt.getQuotedTableName()
        if self.peered:
            sql_table1 = ("main." + ("null" if sql_table1 is None else sql_table1))
            sql_table2 = ("__peer__." + ("null" if sql_table2 is None else sql_table2))
        if self.alt_peered:
            sql_table2 = ("__alt__." + ("null" if sql_table3 is None else sql_table3))
        sql_key_cols = ""
        _g = 0
        _g1 = len(key_cols)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            if (i > 0):
                sql_key_cols = (("null" if sql_key_cols is None else sql_key_cols) + ",")
            sql_key_cols = (("null" if sql_key_cols is None else sql_key_cols) + HxOverrides.stringOrNull(common.getQuotedColumnName((key_cols[i] if i >= 0 and i < len(key_cols) else None))))
        sql_all_cols = ""
        _g = 0
        _g1 = len(all_common_cols)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            if (i > 0):
                sql_all_cols = (("null" if sql_all_cols is None else sql_all_cols) + ",")
            sql_all_cols = (("null" if sql_all_cols is None else sql_all_cols) + HxOverrides.stringOrNull(common.getQuotedColumnName((all_common_cols[i] if i >= 0 and i < len(all_common_cols) else None))))
        sql_all_cols1 = ""
        _g = 0
        _g1 = len(all_cols1)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            if (i > 0):
                sql_all_cols1 = (("null" if sql_all_cols1 is None else sql_all_cols1) + ",")
            sql_all_cols1 = (("null" if sql_all_cols1 is None else sql_all_cols1) + HxOverrides.stringOrNull((((("null" if sql_table1 is None else sql_table1) + ".") + HxOverrides.stringOrNull(self.local.getQuotedColumnName((all_cols1[i] if i >= 0 and i < len(all_cols1) else None)))))))
        sql_all_cols2 = ""
        _g = 0
        _g1 = len(all_cols2)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            if (i > 0):
                sql_all_cols2 = (("null" if sql_all_cols2 is None else sql_all_cols2) + ",")
            sql_all_cols2 = (("null" if sql_all_cols2 is None else sql_all_cols2) + HxOverrides.stringOrNull((((("null" if sql_table2 is None else sql_table2) + ".") + HxOverrides.stringOrNull(self.remote.getQuotedColumnName((all_cols2[i] if i >= 0 and i < len(all_cols2) else None)))))))
        sql_all_cols3 = ""
        if (self.alt is not None):
            _g = 0
            _g1 = len(all_cols3)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                if (i > 0):
                    sql_all_cols3 = (("null" if sql_all_cols3 is None else sql_all_cols3) + ",")
                sql_all_cols3 = (("null" if sql_all_cols3 is None else sql_all_cols3) + HxOverrides.stringOrNull((((("null" if sql_table3 is None else sql_table3) + ".") + HxOverrides.stringOrNull(self.alt.getQuotedColumnName((all_cols3[i] if i >= 0 and i < len(all_cols3) else None)))))))
        sql_key_null = ""
        _g = 0
        _g1 = len(key_cols)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            if (i > 0):
                sql_key_null = (("null" if sql_key_null is None else sql_key_null) + " AND ")
            n = common.getQuotedColumnName((key_cols[i] if i >= 0 and i < len(key_cols) else None))
            sql_key_null = (("null" if sql_key_null is None else sql_key_null) + HxOverrides.stringOrNull(((((("null" if sql_table1 is None else sql_table1) + ".") + ("null" if n is None else n)) + " IS NULL"))))
        sql_key_null2 = ""
        _g = 0
        _g1 = len(key_cols)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            if (i > 0):
                sql_key_null2 = (("null" if sql_key_null2 is None else sql_key_null2) + " AND ")
            n = common.getQuotedColumnName((key_cols[i] if i >= 0 and i < len(key_cols) else None))
            sql_key_null2 = (("null" if sql_key_null2 is None else sql_key_null2) + HxOverrides.stringOrNull(((((("null" if sql_table2 is None else sql_table2) + ".") + ("null" if n is None else n)) + " IS NULL"))))
        sql_key_match2 = ""
        _g = 0
        _g1 = len(key_cols)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            if (i > 0):
                sql_key_match2 = (("null" if sql_key_match2 is None else sql_key_match2) + " AND ")
            n = common.getQuotedColumnName((key_cols[i] if i >= 0 and i < len(key_cols) else None))
            sql_key_match2 = (("null" if sql_key_match2 is None else sql_key_match2) + HxOverrides.stringOrNull((((((((("null" if sql_table1 is None else sql_table1) + ".") + ("null" if n is None else n)) + " IS ") + ("null" if sql_table2 is None else sql_table2)) + ".") + ("null" if n is None else n)))))
        sql_key_match3 = ""
        if (self.alt is not None):
            _g = 0
            _g1 = len(key_cols)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                if (i > 0):
                    sql_key_match3 = (("null" if sql_key_match3 is None else sql_key_match3) + " AND ")
                n = common.getQuotedColumnName((key_cols[i] if i >= 0 and i < len(key_cols) else None))
                sql_key_match3 = (("null" if sql_key_match3 is None else sql_key_match3) + HxOverrides.stringOrNull((((((((("null" if sql_table1 is None else sql_table1) + ".") + ("null" if n is None else n)) + " IS ") + ("null" if sql_table3 is None else sql_table3)) + ".") + ("null" if n is None else n)))))
        sql_data_mismatch = ""
        _g = 0
        _g1 = len(data_common_cols)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            if (i > 0):
                sql_data_mismatch = (("null" if sql_data_mismatch is None else sql_data_mismatch) + " OR ")
            n = common.getQuotedColumnName((data_common_cols[i] if i >= 0 and i < len(data_common_cols) else None))
            sql_data_mismatch = (("null" if sql_data_mismatch is None else sql_data_mismatch) + HxOverrides.stringOrNull((((((((("null" if sql_table1 is None else sql_table1) + ".") + ("null" if n is None else n)) + " IS NOT ") + ("null" if sql_table2 is None else sql_table2)) + ".") + ("null" if n is None else n)))))
        _g = 0
        _g1 = len(all_cols2)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            key = (all_cols2[i] if i >= 0 and i < len(all_cols2) else None)
            if (not (key in present1.h)):
                if (sql_data_mismatch != ""):
                    sql_data_mismatch = (("null" if sql_data_mismatch is None else sql_data_mismatch) + " OR ")
                n = common.getQuotedColumnName(key)
                sql_data_mismatch = (("null" if sql_data_mismatch is None else sql_data_mismatch) + HxOverrides.stringOrNull(((((("null" if sql_table2 is None else sql_table2) + ".") + ("null" if n is None else n)) + " IS NOT NULL"))))
        if (self.alt is not None):
            _g = 0
            _g1 = len(data_common_cols)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                if (len(sql_data_mismatch) > 0):
                    sql_data_mismatch = (("null" if sql_data_mismatch is None else sql_data_mismatch) + " OR ")
                n = common.getQuotedColumnName((data_common_cols[i] if i >= 0 and i < len(data_common_cols) else None))
                sql_data_mismatch = (("null" if sql_data_mismatch is None else sql_data_mismatch) + HxOverrides.stringOrNull((((((((("null" if sql_table1 is None else sql_table1) + ".") + ("null" if n is None else n)) + " IS NOT ") + ("null" if sql_table3 is None else sql_table3)) + ".") + ("null" if n is None else n)))))
            _g = 0
            _g1 = len(all_cols3)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                key = (all_cols3[i] if i >= 0 and i < len(all_cols3) else None)
                if (not (key in present1.h)):
                    if (sql_data_mismatch != ""):
                        sql_data_mismatch = (("null" if sql_data_mismatch is None else sql_data_mismatch) + " OR ")
                    n = common.getQuotedColumnName(key)
                    sql_data_mismatch = (("null" if sql_data_mismatch is None else sql_data_mismatch) + HxOverrides.stringOrNull(((((("null" if sql_table3 is None else sql_table3) + ".") + ("null" if n is None else n)) + " IS NOT NULL"))))
        sql_dbl_cols = ""
        dbl_cols = []
        _g = 0
        _g1 = len(all_cols1)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            if (sql_dbl_cols != ""):
                sql_dbl_cols = (("null" if sql_dbl_cols is None else sql_dbl_cols) + ",")
            buf = ("__coopy_" + Std.string(i))
            n = common.getQuotedColumnName((all_cols1[i] if i >= 0 and i < len(all_cols1) else None))
            sql_dbl_cols = (("null" if sql_dbl_cols is None else sql_dbl_cols) + HxOverrides.stringOrNull((((((("null" if sql_table1 is None else sql_table1) + ".") + ("null" if n is None else n)) + " AS ") + ("null" if buf is None else buf)))))
            dbl_cols.append(buf)
        _g = 0
        _g1 = len(all_cols2)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            if (sql_dbl_cols != ""):
                sql_dbl_cols = (("null" if sql_dbl_cols is None else sql_dbl_cols) + ",")
            buf = (("__coopy_" + Std.string(i)) + "b")
            n = common.getQuotedColumnName((all_cols2[i] if i >= 0 and i < len(all_cols2) else None))
            sql_dbl_cols = (("null" if sql_dbl_cols is None else sql_dbl_cols) + HxOverrides.stringOrNull((((((("null" if sql_table2 is None else sql_table2) + ".") + ("null" if n is None else n)) + " AS ") + ("null" if buf is None else buf)))))
            dbl_cols.append(buf)
        if (self.alt is not None):
            _g = 0
            _g1 = len(all_cols3)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                if (sql_dbl_cols != ""):
                    sql_dbl_cols = (("null" if sql_dbl_cols is None else sql_dbl_cols) + ",")
                buf = (("__coopy_" + Std.string(i)) + "c")
                n = common.getQuotedColumnName((all_cols3[i] if i >= 0 and i < len(all_cols3) else None))
                sql_dbl_cols = (("null" if sql_dbl_cols is None else sql_dbl_cols) + HxOverrides.stringOrNull((((((("null" if sql_table3 is None else sql_table3) + ".") + ("null" if n is None else n)) + " AS ") + ("null" if buf is None else buf)))))
                dbl_cols.append(buf)
        sql_order = ""
        _g = 0
        _g1 = len(key_cols)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            if (i > 0):
                sql_order = (("null" if sql_order is None else sql_order) + ",")
            n = common.getQuotedColumnName((key_cols[i] if i >= 0 and i < len(key_cols) else None))
            sql_order = (("null" if sql_order is None else sql_order) + ("null" if n is None else n))
        rowid = "-3"
        rowid1 = "-3"
        rowid2 = "-3"
        rowid3 = "-3"
        if (rowid_name is not None):
            rowid = rowid_name
            if (self.local is not None):
                rowid1 = ((("null" if sql_table1 is None else sql_table1) + ".") + ("null" if rowid_name is None else rowid_name))
            if (self.remote is not None):
                rowid2 = ((("null" if sql_table2 is None else sql_table2) + ".") + ("null" if rowid_name is None else rowid_name))
            if (self.alt is not None):
                rowid3 = ((("null" if sql_table3 is None else sql_table3) + ".") + ("null" if rowid_name is None else rowid_name))
        self.at0 = 1
        self.at1 = 1
        self.at2 = 1
        self.diff_ct = 0
        if (self.remote is not None):
            sql_inserts = ((((("SELECT DISTINCT 0 AS __coopy_code, NULL, " + ("null" if rowid2 is None else rowid2)) + " AS rowid, NULL, ") + ("null" if sql_all_cols2 is None else sql_all_cols2)) + " FROM ") + ("null" if sql_table2 is None else sql_table2))
            if (self.local is not None):
                sql_inserts = (("null" if sql_inserts is None else sql_inserts) + HxOverrides.stringOrNull(((" LEFT JOIN " + ("null" if sql_table1 is None else sql_table1)))))
                sql_inserts = (("null" if sql_inserts is None else sql_inserts) + HxOverrides.stringOrNull((((" ON " + ("null" if sql_key_match2 is None else sql_key_match2)) + HxOverrides.stringOrNull(self.where(sql_key_null))))))
            if (sql_table1 != sql_table2):
                sql_inserts_order = (["__coopy_code", "NULL", "rowid", "NULL"] + all_cols2)
                self.linkQuery(sql_inserts,sql_inserts_order)
        if (self.alt is not None):
            sql_inserts = ((((("SELECT DISTINCT 0 AS __coopy_code, NULL, NULL, " + ("null" if rowid3 is None else rowid3)) + " AS rowid, ") + ("null" if sql_all_cols3 is None else sql_all_cols3)) + " FROM ") + ("null" if sql_table3 is None else sql_table3))
            if (self.local is not None):
                sql_inserts = (("null" if sql_inserts is None else sql_inserts) + HxOverrides.stringOrNull(((" LEFT JOIN " + ("null" if sql_table1 is None else sql_table1)))))
                sql_inserts = (("null" if sql_inserts is None else sql_inserts) + HxOverrides.stringOrNull((((" ON " + ("null" if sql_key_match3 is None else sql_key_match3)) + HxOverrides.stringOrNull(self.where(sql_key_null))))))
            if (sql_table1 != sql_table3):
                sql_inserts_order = (["__coopy_code", "NULL", "NULL", "rowid"] + all_cols3)
                self.linkQuery(sql_inserts,sql_inserts_order)
        if ((self.local is not None) and ((self.remote is not None))):
            sql_updates = (((("SELECT DISTINCT 2 AS __coopy_code, " + ("null" if rowid1 is None else rowid1)) + " AS __coopy_rowid0, ") + ("null" if rowid2 is None else rowid2)) + " AS __coopy_rowid1, ")
            if (self.alt is not None):
                sql_updates = (("null" if sql_updates is None else sql_updates) + HxOverrides.stringOrNull(((("null" if rowid3 is None else rowid3) + " AS __coopy_rowid2,"))))
            else:
                sql_updates = (("null" if sql_updates is None else sql_updates) + " NULL,")
            sql_updates = (("null" if sql_updates is None else sql_updates) + HxOverrides.stringOrNull((((("null" if sql_dbl_cols is None else sql_dbl_cols) + " FROM ") + ("null" if sql_table1 is None else sql_table1)))))
            if (sql_table1 != sql_table2):
                sql_updates = (("null" if sql_updates is None else sql_updates) + HxOverrides.stringOrNull(((((" INNER JOIN " + ("null" if sql_table2 is None else sql_table2)) + " ON ") + ("null" if sql_key_match2 is None else sql_key_match2)))))
            if ((self.alt is not None) and ((sql_table1 != sql_table3))):
                sql_updates = (("null" if sql_updates is None else sql_updates) + HxOverrides.stringOrNull(((((" INNER JOIN " + ("null" if sql_table3 is None else sql_table3)) + " ON ") + ("null" if sql_key_match3 is None else sql_key_match3)))))
            sql_updates = (("null" if sql_updates is None else sql_updates) + HxOverrides.stringOrNull(self.where(sql_data_mismatch)))
            sql_updates_order = (["__coopy_code", "__coopy_rowid0", "__coopy_rowid1", "__coopy_rowid2"] + dbl_cols)
            self.linkQuery(sql_updates,sql_updates_order)
        if (self.alt is None):
            if (self.local is not None):
                sql_deletes = ((((("SELECT DISTINCT 0 AS __coopy_code, " + ("null" if rowid1 is None else rowid1)) + " AS rowid, NULL, NULL, ") + ("null" if sql_all_cols1 is None else sql_all_cols1)) + " FROM ") + ("null" if sql_table1 is None else sql_table1))
                if (self.remote is not None):
                    sql_deletes = (("null" if sql_deletes is None else sql_deletes) + HxOverrides.stringOrNull(((" LEFT JOIN " + ("null" if sql_table2 is None else sql_table2)))))
                    sql_deletes = (("null" if sql_deletes is None else sql_deletes) + HxOverrides.stringOrNull((((" ON " + ("null" if sql_key_match2 is None else sql_key_match2)) + HxOverrides.stringOrNull(self.where(sql_key_null2))))))
                if (sql_table1 != sql_table2):
                    sql_deletes_order = (["__coopy_code", "rowid", "NULL", "NULL"] + all_cols1)
                    self.linkQuery(sql_deletes,sql_deletes_order)
        if (self.alt is not None):
            sql_deletes = (((("SELECT 2 AS __coopy_code, " + ("null" if rowid1 is None else rowid1)) + " AS __coopy_rowid0, ") + ("null" if rowid2 is None else rowid2)) + " AS __coopy_rowid1, ")
            sql_deletes = (("null" if sql_deletes is None else sql_deletes) + HxOverrides.stringOrNull(((("null" if rowid3 is None else rowid3) + " AS __coopy_rowid2, "))))
            sql_deletes = (("null" if sql_deletes is None else sql_deletes) + ("null" if sql_dbl_cols is None else sql_dbl_cols))
            sql_deletes = (("null" if sql_deletes is None else sql_deletes) + HxOverrides.stringOrNull(((" FROM " + ("null" if sql_table1 is None else sql_table1)))))
            if (self.remote is not None):
                sql_deletes = (("null" if sql_deletes is None else sql_deletes) + HxOverrides.stringOrNull(((((" LEFT OUTER JOIN " + ("null" if sql_table2 is None else sql_table2)) + " ON ") + ("null" if sql_key_match2 is None else sql_key_match2)))))
            sql_deletes = (("null" if sql_deletes is None else sql_deletes) + HxOverrides.stringOrNull(((((" LEFT OUTER JOIN " + ("null" if sql_table3 is None else sql_table3)) + " ON ") + ("null" if sql_key_match3 is None else sql_key_match3)))))
            sql_deletes = (("null" if sql_deletes is None else sql_deletes) + " WHERE __coopy_rowid1 IS NULL OR __coopy_rowid2 IS NULL")
            sql_deletes_order = (["__coopy_code", "__coopy_rowid0", "__coopy_rowid1", "__coopy_rowid2"] + dbl_cols)
            self.linkQuery(sql_deletes,sql_deletes_order)
        if (self.diff_ct == 0):
            self.align.markIdentical()
        return self.align

SqlCompare._hx_class = SqlCompare


class SqlDatabase:
    _hx_class_name = "SqlDatabase"
    __slots__ = ()
    _hx_methods = ["getColumns", "getQuotedTableName", "getQuotedColumnName", "begin", "beginRow", "read", "get", "end", "width", "rowid", "getHelper", "getNameForAttachment"]
SqlDatabase._hx_class = SqlDatabase


class SqlHelper:
    _hx_class_name = "SqlHelper"
    __slots__ = ()
    _hx_methods = ["getTableNames", "countRows", "getRowIDs", "insert", "delete", "update", "attach", "alterColumns"]
SqlHelper._hx_class = SqlHelper


class SqlTable:
    _hx_class_name = "SqlTable"
    __slots__ = ("db", "columns", "name", "quotedTableName", "cache", "columnNames", "h", "helper", "id2rid")
    _hx_fields = ["db", "columns", "name", "quotedTableName", "cache", "columnNames", "h", "helper", "id2rid"]
    _hx_methods = ["getColumns", "getPrimaryKey", "getAllButPrimaryKey", "getColumnNames", "getQuotedTableName", "getQuotedColumnName", "getCell", "setCellCache", "setCell", "getCellView", "isResizable", "resize", "clear", "insertOrDeleteRows", "insertOrDeleteColumns", "trimBlank", "get_width", "get_height", "getData", "clone", "create", "getMeta", "alterColumns", "changeRow", "asTable", "useForColumnChanges", "useForRowChanges", "cloneMeta", "applyFlags", "getDatabase", "getRowStream", "isNested", "isSql", "fetchRow", "fetchColumns", "getName"]
    _hx_interfaces = [RowStream, Meta, Table]

    def __init__(self,db,name,helper = None):
        self.columnNames = None
        self.quotedTableName = None
        self.columns = None
        self.db = db
        self.name = name
        self.helper = helper
        if (helper is None):
            self.helper = db.getHelper()
        self.cache = haxe_ds_IntMap()
        self.h = -1
        self.id2rid = None
        self.getColumns()

    def getColumns(self):
        if (self.columns is not None):
            return
        if (self.db is None):
            return
        self.columns = self.db.getColumns(self.name)
        self.columnNames = list()
        _g = 0
        _g1 = self.columns
        while (_g < len(_g1)):
            col = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            _this = self.columnNames
            x = col.getName()
            _this.append(x)

    def getPrimaryKey(self):
        self.getColumns()
        result = list()
        _g = 0
        _g1 = self.columns
        while (_g < len(_g1)):
            col = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            if (not col.isPrimaryKey()):
                continue
            x = col.getName()
            result.append(x)
        return result

    def getAllButPrimaryKey(self):
        self.getColumns()
        result = list()
        _g = 0
        _g1 = self.columns
        while (_g < len(_g1)):
            col = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            if col.isPrimaryKey():
                continue
            x = col.getName()
            result.append(x)
        return result

    def getColumnNames(self):
        self.getColumns()
        return self.columnNames

    def getQuotedTableName(self):
        if (self.quotedTableName is not None):
            return self.quotedTableName
        self.quotedTableName = self.db.getQuotedTableName(self.name)
        return self.quotedTableName

    def getQuotedColumnName(self,name):
        return self.db.getQuotedColumnName(name)

    def getCell(self,x,y):
        if (self.h >= 0):
            y = (y - 1)
            if (y >= 0):
                y = (self.id2rid[y] if y >= 0 and y < len(self.id2rid) else None)
        elif (y == 0):
            y = -1
        if (y < 0):
            self.getColumns()
            return (self.columns[x] if x >= 0 and x < len(self.columns) else None).name
        row = self.cache.h.get(y,None)
        if (row is None):
            row = haxe_ds_IntMap()
            self.getColumns()
            self.db.beginRow(self.name,y,self.columnNames)
            while self.db.read():
                _g = 0
                _g1 = self.get_width()
                while (_g < _g1):
                    i = _g
                    _g = (_g + 1)
                    v = self.db.get(i)
                    row.set(i,v)
            self.db.end()
            self.cache.set(y,row)
        return self.cache.h.get(y,None).h.get(x,None)

    def setCellCache(self,x,y,c):
        row = self.cache.h.get(y,None)
        if (row is None):
            row = haxe_ds_IntMap()
            self.getColumns()
            self.cache.set(y,row)
        v = c
        row.set(x,v)

    def setCell(self,x,y,c):
        print("SqlTable cannot set cells yet")

    def getCellView(self):
        return SimpleView()

    def isResizable(self):
        return False

    def resize(self,w,h):
        return False

    def clear(self):
        pass

    def insertOrDeleteRows(self,fate,hfate):
        return False

    def insertOrDeleteColumns(self,fate,wfate):
        return False

    def trimBlank(self):
        return False

    def get_width(self):
        self.getColumns()
        return len(self.columns)

    def get_height(self):
        if (self.h >= 0):
            return self.h
        return -1

    def getData(self):
        return None

    def clone(self):
        return None

    def create(self):
        return None

    def getMeta(self):
        return self

    def alterColumns(self,columns):
        result = self.helper.alterColumns(self.db,self.name,columns)
        self.columns = None
        return result

    def changeRow(self,rc):
        if (self.helper is None):
            print("No sql helper")
            return False
        if (rc.action == "+++"):
            return self.helper.insert(self.db,self.name,rc.val)
        elif (rc.action == "---"):
            return self.helper.delete(self.db,self.name,rc.cond)
        elif (rc.action == "->"):
            return self.helper.update(self.db,self.name,rc.cond,rc.val)
        return False

    def asTable(self):
        pct = 3
        self.getColumns()
        w = len(self.columnNames)
        mt = SimpleTable((w + 1),pct)
        mt.setCell(0,0,"@")
        mt.setCell(0,1,"type")
        mt.setCell(0,2,"key")
        _g = 0
        _g1 = w
        while (_g < _g1):
            x = _g
            _g = (_g + 1)
            i = (x + 1)
            mt.setCell(i,0,(self.columnNames[x] if x >= 0 and x < len(self.columnNames) else None))
            mt.setCell(i,1,(self.columns[x] if x >= 0 and x < len(self.columns) else None).type_value)
            mt.setCell(i,2,("primary" if ((self.columns[x] if x >= 0 and x < len(self.columns) else None).primary) else ""))
        return mt

    def useForColumnChanges(self):
        return True

    def useForRowChanges(self):
        return True

    def cloneMeta(self,table = None):
        return None

    def applyFlags(self,flags):
        return False

    def getDatabase(self):
        return self.db

    def getRowStream(self):
        self.getColumns()
        self.db.begin((("SELECT * FROM " + HxOverrides.stringOrNull(self.getQuotedTableName())) + " ORDER BY ?"),[self.db.rowid()],self.columnNames)
        return self

    def isNested(self):
        return False

    def isSql(self):
        return True

    def fetchRow(self):
        if self.db.read():
            row = haxe_ds_StringMap()
            _g = 0
            _g1 = len(self.columnNames)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                k = (self.columnNames[i] if i >= 0 and i < len(self.columnNames) else None)
                v = self.db.get(i)
                row.h[k] = v
            return row
        self.db.end()
        return None

    def fetchColumns(self):
        self.getColumns()
        return self.columnNames

    def getName(self):
        return self.name.toString()

SqlTable._hx_class = SqlTable


class SqlTableName:
    _hx_class_name = "SqlTableName"
    __slots__ = ("name", "prefix")
    _hx_fields = ["name", "prefix"]
    _hx_methods = ["toString"]

    def __init__(self,name = None,prefix = None):
        if (name is None):
            name = ""
        if (prefix is None):
            prefix = ""
        self.name = name
        self.prefix = prefix

    def toString(self):
        if (self.prefix == ""):
            return self.name
        return ((HxOverrides.stringOrNull(self.prefix) + ".") + HxOverrides.stringOrNull(self.name))

SqlTableName._hx_class = SqlTableName


class SqlTables:
    _hx_class_name = "SqlTables"
    __slots__ = ("db", "t", "flags")
    _hx_fields = ["db", "t", "flags"]
    _hx_methods = ["getCell", "setCell", "getCellView", "isResizable", "resize", "clear", "insertOrDeleteRows", "insertOrDeleteColumns", "trimBlank", "get_width", "get_height", "getData", "clone", "create", "getMeta"]
    _hx_interfaces = [Table]

    def __init__(self,db,flags,role):
        self.flags = None
        self.t = None
        self.db = db
        helper = self.db.getHelper()
        names = helper.getTableNames(db)
        allowed = None
        count = len(names)
        if (flags.tables is not None):
            allowed = haxe_ds_StringMap()
            _g = 0
            _g1 = flags.tables
            while (_g < len(_g1)):
                name = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
                _g = (_g + 1)
                key = flags.getNameByRole(name,role)
                value = flags.getCanonicalName(name)
                allowed.h[key] = value
            count = 0
            _g = 0
            while (_g < len(names)):
                name = (names[_g] if _g >= 0 and _g < len(names) else None)
                _g = (_g + 1)
                if (name in allowed.h):
                    count = (count + 1)
        self.t = SimpleTable(2,(count + 1))
        self.t.setCell(0,0,"name")
        self.t.setCell(1,0,"table")
        v = self.t.getCellView()
        at = 1
        _g = 0
        while (_g < len(names)):
            name = (names[_g] if _g >= 0 and _g < len(names) else None)
            _g = (_g + 1)
            cname = name
            if (allowed is not None):
                if (not (name in allowed.h)):
                    continue
                cname = allowed.h.get(name,None)
            self.t.setCell(0,at,cname)
            self.t.setCell(1,at,v.wrapTable(SqlTable(db,SqlTableName(name))))
            at = (at + 1)

    def getCell(self,x,y):
        return self.t.getCell(x,y)

    def setCell(self,x,y,c):
        pass

    def getCellView(self):
        return self.t.getCellView()

    def isResizable(self):
        return False

    def resize(self,w,h):
        return False

    def clear(self):
        pass

    def insertOrDeleteRows(self,fate,hfate):
        return False

    def insertOrDeleteColumns(self,fate,wfate):
        return False

    def trimBlank(self):
        return False

    def get_width(self):
        return self.t.get_width()

    def get_height(self):
        return self.t.get_height()

    def getData(self):
        return None

    def clone(self):
        return None

    def create(self):
        return None

    def getMeta(self):
        return SimpleMeta(self,True,True)

SqlTables._hx_class = SqlTables


class SqliteHelper:
    _hx_class_name = "SqliteHelper"
    __slots__ = ()
    _hx_methods = ["getTableNames", "countRows", "getRowIDs", "update", "delete", "insert", "attach", "columnListSql", "fetchSchema", "splitSchema", "exec", "alterColumns"]
    _hx_interfaces = [SqlHelper]

    def __init__(self):
        pass

    def getTableNames(self,db):
        q = "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
        if (not db.begin(q,None,["name"])):
            return None
        names = list()
        while db.read():
            x = db.get(0)
            names.append(x)
        db.end()
        return names

    def countRows(self,db,name):
        q = ("SELECT COUNT(*) AS ct FROM " + HxOverrides.stringOrNull(db.getQuotedTableName(name)))
        if (not db.begin(q,None,["ct"])):
            return -1
        ct = -1
        while db.read():
            ct = db.get(0)
        db.end()
        return ct

    def getRowIDs(self,db,name):
        result = list()
        q = (("SELECT ROWID AS r FROM " + HxOverrides.stringOrNull(db.getQuotedTableName(name))) + " ORDER BY ROWID")
        if (not db.begin(q,None,["r"])):
            return None
        while db.read():
            c = db.get(0)
            result.append(c)
        db.end()
        return result

    def update(self,db,name,conds,vals):
        q = (("UPDATE " + HxOverrides.stringOrNull(db.getQuotedTableName(name))) + " SET ")
        lst = list()
        k = vals.keys()
        while k.hasNext():
            k1 = k.next()
            if (len(lst) > 0):
                q = (("null" if q is None else q) + ", ")
            q = (("null" if q is None else q) + HxOverrides.stringOrNull(db.getQuotedColumnName(k1)))
            q = (("null" if q is None else q) + " = ?")
            x = vals.h.get(k1,None)
            lst.append(x)
        val_len = len(lst)
        q = (("null" if q is None else q) + " WHERE ")
        k = conds.keys()
        while k.hasNext():
            k1 = k.next()
            if (len(lst) > val_len):
                q = (("null" if q is None else q) + " and ")
            q = (("null" if q is None else q) + HxOverrides.stringOrNull(db.getQuotedColumnName(k1)))
            q = (("null" if q is None else q) + " IS ?")
            x = conds.h.get(k1,None)
            lst.append(x)
        if (not db.begin(q,lst,[])):
            print("Problem with database update")
            return False
        db.end()
        return True

    def delete(self,db,name,conds):
        q = (("DELETE FROM " + HxOverrides.stringOrNull(db.getQuotedTableName(name))) + " WHERE ")
        lst = list()
        k = conds.keys()
        while k.hasNext():
            k1 = k.next()
            if (len(lst) > 0):
                q = (("null" if q is None else q) + " and ")
            q = (("null" if q is None else q) + HxOverrides.stringOrNull(db.getQuotedColumnName(k1)))
            q = (("null" if q is None else q) + " = ?")
            x = conds.h.get(k1,None)
            lst.append(x)
        if (not db.begin(q,lst,[])):
            print("Problem with database delete")
            return False
        db.end()
        return True

    def insert(self,db,name,vals):
        q = (("INSERT INTO " + HxOverrides.stringOrNull(db.getQuotedTableName(name))) + " (")
        lst = list()
        k = vals.keys()
        while k.hasNext():
            k1 = k.next()
            if (len(lst) > 0):
                q = (("null" if q is None else q) + ",")
            q = (("null" if q is None else q) + HxOverrides.stringOrNull(db.getQuotedColumnName(k1)))
            x = vals.h.get(k1,None)
            lst.append(x)
        q = (("null" if q is None else q) + ") VALUES(")
        need_comma = False
        k = vals.keys()
        while k.hasNext():
            k1 = k.next()
            if need_comma:
                q = (("null" if q is None else q) + ",")
            q = (("null" if q is None else q) + "?")
            need_comma = True
        q = (("null" if q is None else q) + ")")
        if (not db.begin(q,lst,[])):
            print("Problem with database insert")
            return False
        db.end()
        return True

    def attach(self,db,tag,resource_name):
        tag_present = False
        tag_correct = False
        result = list()
        q = "PRAGMA database_list"
        if (not db.begin(q,None,["seq", "name", "file"])):
            return False
        while db.read():
            name = db.get(1)
            if (name == tag):
                tag_present = True
                file = db.get(2)
                if (file == resource_name):
                    tag_correct = True
        db.end()
        if tag_present:
            if tag_correct:
                return True
            if (not db.begin((("DETACH `" + ("null" if tag is None else tag)) + "`"),None,[])):
                print(str(("Failed to detach " + ("null" if tag is None else tag))))
                return False
            db.end()
        if (not db.begin((("ATTACH ? AS `" + ("null" if tag is None else tag)) + "`"),[resource_name],[])):
            print(str(((("Failed to attach " + ("null" if resource_name is None else resource_name)) + " as ") + ("null" if tag is None else tag))))
            return False
        db.end()
        return True

    def columnListSql(self,x):
        return ",".join([python_Boot.toString1(x1,'') for x1 in x])

    def fetchSchema(self,db,name):
        tname = db.getQuotedTableName(name)
        query = ("select sql from sqlite_master where name = " + ("null" if tname is None else tname))
        if (not db.begin(query,None,["sql"])):
            print(str(("Cannot find schema for table " + ("null" if tname is None else tname))))
            return None
        sql = ""
        if db.read():
            sql = db.get(0)
        db.end()
        return sql

    def splitSchema(self,db,name,sql):
        preamble = ""
        parts = list()
        double_quote = False
        single_quote = False
        token = ""
        nesting = 0
        _g = 0
        _g1 = len(sql)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            ch = ("" if (((i < 0) or ((i >= len(sql))))) else sql[i])
            if (double_quote or single_quote):
                if double_quote:
                    if (ch == "\""):
                        double_quote = False
                if single_quote:
                    if (ch == "'"):
                        single_quote = False
                token = (("null" if token is None else token) + ("null" if ch is None else ch))
                continue
            brk = False
            if (ch == "("):
                nesting = (nesting + 1)
                if (nesting == 1):
                    brk = True
            elif (ch == ")"):
                nesting = (nesting - 1)
                if (nesting == 0):
                    brk = True
            if (ch == ","):
                brk = True
                tmp = (nesting == 1)
            if brk:
                if ((("" if ((0 >= len(token))) else token[0])) == " "):
                    token = HxString.substr(token,1,len(token))
                if (preamble == ""):
                    preamble = token
                else:
                    parts.append(token)
                token = ""
            else:
                token = (("null" if token is None else token) + ("null" if ch is None else ch))
        cols = db.getColumns(name)
        name2part = haxe_ds_StringMap()
        name2col = haxe_ds_StringMap()
        _g = 0
        _g1 = len(cols)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            col = (cols[i] if i >= 0 and i < len(cols) else None)
            name2part.h[col.name] = (parts[i] if i >= 0 and i < len(parts) else None)
            name2col.h[col.name] = (cols[i] if i >= 0 and i < len(cols) else None)
        return _hx_AnonObject({'preamble': preamble, 'parts': parts, 'name2part': name2part, 'columns': cols, 'name2column': name2col})

    def _hx_exec(self,db,query):
        if (not db.begin(query)):
            print("database problem")
            return False
        db.end()
        return True

    def alterColumns(self,db,name,columns):
        def _hx_local_0(x):
            if (((x is None) or ((x == ""))) or ((x == "null"))):
                return False
            return True
        notBlank = _hx_local_0
        sql = self.fetchSchema(db,name)
        schema = self.splitSchema(db,name,sql)
        parts = schema.parts
        nparts = list()
        new_column_list = list()
        ins_column_list = list()
        sel_column_list = list()
        meta = schema.columns
        _g = 0
        _g1 = len(columns)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            c = (columns[i] if i >= 0 and i < len(columns) else None)
            if (c.name is not None):
                if (c.prevName is not None):
                    x = c.prevName
                    sel_column_list.append(x)
                    x1 = c.name
                    ins_column_list.append(x1)
                orig_type = ""
                orig_primary = False
                if (c.name in schema.name2column.h):
                    m = schema.name2column.h.get(c.name,None)
                    orig_type = m.type_value
                    orig_primary = m.primary
                next_type = orig_type
                next_primary = orig_primary
                if (c.props is not None):
                    _g2 = 0
                    _g3 = c.props
                    while (_g2 < len(_g3)):
                        p = (_g3[_g2] if _g2 >= 0 and _g2 < len(_g3) else None)
                        _g2 = (_g2 + 1)
                        if (p.name == "type"):
                            next_type = p.val
                        if (p.name == "key"):
                            next_primary = (("" + Std.string(p.val)) == "primary")
                part = ("" + HxOverrides.stringOrNull(c.name))
                if notBlank(next_type):
                    part = (("null" if part is None else part) + HxOverrides.stringOrNull(((" " + ("null" if next_type is None else next_type)))))
                if next_primary:
                    part = (("null" if part is None else part) + " PRIMARY KEY")
                nparts.append(part)
                x2 = c.name
                new_column_list.append(x2)
        if (not self._hx_exec(db,"BEGIN TRANSACTION")):
            return False
        c1 = self.columnListSql(ins_column_list)
        tname = db.getQuotedTableName(name)
        if (not self._hx_exec(db,(("CREATE TEMPORARY TABLE __coopy_backup(" + ("null" if c1 is None else c1)) + ")"))):
            return False
        if (not self._hx_exec(db,((((("INSERT INTO __coopy_backup (" + ("null" if c1 is None else c1)) + ") SELECT ") + ("null" if c1 is None else c1)) + " FROM ") + ("null" if tname is None else tname)))):
            return False
        if (not self._hx_exec(db,("DROP TABLE " + ("null" if tname is None else tname)))):
            return False
        if (not self._hx_exec(db,(((HxOverrides.stringOrNull(schema.preamble) + "(") + HxOverrides.stringOrNull(", ".join([python_Boot.toString1(x1,'') for x1 in nparts]))) + ")"))):
            return False
        if (not self._hx_exec(db,(((((("INSERT INTO " + ("null" if tname is None else tname)) + " (") + ("null" if c1 is None else c1)) + ") SELECT ") + ("null" if c1 is None else c1)) + " FROM __coopy_backup"))):
            return False
        if (not self._hx_exec(db,"DROP TABLE __coopy_backup")):
            return False
        if (not self._hx_exec(db,"COMMIT")):
            return False
        return True

SqliteHelper._hx_class = SqliteHelper


class Std:
    _hx_class_name = "Std"
    __slots__ = ()
    _hx_statics = ["isOfType", "string", "parseInt", "shortenPossibleNumber", "parseFloat"]

    @staticmethod
    def isOfType(v,t):
        if ((v is None) and ((t is None))):
            return False
        if (t is None):
            return False
        if ((type(t) == type) and (t == Dynamic)):
            return (v is not None)
        isBool = isinstance(v,bool)
        if (((type(t) == type) and (t == Bool)) and isBool):
            return True
        if ((((not isBool) and (not ((type(t) == type) and (t == Bool)))) and ((type(t) == type) and (t == Int))) and isinstance(v,int)):
            return True
        vIsFloat = isinstance(v,float)
        tmp = None
        tmp1 = None
        if (((not isBool) and vIsFloat) and ((type(t) == type) and (t == Int))):
            f = v
            tmp1 = (((f != Math.POSITIVE_INFINITY) and ((f != Math.NEGATIVE_INFINITY))) and (not python_lib_Math.isnan(f)))
        else:
            tmp1 = False
        if tmp1:
            tmp1 = None
            try:
                tmp1 = int(v)
            except BaseException as _g:
                None
                tmp1 = None
            tmp = (v == tmp1)
        else:
            tmp = False
        if ((tmp and ((v <= 2147483647))) and ((v >= -2147483648))):
            return True
        if (((not isBool) and ((type(t) == type) and (t == Float))) and isinstance(v,(float, int))):
            return True
        if ((type(t) == type) and (t == str)):
            return isinstance(v,str)
        isEnumType = ((type(t) == type) and (t == Enum))
        if ((isEnumType and python_lib_Inspect.isclass(v)) and hasattr(v,"_hx_constructs")):
            return True
        if isEnumType:
            return False
        isClassType = ((type(t) == type) and (t == Class))
        if ((((isClassType and (not isinstance(v,Enum))) and python_lib_Inspect.isclass(v)) and hasattr(v,"_hx_class_name")) and (not hasattr(v,"_hx_constructs"))):
            return True
        if isClassType:
            return False
        tmp = None
        try:
            tmp = isinstance(v,t)
        except BaseException as _g:
            None
            tmp = False
        if tmp:
            return True
        if python_lib_Inspect.isclass(t):
            cls = t
            loop = None
            def _hx_local_1(intf):
                f = (intf._hx_interfaces if (hasattr(intf,"_hx_interfaces")) else [])
                if (f is not None):
                    _g = 0
                    while (_g < len(f)):
                        i = (f[_g] if _g >= 0 and _g < len(f) else None)
                        _g = (_g + 1)
                        if (i == cls):
                            return True
                        else:
                            l = loop(i)
                            if l:
                                return True
                    return False
                else:
                    return False
            loop = _hx_local_1
            currentClass = v.__class__
            result = False
            while (currentClass is not None):
                if loop(currentClass):
                    result = True
                    break
                currentClass = python_Boot.getSuperClass(currentClass)
            return result
        else:
            return False

    @staticmethod
    def string(s):
        return python_Boot.toString1(s,"")

    @staticmethod
    def parseInt(x):
        if (x is None):
            return None
        try:
            return int(x)
        except BaseException as _g:
            None
            base = 10
            _hx_len = len(x)
            foundCount = 0
            sign = 0
            firstDigitIndex = 0
            lastDigitIndex = -1
            previous = 0
            _g = 0
            _g1 = _hx_len
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                c = (-1 if ((i >= len(x))) else ord(x[i]))
                if (((c > 8) and ((c < 14))) or ((c == 32))):
                    if (foundCount > 0):
                        return None
                    continue
                else:
                    c1 = c
                    if (c1 == 43):
                        if (foundCount == 0):
                            sign = 1
                        elif (not (((48 <= c) and ((c <= 57))))):
                            if (not (((base == 16) and ((((97 <= c) and ((c <= 122))) or (((65 <= c) and ((c <= 90))))))))):
                                break
                    elif (c1 == 45):
                        if (foundCount == 0):
                            sign = -1
                        elif (not (((48 <= c) and ((c <= 57))))):
                            if (not (((base == 16) and ((((97 <= c) and ((c <= 122))) or (((65 <= c) and ((c <= 90))))))))):
                                break
                    elif (c1 == 48):
                        if (not (((foundCount == 0) or (((foundCount == 1) and ((sign != 0))))))):
                            if (not (((48 <= c) and ((c <= 57))))):
                                if (not (((base == 16) and ((((97 <= c) and ((c <= 122))) or (((65 <= c) and ((c <= 90))))))))):
                                    break
                    elif ((c1 == 120) or ((c1 == 88))):
                        if ((previous == 48) and ((((foundCount == 1) and ((sign == 0))) or (((foundCount == 2) and ((sign != 0))))))):
                            base = 16
                        elif (not (((48 <= c) and ((c <= 57))))):
                            if (not (((base == 16) and ((((97 <= c) and ((c <= 122))) or (((65 <= c) and ((c <= 90))))))))):
                                break
                    elif (not (((48 <= c) and ((c <= 57))))):
                        if (not (((base == 16) and ((((97 <= c) and ((c <= 122))) or (((65 <= c) and ((c <= 90))))))))):
                            break
                if (((foundCount == 0) and ((sign == 0))) or (((foundCount == 1) and ((sign != 0))))):
                    firstDigitIndex = i
                foundCount = (foundCount + 1)
                lastDigitIndex = i
                previous = c
            if (firstDigitIndex <= lastDigitIndex):
                digits = HxString.substring(x,firstDigitIndex,(lastDigitIndex + 1))
                try:
                    return (((-1 if ((sign == -1)) else 1)) * int(digits,base))
                except BaseException as _g:
                    return None
            return None

    @staticmethod
    def shortenPossibleNumber(x):
        r = ""
        _g = 0
        _g1 = len(x)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            c = ("" if (((i < 0) or ((i >= len(x))))) else x[i])
            _g2 = HxString.charCodeAt(c,0)
            if (_g2 is None):
                break
            else:
                _g3 = _g2
                if (((((((((((_g3 == 57) or ((_g3 == 56))) or ((_g3 == 55))) or ((_g3 == 54))) or ((_g3 == 53))) or ((_g3 == 52))) or ((_g3 == 51))) or ((_g3 == 50))) or ((_g3 == 49))) or ((_g3 == 48))) or ((_g3 == 46))):
                    r = (("null" if r is None else r) + ("null" if c is None else c))
                else:
                    break
        return r

    @staticmethod
    def parseFloat(x):
        try:
            return float(x)
        except BaseException as _g:
            None
            if (x is not None):
                r1 = Std.shortenPossibleNumber(x)
                if (r1 != x):
                    return Std.parseFloat(r1)
            return Math.NaN
Std._hx_class = Std


class Float: pass


class Int: pass


class Bool: pass


class Dynamic: pass


class StringBuf:
    _hx_class_name = "StringBuf"
    __slots__ = ("b",)
    _hx_fields = ["b"]
    _hx_methods = ["get_length"]

    def __init__(self):
        self.b = python_lib_io_StringIO()

    def get_length(self):
        pos = self.b.tell()
        self.b.seek(0,2)
        _hx_len = self.b.tell()
        self.b.seek(pos,0)
        return _hx_len

StringBuf._hx_class = StringBuf


class StringTools:
    _hx_class_name = "StringTools"
    __slots__ = ()
    _hx_statics = ["htmlEscape", "isSpace", "ltrim", "rtrim", "trim", "lpad", "replace"]

    @staticmethod
    def htmlEscape(s,quotes = None):
        buf_b = python_lib_io_StringIO()
        _g_offset = 0
        _g_s = s
        while (_g_offset < len(_g_s)):
            index = _g_offset
            _g_offset = (_g_offset + 1)
            code = ord(_g_s[index])
            code1 = code
            if (code1 == 34):
                if quotes:
                    buf_b.write("&quot;")
                else:
                    buf_b.write("".join(map(chr,[code])))
            elif (code1 == 38):
                buf_b.write("&amp;")
            elif (code1 == 39):
                if quotes:
                    buf_b.write("&#039;")
                else:
                    buf_b.write("".join(map(chr,[code])))
            elif (code1 == 60):
                buf_b.write("&lt;")
            elif (code1 == 62):
                buf_b.write("&gt;")
            else:
                buf_b.write("".join(map(chr,[code])))
        return buf_b.getvalue()

    @staticmethod
    def isSpace(s,pos):
        if (((len(s) == 0) or ((pos < 0))) or ((pos >= len(s)))):
            return False
        c = HxString.charCodeAt(s,pos)
        if (not (((c > 8) and ((c < 14))))):
            return (c == 32)
        else:
            return True

    @staticmethod
    def ltrim(s):
        l = len(s)
        r = 0
        while ((r < l) and StringTools.isSpace(s,r)):
            r = (r + 1)
        if (r > 0):
            return HxString.substr(s,r,(l - r))
        else:
            return s

    @staticmethod
    def rtrim(s):
        l = len(s)
        r = 0
        while ((r < l) and StringTools.isSpace(s,((l - r) - 1))):
            r = (r + 1)
        if (r > 0):
            return HxString.substr(s,0,(l - r))
        else:
            return s

    @staticmethod
    def trim(s):
        return StringTools.ltrim(StringTools.rtrim(s))

    @staticmethod
    def lpad(s,c,l):
        if (len(c) <= 0):
            return s
        buf = StringBuf()
        l = (l - len(s))
        while (buf.get_length() < l):
            s1 = Std.string(c)
            buf.b.write(s1)
        s1 = Std.string(s)
        buf.b.write(s1)
        return buf.b.getvalue()

    @staticmethod
    def replace(s,sub,by):
        _this = (list(s) if ((sub == "")) else s.split(sub))
        return by.join([python_Boot.toString1(x1,'') for x1 in _this])
StringTools._hx_class = StringTools


class sys_FileSystem:
    _hx_class_name = "sys.FileSystem"
    __slots__ = ()
    _hx_statics = ["exists"]

    @staticmethod
    def exists(path):
        return python_lib_os_Path.exists(path)
sys_FileSystem._hx_class = sys_FileSystem


class Sys:
    _hx_class_name = "Sys"
    __slots__ = ()
    _hx_statics = ["environ", "get_environ", "exit", "args", "getEnv", "command", "stdout", "stderr"]
    environ = None

    @staticmethod
    def get_environ():
        _g = Sys.environ
        if (_g is None):
            environ = haxe_ds_StringMap()
            env = python_lib_Os.environ
            key = python_HaxeIterator(iter(env.keys()))
            while key.hasNext():
                key1 = key.next()
                value = env.get(key1,None)
                environ.h[key1] = value
            def _hx_local_1():
                def _hx_local_0():
                    Sys.environ = environ
                    return Sys.environ
                return _hx_local_0()
            return _hx_local_1()
        else:
            env = _g
            return env

    @staticmethod
    def exit(code):
        python_lib_Sys.exit(code)

    @staticmethod
    def args():
        argv = python_lib_Sys.argv
        return argv[1:None]

    @staticmethod
    def getEnv(s):
        return Sys.get_environ().h.get(s,None)

    @staticmethod
    def command(cmd,args = None):
        if (args is None):
            return python_lib_Subprocess.call(cmd,**python__KwArgs_KwArgs_Impl_.fromT(_hx_AnonObject({'shell': True})))
        else:
            return python_lib_Subprocess.call(([cmd] + args))

    @staticmethod
    def stdout():
        return python_io_IoTools.createFileOutputFromText(python_lib_Sys.stdout)

    @staticmethod
    def stderr():
        return python_io_IoTools.createFileOutputFromText(python_lib_Sys.stderr)
Sys._hx_class = Sys


class TableComparisonState:
    _hx_class_name = "TableComparisonState"
    __slots__ = ("p", "a", "b", "completed", "run_to_completion", "is_equal", "is_equal_known", "has_same_columns", "has_same_columns_known", "compare_flags", "p_meta", "a_meta", "b_meta", "alignment", "children", "child_order")
    _hx_fields = ["p", "a", "b", "completed", "run_to_completion", "is_equal", "is_equal_known", "has_same_columns", "has_same_columns_known", "compare_flags", "p_meta", "a_meta", "b_meta", "alignment", "children", "child_order"]
    _hx_methods = ["reset", "getMeta"]

    def __init__(self):
        self.child_order = None
        self.children = None
        self.alignment = None
        self.b_meta = None
        self.a_meta = None
        self.p_meta = None
        self.compare_flags = None
        self.has_same_columns_known = None
        self.has_same_columns = None
        self.is_equal_known = None
        self.is_equal = None
        self.run_to_completion = None
        self.completed = None
        self.b = None
        self.a = None
        self.p = None
        self.reset()

    def reset(self):
        self.completed = False
        self.run_to_completion = True
        self.is_equal_known = False
        self.is_equal = False
        self.has_same_columns = False
        self.has_same_columns_known = False
        self.compare_flags = None
        self.alignment = None
        self.children = None
        self.child_order = None

    def getMeta(self):
        if ((self.p is not None) and ((self.p_meta is None))):
            self.p_meta = self.p.getMeta()
        if ((self.a is not None) and ((self.a_meta is None))):
            self.a_meta = self.a.getMeta()
        if ((self.b is not None) and ((self.b_meta is None))):
            self.b_meta = self.b.getMeta()

TableComparisonState._hx_class = TableComparisonState


class TableDiff:
    _hx_class_name = "TableDiff"
    __slots__ = ("align", "flags", "builder", "row_map", "col_map", "has_parent", "a", "b", "p", "rp_header", "ra_header", "rb_header", "is_index_p", "is_index_a", "is_index_b", "order", "row_units", "column_units", "show_rc_numbers", "row_moves", "col_moves", "active_row", "active_column", "allow_insert", "allow_delete", "allow_update", "allow_column", "v", "sep", "conflict_sep", "schema", "have_schema", "top_line_done", "have_addition", "act", "publish", "diff_found", "schema_diff_found", "preserve_columns", "row_deletes", "row_inserts", "row_updates", "row_reorders", "col_deletes", "col_inserts", "col_updates", "col_renames", "col_reorders", "column_units_updated", "nested", "nesting_present")
    _hx_fields = ["align", "flags", "builder", "row_map", "col_map", "has_parent", "a", "b", "p", "rp_header", "ra_header", "rb_header", "is_index_p", "is_index_a", "is_index_b", "order", "row_units", "column_units", "show_rc_numbers", "row_moves", "col_moves", "active_row", "active_column", "allow_insert", "allow_delete", "allow_update", "allow_column", "v", "sep", "conflict_sep", "schema", "have_schema", "top_line_done", "have_addition", "act", "publish", "diff_found", "schema_diff_found", "preserve_columns", "row_deletes", "row_inserts", "row_updates", "row_reorders", "col_deletes", "col_inserts", "col_updates", "col_renames", "col_reorders", "column_units_updated", "nested", "nesting_present"]
    _hx_methods = ["setCellBuilder", "getSeparator", "isReordered", "spreadContext", "setIgnore", "countActive", "reset", "setupTables", "scanActivity", "setupColumns", "setupMoves", "scanSchema", "checkRcNumbers", "addRcNumbers", "elideColumns", "addSchema", "addHeader", "checkMeta", "getMetaTable", "addMeta", "refineActivity", "normalizeString", "isEqual", "checkNesting", "scanRow", "hilite", "hiliteSingle", "hiliteWithNesting", "hasDifference", "hasSchemaDifference", "isNested", "getComparisonState", "getSummary"]

    def __init__(self,align,flags):
        self.nesting_present = None
        self.nested = None
        self.column_units_updated = None
        self.col_reorders = None
        self.col_renames = None
        self.col_updates = None
        self.col_inserts = None
        self.col_deletes = None
        self.row_reorders = None
        self.row_updates = None
        self.row_inserts = None
        self.row_deletes = None
        self.schema_diff_found = None
        self.diff_found = None
        self.publish = None
        self.act = None
        self.have_addition = None
        self.top_line_done = None
        self.have_schema = None
        self.schema = None
        self.conflict_sep = None
        self.sep = None
        self.v = None
        self.allow_column = None
        self.allow_update = None
        self.allow_delete = None
        self.allow_insert = None
        self.active_column = None
        self.active_row = None
        self.col_moves = None
        self.row_moves = None
        self.show_rc_numbers = None
        self.column_units = None
        self.row_units = None
        self.order = None
        self.is_index_b = None
        self.is_index_a = None
        self.is_index_p = None
        self.rb_header = None
        self.ra_header = None
        self.rp_header = None
        self.p = None
        self.b = None
        self.a = None
        self.has_parent = None
        self.col_map = None
        self.row_map = None
        self.align = align
        self.flags = flags
        self.builder = None
        self.preserve_columns = False

    def setCellBuilder(self,builder):
        self.builder = builder

    def getSeparator(self,t,t2,root):
        sep = root
        w = t.get_width()
        h = t.get_height()
        view = t.getCellView()
        _g = 0
        _g1 = h
        while (_g < _g1):
            y = _g
            _g = (_g + 1)
            _g2 = 0
            _g3 = w
            while (_g2 < _g3):
                x = _g2
                _g2 = (_g2 + 1)
                txt = view.toString(t.getCell(x,y))
                if (txt is None):
                    continue
                while True:
                    startIndex = None
                    if (not ((((txt.find(sep) if ((startIndex is None)) else HxString.indexOfImpl(txt,sep,startIndex))) >= 0))):
                        break
                    sep = ("-" + ("null" if sep is None else sep))
        if (t2 is not None):
            w = t2.get_width()
            h = t2.get_height()
            _g = 0
            _g1 = h
            while (_g < _g1):
                y = _g
                _g = (_g + 1)
                _g2 = 0
                _g3 = w
                while (_g2 < _g3):
                    x = _g2
                    _g2 = (_g2 + 1)
                    txt = view.toString(t2.getCell(x,y))
                    if (txt is None):
                        continue
                    while True:
                        startIndex = None
                        if (not ((((txt.find(sep) if ((startIndex is None)) else HxString.indexOfImpl(txt,sep,startIndex))) >= 0))):
                            break
                        sep = ("-" + ("null" if sep is None else sep))
        return sep

    def isReordered(self,m,ct):
        reordered = False
        l = -1
        r = -1
        _g = 0
        _g1 = ct
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            unit = m.h.get(i,None)
            if (unit is None):
                continue
            if (unit.l >= 0):
                if (unit.l < l):
                    reordered = True
                    break
                l = unit.l
            if (unit.r >= 0):
                if (unit.r < r):
                    reordered = True
                    break
                r = unit.r
        return reordered

    def spreadContext(self,units,_hx_del,active):
        if ((_hx_del > 0) and ((active is not None))):
            mark = (-_hx_del - 1)
            skips = 0
            _g = 0
            _g1 = len(units)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                if ((active[i] if i >= 0 and i < len(active) else None) == -3):
                    skips = (skips + 1)
                    continue
                if (((active[i] if i >= 0 and i < len(active) else None) == 0) or (((active[i] if i >= 0 and i < len(active) else None) == 3))):
                    if ((i - mark) <= ((_hx_del + skips))):
                        python_internal_ArrayImpl._set(active, i, 2)
                    elif ((i - mark) == (((_hx_del + 1) + skips))):
                        python_internal_ArrayImpl._set(active, i, 3)
                elif ((active[i] if i >= 0 and i < len(active) else None) == 1):
                    mark = i
                    skips = 0
            mark = ((len(units) + _hx_del) + 1)
            skips = 0
            _g = 0
            _g1 = len(units)
            while (_g < _g1):
                j = _g
                _g = (_g + 1)
                i = ((len(units) - 1) - j)
                if ((active[i] if i >= 0 and i < len(active) else None) == -3):
                    skips = (skips + 1)
                    continue
                if (((active[i] if i >= 0 and i < len(active) else None) == 0) or (((active[i] if i >= 0 and i < len(active) else None) == 3))):
                    if ((mark - i) <= ((_hx_del + skips))):
                        python_internal_ArrayImpl._set(active, i, 2)
                    elif ((mark - i) == (((_hx_del + 1) + skips))):
                        python_internal_ArrayImpl._set(active, i, 3)
                elif ((active[i] if i >= 0 and i < len(active) else None) == 1):
                    mark = i
                    skips = 0

    def setIgnore(self,ignore,idx_ignore,tab,r_header):
        v = tab.getCellView()
        if (tab.get_height() >= r_header):
            _g = 0
            _g1 = tab.get_width()
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                name = v.toString(tab.getCell(i,r_header))
                if (not (name in ignore.h)):
                    continue
                idx_ignore.set(i,True)

    def countActive(self,active):
        ct = 0
        showed_dummy = False
        _g = 0
        _g1 = len(active)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            publish = ((active[i] if i >= 0 and i < len(active) else None) > 0)
            dummy = ((active[i] if i >= 0 and i < len(active) else None) == 3)
            if (dummy and showed_dummy):
                continue
            if (not publish):
                continue
            showed_dummy = dummy
            ct = (ct + 1)
        return ct

    def reset(self):
        self.has_parent = False
        def _hx_local_1():
            def _hx_local_0():
                self.rb_header = 0
                return self.rb_header
            self.ra_header = _hx_local_0()
            return self.ra_header
        self.rp_header = _hx_local_1()
        self.is_index_p = haxe_ds_IntMap()
        self.is_index_a = haxe_ds_IntMap()
        self.is_index_b = haxe_ds_IntMap()
        self.row_map = haxe_ds_IntMap()
        self.col_map = haxe_ds_IntMap()
        self.show_rc_numbers = False
        self.row_moves = None
        self.col_moves = None
        def _hx_local_4():
            def _hx_local_3():
                def _hx_local_2():
                    self.allow_column = True
                    return self.allow_column
                self.allow_update = _hx_local_2()
                return self.allow_update
            self.allow_delete = _hx_local_3()
            return self.allow_delete
        self.allow_insert = _hx_local_4()
        self.sep = ""
        self.conflict_sep = ""
        self.top_line_done = False
        self.diff_found = False
        self.schema_diff_found = False
        self.row_deletes = 0
        self.row_inserts = 0
        self.row_updates = 0
        self.row_reorders = 0
        self.col_deletes = 0
        self.col_inserts = 0
        self.col_updates = 0
        self.col_renames = 0
        self.col_reorders = 0
        self.column_units_updated = haxe_ds_IntMap()

    def setupTables(self):
        self.order = self.align.toOrder()
        self.row_units = self.order.getList()
        self.has_parent = (self.align.reference is not None)
        if self.has_parent:
            self.p = self.align.getSource()
            self.a = self.align.reference.getTarget()
            self.b = self.align.getTarget()
            self.rp_header = self.align.reference.meta.getSourceHeader()
            self.ra_header = self.align.reference.meta.getTargetHeader()
            self.rb_header = self.align.meta.getTargetHeader()
            if (self.align.getIndexColumns() is not None):
                _g = 0
                _g1 = self.align.getIndexColumns()
                while (_g < len(_g1)):
                    p2b = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
                    _g = (_g + 1)
                    if (p2b.l >= 0):
                        self.is_index_p.set(p2b.l,True)
                    if (p2b.r >= 0):
                        self.is_index_b.set(p2b.r,True)
            if (self.align.reference.getIndexColumns() is not None):
                _g = 0
                _g1 = self.align.reference.getIndexColumns()
                while (_g < len(_g1)):
                    p2a = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
                    _g = (_g + 1)
                    if (p2a.l >= 0):
                        self.is_index_p.set(p2a.l,True)
                    if (p2a.r >= 0):
                        self.is_index_a.set(p2a.r,True)
        else:
            self.a = self.align.getSource()
            self.b = self.align.getTarget()
            self.p = self.a
            self.ra_header = self.align.meta.getSourceHeader()
            self.rp_header = self.ra_header
            self.rb_header = self.align.meta.getTargetHeader()
            if (self.align.getIndexColumns() is not None):
                _g = 0
                _g1 = self.align.getIndexColumns()
                while (_g < len(_g1)):
                    a2b = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
                    _g = (_g + 1)
                    if (a2b.l >= 0):
                        self.is_index_a.set(a2b.l,True)
                    if (a2b.r >= 0):
                        self.is_index_b.set(a2b.r,True)
        self.allow_insert = self.flags.allowInsert()
        self.allow_delete = self.flags.allowDelete()
        self.allow_update = self.flags.allowUpdate()
        self.allow_column = self.flags.allowColumn()
        common = self.a
        if (common is None):
            common = self.b
        if (common is None):
            common = self.p
        self.v = common.getCellView()
        self.builder.setView(self.v)
        self.nested = False
        meta = common.getMeta()
        if (meta is not None):
            self.nested = meta.isNested()
        self.nesting_present = False

    def scanActivity(self):
        self.active_row = list()
        self.active_column = None
        if (not self.flags.show_unchanged):
            _g = 0
            _g1 = len(self.row_units)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                python_internal_ArrayImpl._set(self.active_row, ((len(self.row_units) - 1) - i), 0)
        if (not self.flags.show_unchanged_columns):
            self.active_column = list()
            _g = 0
            _g1 = len(self.column_units)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                v = 0
                unit = (self.column_units[i] if i >= 0 and i < len(self.column_units) else None)
                if ((unit.l >= 0) and self.is_index_a.h.get(unit.l,None)):
                    v = 1
                if ((unit.r >= 0) and self.is_index_b.h.get(unit.r,None)):
                    v = 1
                if ((unit.p >= 0) and self.is_index_p.h.get(unit.p,None)):
                    v = 1
                python_internal_ArrayImpl._set(self.active_column, i, v)

    def setupColumns(self):
        column_order = self.align.meta.toOrder()
        self.column_units = column_order.getList()
        ignore = self.flags.getIgnoredColumns()
        if (ignore is not None):
            p_ignore = haxe_ds_IntMap()
            a_ignore = haxe_ds_IntMap()
            b_ignore = haxe_ds_IntMap()
            self.setIgnore(ignore,p_ignore,self.p,self.rp_header)
            self.setIgnore(ignore,a_ignore,self.a,self.ra_header)
            self.setIgnore(ignore,b_ignore,self.b,self.rb_header)
            ncolumn_units = list()
            _g = 0
            _g1 = len(self.column_units)
            while (_g < _g1):
                j = _g
                _g = (_g + 1)
                cunit = (self.column_units[j] if j >= 0 and j < len(self.column_units) else None)
                if (((cunit.p in p_ignore.h) or (cunit.l in a_ignore.h)) or (cunit.r in b_ignore.h)):
                    continue
                ncolumn_units.append(cunit)
            self.column_units = ncolumn_units

    def setupMoves(self):
        if self.flags.ordered:
            self.row_moves = haxe_ds_IntMap()
            moves = Mover.moveUnits(self.row_units)
            _g = 0
            _g1 = len(moves)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                self.row_moves.set((moves[i] if i >= 0 and i < len(moves) else None),i)
            self.col_moves = haxe_ds_IntMap()
            moves = Mover.moveUnits(self.column_units)
            _g = 0
            _g1 = len(moves)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                self.col_moves.set((moves[i] if i >= 0 and i < len(moves) else None),i)

    def scanSchema(self):
        self.schema = list()
        self.have_schema = False
        _g = 0
        _g1 = len(self.column_units)
        while (_g < _g1):
            j = _g
            _g = (_g + 1)
            cunit = (self.column_units[j] if j >= 0 and j < len(self.column_units) else None)
            reordered = False
            if self.flags.ordered:
                if (j in self.col_moves.h):
                    reordered = True
                if reordered:
                    self.show_rc_numbers = True
            act = ""
            if ((cunit.r >= 0) and ((cunit.lp() == -1))):
                self.have_schema = True
                act = "+++"
                if (self.active_column is not None):
                    if self.allow_column:
                        python_internal_ArrayImpl._set(self.active_column, j, 1)
                if self.allow_column:
                    _hx_local_0 = self
                    _hx_local_1 = _hx_local_0.col_inserts
                    _hx_local_0.col_inserts = (_hx_local_1 + 1)
                    _hx_local_1
            if ((cunit.r < 0) and ((cunit.lp() >= 0))):
                self.have_schema = True
                act = "---"
                if (self.active_column is not None):
                    if self.allow_column:
                        python_internal_ArrayImpl._set(self.active_column, j, 1)
                if self.allow_column:
                    _hx_local_2 = self
                    _hx_local_3 = _hx_local_2.col_deletes
                    _hx_local_2.col_deletes = (_hx_local_3 + 1)
                    _hx_local_3
            if ((cunit.r >= 0) and ((cunit.lp() >= 0))):
                if ((self.p.get_height() >= self.rp_header) and ((self.b.get_height() >= self.rb_header))):
                    pp = self.p.getCell(cunit.lp(),self.rp_header)
                    bb = self.b.getCell(cunit.r,self.rb_header)
                    if (not self.isEqual(self.v,pp,bb)):
                        self.have_schema = True
                        act = "("
                        act = (("null" if act is None else act) + HxOverrides.stringOrNull(self.v.toString(pp)))
                        act = (("null" if act is None else act) + ")")
                        if (self.active_column is not None):
                            python_internal_ArrayImpl._set(self.active_column, j, 1)
                            _hx_local_6 = self
                            _hx_local_7 = _hx_local_6.col_renames
                            _hx_local_6.col_renames = (_hx_local_7 + 1)
                            _hx_local_7
            if reordered:
                act = (":" + ("null" if act is None else act))
                self.have_schema = True
                if (self.active_column is not None):
                    self.active_column = None
                _hx_local_8 = self
                _hx_local_9 = _hx_local_8.col_reorders
                _hx_local_8.col_reorders = (_hx_local_9 + 1)
                _hx_local_9
            _this = self.schema
            _this.append(act)

    def checkRcNumbers(self,w,h):
        if (not self.show_rc_numbers):
            if self.flags.always_show_order:
                self.show_rc_numbers = True
            elif self.flags.ordered:
                self.show_rc_numbers = self.isReordered(self.row_map,h)
                if (not self.show_rc_numbers):
                    self.show_rc_numbers = self.isReordered(self.col_map,w)

    def addRcNumbers(self,output):
        admin_w = 1
        if (self.show_rc_numbers and (not self.flags.never_show_order)):
            admin_w = (admin_w + 1)
            target = list()
            _g = 0
            _g1 = output.get_width()
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                target.append((i + 1))
            output.insertOrDeleteColumns(target,(output.get_width() + 1))
            _g = 0
            _g1 = output.get_height()
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                unit = self.row_map.h.get(i,None)
                if (unit is None):
                    output.setCell(0,i,"")
                    continue
                output.setCell(0,i,self.builder.links(unit,True))
            target = list()
            _g = 0
            _g1 = output.get_height()
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                target.append((i + 1))
            output.insertOrDeleteRows(target,(output.get_height() + 1))
            _g = 1
            _g1 = output.get_width()
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                unit = self.col_map.h.get((i - 1),None)
                if (unit is None):
                    output.setCell(i,0,"")
                    continue
                output.setCell(i,0,self.builder.links(unit,False))
            output.setCell(0,0,self.builder.marker("@:@"))
        return admin_w

    def elideColumns(self,output,admin_w):
        if (self.active_column is not None):
            all_active = True
            _g = 0
            _g1 = len(self.active_column)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                if ((self.active_column[i] if i >= 0 and i < len(self.active_column) else None) == 0):
                    all_active = False
                    break
            if (not all_active):
                fate = list()
                _g = 0
                _g1 = admin_w
                while (_g < _g1):
                    i = _g
                    _g = (_g + 1)
                    fate.append(i)
                at = admin_w
                ct = 0
                dots = list()
                _g = 0
                _g1 = len(self.active_column)
                while (_g < _g1):
                    i = _g
                    _g = (_g + 1)
                    off = ((self.active_column[i] if i >= 0 and i < len(self.active_column) else None) == 0)
                    if off:
                        ct = (ct + 1)
                    else:
                        ct = 0
                    if (off and ((ct > 1))):
                        fate.append(-1)
                    else:
                        if off:
                            dots.append(at)
                        fate.append(at)
                        at = (at + 1)
                output.insertOrDeleteColumns(fate,at)
                _g = 0
                while (_g < len(dots)):
                    d = (dots[_g] if _g >= 0 and _g < len(dots) else None)
                    _g = (_g + 1)
                    _g1 = 0
                    _g2 = output.get_height()
                    while (_g1 < _g2):
                        j = _g1
                        _g1 = (_g1 + 1)
                        output.setCell(d,j,self.builder.marker("..."))

    def addSchema(self,output):
        if self.have_schema:
            at = output.get_height()
            output.resize((len(self.column_units) + 1),(at + 1))
            output.setCell(0,at,self.builder.marker("!"))
            _g = 0
            _g1 = len(self.column_units)
            while (_g < _g1):
                j = _g
                _g = (_g + 1)
                output.setCell((j + 1),at,self.v.toDatum((self.schema[j] if j >= 0 and j < len(self.schema) else None)))
            self.schema_diff_found = True

    def addHeader(self,output):
        if self.flags.always_show_header:
            at = output.get_height()
            output.resize((len(self.column_units) + 1),(at + 1))
            output.setCell(0,at,self.builder.marker("@@"))
            _g = 0
            _g1 = len(self.column_units)
            while (_g < _g1):
                j = _g
                _g = (_g + 1)
                cunit = (self.column_units[j] if j >= 0 and j < len(self.column_units) else None)
                if (cunit.r >= 0):
                    if (self.b.get_height() != 0):
                        output.setCell((j + 1),at,self.b.getCell(cunit.r,self.rb_header))
                elif (cunit.l >= 0):
                    if (self.a.get_height() != 0):
                        output.setCell((j + 1),at,self.a.getCell(cunit.l,self.ra_header))
                elif (cunit.lp() >= 0):
                    if (self.p.get_height() != 0):
                        output.setCell((j + 1),at,self.p.getCell(cunit.lp(),self.rp_header))
                self.col_map.set((j + 1),cunit)
            self.top_line_done = True

    def checkMeta(self,t,meta):
        if (meta is None):
            return False
        if (t is None):
            if (meta.get_width() == 1):
                return (meta.get_height() == 1)
            else:
                return False
        if (meta.get_width() != ((t.get_width() + 1))):
            return False
        if ((meta.get_width() == 0) or ((meta.get_height() == 0))):
            return False
        return True

    def getMetaTable(self,t):
        if (t is None):
            result = SimpleTable(1,1)
            result.setCell(0,0,"@")
            return result
        meta = t.getMeta()
        if (meta is None):
            return None
        return meta.asTable()

    def addMeta(self,output):
        if (((self.a is None) and ((self.b is None))) and ((self.p is None))):
            return False
        if (not self.flags.show_meta):
            return False
        a_meta = self.getMetaTable(self.a)
        b_meta = self.getMetaTable(self.b)
        p_meta = self.getMetaTable(self.p)
        if (not self.checkMeta(self.a,a_meta)):
            return False
        if (not self.checkMeta(self.b,b_meta)):
            return False
        if (not self.checkMeta(self.p,p_meta)):
            return False
        meta_diff = SimpleTable(0,0)
        meta_flags = CompareFlags()
        meta_flags.addPrimaryKey("@@")
        meta_flags.addPrimaryKey("@")
        meta_flags.unchanged_column_context = 65536
        meta_flags.unchanged_context = 0
        meta_align = Coopy.compareTables3((None if ((a_meta == p_meta)) else p_meta),a_meta,b_meta,meta_flags).align()
        td = TableDiff(meta_align,meta_flags)
        td.preserve_columns = True
        td.hilite(meta_diff)
        if (td.hasDifference() or td.hasSchemaDifference()):
            h = output.get_height()
            dh = meta_diff.get_height()
            offset = (2 if (td.hasSchemaDifference()) else 1)
            output.resize(output.get_width(),((h + dh) - offset))
            v = meta_diff.getCellView()
            _g = offset
            _g1 = dh
            while (_g < _g1):
                y = _g
                _g = (_g + 1)
                _g2 = 1
                _g3 = meta_diff.get_width()
                while (_g2 < _g3):
                    x = _g2
                    _g2 = (_g2 + 1)
                    c = meta_diff.getCell(x,y)
                    if (x == 1):
                        c = ((("@" + HxOverrides.stringOrNull(v.toString(c))) + "@") + HxOverrides.stringOrNull(v.toString(meta_diff.getCell(0,y))))
                    output.setCell((x - 1),((h + y) - offset),c)
            if (self.active_column is not None):
                if (len(td.active_column) == meta_diff.get_width()):
                    _g = 1
                    _g1 = meta_diff.get_width()
                    while (_g < _g1):
                        i = _g
                        _g = (_g + 1)
                        if ((td.active_column[i] if i >= 0 and i < len(td.active_column) else None) >= 0):
                            python_internal_ArrayImpl._set(self.active_column, (i - 1), 1)
        return False

    def refineActivity(self):
        self.spreadContext(self.row_units,self.flags.unchanged_context,self.active_row)
        self.spreadContext(self.column_units,self.flags.unchanged_column_context,self.active_column)
        if (self.active_column is not None):
            _g = 0
            _g1 = len(self.column_units)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                if ((self.active_column[i] if i >= 0 and i < len(self.active_column) else None) == 3):
                    python_internal_ArrayImpl._set(self.active_column, i, 0)

    def normalizeString(self,v,_hx_str):
        if (_hx_str is None):
            return _hx_str
        if (not ((self.flags.ignore_whitespace or self.flags.ignore_case))):
            return _hx_str
        txt = v.toString(_hx_str)
        if self.flags.ignore_whitespace:
            txt = StringTools.trim(txt)
        if self.flags.ignore_case:
            txt = txt.lower()
        return txt

    def isEqual(self,v,aa,bb):
        if (self.flags.ignore_epsilon > 0):
            fa = Std.parseFloat(aa)
            if (not python_lib_Math.isnan(fa)):
                fb = Std.parseFloat(bb)
                if (not python_lib_Math.isnan(fb)):
                    if (Reflect.field(Math,"fabs")((fa - fb)) < self.flags.ignore_epsilon):
                        return True
        if (self.flags.ignore_whitespace or self.flags.ignore_case):
            return (self.normalizeString(v,aa) == self.normalizeString(v,bb))
        return v.equals(aa,bb)

    def checkNesting(self,v,have_ll,ll,have_rr,rr,have_pp,pp,x,y):
        all_tables = True
        if have_ll:
            all_tables = (all_tables and v.isTable(ll))
        if have_rr:
            all_tables = (all_tables and v.isTable(rr))
        if have_pp:
            all_tables = (all_tables and v.isTable(pp))
        if (not all_tables):
            return [ll, rr, pp]
        ll_table = None
        rr_table = None
        pp_table = None
        if have_ll:
            ll_table = v.getTable(ll)
        if have_rr:
            rr_table = v.getTable(rr)
        if have_pp:
            pp_table = v.getTable(pp)
        compare = False
        comp = TableComparisonState()
        comp.a = ll_table
        comp.b = rr_table
        comp.p = pp_table
        comp.compare_flags = self.flags
        comp.getMeta()
        key = None
        if (comp.a_meta is not None):
            key = comp.a_meta.getName()
        if ((key is None) and ((comp.b_meta is not None))):
            key = comp.b_meta.getName()
        if (key is None):
            key = ((Std.string(x) + "_") + Std.string(y))
        if (self.align.comp is not None):
            if (self.align.comp.children is None):
                self.align.comp.children = haxe_ds_StringMap()
                self.align.comp.child_order = list()
                compare = True
            else:
                compare = (not (key in self.align.comp.children.h))
        if compare:
            self.nesting_present = True
            self.align.comp.children.h[key] = comp
            _this = self.align.comp.child_order
            _this.append(key)
            ct = CompareTable(comp)
            ct.align()
        else:
            comp = self.align.comp.children.h.get(key,None)
        ll_out = None
        rr_out = None
        pp_out = None
        if ((comp.alignment.isMarkedAsIdentical() or ((have_ll and (not have_rr)))) or ((have_rr and (not have_ll)))):
            ll_out = (("[" + ("null" if key is None else key)) + "]")
            rr_out = ll_out
            pp_out = ll_out
        else:
            if (ll is not None):
                ll_out = (("[a." + ("null" if key is None else key)) + "]")
            if (rr is not None):
                rr_out = (("[b." + ("null" if key is None else key)) + "]")
            if (pp is not None):
                pp_out = (("[p." + ("null" if key is None else key)) + "]")
        return [ll_out, rr_out, pp_out]

    def scanRow(self,unit,output,at,i,out):
        row_update = False
        _g = 0
        _g1 = len(self.column_units)
        while (_g < _g1):
            j = _g
            _g = (_g + 1)
            cunit = (self.column_units[j] if j >= 0 and j < len(self.column_units) else None)
            pp = None
            ll = None
            rr = None
            dd = None
            dd_to = None
            have_dd_to = False
            dd_to_alt = None
            have_dd_to_alt = False
            have_pp = False
            have_ll = False
            have_rr = False
            if ((cunit.p >= 0) and ((unit.p >= 0))):
                pp = self.p.getCell(cunit.p,unit.p)
                have_pp = True
            if ((cunit.l >= 0) and ((unit.l >= 0))):
                ll = self.a.getCell(cunit.l,unit.l)
                have_ll = True
            if ((cunit.r >= 0) and ((unit.r >= 0))):
                rr = self.b.getCell(cunit.r,unit.r)
                have_rr = True
                if (((cunit.p if have_pp else cunit.l)) < 0):
                    if (rr is not None):
                        if (self.v.toString(rr) != ""):
                            if self.allow_column:
                                self.have_addition = True
            if self.nested:
                ndiff = self.checkNesting(self.v,have_ll,ll,have_rr,rr,have_pp,pp,i,j)
                ll = (ndiff[0] if 0 < len(ndiff) else None)
                rr = (ndiff[1] if 1 < len(ndiff) else None)
                pp = (ndiff[2] if 2 < len(ndiff) else None)
            if have_pp:
                if (not have_rr):
                    dd = pp
                elif self.isEqual(self.v,pp,rr):
                    dd = ll
                else:
                    dd = pp
                    dd_to = rr
                    have_dd_to = True
                    if (not self.isEqual(self.v,pp,ll)):
                        if (not self.isEqual(self.v,pp,rr)):
                            dd_to_alt = ll
                            have_dd_to_alt = True
            elif have_ll:
                if (not have_rr):
                    dd = ll
                elif self.isEqual(self.v,ll,rr):
                    dd = ll
                else:
                    dd = ll
                    dd_to = rr
                    have_dd_to = True
            else:
                dd = rr
            cell = dd
            if (have_dd_to and ((((dd is not None) and self.allow_update) or self.allow_column))):
                if (not row_update):
                    if (out == 0):
                        _hx_local_0 = self
                        _hx_local_1 = _hx_local_0.row_updates
                        _hx_local_0.row_updates = (_hx_local_1 + 1)
                        _hx_local_1
                    row_update = True
                if (self.active_column is not None):
                    python_internal_ArrayImpl._set(self.active_column, j, 1)
                if (self.sep == ""):
                    if self.builder.needSeparator():
                        self.sep = self.getSeparator(self.a,self.b,"->")
                        self.builder.setSeparator(self.sep)
                    else:
                        self.sep = "->"
                is_conflict = False
                if have_dd_to_alt:
                    if (not self.isEqual(self.v,dd_to,dd_to_alt)):
                        is_conflict = True
                if (not is_conflict):
                    cell = self.builder.update(dd,dd_to)
                    if (len(self.sep) > len(self.act)):
                        self.act = self.sep
                else:
                    if (self.conflict_sep == ""):
                        if self.builder.needSeparator():
                            self.conflict_sep = (HxOverrides.stringOrNull(self.getSeparator(self.p,self.a,"!")) + HxOverrides.stringOrNull(self.sep))
                            self.builder.setConflictSeparator(self.conflict_sep)
                        else:
                            self.conflict_sep = "!->"
                    cell = self.builder.conflict(dd,dd_to_alt,dd_to)
                    self.act = self.conflict_sep
                if (not (j in self.column_units_updated.h)):
                    self.column_units_updated.set(j,True)
                    _hx_local_2 = self
                    _hx_local_3 = _hx_local_2.col_updates
                    _hx_local_2.col_updates = (_hx_local_3 + 1)
                    _hx_local_3
            if ((self.act == "") and self.have_addition):
                self.act = "+"
            if (self.act == "+++"):
                if have_rr:
                    if (self.active_column is not None):
                        python_internal_ArrayImpl._set(self.active_column, j, 1)
            if self.publish:
                if ((self.active_column is None) or (((self.active_column[j] if j >= 0 and j < len(self.active_column) else None) > 0))):
                    output.setCell((j + 1),at,cell)
        if self.publish:
            output.setCell(0,at,self.builder.marker(self.act))
            self.row_map.set(at,unit)
        if (self.act != ""):
            self.diff_found = True
            if (not self.publish):
                if (self.active_row is not None):
                    python_internal_ArrayImpl._set(self.active_row, i, 1)

    def hilite(self,output):
        output = Coopy.tablify(output)
        return self.hiliteSingle(output)

    def hiliteSingle(self,output):
        if (not output.isResizable()):
            return False
        if (self.builder is None):
            if self.flags.allow_nested_cells:
                self.builder = NestedCellBuilder()
            else:
                self.builder = FlatCellBuilder(self.flags)
        output.resize(0,0)
        output.clear()
        self.reset()
        self.setupTables()
        self.setupColumns()
        self.setupMoves()
        self.scanActivity()
        self.scanSchema()
        self.addSchema(output)
        self.addHeader(output)
        self.addMeta(output)
        outer_reps_needed = (1 if ((self.flags.show_unchanged and self.flags.show_unchanged_columns)) else 2)
        output_height = output.get_height()
        output_height_init = output.get_height()
        _g = 0
        _g1 = outer_reps_needed
        while (_g < _g1):
            out = _g
            _g = (_g + 1)
            if (out == 1):
                self.refineActivity()
                rows = (self.countActive(self.active_row) + output_height_init)
                if self.top_line_done:
                    rows = (rows - 1)
                output_height = output_height_init
                if (rows > output.get_height()):
                    output.resize((len(self.column_units) + 1),rows)
            showed_dummy = False
            l = -1
            r = -1
            _g2 = 0
            _g3 = len(self.row_units)
            while (_g2 < _g3):
                i = _g2
                _g2 = (_g2 + 1)
                unit = (self.row_units[i] if i >= 0 and i < len(self.row_units) else None)
                reordered = False
                if self.flags.ordered:
                    if (i in self.row_moves.h):
                        reordered = True
                    if reordered:
                        self.show_rc_numbers = True
                if ((unit.r < 0) and ((unit.l < 0))):
                    continue
                if (((unit.r == 0) and ((unit.lp() <= 0))) and self.top_line_done):
                    continue
                self.publish = self.flags.show_unchanged
                dummy = False
                if (out == 1):
                    value = (self.active_row[i] if i >= 0 and i < len(self.active_row) else None)
                    self.publish = ((value is not None) and ((value > 0)))
                    dummy = ((value is not None) and ((value == 3)))
                    if (dummy and showed_dummy):
                        continue
                    if (not self.publish):
                        continue
                if (not dummy):
                    showed_dummy = False
                at = output_height
                if self.publish:
                    output_height = (output_height + 1)
                    if (output.get_height() < output_height):
                        output.resize((len(self.column_units) + 1),output_height)
                if dummy:
                    _g4 = 0
                    _g5 = (len(self.column_units) + 1)
                    while (_g4 < _g5):
                        j = _g4
                        _g4 = (_g4 + 1)
                        output.setCell(j,at,self.v.toDatum("..."))
                    showed_dummy = True
                    continue
                self.have_addition = False
                skip = False
                self.act = ""
                if reordered:
                    self.act = ":"
                    if (out == 0):
                        _hx_local_2 = self
                        _hx_local_3 = _hx_local_2.row_reorders
                        _hx_local_2.row_reorders = (_hx_local_3 + 1)
                        _hx_local_3
                if (((unit.p < 0) and ((unit.l < 0))) and ((unit.r >= 0))):
                    if (not self.allow_insert):
                        skip = True
                    self.act = "+++"
                    if ((out == 0) and (not skip)):
                        _hx_local_4 = self
                        _hx_local_5 = _hx_local_4.row_inserts
                        _hx_local_4.row_inserts = (_hx_local_5 + 1)
                        _hx_local_5
                if (((((unit.p >= 0) or (not self.has_parent))) and ((unit.l >= 0))) and ((unit.r < 0))):
                    if (not self.allow_delete):
                        skip = True
                    self.act = "---"
                    if ((out == 0) and (not skip)):
                        _hx_local_6 = self
                        _hx_local_7 = _hx_local_6.row_deletes
                        _hx_local_6.row_deletes = (_hx_local_7 + 1)
                        _hx_local_7
                if skip:
                    if (not self.publish):
                        if (self.active_row is not None):
                            python_internal_ArrayImpl._set(self.active_row, i, -3)
                    continue
                self.scanRow(unit,output,at,i,out)
        self.checkRcNumbers(output.get_width(),output.get_height())
        admin_w = self.addRcNumbers(output)
        if (not self.preserve_columns):
            self.elideColumns(output,admin_w)
        return True

    def hiliteWithNesting(self,output):
        base = output.add("base")
        result = self.hiliteSingle(base)
        if (not result):
            return False
        if (self.align.comp is None):
            return True
        order = self.align.comp.child_order
        if (order is None):
            return True
        output.alignment = self.align
        _g = 0
        while (_g < len(order)):
            name = (order[_g] if _g >= 0 and _g < len(order) else None)
            _g = (_g + 1)
            child = self.align.comp.children.h.get(name,None)
            alignment = child.alignment
            if alignment.isMarkedAsIdentical():
                self.align.comp.children.h[name] = None
                continue
            td = TableDiff(alignment,self.flags)
            child_output = output.add(name)
            result = (result and td.hiliteSingle(child_output))
        return result

    def hasDifference(self):
        return self.diff_found

    def hasSchemaDifference(self):
        return self.schema_diff_found

    def isNested(self):
        return self.nesting_present

    def getComparisonState(self):
        if (self.align is None):
            return None
        return self.align.comp

    def getSummary(self):
        ds = DiffSummary()
        ds.row_deletes = self.row_deletes
        ds.row_inserts = self.row_inserts
        ds.row_updates = self.row_updates
        ds.row_reorders = self.row_reorders
        ds.col_deletes = self.col_deletes
        ds.col_inserts = self.col_inserts
        ds.col_updates = self.col_updates
        ds.col_renames = self.col_renames
        ds.col_reorders = self.col_reorders
        ds.row_count_initial_with_header = self.align.getSource().get_height()
        ds.row_count_final_with_header = self.align.getTarget().get_height()
        ds.row_count_initial = ((self.align.getSource().get_height() - self.align.getSourceHeader()) - 1)
        ds.row_count_final = ((self.align.getTarget().get_height() - self.align.getTargetHeader()) - 1)
        ds.col_count_initial = self.align.getSource().get_width()
        ds.col_count_final = self.align.getTarget().get_width()
        ds.different = (((((((((self.row_deletes + self.row_inserts) + self.row_updates) + self.row_reorders) + self.col_deletes) + self.col_inserts) + self.col_updates) + self.col_renames) + self.col_reorders) > 0)
        return ds

TableDiff._hx_class = TableDiff


class TableIO:
    _hx_class_name = "TableIO"
    __slots__ = ()
    _hx_methods = ["valid", "getContent", "saveContent", "args", "writeStdout", "writeStderr", "command", "hasAsync", "exists", "isTtyKnown", "isTty", "openSqliteDatabase", "sendToBrowser"]

    def __init__(self):
        pass

    def valid(self):
        return True

    def getContent(self,name):
        return sys_io_File.getContent(name)

    def saveContent(self,name,txt):
        sys_io_File.saveContent(name,txt)
        return True

    def args(self):
        return Sys.args()

    def writeStdout(self,txt):
        get_stdout().write(txt.encode("utf-8", "strict"))

    def writeStderr(self,txt):
        Sys.stderr().writeString(txt)

    def command(self,cmd,args):
        try:
            return Sys.command(cmd,args)
        except BaseException as _g:
            None
            return 1

    def hasAsync(self):
        return False

    def exists(self,path):
        return sys_FileSystem.exists(path)

    def isTtyKnown(self):
        return True

    def isTty(self):
        if __import__('sys').stdout.isatty():
            return True
        if (Sys.getEnv("GIT_PAGER_IN_USE") == "true"):
            return True
        return False

    def openSqliteDatabase(self,path):
        return SqliteDatabase(path,path)

    def sendToBrowser(self,html):
        f = __import__('tempfile').NamedTemporaryFile('wb', delete=False, suffix='.html')
        f.write(html.encode('utf-8', 'strict'))
        f.close()
        __import__('webbrowser').open('file://' + f.name)

TableIO._hx_class = TableIO


class TableModifier:
    _hx_class_name = "TableModifier"
    __slots__ = ("t",)
    _hx_fields = ["t"]
    _hx_methods = ["removeColumn"]

    def __init__(self,t):
        self.t = t

    def removeColumn(self,at):
        fate = []
        _g = 0
        _g1 = self.t.get_width()
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            if (i < at):
                fate.append(i)
            elif (i > at):
                fate.append((i - 1))
            else:
                fate.append(-1)
        return self.t.insertOrDeleteColumns(fate,(self.t.get_width() - 1))

TableModifier._hx_class = TableModifier


class TableStream:
    _hx_class_name = "TableStream"
    __slots__ = ("t", "at", "h", "src", "columns", "row")
    _hx_fields = ["t", "at", "h", "src", "columns", "row"]
    _hx_methods = ["fetchColumns", "fetchRow", "fetch", "getCell", "width"]
    _hx_interfaces = [RowStream]

    def __init__(self,t):
        self.row = None
        self.columns = None
        self.t = t
        self.at = -1
        self.h = t.get_height()
        self.src = None
        if (self.h < 0):
            meta = t.getMeta()
            if (meta is None):
                raise haxe_Exception.thrown("Cannot get meta information for table")
            self.src = meta.getRowStream()
            if (self.src is None):
                raise haxe_Exception.thrown("Cannot iterate table")

    def fetchColumns(self):
        if (self.columns is not None):
            return self.columns
        if (self.src is not None):
            self.columns = self.src.fetchColumns()
            return self.columns
        self.columns = list()
        _g = 0
        _g1 = self.t.get_width()
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            _this = self.columns
            x = self.t.getCell(i,0)
            _this.append(x)
        return self.columns

    def fetchRow(self):
        if (self.src is not None):
            return self.src.fetchRow()
        if (self.at >= self.h):
            return None
        row = haxe_ds_StringMap()
        _g = 0
        _g1 = len(self.columns)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            k = (self.columns[i] if i >= 0 and i < len(self.columns) else None)
            v = self.t.getCell(i,self.at)
            row.h[k] = v
        return row

    def fetch(self):
        if (self.at == -1):
            _hx_local_0 = self
            _hx_local_1 = _hx_local_0.at
            _hx_local_0.at = (_hx_local_1 + 1)
            _hx_local_1
            if (self.src is not None):
                self.fetchColumns()
            return True
        if (self.src is not None):
            self.at = 1
            self.row = self.fetchRow()
            return (self.row is not None)
        _hx_local_2 = self
        _hx_local_3 = _hx_local_2.at
        _hx_local_2.at = (_hx_local_3 + 1)
        _hx_local_3
        return (self.at < self.h)

    def getCell(self,x):
        if (self.at == 0):
            return (self.columns[x] if x >= 0 and x < len(self.columns) else None)
        if (self.row is not None):
            return self.row.h.get((self.columns[x] if x >= 0 and x < len(self.columns) else None),None)
        return self.t.getCell(x,self.at)

    def width(self):
        self.fetchColumns()
        return len(self.columns)

TableStream._hx_class = TableStream


class Tables:
    _hx_class_name = "Tables"
    __slots__ = ("template", "tables", "table_order", "alignment")
    _hx_fields = ["template", "tables", "table_order", "alignment"]
    _hx_methods = ["add", "getOrder", "get", "one", "hasInsDel"]

    def __init__(self,template):
        self.alignment = None
        self.template = template
        self.tables = haxe_ds_StringMap()
        self.table_order = list()

    def add(self,name):
        t = self.template.clone()
        self.tables.h[name] = t
        _this = self.table_order
        _this.append(name)
        return t

    def getOrder(self):
        return self.table_order

    def get(self,name):
        return self.tables.h.get(name,None)

    def one(self):
        return self.tables.h.get((self.table_order[0] if 0 < len(self.table_order) else None),None)

    def hasInsDel(self):
        if (self.alignment is None):
            return False
        if self.alignment.has_addition:
            return True
        if self.alignment.has_removal:
            return True
        return False

Tables._hx_class = Tables


class TerminalDiffRender:
    _hx_class_name = "TerminalDiffRender"
    __slots__ = ("codes", "t", "csv", "v", "align_columns", "wide_columns", "use_glyphs", "flags", "delim", "diff")
    _hx_fields = ["codes", "t", "csv", "v", "align_columns", "wide_columns", "use_glyphs", "flags", "delim", "diff"]
    _hx_methods = ["alignColumns", "render", "getText", "pickSizes"]

    def __init__(self,flags = None,delim = None,diff = None):
        if (diff is None):
            diff = True
        self.v = None
        self.csv = None
        self.t = None
        self.codes = None
        self.align_columns = True
        self.wide_columns = False
        self.use_glyphs = True
        self.flags = flags
        if (flags is not None):
            if (flags.padding_strategy == "dense"):
                self.align_columns = False
            if (flags.padding_strategy == "sparse"):
                self.wide_columns = True
            self.use_glyphs = flags.use_glyphs
        self.delim = (delim if ((delim is not None)) else ",")
        self.diff = diff

    def alignColumns(self,enable):
        self.align_columns = enable

    def render(self,t):
        self.csv = Csv()
        result = ""
        w = t.get_width()
        h = t.get_height()
        self.t = t
        self.v = t.getCellView()
        self.codes = haxe_ds_StringMap()
        self.codes.h["header"] = "\x1B[0;1m"
        self.codes.h["minor"] = "\x1B[33m"
        self.codes.h["done"] = "\x1B[0m"
        self.codes.h["meta"] = "\x1B[0;1m"
        self.codes.h["spec"] = "\x1B[35;1m"
        self.codes.h["add"] = "\x1B[32;1m"
        self.codes.h["conflict"] = "\x1B[33;1m"
        self.codes.h["modify"] = "\x1B[34;1m"
        self.codes.h["remove"] = "\x1B[31;1m"
        sizes = None
        if self.align_columns:
            sizes = self.pickSizes(t)
        txts = list()
        _g = 0
        _g1 = h
        while (_g < _g1):
            y = _g
            _g = (_g + 1)
            target = 0
            at = 0
            _g2 = 0
            _g3 = w
            while (_g2 < _g3):
                x = _g2
                _g2 = (_g2 + 1)
                if (sizes is not None):
                    spaces = (target - at)
                    _g4 = 0
                    _g5 = spaces
                    while (_g4 < _g5):
                        i = _g4
                        _g4 = (_g4 + 1)
                        txts.append(" ")
                        at = (at + 1)
                if (x > 0):
                    x1 = self.codes.h.get("minor",None)
                    txts.append(x1)
                    x2 = self.delim
                    txts.append(x2)
                    x3 = self.codes.h.get("done",None)
                    txts.append(x3)
                x4 = self.getText(x,y,True)
                txts.append(x4)
                if (sizes is not None):
                    bit = self.getText(x,y,False)
                    at = (at + len(bit))
                    target = (target + (sizes[x] if x >= 0 and x < len(sizes) else None))
            txts.append("\r\n")
        self.t = None
        self.v = None
        self.csv = None
        self.codes = None
        return "".join([python_Boot.toString1(x1,'') for x1 in txts])

    def getText(self,x,y,color):
        val = self.t.getCell(x,y)
        cell = DiffRender.renderCell(self.t,self.v,x,y)
        if (color and self.diff):
            code = None
            if (cell.category is not None):
                code = self.codes.h.get(cell.category,None)
            if (cell.category_given_tr is not None):
                code_tr = self.codes.h.get(cell.category_given_tr,None)
                if (code_tr is not None):
                    code = code_tr
            if (code is not None):
                separator = (cell.pretty_separator if (self.use_glyphs) else cell.separator)
                if (cell.rvalue is not None):
                    val = ((((((HxOverrides.stringOrNull(self.codes.h.get("remove",None)) + HxOverrides.stringOrNull(cell.lvalue)) + HxOverrides.stringOrNull(self.codes.h.get("modify",None))) + ("null" if separator is None else separator)) + HxOverrides.stringOrNull(self.codes.h.get("add",None))) + HxOverrides.stringOrNull(cell.rvalue)) + HxOverrides.stringOrNull(self.codes.h.get("done",None)))
                    if (cell.pvalue is not None):
                        val = ((((HxOverrides.stringOrNull(self.codes.h.get("conflict",None)) + HxOverrides.stringOrNull(cell.pvalue)) + HxOverrides.stringOrNull(self.codes.h.get("modify",None))) + ("null" if separator is None else separator)) + Std.string(val))
                else:
                    val = (cell.pretty_value if (self.use_glyphs) else cell.value)
                    val = ((("null" if code is None else code) + Std.string(val)) + HxOverrides.stringOrNull(self.codes.h.get("done",None)))
        elif (color and (not self.diff)):
            if (y == 0):
                val = ((HxOverrides.stringOrNull(self.codes.h.get("header",None)) + Std.string(val)) + HxOverrides.stringOrNull(self.codes.h.get("done",None)))
        else:
            val = (cell.pretty_value if (self.use_glyphs) else cell.value)
        return self.csv.renderCell(self.v,val)

    def pickSizes(self,t):
        w = t.get_width()
        h = t.get_height()
        v = t.getCellView()
        csv = Csv()
        sizes = list()
        row = -1
        total = (w - 1)
        _g = 0
        _g1 = w
        while (_g < _g1):
            x = _g
            _g = (_g + 1)
            m = 0
            m2 = 0
            mmax = 0
            mmostmax = 0
            mmin = -1
            _g2 = 0
            _g3 = h
            while (_g2 < _g3):
                y = _g2
                _g2 = (_g2 + 1)
                txt = self.getText(x,y,False)
                if (((txt == "@@") and ((row == -1))) and self.diff):
                    row = y
                if ((row == -1) and (not self.diff)):
                    row = y
                _hx_len = len(txt)
                if (y == row):
                    mmin = _hx_len
                m = (m + _hx_len)
                m2 = (m2 + ((_hx_len * _hx_len)))
                if (_hx_len > mmax):
                    mmax = _hx_len
            mean = (m / h)
            v = ((m2 / h) - ((mean * mean)))
            stddev = (Math.NaN if ((v < 0)) else python_lib_Math.sqrt(v))
            most = None
            try:
                most = int(((mean + ((stddev * 2))) + 0.5))
            except BaseException as _g4:
                None
                most = None
            most1 = most
            _g5 = 0
            _g6 = h
            while (_g5 < _g6):
                y1 = _g5
                _g5 = (_g5 + 1)
                txt1 = self.getText(x,y1,False)
                len1 = len(txt1)
                if (len1 <= most1):
                    if (len1 > mmostmax):
                        mmostmax = len1
            full = mmax
            most1 = mmostmax
            if (mmin != -1):
                if (most1 < mmin):
                    most1 = mmin
            if self.wide_columns:
                most1 = full
            sizes.append(most1)
            total = (total + most1)
        if ((total > 130) and (not self.wide_columns)):
            return None
        return sizes

TerminalDiffRender._hx_class = TerminalDiffRender

class ValueType(Enum):
    __slots__ = ()
    _hx_class_name = "ValueType"
    _hx_constructs = ["TNull", "TInt", "TFloat", "TBool", "TObject", "TFunction", "TClass", "TEnum", "TUnknown"]

    @staticmethod
    def TClass(c):
        return ValueType("TClass", 6, (c,))

    @staticmethod
    def TEnum(e):
        return ValueType("TEnum", 7, (e,))
ValueType.TNull = ValueType("TNull", 0, ())
ValueType.TInt = ValueType("TInt", 1, ())
ValueType.TFloat = ValueType("TFloat", 2, ())
ValueType.TBool = ValueType("TBool", 3, ())
ValueType.TObject = ValueType("TObject", 4, ())
ValueType.TFunction = ValueType("TFunction", 5, ())
ValueType.TUnknown = ValueType("TUnknown", 8, ())
ValueType._hx_class = ValueType


class Type:
    _hx_class_name = "Type"
    __slots__ = ()
    _hx_statics = ["getClass", "typeof"]

    @staticmethod
    def getClass(o):
        if (o is None):
            return None
        o1 = o
        if ((o1 is not None) and ((HxOverrides.eq(o1,str) or python_lib_Inspect.isclass(o1)))):
            return None
        if isinstance(o,_hx_AnonObject):
            return None
        if hasattr(o,"_hx_class"):
            return o._hx_class
        if hasattr(o,"__class__"):
            return o.__class__
        else:
            return None

    @staticmethod
    def typeof(v):
        if (v is None):
            return ValueType.TNull
        elif isinstance(v,bool):
            return ValueType.TBool
        elif isinstance(v,int):
            return ValueType.TInt
        elif isinstance(v,float):
            return ValueType.TFloat
        elif isinstance(v,str):
            return ValueType.TClass(str)
        elif isinstance(v,list):
            return ValueType.TClass(list)
        elif (isinstance(v,_hx_AnonObject) or python_lib_Inspect.isclass(v)):
            return ValueType.TObject
        elif isinstance(v,Enum):
            return ValueType.TEnum(v.__class__)
        elif (isinstance(v,type) or hasattr(v,"_hx_class")):
            return ValueType.TClass(v.__class__)
        elif callable(v):
            return ValueType.TFunction
        else:
            return ValueType.TUnknown
Type._hx_class = Type


class Unit:
    _hx_class_name = "Unit"
    __slots__ = ("l", "r", "p")
    _hx_fields = ["l", "r", "p"]
    _hx_methods = ["lp", "toString", "fromString", "base26", "toBase26String"]
    _hx_statics = ["describe"]

    def __init__(self,l = None,r = None,p = None):
        if (l is None):
            l = -2
        if (r is None):
            r = -2
        if (p is None):
            p = -2
        self.l = l
        self.r = r
        self.p = p

    def lp(self):
        if (self.p == -2):
            return self.l
        else:
            return self.p

    def toString(self):
        if (self.p >= -1):
            return ((((HxOverrides.stringOrNull(Unit.describe(self.p)) + "|") + HxOverrides.stringOrNull(Unit.describe(self.l))) + ":") + HxOverrides.stringOrNull(Unit.describe(self.r)))
        return ((HxOverrides.stringOrNull(Unit.describe(self.l)) + ":") + HxOverrides.stringOrNull(Unit.describe(self.r)))

    def fromString(self,txt):
        txt = (("null" if txt is None else txt) + "]")
        at = 0
        _g = 0
        _g1 = len(txt)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            ch = HxString.charCodeAt(txt,i)
            if ((ch >= 48) and ((ch <= 57))):
                at = (at * 10)
                at = (at + ((ch - 48)))
            elif (ch == 45):
                at = -1
            elif (ch == 124):
                self.p = at
                at = 0
            elif (ch == 58):
                self.l = at
                at = 0
            elif (ch == 93):
                self.r = at
                return True
        return False

    def base26(self,num):
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if (num < 0):
            return "-"
        out = ""
        while True:
            index = HxOverrides.mod(num, 26)
            out = (("null" if out is None else out) + HxOverrides.stringOrNull(("" if (((index < 0) or ((index >= len(alpha))))) else alpha[index])))
            num = (Math.floor((num / 26)) - 1)
            if (not ((num >= 0))):
                break
        return out

    def toBase26String(self):
        if (self.p >= -1):
            return ((((HxOverrides.stringOrNull(self.base26(self.p)) + "|") + HxOverrides.stringOrNull(self.base26(self.l))) + ":") + HxOverrides.stringOrNull(self.base26(self.r)))
        return ((HxOverrides.stringOrNull(self.base26(self.l)) + ":") + HxOverrides.stringOrNull(self.base26(self.r)))

    @staticmethod
    def describe(i):
        if (i >= 0):
            return ("" + Std.string(i))
        else:
            return "-"

Unit._hx_class = Unit


class Viterbi:
    _hx_class_name = "Viterbi"
    __slots__ = ("K", "T", "index", "mode", "path_valid", "best_cost", "cost", "src", "path")
    _hx_fields = ["K", "T", "index", "mode", "path_valid", "best_cost", "cost", "src", "path"]
    _hx_methods = ["reset", "setSize", "assertMode", "addTransition", "endTransitions", "beginTransitions", "calculatePath", "toString", "length", "get", "getCost"]

    def __init__(self):
        self.path = None
        self.src = None
        self.cost = None
        self.best_cost = None
        self.path_valid = None
        self.mode = None
        self.index = None
        def _hx_local_0():
            self.T = 0
            return self.T
        self.K = _hx_local_0()
        self.reset()
        self.cost = SparseSheet()
        self.src = SparseSheet()
        self.path = SparseSheet()

    def reset(self):
        self.index = 0
        self.mode = 0
        self.path_valid = False
        self.best_cost = 0

    def setSize(self,states,sequence_length):
        self.K = states
        self.T = sequence_length
        self.cost.resize(self.K,self.T,0)
        self.src.resize(self.K,self.T,-1)
        self.path.resize(1,self.T,-1)

    def assertMode(self,next):
        if ((next == 0) and ((self.mode == 1))):
            _hx_local_0 = self
            _hx_local_1 = _hx_local_0.index
            _hx_local_0.index = (_hx_local_1 + 1)
            _hx_local_1
        self.mode = next

    def addTransition(self,s0,s1,c):
        resize = False
        if (s0 >= self.K):
            self.K = (s0 + 1)
            resize = True
        if (s1 >= self.K):
            self.K = (s1 + 1)
            resize = True
        if resize:
            self.cost.nonDestructiveResize(self.K,self.T,0)
            self.src.nonDestructiveResize(self.K,self.T,-1)
            self.path.nonDestructiveResize(1,self.T,-1)
        self.path_valid = False
        self.assertMode(1)
        if (self.index >= self.T):
            self.T = (self.index + 1)
            self.cost.nonDestructiveResize(self.K,self.T,0)
            self.src.nonDestructiveResize(self.K,self.T,-1)
            self.path.nonDestructiveResize(1,self.T,-1)
        sourced = False
        if (self.index > 0):
            c = (c + self.cost.get(s0,(self.index - 1)))
            sourced = (self.src.get(s0,(self.index - 1)) != -1)
        else:
            sourced = True
        if sourced:
            if ((c < self.cost.get(s1,self.index)) or ((self.src.get(s1,self.index) == -1))):
                self.cost.set(s1,self.index,c)
                self.src.set(s1,self.index,s0)

    def endTransitions(self):
        self.path_valid = False
        self.assertMode(0)

    def beginTransitions(self):
        self.path_valid = False
        self.assertMode(1)

    def calculatePath(self):
        if self.path_valid:
            return
        self.endTransitions()
        best = 0
        bestj = -1
        if (self.index <= 0):
            self.path_valid = True
            return
        _g = 0
        _g1 = self.K
        while (_g < _g1):
            j = _g
            _g = (_g + 1)
            if ((((self.cost.get(j,(self.index - 1)) < best) or ((bestj == -1)))) and ((self.src.get(j,(self.index - 1)) != -1))):
                best = self.cost.get(j,(self.index - 1))
                bestj = j
        self.best_cost = best
        _g = 0
        _g1 = self.index
        while (_g < _g1):
            j = _g
            _g = (_g + 1)
            i = ((self.index - 1) - j)
            self.path.set(0,i,bestj)
            if (not (((bestj != -1) and (((bestj >= 0) and ((bestj < self.K))))))):
                print("Problem in Viterbi")
            bestj = self.src.get(bestj,i)
        self.path_valid = True

    def toString(self):
        self.calculatePath()
        txt = ""
        _g = 0
        _g1 = self.index
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            if (self.path.get(0,i) == -1):
                txt = (("null" if txt is None else txt) + "*")
            else:
                txt = (("null" if txt is None else txt) + Std.string(self.path.get(0,i)))
            if (self.K >= 10):
                txt = (("null" if txt is None else txt) + " ")
        txt = (("null" if txt is None else txt) + HxOverrides.stringOrNull(((" costs " + Std.string(self.getCost())))))
        return txt

    def length(self):
        if (self.index > 0):
            self.calculatePath()
        return self.index

    def get(self,i):
        self.calculatePath()
        return self.path.get(0,i)

    def getCost(self):
        self.calculatePath()
        return self.best_cost

Viterbi._hx_class = Viterbi


class haxe_IMap:
    _hx_class_name = "haxe.IMap"
    __slots__ = ()
haxe_IMap._hx_class = haxe_IMap


class haxe_Exception(Exception):
    _hx_class_name = "haxe.Exception"
    __slots__ = ("_hx___nativeStack", "_hx___skipStack", "_hx___nativeException", "_hx___previousException")
    _hx_fields = ["__nativeStack", "__skipStack", "__nativeException", "__previousException"]
    _hx_methods = ["unwrap", "toString", "get_message", "get_native"]
    _hx_statics = ["caught", "thrown"]
    _hx_interfaces = []
    _hx_super = Exception


    def __init__(self,message,previous = None,native = None):
        self._hx___previousException = None
        self._hx___nativeException = None
        self._hx___nativeStack = None
        self._hx___skipStack = 0
        super().__init__(message)
        self._hx___previousException = previous
        if ((native is not None) and Std.isOfType(native,BaseException)):
            self._hx___nativeException = native
            self._hx___nativeStack = haxe_NativeStackTrace.exceptionStack()
        else:
            self._hx___nativeException = self
            infos = python_lib_Traceback.extract_stack()
            if (len(infos) != 0):
                infos.pop()
            infos.reverse()
            self._hx___nativeStack = infos

    def unwrap(self):
        return self._hx___nativeException

    def toString(self):
        return self.get_message()

    def get_message(self):
        return str(self)

    def get_native(self):
        return self._hx___nativeException

    @staticmethod
    def caught(value):
        if Std.isOfType(value,haxe_Exception):
            return value
        elif Std.isOfType(value,BaseException):
            return haxe_Exception(str(value),None,value)
        else:
            return haxe_ValueException(value,None,value)

    @staticmethod
    def thrown(value):
        if Std.isOfType(value,haxe_Exception):
            return value.get_native()
        elif Std.isOfType(value,BaseException):
            return value
        else:
            e = haxe_ValueException(value)
            e._hx___skipStack = (e._hx___skipStack + 1)
            return e

haxe_Exception._hx_class = haxe_Exception


class haxe_NativeStackTrace:
    _hx_class_name = "haxe.NativeStackTrace"
    __slots__ = ()
    _hx_statics = ["saveStack", "exceptionStack"]

    @staticmethod
    def saveStack(exception):
        pass

    @staticmethod
    def exceptionStack():
        exc = python_lib_Sys.exc_info()
        if (exc[2] is not None):
            infos = python_lib_Traceback.extract_tb(exc[2])
            infos.reverse()
            return infos
        else:
            return []
haxe_NativeStackTrace._hx_class = haxe_NativeStackTrace


class haxe_ValueException(haxe_Exception):
    _hx_class_name = "haxe.ValueException"
    __slots__ = ("value",)
    _hx_fields = ["value"]
    _hx_methods = ["unwrap"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_Exception


    def __init__(self,value,previous = None,native = None):
        self.value = None
        super().__init__(Std.string(value),previous,native)
        self.value = value

    def unwrap(self):
        return self.value

haxe_ValueException._hx_class = haxe_ValueException


class haxe_ds_IntMap:
    _hx_class_name = "haxe.ds.IntMap"
    __slots__ = ("h",)
    _hx_fields = ["h"]
    _hx_methods = ["set", "remove", "keys", "toString"]
    _hx_interfaces = [haxe_IMap]

    def __init__(self):
        self.h = dict()

    def set(self,key,value):
        self.h[key] = value

    def remove(self,key):
        if (not (key in self.h)):
            return False
        del self.h[key]
        return True

    def keys(self):
        return python_HaxeIterator(iter(self.h.keys()))

    def toString(self):
        s_b = python_lib_io_StringIO()
        s_b.write("{")
        it = self.keys()
        i = it
        while i.hasNext():
            i1 = i.next()
            s_b.write(Std.string(i1))
            s_b.write(" => ")
            s_b.write(Std.string(Std.string(self.h.get(i1,None))))
            if it.hasNext():
                s_b.write(", ")
        s_b.write("}")
        return s_b.getvalue()

haxe_ds_IntMap._hx_class = haxe_ds_IntMap


class haxe_ds_StringMap:
    _hx_class_name = "haxe.ds.StringMap"
    __slots__ = ("h",)
    _hx_fields = ["h"]
    _hx_methods = ["keys", "iterator"]
    _hx_interfaces = [haxe_IMap]

    def __init__(self):
        self.h = dict()

    def keys(self):
        return python_HaxeIterator(iter(self.h.keys()))

    def iterator(self):
        return python_HaxeIterator(iter(self.h.values()))

haxe_ds_StringMap._hx_class = haxe_ds_StringMap


class haxe_exceptions_PosException(haxe_Exception):
    _hx_class_name = "haxe.exceptions.PosException"
    __slots__ = ("posInfos",)
    _hx_fields = ["posInfos"]
    _hx_methods = ["toString"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_Exception


    def __init__(self,message,previous = None,pos = None):
        self.posInfos = None
        super().__init__(message,previous)
        if (pos is None):
            self.posInfos = _hx_AnonObject({'fileName': "(unknown)", 'lineNumber': 0, 'className': "(unknown)", 'methodName': "(unknown)"})
        else:
            self.posInfos = pos

    def toString(self):
        return ((((((((("" + HxOverrides.stringOrNull(super().toString())) + " in ") + HxOverrides.stringOrNull(self.posInfos.className)) + ".") + HxOverrides.stringOrNull(self.posInfos.methodName)) + " at ") + HxOverrides.stringOrNull(self.posInfos.fileName)) + ":") + Std.string(self.posInfos.lineNumber))

haxe_exceptions_PosException._hx_class = haxe_exceptions_PosException


class haxe_exceptions_NotImplementedException(haxe_exceptions_PosException):
    _hx_class_name = "haxe.exceptions.NotImplementedException"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_exceptions_PosException


    def __init__(self,message = None,previous = None,pos = None):
        if (message is None):
            message = "Not implemented"
        super().__init__(message,previous,pos)
haxe_exceptions_NotImplementedException._hx_class = haxe_exceptions_NotImplementedException


class haxe_format_JsonPrinter:
    _hx_class_name = "haxe.format.JsonPrinter"
    __slots__ = ("buf", "replacer", "indent", "pretty", "nind")
    _hx_fields = ["buf", "replacer", "indent", "pretty", "nind"]
    _hx_methods = ["write", "classString", "fieldsString", "quote"]
    _hx_statics = ["print"]

    def __init__(self,replacer,space):
        self.replacer = replacer
        self.indent = space
        self.pretty = (space is not None)
        self.nind = 0
        self.buf = StringBuf()

    def write(self,k,v):
        if (self.replacer is not None):
            v = self.replacer(k,v)
        _g = Type.typeof(v)
        tmp = _g.index
        if (tmp == 0):
            self.buf.b.write("null")
        elif (tmp == 1):
            _this = self.buf
            s = Std.string(v)
            _this.b.write(s)
        elif (tmp == 2):
            f = v
            v1 = (Std.string(v) if ((((f != Math.POSITIVE_INFINITY) and ((f != Math.NEGATIVE_INFINITY))) and (not python_lib_Math.isnan(f)))) else "null")
            _this = self.buf
            s = Std.string(v1)
            _this.b.write(s)
        elif (tmp == 3):
            _this = self.buf
            s = Std.string(v)
            _this.b.write(s)
        elif (tmp == 4):
            self.fieldsString(v,python_Boot.fields(v))
        elif (tmp == 5):
            self.buf.b.write("\"<fun>\"")
        elif (tmp == 6):
            c = _g.params[0]
            if (c == str):
                self.quote(v)
            elif (c == list):
                v1 = v
                _this = self.buf
                s = "".join(map(chr,[91]))
                _this.b.write(s)
                _hx_len = len(v1)
                last = (_hx_len - 1)
                _g1 = 0
                _g2 = _hx_len
                while (_g1 < _g2):
                    i = _g1
                    _g1 = (_g1 + 1)
                    if (i > 0):
                        _this = self.buf
                        s = "".join(map(chr,[44]))
                        _this.b.write(s)
                    else:
                        _hx_local_0 = self
                        _hx_local_1 = _hx_local_0.nind
                        _hx_local_0.nind = (_hx_local_1 + 1)
                        _hx_local_1
                    if self.pretty:
                        _this1 = self.buf
                        s1 = "".join(map(chr,[10]))
                        _this1.b.write(s1)
                    if self.pretty:
                        v2 = StringTools.lpad("",self.indent,(self.nind * len(self.indent)))
                        _this2 = self.buf
                        s2 = Std.string(v2)
                        _this2.b.write(s2)
                    self.write(i,(v1[i] if i >= 0 and i < len(v1) else None))
                    if (i == last):
                        _hx_local_2 = self
                        _hx_local_3 = _hx_local_2.nind
                        _hx_local_2.nind = (_hx_local_3 - 1)
                        _hx_local_3
                        if self.pretty:
                            _this3 = self.buf
                            s3 = "".join(map(chr,[10]))
                            _this3.b.write(s3)
                        if self.pretty:
                            v3 = StringTools.lpad("",self.indent,(self.nind * len(self.indent)))
                            _this4 = self.buf
                            s4 = Std.string(v3)
                            _this4.b.write(s4)
                _this = self.buf
                s = "".join(map(chr,[93]))
                _this.b.write(s)
            elif (c == haxe_ds_StringMap):
                v1 = v
                o = _hx_AnonObject({})
                k = v1.keys()
                while k.hasNext():
                    k1 = k.next()
                    value = v1.h.get(k1,None)
                    setattr(o,(("_hx_" + k1) if ((k1 in python_Boot.keywords)) else (("_hx_" + k1) if (((((len(k1) > 2) and ((ord(k1[0]) == 95))) and ((ord(k1[1]) == 95))) and ((ord(k1[(len(k1) - 1)]) != 95)))) else k1)),value)
                v1 = o
                self.fieldsString(v1,python_Boot.fields(v1))
            elif (c == Date):
                v1 = v
                self.quote(v1.toString())
            else:
                self.classString(v)
        elif (tmp == 7):
            _g1 = _g.params[0]
            i = v.index
            _this = self.buf
            s = Std.string(i)
            _this.b.write(s)
        elif (tmp == 8):
            self.buf.b.write("\"???\"")
        else:
            pass

    def classString(self,v):
        self.fieldsString(v,python_Boot.getInstanceFields(Type.getClass(v)))

    def fieldsString(self,v,fields):
        _this = self.buf
        s = "".join(map(chr,[123]))
        _this.b.write(s)
        _hx_len = len(fields)
        last = (_hx_len - 1)
        first = True
        _g = 0
        _g1 = _hx_len
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            f = (fields[i] if i >= 0 and i < len(fields) else None)
            value = Reflect.field(v,f)
            if Reflect.isFunction(value):
                continue
            if first:
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.nind
                _hx_local_0.nind = (_hx_local_1 + 1)
                _hx_local_1
                first = False
            else:
                _this = self.buf
                s = "".join(map(chr,[44]))
                _this.b.write(s)
            if self.pretty:
                _this1 = self.buf
                s1 = "".join(map(chr,[10]))
                _this1.b.write(s1)
            if self.pretty:
                v1 = StringTools.lpad("",self.indent,(self.nind * len(self.indent)))
                _this2 = self.buf
                s2 = Std.string(v1)
                _this2.b.write(s2)
            self.quote(f)
            _this3 = self.buf
            s3 = "".join(map(chr,[58]))
            _this3.b.write(s3)
            if self.pretty:
                _this4 = self.buf
                s4 = "".join(map(chr,[32]))
                _this4.b.write(s4)
            self.write(f,value)
            if (i == last):
                _hx_local_2 = self
                _hx_local_3 = _hx_local_2.nind
                _hx_local_2.nind = (_hx_local_3 - 1)
                _hx_local_3
                if self.pretty:
                    _this5 = self.buf
                    s5 = "".join(map(chr,[10]))
                    _this5.b.write(s5)
                if self.pretty:
                    v2 = StringTools.lpad("",self.indent,(self.nind * len(self.indent)))
                    _this6 = self.buf
                    s6 = Std.string(v2)
                    _this6.b.write(s6)
        _this = self.buf
        s = "".join(map(chr,[125]))
        _this.b.write(s)

    def quote(self,s):
        _this = self.buf
        s1 = "".join(map(chr,[34]))
        _this.b.write(s1)
        i = 0
        length = len(s)
        while (i < length):
            index = i
            i = (i + 1)
            c = ord(s[index])
            c1 = c
            if (c1 == 8):
                self.buf.b.write("\\b")
            elif (c1 == 9):
                self.buf.b.write("\\t")
            elif (c1 == 10):
                self.buf.b.write("\\n")
            elif (c1 == 12):
                self.buf.b.write("\\f")
            elif (c1 == 13):
                self.buf.b.write("\\r")
            elif (c1 == 34):
                self.buf.b.write("\\\"")
            elif (c1 == 92):
                self.buf.b.write("\\\\")
            else:
                _this = self.buf
                s1 = "".join(map(chr,[c]))
                _this.b.write(s1)
        _this = self.buf
        s = "".join(map(chr,[34]))
        _this.b.write(s)

    @staticmethod
    def print(o,replacer = None,space = None):
        printer = haxe_format_JsonPrinter(replacer,space)
        printer.write("",o)
        return printer.buf.b.getvalue()

haxe_format_JsonPrinter._hx_class = haxe_format_JsonPrinter


class haxe_io_Bytes:
    _hx_class_name = "haxe.io.Bytes"
    __slots__ = ("length", "b")
    _hx_fields = ["length", "b"]
    _hx_statics = ["ofString"]

    def __init__(self,length,b):
        self.length = length
        self.b = b

    @staticmethod
    def ofString(s,encoding = None):
        b = bytearray(s,"UTF-8")
        return haxe_io_Bytes(len(b),b)

haxe_io_Bytes._hx_class = haxe_io_Bytes

class haxe_io_Encoding(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.io.Encoding"
    _hx_constructs = ["UTF8", "RawNative"]
haxe_io_Encoding.UTF8 = haxe_io_Encoding("UTF8", 0, ())
haxe_io_Encoding.RawNative = haxe_io_Encoding("RawNative", 1, ())
haxe_io_Encoding._hx_class = haxe_io_Encoding

class haxe_io_Error(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.io.Error"
    _hx_constructs = ["Blocked", "Overflow", "OutsideBounds", "Custom"]

    @staticmethod
    def Custom(e):
        return haxe_io_Error("Custom", 3, (e,))
haxe_io_Error.Blocked = haxe_io_Error("Blocked", 0, ())
haxe_io_Error.Overflow = haxe_io_Error("Overflow", 1, ())
haxe_io_Error.OutsideBounds = haxe_io_Error("OutsideBounds", 2, ())
haxe_io_Error._hx_class = haxe_io_Error


class haxe_io_Output:
    _hx_class_name = "haxe.io.Output"
    __slots__ = ("bigEndian",)
    _hx_fields = ["bigEndian"]
    _hx_methods = ["writeByte", "writeBytes", "set_bigEndian", "writeFullBytes", "writeString"]

    def writeByte(self,c):
        raise haxe_exceptions_NotImplementedException(None,None,_hx_AnonObject({'fileName': "haxe/io/Output.hx", 'lineNumber': 47, 'className': "haxe.io.Output", 'methodName': "writeByte"}))

    def writeBytes(self,s,pos,_hx_len):
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > s.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        b = s.b
        k = _hx_len
        while (k > 0):
            self.writeByte(b[pos])
            pos = (pos + 1)
            k = (k - 1)
        return _hx_len

    def set_bigEndian(self,b):
        self.bigEndian = b
        return b

    def writeFullBytes(self,s,pos,_hx_len):
        while (_hx_len > 0):
            k = self.writeBytes(s,pos,_hx_len)
            pos = (pos + k)
            _hx_len = (_hx_len - k)

    def writeString(self,s,encoding = None):
        b = haxe_io_Bytes.ofString(s,encoding)
        self.writeFullBytes(b,0,b.length)

haxe_io_Output._hx_class = haxe_io_Output


class haxe_iterators_ArrayIterator:
    _hx_class_name = "haxe.iterators.ArrayIterator"
    __slots__ = ("array", "current")
    _hx_fields = ["array", "current"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,array):
        self.current = 0
        self.array = array

    def hasNext(self):
        return (self.current < len(self.array))

    def next(self):
        def _hx_local_3():
            def _hx_local_2():
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.current
                _hx_local_0.current = (_hx_local_1 + 1)
                return _hx_local_1
            return python_internal_ArrayImpl._get(self.array, _hx_local_2())
        return _hx_local_3()

haxe_iterators_ArrayIterator._hx_class = haxe_iterators_ArrayIterator


class haxe_iterators_ArrayKeyValueIterator:
    _hx_class_name = "haxe.iterators.ArrayKeyValueIterator"
    __slots__ = ("current", "array")
    _hx_fields = ["current", "array"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,array):
        self.current = 0
        self.array = array

    def hasNext(self):
        return (self.current < len(self.array))

    def next(self):
        def _hx_local_3():
            def _hx_local_2():
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.current
                _hx_local_0.current = (_hx_local_1 + 1)
                return _hx_local_1
            return _hx_AnonObject({'value': python_internal_ArrayImpl._get(self.array, self.current), 'key': _hx_local_2()})
        return _hx_local_3()

haxe_iterators_ArrayKeyValueIterator._hx_class = haxe_iterators_ArrayKeyValueIterator


class python_Boot:
    _hx_class_name = "python.Boot"
    __slots__ = ()
    _hx_statics = ["keywords", "toString1", "fields", "simpleField", "hasField", "field", "getInstanceFields", "getSuperClass", "getClassFields", "prefixLength", "unhandleKeywords"]

    @staticmethod
    def toString1(o,s):
        if (o is None):
            return "null"
        if isinstance(o,str):
            return o
        if (s is None):
            s = ""
        if (len(s) >= 5):
            return "<...>"
        if isinstance(o,bool):
            if o:
                return "true"
            else:
                return "false"
        if (isinstance(o,int) and (not isinstance(o,bool))):
            return str(o)
        if isinstance(o,float):
            try:
                if (o == int(o)):
                    return str(Math.floor((o + 0.5)))
                else:
                    return str(o)
            except BaseException as _g:
                None
                return str(o)
        if isinstance(o,list):
            o1 = o
            l = len(o1)
            st = "["
            s = (("null" if s is None else s) + "\t")
            _g = 0
            _g1 = l
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                prefix = ""
                if (i > 0):
                    prefix = ","
                st = (("null" if st is None else st) + HxOverrides.stringOrNull(((("null" if prefix is None else prefix) + HxOverrides.stringOrNull(python_Boot.toString1((o1[i] if i >= 0 and i < len(o1) else None),s))))))
            st = (("null" if st is None else st) + "]")
            return st
        try:
            if hasattr(o,"toString"):
                return o.toString()
        except BaseException as _g:
            None
        if hasattr(o,"__class__"):
            if isinstance(o,_hx_AnonObject):
                toStr = None
                try:
                    fields = python_Boot.fields(o)
                    _g = []
                    _g1 = 0
                    while (_g1 < len(fields)):
                        f = (fields[_g1] if _g1 >= 0 and _g1 < len(fields) else None)
                        _g1 = (_g1 + 1)
                        x = ((("" + ("null" if f is None else f)) + " : ") + HxOverrides.stringOrNull(python_Boot.toString1(python_Boot.simpleField(o,f),(("null" if s is None else s) + "\t"))))
                        _g.append(x)
                    fieldsStr = _g
                    toStr = (("{ " + HxOverrides.stringOrNull(", ".join([x1 for x1 in fieldsStr]))) + " }")
                except BaseException as _g:
                    None
                    return "{ ... }"
                if (toStr is None):
                    return "{ ... }"
                else:
                    return toStr
            if isinstance(o,Enum):
                o1 = o
                l = len(o1.params)
                hasParams = (l > 0)
                if hasParams:
                    paramsStr = ""
                    _g = 0
                    _g1 = l
                    while (_g < _g1):
                        i = _g
                        _g = (_g + 1)
                        prefix = ""
                        if (i > 0):
                            prefix = ","
                        paramsStr = (("null" if paramsStr is None else paramsStr) + HxOverrides.stringOrNull(((("null" if prefix is None else prefix) + HxOverrides.stringOrNull(python_Boot.toString1(o1.params[i],s))))))
                    return (((HxOverrides.stringOrNull(o1.tag) + "(") + ("null" if paramsStr is None else paramsStr)) + ")")
                else:
                    return o1.tag
            if hasattr(o,"_hx_class_name"):
                if (o.__class__.__name__ != "type"):
                    fields = python_Boot.getInstanceFields(o)
                    _g = []
                    _g1 = 0
                    while (_g1 < len(fields)):
                        f = (fields[_g1] if _g1 >= 0 and _g1 < len(fields) else None)
                        _g1 = (_g1 + 1)
                        x = ((("" + ("null" if f is None else f)) + " : ") + HxOverrides.stringOrNull(python_Boot.toString1(python_Boot.simpleField(o,f),(("null" if s is None else s) + "\t"))))
                        _g.append(x)
                    fieldsStr = _g
                    toStr = (((HxOverrides.stringOrNull(o._hx_class_name) + "( ") + HxOverrides.stringOrNull(", ".join([x1 for x1 in fieldsStr]))) + " )")
                    return toStr
                else:
                    fields = python_Boot.getClassFields(o)
                    _g = []
                    _g1 = 0
                    while (_g1 < len(fields)):
                        f = (fields[_g1] if _g1 >= 0 and _g1 < len(fields) else None)
                        _g1 = (_g1 + 1)
                        x = ((("" + ("null" if f is None else f)) + " : ") + HxOverrides.stringOrNull(python_Boot.toString1(python_Boot.simpleField(o,f),(("null" if s is None else s) + "\t"))))
                        _g.append(x)
                    fieldsStr = _g
                    toStr = (((("#" + HxOverrides.stringOrNull(o._hx_class_name)) + "( ") + HxOverrides.stringOrNull(", ".join([x1 for x1 in fieldsStr]))) + " )")
                    return toStr
            if ((type(o) == type) and (o == str)):
                return "#String"
            if ((type(o) == type) and (o == list)):
                return "#Array"
            if callable(o):
                return "function"
            try:
                if hasattr(o,"__repr__"):
                    return o.__repr__()
            except BaseException as _g:
                None
            if hasattr(o,"__str__"):
                return o.__str__([])
            if hasattr(o,"__name__"):
                return o.__name__
            return "???"
        else:
            return str(o)

    @staticmethod
    def fields(o):
        a = []
        if (o is not None):
            if hasattr(o,"_hx_fields"):
                fields = o._hx_fields
                if (fields is not None):
                    return list(fields)
            if isinstance(o,_hx_AnonObject):
                d = o.__dict__
                keys = d.keys()
                handler = python_Boot.unhandleKeywords
                for k in keys:
                    if (k != '_hx_disable_getattr'):
                        a.append(handler(k))
            elif hasattr(o,"__dict__"):
                d = o.__dict__
                keys1 = d.keys()
                for k in keys1:
                    a.append(k)
        return a

    @staticmethod
    def simpleField(o,field):
        if (field is None):
            return None
        field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
        if hasattr(o,field1):
            return getattr(o,field1)
        else:
            return None

    @staticmethod
    def hasField(o,field):
        if isinstance(o,_hx_AnonObject):
            return o._hx_hasattr(field)
        return hasattr(o,(("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field)))

    @staticmethod
    def field(o,field):
        if (field is None):
            return None
        if isinstance(o,str):
            field1 = field
            _hx_local_0 = len(field1)
            if (_hx_local_0 == 10):
                if (field1 == "charCodeAt"):
                    return python_internal_MethodClosure(o,HxString.charCodeAt)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_0 == 11):
                if (field1 == "lastIndexOf"):
                    return python_internal_MethodClosure(o,HxString.lastIndexOf)
                elif (field1 == "toLowerCase"):
                    return python_internal_MethodClosure(o,HxString.toLowerCase)
                elif (field1 == "toUpperCase"):
                    return python_internal_MethodClosure(o,HxString.toUpperCase)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_0 == 9):
                if (field1 == "substring"):
                    return python_internal_MethodClosure(o,HxString.substring)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_0 == 5):
                if (field1 == "split"):
                    return python_internal_MethodClosure(o,HxString.split)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_0 == 7):
                if (field1 == "indexOf"):
                    return python_internal_MethodClosure(o,HxString.indexOf)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_0 == 8):
                if (field1 == "toString"):
                    return python_internal_MethodClosure(o,HxString.toString)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_0 == 6):
                if (field1 == "charAt"):
                    return python_internal_MethodClosure(o,HxString.charAt)
                elif (field1 == "length"):
                    return len(o)
                elif (field1 == "substr"):
                    return python_internal_MethodClosure(o,HxString.substr)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            else:
                field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                if hasattr(o,field1):
                    return getattr(o,field1)
                else:
                    return None
        elif isinstance(o,list):
            field1 = field
            _hx_local_1 = len(field1)
            if (_hx_local_1 == 11):
                if (field1 == "lastIndexOf"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.lastIndexOf)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_1 == 4):
                if (field1 == "copy"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.copy)
                elif (field1 == "join"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.join)
                elif (field1 == "push"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.push)
                elif (field1 == "sort"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.sort)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_1 == 5):
                if (field1 == "shift"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.shift)
                elif (field1 == "slice"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.slice)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_1 == 7):
                if (field1 == "indexOf"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.indexOf)
                elif (field1 == "reverse"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.reverse)
                elif (field1 == "unshift"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.unshift)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_1 == 3):
                if (field1 == "map"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.map)
                elif (field1 == "pop"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.pop)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_1 == 8):
                if (field1 == "contains"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.contains)
                elif (field1 == "iterator"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.iterator)
                elif (field1 == "toString"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.toString)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_1 == 16):
                if (field1 == "keyValueIterator"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.keyValueIterator)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_1 == 6):
                if (field1 == "concat"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.concat)
                elif (field1 == "filter"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.filter)
                elif (field1 == "insert"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.insert)
                elif (field1 == "length"):
                    return len(o)
                elif (field1 == "remove"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.remove)
                elif (field1 == "splice"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.splice)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            else:
                field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                if hasattr(o,field1):
                    return getattr(o,field1)
                else:
                    return None
        else:
            field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
            if hasattr(o,field1):
                return getattr(o,field1)
            else:
                return None

    @staticmethod
    def getInstanceFields(c):
        f = (list(c._hx_fields) if (hasattr(c,"_hx_fields")) else [])
        if hasattr(c,"_hx_methods"):
            f = (f + c._hx_methods)
        sc = python_Boot.getSuperClass(c)
        if (sc is None):
            return f
        else:
            scArr = python_Boot.getInstanceFields(sc)
            scMap = set(scArr)
            _g = 0
            while (_g < len(f)):
                f1 = (f[_g] if _g >= 0 and _g < len(f) else None)
                _g = (_g + 1)
                if (not (f1 in scMap)):
                    scArr.append(f1)
            return scArr

    @staticmethod
    def getSuperClass(c):
        if (c is None):
            return None
        try:
            if hasattr(c,"_hx_super"):
                return c._hx_super
            return None
        except BaseException as _g:
            None
        return None

    @staticmethod
    def getClassFields(c):
        if hasattr(c,"_hx_statics"):
            x = c._hx_statics
            return list(x)
        else:
            return []

    @staticmethod
    def unhandleKeywords(name):
        if (HxString.substr(name,0,python_Boot.prefixLength) == "_hx_"):
            real = HxString.substr(name,python_Boot.prefixLength,None)
            if (real in python_Boot.keywords):
                return real
        return name
python_Boot._hx_class = python_Boot


class python_HaxeIterator:
    _hx_class_name = "python.HaxeIterator"
    __slots__ = ("it", "x", "has", "checked")
    _hx_fields = ["it", "x", "has", "checked"]
    _hx_methods = ["next", "hasNext"]

    def __init__(self,it):
        self.checked = False
        self.has = False
        self.x = None
        self.it = it

    def next(self):
        if (not self.checked):
            self.hasNext()
        self.checked = False
        return self.x

    def hasNext(self):
        if (not self.checked):
            try:
                self.x = self.it.__next__()
                self.has = True
            except BaseException as _g:
                None
                if Std.isOfType(haxe_Exception.caught(_g).unwrap(),StopIteration):
                    self.has = False
                    self.x = None
                else:
                    raise _g
            self.checked = True
        return self.has

python_HaxeIterator._hx_class = python_HaxeIterator


class python__KwArgs_KwArgs_Impl_:
    _hx_class_name = "python._KwArgs.KwArgs_Impl_"
    __slots__ = ()
    _hx_statics = ["fromT"]

    @staticmethod
    def fromT(d):
        this1 = python_Lib.anonAsDict(d)
        return this1
python__KwArgs_KwArgs_Impl_._hx_class = python__KwArgs_KwArgs_Impl_


class python_Lib:
    _hx_class_name = "python.Lib"
    __slots__ = ()
    _hx_statics = ["dictToAnon", "anonToDict", "anonAsDict"]

    @staticmethod
    def dictToAnon(v):
        return _hx_AnonObject(v.copy())

    @staticmethod
    def anonToDict(o):
        if isinstance(o,_hx_AnonObject):
            return o.__dict__.copy()
        else:
            return None

    @staticmethod
    def anonAsDict(o):
        if isinstance(o,_hx_AnonObject):
            return o.__dict__
        else:
            return None
python_Lib._hx_class = python_Lib


class python_internal_ArrayImpl:
    _hx_class_name = "python.internal.ArrayImpl"
    __slots__ = ()
    _hx_statics = ["concat", "copy", "iterator", "keyValueIterator", "indexOf", "lastIndexOf", "join", "toString", "pop", "push", "unshift", "remove", "contains", "shift", "slice", "sort", "splice", "map", "filter", "insert", "reverse", "_get", "_set"]

    @staticmethod
    def concat(a1,a2):
        return (a1 + a2)

    @staticmethod
    def copy(x):
        return list(x)

    @staticmethod
    def iterator(x):
        return python_HaxeIterator(x.__iter__())

    @staticmethod
    def keyValueIterator(x):
        return haxe_iterators_ArrayKeyValueIterator(x)

    @staticmethod
    def indexOf(a,x,fromIndex = None):
        _hx_len = len(a)
        l = (0 if ((fromIndex is None)) else ((_hx_len + fromIndex) if ((fromIndex < 0)) else fromIndex))
        if (l < 0):
            l = 0
        _g = l
        _g1 = _hx_len
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            if HxOverrides.eq(a[i],x):
                return i
        return -1

    @staticmethod
    def lastIndexOf(a,x,fromIndex = None):
        _hx_len = len(a)
        l = (_hx_len if ((fromIndex is None)) else (((_hx_len + fromIndex) + 1) if ((fromIndex < 0)) else (fromIndex + 1)))
        if (l > _hx_len):
            l = _hx_len
        while True:
            l = (l - 1)
            tmp = l
            if (not ((tmp > -1))):
                break
            if HxOverrides.eq(a[l],x):
                return l
        return -1

    @staticmethod
    def join(x,sep):
        return sep.join([python_Boot.toString1(x1,'') for x1 in x])

    @staticmethod
    def toString(x):
        return (("[" + HxOverrides.stringOrNull(",".join([python_Boot.toString1(x1,'') for x1 in x]))) + "]")

    @staticmethod
    def pop(x):
        if (len(x) == 0):
            return None
        else:
            return x.pop()

    @staticmethod
    def push(x,e):
        x.append(e)
        return len(x)

    @staticmethod
    def unshift(x,e):
        x.insert(0, e)

    @staticmethod
    def remove(x,e):
        try:
            x.remove(e)
            return True
        except BaseException as _g:
            None
            return False

    @staticmethod
    def contains(x,e):
        return (e in x)

    @staticmethod
    def shift(x):
        if (len(x) == 0):
            return None
        return x.pop(0)

    @staticmethod
    def slice(x,pos,end = None):
        return x[pos:end]

    @staticmethod
    def sort(x,f):
        x.sort(key= python_lib_Functools.cmp_to_key(f))

    @staticmethod
    def splice(x,pos,_hx_len):
        if (pos < 0):
            pos = (len(x) + pos)
        if (pos < 0):
            pos = 0
        res = x[pos:(pos + _hx_len)]
        del x[pos:(pos + _hx_len)]
        return res

    @staticmethod
    def map(x,f):
        return list(map(f,x))

    @staticmethod
    def filter(x,f):
        return list(filter(f,x))

    @staticmethod
    def insert(a,pos,x):
        a.insert(pos, x)

    @staticmethod
    def reverse(a):
        a.reverse()

    @staticmethod
    def _get(x,idx):
        if ((idx > -1) and ((idx < len(x)))):
            return x[idx]
        else:
            return None

    @staticmethod
    def _set(x,idx,v):
        l = len(x)
        while (l < idx):
            x.append(None)
            l = (l + 1)
        if (l == idx):
            x.append(v)
        else:
            x[idx] = v
        return v
python_internal_ArrayImpl._hx_class = python_internal_ArrayImpl


class HxOverrides:
    _hx_class_name = "HxOverrides"
    __slots__ = ()
    _hx_statics = ["iterator", "eq", "stringOrNull", "modf", "mod", "mapKwArgs"]

    @staticmethod
    def iterator(x):
        if isinstance(x,list):
            return haxe_iterators_ArrayIterator(x)
        return x.iterator()

    @staticmethod
    def eq(a,b):
        if (isinstance(a,list) or isinstance(b,list)):
            return a is b
        return (a == b)

    @staticmethod
    def stringOrNull(s):
        if (s is None):
            return "null"
        else:
            return s

    @staticmethod
    def modf(a,b):
        if (b == 0.0):
            return float('nan')
        elif (a < 0):
            if (b < 0):
                return -(-a % (-b))
            else:
                return -(-a % b)
        elif (b < 0):
            return a % (-b)
        else:
            return a % b

    @staticmethod
    def mod(a,b):
        if (a < 0):
            if (b < 0):
                return -(-a % (-b))
            else:
                return -(-a % b)
        elif (b < 0):
            return a % (-b)
        else:
            return a % b

    @staticmethod
    def mapKwArgs(a,v):
        a1 = _hx_AnonObject(python_Lib.anonToDict(a))
        k = python_HaxeIterator(iter(v.keys()))
        while k.hasNext():
            k1 = k.next()
            val = v.get(k1)
            if a1._hx_hasattr(k1):
                x = getattr(a1,k1)
                setattr(a1,val,x)
                delattr(a1,k1)
        return a1
HxOverrides._hx_class = HxOverrides


class python_internal_MethodClosure:
    _hx_class_name = "python.internal.MethodClosure"
    __slots__ = ("obj", "func")
    _hx_fields = ["obj", "func"]
    _hx_methods = ["__call__"]

    def __init__(self,obj,func):
        self.obj = obj
        self.func = func

    def __call__(self,*args):
        return self.func(self.obj,*args)

python_internal_MethodClosure._hx_class = python_internal_MethodClosure


class HxString:
    _hx_class_name = "HxString"
    __slots__ = ()
    _hx_statics = ["split", "charCodeAt", "charAt", "lastIndexOf", "toUpperCase", "toLowerCase", "indexOf", "indexOfImpl", "toString", "substring", "substr"]

    @staticmethod
    def split(s,d):
        if (d == ""):
            return list(s)
        else:
            return s.split(d)

    @staticmethod
    def charCodeAt(s,index):
        if ((((s is None) or ((len(s) == 0))) or ((index < 0))) or ((index >= len(s)))):
            return None
        else:
            return ord(s[index])

    @staticmethod
    def charAt(s,index):
        if ((index < 0) or ((index >= len(s)))):
            return ""
        else:
            return s[index]

    @staticmethod
    def lastIndexOf(s,_hx_str,startIndex = None):
        if (startIndex is None):
            return s.rfind(_hx_str, 0, len(s))
        elif (_hx_str == ""):
            length = len(s)
            if (startIndex < 0):
                startIndex = (length + startIndex)
                if (startIndex < 0):
                    startIndex = 0
            if (startIndex > length):
                return length
            else:
                return startIndex
        else:
            i = s.rfind(_hx_str, 0, (startIndex + 1))
            startLeft = (max(0,((startIndex + 1) - len(_hx_str))) if ((i == -1)) else (i + 1))
            check = s.find(_hx_str, startLeft, len(s))
            if ((check > i) and ((check <= startIndex))):
                return check
            else:
                return i

    @staticmethod
    def toUpperCase(s):
        return s.upper()

    @staticmethod
    def toLowerCase(s):
        return s.lower()

    @staticmethod
    def indexOf(s,_hx_str,startIndex = None):
        if (startIndex is None):
            return s.find(_hx_str)
        else:
            return HxString.indexOfImpl(s,_hx_str,startIndex)

    @staticmethod
    def indexOfImpl(s,_hx_str,startIndex):
        if (_hx_str == ""):
            length = len(s)
            if (startIndex < 0):
                startIndex = (length + startIndex)
                if (startIndex < 0):
                    startIndex = 0
            if (startIndex > length):
                return length
            else:
                return startIndex
        return s.find(_hx_str, startIndex)

    @staticmethod
    def toString(s):
        return s

    @staticmethod
    def substring(s,startIndex,endIndex = None):
        if (startIndex < 0):
            startIndex = 0
        if (endIndex is None):
            return s[startIndex:]
        else:
            if (endIndex < 0):
                endIndex = 0
            if (endIndex < startIndex):
                return s[endIndex:startIndex]
            else:
                return s[startIndex:endIndex]

    @staticmethod
    def substr(s,startIndex,_hx_len = None):
        if (_hx_len is None):
            return s[startIndex:]
        else:
            if (_hx_len == 0):
                return ""
            if (startIndex < 0):
                startIndex = (len(s) + startIndex)
                if (startIndex < 0):
                    startIndex = 0
            return s[startIndex:(startIndex + _hx_len)]
HxString._hx_class = HxString


class python_io_NativeOutput(haxe_io_Output):
    _hx_class_name = "python.io.NativeOutput"
    __slots__ = ("stream",)
    _hx_fields = ["stream"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_io_Output


    def __init__(self,stream):
        self.stream = None
        self.set_bigEndian(False)
        self.stream = stream
        if (not stream.writable()):
            raise haxe_Exception.thrown("Read only stream")

python_io_NativeOutput._hx_class = python_io_NativeOutput


class python_io_IOutput:
    _hx_class_name = "python.io.IOutput"
    __slots__ = ("bigEndian",)
    _hx_fields = ["bigEndian"]
    _hx_methods = ["set_bigEndian", "writeByte", "writeBytes", "writeFullBytes", "writeString"]
python_io_IOutput._hx_class = python_io_IOutput


class python_io_IFileOutput:
    _hx_class_name = "python.io.IFileOutput"
    __slots__ = ()
    _hx_interfaces = [python_io_IOutput]
python_io_IFileOutput._hx_class = python_io_IFileOutput


class python_io_NativeTextOutput(python_io_NativeOutput):
    _hx_class_name = "python.io.NativeTextOutput"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["writeBytes", "writeByte"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = python_io_NativeOutput


    def __init__(self,stream):
        super().__init__(stream)
        if (not stream.writable()):
            raise haxe_Exception.thrown("Read only stream")

    def writeBytes(self,s,pos,_hx_len):
        return stream_write(self.stream)(s.b[pos:(pos + _hx_len)])

    def writeByte(self,c):
        self.stream.write("".join(map(chr,[c])))

python_io_NativeTextOutput._hx_class = python_io_NativeTextOutput


class python_io_FileTextOutput(python_io_NativeTextOutput):
    _hx_class_name = "python.io.FileTextOutput"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = [python_io_IFileOutput]
    _hx_super = python_io_NativeTextOutput


    def __init__(self,stream):
        super().__init__(stream)
python_io_FileTextOutput._hx_class = python_io_FileTextOutput


class python_io_IoTools:
    _hx_class_name = "python.io.IoTools"
    __slots__ = ()
    _hx_statics = ["createFileOutputFromText"]

    @staticmethod
    def createFileOutputFromText(t):
        return sys_io_FileOutput(python_io_FileTextOutput(t))
python_io_IoTools._hx_class = python_io_IoTools


class sys_io_File:
    _hx_class_name = "sys.io.File"
    __slots__ = ()
    _hx_statics = ["getContent", "saveContent"]

    @staticmethod
    def getContent(path):
        f = python_lib_Builtins.open(path,"r",-1,"utf-8",None,"")
        content = f.read(-1)
        f.close()
        return content

    @staticmethod
    def saveContent(path,content):
        f = python_lib_Builtins.open(path,"w",-1,"utf-8",None,"")
        f.write(content)
        f.close()
sys_io_File._hx_class = sys_io_File


class sys_io_FileOutput(haxe_io_Output):
    _hx_class_name = "sys.io.FileOutput"
    __slots__ = ("impl",)
    _hx_fields = ["impl"]
    _hx_methods = ["set_bigEndian", "writeByte", "writeBytes", "writeFullBytes", "writeString"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_io_Output


    def __init__(self,impl):
        self.impl = impl

    def set_bigEndian(self,b):
        return self.impl.set_bigEndian(b)

    def writeByte(self,c):
        self.impl.writeByte(c)

    def writeBytes(self,s,pos,_hx_len):
        return self.impl.writeBytes(s,pos,_hx_len)

    def writeFullBytes(self,s,pos,_hx_len):
        self.impl.writeFullBytes(s,pos,_hx_len)

    def writeString(self,s,encoding = None):
        self.impl.writeString(s)

sys_io_FileOutput._hx_class = sys_io_FileOutput

Math.NEGATIVE_INFINITY = float("-inf")
Math.POSITIVE_INFINITY = float("inf")
Math.NaN = float("nan")
Math.PI = python_lib_Math.pi

Coopy.VERSION = "1.3.47"
python_Boot.keywords = set(["and", "del", "from", "not", "with", "as", "elif", "global", "or", "yield", "assert", "else", "if", "pass", "None", "break", "except", "import", "raise", "True", "class", "exec", "in", "return", "False", "continue", "finally", "is", "try", "def", "for", "lambda", "while"])
python_Boot.prefixLength = len("_hx_")



class PythonCellView(View):
    def __init__(self):
        pass

    def toString(self,d):
        return str(d) if (d!=None) else ""

    def equals(self,d1,d2):
        return str(d1) == str(d2)

    def toDatum(self,d):
        return d

    def makeHash(self):
        return {}

    def isHash(self,d):
        return type(d) is dict

    def hashSet(self,d,k,v):
        d[k] = v
        
    def hashGet(self,d,k):
        return d[k]

    def hashExists(self,d,k):
        return k in d


class PythonTableView(Table):
    def __init__(self,data):
        self.data = data
        self.height = len(data)
        self.width = 0
        if self.height>0:
            self.width = len(data[0])

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def getCell(self,x,y):
        return self.data[y][x]

    def setCell(self,x,y,c):
        self.data[y][x] = c

    def toString(self):
        return SimpleTable.tableToString(self)

    def getCellView(self):
        return PythonCellView()
        # return SimpleView()

    def isResizable(self):
        return True

    def resize(self,w,h):
        self.width = w
        self.height = h
        for i in range(len(self.data)):
            row = self.data[i]
            if row == None:
                row = self.data[i] = []
            while len(row)<w:
                row.append(None)
        while len(self.data)<h:
            row = []
            for i in range(w):
                row.append(None)
            self.data.append(row)
        return True

    def clear(self):
        for i in range(len(self.data)):
            row = self.data[i]
            for j in range(len(row)):
                row[j] = None
        self.width = 0
        self.height = 0

    def trimBlank(self): 
        return False

    def getData(self):
        return self.data

    def insertOrDeleteRows(self,fate,hfate):
        ndata = []
        for i in range(len(fate)):
            j = fate[i];
            if j!=-1:
                if j>=len(ndata):
                    for k in range(j-len(ndata)+1):
                        ndata.append(None)
                ndata[j] = self.data[i]

        del self.data[:]
        for i in range(len(ndata)):
            self.data.append(ndata[i])
        self.resize(self.width,hfate)
        return True

    def insertOrDeleteColumns(self,fate,wfate):
        if wfate==self.width and wfate==len(fate):
            eq = True
            for i in range(wfate):
                if fate[i]!=i:
                    eq = False
                    break
            if eq:
                return True

        for i in range(self.height):
            row = self.data[i]
            nrow = []
            for j in range(self.width):
                if fate[j]==-1:
                    continue
                at = fate[j]
                if at>=len(nrow):
                    for k in range(at-len(nrow)+1):
                        nrow.append(None)
                nrow[at] = row[j]
            while len(nrow)<wfate:
                nrow.append(None)
            self.data[i] = nrow
        self.width = wfate
        return True

    def isSimilar(self,alt):
        if alt.width!=self.width:
            return False
        if alt.height!=self.height:
            return False
        for c in range(self.width):
            for r in range(self.height):
                v1 = "" + str(self.getCell(c,r))
                v2 = "" + str(alt.getCell(c,r))
                if (v1!=v2):
                    print("MISMATCH "+ v1 + " " + v2);
                    return False
        return True

    def clone(self):
        result = PythonTableView([])
        result.resize(self.get_width(), self.get_height())
        for c in range(self.width):
            for r in range(self.height):
                result.setCell(c,r,self.getCell(c,r))
        return result

    def create(self):
        return PythonTableView([])

    def getMeta(self):
        return None
for name in dir(Coopy):
    if name[0] != '_':
        vars()[name] = getattr(Coopy, name)
class SqliteDatabase(SqlDatabase):
    def __init__(self,db,fname):
        import sqlite3
        if not hasattr(db, 'cursor'):
            db = sqlite3.connect(db)
        self.db = db
        db.isolation_level = None
        self.fname = fname
        self.cursor = db.cursor()
        self.row = None
        # quoting rule for CSV is compatible with Sqlite
        self.quoter = Csv()
        self.view = SimpleView()

    # needed because pragmas do not support bound parameters
    def getQuotedColumnName(self,name):
        if hasattr(name,'decode'):
            name = unicode(name)
        return self.quoter.renderCell(self.view, name, True)

    # needed because pragmas do not support bound parameters
    def getQuotedTableName(self,name):
        return self.quoter.renderCell(self.view, name.toString(), True)

    def getColumns(self,name):
        qname = self.getQuotedTableName(name)
        info = self.cursor.execute("pragma table_info(%s)"%qname).fetchall()
        columns = []
        for row in info:
            column = SqlColumn()
            column.setName(row[1])
            column.setPrimaryKey(row[5]>0)
            column.setType(row[2],'sqlite')
            columns.append(column)
        return columns

    def begin(self,query,args=[],order=[]):
        self.cursor.execute(query,args or [])
        return True

    def beginRow(self,tab,row,order=[]):
        self.cursor.execute("SELECT * FROM " + self.getQuotedTableName(tab) + " WHERE rowid = ?",[row])
        return True

    def read(self):
        self.row = self.cursor.fetchone()
        return self.row!=None

    def get(self,index):
        v = self.row[index]
        if v is None:
            return v
        return v

    def end(self):
        pass

    def rowid(self):
        return "rowid"

    def getHelper(self):
        return SqliteHelper()
    
    def getNameForAttachment(self):
        return self.fname
def get_stdout():
	return (python_lib_Sys.stdout.buffer if hasattr(python_lib_Sys.stdout,"buffer") else python_lib_Sys.stdout)
def stream_write(s):
	return lambda txt: (s.buffer.write(txt) if hasattr(s,"buffer") else (s.write(txt) or len(txt)))
if __name__ == '__main__':
	Coopy.main()
