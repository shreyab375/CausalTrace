from _log import _w as _emit, _xid

STAXSKOSK = 'staxskosk'
GRIMGLULSLAX = 'grimglulslax'
DRIMKREL = 'drimkrel'
KRAXSPELKRURK = 'kraxspelkrurk'
GRIMGLOSSPIMK = 'grimglosspimk'
BLORVURBLIXN = 'blorvurblixn'
KRORBROST = 'krorbrost'
KREXGLARR = 'krexglarr'
STEXGLELBLEXR = 'stexglelblexr'
GRAXSKEXGREXN = 'graxskexgrexn'
KRALSKAX = 'kralskax'
FLARBRONGLAX = 'flarbronglax'
PRENKRANSKEN = 'prenkransken'
CLULBLIMFLIXX = 'clulblimflixx'
BLARGREXN = 'blargrexn'
GRELSLENSLAXT = 'grelslenslaxt'
VALSTALBRULK = 'valstalbrulk'
STALVIMSKAN = 'stalvimskan'
SPALBRARKRAR = 'spalbrarkrar'
VENVIM = 'venvim'
CLONKROS = 'clonkros'
TROSSKELK = 'trosskelk'
GRELSKEXX = 'grelskexx'
GROSPROS = 'grospros'
SLIMCLENK = 'slimclenk'
TROSPRALVELN = 'trospralveln'
CLAXDRORL = 'claxdrorl'
CLEXTROR = 'clextror'
STAXFLENR = 'staxflenr'
SPARDREL = 'spardrel'
CLELKREN = 'clelkren'
GLORGLANL = 'glorglanl'
DRONBLAXSKAL = 'dronblaxskal'
CLURCLORR = 'clurclorr'
KRAXKRIMGRULX = 'kraxkrimgrulx'
SLIXKRAXSTONT = 'slixkraxstont'
GRIMGRENGLALK = 'grimgrenglalk'
VOSSPULN = 'vosspuln'
CLULGRAL = 'clulgral'
BLENCLEXFLOS = 'blenclexflos'
DREXGLIXSTIXT = 'drexglixstixt'
FLALPRORR = 'flalprorr'
GRIMTRALSPANT = 'grimtralspant'
SKANKRULBRENT = 'skankrulbrent'
SLENSTORX = 'slenstorx'
BRURSPAR = 'brurspar'
CLULBROSBLAX = 'clulbrosblax'
BRALTRAXVIX = 'braltraxvix'
TRULGLAX = 'trulglax'
SPANKREXKRAX = 'spankrexkrax'
SPURKROR = 'spurkror'
DRAXGLURL = 'draxglurl'
TRORBRANPRORX = 'trorbranprorx'
STELKRIXSKIXK = 'stelkrixskixk'
KRALFLOS = 'kralflos'
BRORGRELK = 'brorgrelk'
CLIXSLARPRUL = 'clixslarprul'
GLELTRORX = 'gleltrorx'
GLENSLAXSKAL = 'glenslaxskal'
SPULFLELGRAR = 'spulflelgrar'
BLIMKRURL = 'blimkrurl'
FLOSVIMSPURT = 'flosvimspurt'
KRARBLANR = 'krarblanr'
GRULPRORL = 'grulprorl'
TRALSKARVAX = 'tralskarvax'
KRORTRALFLOST = 'krortralflost'
PRONDRALSKUL = 'prondralskul'
KRENKRIMK = 'krenkrimk'

_R = {
    KRORTRALFLOST: 0,
    PRONDRALSKUL: 1,
    KRENKRIMK: 2,
}

_CTX_READS_KEY = 'flurslex'
_CTX_THRESHOLD = 16

