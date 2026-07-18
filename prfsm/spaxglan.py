from _log import _w as _emit, _xid

DRIXBRIMBROSX = 'drixbrimbrosx'
SPORGLIMSKURK = 'sporglimskurk'
KRONPRENSLAR = 'kronprenslar'
BLULTRORX = 'blultrorx'
SKORSPELKRAR = 'skorspelkrar'
SLURFLEX = 'slurflex'
BRALKRIMT = 'bralkrimt'
FLULGROSVONX = 'flulgrosvonx'
GLURTRENSPUR = 'glurtrenspur'
TRORSTAR = 'trorstar'
STIMSLEXX = 'stimslexx'
CLONGLAN = 'clonglan'
FLANTRALL = 'flantrall'
GRELKRULPRIMN = 'grelkrulprimn'
SPENSPAXPRUL = 'spenspaxprul'
FLURFLARKREN = 'flurflarkren'
STAXSPENGLONX = 'staxspenglonx'
CLIXBRUR = 'clixbrur'
DRIXFLUL = 'drixflul'
KRULPRAN = 'krulpran'
BRIMTRELX = 'brimtrelx'
DRIMVONTRUL = 'drimvontrul'
CLIMVURSKOR = 'climvurskor'
VIXSKALSLURX = 'vixskalslurx'
GLIMFLEX = 'glimflex'
PRANGRIX = 'prangrix'
DRAXGLULR = 'draxglulr'
SPIXFLANCLONT = 'spixflanclont'
CLOSFLIMGREN = 'closflimgren'
BLIMBLARSLUL = 'blimblarslul'
KRULFLELFLELL = 'krulflelflell'
GLEXSTEX = 'glexstex'
CLARTRIMBRURL = 'clartrimbrurl'
PRARSLIMSKANL = 'prarslimskanl'
TRALGLIX = 'tralglix'
GLENTRENT = 'glentrent'
BLAXDRULPRON = 'blaxdrulpron'
FLORBRENN = 'florbrenn'
KRONPRIXBRONK = 'kronprixbronk'
SKAXBLIXX = 'skaxblixx'
KRURDRELSLEL = 'krurdrelslel'
SPANGLOSFLAN = 'spanglosflan'
SPENBRIMSKAXN = 'spenbrimskaxn'
TRIXGLIMKRANR = 'trixglimkranr'
FLANFLENTROS = 'flanflentros'
BRELCLEXK = 'brelclexk'
VALBLUL = 'valblul'
GRIMSKAXKREXL = 'grimskaxkrexl'
SPENGRORBRULK = 'spengrorbrulk'
GROSTRAXBROR = 'grostraxbror'
SKELCLAX = 'skelclax'
SKULBLORGLONT = 'skulblorglont'
TRARKROS = 'trarkros'
GLARSTAXFLOS = 'glarstaxflos'
DRONKRANBLOSK = 'dronkranblosk'
BRONGRAXN = 'brongraxn'
GRANTRELGROS = 'grantrelgros'
SPIMPRALL = 'spimprall'
GRALFLARGLONT = 'gralflarglont'
SPAXBRALKROSL = 'spaxbralkrosl'
PRIMSPULSKELL = 'primspulskell'
GRENPRAX = 'grenprax'
STARGLOSGRON = 'starglosgron'
TRORKROSVOR = 'trorkrosvor'
CLONCLELBLORT = 'clonclelblort'
SLARFLANR = 'slarflanr'
DRAXSPORR = 'draxsporr'
BLIXCLAXBRALN = 'blixclaxbraln'

_R = {
    SLARFLANR: 0,
    DRAXSPORR: 1,
    BLIXCLAXBRALN: 2,
}

_CTX_WRITES_KEY  = 'flurslex'
_CTX_WRITE_STATE = GLURTRENSPUR

