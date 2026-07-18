from _log import _w as _emit, _xid

SLULSLEN = 'slulslen'
TROSCLOST = 'trosclost'
FLALSKIM = 'flalskim'
BRELBLIMDRUR = 'brelblimdrur'
SKIMCLULGLON = 'skimclulglon'
BLORDRORBLAXL = 'blordrorblaxl'
BREXGRON = 'brexgron'
FLULBRALBLAX = 'flulbralblax'
GRARCLEN = 'grarclen'
PRIMVOS = 'primvos'
CLURPRIXR = 'clurprixr'
PRONGRURPRELX = 'prongrurprelx'
TRANSLULSLAXX = 'translulslaxx'
BLOSSLORSLAR = 'blosslorslar'
GLANSTOSDROS = 'glanstosdros'
BRONTROSGRONT = 'brontrosgront'
CLAXFLELN = 'claxfleln'
BRONVURVAL = 'bronvurval'
GLALKRANTRIX = 'glalkrantrix'
SPELDRORBLEX = 'speldrorblex'
SKIMPRUL = 'skimprul'
BRARSKONKRAXN = 'brarskonkraxn'
GLAXBLELTRENR = 'glaxbleltrenr'
VANSLEX = 'vanslex'
SLELBRIXX = 'slelbrixx'
TRIMTRIMT = 'trimtrimt'
KRIMDRANCLEXR = 'krimdranclexr'
DRIXCLIXBLOS = 'drixclixblos'
STONBRULKRUL = 'stonbrulkrul'
SKAXCLALX = 'skaxclalx'
GLORVAXSTIX = 'glorvaxstix'
GRIMPRALT = 'grimpralt'
KROSGRONTRALR = 'krosgrontralr'
CLIMSTELDREXL = 'climsteldrexl'
BRENSPAL = 'brenspal'
VAXFLIMR = 'vaxflimr'
KREXVIMKRAXR = 'krexvimkraxr'
SLARKRELGRONX = 'slarkrelgronx'
DRENVORBROS = 'drenvorbros'
CLENSLULSTAX = 'clenslulstax'
FLENTRORGRON = 'flentrorgron'
FLOSSLAL = 'flosslal'
VIXKRANBLORL = 'vixkranblorl'
CLARTREL = 'clartrel'
VARGRONFLART = 'vargronflart'
DRENDRIX = 'drendrix'
SKORCLEX = 'skorclex'
SPANFLUR = 'spanflur'
SLELBLURBRALL = 'slelblurbrall'
STALPRELN = 'stalpreln'
SKENKRANK = 'skenkrank'
BRALSTIMPRANT = 'bralstimprant'
GRONCLURSPORT = 'gronclursport'
GRURVONDREX = 'grurvondrex'
DRULSTORBLUR = 'drulstorblur'
VOSBLORR = 'vosblorr'
PRURPRORDRAXR = 'prurprordraxr'
SLALSPORGRALL = 'slalsporgrall'
BRARSLULN = 'brarsluln'
DRURTRURGRIMK = 'drurtrurgrimk'
DRANFLENBRALK = 'dranflenbralk'
SLARFLAL = 'slarflal'
STARTREL = 'startrel'
STORKRALSLAX = 'storkralslax'
STIMVEXDRANN = 'stimvexdrann'
TRELBRALCLIM = 'trelbralclim'
STIMDRURFLANK = 'stimdrurflank'
KRURKROSTRANK = 'krurkrostrank'

_R = {
    TRELBRALCLIM: 0,
    STIMDRURFLANK: 1,
    KRURKROSTRANK: 2,
}

_CTX_WRITES_KEY  = 'flurslex'
_CTX_WRITE_STATE = BLOSSLORSLAR

