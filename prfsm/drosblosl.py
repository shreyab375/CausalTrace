from _log import _w as _emit, _xid

FLAXDRANR = 'flaxdranr'
BRENKRAN = 'brenkran'
PRONSTARSLAX = 'pronstarslax'
GLIMCLART = 'glimclart'
SLANKRALFLELR = 'slankralflelr'
BRENDRENK = 'brendrenk'
SPEXBLUR = 'spexblur'
BLANDREXSKAR = 'blandrexskar'
FLULBLARN = 'flulblarn'
SLALGRULR = 'slalgrulr'
TRENVAXGRENR = 'trenvaxgrenr'
BLONSLAR = 'blonslar'
GLARSTORGLON = 'glarstorglon'
CLULKROSSPIMX = 'clulkrosspimx'
BROSFLENDRIM = 'brosflendrim'
VULPRAXN = 'vulpraxn'
CLIMGLORBLOR = 'climglorblor'
FLARVOSSKAX = 'flarvosskax'
BREXCLARBLAN = 'brexclarblan'
STAXPROS = 'staxpros'
PRALSLAXR = 'pralslaxr'
VELGLAXT = 'velglaxt'
SPARSPULSKAX = 'sparspulskax'
CLOSDRENFLON = 'closdrenflon'
KRIMVORGRAR = 'krimvorgrar'
GRORVAXK = 'grorvaxk'
VAXSTEXPRELK = 'vaxstexprelk'
GLELSPURL = 'glelspurl'
SKOSPRURSTAX = 'skosprurstax'
DREXSPENSKORN = 'drexspenskorn'
GRURBRULGRORX = 'grurbrulgrorx'
SKIXGLEX = 'skixglex'
TRARSLELX = 'trarslelx'
BRENSTONR = 'brenstonr'
KRONSTANCLOSX = 'kronstanclosx'
CLIXSTORT = 'clixstort'
CLURGLELDRAN = 'clurgleldran'
VIXDRANGLALT = 'vixdranglalt'
DRAXVELSTALT = 'draxvelstalt'
SLIMBLIM = 'slimblim'
PRENVELK = 'prenvelk'
SPENGRORSKEX = 'spengrorskex'
FLIMDREL = 'flimdrel'
FLIXCLIX = 'flixclix'
SLURFLAN = 'slurflan'
SLIXSLEX = 'slixslex'
GRONSPORBRAL = 'gronsporbral'
SKENTRULX = 'skentrulx'
DRURGRELBRELR = 'drurgrelbrelr'
CLAXFLONVELT = 'claxflonvelt'
STARSPONSTAL = 'starsponstal'
BLEXTRAXSKULT = 'blextraxskult'
PRENKRANPRAR = 'prenkranprar'
BREXPRALDRELR = 'brexpraldrelr'
CLORDREN = 'clordren'
BLIMSKULDRIX = 'blimskuldrix'
STURCLURSPIMK = 'sturclurspimk'
GRARPRIMTRARX = 'grarprimtrarx'
DRELSTARBRIX = 'drelstarbrix'
VELCLAN = 'velclan'
PRANKRULSPALL = 'prankrulspall'
GLELPRURR = 'glelprurr'
BLAXPRARBREXL = 'blaxprarbrexl'
GLANTRELL = 'glantrell'
BRARVANKREX = 'brarvankrex'
SLONKRARTRORR = 'slonkrartrorr'
GLELSPALBRAL = 'glelspalbral'
BREXSKORFLANR = 'brexskorflanr'

_R = {
    SLONKRARTRORR: 0,
    GLELSPALBRAL: 1,
    BREXSKORFLANR: 2,
}

_CTX_WRITES_KEY  = 'flurslex'
_CTX_WRITE_STATE = GLARSTORGLON

