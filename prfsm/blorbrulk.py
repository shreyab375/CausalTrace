from _log import _w as _emit, _xid

FLANSLAL = 'flanslal'
SPOSTREXR = 'spostrexr'
DROSBREL = 'drosbrel'
PRORBLORN = 'prorblorn'
BLEXDRUL = 'blexdrul'
KRONBLIXTROR = 'kronblixtror'
STIMBRALBLAX = 'stimbralblax'
DRENTRULKRARN = 'drentrulkrarn'
GLORSKURBRAN = 'glorskurbran'
SKELGLAXSPEXK = 'skelglaxspexk'
STULBRAXR = 'stulbraxr'
DRENKRONBRIXX = 'drenkronbrixx'
VOSFLON = 'vosflon'
TRULTRONGRULK = 'trultrongrulk'
TRANSLELN = 'transleln'
BLURTRAX = 'blurtrax'
FLONBRALCLEN = 'flonbralclen'
SLULCLIXBLARL = 'slulclixblarl'
CLALPRORR = 'clalprorr'
STIXSPIM = 'stixspim'
VELGLEL = 'velglel'
TRONSPELFLIX = 'tronspelflix'
SKULSTONN = 'skulstonn'
SPAXCLULGLON = 'spaxclulglon'
PRIMGLURX = 'primglurx'
CLIXSLONTRONX = 'clixslontronx'
VELDRURCLULK = 'veldrurclulk'
CLULKRORGROR = 'clulkrorgror'
BRORFLELX = 'brorflelx'
BLANCLOR = 'blanclor'
STOSTRAR = 'stostrar'
SKALKRELR = 'skalkrelr'
STELGRAN = 'stelgran'
BRALGLELVANT = 'bralglelvant'
DRIXFLURN = 'drixflurn'
SLARBRURGRIML = 'slarbrurgriml'
GROSBLENPRULT = 'grosblenprult'
SKENGLELVAR = 'skenglelvar'
CLOSSLORVIMN = 'closslorvimn'
CLURSKIXGRAR = 'clurskixgrar'
FLULPRIXVAL = 'flulprixval'
VALGROSVUR = 'valgrosvur'
BLIMBRULCLIM = 'blimbrulclim'
TRARPROSCLEL = 'trarprosclel'
SPIXCLORSKEX = 'spixclorskex'
KRARGLELK = 'krarglelk'
KRARDRARPREXX = 'krardrarprexx'
GLALCLELK = 'glalclelk'
KRENSLUL = 'krenslul'
CLAXPRAR = 'claxprar'
PRORSLEX = 'prorslex'
DRURCLENSKIX = 'drurclenskix'
PRENTRON = 'prentron'
PRALGLEXSKUL = 'pralglexskul'
STELSTELL = 'stelstell'
CLELSPENL = 'clelspenl'
SPONVAXVIMR = 'sponvaxvimr'
GRURGRURPRURK = 'grurgrurprurk'
DRULVEX = 'drulvex'
KROSSTOSBLAR = 'krosstosblar'
SPAXKRON = 'spaxkron'
SPENSTEX = 'spenstex'
STOSCLIMX = 'stosclimx'
STONTRANGLENK = 'stontranglenk'
SKONSLURK = 'skonslurk'
SLOSGLOR = 'slosglor'
STOSPROSKRANL = 'stosproskranl'
PRARGRURTRULK = 'prargrurtrulk'

_R = {
    SLOSGLOR: 0,
    STOSPROSKRANL: 1,
    PRARGRURTRULK: 2,
}

_CTX_READS_KEY = 'flurslex'
_CTX_THRESHOLD = 16

