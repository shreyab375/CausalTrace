from _log import _w as _emit, _xid

PRULCLORFLIXK = 'prulclorflixk'
PRONPRIXCLEN = 'pronprixclen'
TROSKREN = 'troskren'
TRANSPIXDRAXT = 'transpixdraxt'
DRENPRELGREN = 'drenprelgren'
SKURBLAXR = 'skurblaxr'
TRELGLELK = 'trelglelk'
SPOSGLARDREXN = 'sposglardrexn'
FLAXSPELSLANR = 'flaxspelslanr'
GRURCLAL = 'grurclal'
BRIMKRAXVALX = 'brimkraxvalx'
KRULSPONK = 'krulsponk'
CLURBLALSPUL = 'clurblalspul'
BRENGLARL = 'brenglarl'
FLONSLOSBLAX = 'flonslosblax'
STULGLEN = 'stulglen'
DRONBLELT = 'dronblelt'
CLAXFLAR = 'claxflar'
TRALFLONR = 'tralflonr'
TRANSPIX = 'transpix'
CLULCLEX = 'clulclex'
CLALSLOS = 'clalslos'
SPARKRAL = 'sparkral'
KRELGROSL = 'krelgrosl'
TRARTRORT = 'trartrort'
SLALBLOSFLOS = 'slalblosflos'
STAXBRAXT = 'staxbraxt'
BLAXSLALFLOS = 'blaxslalflos'
SLIMSKARVENR = 'slimskarvenr'
STENDRANGRONL = 'stendrangronl'
DRULBRIXN = 'drulbrixn'
TRELSLARK = 'trelslark'
BLARTRENSTENX = 'blartrenstenx'
DRARPROSBRORK = 'drarprosbrork'
VENSLOSCLIXL = 'venslosclixl'
KRULTRONT = 'krultront'
PRIXBRAL = 'prixbral'
TRARFLAR = 'trarflar'
GRURGLUR = 'grurglur'
KRELDRURVORN = 'kreldrurvorn'
GLALBLAN = 'glalblan'
TRIMCLANTRARR = 'trimclantrarr'
GLULBLIMN = 'glulblimn'
BLAXGLEL = 'blaxglel'
PROSTRIXT = 'prostrixt'
BLOSSPAL = 'blosspal'
DRORTRANX = 'drortranx'
TRANSPIXT = 'transpixt'
TREXSTONPRIXR = 'trexstonprixr'
VEXTRALVAXL = 'vextralvaxl'
GRONTRIXGRANT = 'grontrixgrant'
PRONGRIXL = 'prongrixl'
TRORSTARL = 'trorstarl'
DRALVAL = 'dralval'
GRENCLURN = 'grenclurn'
BLALSTIXSPULT = 'blalstixspult'
PRONSPELK = 'pronspelk'
BLONBRELN = 'blonbreln'
STONBRURBLEX = 'stonbrurblex'
KRIXTREX = 'krixtrex'
SLENBRALCLEL = 'slenbralclel'
BRULFLEX = 'brulflex'
SPAXCLORN = 'spaxclorn'
GLONBLON = 'glonblon'
PREXSKEXDRORN = 'prexskexdrorn'
FLURTRULSPAXT = 'flurtrulspaxt'
SPIXSPONN = 'spixsponn'
FLONCLEXSTAX = 'flonclexstax'

_R = {
    FLURTRULSPAXT: 0,
    SPIXSPONN: 1,
    FLONCLEXSTAX: 2,
}

_CTX_READS_KEY = 'flurslex'
_CTX_THRESHOLD = 16

