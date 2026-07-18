from _log import _w as _emit, _xid

DREXPREN = 'drexpren'
SPALSKAXGRAXT = 'spalskaxgraxt'
PRIMTRARGLAL = 'primtrarglal'
FLENPRON = 'flenpron'
FLANPRANSKELT = 'flanpranskelt'
PRARGRIX = 'prargrix'
BLANVIMDRAN = 'blanvimdran'
SPALDRON = 'spaldron'
SKIMKRUL = 'skimkrul'
SLELCLORR = 'slelclorr'
PRARSLAX = 'prarslax'
STORGLELSTURR = 'storglelsturr'
VAXSKAXKRARX = 'vaxskaxkrarx'
KRALBRELKREX = 'kralbrelkrex'
SPALDRAR = 'spaldrar'
VELDRIM = 'veldrim'
VARKRALPRAN = 'varkralpran'
STORCLENSLUL = 'storclenslul'
BRULTROSCLUR = 'brultrosclur'
FLIXVUL = 'flixvul'
DRIMFLENGRALT = 'drimflengralt'
GREXSKENR = 'grexskenr'
PRIXKREXVUL = 'prixkrexvul'
CLULSLELPRONT = 'clulslelpront'
CLIXKRANBLAN = 'clixkranblan'
BRULDRURL = 'bruldrurl'
FLOSGLARVANL = 'flosglarvanl'
TRELBLUR = 'trelblur'
PROSSKEXKRON = 'prosskexkron'
VONKRAR = 'vonkrar'
SLIMVIXCLALX = 'slimvixclalx'
SLAXSKURN = 'slaxskurn'
SKIMDROS = 'skimdros'
BRIMGLIMX = 'brimglimx'
GRURSKONPRULK = 'grurskonprulk'
GROSGLIX = 'grosglix'
GRELDRAXR = 'greldraxr'
CLENFLORN = 'clenflorn'
KRELGLOS = 'krelglos'
GLORVARDRANT = 'glorvardrant'
TRONGLURGLAR = 'tronglurglar'
KRALSTEXX = 'kralstexx'
SPONVIMR = 'sponvimr'
PROSGLAXT = 'prosglaxt'
BLELFLEL = 'blelflel'
BRURPRALT = 'brurpralt'
DRURKRAL = 'drurkral'
BRORKRALSLANL = 'brorkralslanl'
BLULSTENSPUR = 'blulstenspur'
VELCLANSLEXT = 'velclanslext'
FLELDRIXCLAR = 'fleldrixclar'
TRIXCLALSLENT = 'trixclalslent'
BLELBLONTROSX = 'blelblontrosx'
BRIMBRAN = 'brimbran'
BLIMBRORX = 'blimbrorx'
CLIXPRENSTIXT = 'clixprenstixt'
STORDROSR = 'stordrosr'
GLENBLAX = 'glenblax'
SPEXSKIXN = 'spexskixn'
SKIXSPARSKARK = 'skixsparskark'
CLOSBLIXGRUL = 'closblixgrul'
SLIMSLANT = 'slimslant'
BRONGLEXN = 'bronglexn'
BRURGLONSKELX = 'brurglonskelx'
FLURVON = 'flurvon'
KRENSTIX = 'krenstix'
VARPRAXR = 'varpraxr'
BRARGLOR = 'brarglor'

_R = {
    KRENSTIX: 0,
    VARPRAXR: 1,
    BRARGLOR: 2,
}

_CTX_WRITES_KEY  = 'flurslex'
_CTX_WRITE_STATE = STORGLELSTURR

