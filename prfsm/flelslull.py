from _log import _w as _emit, _xid

GRURDRIXT = 'grurdrixt'
SLURPRANVEN = 'slurpranven'
KRARBLEN = 'krarblen'
GLARCLIXVONK = 'glarclixvonk'
STANBRONL = 'stanbronl'
BLIMKREXGREN = 'blimkrexgren'
SKOSSPOSFLORX = 'skossposflorx'
STOSSTEXGRARK = 'stosstexgrark'
CLORSLANSPOSN = 'clorslansposn'
GRONDRAL = 'grondral'
BLEXPRARGLEXL = 'blexprarglexl'
TRALGRELDREX = 'tralgreldrex'
SKORKROST = 'skorkrost'
BLELVIMPROSR = 'blelvimprosr'
VENBLIMCLELX = 'venblimclelx'
SLOSDRARGLALN = 'slosdrarglaln'
SKENGLONVOS = 'skenglonvos'
CLELSKAXX = 'clelskaxx'
DRONBLEXX = 'dronblexx'
SPALKREX = 'spalkrex'
CLELGLALSPEN = 'clelglalspen'
SLELKRURKREXL = 'slelkrurkrexl'
FLIMBREN = 'flimbren'
SKENTRURPRUL = 'skentrurprul'
SPIXSPEXBLUL = 'spixspexblul'
GRARBRULVONL = 'grarbrulvonl'
FLORSLAXX = 'florslaxx'
SKENVUR = 'skenvur'
SLEXFLEXSPIMT = 'slexflexspimt'
GRORKRAXGRIML = 'grorkraxgriml'
DRIMTRIMSLIX = 'drimtrimslix'
GLARKRARSKON = 'glarkrarskon'
SPALSTAN = 'spalstan'
DRURVURGREN = 'drurvurgren'
TROSDROSGLIX = 'trosdrosglix'
PRURPRULN = 'prurpruln'
GREXSPORK = 'grexspork'
KRANPRON = 'kranpron'
GLIMSPEXDRIXR = 'glimspexdrixr'
KRENDRAR = 'krendrar'
FLULSTELR = 'flulstelr'
GLORBREXR = 'glorbrexr'
FLIMCLEXT = 'flimclext'
GLULGRALSLIMK = 'glulgralslimk'
TRENGRIXGREN = 'trengrixgren'
GLAXKREN = 'glaxkren'
SPORBRANSLOSK = 'sporbranslosk'
KRURCLOSDREL = 'krurclosdrel'
SPORSKOS = 'sporskos'
GRONGLELR = 'gronglelr'
GRIXCLEXN = 'grixclexn'
FLARSPONKRON = 'flarsponkron'
TRIMSLALL = 'trimslall'
VAXBLUR = 'vaxblur'
VARPRANDRUL = 'varprandrul'
SKELVAXSKALR = 'skelvaxskalr'
SLENBROS = 'slenbros'
KRIXFLAR = 'krixflar'
VIXSLEXR = 'vixslexr'
CLORVENPRENL = 'clorvenprenl'
FLAXGLAN = 'flaxglan'
SLOSVEXSTIXR = 'slosvexstixr'
DRONTREX = 'drontrex'
TRIXSPORL = 'trixsporl'
BREXKRIXPROR = 'brexkrixpror'
SKORSTON = 'skorston'
TRURKRAL = 'trurkral'
GRELFLEX = 'grelflex'

_R = {
    SKORSTON: 0,
    TRURKRAL: 1,
    GRELFLEX: 2,
}

_CTX_WRITES_KEY  = 'flurslex'
_CTX_WRITE_STATE = GRONDRAL

