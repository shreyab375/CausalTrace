from _log import _w as _emit, _xid

KRENPRELK = 'krenprelk'
KROSGLEXPRIMX = 'krosglexprimx'
FLOSVOSDREXX = 'flosvosdrexx'
GRONBLEN = 'gronblen'
SKELSTIXPREXK = 'skelstixprexk'
SPEXDREXPROR = 'spexdrexpror'
KRALSPON = 'kralspon'
SKIMVOSSKANK = 'skimvosskank'
PRIXGLIMTRIM = 'prixglimtrim'
SLALFLAXPRAXK = 'slalflaxpraxk'
STARDRONVORR = 'stardronvorr'
BLENSPORGROS = 'blensporgros'
TRORGLENFLEXX = 'trorglenflexx'
DRAXBRIXKRELR = 'draxbrixkrelr'
BLOSSLORSKEN = 'blosslorsken'
BLURKRARFLARL = 'blurkrarflarl'
VELTREXBRIXL = 'veltrexbrixl'
VAXBRIM = 'vaxbrim'
STEXVOSDRULL = 'stexvosdrull'
GLULGRANTRAN = 'glulgrantran'
GREXSTELR = 'grexstelr'
SKIMPRIMDROR = 'skimprimdror'
GRURGREXGRURN = 'grurgrexgrurn'
FLANVANKRONR = 'flanvankronr'
KRIMSLEXKREN = 'krimslexkren'
KRULSPONSKAX = 'krulsponskax'
CLIMSTARSKANK = 'climstarskank'
TRIMSTUR = 'trimstur'
SPARSTAL = 'sparstal'
CLANSPARK = 'clanspark'
KROSPRIXVIM = 'krosprixvim'
BLANBRENR = 'blanbrenr'
TREXGLIM = 'trexglim'
CLORFLIX = 'clorflix'
FLULGRORBREXL = 'flulgrorbrexl'
SPARBLIXSTEXL = 'sparblixstexl'
CLIXCLONBRENN = 'clixclonbrenn'
STELSPALFLUL = 'stelspalflul'
SKENGLURKRAXK = 'skenglurkraxk'
GRARPRAX = 'grarprax'
BLOSFLAX = 'blosflax'
KRELSPONSPIXK = 'krelsponspixk'
PRIXVELK = 'prixvelk'
DRALGLORVEX = 'dralglorvex'
TRALSLARX = 'tralslarx'
GRAXPRANSLURN = 'graxpranslurn'
FLONCLOS = 'flonclos'
TROSKRAN = 'troskran'
GLARKRONSKAX = 'glarkronskax'
STIMSPEL = 'stimspel'
STARPREXFLAR = 'starprexflar'
SKEXBRAXT = 'skexbraxt'
KRONBRALSTONK = 'kronbralstonk'
GLAXSPALGLIXK = 'glaxspalglixk'
SKULFLENDRUL = 'skulflendrul'
KRARGRIXR = 'krargrixr'
BRURSTENK = 'brurstenk'
STALGRONK = 'stalgronk'
BRAXKRUL = 'braxkrul'
CLELPRAXGRIMX = 'clelpraxgrimx'
KRARCLIMGRUL = 'krarclimgrul'
GLEXGLALSKIX = 'glexglalskix'
FLARFLONN = 'flarflonn'
VOSFLEXN = 'vosflexn'
KRENSKEXK = 'krenskexk'
CLIMBREL = 'climbrel'
GLANBRORFLULT = 'glanbrorflult'
PRURSTONVULT = 'prurstonvult'

_R = {
    CLIMBREL: 0,
    GLANBRORFLULT: 1,
    PRURSTONVULT: 2,
}

_CTX_WRITES_KEY  = 'flurslex'
_CTX_WRITE_STATE = GRONBLEN