class FlaxclimnFSM:
    def __init__(self):
        self._state = {}

    def _staxskosk(self, hint):
        assert self._state.get("current") == STAXSKOSK, \
            f"flaxclimn.staxskosk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'staxskosk', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'staxskosk', 1:
                self._state["current"] = PRONDRALSKUL
                self._state["trig"]    = "hint:1"
            case 'staxskosk', _:
                self._state["current"] = GRIMGLULSLAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'staxskosk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'staxskosk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"staxskosk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grimglulslax(self, hint):
        assert self._state.get("current") == GRIMGLULSLAX, \
            f"flaxclimn.grimglulslax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grimglulslax', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'grimglulslax', 0:
                self._state["current"] = PRONDRALSKUL
                self._state["trig"]    = "hint:0"
            case 'grimglulslax', _:
                self._state["current"] = DRIMKREL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grimglulslax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grimglulslax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grimglulslax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drimkrel(self, hint):
        assert self._state.get("current") == DRIMKREL, \
            f"flaxclimn.drimkrel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drimkrel', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'drimkrel', 0:
                self._state["current"] = PRONDRALSKUL
                self._state["trig"]    = "hint:0"
            case 'drimkrel', _:
                self._state["current"] = KRAXSPELKRURK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drimkrel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drimkrel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drimkrel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _kraxspelkrurk(self, hint):
        assert self._state.get("current") == KRAXSPELKRURK, \
            f"flaxclimn.kraxspelkrurk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'kraxspelkrurk', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'kraxspelkrurk', _:
                self._state["current"] = GRIMGLOSSPIMK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'kraxspelkrurk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'kraxspelkrurk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"kraxspelkrurk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grimglosspimk(self, hint):
        assert self._state.get("current") == GRIMGLOSSPIMK, \
            f"flaxclimn.grimglosspimk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grimglosspimk', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'grimglosspimk', _:
                self._state["current"] = BLORVURBLIXN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grimglosspimk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grimglosspimk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grimglosspimk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blorvurblixn(self, hint):
        assert self._state.get("current") == BLORVURBLIXN, \
            f"flaxclimn.blorvurblixn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blorvurblixn', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'blorvurblixn', _:
                self._state["current"] = KRORBROST
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blorvurblixn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blorvurblixn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blorvurblixn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krorbrost(self, hint):
        assert self._state.get("current") == KRORBROST, \
            f"flaxclimn.krorbrost: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krorbrost', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'krorbrost', _:
                self._state["current"] = KREXGLARR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krorbrost', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krorbrost',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krorbrost->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krexglarr(self, hint):
        assert self._state.get("current") == KREXGLARR, \
            f"flaxclimn.krexglarr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krexglarr', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'krexglarr', _:
                self._state["current"] = STEXGLELBLEXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krexglarr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krexglarr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krexglarr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stexglelblexr(self, hint):
        assert self._state.get("current") == STEXGLELBLEXR, \
            f"flaxclimn.stexglelblexr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stexglelblexr', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'stexglelblexr', 0:
                self._state["current"] = PRONDRALSKUL
                self._state["trig"]    = "hint:0"
            case 'stexglelblexr', _:
                self._state["current"] = GRAXSKEXGREXN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stexglelblexr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stexglelblexr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stexglelblexr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _graxskexgrexn(self, hint):
        assert self._state.get("current") == GRAXSKEXGREXN, \
            f"flaxclimn.graxskexgrexn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'graxskexgrexn', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'graxskexgrexn', _:
                self._state["current"] = KRALSKAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'graxskexgrexn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'graxskexgrexn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"graxskexgrexn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _kralskax(self, hint):
        assert self._state.get("current") == KRALSKAX, \
            f"flaxclimn.kralskax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'kralskax', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'kralskax', 0:
                self._state["current"] = PRENKRANSKEN
                self._state["trig"]    = "hint:0"
            case 'kralskax', _:
                self._state["current"] = FLARBRONGLAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'kralskax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'kralskax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"kralskax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flarbronglax(self, hint):
        assert self._state.get("current") == FLARBRONGLAX, \
            f"flaxclimn.flarbronglax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flarbronglax', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'flarbronglax', 1:
                self._state["current"] = CLULBLIMFLIXX
                self._state["trig"]    = "hint:1"
            case 'flarbronglax', _:
                self._state["current"] = PRENKRANSKEN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flarbronglax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flarbronglax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flarbronglax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prenkransken(self, hint):
        assert self._state.get("current") == PRENKRANSKEN, \
            f"flaxclimn.prenkransken: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prenkransken', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'prenkransken', _:
                self._state["current"] = CLULBLIMFLIXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prenkransken', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prenkransken',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prenkransken->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clulblimflixx(self, hint):
        assert self._state.get("current") == CLULBLIMFLIXX, \
            f"flaxclimn.clulblimflixx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clulblimflixx', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'clulblimflixx', _:
                self._state["current"] = BLARGREXN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clulblimflixx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clulblimflixx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clulblimflixx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blargrexn(self, hint):
        assert self._state.get("current") == BLARGREXN, \
            f"flaxclimn.blargrexn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blargrexn', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'blargrexn', _:
                self._state["current"] = GRELSLENSLAXT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blargrexn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blargrexn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blargrexn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grelslenslaxt(self, hint):
        assert self._state.get("current") == GRELSLENSLAXT, \
            f"flaxclimn.grelslenslaxt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grelslenslaxt', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'grelslenslaxt', 1:
                self._state["current"] = PRONDRALSKUL
                self._state["trig"]    = "hint:1"
            case 'grelslenslaxt', _:
                self._state["current"] = VALSTALBRULK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grelslenslaxt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grelslenslaxt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grelslenslaxt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _valstalbrulk(self, hint):
        assert self._state.get("current") == VALSTALBRULK, \
            f"flaxclimn.valstalbrulk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'valstalbrulk', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'valstalbrulk', 1:
                self._state["current"] = PRONDRALSKUL
                self._state["trig"]    = "hint:1"
            case 'valstalbrulk', _:
                self._state["current"] = STALVIMSKAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'valstalbrulk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'valstalbrulk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"valstalbrulk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stalvimskan(self, hint):
        assert self._state.get("current") == STALVIMSKAN, \
            f"flaxclimn.stalvimskan: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stalvimskan', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'stalvimskan', 1:
                self._state["current"] = PRONDRALSKUL
                self._state["trig"]    = "hint:1"
            case 'stalvimskan', _:
                self._state["current"] = SPALBRARKRAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stalvimskan', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stalvimskan',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stalvimskan->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spalbrarkrar(self, hint):
        assert self._state.get("current") == SPALBRARKRAR, \
            f"flaxclimn.spalbrarkrar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spalbrarkrar', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'spalbrarkrar', 1:
                self._state["current"] = CLONKROS
                self._state["trig"]    = "hint:1"
            case 'spalbrarkrar', _:
                self._state["current"] = VENVIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spalbrarkrar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spalbrarkrar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spalbrarkrar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _venvim(self, hint):
        assert self._state.get("current") == VENVIM, \
            f"flaxclimn.venvim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'venvim', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'venvim', _:
                self._state["current"] = CLONKROS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'venvim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'venvim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"venvim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clonkros(self, hint):
        assert self._state.get("current") == CLONKROS, \
            f"flaxclimn.clonkros: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clonkros', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'clonkros', 1:
                self._state["current"] = PRONDRALSKUL
                self._state["trig"]    = "hint:1"
            case 'clonkros', _:
                self._state["current"] = TROSSKELK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clonkros', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clonkros',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clonkros->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trosskelk(self, hint):
        assert self._state.get("current") == TROSSKELK, \
            f"flaxclimn.trosskelk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trosskelk', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'trosskelk', 1:
                self._state["current"] = PRONDRALSKUL
                self._state["trig"]    = "hint:1"
            case 'trosskelk', _:
                self._state["current"] = GRELSKEXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trosskelk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trosskelk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trosskelk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grelskexx(self, hint):
        assert self._state.get("current") == GRELSKEXX, \
            f"flaxclimn.grelskexx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grelskexx', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'grelskexx', _:
                self._state["current"] = GROSPROS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grelskexx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grelskexx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grelskexx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grospros(self, hint):
        assert self._state.get("current") == GROSPROS, \
            f"flaxclimn.grospros: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grospros', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'grospros', _:
                self._state["current"] = SLIMCLENK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grospros', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grospros',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grospros->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slimclenk(self, hint):
        assert self._state.get("current") == SLIMCLENK, \
            f"flaxclimn.slimclenk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slimclenk', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'slimclenk', 0:
                self._state["current"] = PRONDRALSKUL
                self._state["trig"]    = "hint:0"
            case 'slimclenk', _:
                self._state["current"] = TROSPRALVELN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slimclenk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slimclenk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slimclenk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trospralveln(self, hint):
        assert self._state.get("current") == TROSPRALVELN, \
            f"flaxclimn.trospralveln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trospralveln', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'trospralveln', 0:
                self._state["current"] = CLEXTROR
                self._state["trig"]    = "hint:0"
            case 'trospralveln', _:
                self._state["current"] = CLAXDRORL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trospralveln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trospralveln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trospralveln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _claxdrorl(self, hint):
        assert self._state.get("current") == CLAXDRORL, \
            f"flaxclimn.claxdrorl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'claxdrorl', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'claxdrorl', 0:
                self._state["current"] = PRONDRALSKUL
                self._state["trig"]    = "hint:0"
            case 'claxdrorl', _:
                self._state["current"] = CLEXTROR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'claxdrorl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'claxdrorl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"claxdrorl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clextror(self, hint):
        assert self._state.get("current") == CLEXTROR, \
            f"flaxclimn.clextror: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clextror', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'clextror', 1:
                self._state["current"] = PRONDRALSKUL
                self._state["trig"]    = "hint:1"
            case 'clextror', _:
                self._state["current"] = STAXFLENR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clextror', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clextror',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clextror->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _staxflenr(self, hint):
        assert self._state.get("current") == STAXFLENR, \
            f"flaxclimn.staxflenr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'staxflenr', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'staxflenr', _:
                self._state["current"] = SPARDREL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'staxflenr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'staxflenr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"staxflenr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spardrel(self, hint):
        assert self._state.get("current") == SPARDREL, \
            f"flaxclimn.spardrel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spardrel', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'spardrel', _:
                self._state["current"] = CLELKREN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spardrel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spardrel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spardrel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clelkren(self, hint):
        assert self._state.get("current") == CLELKREN, \
            f"flaxclimn.clelkren: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clelkren', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'clelkren', 1:
                self._state["current"] = DRONBLAXSKAL
                self._state["trig"]    = "hint:1"
            case 'clelkren', _:
                self._state["current"] = GLORGLANL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clelkren', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clelkren',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clelkren->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glorglanl(self, hint):
        assert self._state.get("current") == GLORGLANL, \
            f"flaxclimn.glorglanl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glorglanl', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'glorglanl', 1:
                self._state["current"] = CLURCLORR
                self._state["trig"]    = "hint:1"
            case 'glorglanl', _:
                self._state["current"] = DRONBLAXSKAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glorglanl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glorglanl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glorglanl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _dronblaxskal(self, hint):
        assert self._state.get("current") == DRONBLAXSKAL, \
            f"flaxclimn.dronblaxskal: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'dronblaxskal', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'dronblaxskal', 0:
                self._state["current"] = PRONDRALSKUL
                self._state["trig"]    = "hint:0"
            case 'dronblaxskal', _:
                self._state["current"] = CLURCLORR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'dronblaxskal', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'dronblaxskal',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"dronblaxskal->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clurclorr(self, hint):
        assert self._state.get("current") == CLURCLORR, \
            f"flaxclimn.clurclorr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clurclorr', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'clurclorr', _:
                self._state["current"] = KRAXKRIMGRULX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clurclorr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clurclorr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clurclorr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _kraxkrimgrulx(self, hint):
        assert self._state.get("current") == KRAXKRIMGRULX, \
            f"flaxclimn.kraxkrimgrulx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'kraxkrimgrulx', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'kraxkrimgrulx', _:
                self._state["current"] = SLIXKRAXSTONT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'kraxkrimgrulx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'kraxkrimgrulx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"kraxkrimgrulx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slixkraxstont(self, hint):
        assert self._state.get("current") == SLIXKRAXSTONT, \
            f"flaxclimn.slixkraxstont: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slixkraxstont', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'slixkraxstont', 1:
                self._state["current"] = PRONDRALSKUL
                self._state["trig"]    = "hint:1"
            case 'slixkraxstont', _:
                self._state["current"] = GRIMGRENGLALK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slixkraxstont', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slixkraxstont',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slixkraxstont->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grimgrenglalk(self, hint):
        assert self._state.get("current") == GRIMGRENGLALK, \
            f"flaxclimn.grimgrenglalk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grimgrenglalk', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'grimgrenglalk', 0:
                self._state["current"] = PRONDRALSKUL
                self._state["trig"]    = "hint:0"
            case 'grimgrenglalk', _:
                self._state["current"] = VOSSPULN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grimgrenglalk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grimgrenglalk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grimgrenglalk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vosspuln(self, hint):
        assert self._state.get("current") == VOSSPULN, \
            f"flaxclimn.vosspuln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vosspuln', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'vosspuln', _:
                self._state["current"] = CLULGRAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vosspuln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vosspuln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vosspuln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clulgral(self, hint):
        assert self._state.get("current") == CLULGRAL, \
            f"flaxclimn.clulgral: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clulgral', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'clulgral', _:
                self._state["current"] = BLENCLEXFLOS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clulgral', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clulgral',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clulgral->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blenclexflos(self, hint):
        assert self._state.get("current") == BLENCLEXFLOS, \
            f"flaxclimn.blenclexflos: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blenclexflos', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'blenclexflos', 1:
                self._state["current"] = FLALPRORR
                self._state["trig"]    = "hint:1"
            case 'blenclexflos', _:
                self._state["current"] = DREXGLIXSTIXT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blenclexflos', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blenclexflos',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blenclexflos->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drexglixstixt(self, hint):
        assert self._state.get("current") == DREXGLIXSTIXT, \
            f"flaxclimn.drexglixstixt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drexglixstixt', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'drexglixstixt', _:
                self._state["current"] = FLALPRORR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drexglixstixt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drexglixstixt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drexglixstixt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flalprorr(self, hint):
        assert self._state.get("current") == FLALPRORR, \
            f"flaxclimn.flalprorr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flalprorr', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'flalprorr', _:
                self._state["current"] = GRIMTRALSPANT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flalprorr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flalprorr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flalprorr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grimtralspant(self, hint):
        assert self._state.get("current") == GRIMTRALSPANT, \
            f"flaxclimn.grimtralspant: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grimtralspant', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'grimtralspant', _:
                self._state["current"] = SKANKRULBRENT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grimtralspant', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grimtralspant',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grimtralspant->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skankrulbrent(self, hint):
        assert self._state.get("current") == SKANKRULBRENT, \
            f"flaxclimn.skankrulbrent: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skankrulbrent', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'skankrulbrent', _:
                self._state["current"] = SLENSTORX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skankrulbrent', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skankrulbrent',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skankrulbrent->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slenstorx(self, hint):
        assert self._state.get("current") == SLENSTORX, \
            f"flaxclimn.slenstorx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slenstorx', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'slenstorx', _:
                self._state["current"] = BRURSPAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slenstorx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slenstorx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slenstorx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brurspar(self, hint):
        assert self._state.get("current") == BRURSPAR, \
            f"flaxclimn.brurspar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brurspar', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'brurspar', _:
                self._state["current"] = CLULBROSBLAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brurspar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brurspar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brurspar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clulbrosblax(self, hint):
        assert self._state.get("current") == CLULBROSBLAX, \
            f"flaxclimn.clulbrosblax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clulbrosblax', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'clulbrosblax', _:
                self._state["current"] = BRALTRAXVIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clulbrosblax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clulbrosblax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clulbrosblax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _braltraxvix(self, hint):
        assert self._state.get("current") == BRALTRAXVIX, \
            f"flaxclimn.braltraxvix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'braltraxvix', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'braltraxvix', 1:
                self._state["current"] = SPANKREXKRAX
                self._state["trig"]    = "hint:1"
            case 'braltraxvix', _:
                self._state["current"] = TRULGLAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'braltraxvix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'braltraxvix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"braltraxvix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trulglax(self, hint):
        assert self._state.get("current") == TRULGLAX, \
            f"flaxclimn.trulglax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trulglax', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'trulglax', _:
                self._state["current"] = SPANKREXKRAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trulglax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trulglax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trulglax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spankrexkrax(self, hint):
        assert self._state.get("current") == SPANKREXKRAX, \
            f"flaxclimn.spankrexkrax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spankrexkrax', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'spankrexkrax', 0:
                self._state["current"] = PRONDRALSKUL
                self._state["trig"]    = "hint:0"
            case 'spankrexkrax', _:
                self._state["current"] = SPURKROR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spankrexkrax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spankrexkrax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spankrexkrax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spurkror(self, hint):
        assert self._state.get("current") == SPURKROR, \
            f"flaxclimn.spurkror: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spurkror', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'spurkror', _:
                self._state["current"] = DRAXGLURL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spurkror', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spurkror',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spurkror->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _draxglurl(self, hint):
        assert self._state.get("current") == DRAXGLURL, \
            f"flaxclimn.draxglurl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'draxglurl', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'draxglurl', 1:
                self._state["current"] = STELKRIXSKIXK
                self._state["trig"]    = "hint:1"
            case 'draxglurl', _:
                self._state["current"] = TRORBRANPRORX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'draxglurl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'draxglurl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"draxglurl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trorbranprorx(self, hint):
        assert self._state.get("current") == TRORBRANPRORX, \
            f"flaxclimn.trorbranprorx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trorbranprorx', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'trorbranprorx', _:
                self._state["current"] = STELKRIXSKIXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trorbranprorx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trorbranprorx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trorbranprorx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stelkrixskixk(self, hint):
        assert self._state.get("current") == STELKRIXSKIXK, \
            f"flaxclimn.stelkrixskixk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stelkrixskixk', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'stelkrixskixk', 1:
                self._state["current"] = BRORGRELK
                self._state["trig"]    = "hint:1"
            case 'stelkrixskixk', _:
                self._state["current"] = KRALFLOS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stelkrixskixk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stelkrixskixk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stelkrixskixk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _kralflos(self, hint):
        assert self._state.get("current") == KRALFLOS, \
            f"flaxclimn.kralflos: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'kralflos', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'kralflos', 1:
                self._state["current"] = CLIXSLARPRUL
                self._state["trig"]    = "hint:1"
            case 'kralflos', _:
                self._state["current"] = BRORGRELK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'kralflos', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'kralflos',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"kralflos->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brorgrelk(self, hint):
        assert self._state.get("current") == BRORGRELK, \
            f"flaxclimn.brorgrelk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brorgrelk', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'brorgrelk', 1:
                self._state["current"] = PRONDRALSKUL
                self._state["trig"]    = "hint:1"
            case 'brorgrelk', _:
                self._state["current"] = CLIXSLARPRUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brorgrelk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brorgrelk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brorgrelk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clixslarprul(self, hint):
        assert self._state.get("current") == CLIXSLARPRUL, \
            f"flaxclimn.clixslarprul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clixslarprul', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'clixslarprul', 0:
                self._state["current"] = GLENSLAXSKAL
                self._state["trig"]    = "hint:0"
            case 'clixslarprul', _:
                self._state["current"] = GLELTRORX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clixslarprul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clixslarprul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clixslarprul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _gleltrorx(self, hint):
        assert self._state.get("current") == GLELTRORX, \
            f"flaxclimn.gleltrorx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'gleltrorx', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'gleltrorx', _:
                self._state["current"] = GLENSLAXSKAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'gleltrorx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'gleltrorx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"gleltrorx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glenslaxskal(self, hint):
        assert self._state.get("current") == GLENSLAXSKAL, \
            f"flaxclimn.glenslaxskal: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glenslaxskal', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'glenslaxskal', 1:
                self._state["current"] = PRONDRALSKUL
                self._state["trig"]    = "hint:1"
            case 'glenslaxskal', _:
                self._state["current"] = SPULFLELGRAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glenslaxskal', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glenslaxskal',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glenslaxskal->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spulflelgrar(self, hint):
        assert self._state.get("current") == SPULFLELGRAR, \
            f"flaxclimn.spulflelgrar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spulflelgrar', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'spulflelgrar', _:
                self._state["current"] = BLIMKRURL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spulflelgrar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spulflelgrar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spulflelgrar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blimkrurl(self, hint):
        assert self._state.get("current") == BLIMKRURL, \
            f"flaxclimn.blimkrurl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blimkrurl', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'blimkrurl', _:
                self._state["current"] = FLOSVIMSPURT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blimkrurl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blimkrurl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blimkrurl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flosvimspurt(self, hint):
        assert self._state.get("current") == FLOSVIMSPURT, \
            f"flaxclimn.flosvimspurt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flosvimspurt', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'flosvimspurt', 1:
                self._state["current"] = PRONDRALSKUL
                self._state["trig"]    = "hint:1"
            case 'flosvimspurt', _:
                self._state["current"] = KRARBLANR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flosvimspurt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flosvimspurt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flosvimspurt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krarblanr(self, hint):
        assert self._state.get("current") == KRARBLANR, \
            f"flaxclimn.krarblanr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krarblanr', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'krarblanr', _:
                self._state["current"] = GRULPRORL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krarblanr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krarblanr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krarblanr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grulprorl(self, hint):
        assert self._state.get("current") == GRULPRORL, \
            f"flaxclimn.grulprorl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grulprorl', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'grulprorl', 1:
                self._state["current"] = PRONDRALSKUL
                self._state["trig"]    = "hint:1"
            case 'grulprorl', _:
                self._state["current"] = TRALSKARVAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grulprorl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grulprorl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grulprorl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _tralskarvax(self, hint):
        assert self._state.get("current") == TRALSKARVAX, \
            f"flaxclimn.tralskarvax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'tralskarvax', 2:
                self._state["current"] = KRENKRIMK
                self._state["trig"]    = "hint:2"
            case 'tralskarvax', 1:
                self._state["current"] = PRONDRALSKUL
                self._state["trig"]    = "hint:1"
            case 'tralskarvax', _:
                self._state["current"] = KRORTRALFLOST
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'tralskarvax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'tralskarvax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"tralskarvax->{_to}", _xid_val)
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
            _xid_val = _xid(__name__, 'staxskosk', "error", "assert_fail")
            _emit(cycle, 1, __name__, 'staxskosk',
                   {"hint": hint, "span": span, "caller": caller},
                   dict(ctx), _conds,
                   "entry_blocked->error", _xid_val, assertion=_asrt)
            return 2, cycle + 1

        self._state = {"current": STAXSKOSK, "ctx": ctx,
                        "span": span, "caller": caller,
                        "trig": "auto", "cycle": cycle}
        _dispatch = {
            STAXSKOSK: self._staxskosk,
            GRIMGLULSLAX: self._grimglulslax,
            DRIMKREL: self._drimkrel,
            KRAXSPELKRURK: self._kraxspelkrurk,
            GRIMGLOSSPIMK: self._grimglosspimk,
            BLORVURBLIXN: self._blorvurblixn,
            KRORBROST: self._krorbrost,
            KREXGLARR: self._krexglarr,
            STEXGLELBLEXR: self._stexglelblexr,
            GRAXSKEXGREXN: self._graxskexgrexn,
            KRALSKAX: self._kralskax,
            FLARBRONGLAX: self._flarbronglax,
            PRENKRANSKEN: self._prenkransken,
            CLULBLIMFLIXX: self._clulblimflixx,
            BLARGREXN: self._blargrexn,
            GRELSLENSLAXT: self._grelslenslaxt,
            VALSTALBRULK: self._valstalbrulk,
            STALVIMSKAN: self._stalvimskan,
            SPALBRARKRAR: self._spalbrarkrar,
            VENVIM: self._venvim,
            CLONKROS: self._clonkros,
            TROSSKELK: self._trosskelk,
            GRELSKEXX: self._grelskexx,
            GROSPROS: self._grospros,
            SLIMCLENK: self._slimclenk,
            TROSPRALVELN: self._trospralveln,
            CLAXDRORL: self._claxdrorl,
            CLEXTROR: self._clextror,
            STAXFLENR: self._staxflenr,
            SPARDREL: self._spardrel,
            CLELKREN: self._clelkren,
            GLORGLANL: self._glorglanl,
            DRONBLAXSKAL: self._dronblaxskal,
            CLURCLORR: self._clurclorr,
            KRAXKRIMGRULX: self._kraxkrimgrulx,
            SLIXKRAXSTONT: self._slixkraxstont,
            GRIMGRENGLALK: self._grimgrenglalk,
            VOSSPULN: self._vosspuln,
            CLULGRAL: self._clulgral,
            BLENCLEXFLOS: self._blenclexflos,
            DREXGLIXSTIXT: self._drexglixstixt,
            FLALPRORR: self._flalprorr,
            GRIMTRALSPANT: self._grimtralspant,
            SKANKRULBRENT: self._skankrulbrent,
            SLENSTORX: self._slenstorx,
            BRURSPAR: self._brurspar,
            CLULBROSBLAX: self._clulbrosblax,
            BRALTRAXVIX: self._braltraxvix,
            TRULGLAX: self._trulglax,
            SPANKREXKRAX: self._spankrexkrax,
            SPURKROR: self._spurkror,
            DRAXGLURL: self._draxglurl,
            TRORBRANPRORX: self._trorbranprorx,
            STELKRIXSKIXK: self._stelkrixskixk,
            KRALFLOS: self._kralflos,
            BRORGRELK: self._brorgrelk,
            CLIXSLARPRUL: self._clixslarprul,
            GLELTRORX: self._gleltrorx,
            GLENSLAXSKAL: self._glenslaxskal,
            SPULFLELGRAR: self._spulflelgrar,
            BLIMKRURL: self._blimkrurl,
            FLOSVIMSPURT: self._flosvimspurt,
            KRARBLANR: self._krarblanr,
            GRULPRORL: self._grulprorl,
            TRALSKARVAX: self._tralskarvax,
        }
        while self._state["current"] not in _R and self._state["cycle"] - cycle < 8000:
            _dispatch[self._state["current"]](hint)
        _ret     = _R.get(self._state["current"], -1)
        _is_err  = self._state["current"] == KRENKRIMK
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
    return FlaxclimnFSM().invoke(hint=hint, span=span, caller=caller, ctx=ctx, cycle=cycle)