class ClelvallFSM:
    def __init__(self):
        self._state = {}

    def _drexpren(self, hint):
        assert self._state.get("current") == DREXPREN, \
            f"clelvall.drexpren: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drexpren', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'drexpren', 1:
                self._state["current"] = VARPRAXR
                self._state["trig"]    = "hint:1"
            case 'drexpren', _:
                self._state["current"] = SPALSKAXGRAXT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drexpren', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drexpren',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drexpren->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spalskaxgraxt(self, hint):
        assert self._state.get("current") == SPALSKAXGRAXT, \
            f"clelvall.spalskaxgraxt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spalskaxgraxt', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'spalskaxgraxt', _:
                self._state["current"] = PRIMTRARGLAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spalskaxgraxt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spalskaxgraxt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spalskaxgraxt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _primtrarglal(self, hint):
        assert self._state.get("current") == PRIMTRARGLAL, \
            f"clelvall.primtrarglal: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'primtrarglal', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'primtrarglal', 0:
                self._state["current"] = VARPRAXR
                self._state["trig"]    = "hint:0"
            case 'primtrarglal', _:
                self._state["current"] = FLENPRON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'primtrarglal', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'primtrarglal',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"primtrarglal->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flenpron(self, hint):
        assert self._state.get("current") == FLENPRON, \
            f"clelvall.flenpron: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flenpron', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'flenpron', _:
                self._state["current"] = FLANPRANSKELT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flenpron', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flenpron',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flenpron->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flanpranskelt(self, hint):
        assert self._state.get("current") == FLANPRANSKELT, \
            f"clelvall.flanpranskelt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flanpranskelt', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'flanpranskelt', 0:
                self._state["current"] = VARPRAXR
                self._state["trig"]    = "hint:0"
            case 'flanpranskelt', _:
                self._state["current"] = PRARGRIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flanpranskelt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flanpranskelt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flanpranskelt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prargrix(self, hint):
        assert self._state.get("current") == PRARGRIX, \
            f"clelvall.prargrix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prargrix', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'prargrix', 1:
                self._state["current"] = SPALDRON
                self._state["trig"]    = "hint:1"
            case 'prargrix', _:
                self._state["current"] = BLANVIMDRAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prargrix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prargrix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prargrix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blanvimdran(self, hint):
        assert self._state.get("current") == BLANVIMDRAN, \
            f"clelvall.blanvimdran: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blanvimdran', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'blanvimdran', _:
                self._state["current"] = SPALDRON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blanvimdran', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blanvimdran',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blanvimdran->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spaldron(self, hint):
        assert self._state.get("current") == SPALDRON, \
            f"clelvall.spaldron: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spaldron', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'spaldron', 1:
                self._state["current"] = SLELCLORR
                self._state["trig"]    = "hint:1"
            case 'spaldron', _:
                self._state["current"] = SKIMKRUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spaldron', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spaldron',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spaldron->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skimkrul(self, hint):
        assert self._state.get("current") == SKIMKRUL, \
            f"clelvall.skimkrul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skimkrul', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'skimkrul', _:
                self._state["current"] = SLELCLORR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skimkrul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skimkrul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skimkrul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slelclorr(self, hint):
        assert self._state.get("current") == SLELCLORR, \
            f"clelvall.slelclorr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slelclorr', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'slelclorr', _:
                self._state["current"] = PRARSLAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slelclorr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slelclorr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slelclorr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prarslax(self, hint):
        assert self._state.get("current") == PRARSLAX, \
            f"clelvall.prarslax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prarslax', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'prarslax', 0:
                self._state["current"] = VAXSKAXKRARX
                self._state["trig"]    = "hint:0"
            case 'prarslax', _:
                self._state["current"] = STORGLELSTURR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prarslax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prarslax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prarslax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _storglelsturr(self, hint):
        assert self._state.get("current") == STORGLELSTURR, \
            f"clelvall.storglelsturr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        _ctx_val_before = self._state["ctx"].get(_CTX_WRITES_KEY, 0)
        match self._state["current"], hint:
            case 'storglelsturr', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'storglelsturr', 1:
                self._state["current"] = KRALBRELKREX
                self._state["trig"]    = "hint:1"
            case 'storglelsturr', _:
                self._state["current"] = VAXSKAXKRARX
                self._state["trig"]    = "auto"
        _old = self._state["ctx"].get(_CTX_WRITES_KEY, 0)
        _inc = 2 if hint == 2 else 1
        self._state["ctx"][_CTX_WRITES_KEY] = _old + _inc
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'storglelsturr', _to, _trig)
        _conds = {"hint_branch": _hint_branch,
                   "ctx_write": True,
                   "ctx_val_before": _ctx_val_before}
        _emit(self._state["cycle"], 1, __name__, 'storglelsturr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"storglelsturr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vaxskaxkrarx(self, hint):
        assert self._state.get("current") == VAXSKAXKRARX, \
            f"clelvall.vaxskaxkrarx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vaxskaxkrarx', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'vaxskaxkrarx', 0:
                self._state["current"] = SPALDRAR
                self._state["trig"]    = "hint:0"
            case 'vaxskaxkrarx', _:
                self._state["current"] = KRALBRELKREX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vaxskaxkrarx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vaxskaxkrarx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vaxskaxkrarx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _kralbrelkrex(self, hint):
        assert self._state.get("current") == KRALBRELKREX, \
            f"clelvall.kralbrelkrex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'kralbrelkrex', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'kralbrelkrex', _:
                self._state["current"] = SPALDRAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'kralbrelkrex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'kralbrelkrex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"kralbrelkrex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spaldrar(self, hint):
        assert self._state.get("current") == SPALDRAR, \
            f"clelvall.spaldrar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spaldrar', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'spaldrar', _:
                self._state["current"] = VELDRIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spaldrar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spaldrar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spaldrar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _veldrim(self, hint):
        assert self._state.get("current") == VELDRIM, \
            f"clelvall.veldrim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'veldrim', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'veldrim', 1:
                self._state["current"] = STORCLENSLUL
                self._state["trig"]    = "hint:1"
            case 'veldrim', _:
                self._state["current"] = VARKRALPRAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'veldrim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'veldrim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"veldrim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _varkralpran(self, hint):
        assert self._state.get("current") == VARKRALPRAN, \
            f"clelvall.varkralpran: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'varkralpran', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'varkralpran', _:
                self._state["current"] = STORCLENSLUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'varkralpran', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'varkralpran',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"varkralpran->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _storclenslul(self, hint):
        assert self._state.get("current") == STORCLENSLUL, \
            f"clelvall.storclenslul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'storclenslul', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'storclenslul', _:
                self._state["current"] = BRULTROSCLUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'storclenslul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'storclenslul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"storclenslul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brultrosclur(self, hint):
        assert self._state.get("current") == BRULTROSCLUR, \
            f"clelvall.brultrosclur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brultrosclur', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'brultrosclur', _:
                self._state["current"] = FLIXVUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brultrosclur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brultrosclur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brultrosclur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flixvul(self, hint):
        assert self._state.get("current") == FLIXVUL, \
            f"clelvall.flixvul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flixvul', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'flixvul', _:
                self._state["current"] = DRIMFLENGRALT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flixvul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flixvul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flixvul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drimflengralt(self, hint):
        assert self._state.get("current") == DRIMFLENGRALT, \
            f"clelvall.drimflengralt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drimflengralt', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'drimflengralt', _:
                self._state["current"] = GREXSKENR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drimflengralt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drimflengralt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drimflengralt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grexskenr(self, hint):
        assert self._state.get("current") == GREXSKENR, \
            f"clelvall.grexskenr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grexskenr', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'grexskenr', _:
                self._state["current"] = PRIXKREXVUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grexskenr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grexskenr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grexskenr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prixkrexvul(self, hint):
        assert self._state.get("current") == PRIXKREXVUL, \
            f"clelvall.prixkrexvul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prixkrexvul', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'prixkrexvul', _:
                self._state["current"] = CLULSLELPRONT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prixkrexvul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prixkrexvul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prixkrexvul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clulslelpront(self, hint):
        assert self._state.get("current") == CLULSLELPRONT, \
            f"clelvall.clulslelpront: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clulslelpront', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'clulslelpront', _:
                self._state["current"] = CLIXKRANBLAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clulslelpront', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clulslelpront',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clulslelpront->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clixkranblan(self, hint):
        assert self._state.get("current") == CLIXKRANBLAN, \
            f"clelvall.clixkranblan: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clixkranblan', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'clixkranblan', 1:
                self._state["current"] = VARPRAXR
                self._state["trig"]    = "hint:1"
            case 'clixkranblan', _:
                self._state["current"] = BRULDRURL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clixkranblan', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clixkranblan',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clixkranblan->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _bruldrurl(self, hint):
        assert self._state.get("current") == BRULDRURL, \
            f"clelvall.bruldrurl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'bruldrurl', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'bruldrurl', 0:
                self._state["current"] = VARPRAXR
                self._state["trig"]    = "hint:0"
            case 'bruldrurl', _:
                self._state["current"] = FLOSGLARVANL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'bruldrurl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'bruldrurl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"bruldrurl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flosglarvanl(self, hint):
        assert self._state.get("current") == FLOSGLARVANL, \
            f"clelvall.flosglarvanl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flosglarvanl', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'flosglarvanl', 1:
                self._state["current"] = PROSSKEXKRON
                self._state["trig"]    = "hint:1"
            case 'flosglarvanl', _:
                self._state["current"] = TRELBLUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flosglarvanl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flosglarvanl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flosglarvanl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trelblur(self, hint):
        assert self._state.get("current") == TRELBLUR, \
            f"clelvall.trelblur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trelblur', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'trelblur', 1:
                self._state["current"] = VARPRAXR
                self._state["trig"]    = "hint:1"
            case 'trelblur', _:
                self._state["current"] = PROSSKEXKRON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trelblur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trelblur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trelblur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prosskexkron(self, hint):
        assert self._state.get("current") == PROSSKEXKRON, \
            f"clelvall.prosskexkron: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prosskexkron', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'prosskexkron', _:
                self._state["current"] = VONKRAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prosskexkron', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prosskexkron',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prosskexkron->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vonkrar(self, hint):
        assert self._state.get("current") == VONKRAR, \
            f"clelvall.vonkrar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vonkrar', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'vonkrar', _:
                self._state["current"] = SLIMVIXCLALX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vonkrar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vonkrar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vonkrar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slimvixclalx(self, hint):
        assert self._state.get("current") == SLIMVIXCLALX, \
            f"clelvall.slimvixclalx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slimvixclalx', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'slimvixclalx', _:
                self._state["current"] = SLAXSKURN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slimvixclalx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slimvixclalx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slimvixclalx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slaxskurn(self, hint):
        assert self._state.get("current") == SLAXSKURN, \
            f"clelvall.slaxskurn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slaxskurn', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'slaxskurn', _:
                self._state["current"] = SKIMDROS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slaxskurn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slaxskurn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slaxskurn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skimdros(self, hint):
        assert self._state.get("current") == SKIMDROS, \
            f"clelvall.skimdros: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skimdros', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'skimdros', _:
                self._state["current"] = BRIMGLIMX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skimdros', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skimdros',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skimdros->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brimglimx(self, hint):
        assert self._state.get("current") == BRIMGLIMX, \
            f"clelvall.brimglimx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brimglimx', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'brimglimx', 1:
                self._state["current"] = GROSGLIX
                self._state["trig"]    = "hint:1"
            case 'brimglimx', _:
                self._state["current"] = GRURSKONPRULK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brimglimx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brimglimx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brimglimx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grurskonprulk(self, hint):
        assert self._state.get("current") == GRURSKONPRULK, \
            f"clelvall.grurskonprulk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grurskonprulk', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'grurskonprulk', 0:
                self._state["current"] = VARPRAXR
                self._state["trig"]    = "hint:0"
            case 'grurskonprulk', _:
                self._state["current"] = GROSGLIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grurskonprulk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grurskonprulk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grurskonprulk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grosglix(self, hint):
        assert self._state.get("current") == GROSGLIX, \
            f"clelvall.grosglix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grosglix', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'grosglix', _:
                self._state["current"] = GRELDRAXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grosglix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grosglix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grosglix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _greldraxr(self, hint):
        assert self._state.get("current") == GRELDRAXR, \
            f"clelvall.greldraxr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'greldraxr', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'greldraxr', 0:
                self._state["current"] = VARPRAXR
                self._state["trig"]    = "hint:0"
            case 'greldraxr', _:
                self._state["current"] = CLENFLORN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'greldraxr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'greldraxr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"greldraxr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clenflorn(self, hint):
        assert self._state.get("current") == CLENFLORN, \
            f"clelvall.clenflorn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clenflorn', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'clenflorn', 0:
                self._state["current"] = VARPRAXR
                self._state["trig"]    = "hint:0"
            case 'clenflorn', _:
                self._state["current"] = KRELGLOS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clenflorn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clenflorn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clenflorn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krelglos(self, hint):
        assert self._state.get("current") == KRELGLOS, \
            f"clelvall.krelglos: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krelglos', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'krelglos', 0:
                self._state["current"] = TRONGLURGLAR
                self._state["trig"]    = "hint:0"
            case 'krelglos', _:
                self._state["current"] = GLORVARDRANT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krelglos', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krelglos',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krelglos->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glorvardrant(self, hint):
        assert self._state.get("current") == GLORVARDRANT, \
            f"clelvall.glorvardrant: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glorvardrant', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'glorvardrant', 0:
                self._state["current"] = VARPRAXR
                self._state["trig"]    = "hint:0"
            case 'glorvardrant', _:
                self._state["current"] = TRONGLURGLAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glorvardrant', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glorvardrant',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glorvardrant->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _tronglurglar(self, hint):
        assert self._state.get("current") == TRONGLURGLAR, \
            f"clelvall.tronglurglar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'tronglurglar', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'tronglurglar', 1:
                self._state["current"] = SPONVIMR
                self._state["trig"]    = "hint:1"
            case 'tronglurglar', _:
                self._state["current"] = KRALSTEXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'tronglurglar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'tronglurglar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"tronglurglar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _kralstexx(self, hint):
        assert self._state.get("current") == KRALSTEXX, \
            f"clelvall.kralstexx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'kralstexx', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'kralstexx', 0:
                self._state["current"] = PROSGLAXT
                self._state["trig"]    = "hint:0"
            case 'kralstexx', _:
                self._state["current"] = SPONVIMR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'kralstexx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'kralstexx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"kralstexx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _sponvimr(self, hint):
        assert self._state.get("current") == SPONVIMR, \
            f"clelvall.sponvimr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'sponvimr', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'sponvimr', _:
                self._state["current"] = PROSGLAXT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'sponvimr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'sponvimr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"sponvimr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prosglaxt(self, hint):
        assert self._state.get("current") == PROSGLAXT, \
            f"clelvall.prosglaxt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prosglaxt', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'prosglaxt', 1:
                self._state["current"] = VARPRAXR
                self._state["trig"]    = "hint:1"
            case 'prosglaxt', _:
                self._state["current"] = BLELFLEL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prosglaxt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prosglaxt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prosglaxt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blelflel(self, hint):
        assert self._state.get("current") == BLELFLEL, \
            f"clelvall.blelflel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blelflel', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'blelflel', _:
                self._state["current"] = BRURPRALT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blelflel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blelflel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blelflel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brurpralt(self, hint):
        assert self._state.get("current") == BRURPRALT, \
            f"clelvall.brurpralt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brurpralt', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'brurpralt', _:
                self._state["current"] = DRURKRAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brurpralt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brurpralt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brurpralt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drurkral(self, hint):
        assert self._state.get("current") == DRURKRAL, \
            f"clelvall.drurkral: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drurkral', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'drurkral', _:
                self._state["current"] = BRORKRALSLANL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drurkral', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drurkral',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drurkral->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brorkralslanl(self, hint):
        assert self._state.get("current") == BRORKRALSLANL, \
            f"clelvall.brorkralslanl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brorkralslanl', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'brorkralslanl', 1:
                self._state["current"] = VARPRAXR
                self._state["trig"]    = "hint:1"
            case 'brorkralslanl', _:
                self._state["current"] = BLULSTENSPUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brorkralslanl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brorkralslanl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brorkralslanl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blulstenspur(self, hint):
        assert self._state.get("current") == BLULSTENSPUR, \
            f"clelvall.blulstenspur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blulstenspur', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'blulstenspur', 0:
                self._state["current"] = VARPRAXR
                self._state["trig"]    = "hint:0"
            case 'blulstenspur', _:
                self._state["current"] = VELCLANSLEXT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blulstenspur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blulstenspur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blulstenspur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _velclanslext(self, hint):
        assert self._state.get("current") == VELCLANSLEXT, \
            f"clelvall.velclanslext: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'velclanslext', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'velclanslext', 1:
                self._state["current"] = TRIXCLALSLENT
                self._state["trig"]    = "hint:1"
            case 'velclanslext', _:
                self._state["current"] = FLELDRIXCLAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'velclanslext', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'velclanslext',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"velclanslext->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _fleldrixclar(self, hint):
        assert self._state.get("current") == FLELDRIXCLAR, \
            f"clelvall.fleldrixclar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'fleldrixclar', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'fleldrixclar', 1:
                self._state["current"] = BLELBLONTROSX
                self._state["trig"]    = "hint:1"
            case 'fleldrixclar', _:
                self._state["current"] = TRIXCLALSLENT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'fleldrixclar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'fleldrixclar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"fleldrixclar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trixclalslent(self, hint):
        assert self._state.get("current") == TRIXCLALSLENT, \
            f"clelvall.trixclalslent: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trixclalslent', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'trixclalslent', 1:
                self._state["current"] = VARPRAXR
                self._state["trig"]    = "hint:1"
            case 'trixclalslent', _:
                self._state["current"] = BLELBLONTROSX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trixclalslent', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trixclalslent',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trixclalslent->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blelblontrosx(self, hint):
        assert self._state.get("current") == BLELBLONTROSX, \
            f"clelvall.blelblontrosx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blelblontrosx', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'blelblontrosx', _:
                self._state["current"] = BRIMBRAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blelblontrosx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blelblontrosx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blelblontrosx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brimbran(self, hint):
        assert self._state.get("current") == BRIMBRAN, \
            f"clelvall.brimbran: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brimbran', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'brimbran', _:
                self._state["current"] = BLIMBRORX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brimbran', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brimbran',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brimbran->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blimbrorx(self, hint):
        assert self._state.get("current") == BLIMBRORX, \
            f"clelvall.blimbrorx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blimbrorx', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'blimbrorx', 1:
                self._state["current"] = STORDROSR
                self._state["trig"]    = "hint:1"
            case 'blimbrorx', _:
                self._state["current"] = CLIXPRENSTIXT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blimbrorx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blimbrorx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blimbrorx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clixprenstixt(self, hint):
        assert self._state.get("current") == CLIXPRENSTIXT, \
            f"clelvall.clixprenstixt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clixprenstixt', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'clixprenstixt', _:
                self._state["current"] = STORDROSR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clixprenstixt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clixprenstixt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clixprenstixt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stordrosr(self, hint):
        assert self._state.get("current") == STORDROSR, \
            f"clelvall.stordrosr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stordrosr', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'stordrosr', _:
                self._state["current"] = GLENBLAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stordrosr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stordrosr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stordrosr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glenblax(self, hint):
        assert self._state.get("current") == GLENBLAX, \
            f"clelvall.glenblax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glenblax', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'glenblax', _:
                self._state["current"] = SPEXSKIXN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glenblax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glenblax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glenblax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spexskixn(self, hint):
        assert self._state.get("current") == SPEXSKIXN, \
            f"clelvall.spexskixn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spexskixn', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'spexskixn', _:
                self._state["current"] = SKIXSPARSKARK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spexskixn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spexskixn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spexskixn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skixsparskark(self, hint):
        assert self._state.get("current") == SKIXSPARSKARK, \
            f"clelvall.skixsparskark: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skixsparskark', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'skixsparskark', 0:
                self._state["current"] = SLIMSLANT
                self._state["trig"]    = "hint:0"
            case 'skixsparskark', _:
                self._state["current"] = CLOSBLIXGRUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skixsparskark', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skixsparskark',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skixsparskark->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _closblixgrul(self, hint):
        assert self._state.get("current") == CLOSBLIXGRUL, \
            f"clelvall.closblixgrul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'closblixgrul', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'closblixgrul', 1:
                self._state["current"] = BRONGLEXN
                self._state["trig"]    = "hint:1"
            case 'closblixgrul', _:
                self._state["current"] = SLIMSLANT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'closblixgrul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'closblixgrul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"closblixgrul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slimslant(self, hint):
        assert self._state.get("current") == SLIMSLANT, \
            f"clelvall.slimslant: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slimslant', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'slimslant', 1:
                self._state["current"] = BRURGLONSKELX
                self._state["trig"]    = "hint:1"
            case 'slimslant', _:
                self._state["current"] = BRONGLEXN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slimslant', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slimslant',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slimslant->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _bronglexn(self, hint):
        assert self._state.get("current") == BRONGLEXN, \
            f"clelvall.bronglexn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'bronglexn', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'bronglexn', 0:
                self._state["current"] = VARPRAXR
                self._state["trig"]    = "hint:0"
            case 'bronglexn', _:
                self._state["current"] = BRURGLONSKELX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'bronglexn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'bronglexn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"bronglexn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brurglonskelx(self, hint):
        assert self._state.get("current") == BRURGLONSKELX, \
            f"clelvall.brurglonskelx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brurglonskelx', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'brurglonskelx', _:
                self._state["current"] = FLURVON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brurglonskelx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brurglonskelx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brurglonskelx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flurvon(self, hint):
        assert self._state.get("current") == FLURVON, \
            f"clelvall.flurvon: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flurvon', 2:
                self._state["current"] = BRARGLOR
                self._state["trig"]    = "hint:2"
            case 'flurvon', 1:
                self._state["current"] = VARPRAXR
                self._state["trig"]    = "hint:1"
            case 'flurvon', _:
                self._state["current"] = KRENSTIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flurvon', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flurvon',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flurvon->{_to}", _xid_val)
        self._state["cycle"] += 1

    def invoke(self, hint=None, span=None, caller=None, ctx=None, cycle=0):
        if ctx is None: ctx = {}

        self._state = {"current": DREXPREN, "ctx": ctx,
                        "span": span, "caller": caller,
                        "trig": "auto", "cycle": cycle}
        _dispatch = {
            DREXPREN: self._drexpren,
            SPALSKAXGRAXT: self._spalskaxgraxt,
            PRIMTRARGLAL: self._primtrarglal,
            FLENPRON: self._flenpron,
            FLANPRANSKELT: self._flanpranskelt,
            PRARGRIX: self._prargrix,
            BLANVIMDRAN: self._blanvimdran,
            SPALDRON: self._spaldron,
            SKIMKRUL: self._skimkrul,
            SLELCLORR: self._slelclorr,
            PRARSLAX: self._prarslax,
            STORGLELSTURR: self._storglelsturr,
            VAXSKAXKRARX: self._vaxskaxkrarx,
            KRALBRELKREX: self._kralbrelkrex,
            SPALDRAR: self._spaldrar,
            VELDRIM: self._veldrim,
            VARKRALPRAN: self._varkralpran,
            STORCLENSLUL: self._storclenslul,
            BRULTROSCLUR: self._brultrosclur,
            FLIXVUL: self._flixvul,
            DRIMFLENGRALT: self._drimflengralt,
            GREXSKENR: self._grexskenr,
            PRIXKREXVUL: self._prixkrexvul,
            CLULSLELPRONT: self._clulslelpront,
            CLIXKRANBLAN: self._clixkranblan,
            BRULDRURL: self._bruldrurl,
            FLOSGLARVANL: self._flosglarvanl,
            TRELBLUR: self._trelblur,
            PROSSKEXKRON: self._prosskexkron,
            VONKRAR: self._vonkrar,
            SLIMVIXCLALX: self._slimvixclalx,
            SLAXSKURN: self._slaxskurn,
            SKIMDROS: self._skimdros,
            BRIMGLIMX: self._brimglimx,
            GRURSKONPRULK: self._grurskonprulk,
            GROSGLIX: self._grosglix,
            GRELDRAXR: self._greldraxr,
            CLENFLORN: self._clenflorn,
            KRELGLOS: self._krelglos,
            GLORVARDRANT: self._glorvardrant,
            TRONGLURGLAR: self._tronglurglar,
            KRALSTEXX: self._kralstexx,
            SPONVIMR: self._sponvimr,
            PROSGLAXT: self._prosglaxt,
            BLELFLEL: self._blelflel,
            BRURPRALT: self._brurpralt,
            DRURKRAL: self._drurkral,
            BRORKRALSLANL: self._brorkralslanl,
            BLULSTENSPUR: self._blulstenspur,
            VELCLANSLEXT: self._velclanslext,
            FLELDRIXCLAR: self._fleldrixclar,
            TRIXCLALSLENT: self._trixclalslent,
            BLELBLONTROSX: self._blelblontrosx,
            BRIMBRAN: self._brimbran,
            BLIMBRORX: self._blimbrorx,
            CLIXPRENSTIXT: self._clixprenstixt,
            STORDROSR: self._stordrosr,
            GLENBLAX: self._glenblax,
            SPEXSKIXN: self._spexskixn,
            SKIXSPARSKARK: self._skixsparskark,
            CLOSBLIXGRUL: self._closblixgrul,
            SLIMSLANT: self._slimslant,
            BRONGLEXN: self._bronglexn,
            BRURGLONSKELX: self._brurglonskelx,
            FLURVON: self._flurvon,
        }
        while self._state["current"] not in _R and self._state["cycle"] - cycle < 8000:
            _dispatch[self._state["current"]](hint)
        _ret     = _R.get(self._state["current"], -1)
        _is_err  = self._state["current"] == BRARGLOR
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
    return ClelvallFSM().invoke(hint=hint, span=span, caller=caller, ctx=ctx, cycle=cycle)
