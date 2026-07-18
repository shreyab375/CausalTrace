from _log import _w as _emit, _xid

SLIXFLENGLAXN = 'slixflenglaxn'
STAXGREXSLARK = 'staxgrexslark'
GLOSGRIXGRENN = 'glosgrixgrenn'
CLORVAX = 'clorvax'
STORBLENBLUL = 'storblenblul'
BREXPRALR = 'brexpralr'
BRORCLURGRORN = 'brorclurgrorn'
KREXPRANFLAN = 'krexpranflan'
SKALVURX = 'skalvurx'
DRONKRANR = 'dronkranr'
VIMPRALSLIM = 'vimpralslim'
VANFLEXTRANK = 'vanflextrank'
FLAXVEXSKON = 'flaxvexskon'
DRELFLORN = 'drelflorn'
SKENSTURTRELR = 'skensturtrelr'
SPIXCLIXSTAL = 'spixclixstal'
PROSPRURR = 'prosprurr'
TREXBRANPRAN = 'trexbranpran'
BROSTRAL = 'brostral'
SLEXSLANK = 'slexslank'
STANSLELPRAX = 'stanslelprax'
KROSGRAN = 'krosgran'
GLOSCLOST = 'glosclost'
KRIMBLIMSKOSN = 'krimblimskosn'
TRURCLORGLON = 'trurclorglon'
VELTRIXSKELN = 'veltrixskeln'
GLENVALSTUR = 'glenvalstur'
BLENFLULTROR = 'blenflultror'
DRURSPAXGLIX = 'drurspaxglix'
STORTRON = 'stortron'
CLULGRENT = 'clulgrent'
BRENGLAXDRORR = 'brenglaxdrorr'
FLEXFLULDRANN = 'flexfluldrann'
SPIMGLEN = 'spimglen'
STULTRURN = 'stultrurn'
SPEXKRALX = 'spexkralx'
STAXBRORDRORR = 'staxbrordrorr'
BRURDRENSTIX = 'brurdrenstix'
SPIMBLARDRORR = 'spimblardrorr'
SKIMTRURSKENR = 'skimtrurskenr'
STENSPONL = 'stensponl'
TRENSTON = 'trenston'
SPURBLENTRAX = 'spurblentrax'
GRELSLIMBLIM = 'grelslimblim'
PRURFLAN = 'prurflan'
CLIXBRURSTOS = 'clixbrurstos'
PRARKRALSTIXX = 'prarkralstixx'
GLULDRARSPAR = 'gluldrarspar'
FLANGLENCLURK = 'flanglenclurk'
DRURBLAL = 'drurblal'
PRIMVIM = 'primvim'
GLENGLULDRANX = 'glengluldranx'
BRENTRAR = 'brentrar'
GRANBRELT = 'granbrelt'
SKONKRENR = 'skonkrenr'
FLARGRARK = 'flargrark'
GRELSTANGLONL = 'grelstanglonl'
PRURKRONX = 'prurkronx'
GREXTRARR = 'grextrarr'
KRALPRULK = 'kralprulk'
BRIMTRULX = 'brimtrulx'
STURCLUR = 'sturclur'
GLOSFLORX = 'glosflorx'
DRAXPROSBREX = 'draxprosbrex'
SPULSPULSPELR = 'spulspulspelr'
SKALCLURN = 'skalclurn'
PRORGRELT = 'prorgrelt'
GRONKREXN = 'gronkrexn'

_R = {
    SKALCLURN: 0,
    PRORGRELT: 1,
    GRONKREXN: 2,
}

_CTX_WRITES_KEY  = 'flurslex'
_CTX_WRITE_STATE = STORBLENBLUL