class ClexblaltFSM:
    def __init__(self):
        self._state = {}

    def _prulclorflixk(self, hint):
        assert self._state.get("current") == PRULCLORFLIXK, \
            f"clexblalt.prulclorflixk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prulclorflixk', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'prulclorflixk', 1:
                self._state["current"] = TROSKREN
                self._state["trig"]    = "hint:1"
            case 'prulclorflixk', _:
                self._state["current"] = PRONPRIXCLEN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prulclorflixk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prulclorflixk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prulclorflixk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _pronprixclen(self, hint):
        assert self._state.get("current") == PRONPRIXCLEN, \
            f"clexblalt.pronprixclen: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'pronprixclen', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'pronprixclen', 0:
                self._state["current"] = TRANSPIXDRAXT
                self._state["trig"]    = "hint:0"
            case 'pronprixclen', _:
                self._state["current"] = TROSKREN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'pronprixclen', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'pronprixclen',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"pronprixclen->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _troskren(self, hint):
        assert self._state.get("current") == TROSKREN, \
            f"clexblalt.troskren: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'troskren', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'troskren', 0:
                self._state["current"] = SPIXSPONN
                self._state["trig"]    = "hint:0"
            case 'troskren', _:
                self._state["current"] = TRANSPIXDRAXT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'troskren', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'troskren',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"troskren->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _transpixdraxt(self, hint):
        assert self._state.get("current") == TRANSPIXDRAXT, \
            f"clexblalt.transpixdraxt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'transpixdraxt', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'transpixdraxt', _:
                self._state["current"] = DRENPRELGREN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'transpixdraxt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'transpixdraxt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"transpixdraxt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drenprelgren(self, hint):
        assert self._state.get("current") == DRENPRELGREN, \
            f"clexblalt.drenprelgren: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drenprelgren', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'drenprelgren', 0:
                self._state["current"] = TRELGLELK
                self._state["trig"]    = "hint:0"
            case 'drenprelgren', _:
                self._state["current"] = SKURBLAXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drenprelgren', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drenprelgren',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drenprelgren->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skurblaxr(self, hint):
        assert self._state.get("current") == SKURBLAXR, \
            f"clexblalt.skurblaxr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skurblaxr', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'skurblaxr', _:
                self._state["current"] = TRELGLELK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skurblaxr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skurblaxr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skurblaxr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trelglelk(self, hint):
        assert self._state.get("current") == TRELGLELK, \
            f"clexblalt.trelglelk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trelglelk', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'trelglelk', 0:
                self._state["current"] = FLAXSPELSLANR
                self._state["trig"]    = "hint:0"
            case 'trelglelk', _:
                self._state["current"] = SPOSGLARDREXN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trelglelk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trelglelk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trelglelk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _sposglardrexn(self, hint):
        assert self._state.get("current") == SPOSGLARDREXN, \
            f"clexblalt.sposglardrexn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'sposglardrexn', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'sposglardrexn', _:
                self._state["current"] = FLAXSPELSLANR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'sposglardrexn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'sposglardrexn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"sposglardrexn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flaxspelslanr(self, hint):
        assert self._state.get("current") == FLAXSPELSLANR, \
            f"clexblalt.flaxspelslanr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flaxspelslanr', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'flaxspelslanr', _:
                self._state["current"] = GRURCLAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flaxspelslanr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flaxspelslanr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flaxspelslanr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grurclal(self, hint):
        assert self._state.get("current") == GRURCLAL, \
            f"clexblalt.grurclal: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grurclal', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'grurclal', _:
                self._state["current"] = BRIMKRAXVALX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grurclal', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grurclal',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grurclal->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brimkraxvalx(self, hint):
        assert self._state.get("current") == BRIMKRAXVALX, \
            f"clexblalt.brimkraxvalx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brimkraxvalx', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'brimkraxvalx', 1:
                self._state["current"] = CLURBLALSPUL
                self._state["trig"]    = "hint:1"
            case 'brimkraxvalx', _:
                self._state["current"] = KRULSPONK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brimkraxvalx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brimkraxvalx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brimkraxvalx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krulsponk(self, hint):
        assert self._state.get("current") == KRULSPONK, \
            f"clexblalt.krulsponk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krulsponk', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'krulsponk', 1:
                self._state["current"] = SPIXSPONN
                self._state["trig"]    = "hint:1"
            case 'krulsponk', _:
                self._state["current"] = CLURBLALSPUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krulsponk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krulsponk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krulsponk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clurblalspul(self, hint):
        assert self._state.get("current") == CLURBLALSPUL, \
            f"clexblalt.clurblalspul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clurblalspul', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'clurblalspul', _:
                self._state["current"] = BRENGLARL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clurblalspul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clurblalspul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clurblalspul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brenglarl(self, hint):
        assert self._state.get("current") == BRENGLARL, \
            f"clexblalt.brenglarl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brenglarl', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'brenglarl', _:
                self._state["current"] = FLONSLOSBLAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brenglarl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brenglarl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brenglarl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flonslosblax(self, hint):
        assert self._state.get("current") == FLONSLOSBLAX, \
            f"clexblalt.flonslosblax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flonslosblax', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'flonslosblax', 1:
                self._state["current"] = DRONBLELT
                self._state["trig"]    = "hint:1"
            case 'flonslosblax', _:
                self._state["current"] = STULGLEN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flonslosblax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flonslosblax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flonslosblax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stulglen(self, hint):
        assert self._state.get("current") == STULGLEN, \
            f"clexblalt.stulglen: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stulglen', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'stulglen', _:
                self._state["current"] = DRONBLELT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stulglen', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stulglen',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stulglen->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _dronblelt(self, hint):
        assert self._state.get("current") == DRONBLELT, \
            f"clexblalt.dronblelt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'dronblelt', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'dronblelt', 1:
                self._state["current"] = TRALFLONR
                self._state["trig"]    = "hint:1"
            case 'dronblelt', _:
                self._state["current"] = CLAXFLAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'dronblelt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'dronblelt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"dronblelt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _claxflar(self, hint):
        assert self._state.get("current") == CLAXFLAR, \
            f"clexblalt.claxflar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'claxflar', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'claxflar', _:
                self._state["current"] = TRALFLONR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'claxflar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'claxflar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"claxflar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _tralflonr(self, hint):
        assert self._state.get("current") == TRALFLONR, \
            f"clexblalt.tralflonr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'tralflonr', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'tralflonr', _:
                self._state["current"] = TRANSPIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'tralflonr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'tralflonr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"tralflonr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _transpix(self, hint):
        assert self._state.get("current") == TRANSPIX, \
            f"clexblalt.transpix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'transpix', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'transpix', _:
                self._state["current"] = CLULCLEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'transpix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'transpix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"transpix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clulclex(self, hint):
        assert self._state.get("current") == CLULCLEX, \
            f"clexblalt.clulclex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clulclex', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'clulclex', _:
                self._state["current"] = CLALSLOS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clulclex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clulclex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clulclex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clalslos(self, hint):
        assert self._state.get("current") == CLALSLOS, \
            f"clexblalt.clalslos: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clalslos', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'clalslos', 1:
                self._state["current"] = SPIXSPONN
                self._state["trig"]    = "hint:1"
            case 'clalslos', _:
                self._state["current"] = SPARKRAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clalslos', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clalslos',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clalslos->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _sparkral(self, hint):
        assert self._state.get("current") == SPARKRAL, \
            f"clexblalt.sparkral: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'sparkral', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'sparkral', _:
                self._state["current"] = KRELGROSL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'sparkral', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'sparkral',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"sparkral->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krelgrosl(self, hint):
        assert self._state.get("current") == KRELGROSL, \
            f"clexblalt.krelgrosl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krelgrosl', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'krelgrosl', _:
                self._state["current"] = TRARTRORT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krelgrosl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krelgrosl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krelgrosl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trartrort(self, hint):
        assert self._state.get("current") == TRARTRORT, \
            f"clexblalt.trartrort: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trartrort', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'trartrort', _:
                self._state["current"] = SLALBLOSFLOS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trartrort', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trartrort',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trartrort->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slalblosflos(self, hint):
        assert self._state.get("current") == SLALBLOSFLOS, \
            f"clexblalt.slalblosflos: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slalblosflos', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'slalblosflos', _:
                self._state["current"] = STAXBRAXT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slalblosflos', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slalblosflos',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slalblosflos->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _staxbraxt(self, hint):
        assert self._state.get("current") == STAXBRAXT, \
            f"clexblalt.staxbraxt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'staxbraxt', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'staxbraxt', 1:
                self._state["current"] = SLIMSKARVENR
                self._state["trig"]    = "hint:1"
            case 'staxbraxt', _:
                self._state["current"] = BLAXSLALFLOS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'staxbraxt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'staxbraxt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"staxbraxt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blaxslalflos(self, hint):
        assert self._state.get("current") == BLAXSLALFLOS, \
            f"clexblalt.blaxslalflos: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blaxslalflos', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'blaxslalflos', _:
                self._state["current"] = SLIMSKARVENR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blaxslalflos', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blaxslalflos',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blaxslalflos->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slimskarvenr(self, hint):
        assert self._state.get("current") == SLIMSKARVENR, \
            f"clexblalt.slimskarvenr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slimskarvenr', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'slimskarvenr', _:
                self._state["current"] = STENDRANGRONL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slimskarvenr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slimskarvenr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slimskarvenr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stendrangronl(self, hint):
        assert self._state.get("current") == STENDRANGRONL, \
            f"clexblalt.stendrangronl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stendrangronl', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'stendrangronl', _:
                self._state["current"] = DRULBRIXN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stendrangronl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stendrangronl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stendrangronl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drulbrixn(self, hint):
        assert self._state.get("current") == DRULBRIXN, \
            f"clexblalt.drulbrixn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drulbrixn', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'drulbrixn', 0:
                self._state["current"] = SPIXSPONN
                self._state["trig"]    = "hint:0"
            case 'drulbrixn', _:
                self._state["current"] = TRELSLARK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drulbrixn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drulbrixn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drulbrixn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trelslark(self, hint):
        assert self._state.get("current") == TRELSLARK, \
            f"clexblalt.trelslark: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trelslark', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'trelslark', 1:
                self._state["current"] = DRARPROSBRORK
                self._state["trig"]    = "hint:1"
            case 'trelslark', _:
                self._state["current"] = BLARTRENSTENX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trelslark', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trelslark',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trelslark->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blartrenstenx(self, hint):
        assert self._state.get("current") == BLARTRENSTENX, \
            f"clexblalt.blartrenstenx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blartrenstenx', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'blartrenstenx', 1:
                self._state["current"] = VENSLOSCLIXL
                self._state["trig"]    = "hint:1"
            case 'blartrenstenx', _:
                self._state["current"] = DRARPROSBRORK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blartrenstenx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blartrenstenx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blartrenstenx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drarprosbrork(self, hint):
        assert self._state.get("current") == DRARPROSBRORK, \
            f"clexblalt.drarprosbrork: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drarprosbrork', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'drarprosbrork', _:
                self._state["current"] = VENSLOSCLIXL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drarprosbrork', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drarprosbrork',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drarprosbrork->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _venslosclixl(self, hint):
        assert self._state.get("current") == VENSLOSCLIXL, \
            f"clexblalt.venslosclixl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'venslosclixl', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'venslosclixl', 1:
                self._state["current"] = PRIXBRAL
                self._state["trig"]    = "hint:1"
            case 'venslosclixl', _:
                self._state["current"] = KRULTRONT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'venslosclixl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'venslosclixl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"venslosclixl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krultront(self, hint):
        assert self._state.get("current") == KRULTRONT, \
            f"clexblalt.krultront: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krultront', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'krultront', _:
                self._state["current"] = PRIXBRAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krultront', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krultront',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krultront->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prixbral(self, hint):
        assert self._state.get("current") == PRIXBRAL, \
            f"clexblalt.prixbral: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prixbral', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'prixbral', 0:
                self._state["current"] = GRURGLUR
                self._state["trig"]    = "hint:0"
            case 'prixbral', _:
                self._state["current"] = TRARFLAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prixbral', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prixbral',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prixbral->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trarflar(self, hint):
        assert self._state.get("current") == TRARFLAR, \
            f"clexblalt.trarflar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trarflar', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'trarflar', _:
                self._state["current"] = GRURGLUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trarflar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trarflar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trarflar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grurglur(self, hint):
        assert self._state.get("current") == GRURGLUR, \
            f"clexblalt.grurglur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grurglur', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'grurglur', _:
                self._state["current"] = KRELDRURVORN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grurglur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grurglur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grurglur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _kreldrurvorn(self, hint):
        assert self._state.get("current") == KRELDRURVORN, \
            f"clexblalt.kreldrurvorn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'kreldrurvorn', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'kreldrurvorn', 0:
                self._state["current"] = TRIMCLANTRARR
                self._state["trig"]    = "hint:0"
            case 'kreldrurvorn', _:
                self._state["current"] = GLALBLAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'kreldrurvorn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'kreldrurvorn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"kreldrurvorn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glalblan(self, hint):
        assert self._state.get("current") == GLALBLAN, \
            f"clexblalt.glalblan: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glalblan', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'glalblan', 1:
                self._state["current"] = SPIXSPONN
                self._state["trig"]    = "hint:1"
            case 'glalblan', _:
                self._state["current"] = TRIMCLANTRARR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glalblan', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glalblan',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glalblan->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trimclantrarr(self, hint):
        assert self._state.get("current") == TRIMCLANTRARR, \
            f"clexblalt.trimclantrarr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trimclantrarr', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'trimclantrarr', 0:
                self._state["current"] = BLAXGLEL
                self._state["trig"]    = "hint:0"
            case 'trimclantrarr', _:
                self._state["current"] = GLULBLIMN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trimclantrarr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trimclantrarr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trimclantrarr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glulblimn(self, hint):
        assert self._state.get("current") == GLULBLIMN, \
            f"clexblalt.glulblimn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glulblimn', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'glulblimn', _:
                self._state["current"] = BLAXGLEL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glulblimn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glulblimn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glulblimn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blaxglel(self, hint):
        assert self._state.get("current") == BLAXGLEL, \
            f"clexblalt.blaxglel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blaxglel', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'blaxglel', 0:
                self._state["current"] = BLOSSPAL
                self._state["trig"]    = "hint:0"
            case 'blaxglel', _:
                self._state["current"] = PROSTRIXT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blaxglel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blaxglel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blaxglel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prostrixt(self, hint):
        assert self._state.get("current") == PROSTRIXT, \
            f"clexblalt.prostrixt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prostrixt', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'prostrixt', _:
                self._state["current"] = BLOSSPAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prostrixt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prostrixt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prostrixt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blosspal(self, hint):
        assert self._state.get("current") == BLOSSPAL, \
            f"clexblalt.blosspal: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blosspal', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'blosspal', _:
                self._state["current"] = DRORTRANX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blosspal', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blosspal',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blosspal->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drortranx(self, hint):
        assert self._state.get("current") == DRORTRANX, \
            f"clexblalt.drortranx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drortranx', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'drortranx', _:
                self._state["current"] = TRANSPIXT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drortranx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drortranx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drortranx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _transpixt(self, hint):
        assert self._state.get("current") == TRANSPIXT, \
            f"clexblalt.transpixt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'transpixt', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'transpixt', 0:
                self._state["current"] = VEXTRALVAXL
                self._state["trig"]    = "hint:0"
            case 'transpixt', _:
                self._state["current"] = TREXSTONPRIXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'transpixt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'transpixt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"transpixt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trexstonprixr(self, hint):
        assert self._state.get("current") == TREXSTONPRIXR, \
            f"clexblalt.trexstonprixr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trexstonprixr', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'trexstonprixr', 0:
                self._state["current"] = GRONTRIXGRANT
                self._state["trig"]    = "hint:0"
            case 'trexstonprixr', _:
                self._state["current"] = VEXTRALVAXL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trexstonprixr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trexstonprixr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trexstonprixr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vextralvaxl(self, hint):
        assert self._state.get("current") == VEXTRALVAXL, \
            f"clexblalt.vextralvaxl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vextralvaxl', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'vextralvaxl', _:
                self._state["current"] = GRONTRIXGRANT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vextralvaxl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vextralvaxl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vextralvaxl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grontrixgrant(self, hint):
        assert self._state.get("current") == GRONTRIXGRANT, \
            f"clexblalt.grontrixgrant: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grontrixgrant', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'grontrixgrant', 1:
                self._state["current"] = TRORSTARL
                self._state["trig"]    = "hint:1"
            case 'grontrixgrant', _:
                self._state["current"] = PRONGRIXL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grontrixgrant', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grontrixgrant',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grontrixgrant->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prongrixl(self, hint):
        assert self._state.get("current") == PRONGRIXL, \
            f"clexblalt.prongrixl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prongrixl', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'prongrixl', 1:
                self._state["current"] = SPIXSPONN
                self._state["trig"]    = "hint:1"
            case 'prongrixl', _:
                self._state["current"] = TRORSTARL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prongrixl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prongrixl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prongrixl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trorstarl(self, hint):
        assert self._state.get("current") == TRORSTARL, \
            f"clexblalt.trorstarl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trorstarl', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'trorstarl', _:
                self._state["current"] = DRALVAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trorstarl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trorstarl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trorstarl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _dralval(self, hint):
        assert self._state.get("current") == DRALVAL, \
            f"clexblalt.dralval: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'dralval', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'dralval', 1:
                self._state["current"] = BLALSTIXSPULT
                self._state["trig"]    = "hint:1"
            case 'dralval', _:
                self._state["current"] = GRENCLURN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'dralval', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'dralval',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"dralval->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grenclurn(self, hint):
        assert self._state.get("current") == GRENCLURN, \
            f"clexblalt.grenclurn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grenclurn', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'grenclurn', 1:
                self._state["current"] = PRONSPELK
                self._state["trig"]    = "hint:1"
            case 'grenclurn', _:
                self._state["current"] = BLALSTIXSPULT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grenclurn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grenclurn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grenclurn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blalstixspult(self, hint):
        assert self._state.get("current") == BLALSTIXSPULT, \
            f"clexblalt.blalstixspult: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blalstixspult', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'blalstixspult', 0:
                self._state["current"] = BLONBRELN
                self._state["trig"]    = "hint:0"
            case 'blalstixspult', _:
                self._state["current"] = PRONSPELK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blalstixspult', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blalstixspult',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blalstixspult->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _pronspelk(self, hint):
        assert self._state.get("current") == PRONSPELK, \
            f"clexblalt.pronspelk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'pronspelk', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'pronspelk', _:
                self._state["current"] = BLONBRELN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'pronspelk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'pronspelk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"pronspelk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blonbreln(self, hint):
        assert self._state.get("current") == BLONBRELN, \
            f"clexblalt.blonbreln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blonbreln', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'blonbreln', 1:
                self._state["current"] = KRIXTREX
                self._state["trig"]    = "hint:1"
            case 'blonbreln', _:
                self._state["current"] = STONBRURBLEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blonbreln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blonbreln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blonbreln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stonbrurblex(self, hint):
        assert self._state.get("current") == STONBRURBLEX, \
            f"clexblalt.stonbrurblex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stonbrurblex', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'stonbrurblex', 0:
                self._state["current"] = SLENBRALCLEL
                self._state["trig"]    = "hint:0"
            case 'stonbrurblex', _:
                self._state["current"] = KRIXTREX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stonbrurblex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stonbrurblex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stonbrurblex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krixtrex(self, hint):
        assert self._state.get("current") == KRIXTREX, \
            f"clexblalt.krixtrex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krixtrex', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'krixtrex', 1:
                self._state["current"] = BRULFLEX
                self._state["trig"]    = "hint:1"
            case 'krixtrex', _:
                self._state["current"] = SLENBRALCLEL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krixtrex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krixtrex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krixtrex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slenbralclel(self, hint):
        assert self._state.get("current") == SLENBRALCLEL, \
            f"clexblalt.slenbralclel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slenbralclel', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'slenbralclel', 1:
                self._state["current"] = SPAXCLORN
                self._state["trig"]    = "hint:1"
            case 'slenbralclel', _:
                self._state["current"] = BRULFLEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slenbralclel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slenbralclel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slenbralclel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brulflex(self, hint):
        assert self._state.get("current") == BRULFLEX, \
            f"clexblalt.brulflex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brulflex', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'brulflex', _:
                self._state["current"] = SPAXCLORN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brulflex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brulflex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brulflex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spaxclorn(self, hint):
        assert self._state.get("current") == SPAXCLORN, \
            f"clexblalt.spaxclorn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spaxclorn', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'spaxclorn', _:
                self._state["current"] = GLONBLON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spaxclorn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spaxclorn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spaxclorn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glonblon(self, hint):
        assert self._state.get("current") == GLONBLON, \
            f"clexblalt.glonblon: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glonblon', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'glonblon', _:
                self._state["current"] = PREXSKEXDRORN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glonblon', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glonblon',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glonblon->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prexskexdrorn(self, hint):
        assert self._state.get("current") == PREXSKEXDRORN, \
            f"clexblalt.prexskexdrorn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prexskexdrorn', 2:
                self._state["current"] = FLONCLEXSTAX
                self._state["trig"]    = "hint:2"
            case 'prexskexdrorn', _:
                self._state["current"] = FLURTRULSPAXT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prexskexdrorn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prexskexdrorn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prexskexdrorn->{_to}", _xid_val)
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
            _xid_val = _xid(__name__, 'prulclorflixk', "error", "assert_fail")
            _emit(cycle, 1, __name__, 'prulclorflixk',
                   {"hint": hint, "span": span, "caller": caller},
                   dict(ctx), _conds,
                   "entry_blocked->error", _xid_val, assertion=_asrt)
            return 2, cycle + 1

        self._state = {"current": PRULCLORFLIXK, "ctx": ctx,
                        "span": span, "caller": caller,
                        "trig": "auto", "cycle": cycle}
        _dispatch = {
            PRULCLORFLIXK: self._prulclorflixk,
            PRONPRIXCLEN: self._pronprixclen,
            TROSKREN: self._troskren,
            TRANSPIXDRAXT: self._transpixdraxt,
            DRENPRELGREN: self._drenprelgren,
            SKURBLAXR: self._skurblaxr,
            TRELGLELK: self._trelglelk,
            SPOSGLARDREXN: self._sposglardrexn,
            FLAXSPELSLANR: self._flaxspelslanr,
            GRURCLAL: self._grurclal,
            BRIMKRAXVALX: self._brimkraxvalx,
            KRULSPONK: self._krulsponk,
            CLURBLALSPUL: self._clurblalspul,
            BRENGLARL: self._brenglarl,
            FLONSLOSBLAX: self._flonslosblax,
            STULGLEN: self._stulglen,
            DRONBLELT: self._dronblelt,
            CLAXFLAR: self._claxflar,
            TRALFLONR: self._tralflonr,
            TRANSPIX: self._transpix,
            CLULCLEX: self._clulclex,
            CLALSLOS: self._clalslos,
            SPARKRAL: self._sparkral,
            KRELGROSL: self._krelgrosl,
            TRARTRORT: self._trartrort,
            SLALBLOSFLOS: self._slalblosflos,
            STAXBRAXT: self._staxbraxt,
            BLAXSLALFLOS: self._blaxslalflos,
            SLIMSKARVENR: self._slimskarvenr,
            STENDRANGRONL: self._stendrangronl,
            DRULBRIXN: self._drulbrixn,
            TRELSLARK: self._trelslark,
            BLARTRENSTENX: self._blartrenstenx,
            DRARPROSBRORK: self._drarprosbrork,
            VENSLOSCLIXL: self._venslosclixl,
            KRULTRONT: self._krultront,
            PRIXBRAL: self._prixbral,
            TRARFLAR: self._trarflar,
            GRURGLUR: self._grurglur,
            KRELDRURVORN: self._kreldrurvorn,
            GLALBLAN: self._glalblan,
            TRIMCLANTRARR: self._trimclantrarr,
            GLULBLIMN: self._glulblimn,
            BLAXGLEL: self._blaxglel,
            PROSTRIXT: self._prostrixt,
            BLOSSPAL: self._blosspal,
            DRORTRANX: self._drortranx,
            TRANSPIXT: self._transpixt,
            TREXSTONPRIXR: self._trexstonprixr,
            VEXTRALVAXL: self._vextralvaxl,
            GRONTRIXGRANT: self._grontrixgrant,
            PRONGRIXL: self._prongrixl,
            TRORSTARL: self._trorstarl,
            DRALVAL: self._dralval,
            GRENCLURN: self._grenclurn,
            BLALSTIXSPULT: self._blalstixspult,
            PRONSPELK: self._pronspelk,
            BLONBRELN: self._blonbreln,
            STONBRURBLEX: self._stonbrurblex,
            KRIXTREX: self._krixtrex,
            SLENBRALCLEL: self._slenbralclel,
            BRULFLEX: self._brulflex,
            SPAXCLORN: self._spaxclorn,
            GLONBLON: self._glonblon,
            PREXSKEXDRORN: self._prexskexdrorn,
        }
        while self._state["current"] not in _R and self._state["cycle"] - cycle < 8000:
            _dispatch[self._state["current"]](hint)
        _ret     = _R.get(self._state["current"], -1)
        _is_err  = self._state["current"] == FLONCLEXSTAX
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
    return ClexblaltFSM().invoke(hint=hint, span=span, caller=caller, ctx=ctx, cycle=cycle)