class DrosbloslFSM:
    def __init__(self):
        self._state = {}

    def _flaxdranr(self, hint):
        assert self._state.get("current") == FLAXDRANR, \
            f"drosblosl.flaxdranr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flaxdranr', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'flaxdranr', _:
                self._state["current"] = BRENKRAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flaxdranr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flaxdranr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flaxdranr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brenkran(self, hint):
        assert self._state.get("current") == BRENKRAN, \
            f"drosblosl.brenkran: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brenkran', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'brenkran', 1:
                self._state["current"] = GLELSPALBRAL
                self._state["trig"]    = "hint:1"
            case 'brenkran', _:
                self._state["current"] = PRONSTARSLAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brenkran', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brenkran',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brenkran->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _pronstarslax(self, hint):
        assert self._state.get("current") == PRONSTARSLAX, \
            f"drosblosl.pronstarslax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'pronstarslax', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'pronstarslax', 0:
                self._state["current"] = SLANKRALFLELR
                self._state["trig"]    = "hint:0"
            case 'pronstarslax', _:
                self._state["current"] = GLIMCLART
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'pronstarslax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'pronstarslax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"pronstarslax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glimclart(self, hint):
        assert self._state.get("current") == GLIMCLART, \
            f"drosblosl.glimclart: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glimclart', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'glimclart', 1:
                self._state["current"] = GLELSPALBRAL
                self._state["trig"]    = "hint:1"
            case 'glimclart', _:
                self._state["current"] = SLANKRALFLELR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glimclart', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glimclart',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glimclart->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slankralflelr(self, hint):
        assert self._state.get("current") == SLANKRALFLELR, \
            f"drosblosl.slankralflelr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slankralflelr', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'slankralflelr', _:
                self._state["current"] = BRENDRENK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slankralflelr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slankralflelr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slankralflelr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brendrenk(self, hint):
        assert self._state.get("current") == BRENDRENK, \
            f"drosblosl.brendrenk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brendrenk', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'brendrenk', _:
                self._state["current"] = SPEXBLUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brendrenk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brendrenk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brendrenk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spexblur(self, hint):
        assert self._state.get("current") == SPEXBLUR, \
            f"drosblosl.spexblur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spexblur', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'spexblur', _:
                self._state["current"] = BLANDREXSKAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spexblur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spexblur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spexblur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blandrexskar(self, hint):
        assert self._state.get("current") == BLANDREXSKAR, \
            f"drosblosl.blandrexskar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blandrexskar', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'blandrexskar', _:
                self._state["current"] = FLULBLARN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blandrexskar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blandrexskar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blandrexskar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flulblarn(self, hint):
        assert self._state.get("current") == FLULBLARN, \
            f"drosblosl.flulblarn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flulblarn', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'flulblarn', 1:
                self._state["current"] = GLELSPALBRAL
                self._state["trig"]    = "hint:1"
            case 'flulblarn', _:
                self._state["current"] = SLALGRULR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flulblarn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flulblarn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flulblarn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slalgrulr(self, hint):
        assert self._state.get("current") == SLALGRULR, \
            f"drosblosl.slalgrulr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slalgrulr', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'slalgrulr', _:
                self._state["current"] = TRENVAXGRENR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slalgrulr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slalgrulr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slalgrulr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trenvaxgrenr(self, hint):
        assert self._state.get("current") == TRENVAXGRENR, \
            f"drosblosl.trenvaxgrenr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trenvaxgrenr', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'trenvaxgrenr', 0:
                self._state["current"] = GLARSTORGLON
                self._state["trig"]    = "hint:0"
            case 'trenvaxgrenr', _:
                self._state["current"] = BLONSLAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trenvaxgrenr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trenvaxgrenr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trenvaxgrenr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blonslar(self, hint):
        assert self._state.get("current") == BLONSLAR, \
            f"drosblosl.blonslar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blonslar', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'blonslar', 1:
                self._state["current"] = CLULKROSSPIMX
                self._state["trig"]    = "hint:1"
            case 'blonslar', _:
                self._state["current"] = GLARSTORGLON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blonslar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blonslar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blonslar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glarstorglon(self, hint):
        assert self._state.get("current") == GLARSTORGLON, \
            f"drosblosl.glarstorglon: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        _ctx_val_before = self._state["ctx"].get(_CTX_WRITES_KEY, 0)
        match self._state["current"], hint:
            case 'glarstorglon', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'glarstorglon', _:
                self._state["current"] = CLULKROSSPIMX
                self._state["trig"]    = "auto"
        _old = self._state["ctx"].get(_CTX_WRITES_KEY, 0)
        _inc = 2 if hint == 2 else 1
        self._state["ctx"][_CTX_WRITES_KEY] = _old + _inc
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glarstorglon', _to, _trig)
        _conds = {"hint_branch": _hint_branch,
                   "ctx_write": True,
                   "ctx_val_before": _ctx_val_before}
        _emit(self._state["cycle"], 1, __name__, 'glarstorglon',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glarstorglon->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clulkrosspimx(self, hint):
        assert self._state.get("current") == CLULKROSSPIMX, \
            f"drosblosl.clulkrosspimx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clulkrosspimx', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'clulkrosspimx', 1:
                self._state["current"] = VULPRAXN
                self._state["trig"]    = "hint:1"
            case 'clulkrosspimx', _:
                self._state["current"] = BROSFLENDRIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clulkrosspimx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clulkrosspimx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clulkrosspimx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brosflendrim(self, hint):
        assert self._state.get("current") == BROSFLENDRIM, \
            f"drosblosl.brosflendrim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brosflendrim', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'brosflendrim', 0:
                self._state["current"] = GLELSPALBRAL
                self._state["trig"]    = "hint:0"
            case 'brosflendrim', _:
                self._state["current"] = VULPRAXN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brosflendrim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brosflendrim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brosflendrim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vulpraxn(self, hint):
        assert self._state.get("current") == VULPRAXN, \
            f"drosblosl.vulpraxn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vulpraxn', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'vulpraxn', 1:
                self._state["current"] = GLELSPALBRAL
                self._state["trig"]    = "hint:1"
            case 'vulpraxn', _:
                self._state["current"] = CLIMGLORBLOR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vulpraxn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vulpraxn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vulpraxn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _climglorblor(self, hint):
        assert self._state.get("current") == CLIMGLORBLOR, \
            f"drosblosl.climglorblor: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'climglorblor', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'climglorblor', 1:
                self._state["current"] = BREXCLARBLAN
                self._state["trig"]    = "hint:1"
            case 'climglorblor', _:
                self._state["current"] = FLARVOSSKAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'climglorblor', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'climglorblor',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"climglorblor->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flarvosskax(self, hint):
        assert self._state.get("current") == FLARVOSSKAX, \
            f"drosblosl.flarvosskax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flarvosskax', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'flarvosskax', _:
                self._state["current"] = BREXCLARBLAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flarvosskax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flarvosskax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flarvosskax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brexclarblan(self, hint):
        assert self._state.get("current") == BREXCLARBLAN, \
            f"drosblosl.brexclarblan: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brexclarblan', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'brexclarblan', 1:
                self._state["current"] = GLELSPALBRAL
                self._state["trig"]    = "hint:1"
            case 'brexclarblan', _:
                self._state["current"] = STAXPROS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brexclarblan', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brexclarblan',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brexclarblan->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _staxpros(self, hint):
        assert self._state.get("current") == STAXPROS, \
            f"drosblosl.staxpros: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'staxpros', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'staxpros', _:
                self._state["current"] = PRALSLAXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'staxpros', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'staxpros',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"staxpros->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _pralslaxr(self, hint):
        assert self._state.get("current") == PRALSLAXR, \
            f"drosblosl.pralslaxr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'pralslaxr', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'pralslaxr', _:
                self._state["current"] = VELGLAXT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'pralslaxr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'pralslaxr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"pralslaxr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _velglaxt(self, hint):
        assert self._state.get("current") == VELGLAXT, \
            f"drosblosl.velglaxt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'velglaxt', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'velglaxt', 0:
                self._state["current"] = GLELSPALBRAL
                self._state["trig"]    = "hint:0"
            case 'velglaxt', _:
                self._state["current"] = SPARSPULSKAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'velglaxt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'velglaxt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"velglaxt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _sparspulskax(self, hint):
        assert self._state.get("current") == SPARSPULSKAX, \
            f"drosblosl.sparspulskax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'sparspulskax', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'sparspulskax', 1:
                self._state["current"] = KRIMVORGRAR
                self._state["trig"]    = "hint:1"
            case 'sparspulskax', _:
                self._state["current"] = CLOSDRENFLON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'sparspulskax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'sparspulskax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"sparspulskax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _closdrenflon(self, hint):
        assert self._state.get("current") == CLOSDRENFLON, \
            f"drosblosl.closdrenflon: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'closdrenflon', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'closdrenflon', _:
                self._state["current"] = KRIMVORGRAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'closdrenflon', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'closdrenflon',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"closdrenflon->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krimvorgrar(self, hint):
        assert self._state.get("current") == KRIMVORGRAR, \
            f"drosblosl.krimvorgrar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krimvorgrar', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'krimvorgrar', 1:
                self._state["current"] = VAXSTEXPRELK
                self._state["trig"]    = "hint:1"
            case 'krimvorgrar', _:
                self._state["current"] = GRORVAXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krimvorgrar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krimvorgrar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krimvorgrar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grorvaxk(self, hint):
        assert self._state.get("current") == GRORVAXK, \
            f"drosblosl.grorvaxk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grorvaxk', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'grorvaxk', 0:
                self._state["current"] = GLELSPURL
                self._state["trig"]    = "hint:0"
            case 'grorvaxk', _:
                self._state["current"] = VAXSTEXPRELK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grorvaxk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grorvaxk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grorvaxk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vaxstexprelk(self, hint):
        assert self._state.get("current") == VAXSTEXPRELK, \
            f"drosblosl.vaxstexprelk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vaxstexprelk', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'vaxstexprelk', 0:
                self._state["current"] = GLELSPALBRAL
                self._state["trig"]    = "hint:0"
            case 'vaxstexprelk', _:
                self._state["current"] = GLELSPURL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vaxstexprelk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vaxstexprelk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vaxstexprelk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glelspurl(self, hint):
        assert self._state.get("current") == GLELSPURL, \
            f"drosblosl.glelspurl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glelspurl', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'glelspurl', _:
                self._state["current"] = SKOSPRURSTAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glelspurl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glelspurl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glelspurl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skosprurstax(self, hint):
        assert self._state.get("current") == SKOSPRURSTAX, \
            f"drosblosl.skosprurstax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skosprurstax', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'skosprurstax', 0:
                self._state["current"] = GRURBRULGRORX
                self._state["trig"]    = "hint:0"
            case 'skosprurstax', _:
                self._state["current"] = DREXSPENSKORN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skosprurstax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skosprurstax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skosprurstax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drexspenskorn(self, hint):
        assert self._state.get("current") == DREXSPENSKORN, \
            f"drosblosl.drexspenskorn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drexspenskorn', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'drexspenskorn', _:
                self._state["current"] = GRURBRULGRORX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drexspenskorn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drexspenskorn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drexspenskorn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grurbrulgrorx(self, hint):
        assert self._state.get("current") == GRURBRULGRORX, \
            f"drosblosl.grurbrulgrorx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grurbrulgrorx', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'grurbrulgrorx', _:
                self._state["current"] = SKIXGLEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grurbrulgrorx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grurbrulgrorx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grurbrulgrorx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skixglex(self, hint):
        assert self._state.get("current") == SKIXGLEX, \
            f"drosblosl.skixglex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skixglex', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'skixglex', _:
                self._state["current"] = TRARSLELX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skixglex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skixglex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skixglex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trarslelx(self, hint):
        assert self._state.get("current") == TRARSLELX, \
            f"drosblosl.trarslelx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trarslelx', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'trarslelx', 1:
                self._state["current"] = GLELSPALBRAL
                self._state["trig"]    = "hint:1"
            case 'trarslelx', _:
                self._state["current"] = BRENSTONR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trarslelx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trarslelx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trarslelx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brenstonr(self, hint):
        assert self._state.get("current") == BRENSTONR, \
            f"drosblosl.brenstonr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brenstonr', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'brenstonr', 0:
                self._state["current"] = GLELSPALBRAL
                self._state["trig"]    = "hint:0"
            case 'brenstonr', _:
                self._state["current"] = KRONSTANCLOSX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brenstonr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brenstonr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brenstonr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _kronstanclosx(self, hint):
        assert self._state.get("current") == KRONSTANCLOSX, \
            f"drosblosl.kronstanclosx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'kronstanclosx', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'kronstanclosx', _:
                self._state["current"] = CLIXSTORT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'kronstanclosx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'kronstanclosx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"kronstanclosx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clixstort(self, hint):
        assert self._state.get("current") == CLIXSTORT, \
            f"drosblosl.clixstort: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clixstort', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'clixstort', 1:
                self._state["current"] = VIXDRANGLALT
                self._state["trig"]    = "hint:1"
            case 'clixstort', _:
                self._state["current"] = CLURGLELDRAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clixstort', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clixstort',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clixstort->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clurgleldran(self, hint):
        assert self._state.get("current") == CLURGLELDRAN, \
            f"drosblosl.clurgleldran: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clurgleldran', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'clurgleldran', 1:
                self._state["current"] = GLELSPALBRAL
                self._state["trig"]    = "hint:1"
            case 'clurgleldran', _:
                self._state["current"] = VIXDRANGLALT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clurgleldran', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clurgleldran',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clurgleldran->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vixdranglalt(self, hint):
        assert self._state.get("current") == VIXDRANGLALT, \
            f"drosblosl.vixdranglalt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vixdranglalt', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'vixdranglalt', _:
                self._state["current"] = DRAXVELSTALT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vixdranglalt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vixdranglalt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vixdranglalt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _draxvelstalt(self, hint):
        assert self._state.get("current") == DRAXVELSTALT, \
            f"drosblosl.draxvelstalt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'draxvelstalt', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'draxvelstalt', _:
                self._state["current"] = SLIMBLIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'draxvelstalt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'draxvelstalt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"draxvelstalt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slimblim(self, hint):
        assert self._state.get("current") == SLIMBLIM, \
            f"drosblosl.slimblim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slimblim', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'slimblim', _:
                self._state["current"] = PRENVELK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slimblim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slimblim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slimblim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prenvelk(self, hint):
        assert self._state.get("current") == PRENVELK, \
            f"drosblosl.prenvelk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prenvelk', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'prenvelk', _:
                self._state["current"] = SPENGRORSKEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prenvelk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prenvelk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prenvelk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spengrorskex(self, hint):
        assert self._state.get("current") == SPENGRORSKEX, \
            f"drosblosl.spengrorskex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spengrorskex', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'spengrorskex', _:
                self._state["current"] = FLIMDREL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spengrorskex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spengrorskex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spengrorskex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flimdrel(self, hint):
        assert self._state.get("current") == FLIMDREL, \
            f"drosblosl.flimdrel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flimdrel', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'flimdrel', 1:
                self._state["current"] = SLURFLAN
                self._state["trig"]    = "hint:1"
            case 'flimdrel', _:
                self._state["current"] = FLIXCLIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flimdrel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flimdrel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flimdrel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flixclix(self, hint):
        assert self._state.get("current") == FLIXCLIX, \
            f"drosblosl.flixclix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flixclix', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'flixclix', _:
                self._state["current"] = SLURFLAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flixclix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flixclix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flixclix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slurflan(self, hint):
        assert self._state.get("current") == SLURFLAN, \
            f"drosblosl.slurflan: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slurflan', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'slurflan', _:
                self._state["current"] = SLIXSLEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slurflan', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slurflan',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slurflan->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slixslex(self, hint):
        assert self._state.get("current") == SLIXSLEX, \
            f"drosblosl.slixslex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slixslex', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'slixslex', _:
                self._state["current"] = GRONSPORBRAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slixslex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slixslex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slixslex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _gronsporbral(self, hint):
        assert self._state.get("current") == GRONSPORBRAL, \
            f"drosblosl.gronsporbral: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'gronsporbral', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'gronsporbral', 1:
                self._state["current"] = DRURGRELBRELR
                self._state["trig"]    = "hint:1"
            case 'gronsporbral', _:
                self._state["current"] = SKENTRULX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'gronsporbral', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'gronsporbral',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"gronsporbral->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skentrulx(self, hint):
        assert self._state.get("current") == SKENTRULX, \
            f"drosblosl.skentrulx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skentrulx', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'skentrulx', _:
                self._state["current"] = DRURGRELBRELR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skentrulx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skentrulx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skentrulx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drurgrelbrelr(self, hint):
        assert self._state.get("current") == DRURGRELBRELR, \
            f"drosblosl.drurgrelbrelr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drurgrelbrelr', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'drurgrelbrelr', 0:
                self._state["current"] = STARSPONSTAL
                self._state["trig"]    = "hint:0"
            case 'drurgrelbrelr', _:
                self._state["current"] = CLAXFLONVELT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drurgrelbrelr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drurgrelbrelr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drurgrelbrelr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _claxflonvelt(self, hint):
        assert self._state.get("current") == CLAXFLONVELT, \
            f"drosblosl.claxflonvelt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'claxflonvelt', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'claxflonvelt', 1:
                self._state["current"] = GLELSPALBRAL
                self._state["trig"]    = "hint:1"
            case 'claxflonvelt', _:
                self._state["current"] = STARSPONSTAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'claxflonvelt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'claxflonvelt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"claxflonvelt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _starsponstal(self, hint):
        assert self._state.get("current") == STARSPONSTAL, \
            f"drosblosl.starsponstal: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'starsponstal', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'starsponstal', 0:
                self._state["current"] = PRENKRANPRAR
                self._state["trig"]    = "hint:0"
            case 'starsponstal', _:
                self._state["current"] = BLEXTRAXSKULT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'starsponstal', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'starsponstal',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"starsponstal->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blextraxskult(self, hint):
        assert self._state.get("current") == BLEXTRAXSKULT, \
            f"drosblosl.blextraxskult: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blextraxskult', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'blextraxskult', _:
                self._state["current"] = PRENKRANPRAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blextraxskult', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blextraxskult',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blextraxskult->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prenkranprar(self, hint):
        assert self._state.get("current") == PRENKRANPRAR, \
            f"drosblosl.prenkranprar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prenkranprar', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'prenkranprar', 1:
                self._state["current"] = CLORDREN
                self._state["trig"]    = "hint:1"
            case 'prenkranprar', _:
                self._state["current"] = BREXPRALDRELR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prenkranprar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prenkranprar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prenkranprar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brexpraldrelr(self, hint):
        assert self._state.get("current") == BREXPRALDRELR, \
            f"drosblosl.brexpraldrelr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brexpraldrelr', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'brexpraldrelr', 0:
                self._state["current"] = GLELSPALBRAL
                self._state["trig"]    = "hint:0"
            case 'brexpraldrelr', _:
                self._state["current"] = CLORDREN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brexpraldrelr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brexpraldrelr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brexpraldrelr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clordren(self, hint):
        assert self._state.get("current") == CLORDREN, \
            f"drosblosl.clordren: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clordren', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'clordren', 0:
                self._state["current"] = STURCLURSPIMK
                self._state["trig"]    = "hint:0"
            case 'clordren', _:
                self._state["current"] = BLIMSKULDRIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clordren', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clordren',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clordren->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blimskuldrix(self, hint):
        assert self._state.get("current") == BLIMSKULDRIX, \
            f"drosblosl.blimskuldrix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blimskuldrix', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'blimskuldrix', 1:
                self._state["current"] = GLELSPALBRAL
                self._state["trig"]    = "hint:1"
            case 'blimskuldrix', _:
                self._state["current"] = STURCLURSPIMK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blimskuldrix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blimskuldrix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blimskuldrix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _sturclurspimk(self, hint):
        assert self._state.get("current") == STURCLURSPIMK, \
            f"drosblosl.sturclurspimk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'sturclurspimk', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'sturclurspimk', 1:
                self._state["current"] = GLELSPALBRAL
                self._state["trig"]    = "hint:1"
            case 'sturclurspimk', _:
                self._state["current"] = GRARPRIMTRARX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'sturclurspimk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'sturclurspimk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"sturclurspimk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grarprimtrarx(self, hint):
        assert self._state.get("current") == GRARPRIMTRARX, \
            f"drosblosl.grarprimtrarx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grarprimtrarx', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'grarprimtrarx', _:
                self._state["current"] = DRELSTARBRIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grarprimtrarx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grarprimtrarx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grarprimtrarx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drelstarbrix(self, hint):
        assert self._state.get("current") == DRELSTARBRIX, \
            f"drosblosl.drelstarbrix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drelstarbrix', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'drelstarbrix', 0:
                self._state["current"] = GLELSPALBRAL
                self._state["trig"]    = "hint:0"
            case 'drelstarbrix', _:
                self._state["current"] = VELCLAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drelstarbrix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drelstarbrix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drelstarbrix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _velclan(self, hint):
        assert self._state.get("current") == VELCLAN, \
            f"drosblosl.velclan: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'velclan', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'velclan', 1:
                self._state["current"] = GLELSPALBRAL
                self._state["trig"]    = "hint:1"
            case 'velclan', _:
                self._state["current"] = PRANKRULSPALL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'velclan', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'velclan',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"velclan->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prankrulspall(self, hint):
        assert self._state.get("current") == PRANKRULSPALL, \
            f"drosblosl.prankrulspall: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prankrulspall', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'prankrulspall', _:
                self._state["current"] = GLELPRURR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prankrulspall', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prankrulspall',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prankrulspall->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glelprurr(self, hint):
        assert self._state.get("current") == GLELPRURR, \
            f"drosblosl.glelprurr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glelprurr', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'glelprurr', 0:
                self._state["current"] = GLELSPALBRAL
                self._state["trig"]    = "hint:0"
            case 'glelprurr', _:
                self._state["current"] = BLAXPRARBREXL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glelprurr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glelprurr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glelprurr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blaxprarbrexl(self, hint):
        assert self._state.get("current") == BLAXPRARBREXL, \
            f"drosblosl.blaxprarbrexl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blaxprarbrexl', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'blaxprarbrexl', _:
                self._state["current"] = GLANTRELL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blaxprarbrexl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blaxprarbrexl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blaxprarbrexl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glantrell(self, hint):
        assert self._state.get("current") == GLANTRELL, \
            f"drosblosl.glantrell: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glantrell', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'glantrell', 0:
                self._state["current"] = GLELSPALBRAL
                self._state["trig"]    = "hint:0"
            case 'glantrell', _:
                self._state["current"] = BRARVANKREX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glantrell', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glantrell',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glantrell->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brarvankrex(self, hint):
        assert self._state.get("current") == BRARVANKREX, \
            f"drosblosl.brarvankrex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brarvankrex', 2:
                self._state["current"] = BREXSKORFLANR
                self._state["trig"]    = "hint:2"
            case 'brarvankrex', 1:
                self._state["current"] = GLELSPALBRAL
                self._state["trig"]    = "hint:1"
            case 'brarvankrex', _:
                self._state["current"] = SLONKRARTRORR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brarvankrex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brarvankrex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brarvankrex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def invoke(self, hint=None, span=None, caller=None, ctx=None, cycle=0):
        if ctx is None: ctx = {}

        self._state = {"current": FLAXDRANR, "ctx": ctx,
                        "span": span, "caller": caller,
                        "trig": "auto", "cycle": cycle}
        _dispatch = {
            FLAXDRANR: self._flaxdranr,
            BRENKRAN: self._brenkran,
            PRONSTARSLAX: self._pronstarslax,
            GLIMCLART: self._glimclart,
            SLANKRALFLELR: self._slankralflelr,
            BRENDRENK: self._brendrenk,
            SPEXBLUR: self._spexblur,
            BLANDREXSKAR: self._blandrexskar,
            FLULBLARN: self._flulblarn,
            SLALGRULR: self._slalgrulr,
            TRENVAXGRENR: self._trenvaxgrenr,
            BLONSLAR: self._blonslar,
            GLARSTORGLON: self._glarstorglon,
            CLULKROSSPIMX: self._clulkrosspimx,
            BROSFLENDRIM: self._brosflendrim,
            VULPRAXN: self._vulpraxn,
            CLIMGLORBLOR: self._climglorblor,
            FLARVOSSKAX: self._flarvosskax,
            BREXCLARBLAN: self._brexclarblan,
            STAXPROS: self._staxpros,
            PRALSLAXR: self._pralslaxr,
            VELGLAXT: self._velglaxt,
            SPARSPULSKAX: self._sparspulskax,
            CLOSDRENFLON: self._closdrenflon,
            KRIMVORGRAR: self._krimvorgrar,
            GRORVAXK: self._grorvaxk,
            VAXSTEXPRELK: self._vaxstexprelk,
            GLELSPURL: self._glelspurl,
            SKOSPRURSTAX: self._skosprurstax,
            DREXSPENSKORN: self._drexspenskorn,
            GRURBRULGRORX: self._grurbrulgrorx,
            SKIXGLEX: self._skixglex,
            TRARSLELX: self._trarslelx,
            BRENSTONR: self._brenstonr,
            KRONSTANCLOSX: self._kronstanclosx,
            CLIXSTORT: self._clixstort,
            CLURGLELDRAN: self._clurgleldran,
            VIXDRANGLALT: self._vixdranglalt,
            DRAXVELSTALT: self._draxvelstalt,
            SLIMBLIM: self._slimblim,
            PRENVELK: self._prenvelk,
            SPENGRORSKEX: self._spengrorskex,
            FLIMDREL: self._flimdrel,
            FLIXCLIX: self._flixclix,
            SLURFLAN: self._slurflan,
            SLIXSLEX: self._slixslex,
            GRONSPORBRAL: self._gronsporbral,
            SKENTRULX: self._skentrulx,
            DRURGRELBRELR: self._drurgrelbrelr,
            CLAXFLONVELT: self._claxflonvelt,
            STARSPONSTAL: self._starsponstal,
            BLEXTRAXSKULT: self._blextraxskult,
            PRENKRANPRAR: self._prenkranprar,
            BREXPRALDRELR: self._brexpraldrelr,
            CLORDREN: self._clordren,
            BLIMSKULDRIX: self._blimskuldrix,
            STURCLURSPIMK: self._sturclurspimk,
            GRARPRIMTRARX: self._grarprimtrarx,
            DRELSTARBRIX: self._drelstarbrix,
            VELCLAN: self._velclan,
            PRANKRULSPALL: self._prankrulspall,
            GLELPRURR: self._glelprurr,
            BLAXPRARBREXL: self._blaxprarbrexl,
            GLANTRELL: self._glantrell,
            BRARVANKREX: self._brarvankrex,
        }
        while self._state["current"] not in _R and self._state["cycle"] - cycle < 8000:
            _dispatch[self._state["current"]](hint)
        _ret     = _R.get(self._state["current"], -1)
        _is_err  = self._state["current"] == BREXSKORFLANR
        if _is_err:
            _asrt    = {"failed": "no_error_terminal",
                         "expected": "terminal in {0, 1}",
                         "actual": f"ret={_ret}"}
            _xid_val = _xid(__name__, self._state["current"], "error", "terminal")
            _emit(self._state["cycle"], 1, __name__, self._state["current"],
                   {"hint": hint, "span": span, "caller": caller},
                   dict(ctx), {}, "terminal_error", _xid_val, assertion=_asrt)
            self._state["cycle"] += 1
        return _ret, self._state["cycle"]

def invoke(hint=None, span=None, caller=None, ctx=None, cycle=0):
    return DrosbloslFSM().invoke(hint=hint, span=span, caller=caller, ctx=ctx, cycle=cycle)