class BralskenlFSM:
    def __init__(self):
        self._state = {}

    def _slulslen(self, hint):
        assert self._state.get("current") == SLULSLEN, \
            f"bralskenl.slulslen: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slulslen', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'slulslen', 1:
                self._state["current"] = STIMDRURFLANK
                self._state["trig"]    = "hint:1"
            case 'slulslen', _:
                self._state["current"] = TROSCLOST
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slulslen', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slulslen',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slulslen->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trosclost(self, hint):
        assert self._state.get("current") == TROSCLOST, \
            f"bralskenl.trosclost: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trosclost', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'trosclost', _:
                self._state["current"] = FLALSKIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trosclost', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trosclost',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trosclost->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flalskim(self, hint):
        assert self._state.get("current") == FLALSKIM, \
            f"bralskenl.flalskim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flalskim', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'flalskim', 0:
                self._state["current"] = SKIMCLULGLON
                self._state["trig"]    = "hint:0"
            case 'flalskim', _:
                self._state["current"] = BRELBLIMDRUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flalskim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flalskim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flalskim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brelblimdrur(self, hint):
        assert self._state.get("current") == BRELBLIMDRUR, \
            f"bralskenl.brelblimdrur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brelblimdrur', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'brelblimdrur', 1:
                self._state["current"] = BLORDRORBLAXL
                self._state["trig"]    = "hint:1"
            case 'brelblimdrur', _:
                self._state["current"] = SKIMCLULGLON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brelblimdrur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brelblimdrur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brelblimdrur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skimclulglon(self, hint):
        assert self._state.get("current") == SKIMCLULGLON, \
            f"bralskenl.skimclulglon: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skimclulglon', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'skimclulglon', 0:
                self._state["current"] = BREXGRON
                self._state["trig"]    = "hint:0"
            case 'skimclulglon', _:
                self._state["current"] = BLORDRORBLAXL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skimclulglon', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skimclulglon',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skimclulglon->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blordrorblaxl(self, hint):
        assert self._state.get("current") == BLORDRORBLAXL, \
            f"bralskenl.blordrorblaxl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blordrorblaxl', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'blordrorblaxl', 0:
                self._state["current"] = FLULBRALBLAX
                self._state["trig"]    = "hint:0"
            case 'blordrorblaxl', _:
                self._state["current"] = BREXGRON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blordrorblaxl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blordrorblaxl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blordrorblaxl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brexgron(self, hint):
        assert self._state.get("current") == BREXGRON, \
            f"bralskenl.brexgron: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brexgron', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'brexgron', _:
                self._state["current"] = FLULBRALBLAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brexgron', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brexgron',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brexgron->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flulbralblax(self, hint):
        assert self._state.get("current") == FLULBRALBLAX, \
            f"bralskenl.flulbralblax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flulbralblax', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'flulbralblax', 1:
                self._state["current"] = STIMDRURFLANK
                self._state["trig"]    = "hint:1"
            case 'flulbralblax', _:
                self._state["current"] = GRARCLEN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flulbralblax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flulbralblax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flulbralblax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grarclen(self, hint):
        assert self._state.get("current") == GRARCLEN, \
            f"bralskenl.grarclen: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grarclen', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'grarclen', 1:
                self._state["current"] = STIMDRURFLANK
                self._state["trig"]    = "hint:1"
            case 'grarclen', _:
                self._state["current"] = PRIMVOS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grarclen', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grarclen',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grarclen->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _primvos(self, hint):
        assert self._state.get("current") == PRIMVOS, \
            f"bralskenl.primvos: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'primvos', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'primvos', _:
                self._state["current"] = CLURPRIXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'primvos', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'primvos',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"primvos->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clurprixr(self, hint):
        assert self._state.get("current") == CLURPRIXR, \
            f"bralskenl.clurprixr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clurprixr', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'clurprixr', 0:
                self._state["current"] = TRANSLULSLAXX
                self._state["trig"]    = "hint:0"
            case 'clurprixr', _:
                self._state["current"] = PRONGRURPRELX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clurprixr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clurprixr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clurprixr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prongrurprelx(self, hint):
        assert self._state.get("current") == PRONGRURPRELX, \
            f"bralskenl.prongrurprelx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prongrurprelx', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'prongrurprelx', 0:
                self._state["current"] = BLOSSLORSLAR
                self._state["trig"]    = "hint:0"
            case 'prongrurprelx', _:
                self._state["current"] = TRANSLULSLAXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prongrurprelx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prongrurprelx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prongrurprelx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _translulslaxx(self, hint):
        assert self._state.get("current") == TRANSLULSLAXX, \
            f"bralskenl.translulslaxx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'translulslaxx', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'translulslaxx', _:
                self._state["current"] = BLOSSLORSLAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'translulslaxx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'translulslaxx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"translulslaxx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blosslorslar(self, hint):
        assert self._state.get("current") == BLOSSLORSLAR, \
            f"bralskenl.blosslorslar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        _ctx_val_before = self._state["ctx"].get(_CTX_WRITES_KEY, 0)
        match self._state["current"], hint:
            case 'blosslorslar', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'blosslorslar', 0:
                self._state["current"] = BRONTROSGRONT
                self._state["trig"]    = "hint:0"
            case 'blosslorslar', _:
                self._state["current"] = GLANSTOSDROS
                self._state["trig"]    = "auto"
        _old = self._state["ctx"].get(_CTX_WRITES_KEY, 0)
        _inc = 2 if hint == 2 else 1
        self._state["ctx"][_CTX_WRITES_KEY] = _old + _inc
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blosslorslar', _to, _trig)
        _conds = {"hint_branch": _hint_branch,
                   "ctx_write": True,
                   "ctx_val_before": _ctx_val_before}
        _emit(self._state["cycle"], 1, __name__, 'blosslorslar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blosslorslar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glanstosdros(self, hint):
        assert self._state.get("current") == GLANSTOSDROS, \
            f"bralskenl.glanstosdros: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glanstosdros', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'glanstosdros', 0:
                self._state["current"] = CLAXFLELN
                self._state["trig"]    = "hint:0"
            case 'glanstosdros', _:
                self._state["current"] = BRONTROSGRONT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glanstosdros', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glanstosdros',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glanstosdros->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brontrosgront(self, hint):
        assert self._state.get("current") == BRONTROSGRONT, \
            f"bralskenl.brontrosgront: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brontrosgront', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'brontrosgront', 1:
                self._state["current"] = BRONVURVAL
                self._state["trig"]    = "hint:1"
            case 'brontrosgront', _:
                self._state["current"] = CLAXFLELN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brontrosgront', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brontrosgront',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brontrosgront->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _claxfleln(self, hint):
        assert self._state.get("current") == CLAXFLELN, \
            f"bralskenl.claxfleln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'claxfleln', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'claxfleln', 0:
                self._state["current"] = GLALKRANTRIX
                self._state["trig"]    = "hint:0"
            case 'claxfleln', _:
                self._state["current"] = BRONVURVAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'claxfleln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'claxfleln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"claxfleln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _bronvurval(self, hint):
        assert self._state.get("current") == BRONVURVAL, \
            f"bralskenl.bronvurval: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'bronvurval', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'bronvurval', 0:
                self._state["current"] = STIMDRURFLANK
                self._state["trig"]    = "hint:0"
            case 'bronvurval', _:
                self._state["current"] = GLALKRANTRIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'bronvurval', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'bronvurval',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"bronvurval->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glalkrantrix(self, hint):
        assert self._state.get("current") == GLALKRANTRIX, \
            f"bralskenl.glalkrantrix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glalkrantrix', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'glalkrantrix', _:
                self._state["current"] = SPELDRORBLEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glalkrantrix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glalkrantrix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glalkrantrix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _speldrorblex(self, hint):
        assert self._state.get("current") == SPELDRORBLEX, \
            f"bralskenl.speldrorblex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'speldrorblex', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'speldrorblex', 1:
                self._state["current"] = BRARSKONKRAXN
                self._state["trig"]    = "hint:1"
            case 'speldrorblex', _:
                self._state["current"] = SKIMPRUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'speldrorblex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'speldrorblex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"speldrorblex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skimprul(self, hint):
        assert self._state.get("current") == SKIMPRUL, \
            f"bralskenl.skimprul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skimprul', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'skimprul', 1:
                self._state["current"] = GLAXBLELTRENR
                self._state["trig"]    = "hint:1"
            case 'skimprul', _:
                self._state["current"] = BRARSKONKRAXN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skimprul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skimprul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skimprul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brarskonkraxn(self, hint):
        assert self._state.get("current") == BRARSKONKRAXN, \
            f"bralskenl.brarskonkraxn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brarskonkraxn', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'brarskonkraxn', 0:
                self._state["current"] = STIMDRURFLANK
                self._state["trig"]    = "hint:0"
            case 'brarskonkraxn', _:
                self._state["current"] = GLAXBLELTRENR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brarskonkraxn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brarskonkraxn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brarskonkraxn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glaxbleltrenr(self, hint):
        assert self._state.get("current") == GLAXBLELTRENR, \
            f"bralskenl.glaxbleltrenr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glaxbleltrenr', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'glaxbleltrenr', _:
                self._state["current"] = VANSLEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glaxbleltrenr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glaxbleltrenr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glaxbleltrenr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vanslex(self, hint):
        assert self._state.get("current") == VANSLEX, \
            f"bralskenl.vanslex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vanslex', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'vanslex', _:
                self._state["current"] = SLELBRIXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vanslex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vanslex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vanslex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slelbrixx(self, hint):
        assert self._state.get("current") == SLELBRIXX, \
            f"bralskenl.slelbrixx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slelbrixx', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'slelbrixx', _:
                self._state["current"] = TRIMTRIMT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slelbrixx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slelbrixx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slelbrixx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trimtrimt(self, hint):
        assert self._state.get("current") == TRIMTRIMT, \
            f"bralskenl.trimtrimt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trimtrimt', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'trimtrimt', _:
                self._state["current"] = KRIMDRANCLEXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trimtrimt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trimtrimt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trimtrimt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krimdranclexr(self, hint):
        assert self._state.get("current") == KRIMDRANCLEXR, \
            f"bralskenl.krimdranclexr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krimdranclexr', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'krimdranclexr', _:
                self._state["current"] = DRIXCLIXBLOS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krimdranclexr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krimdranclexr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krimdranclexr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drixclixblos(self, hint):
        assert self._state.get("current") == DRIXCLIXBLOS, \
            f"bralskenl.drixclixblos: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drixclixblos', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'drixclixblos', 1:
                self._state["current"] = STIMDRURFLANK
                self._state["trig"]    = "hint:1"
            case 'drixclixblos', _:
                self._state["current"] = STONBRULKRUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drixclixblos', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drixclixblos',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drixclixblos->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stonbrulkrul(self, hint):
        assert self._state.get("current") == STONBRULKRUL, \
            f"bralskenl.stonbrulkrul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stonbrulkrul', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'stonbrulkrul', 1:
                self._state["current"] = GLORVAXSTIX
                self._state["trig"]    = "hint:1"
            case 'stonbrulkrul', _:
                self._state["current"] = SKAXCLALX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stonbrulkrul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stonbrulkrul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stonbrulkrul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skaxclalx(self, hint):
        assert self._state.get("current") == SKAXCLALX, \
            f"bralskenl.skaxclalx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skaxclalx', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'skaxclalx', _:
                self._state["current"] = GLORVAXSTIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skaxclalx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skaxclalx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skaxclalx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glorvaxstix(self, hint):
        assert self._state.get("current") == GLORVAXSTIX, \
            f"bralskenl.glorvaxstix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glorvaxstix', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'glorvaxstix', _:
                self._state["current"] = GRIMPRALT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glorvaxstix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glorvaxstix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glorvaxstix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grimpralt(self, hint):
        assert self._state.get("current") == GRIMPRALT, \
            f"bralskenl.grimpralt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grimpralt', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'grimpralt', 1:
                self._state["current"] = CLIMSTELDREXL
                self._state["trig"]    = "hint:1"
            case 'grimpralt', _:
                self._state["current"] = KROSGRONTRALR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grimpralt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grimpralt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grimpralt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krosgrontralr(self, hint):
        assert self._state.get("current") == KROSGRONTRALR, \
            f"bralskenl.krosgrontralr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krosgrontralr', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'krosgrontralr', 1:
                self._state["current"] = STIMDRURFLANK
                self._state["trig"]    = "hint:1"
            case 'krosgrontralr', _:
                self._state["current"] = CLIMSTELDREXL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krosgrontralr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krosgrontralr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krosgrontralr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _climsteldrexl(self, hint):
        assert self._state.get("current") == CLIMSTELDREXL, \
            f"bralskenl.climsteldrexl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'climsteldrexl', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'climsteldrexl', 1:
                self._state["current"] = STIMDRURFLANK
                self._state["trig"]    = "hint:1"
            case 'climsteldrexl', _:
                self._state["current"] = BRENSPAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'climsteldrexl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'climsteldrexl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"climsteldrexl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brenspal(self, hint):
        assert self._state.get("current") == BRENSPAL, \
            f"bralskenl.brenspal: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brenspal', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'brenspal', _:
                self._state["current"] = VAXFLIMR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brenspal', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brenspal',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brenspal->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vaxflimr(self, hint):
        assert self._state.get("current") == VAXFLIMR, \
            f"bralskenl.vaxflimr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vaxflimr', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'vaxflimr', 1:
                self._state["current"] = SLARKRELGRONX
                self._state["trig"]    = "hint:1"
            case 'vaxflimr', _:
                self._state["current"] = KREXVIMKRAXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vaxflimr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vaxflimr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vaxflimr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krexvimkraxr(self, hint):
        assert self._state.get("current") == KREXVIMKRAXR, \
            f"bralskenl.krexvimkraxr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krexvimkraxr', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'krexvimkraxr', 1:
                self._state["current"] = DRENVORBROS
                self._state["trig"]    = "hint:1"
            case 'krexvimkraxr', _:
                self._state["current"] = SLARKRELGRONX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krexvimkraxr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krexvimkraxr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krexvimkraxr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slarkrelgronx(self, hint):
        assert self._state.get("current") == SLARKRELGRONX, \
            f"bralskenl.slarkrelgronx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slarkrelgronx', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'slarkrelgronx', _:
                self._state["current"] = DRENVORBROS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slarkrelgronx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slarkrelgronx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slarkrelgronx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drenvorbros(self, hint):
        assert self._state.get("current") == DRENVORBROS, \
            f"bralskenl.drenvorbros: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drenvorbros', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'drenvorbros', _:
                self._state["current"] = CLENSLULSTAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drenvorbros', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drenvorbros',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drenvorbros->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clenslulstax(self, hint):
        assert self._state.get("current") == CLENSLULSTAX, \
            f"bralskenl.clenslulstax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clenslulstax', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'clenslulstax', _:
                self._state["current"] = FLENTRORGRON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clenslulstax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clenslulstax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clenslulstax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flentrorgron(self, hint):
        assert self._state.get("current") == FLENTRORGRON, \
            f"bralskenl.flentrorgron: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flentrorgron', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'flentrorgron', _:
                self._state["current"] = FLOSSLAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flentrorgron', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flentrorgron',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flentrorgron->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flosslal(self, hint):
        assert self._state.get("current") == FLOSSLAL, \
            f"bralskenl.flosslal: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flosslal', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'flosslal', _:
                self._state["current"] = VIXKRANBLORL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flosslal', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flosslal',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flosslal->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vixkranblorl(self, hint):
        assert self._state.get("current") == VIXKRANBLORL, \
            f"bralskenl.vixkranblorl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vixkranblorl', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'vixkranblorl', _:
                self._state["current"] = CLARTREL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vixkranblorl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vixkranblorl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vixkranblorl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clartrel(self, hint):
        assert self._state.get("current") == CLARTREL, \
            f"bralskenl.clartrel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clartrel', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'clartrel', 1:
                self._state["current"] = STIMDRURFLANK
                self._state["trig"]    = "hint:1"
            case 'clartrel', _:
                self._state["current"] = VARGRONFLART
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clartrel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clartrel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clartrel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vargronflart(self, hint):
        assert self._state.get("current") == VARGRONFLART, \
            f"bralskenl.vargronflart: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vargronflart', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'vargronflart', _:
                self._state["current"] = DRENDRIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vargronflart', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vargronflart',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vargronflart->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drendrix(self, hint):
        assert self._state.get("current") == DRENDRIX, \
            f"bralskenl.drendrix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drendrix', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'drendrix', _:
                self._state["current"] = SKORCLEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drendrix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drendrix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drendrix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skorclex(self, hint):
        assert self._state.get("current") == SKORCLEX, \
            f"bralskenl.skorclex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skorclex', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'skorclex', _:
                self._state["current"] = SPANFLUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skorclex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skorclex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skorclex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spanflur(self, hint):
        assert self._state.get("current") == SPANFLUR, \
            f"bralskenl.spanflur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spanflur', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'spanflur', _:
                self._state["current"] = SLELBLURBRALL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spanflur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spanflur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spanflur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slelblurbrall(self, hint):
        assert self._state.get("current") == SLELBLURBRALL, \
            f"bralskenl.slelblurbrall: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slelblurbrall', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'slelblurbrall', _:
                self._state["current"] = STALPRELN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slelblurbrall', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slelblurbrall',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slelblurbrall->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stalpreln(self, hint):
        assert self._state.get("current") == STALPRELN, \
            f"bralskenl.stalpreln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stalpreln', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'stalpreln', _:
                self._state["current"] = SKENKRANK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stalpreln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stalpreln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stalpreln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skenkrank(self, hint):
        assert self._state.get("current") == SKENKRANK, \
            f"bralskenl.skenkrank: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skenkrank', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'skenkrank', _:
                self._state["current"] = BRALSTIMPRANT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skenkrank', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skenkrank',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skenkrank->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _bralstimprant(self, hint):
        assert self._state.get("current") == BRALSTIMPRANT, \
            f"bralskenl.bralstimprant: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'bralstimprant', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'bralstimprant', _:
                self._state["current"] = GRONCLURSPORT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'bralstimprant', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'bralstimprant',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"bralstimprant->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _gronclursport(self, hint):
        assert self._state.get("current") == GRONCLURSPORT, \
            f"bralskenl.gronclursport: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'gronclursport', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'gronclursport', 0:
                self._state["current"] = STIMDRURFLANK
                self._state["trig"]    = "hint:0"
            case 'gronclursport', _:
                self._state["current"] = GRURVONDREX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'gronclursport', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'gronclursport',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"gronclursport->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grurvondrex(self, hint):
        assert self._state.get("current") == GRURVONDREX, \
            f"bralskenl.grurvondrex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grurvondrex', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'grurvondrex', 0:
                self._state["current"] = VOSBLORR
                self._state["trig"]    = "hint:0"
            case 'grurvondrex', _:
                self._state["current"] = DRULSTORBLUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grurvondrex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grurvondrex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grurvondrex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drulstorblur(self, hint):
        assert self._state.get("current") == DRULSTORBLUR, \
            f"bralskenl.drulstorblur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drulstorblur', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'drulstorblur', _:
                self._state["current"] = VOSBLORR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drulstorblur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drulstorblur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drulstorblur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vosblorr(self, hint):
        assert self._state.get("current") == VOSBLORR, \
            f"bralskenl.vosblorr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vosblorr', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'vosblorr', 1:
                self._state["current"] = STIMDRURFLANK
                self._state["trig"]    = "hint:1"
            case 'vosblorr', _:
                self._state["current"] = PRURPRORDRAXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vosblorr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vosblorr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vosblorr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prurprordraxr(self, hint):
        assert self._state.get("current") == PRURPRORDRAXR, \
            f"bralskenl.prurprordraxr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prurprordraxr', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'prurprordraxr', 0:
                self._state["current"] = BRARSLULN
                self._state["trig"]    = "hint:0"
            case 'prurprordraxr', _:
                self._state["current"] = SLALSPORGRALL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prurprordraxr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prurprordraxr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prurprordraxr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slalsporgrall(self, hint):
        assert self._state.get("current") == SLALSPORGRALL, \
            f"bralskenl.slalsporgrall: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slalsporgrall', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'slalsporgrall', _:
                self._state["current"] = BRARSLULN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slalsporgrall', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slalsporgrall',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slalsporgrall->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brarsluln(self, hint):
        assert self._state.get("current") == BRARSLULN, \
            f"bralskenl.brarsluln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brarsluln', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'brarsluln', 1:
                self._state["current"] = STIMDRURFLANK
                self._state["trig"]    = "hint:1"
            case 'brarsluln', _:
                self._state["current"] = DRURTRURGRIMK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brarsluln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brarsluln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brarsluln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drurtrurgrimk(self, hint):
        assert self._state.get("current") == DRURTRURGRIMK, \
            f"bralskenl.drurtrurgrimk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drurtrurgrimk', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'drurtrurgrimk', _:
                self._state["current"] = DRANFLENBRALK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drurtrurgrimk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drurtrurgrimk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drurtrurgrimk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _dranflenbralk(self, hint):
        assert self._state.get("current") == DRANFLENBRALK, \
            f"bralskenl.dranflenbralk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'dranflenbralk', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'dranflenbralk', 0:
                self._state["current"] = STARTREL
                self._state["trig"]    = "hint:0"
            case 'dranflenbralk', _:
                self._state["current"] = SLARFLAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'dranflenbralk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'dranflenbralk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"dranflenbralk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slarflal(self, hint):
        assert self._state.get("current") == SLARFLAL, \
            f"bralskenl.slarflal: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slarflal', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'slarflal', 0:
                self._state["current"] = STORKRALSLAX
                self._state["trig"]    = "hint:0"
            case 'slarflal', _:
                self._state["current"] = STARTREL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slarflal', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slarflal',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slarflal->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _startrel(self, hint):
        assert self._state.get("current") == STARTREL, \
            f"bralskenl.startrel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'startrel', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'startrel', 0:
                self._state["current"] = STIMDRURFLANK
                self._state["trig"]    = "hint:0"
            case 'startrel', _:
                self._state["current"] = STORKRALSLAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'startrel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'startrel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"startrel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _storkralslax(self, hint):
        assert self._state.get("current") == STORKRALSLAX, \
            f"bralskenl.storkralslax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'storkralslax', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'storkralslax', 1:
                self._state["current"] = STIMDRURFLANK
                self._state["trig"]    = "hint:1"
            case 'storkralslax', _:
                self._state["current"] = STIMVEXDRANN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'storkralslax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'storkralslax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"storkralslax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stimvexdrann(self, hint):
        assert self._state.get("current") == STIMVEXDRANN, \
            f"bralskenl.stimvexdrann: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stimvexdrann', 2:
                self._state["current"] = KRURKROSTRANK
                self._state["trig"]    = "hint:2"
            case 'stimvexdrann', _:
                self._state["current"] = TRELBRALCLIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stimvexdrann', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stimvexdrann',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stimvexdrann->{_to}", _xid_val)
        self._state["cycle"] += 1

    def invoke(self, hint=None, span=None, caller=None, ctx=None, cycle=0):
        if ctx is None: ctx = {}

        self._state = {"current": SLULSLEN, "ctx": ctx,
                        "span": span, "caller": caller,
                        "trig": "auto", "cycle": cycle}
        _dispatch = {
            SLULSLEN: self._slulslen,
            TROSCLOST: self._trosclost,
            FLALSKIM: self._flalskim,
            BRELBLIMDRUR: self._brelblimdrur,
            SKIMCLULGLON: self._skimclulglon,
            BLORDRORBLAXL: self._blordrorblaxl,
            BREXGRON: self._brexgron,
            FLULBRALBLAX: self._flulbralblax,
            GRARCLEN: self._grarclen,
            PRIMVOS: self._primvos,
            CLURPRIXR: self._clurprixr,
            PRONGRURPRELX: self._prongrurprelx,
            TRANSLULSLAXX: self._translulslaxx,
            BLOSSLORSLAR: self._blosslorslar,
            GLANSTOSDROS: self._glanstosdros,
            BRONTROSGRONT: self._brontrosgront,
            CLAXFLELN: self._claxfleln,
            BRONVURVAL: self._bronvurval,
            GLALKRANTRIX: self._glalkrantrix,
            SPELDRORBLEX: self._speldrorblex,
            SKIMPRUL: self._skimprul,
            BRARSKONKRAXN: self._brarskonkraxn,
            GLAXBLELTRENR: self._glaxbleltrenr,
            VANSLEX: self._vanslex,
            SLELBRIXX: self._slelbrixx,
            TRIMTRIMT: self._trimtrimt,
            KRIMDRANCLEXR: self._krimdranclexr,
            DRIXCLIXBLOS: self._drixclixblos,
            STONBRULKRUL: self._stonbrulkrul,
            SKAXCLALX: self._skaxclalx,
            GLORVAXSTIX: self._glorvaxstix,
            GRIMPRALT: self._grimpralt,
            KROSGRONTRALR: self._krosgrontralr,
            CLIMSTELDREXL: self._climsteldrexl,
            BRENSPAL: self._brenspal,
            VAXFLIMR: self._vaxflimr,
            KREXVIMKRAXR: self._krexvimkraxr,
            SLARKRELGRONX: self._slarkrelgronx,
            DRENVORBROS: self._drenvorbros,
            CLENSLULSTAX: self._clenslulstax,
            FLENTRORGRON: self._flentrorgron,
            FLOSSLAL: self._flosslal,
            VIXKRANBLORL: self._vixkranblorl,
            CLARTREL: self._clartrel,
            VARGRONFLART: self._vargronflart,
            DRENDRIX: self._drendrix,
            SKORCLEX: self._skorclex,
            SPANFLUR: self._spanflur,
            SLELBLURBRALL: self._slelblurbrall,
            STALPRELN: self._stalpreln,
            SKENKRANK: self._skenkrank,
            BRALSTIMPRANT: self._bralstimprant,
            GRONCLURSPORT: self._gronclursport,
            GRURVONDREX: self._grurvondrex,
            DRULSTORBLUR: self._drulstorblur,
            VOSBLORR: self._vosblorr,
            PRURPRORDRAXR: self._prurprordraxr,
            SLALSPORGRALL: self._slalsporgrall,
            BRARSLULN: self._brarsluln,
            DRURTRURGRIMK: self._drurtrurgrimk,
            DRANFLENBRALK: self._dranflenbralk,
            SLARFLAL: self._slarflal,
            STARTREL: self._startrel,
            STORKRALSLAX: self._storkralslax,
            STIMVEXDRANN: self._stimvexdrann,
        }
        while self._state["current"] not in _R and self._state["cycle"] - cycle < 8000:
            _dispatch[self._state["current"]](hint)
        _ret     = _R.get(self._state["current"], -1)
        _is_err  = self._state["current"] == KRURKROSTRANK
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
    return BralskenlFSM().invoke(hint=hint, span=span, caller=caller, ctx=ctx, cycle=cycle)