class BlorbrulkFSM:
    def __init__(self):
        self._state = {}

    def _flanslal(self, hint):
        assert self._state.get("current") == FLANSLAL, \
            f"blorbrulk.flanslal: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flanslal', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'flanslal', 0:
                self._state["current"] = STOSPROSKRANL
                self._state["trig"]    = "hint:0"
            case 'flanslal', _:
                self._state["current"] = SPOSTREXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flanslal', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flanslal',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flanslal->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spostrexr(self, hint):
        assert self._state.get("current") == SPOSTREXR, \
            f"blorbrulk.spostrexr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spostrexr', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'spostrexr', 1:
                self._state["current"] = PRORBLORN
                self._state["trig"]    = "hint:1"
            case 'spostrexr', _:
                self._state["current"] = DROSBREL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spostrexr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spostrexr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spostrexr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drosbrel(self, hint):
        assert self._state.get("current") == DROSBREL, \
            f"blorbrulk.drosbrel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drosbrel', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'drosbrel', _:
                self._state["current"] = PRORBLORN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drosbrel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drosbrel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drosbrel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prorblorn(self, hint):
        assert self._state.get("current") == PRORBLORN, \
            f"blorbrulk.prorblorn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prorblorn', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'prorblorn', _:
                self._state["current"] = BLEXDRUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prorblorn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prorblorn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prorblorn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blexdrul(self, hint):
        assert self._state.get("current") == BLEXDRUL, \
            f"blorbrulk.blexdrul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blexdrul', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'blexdrul', 0:
                self._state["current"] = STIMBRALBLAX
                self._state["trig"]    = "hint:0"
            case 'blexdrul', _:
                self._state["current"] = KRONBLIXTROR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blexdrul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blexdrul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blexdrul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _kronblixtror(self, hint):
        assert self._state.get("current") == KRONBLIXTROR, \
            f"blorbrulk.kronblixtror: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'kronblixtror', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'kronblixtror', 1:
                self._state["current"] = STOSPROSKRANL
                self._state["trig"]    = "hint:1"
            case 'kronblixtror', _:
                self._state["current"] = STIMBRALBLAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'kronblixtror', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'kronblixtror',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"kronblixtror->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stimbralblax(self, hint):
        assert self._state.get("current") == STIMBRALBLAX, \
            f"blorbrulk.stimbralblax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stimbralblax', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'stimbralblax', _:
                self._state["current"] = DRENTRULKRARN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stimbralblax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stimbralblax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stimbralblax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drentrulkrarn(self, hint):
        assert self._state.get("current") == DRENTRULKRARN, \
            f"blorbrulk.drentrulkrarn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drentrulkrarn', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'drentrulkrarn', 0:
                self._state["current"] = SKELGLAXSPEXK
                self._state["trig"]    = "hint:0"
            case 'drentrulkrarn', _:
                self._state["current"] = GLORSKURBRAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drentrulkrarn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drentrulkrarn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drentrulkrarn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glorskurbran(self, hint):
        assert self._state.get("current") == GLORSKURBRAN, \
            f"blorbrulk.glorskurbran: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glorskurbran', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'glorskurbran', 0:
                self._state["current"] = STULBRAXR
                self._state["trig"]    = "hint:0"
            case 'glorskurbran', _:
                self._state["current"] = SKELGLAXSPEXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glorskurbran', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glorskurbran',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glorskurbran->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skelglaxspexk(self, hint):
        assert self._state.get("current") == SKELGLAXSPEXK, \
            f"blorbrulk.skelglaxspexk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skelglaxspexk', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'skelglaxspexk', 1:
                self._state["current"] = DRENKRONBRIXX
                self._state["trig"]    = "hint:1"
            case 'skelglaxspexk', _:
                self._state["current"] = STULBRAXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skelglaxspexk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skelglaxspexk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skelglaxspexk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stulbraxr(self, hint):
        assert self._state.get("current") == STULBRAXR, \
            f"blorbrulk.stulbraxr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stulbraxr', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'stulbraxr', _:
                self._state["current"] = DRENKRONBRIXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stulbraxr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stulbraxr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stulbraxr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drenkronbrixx(self, hint):
        assert self._state.get("current") == DRENKRONBRIXX, \
            f"blorbrulk.drenkronbrixx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drenkronbrixx', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'drenkronbrixx', 1:
                self._state["current"] = TRULTRONGRULK
                self._state["trig"]    = "hint:1"
            case 'drenkronbrixx', _:
                self._state["current"] = VOSFLON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drenkronbrixx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drenkronbrixx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drenkronbrixx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vosflon(self, hint):
        assert self._state.get("current") == VOSFLON, \
            f"blorbrulk.vosflon: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vosflon', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'vosflon', _:
                self._state["current"] = TRULTRONGRULK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vosflon', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vosflon',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vosflon->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trultrongrulk(self, hint):
        assert self._state.get("current") == TRULTRONGRULK, \
            f"blorbrulk.trultrongrulk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trultrongrulk', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'trultrongrulk', 1:
                self._state["current"] = STOSPROSKRANL
                self._state["trig"]    = "hint:1"
            case 'trultrongrulk', _:
                self._state["current"] = TRANSLELN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trultrongrulk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trultrongrulk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trultrongrulk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _transleln(self, hint):
        assert self._state.get("current") == TRANSLELN, \
            f"blorbrulk.transleln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'transleln', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'transleln', _:
                self._state["current"] = BLURTRAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'transleln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'transleln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"transleln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blurtrax(self, hint):
        assert self._state.get("current") == BLURTRAX, \
            f"blorbrulk.blurtrax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blurtrax', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'blurtrax', _:
                self._state["current"] = FLONBRALCLEN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blurtrax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blurtrax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blurtrax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flonbralclen(self, hint):
        assert self._state.get("current") == FLONBRALCLEN, \
            f"blorbrulk.flonbralclen: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flonbralclen', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'flonbralclen', 0:
                self._state["current"] = CLALPRORR
                self._state["trig"]    = "hint:0"
            case 'flonbralclen', _:
                self._state["current"] = SLULCLIXBLARL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flonbralclen', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flonbralclen',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flonbralclen->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slulclixblarl(self, hint):
        assert self._state.get("current") == SLULCLIXBLARL, \
            f"blorbrulk.slulclixblarl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slulclixblarl', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'slulclixblarl', 1:
                self._state["current"] = STOSPROSKRANL
                self._state["trig"]    = "hint:1"
            case 'slulclixblarl', _:
                self._state["current"] = CLALPRORR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slulclixblarl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slulclixblarl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slulclixblarl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clalprorr(self, hint):
        assert self._state.get("current") == CLALPRORR, \
            f"blorbrulk.clalprorr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clalprorr', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'clalprorr', _:
                self._state["current"] = STIXSPIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clalprorr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clalprorr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clalprorr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stixspim(self, hint):
        assert self._state.get("current") == STIXSPIM, \
            f"blorbrulk.stixspim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stixspim', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'stixspim', _:
                self._state["current"] = VELGLEL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stixspim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stixspim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stixspim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _velglel(self, hint):
        assert self._state.get("current") == VELGLEL, \
            f"blorbrulk.velglel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'velglel', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'velglel', _:
                self._state["current"] = TRONSPELFLIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'velglel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'velglel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"velglel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _tronspelflix(self, hint):
        assert self._state.get("current") == TRONSPELFLIX, \
            f"blorbrulk.tronspelflix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'tronspelflix', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'tronspelflix', 0:
                self._state["current"] = STOSPROSKRANL
                self._state["trig"]    = "hint:0"
            case 'tronspelflix', _:
                self._state["current"] = SKULSTONN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'tronspelflix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'tronspelflix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"tronspelflix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skulstonn(self, hint):
        assert self._state.get("current") == SKULSTONN, \
            f"blorbrulk.skulstonn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skulstonn', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'skulstonn', _:
                self._state["current"] = SPAXCLULGLON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skulstonn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skulstonn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skulstonn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spaxclulglon(self, hint):
        assert self._state.get("current") == SPAXCLULGLON, \
            f"blorbrulk.spaxclulglon: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spaxclulglon', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'spaxclulglon', _:
                self._state["current"] = PRIMGLURX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spaxclulglon', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spaxclulglon',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spaxclulglon->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _primglurx(self, hint):
        assert self._state.get("current") == PRIMGLURX, \
            f"blorbrulk.primglurx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'primglurx', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'primglurx', 1:
                self._state["current"] = STOSPROSKRANL
                self._state["trig"]    = "hint:1"
            case 'primglurx', _:
                self._state["current"] = CLIXSLONTRONX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'primglurx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'primglurx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"primglurx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clixslontronx(self, hint):
        assert self._state.get("current") == CLIXSLONTRONX, \
            f"blorbrulk.clixslontronx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clixslontronx', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'clixslontronx', 0:
                self._state["current"] = CLULKRORGROR
                self._state["trig"]    = "hint:0"
            case 'clixslontronx', _:
                self._state["current"] = VELDRURCLULK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clixslontronx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clixslontronx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clixslontronx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _veldrurclulk(self, hint):
        assert self._state.get("current") == VELDRURCLULK, \
            f"blorbrulk.veldrurclulk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'veldrurclulk', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'veldrurclulk', 0:
                self._state["current"] = BRORFLELX
                self._state["trig"]    = "hint:0"
            case 'veldrurclulk', _:
                self._state["current"] = CLULKRORGROR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'veldrurclulk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'veldrurclulk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"veldrurclulk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clulkrorgror(self, hint):
        assert self._state.get("current") == CLULKRORGROR, \
            f"blorbrulk.clulkrorgror: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clulkrorgror', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'clulkrorgror', _:
                self._state["current"] = BRORFLELX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clulkrorgror', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clulkrorgror',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clulkrorgror->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brorflelx(self, hint):
        assert self._state.get("current") == BRORFLELX, \
            f"blorbrulk.brorflelx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brorflelx', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'brorflelx', _:
                self._state["current"] = BLANCLOR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brorflelx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brorflelx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brorflelx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blanclor(self, hint):
        assert self._state.get("current") == BLANCLOR, \
            f"blorbrulk.blanclor: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blanclor', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'blanclor', 0:
                self._state["current"] = SKALKRELR
                self._state["trig"]    = "hint:0"
            case 'blanclor', _:
                self._state["current"] = STOSTRAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blanclor', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blanclor',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blanclor->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stostrar(self, hint):
        assert self._state.get("current") == STOSTRAR, \
            f"blorbrulk.stostrar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stostrar', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'stostrar', 1:
                self._state["current"] = STOSPROSKRANL
                self._state["trig"]    = "hint:1"
            case 'stostrar', _:
                self._state["current"] = SKALKRELR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stostrar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stostrar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stostrar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skalkrelr(self, hint):
        assert self._state.get("current") == SKALKRELR, \
            f"blorbrulk.skalkrelr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skalkrelr', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'skalkrelr', _:
                self._state["current"] = STELGRAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skalkrelr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skalkrelr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skalkrelr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stelgran(self, hint):
        assert self._state.get("current") == STELGRAN, \
            f"blorbrulk.stelgran: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stelgran', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'stelgran', 0:
                self._state["current"] = DRIXFLURN
                self._state["trig"]    = "hint:0"
            case 'stelgran', _:
                self._state["current"] = BRALGLELVANT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stelgran', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stelgran',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stelgran->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _bralglelvant(self, hint):
        assert self._state.get("current") == BRALGLELVANT, \
            f"blorbrulk.bralglelvant: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'bralglelvant', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'bralglelvant', 0:
                self._state["current"] = STOSPROSKRANL
                self._state["trig"]    = "hint:0"
            case 'bralglelvant', _:
                self._state["current"] = DRIXFLURN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'bralglelvant', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'bralglelvant',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"bralglelvant->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drixflurn(self, hint):
        assert self._state.get("current") == DRIXFLURN, \
            f"blorbrulk.drixflurn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drixflurn', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'drixflurn', _:
                self._state["current"] = SLARBRURGRIML
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drixflurn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drixflurn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drixflurn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slarbrurgriml(self, hint):
        assert self._state.get("current") == SLARBRURGRIML, \
            f"blorbrulk.slarbrurgriml: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slarbrurgriml', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'slarbrurgriml', _:
                self._state["current"] = GROSBLENPRULT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slarbrurgriml', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slarbrurgriml',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slarbrurgriml->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grosblenprult(self, hint):
        assert self._state.get("current") == GROSBLENPRULT, \
            f"blorbrulk.grosblenprult: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grosblenprult', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'grosblenprult', _:
                self._state["current"] = SKENGLELVAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grosblenprult', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grosblenprult',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grosblenprult->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skenglelvar(self, hint):
        assert self._state.get("current") == SKENGLELVAR, \
            f"blorbrulk.skenglelvar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skenglelvar', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'skenglelvar', 0:
                self._state["current"] = CLURSKIXGRAR
                self._state["trig"]    = "hint:0"
            case 'skenglelvar', _:
                self._state["current"] = CLOSSLORVIMN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skenglelvar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skenglelvar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skenglelvar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _closslorvimn(self, hint):
        assert self._state.get("current") == CLOSSLORVIMN, \
            f"blorbrulk.closslorvimn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'closslorvimn', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'closslorvimn', _:
                self._state["current"] = CLURSKIXGRAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'closslorvimn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'closslorvimn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"closslorvimn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clurskixgrar(self, hint):
        assert self._state.get("current") == CLURSKIXGRAR, \
            f"blorbrulk.clurskixgrar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clurskixgrar', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'clurskixgrar', _:
                self._state["current"] = FLULPRIXVAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clurskixgrar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clurskixgrar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clurskixgrar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flulprixval(self, hint):
        assert self._state.get("current") == FLULPRIXVAL, \
            f"blorbrulk.flulprixval: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flulprixval', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'flulprixval', 0:
                self._state["current"] = BLIMBRULCLIM
                self._state["trig"]    = "hint:0"
            case 'flulprixval', _:
                self._state["current"] = VALGROSVUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flulprixval', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flulprixval',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flulprixval->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _valgrosvur(self, hint):
        assert self._state.get("current") == VALGROSVUR, \
            f"blorbrulk.valgrosvur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'valgrosvur', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'valgrosvur', _:
                self._state["current"] = BLIMBRULCLIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'valgrosvur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'valgrosvur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"valgrosvur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blimbrulclim(self, hint):
        assert self._state.get("current") == BLIMBRULCLIM, \
            f"blorbrulk.blimbrulclim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blimbrulclim', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'blimbrulclim', _:
                self._state["current"] = TRARPROSCLEL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blimbrulclim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blimbrulclim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blimbrulclim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trarprosclel(self, hint):
        assert self._state.get("current") == TRARPROSCLEL, \
            f"blorbrulk.trarprosclel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trarprosclel', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'trarprosclel', 0:
                self._state["current"] = KRARGLELK
                self._state["trig"]    = "hint:0"
            case 'trarprosclel', _:
                self._state["current"] = SPIXCLORSKEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trarprosclel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trarprosclel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trarprosclel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spixclorskex(self, hint):
        assert self._state.get("current") == SPIXCLORSKEX, \
            f"blorbrulk.spixclorskex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spixclorskex', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'spixclorskex', _:
                self._state["current"] = KRARGLELK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spixclorskex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spixclorskex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spixclorskex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krarglelk(self, hint):
        assert self._state.get("current") == KRARGLELK, \
            f"blorbrulk.krarglelk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krarglelk', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'krarglelk', 1:
                self._state["current"] = GLALCLELK
                self._state["trig"]    = "hint:1"
            case 'krarglelk', _:
                self._state["current"] = KRARDRARPREXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krarglelk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krarglelk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krarglelk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krardrarprexx(self, hint):
        assert self._state.get("current") == KRARDRARPREXX, \
            f"blorbrulk.krardrarprexx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krardrarprexx', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'krardrarprexx', 0:
                self._state["current"] = STOSPROSKRANL
                self._state["trig"]    = "hint:0"
            case 'krardrarprexx', _:
                self._state["current"] = GLALCLELK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krardrarprexx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krardrarprexx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krardrarprexx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glalclelk(self, hint):
        assert self._state.get("current") == GLALCLELK, \
            f"blorbrulk.glalclelk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glalclelk', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'glalclelk', 0:
                self._state["current"] = STOSPROSKRANL
                self._state["trig"]    = "hint:0"
            case 'glalclelk', _:
                self._state["current"] = KRENSLUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glalclelk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glalclelk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glalclelk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krenslul(self, hint):
        assert self._state.get("current") == KRENSLUL, \
            f"blorbrulk.krenslul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krenslul', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'krenslul', _:
                self._state["current"] = CLAXPRAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krenslul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krenslul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krenslul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _claxprar(self, hint):
        assert self._state.get("current") == CLAXPRAR, \
            f"blorbrulk.claxprar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'claxprar', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'claxprar', _:
                self._state["current"] = PRORSLEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'claxprar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'claxprar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"claxprar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prorslex(self, hint):
        assert self._state.get("current") == PRORSLEX, \
            f"blorbrulk.prorslex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prorslex', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'prorslex', 0:
                self._state["current"] = STOSPROSKRANL
                self._state["trig"]    = "hint:0"
            case 'prorslex', _:
                self._state["current"] = DRURCLENSKIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prorslex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prorslex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prorslex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drurclenskix(self, hint):
        assert self._state.get("current") == DRURCLENSKIX, \
            f"blorbrulk.drurclenskix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drurclenskix', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'drurclenskix', _:
                self._state["current"] = PRENTRON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drurclenskix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drurclenskix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drurclenskix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prentron(self, hint):
        assert self._state.get("current") == PRENTRON, \
            f"blorbrulk.prentron: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prentron', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'prentron', 1:
                self._state["current"] = STOSPROSKRANL
                self._state["trig"]    = "hint:1"
            case 'prentron', _:
                self._state["current"] = PRALGLEXSKUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prentron', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prentron',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prentron->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _pralglexskul(self, hint):
        assert self._state.get("current") == PRALGLEXSKUL, \
            f"blorbrulk.pralglexskul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'pralglexskul', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'pralglexskul', _:
                self._state["current"] = STELSTELL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'pralglexskul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'pralglexskul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"pralglexskul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stelstell(self, hint):
        assert self._state.get("current") == STELSTELL, \
            f"blorbrulk.stelstell: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stelstell', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'stelstell', _:
                self._state["current"] = CLELSPENL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stelstell', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stelstell',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stelstell->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clelspenl(self, hint):
        assert self._state.get("current") == CLELSPENL, \
            f"blorbrulk.clelspenl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clelspenl', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'clelspenl', 0:
                self._state["current"] = GRURGRURPRURK
                self._state["trig"]    = "hint:0"
            case 'clelspenl', _:
                self._state["current"] = SPONVAXVIMR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clelspenl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clelspenl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clelspenl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _sponvaxvimr(self, hint):
        assert self._state.get("current") == SPONVAXVIMR, \
            f"blorbrulk.sponvaxvimr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'sponvaxvimr', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'sponvaxvimr', _:
                self._state["current"] = GRURGRURPRURK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'sponvaxvimr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'sponvaxvimr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"sponvaxvimr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grurgrurprurk(self, hint):
        assert self._state.get("current") == GRURGRURPRURK, \
            f"blorbrulk.grurgrurprurk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grurgrurprurk', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'grurgrurprurk', 0:
                self._state["current"] = KROSSTOSBLAR
                self._state["trig"]    = "hint:0"
            case 'grurgrurprurk', _:
                self._state["current"] = DRULVEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grurgrurprurk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grurgrurprurk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grurgrurprurk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drulvex(self, hint):
        assert self._state.get("current") == DRULVEX, \
            f"blorbrulk.drulvex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drulvex', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'drulvex', 0:
                self._state["current"] = SPAXKRON
                self._state["trig"]    = "hint:0"
            case 'drulvex', _:
                self._state["current"] = KROSSTOSBLAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drulvex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drulvex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drulvex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krosstosblar(self, hint):
        assert self._state.get("current") == KROSSTOSBLAR, \
            f"blorbrulk.krosstosblar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krosstosblar', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'krosstosblar', _:
                self._state["current"] = SPAXKRON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krosstosblar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krosstosblar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krosstosblar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spaxkron(self, hint):
        assert self._state.get("current") == SPAXKRON, \
            f"blorbrulk.spaxkron: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spaxkron', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'spaxkron', 1:
                self._state["current"] = STOSPROSKRANL
                self._state["trig"]    = "hint:1"
            case 'spaxkron', _:
                self._state["current"] = SPENSTEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spaxkron', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spaxkron',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spaxkron->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spenstex(self, hint):
        assert self._state.get("current") == SPENSTEX, \
            f"blorbrulk.spenstex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spenstex', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'spenstex', 1:
                self._state["current"] = STONTRANGLENK
                self._state["trig"]    = "hint:1"
            case 'spenstex', _:
                self._state["current"] = STOSCLIMX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spenstex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spenstex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spenstex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stosclimx(self, hint):
        assert self._state.get("current") == STOSCLIMX, \
            f"blorbrulk.stosclimx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stosclimx', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'stosclimx', _:
                self._state["current"] = STONTRANGLENK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stosclimx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stosclimx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stosclimx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stontranglenk(self, hint):
        assert self._state.get("current") == STONTRANGLENK, \
            f"blorbrulk.stontranglenk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stontranglenk', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'stontranglenk', 0:
                self._state["current"] = STOSPROSKRANL
                self._state["trig"]    = "hint:0"
            case 'stontranglenk', _:
                self._state["current"] = SKONSLURK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stontranglenk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stontranglenk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stontranglenk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skonslurk(self, hint):
        assert self._state.get("current") == SKONSLURK, \
            f"blorbrulk.skonslurk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skonslurk', 2:
                self._state["current"] = PRARGRURTRULK
                self._state["trig"]    = "hint:2"
            case 'skonslurk', 0:
                self._state["current"] = STOSPROSKRANL
                self._state["trig"]    = "hint:0"
            case 'skonslurk', _:
                self._state["current"] = SLOSGLOR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skonslurk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skonslurk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skonslurk->{_to}", _xid_val)
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
            _xid_val = _xid(__name__, 'flanslal', "error", "assert_fail")
            _emit(cycle, 1, __name__, 'flanslal',
                   {"hint": hint, "span": span, "caller": caller},
                   dict(ctx), _conds,
                   "entry_blocked->error", _xid_val, assertion=_asrt)
            return 2, cycle + 1

        self._state = {"current": FLANSLAL, "ctx": ctx,
                        "span": span, "caller": caller,
                        "trig": "auto", "cycle": cycle}
        _dispatch = {
            FLANSLAL: self._flanslal,
            SPOSTREXR: self._spostrexr,
            DROSBREL: self._drosbrel,
            PRORBLORN: self._prorblorn,
            BLEXDRUL: self._blexdrul,
            KRONBLIXTROR: self._kronblixtror,
            STIMBRALBLAX: self._stimbralblax,
            DRENTRULKRARN: self._drentrulkrarn,
            GLORSKURBRAN: self._glorskurbran,
            SKELGLAXSPEXK: self._skelglaxspexk,
            STULBRAXR: self._stulbraxr,
            DRENKRONBRIXX: self._drenkronbrixx,
            VOSFLON: self._vosflon,
            TRULTRONGRULK: self._trultrongrulk,
            TRANSLELN: self._transleln,
            BLURTRAX: self._blurtrax,
            FLONBRALCLEN: self._flonbralclen,
            SLULCLIXBLARL: self._slulclixblarl,
            CLALPRORR: self._clalprorr,
            STIXSPIM: self._stixspim,
            VELGLEL: self._velglel,
            TRONSPELFLIX: self._tronspelflix,
            SKULSTONN: self._skulstonn,
            SPAXCLULGLON: self._spaxclulglon,
            PRIMGLURX: self._primglurx,
            CLIXSLONTRONX: self._clixslontronx,
            VELDRURCLULK: self._veldrurclulk,
            CLULKRORGROR: self._clulkrorgror,
            BRORFLELX: self._brorflelx,
            BLANCLOR: self._blanclor,
            STOSTRAR: self._stostrar,
            SKALKRELR: self._skalkrelr,
            STELGRAN: self._stelgran,
            BRALGLELVANT: self._bralglelvant,
            DRIXFLURN: self._drixflurn,
            SLARBRURGRIML: self._slarbrurgriml,
            GROSBLENPRULT: self._grosblenprult,
            SKENGLELVAR: self._skenglelvar,
            CLOSSLORVIMN: self._closslorvimn,
            CLURSKIXGRAR: self._clurskixgrar,
            FLULPRIXVAL: self._flulprixval,
            VALGROSVUR: self._valgrosvur,
            BLIMBRULCLIM: self._blimbrulclim,
            TRARPROSCLEL: self._trarprosclel,
            SPIXCLORSKEX: self._spixclorskex,
            KRARGLELK: self._krarglelk,
            KRARDRARPREXX: self._krardrarprexx,
            GLALCLELK: self._glalclelk,
            KRENSLUL: self._krenslul,
            CLAXPRAR: self._claxprar,
            PRORSLEX: self._prorslex,
            DRURCLENSKIX: self._drurclenskix,
            PRENTRON: self._prentron,
            PRALGLEXSKUL: self._pralglexskul,
            STELSTELL: self._stelstell,
            CLELSPENL: self._clelspenl,
            SPONVAXVIMR: self._sponvaxvimr,
            GRURGRURPRURK: self._grurgrurprurk,
            DRULVEX: self._drulvex,
            KROSSTOSBLAR: self._krosstosblar,
            SPAXKRON: self._spaxkron,
            SPENSTEX: self._spenstex,
            STOSCLIMX: self._stosclimx,
            STONTRANGLENK: self._stontranglenk,
            SKONSLURK: self._skonslurk,
        }
        while self._state["current"] not in _R and self._state["cycle"] - cycle < 8000:
            _dispatch[self._state["current"]](hint)
        _ret     = _R.get(self._state["current"], -1)
        _is_err  = self._state["current"] == PRARGRURTRULK
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
    return BlorbrulkFSM().invoke(hint=hint, span=span, caller=caller, ctx=ctx, cycle=cycle)