class SpaxglanFSM:
    def __init__(self):
        self._state = {}

    def _drixbrimbrosx(self, hint):
        assert self._state.get("current") == DRIXBRIMBROSX, \
            f"spaxglan.drixbrimbrosx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drixbrimbrosx', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'drixbrimbrosx', _:
                self._state["current"] = SPORGLIMSKURK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drixbrimbrosx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drixbrimbrosx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drixbrimbrosx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _sporglimskurk(self, hint):
        assert self._state.get("current") == SPORGLIMSKURK, \
            f"spaxglan.sporglimskurk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'sporglimskurk', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'sporglimskurk', 1:
                self._state["current"] = DRAXSPORR
                self._state["trig"]    = "hint:1"
            case 'sporglimskurk', _:
                self._state["current"] = KRONPRENSLAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'sporglimskurk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'sporglimskurk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"sporglimskurk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _kronprenslar(self, hint):
        assert self._state.get("current") == KRONPRENSLAR, \
            f"spaxglan.kronprenslar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'kronprenslar', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'kronprenslar', _:
                self._state["current"] = BLULTRORX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'kronprenslar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'kronprenslar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"kronprenslar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blultrorx(self, hint):
        assert self._state.get("current") == BLULTRORX, \
            f"spaxglan.blultrorx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blultrorx', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'blultrorx', 1:
                self._state["current"] = DRAXSPORR
                self._state["trig"]    = "hint:1"
            case 'blultrorx', _:
                self._state["current"] = SKORSPELKRAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blultrorx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blultrorx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blultrorx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skorspelkrar(self, hint):
        assert self._state.get("current") == SKORSPELKRAR, \
            f"spaxglan.skorspelkrar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skorspelkrar', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'skorspelkrar', 0:
                self._state["current"] = DRAXSPORR
                self._state["trig"]    = "hint:0"
            case 'skorspelkrar', _:
                self._state["current"] = SLURFLEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skorspelkrar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skorspelkrar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skorspelkrar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slurflex(self, hint):
        assert self._state.get("current") == SLURFLEX, \
            f"spaxglan.slurflex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slurflex', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'slurflex', _:
                self._state["current"] = BRALKRIMT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slurflex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slurflex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slurflex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _bralkrimt(self, hint):
        assert self._state.get("current") == BRALKRIMT, \
            f"spaxglan.bralkrimt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'bralkrimt', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'bralkrimt', _:
                self._state["current"] = FLULGROSVONX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'bralkrimt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'bralkrimt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"bralkrimt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flulgrosvonx(self, hint):
        assert self._state.get("current") == FLULGROSVONX, \
            f"spaxglan.flulgrosvonx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flulgrosvonx', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'flulgrosvonx', _:
                self._state["current"] = GLURTRENSPUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flulgrosvonx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flulgrosvonx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flulgrosvonx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glurtrenspur(self, hint):
        assert self._state.get("current") == GLURTRENSPUR, \
            f"spaxglan.glurtrenspur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        _ctx_val_before = self._state["ctx"].get(_CTX_WRITES_KEY, 0)
        match self._state["current"], hint:
            case 'glurtrenspur', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'glurtrenspur', _:
                self._state["current"] = TRORSTAR
                self._state["trig"]    = "auto"
        _old = self._state["ctx"].get(_CTX_WRITES_KEY, 0)
        _inc = 2 if hint == 2 else 1
        self._state["ctx"][_CTX_WRITES_KEY] = _old + _inc
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glurtrenspur', _to, _trig)
        _conds = {"hint_branch": _hint_branch,
                   "ctx_write": True,
                   "ctx_val_before": _ctx_val_before}
        _emit(self._state["cycle"], 1, __name__, 'glurtrenspur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glurtrenspur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trorstar(self, hint):
        assert self._state.get("current") == TRORSTAR, \
            f"spaxglan.trorstar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trorstar', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'trorstar', _:
                self._state["current"] = STIMSLEXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trorstar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trorstar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trorstar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stimslexx(self, hint):
        assert self._state.get("current") == STIMSLEXX, \
            f"spaxglan.stimslexx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stimslexx', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'stimslexx', 1:
                self._state["current"] = DRAXSPORR
                self._state["trig"]    = "hint:1"
            case 'stimslexx', _:
                self._state["current"] = CLONGLAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stimslexx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stimslexx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stimslexx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clonglan(self, hint):
        assert self._state.get("current") == CLONGLAN, \
            f"spaxglan.clonglan: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clonglan', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'clonglan', _:
                self._state["current"] = FLANTRALL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clonglan', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clonglan',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clonglan->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flantrall(self, hint):
        assert self._state.get("current") == FLANTRALL, \
            f"spaxglan.flantrall: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flantrall', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'flantrall', _:
                self._state["current"] = GRELKRULPRIMN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flantrall', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flantrall',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flantrall->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grelkrulprimn(self, hint):
        assert self._state.get("current") == GRELKRULPRIMN, \
            f"spaxglan.grelkrulprimn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grelkrulprimn', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'grelkrulprimn', 1:
                self._state["current"] = DRAXSPORR
                self._state["trig"]    = "hint:1"
            case 'grelkrulprimn', _:
                self._state["current"] = SPENSPAXPRUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grelkrulprimn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grelkrulprimn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grelkrulprimn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spenspaxprul(self, hint):
        assert self._state.get("current") == SPENSPAXPRUL, \
            f"spaxglan.spenspaxprul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spenspaxprul', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'spenspaxprul', 1:
                self._state["current"] = STAXSPENGLONX
                self._state["trig"]    = "hint:1"
            case 'spenspaxprul', _:
                self._state["current"] = FLURFLARKREN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spenspaxprul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spenspaxprul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spenspaxprul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flurflarkren(self, hint):
        assert self._state.get("current") == FLURFLARKREN, \
            f"spaxglan.flurflarkren: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flurflarkren', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'flurflarkren', 0:
                self._state["current"] = DRAXSPORR
                self._state["trig"]    = "hint:0"
            case 'flurflarkren', _:
                self._state["current"] = STAXSPENGLONX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flurflarkren', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flurflarkren',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flurflarkren->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _staxspenglonx(self, hint):
        assert self._state.get("current") == STAXSPENGLONX, \
            f"spaxglan.staxspenglonx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'staxspenglonx', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'staxspenglonx', 0:
                self._state["current"] = DRAXSPORR
                self._state["trig"]    = "hint:0"
            case 'staxspenglonx', _:
                self._state["current"] = CLIXBRUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'staxspenglonx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'staxspenglonx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"staxspenglonx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clixbrur(self, hint):
        assert self._state.get("current") == CLIXBRUR, \
            f"spaxglan.clixbrur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clixbrur', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'clixbrur', _:
                self._state["current"] = DRIXFLUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clixbrur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clixbrur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clixbrur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drixflul(self, hint):
        assert self._state.get("current") == DRIXFLUL, \
            f"spaxglan.drixflul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drixflul', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'drixflul', 0:
                self._state["current"] = DRAXSPORR
                self._state["trig"]    = "hint:0"
            case 'drixflul', _:
                self._state["current"] = KRULPRAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drixflul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drixflul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drixflul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krulpran(self, hint):
        assert self._state.get("current") == KRULPRAN, \
            f"spaxglan.krulpran: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krulpran', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'krulpran', _:
                self._state["current"] = BRIMTRELX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krulpran', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krulpran',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krulpran->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brimtrelx(self, hint):
        assert self._state.get("current") == BRIMTRELX, \
            f"spaxglan.brimtrelx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brimtrelx', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'brimtrelx', _:
                self._state["current"] = DRIMVONTRUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brimtrelx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brimtrelx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brimtrelx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drimvontrul(self, hint):
        assert self._state.get("current") == DRIMVONTRUL, \
            f"spaxglan.drimvontrul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drimvontrul', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'drimvontrul', _:
                self._state["current"] = CLIMVURSKOR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drimvontrul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drimvontrul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drimvontrul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _climvurskor(self, hint):
        assert self._state.get("current") == CLIMVURSKOR, \
            f"spaxglan.climvurskor: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'climvurskor', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'climvurskor', _:
                self._state["current"] = VIXSKALSLURX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'climvurskor', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'climvurskor',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"climvurskor->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vixskalslurx(self, hint):
        assert self._state.get("current") == VIXSKALSLURX, \
            f"spaxglan.vixskalslurx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vixskalslurx', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'vixskalslurx', 1:
                self._state["current"] = DRAXSPORR
                self._state["trig"]    = "hint:1"
            case 'vixskalslurx', _:
                self._state["current"] = GLIMFLEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vixskalslurx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vixskalslurx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vixskalslurx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glimflex(self, hint):
        assert self._state.get("current") == GLIMFLEX, \
            f"spaxglan.glimflex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glimflex', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'glimflex', 1:
                self._state["current"] = DRAXSPORR
                self._state["trig"]    = "hint:1"
            case 'glimflex', _:
                self._state["current"] = PRANGRIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glimflex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glimflex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glimflex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prangrix(self, hint):
        assert self._state.get("current") == PRANGRIX, \
            f"spaxglan.prangrix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prangrix', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'prangrix', 0:
                self._state["current"] = DRAXSPORR
                self._state["trig"]    = "hint:0"
            case 'prangrix', _:
                self._state["current"] = DRAXGLULR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prangrix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prangrix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prangrix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _draxglulr(self, hint):
        assert self._state.get("current") == DRAXGLULR, \
            f"spaxglan.draxglulr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'draxglulr', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'draxglulr', _:
                self._state["current"] = SPIXFLANCLONT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'draxglulr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'draxglulr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"draxglulr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spixflanclont(self, hint):
        assert self._state.get("current") == SPIXFLANCLONT, \
            f"spaxglan.spixflanclont: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spixflanclont', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'spixflanclont', _:
                self._state["current"] = CLOSFLIMGREN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spixflanclont', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spixflanclont',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spixflanclont->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _closflimgren(self, hint):
        assert self._state.get("current") == CLOSFLIMGREN, \
            f"spaxglan.closflimgren: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'closflimgren', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'closflimgren', _:
                self._state["current"] = BLIMBLARSLUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'closflimgren', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'closflimgren',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"closflimgren->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blimblarslul(self, hint):
        assert self._state.get("current") == BLIMBLARSLUL, \
            f"spaxglan.blimblarslul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blimblarslul', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'blimblarslul', _:
                self._state["current"] = KRULFLELFLELL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blimblarslul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blimblarslul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blimblarslul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krulflelflell(self, hint):
        assert self._state.get("current") == KRULFLELFLELL, \
            f"spaxglan.krulflelflell: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krulflelflell', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'krulflelflell', _:
                self._state["current"] = GLEXSTEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krulflelflell', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krulflelflell',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krulflelflell->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glexstex(self, hint):
        assert self._state.get("current") == GLEXSTEX, \
            f"spaxglan.glexstex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glexstex', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'glexstex', 1:
                self._state["current"] = DRAXSPORR
                self._state["trig"]    = "hint:1"
            case 'glexstex', _:
                self._state["current"] = CLARTRIMBRURL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glexstex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glexstex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glexstex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clartrimbrurl(self, hint):
        assert self._state.get("current") == CLARTRIMBRURL, \
            f"spaxglan.clartrimbrurl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clartrimbrurl', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'clartrimbrurl', 0:
                self._state["current"] = TRALGLIX
                self._state["trig"]    = "hint:0"
            case 'clartrimbrurl', _:
                self._state["current"] = PRARSLIMSKANL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clartrimbrurl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clartrimbrurl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clartrimbrurl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prarslimskanl(self, hint):
        assert self._state.get("current") == PRARSLIMSKANL, \
            f"spaxglan.prarslimskanl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prarslimskanl', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'prarslimskanl', 0:
                self._state["current"] = DRAXSPORR
                self._state["trig"]    = "hint:0"
            case 'prarslimskanl', _:
                self._state["current"] = TRALGLIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prarslimskanl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prarslimskanl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prarslimskanl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _tralglix(self, hint):
        assert self._state.get("current") == TRALGLIX, \
            f"spaxglan.tralglix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'tralglix', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'tralglix', _:
                self._state["current"] = GLENTRENT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'tralglix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'tralglix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"tralglix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glentrent(self, hint):
        assert self._state.get("current") == GLENTRENT, \
            f"spaxglan.glentrent: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glentrent', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'glentrent', 1:
                self._state["current"] = FLORBRENN
                self._state["trig"]    = "hint:1"
            case 'glentrent', _:
                self._state["current"] = BLAXDRULPRON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glentrent', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glentrent',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glentrent->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blaxdrulpron(self, hint):
        assert self._state.get("current") == BLAXDRULPRON, \
            f"spaxglan.blaxdrulpron: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blaxdrulpron', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'blaxdrulpron', 0:
                self._state["current"] = KRONPRIXBRONK
                self._state["trig"]    = "hint:0"
            case 'blaxdrulpron', _:
                self._state["current"] = FLORBRENN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blaxdrulpron', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blaxdrulpron',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blaxdrulpron->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _florbrenn(self, hint):
        assert self._state.get("current") == FLORBRENN, \
            f"spaxglan.florbrenn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'florbrenn', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'florbrenn', _:
                self._state["current"] = KRONPRIXBRONK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'florbrenn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'florbrenn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"florbrenn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _kronprixbronk(self, hint):
        assert self._state.get("current") == KRONPRIXBRONK, \
            f"spaxglan.kronprixbronk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'kronprixbronk', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'kronprixbronk', 0:
                self._state["current"] = DRAXSPORR
                self._state["trig"]    = "hint:0"
            case 'kronprixbronk', _:
                self._state["current"] = SKAXBLIXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'kronprixbronk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'kronprixbronk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"kronprixbronk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skaxblixx(self, hint):
        assert self._state.get("current") == SKAXBLIXX, \
            f"spaxglan.skaxblixx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skaxblixx', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'skaxblixx', 1:
                self._state["current"] = SPANGLOSFLAN
                self._state["trig"]    = "hint:1"
            case 'skaxblixx', _:
                self._state["current"] = KRURDRELSLEL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skaxblixx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skaxblixx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skaxblixx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krurdrelslel(self, hint):
        assert self._state.get("current") == KRURDRELSLEL, \
            f"spaxglan.krurdrelslel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krurdrelslel', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'krurdrelslel', 0:
                self._state["current"] = SPENBRIMSKAXN
                self._state["trig"]    = "hint:0"
            case 'krurdrelslel', _:
                self._state["current"] = SPANGLOSFLAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krurdrelslel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krurdrelslel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krurdrelslel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spanglosflan(self, hint):
        assert self._state.get("current") == SPANGLOSFLAN, \
            f"spaxglan.spanglosflan: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spanglosflan', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'spanglosflan', 1:
                self._state["current"] = DRAXSPORR
                self._state["trig"]    = "hint:1"
            case 'spanglosflan', _:
                self._state["current"] = SPENBRIMSKAXN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spanglosflan', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spanglosflan',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spanglosflan->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spenbrimskaxn(self, hint):
        assert self._state.get("current") == SPENBRIMSKAXN, \
            f"spaxglan.spenbrimskaxn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spenbrimskaxn', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'spenbrimskaxn', 1:
                self._state["current"] = DRAXSPORR
                self._state["trig"]    = "hint:1"
            case 'spenbrimskaxn', _:
                self._state["current"] = TRIXGLIMKRANR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spenbrimskaxn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spenbrimskaxn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spenbrimskaxn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trixglimkranr(self, hint):
        assert self._state.get("current") == TRIXGLIMKRANR, \
            f"spaxglan.trixglimkranr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trixglimkranr', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'trixglimkranr', 0:
                self._state["current"] = DRAXSPORR
                self._state["trig"]    = "hint:0"
            case 'trixglimkranr', _:
                self._state["current"] = FLANFLENTROS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trixglimkranr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trixglimkranr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trixglimkranr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flanflentros(self, hint):
        assert self._state.get("current") == FLANFLENTROS, \
            f"spaxglan.flanflentros: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flanflentros', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'flanflentros', 0:
                self._state["current"] = VALBLUL
                self._state["trig"]    = "hint:0"
            case 'flanflentros', _:
                self._state["current"] = BRELCLEXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flanflentros', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flanflentros',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flanflentros->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brelclexk(self, hint):
        assert self._state.get("current") == BRELCLEXK, \
            f"spaxglan.brelclexk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brelclexk', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'brelclexk', 1:
                self._state["current"] = GRIMSKAXKREXL
                self._state["trig"]    = "hint:1"
            case 'brelclexk', _:
                self._state["current"] = VALBLUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brelclexk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brelclexk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brelclexk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _valblul(self, hint):
        assert self._state.get("current") == VALBLUL, \
            f"spaxglan.valblul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'valblul', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'valblul', _:
                self._state["current"] = GRIMSKAXKREXL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'valblul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'valblul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"valblul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grimskaxkrexl(self, hint):
        assert self._state.get("current") == GRIMSKAXKREXL, \
            f"spaxglan.grimskaxkrexl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grimskaxkrexl', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'grimskaxkrexl', 1:
                self._state["current"] = DRAXSPORR
                self._state["trig"]    = "hint:1"
            case 'grimskaxkrexl', _:
                self._state["current"] = SPENGRORBRULK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grimskaxkrexl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grimskaxkrexl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grimskaxkrexl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spengrorbrulk(self, hint):
        assert self._state.get("current") == SPENGRORBRULK, \
            f"spaxglan.spengrorbrulk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spengrorbrulk', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'spengrorbrulk', _:
                self._state["current"] = GROSTRAXBROR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spengrorbrulk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spengrorbrulk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spengrorbrulk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grostraxbror(self, hint):
        assert self._state.get("current") == GROSTRAXBROR, \
            f"spaxglan.grostraxbror: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grostraxbror', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'grostraxbror', 0:
                self._state["current"] = DRAXSPORR
                self._state["trig"]    = "hint:0"
            case 'grostraxbror', _:
                self._state["current"] = SKELCLAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grostraxbror', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grostraxbror',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grostraxbror->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skelclax(self, hint):
        assert self._state.get("current") == SKELCLAX, \
            f"spaxglan.skelclax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skelclax', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'skelclax', _:
                self._state["current"] = SKULBLORGLONT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skelclax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skelclax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skelclax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skulblorglont(self, hint):
        assert self._state.get("current") == SKULBLORGLONT, \
            f"spaxglan.skulblorglont: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skulblorglont', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'skulblorglont', 0:
                self._state["current"] = GLARSTAXFLOS
                self._state["trig"]    = "hint:0"
            case 'skulblorglont', _:
                self._state["current"] = TRARKROS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skulblorglont', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skulblorglont',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skulblorglont->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trarkros(self, hint):
        assert self._state.get("current") == TRARKROS, \
            f"spaxglan.trarkros: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trarkros', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'trarkros', 0:
                self._state["current"] = DRONKRANBLOSK
                self._state["trig"]    = "hint:0"
            case 'trarkros', _:
                self._state["current"] = GLARSTAXFLOS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trarkros', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trarkros',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trarkros->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glarstaxflos(self, hint):
        assert self._state.get("current") == GLARSTAXFLOS, \
            f"spaxglan.glarstaxflos: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glarstaxflos', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'glarstaxflos', 1:
                self._state["current"] = DRAXSPORR
                self._state["trig"]    = "hint:1"
            case 'glarstaxflos', _:
                self._state["current"] = DRONKRANBLOSK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glarstaxflos', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glarstaxflos',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glarstaxflos->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _dronkranblosk(self, hint):
        assert self._state.get("current") == DRONKRANBLOSK, \
            f"spaxglan.dronkranblosk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'dronkranblosk', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'dronkranblosk', 0:
                self._state["current"] = GRANTRELGROS
                self._state["trig"]    = "hint:0"
            case 'dronkranblosk', _:
                self._state["current"] = BRONGRAXN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'dronkranblosk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'dronkranblosk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"dronkranblosk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brongraxn(self, hint):
        assert self._state.get("current") == BRONGRAXN, \
            f"spaxglan.brongraxn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brongraxn', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'brongraxn', 1:
                self._state["current"] = SPIMPRALL
                self._state["trig"]    = "hint:1"
            case 'brongraxn', _:
                self._state["current"] = GRANTRELGROS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brongraxn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brongraxn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brongraxn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grantrelgros(self, hint):
        assert self._state.get("current") == GRANTRELGROS, \
            f"spaxglan.grantrelgros: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grantrelgros', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'grantrelgros', 0:
                self._state["current"] = GRALFLARGLONT
                self._state["trig"]    = "hint:0"
            case 'grantrelgros', _:
                self._state["current"] = SPIMPRALL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grantrelgros', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grantrelgros',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grantrelgros->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spimprall(self, hint):
        assert self._state.get("current") == SPIMPRALL, \
            f"spaxglan.spimprall: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spimprall', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'spimprall', _:
                self._state["current"] = GRALFLARGLONT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spimprall', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spimprall',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spimprall->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _gralflarglont(self, hint):
        assert self._state.get("current") == GRALFLARGLONT, \
            f"spaxglan.gralflarglont: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'gralflarglont', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'gralflarglont', 1:
                self._state["current"] = DRAXSPORR
                self._state["trig"]    = "hint:1"
            case 'gralflarglont', _:
                self._state["current"] = SPAXBRALKROSL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'gralflarglont', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'gralflarglont',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"gralflarglont->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spaxbralkrosl(self, hint):
        assert self._state.get("current") == SPAXBRALKROSL, \
            f"spaxglan.spaxbralkrosl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spaxbralkrosl', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'spaxbralkrosl', 1:
                self._state["current"] = GRENPRAX
                self._state["trig"]    = "hint:1"
            case 'spaxbralkrosl', _:
                self._state["current"] = PRIMSPULSKELL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spaxbralkrosl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spaxbralkrosl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spaxbralkrosl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _primspulskell(self, hint):
        assert self._state.get("current") == PRIMSPULSKELL, \
            f"spaxglan.primspulskell: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'primspulskell', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'primspulskell', 0:
                self._state["current"] = STARGLOSGRON
                self._state["trig"]    = "hint:0"
            case 'primspulskell', _:
                self._state["current"] = GRENPRAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'primspulskell', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'primspulskell',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"primspulskell->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grenprax(self, hint):
        assert self._state.get("current") == GRENPRAX, \
            f"spaxglan.grenprax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grenprax', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'grenprax', _:
                self._state["current"] = STARGLOSGRON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grenprax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grenprax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grenprax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _starglosgron(self, hint):
        assert self._state.get("current") == STARGLOSGRON, \
            f"spaxglan.starglosgron: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'starglosgron', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'starglosgron', _:
                self._state["current"] = TRORKROSVOR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'starglosgron', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'starglosgron',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"starglosgron->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trorkrosvor(self, hint):
        assert self._state.get("current") == TRORKROSVOR, \
            f"spaxglan.trorkrosvor: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trorkrosvor', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'trorkrosvor', _:
                self._state["current"] = CLONCLELBLORT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trorkrosvor', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trorkrosvor',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trorkrosvor->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clonclelblort(self, hint):
        assert self._state.get("current") == CLONCLELBLORT, \
            f"spaxglan.clonclelblort: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clonclelblort', 2:
                self._state["current"] = BLIXCLAXBRALN
                self._state["trig"]    = "hint:2"
            case 'clonclelblort', _:
                self._state["current"] = SLARFLANR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clonclelblort', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clonclelblort',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clonclelblort->{_to}", _xid_val)
        self._state["cycle"] += 1

    def invoke(self, hint=None, span=None, caller=None, ctx=None, cycle=0):
        if ctx is None: ctx = {}

        self._state = {"current": DRIXBRIMBROSX, "ctx": ctx,
                        "span": span, "caller": caller,
                        "trig": "auto", "cycle": cycle}
        _dispatch = {
            DRIXBRIMBROSX: self._drixbrimbrosx,
            SPORGLIMSKURK: self._sporglimskurk,
            KRONPRENSLAR: self._kronprenslar,
            BLULTRORX: self._blultrorx,
            SKORSPELKRAR: self._skorspelkrar,
            SLURFLEX: self._slurflex,
            BRALKRIMT: self._bralkrimt,
            FLULGROSVONX: self._flulgrosvonx,
            GLURTRENSPUR: self._glurtrenspur,
            TRORSTAR: self._trorstar,
            STIMSLEXX: self._stimslexx,
            CLONGLAN: self._clonglan,
            FLANTRALL: self._flantrall,
            GRELKRULPRIMN: self._grelkrulprimn,
            SPENSPAXPRUL: self._spenspaxprul,
            FLURFLARKREN: self._flurflarkren,
            STAXSPENGLONX: self._staxspenglonx,
            CLIXBRUR: self._clixbrur,
            DRIXFLUL: self._drixflul,
            KRULPRAN: self._krulpran,
            BRIMTRELX: self._brimtrelx,
            DRIMVONTRUL: self._drimvontrul,
            CLIMVURSKOR: self._climvurskor,
            VIXSKALSLURX: self._vixskalslurx,
            GLIMFLEX: self._glimflex,
            PRANGRIX: self._prangrix,
            DRAXGLULR: self._draxglulr,
            SPIXFLANCLONT: self._spixflanclont,
            CLOSFLIMGREN: self._closflimgren,
            BLIMBLARSLUL: self._blimblarslul,
            KRULFLELFLELL: self._krulflelflell,
            GLEXSTEX: self._glexstex,
            CLARTRIMBRURL: self._clartrimbrurl,
            PRARSLIMSKANL: self._prarslimskanl,
            TRALGLIX: self._tralglix,
            GLENTRENT: self._glentrent,
            BLAXDRULPRON: self._blaxdrulpron,
            FLORBRENN: self._florbrenn,
            KRONPRIXBRONK: self._kronprixbronk,
            SKAXBLIXX: self._skaxblixx,
            KRURDRELSLEL: self._krurdrelslel,
            SPANGLOSFLAN: self._spanglosflan,
            SPENBRIMSKAXN: self._spenbrimskaxn,
            TRIXGLIMKRANR: self._trixglimkranr,
            FLANFLENTROS: self._flanflentros,
            BRELCLEXK: self._brelclexk,
            VALBLUL: self._valblul,
            GRIMSKAXKREXL: self._grimskaxkrexl,
            SPENGRORBRULK: self._spengrorbrulk,
            GROSTRAXBROR: self._grostraxbror,
            SKELCLAX: self._skelclax,
            SKULBLORGLONT: self._skulblorglont,
            TRARKROS: self._trarkros,
            GLARSTAXFLOS: self._glarstaxflos,
            DRONKRANBLOSK: self._dronkranblosk,
            BRONGRAXN: self._brongraxn,
            GRANTRELGROS: self._grantrelgros,
            SPIMPRALL: self._spimprall,
            GRALFLARGLONT: self._gralflarglont,
            SPAXBRALKROSL: self._spaxbralkrosl,
            PRIMSPULSKELL: self._primspulskell,
            GRENPRAX: self._grenprax,
            STARGLOSGRON: self._starglosgron,
            TRORKROSVOR: self._trorkrosvor,
            CLONCLELBLORT: self._clonclelblort,
        }
        while self._state["current"] not in _R and self._state["cycle"] - cycle < 8000:
            _dispatch[self._state["current"]](hint)
        _ret     = _R.get(self._state["current"], -1)
        _is_err  = self._state["current"] == BLIXCLAXBRALN
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
    return SpaxglanFSM().invoke(hint=hint, span=span, caller=caller, ctx=ctx, cycle=cycle)