class FlelslullFSM:
    def __init__(self):
        self._state = {}

    def _grurdrixt(self, hint):
        assert self._state.get("current") == GRURDRIXT, \
            f"flelslull.grurdrixt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grurdrixt', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'grurdrixt', 1:
                self._state["current"] = KRARBLEN
                self._state["trig"]    = "hint:1"
            case 'grurdrixt', _:
                self._state["current"] = SLURPRANVEN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grurdrixt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grurdrixt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grurdrixt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slurpranven(self, hint):
        assert self._state.get("current") == SLURPRANVEN, \
            f"flelslull.slurpranven: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slurpranven', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'slurpranven', _:
                self._state["current"] = KRARBLEN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slurpranven', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slurpranven',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slurpranven->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krarblen(self, hint):
        assert self._state.get("current") == KRARBLEN, \
            f"flelslull.krarblen: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krarblen', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'krarblen', _:
                self._state["current"] = GLARCLIXVONK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krarblen', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krarblen',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krarblen->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glarclixvonk(self, hint):
        assert self._state.get("current") == GLARCLIXVONK, \
            f"flelslull.glarclixvonk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glarclixvonk', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'glarclixvonk', _:
                self._state["current"] = STANBRONL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glarclixvonk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glarclixvonk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glarclixvonk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stanbronl(self, hint):
        assert self._state.get("current") == STANBRONL, \
            f"flelslull.stanbronl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stanbronl', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'stanbronl', 1:
                self._state["current"] = TRURKRAL
                self._state["trig"]    = "hint:1"
            case 'stanbronl', _:
                self._state["current"] = BLIMKREXGREN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stanbronl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stanbronl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stanbronl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blimkrexgren(self, hint):
        assert self._state.get("current") == BLIMKREXGREN, \
            f"flelslull.blimkrexgren: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blimkrexgren', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'blimkrexgren', 1:
                self._state["current"] = STOSSTEXGRARK
                self._state["trig"]    = "hint:1"
            case 'blimkrexgren', _:
                self._state["current"] = SKOSSPOSFLORX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blimkrexgren', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blimkrexgren',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blimkrexgren->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skossposflorx(self, hint):
        assert self._state.get("current") == SKOSSPOSFLORX, \
            f"flelslull.skossposflorx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skossposflorx', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'skossposflorx', _:
                self._state["current"] = STOSSTEXGRARK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skossposflorx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skossposflorx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skossposflorx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stosstexgrark(self, hint):
        assert self._state.get("current") == STOSSTEXGRARK, \
            f"flelslull.stosstexgrark: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stosstexgrark', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'stosstexgrark', 0:
                self._state["current"] = GRONDRAL
                self._state["trig"]    = "hint:0"
            case 'stosstexgrark', _:
                self._state["current"] = CLORSLANSPOSN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stosstexgrark', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stosstexgrark',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stosstexgrark->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clorslansposn(self, hint):
        assert self._state.get("current") == CLORSLANSPOSN, \
            f"flelslull.clorslansposn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clorslansposn', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'clorslansposn', _:
                self._state["current"] = GRONDRAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clorslansposn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clorslansposn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clorslansposn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grondral(self, hint):
        assert self._state.get("current") == GRONDRAL, \
            f"flelslull.grondral: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        _ctx_val_before = self._state["ctx"].get(_CTX_WRITES_KEY, 0)
        match self._state["current"], hint:
            case 'grondral', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'grondral', _:
                self._state["current"] = BLEXPRARGLEXL
                self._state["trig"]    = "auto"
        _old = self._state["ctx"].get(_CTX_WRITES_KEY, 0)
        _inc = 2 if hint == 2 else 1
        self._state["ctx"][_CTX_WRITES_KEY] = _old + _inc
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grondral', _to, _trig)
        _conds = {"hint_branch": _hint_branch,
                   "ctx_write": True,
                   "ctx_val_before": _ctx_val_before}
        _emit(self._state["cycle"], 1, __name__, 'grondral',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grondral->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blexprarglexl(self, hint):
        assert self._state.get("current") == BLEXPRARGLEXL, \
            f"flelslull.blexprarglexl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blexprarglexl', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'blexprarglexl', 0:
                self._state["current"] = SKORKROST
                self._state["trig"]    = "hint:0"
            case 'blexprarglexl', _:
                self._state["current"] = TRALGRELDREX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blexprarglexl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blexprarglexl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blexprarglexl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _tralgreldrex(self, hint):
        assert self._state.get("current") == TRALGRELDREX, \
            f"flelslull.tralgreldrex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'tralgreldrex', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'tralgreldrex', 0:
                self._state["current"] = TRURKRAL
                self._state["trig"]    = "hint:0"
            case 'tralgreldrex', _:
                self._state["current"] = SKORKROST
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'tralgreldrex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'tralgreldrex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"tralgreldrex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skorkrost(self, hint):
        assert self._state.get("current") == SKORKROST, \
            f"flelslull.skorkrost: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skorkrost', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'skorkrost', 1:
                self._state["current"] = VENBLIMCLELX
                self._state["trig"]    = "hint:1"
            case 'skorkrost', _:
                self._state["current"] = BLELVIMPROSR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skorkrost', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skorkrost',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skorkrost->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blelvimprosr(self, hint):
        assert self._state.get("current") == BLELVIMPROSR, \
            f"flelslull.blelvimprosr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blelvimprosr', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'blelvimprosr', _:
                self._state["current"] = VENBLIMCLELX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blelvimprosr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blelvimprosr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blelvimprosr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _venblimclelx(self, hint):
        assert self._state.get("current") == VENBLIMCLELX, \
            f"flelslull.venblimclelx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'venblimclelx', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'venblimclelx', _:
                self._state["current"] = SLOSDRARGLALN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'venblimclelx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'venblimclelx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"venblimclelx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slosdrarglaln(self, hint):
        assert self._state.get("current") == SLOSDRARGLALN, \
            f"flelslull.slosdrarglaln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slosdrarglaln', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'slosdrarglaln', _:
                self._state["current"] = SKENGLONVOS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slosdrarglaln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slosdrarglaln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slosdrarglaln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skenglonvos(self, hint):
        assert self._state.get("current") == SKENGLONVOS, \
            f"flelslull.skenglonvos: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skenglonvos', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'skenglonvos', 1:
                self._state["current"] = TRURKRAL
                self._state["trig"]    = "hint:1"
            case 'skenglonvos', _:
                self._state["current"] = CLELSKAXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skenglonvos', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skenglonvos',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skenglonvos->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clelskaxx(self, hint):
        assert self._state.get("current") == CLELSKAXX, \
            f"flelslull.clelskaxx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clelskaxx', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'clelskaxx', 0:
                self._state["current"] = SPALKREX
                self._state["trig"]    = "hint:0"
            case 'clelskaxx', _:
                self._state["current"] = DRONBLEXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clelskaxx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clelskaxx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clelskaxx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _dronblexx(self, hint):
        assert self._state.get("current") == DRONBLEXX, \
            f"flelslull.dronblexx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'dronblexx', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'dronblexx', 1:
                self._state["current"] = CLELGLALSPEN
                self._state["trig"]    = "hint:1"
            case 'dronblexx', _:
                self._state["current"] = SPALKREX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'dronblexx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'dronblexx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"dronblexx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spalkrex(self, hint):
        assert self._state.get("current") == SPALKREX, \
            f"flelslull.spalkrex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spalkrex', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'spalkrex', _:
                self._state["current"] = CLELGLALSPEN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spalkrex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spalkrex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spalkrex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clelglalspen(self, hint):
        assert self._state.get("current") == CLELGLALSPEN, \
            f"flelslull.clelglalspen: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clelglalspen', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'clelglalspen', _:
                self._state["current"] = SLELKRURKREXL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clelglalspen', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clelglalspen',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clelglalspen->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slelkrurkrexl(self, hint):
        assert self._state.get("current") == SLELKRURKREXL, \
            f"flelslull.slelkrurkrexl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slelkrurkrexl', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'slelkrurkrexl', 0:
                self._state["current"] = SKENTRURPRUL
                self._state["trig"]    = "hint:0"
            case 'slelkrurkrexl', _:
                self._state["current"] = FLIMBREN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slelkrurkrexl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slelkrurkrexl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slelkrurkrexl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flimbren(self, hint):
        assert self._state.get("current") == FLIMBREN, \
            f"flelslull.flimbren: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flimbren', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'flimbren', 1:
                self._state["current"] = TRURKRAL
                self._state["trig"]    = "hint:1"
            case 'flimbren', _:
                self._state["current"] = SKENTRURPRUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flimbren', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flimbren',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flimbren->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skentrurprul(self, hint):
        assert self._state.get("current") == SKENTRURPRUL, \
            f"flelslull.skentrurprul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skentrurprul', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'skentrurprul', _:
                self._state["current"] = SPIXSPEXBLUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skentrurprul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skentrurprul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skentrurprul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spixspexblul(self, hint):
        assert self._state.get("current") == SPIXSPEXBLUL, \
            f"flelslull.spixspexblul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spixspexblul', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'spixspexblul', _:
                self._state["current"] = GRARBRULVONL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spixspexblul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spixspexblul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spixspexblul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grarbrulvonl(self, hint):
        assert self._state.get("current") == GRARBRULVONL, \
            f"flelslull.grarbrulvonl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grarbrulvonl', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'grarbrulvonl', _:
                self._state["current"] = FLORSLAXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grarbrulvonl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grarbrulvonl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grarbrulvonl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _florslaxx(self, hint):
        assert self._state.get("current") == FLORSLAXX, \
            f"flelslull.florslaxx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'florslaxx', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'florslaxx', 0:
                self._state["current"] = TRURKRAL
                self._state["trig"]    = "hint:0"
            case 'florslaxx', _:
                self._state["current"] = SKENVUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'florslaxx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'florslaxx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"florslaxx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skenvur(self, hint):
        assert self._state.get("current") == SKENVUR, \
            f"flelslull.skenvur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skenvur', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'skenvur', _:
                self._state["current"] = SLEXFLEXSPIMT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skenvur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skenvur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skenvur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slexflexspimt(self, hint):
        assert self._state.get("current") == SLEXFLEXSPIMT, \
            f"flelslull.slexflexspimt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slexflexspimt', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'slexflexspimt', 0:
                self._state["current"] = DRIMTRIMSLIX
                self._state["trig"]    = "hint:0"
            case 'slexflexspimt', _:
                self._state["current"] = GRORKRAXGRIML
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slexflexspimt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slexflexspimt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slexflexspimt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grorkraxgriml(self, hint):
        assert self._state.get("current") == GRORKRAXGRIML, \
            f"flelslull.grorkraxgriml: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grorkraxgriml', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'grorkraxgriml', 0:
                self._state["current"] = GLARKRARSKON
                self._state["trig"]    = "hint:0"
            case 'grorkraxgriml', _:
                self._state["current"] = DRIMTRIMSLIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grorkraxgriml', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grorkraxgriml',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grorkraxgriml->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drimtrimslix(self, hint):
        assert self._state.get("current") == DRIMTRIMSLIX, \
            f"flelslull.drimtrimslix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drimtrimslix', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'drimtrimslix', _:
                self._state["current"] = GLARKRARSKON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drimtrimslix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drimtrimslix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drimtrimslix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glarkrarskon(self, hint):
        assert self._state.get("current") == GLARKRARSKON, \
            f"flelslull.glarkrarskon: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glarkrarskon', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'glarkrarskon', 0:
                self._state["current"] = TRURKRAL
                self._state["trig"]    = "hint:0"
            case 'glarkrarskon', _:
                self._state["current"] = SPALSTAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glarkrarskon', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glarkrarskon',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glarkrarskon->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spalstan(self, hint):
        assert self._state.get("current") == SPALSTAN, \
            f"flelslull.spalstan: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spalstan', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'spalstan', _:
                self._state["current"] = DRURVURGREN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spalstan', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spalstan',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spalstan->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drurvurgren(self, hint):
        assert self._state.get("current") == DRURVURGREN, \
            f"flelslull.drurvurgren: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drurvurgren', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'drurvurgren', _:
                self._state["current"] = TROSDROSGLIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drurvurgren', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drurvurgren',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drurvurgren->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trosdrosglix(self, hint):
        assert self._state.get("current") == TROSDROSGLIX, \
            f"flelslull.trosdrosglix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trosdrosglix', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'trosdrosglix', 1:
                self._state["current"] = TRURKRAL
                self._state["trig"]    = "hint:1"
            case 'trosdrosglix', _:
                self._state["current"] = PRURPRULN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trosdrosglix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trosdrosglix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trosdrosglix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prurpruln(self, hint):
        assert self._state.get("current") == PRURPRULN, \
            f"flelslull.prurpruln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prurpruln', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'prurpruln', 1:
                self._state["current"] = TRURKRAL
                self._state["trig"]    = "hint:1"
            case 'prurpruln', _:
                self._state["current"] = GREXSPORK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prurpruln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prurpruln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prurpruln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grexspork(self, hint):
        assert self._state.get("current") == GREXSPORK, \
            f"flelslull.grexspork: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grexspork', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'grexspork', 1:
                self._state["current"] = TRURKRAL
                self._state["trig"]    = "hint:1"
            case 'grexspork', _:
                self._state["current"] = KRANPRON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grexspork', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grexspork',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grexspork->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _kranpron(self, hint):
        assert self._state.get("current") == KRANPRON, \
            f"flelslull.kranpron: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'kranpron', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'kranpron', _:
                self._state["current"] = GLIMSPEXDRIXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'kranpron', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'kranpron',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"kranpron->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glimspexdrixr(self, hint):
        assert self._state.get("current") == GLIMSPEXDRIXR, \
            f"flelslull.glimspexdrixr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glimspexdrixr', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'glimspexdrixr', 0:
                self._state["current"] = TRURKRAL
                self._state["trig"]    = "hint:0"
            case 'glimspexdrixr', _:
                self._state["current"] = KRENDRAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glimspexdrixr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glimspexdrixr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glimspexdrixr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krendrar(self, hint):
        assert self._state.get("current") == KRENDRAR, \
            f"flelslull.krendrar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krendrar', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'krendrar', _:
                self._state["current"] = FLULSTELR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krendrar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krendrar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krendrar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flulstelr(self, hint):
        assert self._state.get("current") == FLULSTELR, \
            f"flelslull.flulstelr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flulstelr', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'flulstelr', 0:
                self._state["current"] = FLIMCLEXT
                self._state["trig"]    = "hint:0"
            case 'flulstelr', _:
                self._state["current"] = GLORBREXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flulstelr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flulstelr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flulstelr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glorbrexr(self, hint):
        assert self._state.get("current") == GLORBREXR, \
            f"flelslull.glorbrexr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glorbrexr', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'glorbrexr', _:
                self._state["current"] = FLIMCLEXT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glorbrexr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glorbrexr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glorbrexr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flimclext(self, hint):
        assert self._state.get("current") == FLIMCLEXT, \
            f"flelslull.flimclext: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flimclext', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'flimclext', _:
                self._state["current"] = GLULGRALSLIMK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flimclext', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flimclext',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flimclext->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glulgralslimk(self, hint):
        assert self._state.get("current") == GLULGRALSLIMK, \
            f"flelslull.glulgralslimk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glulgralslimk', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'glulgralslimk', _:
                self._state["current"] = TRENGRIXGREN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glulgralslimk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glulgralslimk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glulgralslimk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trengrixgren(self, hint):
        assert self._state.get("current") == TRENGRIXGREN, \
            f"flelslull.trengrixgren: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trengrixgren', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'trengrixgren', 1:
                self._state["current"] = TRURKRAL
                self._state["trig"]    = "hint:1"
            case 'trengrixgren', _:
                self._state["current"] = GLAXKREN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trengrixgren', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trengrixgren',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trengrixgren->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glaxkren(self, hint):
        assert self._state.get("current") == GLAXKREN, \
            f"flelslull.glaxkren: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glaxkren', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'glaxkren', 0:
                self._state["current"] = TRURKRAL
                self._state["trig"]    = "hint:0"
            case 'glaxkren', _:
                self._state["current"] = SPORBRANSLOSK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glaxkren', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glaxkren',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glaxkren->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _sporbranslosk(self, hint):
        assert self._state.get("current") == SPORBRANSLOSK, \
            f"flelslull.sporbranslosk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'sporbranslosk', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'sporbranslosk', _:
                self._state["current"] = KRURCLOSDREL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'sporbranslosk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'sporbranslosk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"sporbranslosk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krurclosdrel(self, hint):
        assert self._state.get("current") == KRURCLOSDREL, \
            f"flelslull.krurclosdrel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krurclosdrel', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'krurclosdrel', _:
                self._state["current"] = SPORSKOS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krurclosdrel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krurclosdrel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krurclosdrel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _sporskos(self, hint):
        assert self._state.get("current") == SPORSKOS, \
            f"flelslull.sporskos: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'sporskos', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'sporskos', 1:
                self._state["current"] = GRIXCLEXN
                self._state["trig"]    = "hint:1"
            case 'sporskos', _:
                self._state["current"] = GRONGLELR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'sporskos', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'sporskos',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"sporskos->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _gronglelr(self, hint):
        assert self._state.get("current") == GRONGLELR, \
            f"flelslull.gronglelr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'gronglelr', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'gronglelr', 0:
                self._state["current"] = FLARSPONKRON
                self._state["trig"]    = "hint:0"
            case 'gronglelr', _:
                self._state["current"] = GRIXCLEXN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'gronglelr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'gronglelr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"gronglelr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grixclexn(self, hint):
        assert self._state.get("current") == GRIXCLEXN, \
            f"flelslull.grixclexn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grixclexn', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'grixclexn', 1:
                self._state["current"] = TRURKRAL
                self._state["trig"]    = "hint:1"
            case 'grixclexn', _:
                self._state["current"] = FLARSPONKRON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grixclexn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grixclexn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grixclexn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flarsponkron(self, hint):
        assert self._state.get("current") == FLARSPONKRON, \
            f"flelslull.flarsponkron: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flarsponkron', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'flarsponkron', 1:
                self._state["current"] = VAXBLUR
                self._state["trig"]    = "hint:1"
            case 'flarsponkron', _:
                self._state["current"] = TRIMSLALL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flarsponkron', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flarsponkron',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flarsponkron->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trimslall(self, hint):
        assert self._state.get("current") == TRIMSLALL, \
            f"flelslull.trimslall: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trimslall', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'trimslall', 1:
                self._state["current"] = VARPRANDRUL
                self._state["trig"]    = "hint:1"
            case 'trimslall', _:
                self._state["current"] = VAXBLUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trimslall', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trimslall',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trimslall->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vaxblur(self, hint):
        assert self._state.get("current") == VAXBLUR, \
            f"flelslull.vaxblur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vaxblur', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'vaxblur', _:
                self._state["current"] = VARPRANDRUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vaxblur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vaxblur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vaxblur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _varprandrul(self, hint):
        assert self._state.get("current") == VARPRANDRUL, \
            f"flelslull.varprandrul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'varprandrul', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'varprandrul', _:
                self._state["current"] = SKELVAXSKALR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'varprandrul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'varprandrul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"varprandrul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skelvaxskalr(self, hint):
        assert self._state.get("current") == SKELVAXSKALR, \
            f"flelslull.skelvaxskalr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skelvaxskalr', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'skelvaxskalr', _:
                self._state["current"] = SLENBROS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skelvaxskalr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skelvaxskalr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skelvaxskalr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slenbros(self, hint):
        assert self._state.get("current") == SLENBROS, \
            f"flelslull.slenbros: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slenbros', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'slenbros', _:
                self._state["current"] = KRIXFLAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slenbros', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slenbros',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slenbros->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krixflar(self, hint):
        assert self._state.get("current") == KRIXFLAR, \
            f"flelslull.krixflar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krixflar', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'krixflar', 0:
                self._state["current"] = CLORVENPRENL
                self._state["trig"]    = "hint:0"
            case 'krixflar', _:
                self._state["current"] = VIXSLEXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krixflar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krixflar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krixflar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vixslexr(self, hint):
        assert self._state.get("current") == VIXSLEXR, \
            f"flelslull.vixslexr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vixslexr', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'vixslexr', _:
                self._state["current"] = CLORVENPRENL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vixslexr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vixslexr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vixslexr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clorvenprenl(self, hint):
        assert self._state.get("current") == CLORVENPRENL, \
            f"flelslull.clorvenprenl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clorvenprenl', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'clorvenprenl', 1:
                self._state["current"] = TRURKRAL
                self._state["trig"]    = "hint:1"
            case 'clorvenprenl', _:
                self._state["current"] = FLAXGLAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clorvenprenl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clorvenprenl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clorvenprenl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flaxglan(self, hint):
        assert self._state.get("current") == FLAXGLAN, \
            f"flelslull.flaxglan: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flaxglan', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'flaxglan', _:
                self._state["current"] = SLOSVEXSTIXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flaxglan', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flaxglan',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flaxglan->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slosvexstixr(self, hint):
        assert self._state.get("current") == SLOSVEXSTIXR, \
            f"flelslull.slosvexstixr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slosvexstixr', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'slosvexstixr', _:
                self._state["current"] = DRONTREX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slosvexstixr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slosvexstixr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slosvexstixr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drontrex(self, hint):
        assert self._state.get("current") == DRONTREX, \
            f"flelslull.drontrex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drontrex', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'drontrex', 0:
                self._state["current"] = BREXKRIXPROR
                self._state["trig"]    = "hint:0"
            case 'drontrex', _:
                self._state["current"] = TRIXSPORL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drontrex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drontrex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drontrex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trixsporl(self, hint):
        assert self._state.get("current") == TRIXSPORL, \
            f"flelslull.trixsporl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trixsporl', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'trixsporl', _:
                self._state["current"] = BREXKRIXPROR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trixsporl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trixsporl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trixsporl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brexkrixpror(self, hint):
        assert self._state.get("current") == BREXKRIXPROR, \
            f"flelslull.brexkrixpror: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brexkrixpror', 2:
                self._state["current"] = GRELFLEX
                self._state["trig"]    = "hint:2"
            case 'brexkrixpror', _:
                self._state["current"] = SKORSTON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brexkrixpror', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brexkrixpror',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brexkrixpror->{_to}", _xid_val)
        self._state["cycle"] += 1

    def invoke(self, hint=None, span=None, caller=None, ctx=None, cycle=0):
        if ctx is None: ctx = {}

        self._state = {"current": GRURDRIXT, "ctx": ctx,
                        "span": span, "caller": caller,
                        "trig": "auto", "cycle": cycle}
        _dispatch = {
            GRURDRIXT: self._grurdrixt,
            SLURPRANVEN: self._slurpranven,
            KRARBLEN: self._krarblen,
            GLARCLIXVONK: self._glarclixvonk,
            STANBRONL: self._stanbronl,
            BLIMKREXGREN: self._blimkrexgren,
            SKOSSPOSFLORX: self._skossposflorx,
            STOSSTEXGRARK: self._stosstexgrark,
            CLORSLANSPOSN: self._clorslansposn,
            GRONDRAL: self._grondral,
            BLEXPRARGLEXL: self._blexprarglexl,
            TRALGRELDREX: self._tralgreldrex,
            SKORKROST: self._skorkrost,
            BLELVIMPROSR: self._blelvimprosr,
            VENBLIMCLELX: self._venblimclelx,
            SLOSDRARGLALN: self._slosdrarglaln,
            SKENGLONVOS: self._skenglonvos,
            CLELSKAXX: self._clelskaxx,
            DRONBLEXX: self._dronblexx,
            SPALKREX: self._spalkrex,
            CLELGLALSPEN: self._clelglalspen,
            SLELKRURKREXL: self._slelkrurkrexl,
            FLIMBREN: self._flimbren,
            SKENTRURPRUL: self._skentrurprul,
            SPIXSPEXBLUL: self._spixspexblul,
            GRARBRULVONL: self._grarbrulvonl,
            FLORSLAXX: self._florslaxx,
            SKENVUR: self._skenvur,
            SLEXFLEXSPIMT: self._slexflexspimt,
            GRORKRAXGRIML: self._grorkraxgriml,
            DRIMTRIMSLIX: self._drimtrimslix,
            GLARKRARSKON: self._glarkrarskon,
            SPALSTAN: self._spalstan,
            DRURVURGREN: self._drurvurgren,
            TROSDROSGLIX: self._trosdrosglix,
            PRURPRULN: self._prurpruln,
            GREXSPORK: self._grexspork,
            KRANPRON: self._kranpron,
            GLIMSPEXDRIXR: self._glimspexdrixr,
            KRENDRAR: self._krendrar,
            FLULSTELR: self._flulstelr,
            GLORBREXR: self._glorbrexr,
            FLIMCLEXT: self._flimclext,
            GLULGRALSLIMK: self._glulgralslimk,
            TRENGRIXGREN: self._trengrixgren,
            GLAXKREN: self._glaxkren,
            SPORBRANSLOSK: self._sporbranslosk,
            KRURCLOSDREL: self._krurclosdrel,
            SPORSKOS: self._sporskos,
            GRONGLELR: self._gronglelr,
            GRIXCLEXN: self._grixclexn,
            FLARSPONKRON: self._flarsponkron,
            TRIMSLALL: self._trimslall,
            VAXBLUR: self._vaxblur,
            VARPRANDRUL: self._varprandrul,
            SKELVAXSKALR: self._skelvaxskalr,
            SLENBROS: self._slenbros,
            KRIXFLAR: self._krixflar,
            VIXSLEXR: self._vixslexr,
            CLORVENPRENL: self._clorvenprenl,
            FLAXGLAN: self._flaxglan,
            SLOSVEXSTIXR: self._slosvexstixr,
            DRONTREX: self._drontrex,
            TRIXSPORL: self._trixsporl,
            BREXKRIXPROR: self._brexkrixpror,
        }
        while self._state["current"] not in _R and self._state["cycle"] - cycle < 8000:
            _dispatch[self._state["current"]](hint)
        _ret     = _R.get(self._state["current"], -1)
        _is_err  = self._state["current"] == GRELFLEX
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
    return FlelslullFSM().invoke(hint=hint, span=span, caller=caller, ctx=ctx, cycle=cycle)
