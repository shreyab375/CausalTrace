from _log import _w as _emit, _xid

VONCLORBRAL = 'vonclorbral'
KRIXPRIXSTIXX = 'krixprixstixx'
GLAXPRANSTEL = 'glaxpranstel'
PRIMSKELN = 'primskeln'
DRORSTAX = 'drorstax'
DRARSKEN = 'drarsken'
TRELBRURT = 'trelbrurt'
PRELBLALTRUL = 'prelblaltrul'
GLORKRAXVOR = 'glorkraxvor'
DRENGRAR = 'drengrar'
KREXCLAX = 'krexclax'
SPANFLANX = 'spanflanx'
SKENDRIXX = 'skendrixx'
DRONCLORR = 'dronclorr'
DRENCLEX = 'drenclex'
CLURBRULFLUL = 'clurbrulflul'
KRIXPROSSLONR = 'krixprosslonr'
SPURGLIMX = 'spurglimx'
TRARTRIMCLAX = 'trartrimclax'
SPULTRIX = 'spultrix'
SLALSKELBROR = 'slalskelbror'
SPULSTIMSKAL = 'spulstimskal'
TRANDRORGLENX = 'trandrorglenx'
BLELBLALGRENL = 'blelblalgrenl'
VENCLAN = 'venclan'
BRIMGLEN = 'brimglen'
TRAXSPIXT = 'traxspixt'
CLIMSLURSKALK = 'climslurskalk'
PRURTRENSKENT = 'prurtrenskent'
BRANSTULDRELN = 'branstuldreln'
SPULBLIMVAXN = 'spulblimvaxn'
SLARSTOR = 'slarstor'
VEXSLEXVEN = 'vexslexven'
BRELSKURL = 'brelskurl'
GRURGRULDREX = 'grurgruldrex'
SPANTRAXCLARK = 'spantraxclark'
SKENSPELT = 'skenspelt'
KRELGROS = 'krelgros'
BLORDRIXCLURN = 'blordrixclurn'
SLONSKANT = 'slonskant'
VAXDRAXN = 'vaxdraxn'
STONKRORSPARL = 'stonkrorsparl'
GLIMSLOS = 'glimslos'
PRARPRELFLEXR = 'prarprelflexr'
STENGLONBRIXL = 'stenglonbrixl'
GREXSKOSK = 'grexskosk'
CLELDRART = 'cleldrart'
BROSTRIXL = 'brostrixl'
SKIMGLEXL = 'skimglexl'
CLARPRORSKEXX = 'clarprorskexx'
SLENTRAR = 'slentrar'
GLULBLELX = 'glulblelx'
SKIMPRELKRAR = 'skimprelkrar'
BLANSLART = 'blanslart'
PREXBRENSTEL = 'prexbrenstel'
GRULBLORR = 'grulblorr'
VARSTENDRAN = 'varstendran'
BLAXBLULKRIMN = 'blaxblulkrimn'
FLULDRALVALT = 'fluldralvalt'
DRANSLAN = 'dranslan'
DREXDRAXN = 'drexdraxn'
TRULDRIXCLOS = 'truldrixclos'
BRIXKRURBLEN = 'brixkrurblen'
CLANDRORFLON = 'clandrorflon'
SKONBLORGRALX = 'skonblorgralx'
SLARKRANPRART = 'slarkranprart'
STELKRAL = 'stelkral'
SPENBRIMX = 'spenbrimx'

_R = {
    SLARKRANPRART: 0,
    STELKRAL: 1,
    SPENBRIMX: 2,
}

_CTX_READS_KEY = 'flurslex'
_CTX_THRESHOLD = 16