class BlixflimxFSM:
    def __init__(self):
        self._state = {}

    def _krenprelk(self, hint):
        assert self._state.get("current") == KRENPRELK, \
            f"blixflimx.krenprelk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krenprelk', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'krenprelk', _:
                self._state["current"] = KROSGLEXPRIMX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krenprelk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krenprelk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krenprelk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krosglexprimx(self, hint):
        assert self._state.get("current") == KROSGLEXPRIMX, \
            f"blixflimx.krosglexprimx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krosglexprimx', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'krosglexprimx', _:
                self._state["current"] = FLOSVOSDREXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krosglexprimx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krosglexprimx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krosglexprimx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flosvosdrexx(self, hint):
        assert self._state.get("current") == FLOSVOSDREXX, \
            f"blixflimx.flosvosdrexx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flosvosdrexx', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'flosvosdrexx', 1:
                self._state["current"] = SKELSTIXPREXK
                self._state["trig"]    = "hint:1"
            case 'flosvosdrexx', _:
                self._state["current"] = GRONBLEN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flosvosdrexx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flosvosdrexx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flosvosdrexx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _gronblen(self, hint):
        assert self._state.get("current") == GRONBLEN, \
            f"blixflimx.gronblen: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        _ctx_val_before = self._state["ctx"].get(_CTX_WRITES_KEY, 0)
        match self._state["current"], hint:
            case 'gronblen', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'gronblen', _:
                self._state["current"] = SKELSTIXPREXK
                self._state["trig"]    = "auto"
        _old = self._state["ctx"].get(_CTX_WRITES_KEY, 0)
        _inc = 2 if hint == 2 else 1
        self._state["ctx"][_CTX_WRITES_KEY] = _old + _inc
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'gronblen', _to, _trig)
        _conds = {"hint_branch": _hint_branch,
                   "ctx_write": True,
                   "ctx_val_before": _ctx_val_before}
        _emit(self._state["cycle"], 1, __name__, 'gronblen',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"gronblen->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skelstixprexk(self, hint):
        assert self._state.get("current") == SKELSTIXPREXK, \
            f"blixflimx.skelstixprexk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skelstixprexk', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'skelstixprexk', 0:
                self._state["current"] = GLANBRORFLULT
                self._state["trig"]    = "hint:0"
            case 'skelstixprexk', _:
                self._state["current"] = SPEXDREXPROR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skelstixprexk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skelstixprexk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skelstixprexk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spexdrexpror(self, hint):
        assert self._state.get("current") == SPEXDREXPROR, \
            f"blixflimx.spexdrexpror: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spexdrexpror', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'spexdrexpror', 1:
                self._state["current"] = SKIMVOSSKANK
                self._state["trig"]    = "hint:1"
            case 'spexdrexpror', _:
                self._state["current"] = KRALSPON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spexdrexpror', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spexdrexpror',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spexdrexpror->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _kralspon(self, hint):
        assert self._state.get("current") == KRALSPON, \
            f"blixflimx.kralspon: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'kralspon', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'kralspon', _:
                self._state["current"] = SKIMVOSSKANK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'kralspon', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'kralspon',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"kralspon->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skimvosskank(self, hint):
        assert self._state.get("current") == SKIMVOSSKANK, \
            f"blixflimx.skimvosskank: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skimvosskank', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'skimvosskank', _:
                self._state["current"] = PRIXGLIMTRIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skimvosskank', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skimvosskank',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skimvosskank->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prixglimtrim(self, hint):
        assert self._state.get("current") == PRIXGLIMTRIM, \
            f"blixflimx.prixglimtrim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prixglimtrim', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'prixglimtrim', _:
                self._state["current"] = SLALFLAXPRAXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prixglimtrim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prixglimtrim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prixglimtrim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slalflaxpraxk(self, hint):
        assert self._state.get("current") == SLALFLAXPRAXK, \
            f"blixflimx.slalflaxpraxk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slalflaxpraxk', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'slalflaxpraxk', _:
                self._state["current"] = STARDRONVORR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slalflaxpraxk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slalflaxpraxk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slalflaxpraxk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stardronvorr(self, hint):
        assert self._state.get("current") == STARDRONVORR, \
            f"blixflimx.stardronvorr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stardronvorr', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'stardronvorr', 1:
                self._state["current"] = GLANBRORFLULT
                self._state["trig"]    = "hint:1"
            case 'stardronvorr', _:
                self._state["current"] = BLENSPORGROS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stardronvorr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stardronvorr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stardronvorr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blensporgros(self, hint):
        assert self._state.get("current") == BLENSPORGROS, \
            f"blixflimx.blensporgros: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blensporgros', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'blensporgros', _:
                self._state["current"] = TRORGLENFLEXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blensporgros', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blensporgros',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blensporgros->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trorglenflexx(self, hint):
        assert self._state.get("current") == TRORGLENFLEXX, \
            f"blixflimx.trorglenflexx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trorglenflexx', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'trorglenflexx', _:
                self._state["current"] = DRAXBRIXKRELR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trorglenflexx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trorglenflexx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trorglenflexx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _draxbrixkrelr(self, hint):
        assert self._state.get("current") == DRAXBRIXKRELR, \
            f"blixflimx.draxbrixkrelr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'draxbrixkrelr', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'draxbrixkrelr', 0:
                self._state["current"] = GLANBRORFLULT
                self._state["trig"]    = "hint:0"
            case 'draxbrixkrelr', _:
                self._state["current"] = BLOSSLORSKEN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'draxbrixkrelr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'draxbrixkrelr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"draxbrixkrelr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blosslorsken(self, hint):
        assert self._state.get("current") == BLOSSLORSKEN, \
            f"blixflimx.blosslorsken: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blosslorsken', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'blosslorsken', 1:
                self._state["current"] = VELTREXBRIXL
                self._state["trig"]    = "hint:1"
            case 'blosslorsken', _:
                self._state["current"] = BLURKRARFLARL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blosslorsken', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blosslorsken',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blosslorsken->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blurkrarflarl(self, hint):
        assert self._state.get("current") == BLURKRARFLARL, \
            f"blixflimx.blurkrarflarl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blurkrarflarl', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'blurkrarflarl', _:
                self._state["current"] = VELTREXBRIXL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blurkrarflarl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blurkrarflarl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blurkrarflarl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _veltrexbrixl(self, hint):
        assert self._state.get("current") == VELTREXBRIXL, \
            f"blixflimx.veltrexbrixl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'veltrexbrixl', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'veltrexbrixl', 0:
                self._state["current"] = STEXVOSDRULL
                self._state["trig"]    = "hint:0"
            case 'veltrexbrixl', _:
                self._state["current"] = VAXBRIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'veltrexbrixl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'veltrexbrixl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"veltrexbrixl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vaxbrim(self, hint):
        assert self._state.get("current") == VAXBRIM, \
            f"blixflimx.vaxbrim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vaxbrim', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'vaxbrim', _:
                self._state["current"] = STEXVOSDRULL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vaxbrim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vaxbrim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vaxbrim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stexvosdrull(self, hint):
        assert self._state.get("current") == STEXVOSDRULL, \
            f"blixflimx.stexvosdrull: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stexvosdrull', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'stexvosdrull', 1:
                self._state["current"] = GLANBRORFLULT
                self._state["trig"]    = "hint:1"
            case 'stexvosdrull', _:
                self._state["current"] = GLULGRANTRAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stexvosdrull', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stexvosdrull',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stexvosdrull->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glulgrantran(self, hint):
        assert self._state.get("current") == GLULGRANTRAN, \
            f"blixflimx.glulgrantran: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glulgrantran', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'glulgrantran', _:
                self._state["current"] = GREXSTELR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glulgrantran', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glulgrantran',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glulgrantran->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grexstelr(self, hint):
        assert self._state.get("current") == GREXSTELR, \
            f"blixflimx.grexstelr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grexstelr', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'grexstelr', 1:
                self._state["current"] = GRURGREXGRURN
                self._state["trig"]    = "hint:1"
            case 'grexstelr', _:
                self._state["current"] = SKIMPRIMDROR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grexstelr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grexstelr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grexstelr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skimprimdror(self, hint):
        assert self._state.get("current") == SKIMPRIMDROR, \
            f"blixflimx.skimprimdror: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skimprimdror', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'skimprimdror', 0:
                self._state["current"] = FLANVANKRONR
                self._state["trig"]    = "hint:0"
            case 'skimprimdror', _:
                self._state["current"] = GRURGREXGRURN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skimprimdror', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skimprimdror',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skimprimdror->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grurgrexgrurn(self, hint):
        assert self._state.get("current") == GRURGREXGRURN, \
            f"blixflimx.grurgrexgrurn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grurgrexgrurn', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'grurgrexgrurn', _:
                self._state["current"] = FLANVANKRONR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grurgrexgrurn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grurgrexgrurn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grurgrexgrurn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flanvankronr(self, hint):
        assert self._state.get("current") == FLANVANKRONR, \
            f"blixflimx.flanvankronr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flanvankronr', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'flanvankronr', 0:
                self._state["current"] = KRULSPONSKAX
                self._state["trig"]    = "hint:0"
            case 'flanvankronr', _:
                self._state["current"] = KRIMSLEXKREN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flanvankronr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flanvankronr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flanvankronr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krimslexkren(self, hint):
        assert self._state.get("current") == KRIMSLEXKREN, \
            f"blixflimx.krimslexkren: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krimslexkren', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'krimslexkren', 0:
                self._state["current"] = CLIMSTARSKANK
                self._state["trig"]    = "hint:0"
            case 'krimslexkren', _:
                self._state["current"] = KRULSPONSKAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krimslexkren', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krimslexkren',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krimslexkren->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krulsponskax(self, hint):
        assert self._state.get("current") == KRULSPONSKAX, \
            f"blixflimx.krulsponskax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krulsponskax', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'krulsponskax', 0:
                self._state["current"] = TRIMSTUR
                self._state["trig"]    = "hint:0"
            case 'krulsponskax', _:
                self._state["current"] = CLIMSTARSKANK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krulsponskax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krulsponskax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krulsponskax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _climstarskank(self, hint):
        assert self._state.get("current") == CLIMSTARSKANK, \
            f"blixflimx.climstarskank: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'climstarskank', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'climstarskank', _:
                self._state["current"] = TRIMSTUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'climstarskank', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'climstarskank',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"climstarskank->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trimstur(self, hint):
        assert self._state.get("current") == TRIMSTUR, \
            f"blixflimx.trimstur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trimstur', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'trimstur', 0:
                self._state["current"] = CLANSPARK
                self._state["trig"]    = "hint:0"
            case 'trimstur', _:
                self._state["current"] = SPARSTAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trimstur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trimstur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trimstur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _sparstal(self, hint):
        assert self._state.get("current") == SPARSTAL, \
            f"blixflimx.sparstal: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'sparstal', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'sparstal', _:
                self._state["current"] = CLANSPARK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'sparstal', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'sparstal',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"sparstal->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clanspark(self, hint):
        assert self._state.get("current") == CLANSPARK, \
            f"blixflimx.clanspark: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clanspark', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'clanspark', _:
                self._state["current"] = KROSPRIXVIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clanspark', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clanspark',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clanspark->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krosprixvim(self, hint):
        assert self._state.get("current") == KROSPRIXVIM, \
            f"blixflimx.krosprixvim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krosprixvim', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'krosprixvim', 1:
                self._state["current"] = TREXGLIM
                self._state["trig"]    = "hint:1"
            case 'krosprixvim', _:
                self._state["current"] = BLANBRENR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krosprixvim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krosprixvim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krosprixvim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blanbrenr(self, hint):
        assert self._state.get("current") == BLANBRENR, \
            f"blixflimx.blanbrenr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blanbrenr', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'blanbrenr', _:
                self._state["current"] = TREXGLIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blanbrenr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blanbrenr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blanbrenr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trexglim(self, hint):
        assert self._state.get("current") == TREXGLIM, \
            f"blixflimx.trexglim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trexglim', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'trexglim', _:
                self._state["current"] = CLORFLIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trexglim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trexglim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trexglim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clorflix(self, hint):
        assert self._state.get("current") == CLORFLIX, \
            f"blixflimx.clorflix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clorflix', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'clorflix', 1:
                self._state["current"] = SPARBLIXSTEXL
                self._state["trig"]    = "hint:1"
            case 'clorflix', _:
                self._state["current"] = FLULGRORBREXL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clorflix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clorflix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clorflix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flulgrorbrexl(self, hint):
        assert self._state.get("current") == FLULGRORBREXL, \
            f"blixflimx.flulgrorbrexl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flulgrorbrexl', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'flulgrorbrexl', 0:
                self._state["current"] = CLIXCLONBRENN
                self._state["trig"]    = "hint:0"
            case 'flulgrorbrexl', _:
                self._state["current"] = SPARBLIXSTEXL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flulgrorbrexl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flulgrorbrexl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flulgrorbrexl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _sparblixstexl(self, hint):
        assert self._state.get("current") == SPARBLIXSTEXL, \
            f"blixflimx.sparblixstexl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'sparblixstexl', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'sparblixstexl', 1:
                self._state["current"] = STELSPALFLUL
                self._state["trig"]    = "hint:1"
            case 'sparblixstexl', _:
                self._state["current"] = CLIXCLONBRENN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'sparblixstexl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'sparblixstexl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"sparblixstexl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clixclonbrenn(self, hint):
        assert self._state.get("current") == CLIXCLONBRENN, \
            f"blixflimx.clixclonbrenn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clixclonbrenn', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'clixclonbrenn', _:
                self._state["current"] = STELSPALFLUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clixclonbrenn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clixclonbrenn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clixclonbrenn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stelspalflul(self, hint):
        assert self._state.get("current") == STELSPALFLUL, \
            f"blixflimx.stelspalflul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stelspalflul', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'stelspalflul', _:
                self._state["current"] = SKENGLURKRAXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stelspalflul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stelspalflul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stelspalflul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skenglurkraxk(self, hint):
        assert self._state.get("current") == SKENGLURKRAXK, \
            f"blixflimx.skenglurkraxk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skenglurkraxk', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'skenglurkraxk', _:
                self._state["current"] = GRARPRAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skenglurkraxk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skenglurkraxk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skenglurkraxk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grarprax(self, hint):
        assert self._state.get("current") == GRARPRAX, \
            f"blixflimx.grarprax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grarprax', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'grarprax', 1:
                self._state["current"] = GLANBRORFLULT
                self._state["trig"]    = "hint:1"
            case 'grarprax', _:
                self._state["current"] = BLOSFLAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grarprax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grarprax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grarprax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blosflax(self, hint):
        assert self._state.get("current") == BLOSFLAX, \
            f"blixflimx.blosflax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blosflax', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'blosflax', 1:
                self._state["current"] = GLANBRORFLULT
                self._state["trig"]    = "hint:1"
            case 'blosflax', _:
                self._state["current"] = KRELSPONSPIXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blosflax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blosflax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blosflax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krelsponspixk(self, hint):
        assert self._state.get("current") == KRELSPONSPIXK, \
            f"blixflimx.krelsponspixk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krelsponspixk', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'krelsponspixk', _:
                self._state["current"] = PRIXVELK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krelsponspixk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krelsponspixk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krelsponspixk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prixvelk(self, hint):
        assert self._state.get("current") == PRIXVELK, \
            f"blixflimx.prixvelk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prixvelk', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'prixvelk', 1:
                self._state["current"] = GLANBRORFLULT
                self._state["trig"]    = "hint:1"
            case 'prixvelk', _:
                self._state["current"] = DRALGLORVEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prixvelk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prixvelk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prixvelk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _dralglorvex(self, hint):
        assert self._state.get("current") == DRALGLORVEX, \
            f"blixflimx.dralglorvex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'dralglorvex', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'dralglorvex', 1:
                self._state["current"] = GRAXPRANSLURN
                self._state["trig"]    = "hint:1"
            case 'dralglorvex', _:
                self._state["current"] = TRALSLARX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'dralglorvex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'dralglorvex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"dralglorvex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _tralslarx(self, hint):
        assert self._state.get("current") == TRALSLARX, \
            f"blixflimx.tralslarx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'tralslarx', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'tralslarx', _:
                self._state["current"] = GRAXPRANSLURN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'tralslarx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'tralslarx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"tralslarx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _graxpranslurn(self, hint):
        assert self._state.get("current") == GRAXPRANSLURN, \
            f"blixflimx.graxpranslurn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'graxpranslurn', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'graxpranslurn', 0:
                self._state["current"] = GLANBRORFLULT
                self._state["trig"]    = "hint:0"
            case 'graxpranslurn', _:
                self._state["current"] = FLONCLOS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'graxpranslurn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'graxpranslurn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"graxpranslurn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flonclos(self, hint):
        assert self._state.get("current") == FLONCLOS, \
            f"blixflimx.flonclos: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flonclos', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'flonclos', _:
                self._state["current"] = TROSKRAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flonclos', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flonclos',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flonclos->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _troskran(self, hint):
        assert self._state.get("current") == TROSKRAN, \
            f"blixflimx.troskran: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'troskran', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'troskran', 1:
                self._state["current"] = STIMSPEL
                self._state["trig"]    = "hint:1"
            case 'troskran', _:
                self._state["current"] = GLARKRONSKAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'troskran', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'troskran',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"troskran->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glarkronskax(self, hint):
        assert self._state.get("current") == GLARKRONSKAX, \
            f"blixflimx.glarkronskax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glarkronskax', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'glarkronskax', _:
                self._state["current"] = STIMSPEL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glarkronskax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glarkronskax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glarkronskax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stimspel(self, hint):
        assert self._state.get("current") == STIMSPEL, \
            f"blixflimx.stimspel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stimspel', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'stimspel', _:
                self._state["current"] = STARPREXFLAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stimspel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stimspel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stimspel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _starprexflar(self, hint):
        assert self._state.get("current") == STARPREXFLAR, \
            f"blixflimx.starprexflar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'starprexflar', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'starprexflar', _:
                self._state["current"] = SKEXBRAXT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'starprexflar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'starprexflar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"starprexflar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skexbraxt(self, hint):
        assert self._state.get("current") == SKEXBRAXT, \
            f"blixflimx.skexbraxt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skexbraxt', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'skexbraxt', 0:
                self._state["current"] = GLANBRORFLULT
                self._state["trig"]    = "hint:0"
            case 'skexbraxt', _:
                self._state["current"] = KRONBRALSTONK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skexbraxt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skexbraxt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skexbraxt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _kronbralstonk(self, hint):
        assert self._state.get("current") == KRONBRALSTONK, \
            f"blixflimx.kronbralstonk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'kronbralstonk', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'kronbralstonk', 0:
                self._state["current"] = GLANBRORFLULT
                self._state["trig"]    = "hint:0"
            case 'kronbralstonk', _:
                self._state["current"] = GLAXSPALGLIXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'kronbralstonk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'kronbralstonk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"kronbralstonk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glaxspalglixk(self, hint):
        assert self._state.get("current") == GLAXSPALGLIXK, \
            f"blixflimx.glaxspalglixk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glaxspalglixk', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'glaxspalglixk', _:
                self._state["current"] = SKULFLENDRUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glaxspalglixk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glaxspalglixk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glaxspalglixk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skulflendrul(self, hint):
        assert self._state.get("current") == SKULFLENDRUL, \
            f"blixflimx.skulflendrul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skulflendrul', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'skulflendrul', 0:
                self._state["current"] = BRURSTENK
                self._state["trig"]    = "hint:0"
            case 'skulflendrul', _:
                self._state["current"] = KRARGRIXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skulflendrul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skulflendrul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skulflendrul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krargrixr(self, hint):
        assert self._state.get("current") == KRARGRIXR, \
            f"blixflimx.krargrixr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krargrixr', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'krargrixr', 0:
                self._state["current"] = STALGRONK
                self._state["trig"]    = "hint:0"
            case 'krargrixr', _:
                self._state["current"] = BRURSTENK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krargrixr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krargrixr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krargrixr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brurstenk(self, hint):
        assert self._state.get("current") == BRURSTENK, \
            f"blixflimx.brurstenk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brurstenk', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'brurstenk', 0:
                self._state["current"] = GLANBRORFLULT
                self._state["trig"]    = "hint:0"
            case 'brurstenk', _:
                self._state["current"] = STALGRONK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brurstenk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brurstenk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brurstenk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stalgronk(self, hint):
        assert self._state.get("current") == STALGRONK, \
            f"blixflimx.stalgronk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stalgronk', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'stalgronk', 1:
                self._state["current"] = GLANBRORFLULT
                self._state["trig"]    = "hint:1"
            case 'stalgronk', _:
                self._state["current"] = BRAXKRUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stalgronk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stalgronk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stalgronk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _braxkrul(self, hint):
        assert self._state.get("current") == BRAXKRUL, \
            f"blixflimx.braxkrul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'braxkrul', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'braxkrul', _:
                self._state["current"] = CLELPRAXGRIMX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'braxkrul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'braxkrul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"braxkrul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clelpraxgrimx(self, hint):
        assert self._state.get("current") == CLELPRAXGRIMX, \
            f"blixflimx.clelpraxgrimx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clelpraxgrimx', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'clelpraxgrimx', 0:
                self._state["current"] = GLEXGLALSKIX
                self._state["trig"]    = "hint:0"
            case 'clelpraxgrimx', _:
                self._state["current"] = KRARCLIMGRUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clelpraxgrimx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clelpraxgrimx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clelpraxgrimx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krarclimgrul(self, hint):
        assert self._state.get("current") == KRARCLIMGRUL, \
            f"blixflimx.krarclimgrul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krarclimgrul', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'krarclimgrul', _:
                self._state["current"] = GLEXGLALSKIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krarclimgrul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krarclimgrul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krarclimgrul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glexglalskix(self, hint):
        assert self._state.get("current") == GLEXGLALSKIX, \
            f"blixflimx.glexglalskix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glexglalskix', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'glexglalskix', _:
                self._state["current"] = FLARFLONN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glexglalskix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glexglalskix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glexglalskix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flarflonn(self, hint):
        assert self._state.get("current") == FLARFLONN, \
            f"blixflimx.flarflonn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flarflonn', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'flarflonn', _:
                self._state["current"] = VOSFLEXN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flarflonn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flarflonn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flarflonn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vosflexn(self, hint):
        assert self._state.get("current") == VOSFLEXN, \
            f"blixflimx.vosflexn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vosflexn', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'vosflexn', _:
                self._state["current"] = KRENSKEXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vosflexn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vosflexn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vosflexn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krenskexk(self, hint):
        assert self._state.get("current") == KRENSKEXK, \
            f"blixflimx.krenskexk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krenskexk', 2:
                self._state["current"] = PRURSTONVULT
                self._state["trig"]    = "hint:2"
            case 'krenskexk', _:
                self._state["current"] = CLIMBREL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krenskexk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krenskexk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krenskexk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def invoke(self, hint=None, span=None, caller=None, ctx=None, cycle=0):
        if ctx is None: ctx = {}

        self._state = {"current": KRENPRELK, "ctx": ctx,
                        "span": span, "caller": caller,
                        "trig": "auto", "cycle": cycle}
        _dispatch = {
            KRENPRELK: self._krenprelk,
            KROSGLEXPRIMX: self._krosglexprimx,
            FLOSVOSDREXX: self._flosvosdrexx,
            GRONBLEN: self._gronblen,
            SKELSTIXPREXK: self._skelstixprexk,
            SPEXDREXPROR: self._spexdrexpror,
            KRALSPON: self._kralspon,
            SKIMVOSSKANK: self._skimvosskank,
            PRIXGLIMTRIM: self._prixglimtrim,
            SLALFLAXPRAXK: self._slalflaxpraxk,
            STARDRONVORR: self._stardronvorr,
            BLENSPORGROS: self._blensporgros,
            TRORGLENFLEXX: self._trorglenflexx,
            DRAXBRIXKRELR: self._draxbrixkrelr,
            BLOSSLORSKEN: self._blosslorsken,
            BLURKRARFLARL: self._blurkrarflarl,
            VELTREXBRIXL: self._veltrexbrixl,
            VAXBRIM: self._vaxbrim,
            STEXVOSDRULL: self._stexvosdrull,
            GLULGRANTRAN: self._glulgrantran,
            GREXSTELR: self._grexstelr,
            SKIMPRIMDROR: self._skimprimdror,
            GRURGREXGRURN: self._grurgrexgrurn,
            FLANVANKRONR: self._flanvankronr,
            KRIMSLEXKREN: self._krimslexkren,
            KRULSPONSKAX: self._krulsponskax,
            CLIMSTARSKANK: self._climstarskank,
            TRIMSTUR: self._trimstur,
            SPARSTAL: self._sparstal,
            CLANSPARK: self._clanspark,
            KROSPRIXVIM: self._krosprixvim,
            BLANBRENR: self._blanbrenr,
            TREXGLIM: self._trexglim,
            CLORFLIX: self._clorflix,
            FLULGRORBREXL: self._flulgrorbrexl,
            SPARBLIXSTEXL: self._sparblixstexl,
            CLIXCLONBRENN: self._clixclonbrenn,
            STELSPALFLUL: self._stelspalflul,
            SKENGLURKRAXK: self._skenglurkraxk,
            GRARPRAX: self._grarprax,
            BLOSFLAX: self._blosflax,
            KRELSPONSPIXK: self._krelsponspixk,
            PRIXVELK: self._prixvelk,
            DRALGLORVEX: self._dralglorvex,
            TRALSLARX: self._tralslarx,
            GRAXPRANSLURN: self._graxpranslurn,
            FLONCLOS: self._flonclos,
            TROSKRAN: self._troskran,
            GLARKRONSKAX: self._glarkronskax,
            STIMSPEL: self._stimspel,
            STARPREXFLAR: self._starprexflar,
            SKEXBRAXT: self._skexbraxt,
            KRONBRALSTONK: self._kronbralstonk,
            GLAXSPALGLIXK: self._glaxspalglixk,
            SKULFLENDRUL: self._skulflendrul,
            KRARGRIXR: self._krargrixr,
            BRURSTENK: self._brurstenk,
            STALGRONK: self._stalgronk,
            BRAXKRUL: self._braxkrul,
            CLELPRAXGRIMX: self._clelpraxgrimx,
            KRARCLIMGRUL: self._krarclimgrul,
            GLEXGLALSKIX: self._glexglalskix,
            FLARFLONN: self._flarflonn,
            VOSFLEXN: self._vosflexn,
            KRENSKEXK: self._krenskexk,
        }
        while self._state["current"] not in _R and self._state["cycle"] - cycle < 8000:
            _dispatch[self._state["current"]](hint)
        _ret     = _R.get(self._state["current"], -1)
        _is_err  = self._state["current"] == PRURSTONVULT
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
    return BlixflimxFSM().invoke(hint=hint, span=span, caller=caller, ctx=ctx, cycle=cycle)