class ClalclexrFSM:
    def __init__(self):
        self._state = {}

    def _slixflenglaxn(self, hint):
        assert self._state.get("current") == SLIXFLENGLAXN, \
            f"clalclexr.slixflenglaxn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slixflenglaxn', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'slixflenglaxn', 1:
                self._state["current"] = PRORGRELT
                self._state["trig"]    = "hint:1"
            case 'slixflenglaxn', _:
                self._state["current"] = STAXGREXSLARK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slixflenglaxn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slixflenglaxn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slixflenglaxn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _staxgrexslark(self, hint):
        assert self._state.get("current") == STAXGREXSLARK, \
            f"clalclexr.staxgrexslark: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'staxgrexslark', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'staxgrexslark', 0:
                self._state["current"] = CLORVAX
                self._state["trig"]    = "hint:0"
            case 'staxgrexslark', _:
                self._state["current"] = GLOSGRIXGRENN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'staxgrexslark', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'staxgrexslark',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"staxgrexslark->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glosgrixgrenn(self, hint):
        assert self._state.get("current") == GLOSGRIXGRENN, \
            f"clalclexr.glosgrixgrenn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glosgrixgrenn', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'glosgrixgrenn', 0:
                self._state["current"] = STORBLENBLUL
                self._state["trig"]    = "hint:0"
            case 'glosgrixgrenn', _:
                self._state["current"] = CLORVAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glosgrixgrenn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glosgrixgrenn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glosgrixgrenn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clorvax(self, hint):
        assert self._state.get("current") == CLORVAX, \
            f"clalclexr.clorvax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clorvax', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'clorvax', 1:
                self._state["current"] = BREXPRALR
                self._state["trig"]    = "hint:1"
            case 'clorvax', _:
                self._state["current"] = STORBLENBLUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clorvax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clorvax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clorvax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _storblenblul(self, hint):
        assert self._state.get("current") == STORBLENBLUL, \
            f"clalclexr.storblenblul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        _ctx_val_before = self._state["ctx"].get(_CTX_WRITES_KEY, 0)
        match self._state["current"], hint:
            case 'storblenblul', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'storblenblul', _:
                self._state["current"] = BREXPRALR
                self._state["trig"]    = "auto"
        _old = self._state["ctx"].get(_CTX_WRITES_KEY, 0)
        _inc = 2 if hint == 2 else 1
        self._state["ctx"][_CTX_WRITES_KEY] = _old + _inc
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'storblenblul', _to, _trig)
        _conds = {"hint_branch": _hint_branch,
                   "ctx_write": True,
                   "ctx_val_before": _ctx_val_before}
        _emit(self._state["cycle"], 1, __name__, 'storblenblul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"storblenblul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brexpralr(self, hint):
        assert self._state.get("current") == BREXPRALR, \
            f"clalclexr.brexpralr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brexpralr', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'brexpralr', _:
                self._state["current"] = BRORCLURGRORN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brexpralr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brexpralr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brexpralr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brorclurgrorn(self, hint):
        assert self._state.get("current") == BRORCLURGRORN, \
            f"clalclexr.brorclurgrorn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brorclurgrorn', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'brorclurgrorn', 0:
                self._state["current"] = PRORGRELT
                self._state["trig"]    = "hint:0"
            case 'brorclurgrorn', _:
                self._state["current"] = KREXPRANFLAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brorclurgrorn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brorclurgrorn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brorclurgrorn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krexpranflan(self, hint):
        assert self._state.get("current") == KREXPRANFLAN, \
            f"clalclexr.krexpranflan: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krexpranflan', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'krexpranflan', _:
                self._state["current"] = SKALVURX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krexpranflan', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krexpranflan',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krexpranflan->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skalvurx(self, hint):
        assert self._state.get("current") == SKALVURX, \
            f"clalclexr.skalvurx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skalvurx', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'skalvurx', _:
                self._state["current"] = DRONKRANR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skalvurx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skalvurx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skalvurx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _dronkranr(self, hint):
        assert self._state.get("current") == DRONKRANR, \
            f"clalclexr.dronkranr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'dronkranr', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'dronkranr', 1:
                self._state["current"] = PRORGRELT
                self._state["trig"]    = "hint:1"
            case 'dronkranr', _:
                self._state["current"] = VIMPRALSLIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'dronkranr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'dronkranr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"dronkranr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vimpralslim(self, hint):
        assert self._state.get("current") == VIMPRALSLIM, \
            f"clalclexr.vimpralslim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vimpralslim', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'vimpralslim', _:
                self._state["current"] = VANFLEXTRANK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vimpralslim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vimpralslim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vimpralslim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vanflextrank(self, hint):
        assert self._state.get("current") == VANFLEXTRANK, \
            f"clalclexr.vanflextrank: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vanflextrank', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'vanflextrank', 0:
                self._state["current"] = DRELFLORN
                self._state["trig"]    = "hint:0"
            case 'vanflextrank', _:
                self._state["current"] = FLAXVEXSKON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vanflextrank', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vanflextrank',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vanflextrank->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flaxvexskon(self, hint):
        assert self._state.get("current") == FLAXVEXSKON, \
            f"clalclexr.flaxvexskon: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flaxvexskon', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'flaxvexskon', _:
                self._state["current"] = DRELFLORN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flaxvexskon', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flaxvexskon',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flaxvexskon->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drelflorn(self, hint):
        assert self._state.get("current") == DRELFLORN, \
            f"clalclexr.drelflorn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drelflorn', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'drelflorn', _:
                self._state["current"] = SKENSTURTRELR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drelflorn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drelflorn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drelflorn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skensturtrelr(self, hint):
        assert self._state.get("current") == SKENSTURTRELR, \
            f"clalclexr.skensturtrelr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skensturtrelr', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'skensturtrelr', 0:
                self._state["current"] = PRORGRELT
                self._state["trig"]    = "hint:0"
            case 'skensturtrelr', _:
                self._state["current"] = SPIXCLIXSTAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skensturtrelr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skensturtrelr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skensturtrelr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spixclixstal(self, hint):
        assert self._state.get("current") == SPIXCLIXSTAL, \
            f"clalclexr.spixclixstal: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spixclixstal', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'spixclixstal', 1:
                self._state["current"] = TREXBRANPRAN
                self._state["trig"]    = "hint:1"
            case 'spixclixstal', _:
                self._state["current"] = PROSPRURR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spixclixstal', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spixclixstal',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spixclixstal->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prosprurr(self, hint):
        assert self._state.get("current") == PROSPRURR, \
            f"clalclexr.prosprurr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prosprurr', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'prosprurr', _:
                self._state["current"] = TREXBRANPRAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prosprurr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prosprurr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prosprurr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trexbranpran(self, hint):
        assert self._state.get("current") == TREXBRANPRAN, \
            f"clalclexr.trexbranpran: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trexbranpran', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'trexbranpran', _:
                self._state["current"] = BROSTRAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trexbranpran', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trexbranpran',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trexbranpran->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brostral(self, hint):
        assert self._state.get("current") == BROSTRAL, \
            f"clalclexr.brostral: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brostral', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'brostral', _:
                self._state["current"] = SLEXSLANK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brostral', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brostral',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brostral->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slexslank(self, hint):
        assert self._state.get("current") == SLEXSLANK, \
            f"clalclexr.slexslank: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slexslank', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'slexslank', 0:
                self._state["current"] = KROSGRAN
                self._state["trig"]    = "hint:0"
            case 'slexslank', _:
                self._state["current"] = STANSLELPRAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slexslank', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slexslank',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slexslank->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stanslelprax(self, hint):
        assert self._state.get("current") == STANSLELPRAX, \
            f"clalclexr.stanslelprax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stanslelprax', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'stanslelprax', 1:
                self._state["current"] = GLOSCLOST
                self._state["trig"]    = "hint:1"
            case 'stanslelprax', _:
                self._state["current"] = KROSGRAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stanslelprax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stanslelprax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stanslelprax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krosgran(self, hint):
        assert self._state.get("current") == KROSGRAN, \
            f"clalclexr.krosgran: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krosgran', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'krosgran', _:
                self._state["current"] = GLOSCLOST
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krosgran', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krosgran',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krosgran->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glosclost(self, hint):
        assert self._state.get("current") == GLOSCLOST, \
            f"clalclexr.glosclost: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glosclost', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'glosclost', 0:
                self._state["current"] = PRORGRELT
                self._state["trig"]    = "hint:0"
            case 'glosclost', _:
                self._state["current"] = KRIMBLIMSKOSN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glosclost', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glosclost',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glosclost->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krimblimskosn(self, hint):
        assert self._state.get("current") == KRIMBLIMSKOSN, \
            f"clalclexr.krimblimskosn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krimblimskosn', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'krimblimskosn', 0:
                self._state["current"] = PRORGRELT
                self._state["trig"]    = "hint:0"
            case 'krimblimskosn', _:
                self._state["current"] = TRURCLORGLON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krimblimskosn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krimblimskosn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krimblimskosn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trurclorglon(self, hint):
        assert self._state.get("current") == TRURCLORGLON, \
            f"clalclexr.trurclorglon: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trurclorglon', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'trurclorglon', _:
                self._state["current"] = VELTRIXSKELN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trurclorglon', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trurclorglon',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trurclorglon->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _veltrixskeln(self, hint):
        assert self._state.get("current") == VELTRIXSKELN, \
            f"clalclexr.veltrixskeln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'veltrixskeln', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'veltrixskeln', 1:
                self._state["current"] = PRORGRELT
                self._state["trig"]    = "hint:1"
            case 'veltrixskeln', _:
                self._state["current"] = GLENVALSTUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'veltrixskeln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'veltrixskeln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"veltrixskeln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glenvalstur(self, hint):
        assert self._state.get("current") == GLENVALSTUR, \
            f"clalclexr.glenvalstur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glenvalstur', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'glenvalstur', _:
                self._state["current"] = BLENFLULTROR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glenvalstur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glenvalstur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glenvalstur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blenflultror(self, hint):
        assert self._state.get("current") == BLENFLULTROR, \
            f"clalclexr.blenflultror: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blenflultror', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'blenflultror', 0:
                self._state["current"] = STORTRON
                self._state["trig"]    = "hint:0"
            case 'blenflultror', _:
                self._state["current"] = DRURSPAXGLIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blenflultror', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blenflultror',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blenflultror->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drurspaxglix(self, hint):
        assert self._state.get("current") == DRURSPAXGLIX, \
            f"clalclexr.drurspaxglix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drurspaxglix', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'drurspaxglix', 1:
                self._state["current"] = PRORGRELT
                self._state["trig"]    = "hint:1"
            case 'drurspaxglix', _:
                self._state["current"] = STORTRON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drurspaxglix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drurspaxglix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drurspaxglix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stortron(self, hint):
        assert self._state.get("current") == STORTRON, \
            f"clalclexr.stortron: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stortron', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'stortron', 0:
                self._state["current"] = BRENGLAXDRORR
                self._state["trig"]    = "hint:0"
            case 'stortron', _:
                self._state["current"] = CLULGRENT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stortron', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stortron',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stortron->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clulgrent(self, hint):
        assert self._state.get("current") == CLULGRENT, \
            f"clalclexr.clulgrent: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clulgrent', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'clulgrent', _:
                self._state["current"] = BRENGLAXDRORR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clulgrent', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clulgrent',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clulgrent->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brenglaxdrorr(self, hint):
        assert self._state.get("current") == BRENGLAXDRORR, \
            f"clalclexr.brenglaxdrorr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brenglaxdrorr', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'brenglaxdrorr', _:
                self._state["current"] = FLEXFLULDRANN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brenglaxdrorr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brenglaxdrorr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brenglaxdrorr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flexfluldrann(self, hint):
        assert self._state.get("current") == FLEXFLULDRANN, \
            f"clalclexr.flexfluldrann: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flexfluldrann', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'flexfluldrann', _:
                self._state["current"] = SPIMGLEN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flexfluldrann', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flexfluldrann',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flexfluldrann->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spimglen(self, hint):
        assert self._state.get("current") == SPIMGLEN, \
            f"clalclexr.spimglen: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spimglen', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'spimglen', _:
                self._state["current"] = STULTRURN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spimglen', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spimglen',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spimglen->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stultrurn(self, hint):
        assert self._state.get("current") == STULTRURN, \
            f"clalclexr.stultrurn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stultrurn', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'stultrurn', _:
                self._state["current"] = SPEXKRALX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stultrurn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stultrurn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stultrurn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spexkralx(self, hint):
        assert self._state.get("current") == SPEXKRALX, \
            f"clalclexr.spexkralx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spexkralx', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'spexkralx', 1:
                self._state["current"] = PRORGRELT
                self._state["trig"]    = "hint:1"
            case 'spexkralx', _:
                self._state["current"] = STAXBRORDRORR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spexkralx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spexkralx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spexkralx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _staxbrordrorr(self, hint):
        assert self._state.get("current") == STAXBRORDRORR, \
            f"clalclexr.staxbrordrorr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'staxbrordrorr', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'staxbrordrorr', _:
                self._state["current"] = BRURDRENSTIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'staxbrordrorr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'staxbrordrorr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"staxbrordrorr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brurdrenstix(self, hint):
        assert self._state.get("current") == BRURDRENSTIX, \
            f"clalclexr.brurdrenstix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brurdrenstix', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'brurdrenstix', _:
                self._state["current"] = SPIMBLARDRORR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brurdrenstix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brurdrenstix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brurdrenstix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spimblardrorr(self, hint):
        assert self._state.get("current") == SPIMBLARDRORR, \
            f"clalclexr.spimblardrorr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spimblardrorr', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'spimblardrorr', _:
                self._state["current"] = SKIMTRURSKENR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spimblardrorr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spimblardrorr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spimblardrorr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skimtrurskenr(self, hint):
        assert self._state.get("current") == SKIMTRURSKENR, \
            f"clalclexr.skimtrurskenr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skimtrurskenr', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'skimtrurskenr', _:
                self._state["current"] = STENSPONL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skimtrurskenr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skimtrurskenr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skimtrurskenr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stensponl(self, hint):
        assert self._state.get("current") == STENSPONL, \
            f"clalclexr.stensponl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stensponl', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'stensponl', _:
                self._state["current"] = TRENSTON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stensponl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stensponl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stensponl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trenston(self, hint):
        assert self._state.get("current") == TRENSTON, \
            f"clalclexr.trenston: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trenston', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'trenston', 1:
                self._state["current"] = GRELSLIMBLIM
                self._state["trig"]    = "hint:1"
            case 'trenston', _:
                self._state["current"] = SPURBLENTRAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trenston', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trenston',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trenston->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spurblentrax(self, hint):
        assert self._state.get("current") == SPURBLENTRAX, \
            f"clalclexr.spurblentrax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spurblentrax', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'spurblentrax', _:
                self._state["current"] = GRELSLIMBLIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spurblentrax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spurblentrax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spurblentrax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grelslimblim(self, hint):
        assert self._state.get("current") == GRELSLIMBLIM, \
            f"clalclexr.grelslimblim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grelslimblim', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'grelslimblim', _:
                self._state["current"] = PRURFLAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grelslimblim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grelslimblim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grelslimblim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prurflan(self, hint):
        assert self._state.get("current") == PRURFLAN, \
            f"clalclexr.prurflan: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prurflan', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'prurflan', 0:
                self._state["current"] = PRARKRALSTIXX
                self._state["trig"]    = "hint:0"
            case 'prurflan', _:
                self._state["current"] = CLIXBRURSTOS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prurflan', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prurflan',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prurflan->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clixbrurstos(self, hint):
        assert self._state.get("current") == CLIXBRURSTOS, \
            f"clalclexr.clixbrurstos: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clixbrurstos', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'clixbrurstos', 1:
                self._state["current"] = GLULDRARSPAR
                self._state["trig"]    = "hint:1"
            case 'clixbrurstos', _:
                self._state["current"] = PRARKRALSTIXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clixbrurstos', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clixbrurstos',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clixbrurstos->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prarkralstixx(self, hint):
        assert self._state.get("current") == PRARKRALSTIXX, \
            f"clalclexr.prarkralstixx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prarkralstixx', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'prarkralstixx', _:
                self._state["current"] = GLULDRARSPAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prarkralstixx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prarkralstixx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prarkralstixx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _gluldrarspar(self, hint):
        assert self._state.get("current") == GLULDRARSPAR, \
            f"clalclexr.gluldrarspar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'gluldrarspar', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'gluldrarspar', _:
                self._state["current"] = FLANGLENCLURK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'gluldrarspar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'gluldrarspar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"gluldrarspar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flanglenclurk(self, hint):
        assert self._state.get("current") == FLANGLENCLURK, \
            f"clalclexr.flanglenclurk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flanglenclurk', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'flanglenclurk', 1:
                self._state["current"] = PRORGRELT
                self._state["trig"]    = "hint:1"
            case 'flanglenclurk', _:
                self._state["current"] = DRURBLAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flanglenclurk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flanglenclurk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flanglenclurk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drurblal(self, hint):
        assert self._state.get("current") == DRURBLAL, \
            f"clalclexr.drurblal: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drurblal', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'drurblal', 0:
                self._state["current"] = GLENGLULDRANX
                self._state["trig"]    = "hint:0"
            case 'drurblal', _:
                self._state["current"] = PRIMVIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drurblal', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drurblal',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drurblal->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _primvim(self, hint):
        assert self._state.get("current") == PRIMVIM, \
            f"clalclexr.primvim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'primvim', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'primvim', 1:
                self._state["current"] = PRORGRELT
                self._state["trig"]    = "hint:1"
            case 'primvim', _:
                self._state["current"] = GLENGLULDRANX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'primvim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'primvim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"primvim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glengluldranx(self, hint):
        assert self._state.get("current") == GLENGLULDRANX, \
            f"clalclexr.glengluldranx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glengluldranx', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'glengluldranx', 1:
                self._state["current"] = PRORGRELT
                self._state["trig"]    = "hint:1"
            case 'glengluldranx', _:
                self._state["current"] = BRENTRAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glengluldranx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glengluldranx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glengluldranx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brentrar(self, hint):
        assert self._state.get("current") == BRENTRAR, \
            f"clalclexr.brentrar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brentrar', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'brentrar', _:
                self._state["current"] = GRANBRELT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brentrar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brentrar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brentrar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _granbrelt(self, hint):
        assert self._state.get("current") == GRANBRELT, \
            f"clalclexr.granbrelt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'granbrelt', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'granbrelt', _:
                self._state["current"] = SKONKRENR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'granbrelt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'granbrelt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"granbrelt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skonkrenr(self, hint):
        assert self._state.get("current") == SKONKRENR, \
            f"clalclexr.skonkrenr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skonkrenr', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'skonkrenr', _:
                self._state["current"] = FLARGRARK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skonkrenr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skonkrenr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skonkrenr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flargrark(self, hint):
        assert self._state.get("current") == FLARGRARK, \
            f"clalclexr.flargrark: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flargrark', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'flargrark', 1:
                self._state["current"] = PRORGRELT
                self._state["trig"]    = "hint:1"
            case 'flargrark', _:
                self._state["current"] = GRELSTANGLONL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flargrark', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flargrark',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flargrark->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grelstanglonl(self, hint):
        assert self._state.get("current") == GRELSTANGLONL, \
            f"clalclexr.grelstanglonl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grelstanglonl', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'grelstanglonl', _:
                self._state["current"] = PRURKRONX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grelstanglonl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grelstanglonl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grelstanglonl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prurkronx(self, hint):
        assert self._state.get("current") == PRURKRONX, \
            f"clalclexr.prurkronx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prurkronx', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'prurkronx', _:
                self._state["current"] = GREXTRARR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prurkronx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prurkronx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prurkronx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grextrarr(self, hint):
        assert self._state.get("current") == GREXTRARR, \
            f"clalclexr.grextrarr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grextrarr', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'grextrarr', 1:
                self._state["current"] = BRIMTRULX
                self._state["trig"]    = "hint:1"
            case 'grextrarr', _:
                self._state["current"] = KRALPRULK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grextrarr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grextrarr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grextrarr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _kralprulk(self, hint):
        assert self._state.get("current") == KRALPRULK, \
            f"clalclexr.kralprulk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'kralprulk', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'kralprulk', 1:
                self._state["current"] = PRORGRELT
                self._state["trig"]    = "hint:1"
            case 'kralprulk', _:
                self._state["current"] = BRIMTRULX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'kralprulk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'kralprulk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"kralprulk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brimtrulx(self, hint):
        assert self._state.get("current") == BRIMTRULX, \
            f"clalclexr.brimtrulx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brimtrulx', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'brimtrulx', 0:
                self._state["current"] = PRORGRELT
                self._state["trig"]    = "hint:0"
            case 'brimtrulx', _:
                self._state["current"] = STURCLUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brimtrulx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brimtrulx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brimtrulx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _sturclur(self, hint):
        assert self._state.get("current") == STURCLUR, \
            f"clalclexr.sturclur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'sturclur', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'sturclur', _:
                self._state["current"] = GLOSFLORX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'sturclur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'sturclur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"sturclur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glosflorx(self, hint):
        assert self._state.get("current") == GLOSFLORX, \
            f"clalclexr.glosflorx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glosflorx', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'glosflorx', _:
                self._state["current"] = DRAXPROSBREX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glosflorx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glosflorx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glosflorx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _draxprosbrex(self, hint):
        assert self._state.get("current") == DRAXPROSBREX, \
            f"clalclexr.draxprosbrex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'draxprosbrex', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'draxprosbrex', _:
                self._state["current"] = SPULSPULSPELR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'draxprosbrex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'draxprosbrex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"draxprosbrex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spulspulspelr(self, hint):
        assert self._state.get("current") == SPULSPULSPELR, \
            f"clalclexr.spulspulspelr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spulspulspelr', 2:
                self._state["current"] = GRONKREXN
                self._state["trig"]    = "hint:2"
            case 'spulspulspelr', 1:
                self._state["current"] = PRORGRELT
                self._state["trig"]    = "hint:1"
            case 'spulspulspelr', _:
                self._state["current"] = SKALCLURN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spulspulspelr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spulspulspelr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spulspulspelr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def invoke(self, hint=None, span=None, caller=None, ctx=None, cycle=0):
        if ctx is None: ctx = {}

        self._state = {"current": SLIXFLENGLAXN, "ctx": ctx,
                        "span": span, "caller": caller,
                        "trig": "auto", "cycle": cycle}
        _dispatch = {
            SLIXFLENGLAXN: self._slixflenglaxn,
            STAXGREXSLARK: self._staxgrexslark,
            GLOSGRIXGRENN: self._glosgrixgrenn,
            CLORVAX: self._clorvax,
            STORBLENBLUL: self._storblenblul,
            BREXPRALR: self._brexpralr,
            BRORCLURGRORN: self._brorclurgrorn,
            KREXPRANFLAN: self._krexpranflan,
            SKALVURX: self._skalvurx,
            DRONKRANR: self._dronkranr,
            VIMPRALSLIM: self._vimpralslim,
            VANFLEXTRANK: self._vanflextrank,
            FLAXVEXSKON: self._flaxvexskon,
            DRELFLORN: self._drelflorn,
            SKENSTURTRELR: self._skensturtrelr,
            SPIXCLIXSTAL: self._spixclixstal,
            PROSPRURR: self._prosprurr,
            TREXBRANPRAN: self._trexbranpran,
            BROSTRAL: self._brostral,
            SLEXSLANK: self._slexslank,
            STANSLELPRAX: self._stanslelprax,
            KROSGRAN: self._krosgran,
            GLOSCLOST: self._glosclost,
            KRIMBLIMSKOSN: self._krimblimskosn,
            TRURCLORGLON: self._trurclorglon,
            VELTRIXSKELN: self._veltrixskeln,
            GLENVALSTUR: self._glenvalstur,
            BLENFLULTROR: self._blenflultror,
            DRURSPAXGLIX: self._drurspaxglix,
            STORTRON: self._stortron,
            CLULGRENT: self._clulgrent,
            BRENGLAXDRORR: self._brenglaxdrorr,
            FLEXFLULDRANN: self._flexfluldrann,
            SPIMGLEN: self._spimglen,
            STULTRURN: self._stultrurn,
            SPEXKRALX: self._spexkralx,
            STAXBRORDRORR: self._staxbrordrorr,
            BRURDRENSTIX: self._brurdrenstix,
            SPIMBLARDRORR: self._spimblardrorr,
            SKIMTRURSKENR: self._skimtrurskenr,
            STENSPONL: self._stensponl,
            TRENSTON: self._trenston,
            SPURBLENTRAX: self._spurblentrax,
            GRELSLIMBLIM: self._grelslimblim,
            PRURFLAN: self._prurflan,
            CLIXBRURSTOS: self._clixbrurstos,
            PRARKRALSTIXX: self._prarkralstixx,
            GLULDRARSPAR: self._gluldrarspar,
            FLANGLENCLURK: self._flanglenclurk,
            DRURBLAL: self._drurblal,
            PRIMVIM: self._primvim,
            GLENGLULDRANX: self._glengluldranx,
            BRENTRAR: self._brentrar,
            GRANBRELT: self._granbrelt,
            SKONKRENR: self._skonkrenr,
            FLARGRARK: self._flargrark,
            GRELSTANGLONL: self._grelstanglonl,
            PRURKRONX: self._prurkronx,
            GREXTRARR: self._grextrarr,
            KRALPRULK: self._kralprulk,
            BRIMTRULX: self._brimtrulx,
            STURCLUR: self._sturclur,
            GLOSFLORX: self._glosflorx,
            DRAXPROSBREX: self._draxprosbrex,
            SPULSPULSPELR: self._spulspulspelr,
        }
        while self._state["current"] not in _R and self._state["cycle"] - cycle < 8000:
            _dispatch[self._state["current"]](hint)
        _ret     = _R.get(self._state["current"], -1)
        _is_err  = self._state["current"] == GRONKREXN
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
    return ClalclexrFSM().invoke(hint=hint, span=span, caller=caller, ctx=ctx, cycle=cycle)