class DrixslimFSM:
    def __init__(self):
        self._state = {}

    def _vonclorbral(self, hint):
        assert self._state.get("current") == VONCLORBRAL, \
            f"drixslim.vonclorbral: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vonclorbral', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'vonclorbral', 0:
                self._state["current"] = GLAXPRANSTEL
                self._state["trig"]    = "hint:0"
            case 'vonclorbral', _:
                self._state["current"] = KRIXPRIXSTIXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vonclorbral', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vonclorbral',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vonclorbral->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krixprixstixx(self, hint):
        assert self._state.get("current") == KRIXPRIXSTIXX, \
            f"drixslim.krixprixstixx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krixprixstixx', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'krixprixstixx', _:
                self._state["current"] = GLAXPRANSTEL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krixprixstixx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krixprixstixx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krixprixstixx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glaxpranstel(self, hint):
        assert self._state.get("current") == GLAXPRANSTEL, \
            f"drixslim.glaxpranstel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glaxpranstel', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'glaxpranstel', _:
                self._state["current"] = PRIMSKELN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glaxpranstel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glaxpranstel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glaxpranstel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _primskeln(self, hint):
        assert self._state.get("current") == PRIMSKELN, \
            f"drixslim.primskeln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'primskeln', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'primskeln', _:
                self._state["current"] = DRORSTAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'primskeln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'primskeln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"primskeln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drorstax(self, hint):
        assert self._state.get("current") == DRORSTAX, \
            f"drixslim.drorstax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drorstax', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'drorstax', _:
                self._state["current"] = DRARSKEN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drorstax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drorstax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drorstax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drarsken(self, hint):
        assert self._state.get("current") == DRARSKEN, \
            f"drixslim.drarsken: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drarsken', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'drarsken', 0:
                self._state["current"] = PRELBLALTRUL
                self._state["trig"]    = "hint:0"
            case 'drarsken', _:
                self._state["current"] = TRELBRURT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drarsken', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drarsken',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drarsken->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trelbrurt(self, hint):
        assert self._state.get("current") == TRELBRURT, \
            f"drixslim.trelbrurt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trelbrurt', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'trelbrurt', 1:
                self._state["current"] = STELKRAL
                self._state["trig"]    = "hint:1"
            case 'trelbrurt', _:
                self._state["current"] = PRELBLALTRUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trelbrurt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trelbrurt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trelbrurt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prelblaltrul(self, hint):
        assert self._state.get("current") == PRELBLALTRUL, \
            f"drixslim.prelblaltrul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prelblaltrul', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'prelblaltrul', 1:
                self._state["current"] = STELKRAL
                self._state["trig"]    = "hint:1"
            case 'prelblaltrul', _:
                self._state["current"] = GLORKRAXVOR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prelblaltrul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prelblaltrul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prelblaltrul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glorkraxvor(self, hint):
        assert self._state.get("current") == GLORKRAXVOR, \
            f"drixslim.glorkraxvor: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glorkraxvor', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'glorkraxvor', _:
                self._state["current"] = DRENGRAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glorkraxvor', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glorkraxvor',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glorkraxvor->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drengrar(self, hint):
        assert self._state.get("current") == DRENGRAR, \
            f"drixslim.drengrar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drengrar', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'drengrar', 1:
                self._state["current"] = SPANFLANX
                self._state["trig"]    = "hint:1"
            case 'drengrar', _:
                self._state["current"] = KREXCLAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drengrar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drengrar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drengrar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krexclax(self, hint):
        assert self._state.get("current") == KREXCLAX, \
            f"drixslim.krexclax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krexclax', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'krexclax', _:
                self._state["current"] = SPANFLANX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krexclax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krexclax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krexclax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spanflanx(self, hint):
        assert self._state.get("current") == SPANFLANX, \
            f"drixslim.spanflanx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spanflanx', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'spanflanx', 1:
                self._state["current"] = STELKRAL
                self._state["trig"]    = "hint:1"
            case 'spanflanx', _:
                self._state["current"] = SKENDRIXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spanflanx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spanflanx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spanflanx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skendrixx(self, hint):
        assert self._state.get("current") == SKENDRIXX, \
            f"drixslim.skendrixx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skendrixx', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'skendrixx', 0:
                self._state["current"] = DRENCLEX
                self._state["trig"]    = "hint:0"
            case 'skendrixx', _:
                self._state["current"] = DRONCLORR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skendrixx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skendrixx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skendrixx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _dronclorr(self, hint):
        assert self._state.get("current") == DRONCLORR, \
            f"drixslim.dronclorr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'dronclorr', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'dronclorr', _:
                self._state["current"] = DRENCLEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'dronclorr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'dronclorr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"dronclorr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drenclex(self, hint):
        assert self._state.get("current") == DRENCLEX, \
            f"drixslim.drenclex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drenclex', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'drenclex', _:
                self._state["current"] = CLURBRULFLUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drenclex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drenclex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drenclex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clurbrulflul(self, hint):
        assert self._state.get("current") == CLURBRULFLUL, \
            f"drixslim.clurbrulflul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clurbrulflul', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'clurbrulflul', _:
                self._state["current"] = KRIXPROSSLONR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clurbrulflul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clurbrulflul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clurbrulflul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krixprosslonr(self, hint):
        assert self._state.get("current") == KRIXPROSSLONR, \
            f"drixslim.krixprosslonr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krixprosslonr', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'krixprosslonr', 1:
                self._state["current"] = TRARTRIMCLAX
                self._state["trig"]    = "hint:1"
            case 'krixprosslonr', _:
                self._state["current"] = SPURGLIMX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krixprosslonr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krixprosslonr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krixprosslonr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spurglimx(self, hint):
        assert self._state.get("current") == SPURGLIMX, \
            f"drixslim.spurglimx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spurglimx', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'spurglimx', 1:
                self._state["current"] = STELKRAL
                self._state["trig"]    = "hint:1"
            case 'spurglimx', _:
                self._state["current"] = TRARTRIMCLAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spurglimx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spurglimx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spurglimx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trartrimclax(self, hint):
        assert self._state.get("current") == TRARTRIMCLAX, \
            f"drixslim.trartrimclax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trartrimclax', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'trartrimclax', 0:
                self._state["current"] = SLALSKELBROR
                self._state["trig"]    = "hint:0"
            case 'trartrimclax', _:
                self._state["current"] = SPULTRIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trartrimclax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trartrimclax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trartrimclax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spultrix(self, hint):
        assert self._state.get("current") == SPULTRIX, \
            f"drixslim.spultrix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spultrix', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'spultrix', _:
                self._state["current"] = SLALSKELBROR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spultrix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spultrix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spultrix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slalskelbror(self, hint):
        assert self._state.get("current") == SLALSKELBROR, \
            f"drixslim.slalskelbror: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slalskelbror', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'slalskelbror', 0:
                self._state["current"] = STELKRAL
                self._state["trig"]    = "hint:0"
            case 'slalskelbror', _:
                self._state["current"] = SPULSTIMSKAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slalskelbror', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slalskelbror',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slalskelbror->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spulstimskal(self, hint):
        assert self._state.get("current") == SPULSTIMSKAL, \
            f"drixslim.spulstimskal: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spulstimskal', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'spulstimskal', _:
                self._state["current"] = TRANDRORGLENX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spulstimskal', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spulstimskal',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spulstimskal->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trandrorglenx(self, hint):
        assert self._state.get("current") == TRANDRORGLENX, \
            f"drixslim.trandrorglenx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trandrorglenx', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'trandrorglenx', _:
                self._state["current"] = BLELBLALGRENL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trandrorglenx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trandrorglenx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trandrorglenx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blelblalgrenl(self, hint):
        assert self._state.get("current") == BLELBLALGRENL, \
            f"drixslim.blelblalgrenl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blelblalgrenl', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'blelblalgrenl', _:
                self._state["current"] = VENCLAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blelblalgrenl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blelblalgrenl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blelblalgrenl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _venclan(self, hint):
        assert self._state.get("current") == VENCLAN, \
            f"drixslim.venclan: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'venclan', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'venclan', 0:
                self._state["current"] = STELKRAL
                self._state["trig"]    = "hint:0"
            case 'venclan', _:
                self._state["current"] = BRIMGLEN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'venclan', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'venclan',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"venclan->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brimglen(self, hint):
        assert self._state.get("current") == BRIMGLEN, \
            f"drixslim.brimglen: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brimglen', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'brimglen', _:
                self._state["current"] = TRAXSPIXT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brimglen', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brimglen',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brimglen->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _traxspixt(self, hint):
        assert self._state.get("current") == TRAXSPIXT, \
            f"drixslim.traxspixt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'traxspixt', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'traxspixt', 1:
                self._state["current"] = STELKRAL
                self._state["trig"]    = "hint:1"
            case 'traxspixt', _:
                self._state["current"] = CLIMSLURSKALK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'traxspixt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'traxspixt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"traxspixt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _climslurskalk(self, hint):
        assert self._state.get("current") == CLIMSLURSKALK, \
            f"drixslim.climslurskalk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'climslurskalk', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'climslurskalk', _:
                self._state["current"] = PRURTRENSKENT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'climslurskalk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'climslurskalk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"climslurskalk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prurtrenskent(self, hint):
        assert self._state.get("current") == PRURTRENSKENT, \
            f"drixslim.prurtrenskent: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prurtrenskent', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'prurtrenskent', _:
                self._state["current"] = BRANSTULDRELN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prurtrenskent', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prurtrenskent',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prurtrenskent->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _branstuldreln(self, hint):
        assert self._state.get("current") == BRANSTULDRELN, \
            f"drixslim.branstuldreln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'branstuldreln', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'branstuldreln', 0:
                self._state["current"] = SLARSTOR
                self._state["trig"]    = "hint:0"
            case 'branstuldreln', _:
                self._state["current"] = SPULBLIMVAXN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'branstuldreln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'branstuldreln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"branstuldreln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spulblimvaxn(self, hint):
        assert self._state.get("current") == SPULBLIMVAXN, \
            f"drixslim.spulblimvaxn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spulblimvaxn', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'spulblimvaxn', _:
                self._state["current"] = SLARSTOR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spulblimvaxn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spulblimvaxn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spulblimvaxn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slarstor(self, hint):
        assert self._state.get("current") == SLARSTOR, \
            f"drixslim.slarstor: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slarstor', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'slarstor', _:
                self._state["current"] = VEXSLEXVEN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slarstor', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slarstor',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slarstor->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vexslexven(self, hint):
        assert self._state.get("current") == VEXSLEXVEN, \
            f"drixslim.vexslexven: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vexslexven', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'vexslexven', _:
                self._state["current"] = BRELSKURL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vexslexven', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vexslexven',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vexslexven->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brelskurl(self, hint):
        assert self._state.get("current") == BRELSKURL, \
            f"drixslim.brelskurl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brelskurl', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'brelskurl', 1:
                self._state["current"] = STELKRAL
                self._state["trig"]    = "hint:1"
            case 'brelskurl', _:
                self._state["current"] = GRURGRULDREX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brelskurl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brelskurl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brelskurl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grurgruldrex(self, hint):
        assert self._state.get("current") == GRURGRULDREX, \
            f"drixslim.grurgruldrex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grurgruldrex', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'grurgruldrex', 0:
                self._state["current"] = STELKRAL
                self._state["trig"]    = "hint:0"
            case 'grurgruldrex', _:
                self._state["current"] = SPANTRAXCLARK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grurgruldrex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grurgruldrex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grurgruldrex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spantraxclark(self, hint):
        assert self._state.get("current") == SPANTRAXCLARK, \
            f"drixslim.spantraxclark: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spantraxclark', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'spantraxclark', _:
                self._state["current"] = SKENSPELT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spantraxclark', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spantraxclark',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spantraxclark->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skenspelt(self, hint):
        assert self._state.get("current") == SKENSPELT, \
            f"drixslim.skenspelt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skenspelt', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'skenspelt', 0:
                self._state["current"] = STELKRAL
                self._state["trig"]    = "hint:0"
            case 'skenspelt', _:
                self._state["current"] = KRELGROS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skenspelt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skenspelt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skenspelt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krelgros(self, hint):
        assert self._state.get("current") == KRELGROS, \
            f"drixslim.krelgros: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krelgros', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'krelgros', _:
                self._state["current"] = BLORDRIXCLURN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krelgros', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krelgros',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krelgros->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blordrixclurn(self, hint):
        assert self._state.get("current") == BLORDRIXCLURN, \
            f"drixslim.blordrixclurn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blordrixclurn', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'blordrixclurn', _:
                self._state["current"] = SLONSKANT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blordrixclurn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blordrixclurn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blordrixclurn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slonskant(self, hint):
        assert self._state.get("current") == SLONSKANT, \
            f"drixslim.slonskant: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slonskant', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'slonskant', 1:
                self._state["current"] = STONKRORSPARL
                self._state["trig"]    = "hint:1"
            case 'slonskant', _:
                self._state["current"] = VAXDRAXN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slonskant', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slonskant',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slonskant->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vaxdraxn(self, hint):
        assert self._state.get("current") == VAXDRAXN, \
            f"drixslim.vaxdraxn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vaxdraxn', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'vaxdraxn', _:
                self._state["current"] = STONKRORSPARL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vaxdraxn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vaxdraxn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vaxdraxn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stonkrorsparl(self, hint):
        assert self._state.get("current") == STONKRORSPARL, \
            f"drixslim.stonkrorsparl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stonkrorsparl', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'stonkrorsparl', 0:
                self._state["current"] = PRARPRELFLEXR
                self._state["trig"]    = "hint:0"
            case 'stonkrorsparl', _:
                self._state["current"] = GLIMSLOS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stonkrorsparl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stonkrorsparl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stonkrorsparl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glimslos(self, hint):
        assert self._state.get("current") == GLIMSLOS, \
            f"drixslim.glimslos: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glimslos', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'glimslos', 0:
                self._state["current"] = STENGLONBRIXL
                self._state["trig"]    = "hint:0"
            case 'glimslos', _:
                self._state["current"] = PRARPRELFLEXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glimslos', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glimslos',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glimslos->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prarprelflexr(self, hint):
        assert self._state.get("current") == PRARPRELFLEXR, \
            f"drixslim.prarprelflexr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prarprelflexr', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'prarprelflexr', 0:
                self._state["current"] = STELKRAL
                self._state["trig"]    = "hint:0"
            case 'prarprelflexr', _:
                self._state["current"] = STENGLONBRIXL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prarprelflexr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prarprelflexr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prarprelflexr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stenglonbrixl(self, hint):
        assert self._state.get("current") == STENGLONBRIXL, \
            f"drixslim.stenglonbrixl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stenglonbrixl', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'stenglonbrixl', 0:
                self._state["current"] = CLELDRART
                self._state["trig"]    = "hint:0"
            case 'stenglonbrixl', _:
                self._state["current"] = GREXSKOSK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stenglonbrixl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stenglonbrixl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stenglonbrixl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grexskosk(self, hint):
        assert self._state.get("current") == GREXSKOSK, \
            f"drixslim.grexskosk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grexskosk', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'grexskosk', 1:
                self._state["current"] = STELKRAL
                self._state["trig"]    = "hint:1"
            case 'grexskosk', _:
                self._state["current"] = CLELDRART
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grexskosk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grexskosk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grexskosk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _cleldrart(self, hint):
        assert self._state.get("current") == CLELDRART, \
            f"drixslim.cleldrart: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'cleldrart', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'cleldrart', _:
                self._state["current"] = BROSTRIXL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'cleldrart', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'cleldrart',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"cleldrart->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brostrixl(self, hint):
        assert self._state.get("current") == BROSTRIXL, \
            f"drixslim.brostrixl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brostrixl', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'brostrixl', _:
                self._state["current"] = SKIMGLEXL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brostrixl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brostrixl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brostrixl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skimglexl(self, hint):
        assert self._state.get("current") == SKIMGLEXL, \
            f"drixslim.skimglexl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skimglexl', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'skimglexl', _:
                self._state["current"] = CLARPRORSKEXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skimglexl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skimglexl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skimglexl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clarprorskexx(self, hint):
        assert self._state.get("current") == CLARPRORSKEXX, \
            f"drixslim.clarprorskexx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clarprorskexx', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'clarprorskexx', _:
                self._state["current"] = SLENTRAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clarprorskexx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clarprorskexx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clarprorskexx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slentrar(self, hint):
        assert self._state.get("current") == SLENTRAR, \
            f"drixslim.slentrar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slentrar', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'slentrar', _:
                self._state["current"] = GLULBLELX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slentrar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slentrar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slentrar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glulblelx(self, hint):
        assert self._state.get("current") == GLULBLELX, \
            f"drixslim.glulblelx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glulblelx', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'glulblelx', _:
                self._state["current"] = SKIMPRELKRAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glulblelx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glulblelx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glulblelx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skimprelkrar(self, hint):
        assert self._state.get("current") == SKIMPRELKRAR, \
            f"drixslim.skimprelkrar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skimprelkrar', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'skimprelkrar', 0:
                self._state["current"] = STELKRAL
                self._state["trig"]    = "hint:0"
            case 'skimprelkrar', _:
                self._state["current"] = BLANSLART
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skimprelkrar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skimprelkrar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skimprelkrar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blanslart(self, hint):
        assert self._state.get("current") == BLANSLART, \
            f"drixslim.blanslart: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blanslart', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'blanslart', _:
                self._state["current"] = PREXBRENSTEL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blanslart', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blanslart',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blanslart->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prexbrenstel(self, hint):
        assert self._state.get("current") == PREXBRENSTEL, \
            f"drixslim.prexbrenstel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prexbrenstel', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'prexbrenstel', 0:
                self._state["current"] = VARSTENDRAN
                self._state["trig"]    = "hint:0"
            case 'prexbrenstel', _:
                self._state["current"] = GRULBLORR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prexbrenstel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prexbrenstel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prexbrenstel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grulblorr(self, hint):
        assert self._state.get("current") == GRULBLORR, \
            f"drixslim.grulblorr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grulblorr', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'grulblorr', 1:
                self._state["current"] = BLAXBLULKRIMN
                self._state["trig"]    = "hint:1"
            case 'grulblorr', _:
                self._state["current"] = VARSTENDRAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grulblorr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grulblorr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grulblorr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _varstendran(self, hint):
        assert self._state.get("current") == VARSTENDRAN, \
            f"drixslim.varstendran: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'varstendran', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'varstendran', _:
                self._state["current"] = BLAXBLULKRIMN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'varstendran', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'varstendran',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"varstendran->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blaxblulkrimn(self, hint):
        assert self._state.get("current") == BLAXBLULKRIMN, \
            f"drixslim.blaxblulkrimn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blaxblulkrimn', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'blaxblulkrimn', _:
                self._state["current"] = FLULDRALVALT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blaxblulkrimn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blaxblulkrimn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blaxblulkrimn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _fluldralvalt(self, hint):
        assert self._state.get("current") == FLULDRALVALT, \
            f"drixslim.fluldralvalt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'fluldralvalt', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'fluldralvalt', 0:
                self._state["current"] = STELKRAL
                self._state["trig"]    = "hint:0"
            case 'fluldralvalt', _:
                self._state["current"] = DRANSLAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'fluldralvalt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'fluldralvalt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"fluldralvalt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _dranslan(self, hint):
        assert self._state.get("current") == DRANSLAN, \
            f"drixslim.dranslan: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'dranslan', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'dranslan', _:
                self._state["current"] = DREXDRAXN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'dranslan', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'dranslan',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"dranslan->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drexdraxn(self, hint):
        assert self._state.get("current") == DREXDRAXN, \
            f"drixslim.drexdraxn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drexdraxn', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'drexdraxn', _:
                self._state["current"] = TRULDRIXCLOS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drexdraxn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drexdraxn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drexdraxn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _truldrixclos(self, hint):
        assert self._state.get("current") == TRULDRIXCLOS, \
            f"drixslim.truldrixclos: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'truldrixclos', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'truldrixclos', 1:
                self._state["current"] = STELKRAL
                self._state["trig"]    = "hint:1"
            case 'truldrixclos', _:
                self._state["current"] = BRIXKRURBLEN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'truldrixclos', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'truldrixclos',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"truldrixclos->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brixkrurblen(self, hint):
        assert self._state.get("current") == BRIXKRURBLEN, \
            f"drixslim.brixkrurblen: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brixkrurblen', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'brixkrurblen', _:
                self._state["current"] = CLANDRORFLON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brixkrurblen', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brixkrurblen',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brixkrurblen->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clandrorflon(self, hint):
        assert self._state.get("current") == CLANDRORFLON, \
            f"drixslim.clandrorflon: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clandrorflon', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'clandrorflon', 0:
                self._state["current"] = STELKRAL
                self._state["trig"]    = "hint:0"
            case 'clandrorflon', _:
                self._state["current"] = SKONBLORGRALX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clandrorflon', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clandrorflon',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clandrorflon->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skonblorgralx(self, hint):
        assert self._state.get("current") == SKONBLORGRALX, \
            f"drixslim.skonblorgralx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skonblorgralx', 2:
                self._state["current"] = SPENBRIMX
                self._state["trig"]    = "hint:2"
            case 'skonblorgralx', 1:
                self._state["current"] = STELKRAL
                self._state["trig"]    = "hint:1"
            case 'skonblorgralx', _:
                self._state["current"] = SLARKRANPRART
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skonblorgralx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skonblorgralx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skonblorgralx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def invoke(self, hint=None, span=None, caller=None, ctx=None, cycle=0):
        if ctx is None: ctx = {}

        _cv    = ctx.get(_CTX_READS_KEY, 0)
        _conds = {"ctx_degraded": _cv > 0,
                   "threshold_exceeded": _cv >= _CTX_THRESHOLD}
        if _cv >= _CTX_THRESHOLD:
            _asrt = {"failed": "ctx_below_threshold",
                      "expected": f"ctx[{_CTX_READS_KEY}] < {_CTX_THRESHOLD}",
                      "actual":   f"ctx[{_CTX_READS_KEY}] == {_cv}"}
            _xid_val = _xid(__name__, 'vonclorbral', "error", "assert_fail")
            _emit(cycle, 1, __name__, 'vonclorbral',
                   {"hint": hint, "span": span, "caller": caller},
                   dict(ctx), _conds,
                   "entry_blocked->error", _xid_val, assertion=_asrt)
            return 2, cycle + 1

        self._state = {"current": VONCLORBRAL, "ctx": ctx,
                        "span": span, "caller": caller,
                        "trig": "auto", "cycle": cycle}
        _dispatch = {
            VONCLORBRAL: self._vonclorbral,
            KRIXPRIXSTIXX: self._krixprixstixx,
            GLAXPRANSTEL: self._glaxpranstel,
            PRIMSKELN: self._primskeln,
            DRORSTAX: self._drorstax,
            DRARSKEN: self._drarsken,
            TRELBRURT: self._trelbrurt,
            PRELBLALTRUL: self._prelblaltrul,
            GLORKRAXVOR: self._glorkraxvor,
            DRENGRAR: self._drengrar,
            KREXCLAX: self._krexclax,
            SPANFLANX: self._spanflanx,
            SKENDRIXX: self._skendrixx,
            DRONCLORR: self._dronclorr,
            DRENCLEX: self._drenclex,
            CLURBRULFLUL: self._clurbrulflul,
            KRIXPROSSLONR: self._krixprosslonr,
            SPURGLIMX: self._spurglimx,
            TRARTRIMCLAX: self._trartrimclax,
            SPULTRIX: self._spultrix,
            SLALSKELBROR: self._slalskelbror,
            SPULSTIMSKAL: self._spulstimskal,
            TRANDRORGLENX: self._trandrorglenx,
            BLELBLALGRENL: self._blelblalgrenl,
            VENCLAN: self._venclan,
            BRIMGLEN: self._brimglen,
            TRAXSPIXT: self._traxspixt,
            CLIMSLURSKALK: self._climslurskalk,
            PRURTRENSKENT: self._prurtrenskent,
            BRANSTULDRELN: self._branstuldreln,
            SPULBLIMVAXN: self._spulblimvaxn,
            SLARSTOR: self._slarstor,
            VEXSLEXVEN: self._vexslexven,
            BRELSKURL: self._brelskurl,
            GRURGRULDREX: self._grurgruldrex,
            SPANTRAXCLARK: self._spantraxclark,
            SKENSPELT: self._skenspelt,
            KRELGROS: self._krelgros,
            BLORDRIXCLURN: self._blordrixclurn,
            SLONSKANT: self._slonskant,
            VAXDRAXN: self._vaxdraxn,
            STONKRORSPARL: self._stonkrorsparl,
            GLIMSLOS: self._glimslos,
            PRARPRELFLEXR: self._prarprelflexr,
            STENGLONBRIXL: self._stenglonbrixl,
            GREXSKOSK: self._grexskosk,
            CLELDRART: self._cleldrart,
            BROSTRIXL: self._brostrixl,
            SKIMGLEXL: self._skimglexl,
            CLARPRORSKEXX: self._clarprorskexx,
            SLENTRAR: self._slentrar,
            GLULBLELX: self._glulblelx,
            SKIMPRELKRAR: self._skimprelkrar,
            BLANSLART: self._blanslart,
            PREXBRENSTEL: self._prexbrenstel,
            GRULBLORR: self._grulblorr,
            VARSTENDRAN: self._varstendran,
            BLAXBLULKRIMN: self._blaxblulkrimn,
            FLULDRALVALT: self._fluldralvalt,
            DRANSLAN: self._dranslan,
            DREXDRAXN: self._drexdraxn,
            TRULDRIXCLOS: self._truldrixclos,
            BRIXKRURBLEN: self._brixkrurblen,
            CLANDRORFLON: self._clandrorflon,
            SKONBLORGRALX: self._skonblorgralx,
        }
        while self._state["current"] not in _R and self._state["cycle"] - cycle < 8000:
            _dispatch[self._state["current"]](hint)
        _ret     = _R.get(self._state["current"], -1)
        _is_err  = self._state["current"] == SPENBRIMX
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
    return DrixslimFSM().invoke(hint=hint, span=span, caller=caller, ctx=ctx, cycle=cycle)
