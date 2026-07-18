from _log import _w as _emit, _xid

SPIXGRELR = 'spixgrelr'
FLELBLIXL = 'flelblixl'
DRALTRAXKRANL = 'draltraxkranl'
TRALGRARSTIML = 'tralgrarstiml'
STORSLIMN = 'storslimn'
GLENFLON = 'glenflon'
BLULSKIMVAL = 'blulskimval'
GLALDRELSLIX = 'glaldrelslix'
FLONDROSSLEX = 'flondrosslex'
PREXFLARGRAXN = 'prexflargraxn'
SLIXGRIXGLUR = 'slixgrixglur'
BRENCLEL = 'brenclel'
CLULGRELGREXL = 'clulgrelgrexl'
SPIXBRURTRIX = 'spixbrurtrix'
SLEXBLUR = 'slexblur'
SPAXGLAXT = 'spaxglaxt'
TRULFLOR = 'trulflor'
SLORSLART = 'slorslart'
STURFLONSLAR = 'sturflonslar'
SKANSKULX = 'skanskulx'
KREXSKEX = 'krexskex'
GRORTRONFLIX = 'grortronflix'
GROSSLEN = 'grosslen'
CLANDRON = 'clandron'
SLULPRARCLOSR = 'slulprarclosr'
CLORCLUR = 'clorclur'
KRANSPIMK = 'kranspimk'
TRENBRORFLON = 'trenbrorflon'
BLAXBRENN = 'blaxbrenn'
STENTRENGLOR = 'stentrenglor'
SKONSLONN = 'skonslonn'
SPIMGRELGRAXL = 'spimgrelgraxl'
BRARBLORSTAX = 'brarblorstax'
SLIXPRAXX = 'slixpraxx'
VIMSLAN = 'vimslan'
VARSKOSX = 'varskosx'
SPULCLARFLOR = 'spulclarflor'
SLELCLONSLOSR = 'slelclonslosr'
STELSKORSTON = 'stelskorston'
GLELCLURBLONX = 'glelclurblonx'
STARPRONFLAL = 'starpronflal'
SLANTRELSLON = 'slantrelslon'
BLOSFLALSKALK = 'blosflalskalk'
BLORSPUL = 'blorspul'
PRIXSTARX = 'prixstarx'
STORBLALSLEL = 'storblalslel'
VULDRAR = 'vuldrar'
CLORVUL = 'clorvul'
PRIMBLALGRARX = 'primblalgrarx'
SKIXSLAXPRARK = 'skixslaxprark'
SPENFLARSTELL = 'spenflarstell'
BRENBLALTRELL = 'brenblaltrell'
GRONTRONR = 'grontronr'
SPULPRIXVAXX = 'spulprixvaxx'
VEXGLENSTALR = 'vexglenstalr'
TRULSTANSTAR = 'trulstanstar'
PROSVAXBRULX = 'prosvaxbrulx'
GLALDRIM = 'glaldrim'
SPEXVONR = 'spexvonr'
GLONGREN = 'glongren'
PRANFLIXX = 'pranflixx'
SKEXTROS = 'skextros'
GLORSLENGRULK = 'glorslengrulk'
VANSKAN = 'vanskan'
FLULGLARL = 'flulglarl'
VIXPRURCLIXK = 'vixprurclixk'
SKURTRALK = 'skurtralk'
SKELDRELFLON = 'skeldrelflon'

_R = {
    VIXPRURCLIXK: 0,
    SKURTRALK: 1,
    SKELDRELFLON: 2,
}

_CTX_READS_KEY = 'flurslex'
_CTX_THRESHOLD = 16

class BrorstornFSM:
    def __init__(self):
        self._state = {}

    def _spixgrelr(self, hint):
        assert self._state.get("current") == SPIXGRELR, \
            f"brorstorn.spixgrelr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spixgrelr', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'spixgrelr', _:
                self._state["current"] = FLELBLIXL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spixgrelr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spixgrelr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spixgrelr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flelblixl(self, hint):
        assert self._state.get("current") == FLELBLIXL, \
            f"brorstorn.flelblixl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flelblixl', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'flelblixl', 0:
                self._state["current"] = TRALGRARSTIML
                self._state["trig"]    = "hint:0"
            case 'flelblixl', _:
                self._state["current"] = DRALTRAXKRANL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flelblixl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flelblixl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flelblixl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _draltraxkranl(self, hint):
        assert self._state.get("current") == DRALTRAXKRANL, \
            f"brorstorn.draltraxkranl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'draltraxkranl', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'draltraxkranl', _:
                self._state["current"] = TRALGRARSTIML
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'draltraxkranl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'draltraxkranl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"draltraxkranl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _tralgrarstiml(self, hint):
        assert self._state.get("current") == TRALGRARSTIML, \
            f"brorstorn.tralgrarstiml: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'tralgrarstiml', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'tralgrarstiml', _:
                self._state["current"] = STORSLIMN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'tralgrarstiml', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'tralgrarstiml',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"tralgrarstiml->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _storslimn(self, hint):
        assert self._state.get("current") == STORSLIMN, \
            f"brorstorn.storslimn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'storslimn', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'storslimn', 1:
                self._state["current"] = SKURTRALK
                self._state["trig"]    = "hint:1"
            case 'storslimn', _:
                self._state["current"] = GLENFLON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'storslimn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'storslimn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"storslimn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glenflon(self, hint):
        assert self._state.get("current") == GLENFLON, \
            f"brorstorn.glenflon: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glenflon', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'glenflon', 0:
                self._state["current"] = SKURTRALK
                self._state["trig"]    = "hint:0"
            case 'glenflon', _:
                self._state["current"] = BLULSKIMVAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glenflon', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glenflon',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glenflon->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blulskimval(self, hint):
        assert self._state.get("current") == BLULSKIMVAL, \
            f"brorstorn.blulskimval: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blulskimval', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'blulskimval', 0:
                self._state["current"] = FLONDROSSLEX
                self._state["trig"]    = "hint:0"
            case 'blulskimval', _:
                self._state["current"] = GLALDRELSLIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blulskimval', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blulskimval',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blulskimval->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glaldrelslix(self, hint):
        assert self._state.get("current") == GLALDRELSLIX, \
            f"brorstorn.glaldrelslix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glaldrelslix', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'glaldrelslix', 1:
                self._state["current"] = SKURTRALK
                self._state["trig"]    = "hint:1"
            case 'glaldrelslix', _:
                self._state["current"] = FLONDROSSLEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glaldrelslix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glaldrelslix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glaldrelslix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flondrosslex(self, hint):
        assert self._state.get("current") == FLONDROSSLEX, \
            f"brorstorn.flondrosslex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flondrosslex', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'flondrosslex', 0:
                self._state["current"] = SLIXGRIXGLUR
                self._state["trig"]    = "hint:0"
            case 'flondrosslex', _:
                self._state["current"] = PREXFLARGRAXN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flondrosslex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flondrosslex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flondrosslex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prexflargraxn(self, hint):
        assert self._state.get("current") == PREXFLARGRAXN, \
            f"brorstorn.prexflargraxn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prexflargraxn', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'prexflargraxn', _:
                self._state["current"] = SLIXGRIXGLUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prexflargraxn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prexflargraxn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prexflargraxn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slixgrixglur(self, hint):
        assert self._state.get("current") == SLIXGRIXGLUR, \
            f"brorstorn.slixgrixglur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slixgrixglur', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'slixgrixglur', _:
                self._state["current"] = BRENCLEL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slixgrixglur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slixgrixglur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slixgrixglur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brenclel(self, hint):
        assert self._state.get("current") == BRENCLEL, \
            f"brorstorn.brenclel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brenclel', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'brenclel', 0:
                self._state["current"] = SKURTRALK
                self._state["trig"]    = "hint:0"
            case 'brenclel', _:
                self._state["current"] = CLULGRELGREXL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brenclel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brenclel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brenclel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clulgrelgrexl(self, hint):
        assert self._state.get("current") == CLULGRELGREXL, \
            f"brorstorn.clulgrelgrexl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clulgrelgrexl', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'clulgrelgrexl', 1:
                self._state["current"] = SKURTRALK
                self._state["trig"]    = "hint:1"
            case 'clulgrelgrexl', _:
                self._state["current"] = SPIXBRURTRIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clulgrelgrexl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clulgrelgrexl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clulgrelgrexl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spixbrurtrix(self, hint):
        assert self._state.get("current") == SPIXBRURTRIX, \
            f"brorstorn.spixbrurtrix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spixbrurtrix', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'spixbrurtrix', _:
                self._state["current"] = SLEXBLUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spixbrurtrix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spixbrurtrix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spixbrurtrix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slexblur(self, hint):
        assert self._state.get("current") == SLEXBLUR, \
            f"brorstorn.slexblur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slexblur', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'slexblur', _:
                self._state["current"] = SPAXGLAXT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slexblur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slexblur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slexblur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spaxglaxt(self, hint):
        assert self._state.get("current") == SPAXGLAXT, \
            f"brorstorn.spaxglaxt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spaxglaxt', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'spaxglaxt', _:
                self._state["current"] = TRULFLOR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spaxglaxt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spaxglaxt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spaxglaxt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trulflor(self, hint):
        assert self._state.get("current") == TRULFLOR, \
            f"brorstorn.trulflor: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trulflor', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'trulflor', 0:
                self._state["current"] = SKURTRALK
                self._state["trig"]    = "hint:0"
            case 'trulflor', _:
                self._state["current"] = SLORSLART
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trulflor', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trulflor',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trulflor->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slorslart(self, hint):
        assert self._state.get("current") == SLORSLART, \
            f"brorstorn.slorslart: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slorslart', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'slorslart', _:
                self._state["current"] = STURFLONSLAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slorslart', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slorslart',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slorslart->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _sturflonslar(self, hint):
        assert self._state.get("current") == STURFLONSLAR, \
            f"brorstorn.sturflonslar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'sturflonslar', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'sturflonslar', 1:
                self._state["current"] = KREXSKEX
                self._state["trig"]    = "hint:1"
            case 'sturflonslar', _:
                self._state["current"] = SKANSKULX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'sturflonslar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'sturflonslar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"sturflonslar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skanskulx(self, hint):
        assert self._state.get("current") == SKANSKULX, \
            f"brorstorn.skanskulx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skanskulx', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'skanskulx', _:
                self._state["current"] = KREXSKEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skanskulx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skanskulx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skanskulx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krexskex(self, hint):
        assert self._state.get("current") == KREXSKEX, \
            f"brorstorn.krexskex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krexskex', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'krexskex', 0:
                self._state["current"] = GROSSLEN
                self._state["trig"]    = "hint:0"
            case 'krexskex', _:
                self._state["current"] = GRORTRONFLIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krexskex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krexskex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krexskex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grortronflix(self, hint):
        assert self._state.get("current") == GRORTRONFLIX, \
            f"brorstorn.grortronflix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grortronflix', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'grortronflix', _:
                self._state["current"] = GROSSLEN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grortronflix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grortronflix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grortronflix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grosslen(self, hint):
        assert self._state.get("current") == GROSSLEN, \
            f"brorstorn.grosslen: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grosslen', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'grosslen', 1:
                self._state["current"] = SLULPRARCLOSR
                self._state["trig"]    = "hint:1"
            case 'grosslen', _:
                self._state["current"] = CLANDRON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grosslen', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grosslen',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grosslen->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clandron(self, hint):
        assert self._state.get("current") == CLANDRON, \
            f"brorstorn.clandron: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clandron', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'clandron', 1:
                self._state["current"] = SKURTRALK
                self._state["trig"]    = "hint:1"
            case 'clandron', _:
                self._state["current"] = SLULPRARCLOSR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clandron', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clandron',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clandron->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slulprarclosr(self, hint):
        assert self._state.get("current") == SLULPRARCLOSR, \
            f"brorstorn.slulprarclosr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slulprarclosr', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'slulprarclosr', _:
                self._state["current"] = CLORCLUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slulprarclosr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slulprarclosr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slulprarclosr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clorclur(self, hint):
        assert self._state.get("current") == CLORCLUR, \
            f"brorstorn.clorclur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clorclur', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'clorclur', _:
                self._state["current"] = KRANSPIMK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clorclur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clorclur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clorclur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _kranspimk(self, hint):
        assert self._state.get("current") == KRANSPIMK, \
            f"brorstorn.kranspimk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'kranspimk', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'kranspimk', _:
                self._state["current"] = TRENBRORFLON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'kranspimk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'kranspimk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"kranspimk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trenbrorflon(self, hint):
        assert self._state.get("current") == TRENBRORFLON, \
            f"brorstorn.trenbrorflon: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trenbrorflon', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'trenbrorflon', 1:
                self._state["current"] = SKURTRALK
                self._state["trig"]    = "hint:1"
            case 'trenbrorflon', _:
                self._state["current"] = BLAXBRENN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trenbrorflon', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trenbrorflon',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trenbrorflon->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blaxbrenn(self, hint):
        assert self._state.get("current") == BLAXBRENN, \
            f"brorstorn.blaxbrenn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blaxbrenn', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'blaxbrenn', 1:
                self._state["current"] = SKONSLONN
                self._state["trig"]    = "hint:1"
            case 'blaxbrenn', _:
                self._state["current"] = STENTRENGLOR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blaxbrenn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blaxbrenn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blaxbrenn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stentrenglor(self, hint):
        assert self._state.get("current") == STENTRENGLOR, \
            f"brorstorn.stentrenglor: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stentrenglor', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'stentrenglor', 1:
                self._state["current"] = SPIMGRELGRAXL
                self._state["trig"]    = "hint:1"
            case 'stentrenglor', _:
                self._state["current"] = SKONSLONN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stentrenglor', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stentrenglor',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stentrenglor->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skonslonn(self, hint):
        assert self._state.get("current") == SKONSLONN, \
            f"brorstorn.skonslonn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skonslonn', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'skonslonn', 0:
                self._state["current"] = SKURTRALK
                self._state["trig"]    = "hint:0"
            case 'skonslonn', _:
                self._state["current"] = SPIMGRELGRAXL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skonslonn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skonslonn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skonslonn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spimgrelgraxl(self, hint):
        assert self._state.get("current") == SPIMGRELGRAXL, \
            f"brorstorn.spimgrelgraxl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spimgrelgraxl', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'spimgrelgraxl', _:
                self._state["current"] = BRARBLORSTAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spimgrelgraxl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spimgrelgraxl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spimgrelgraxl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brarblorstax(self, hint):
        assert self._state.get("current") == BRARBLORSTAX, \
            f"brorstorn.brarblorstax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brarblorstax', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'brarblorstax', 0:
                self._state["current"] = SKURTRALK
                self._state["trig"]    = "hint:0"
            case 'brarblorstax', _:
                self._state["current"] = SLIXPRAXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brarblorstax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brarblorstax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brarblorstax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slixpraxx(self, hint):
        assert self._state.get("current") == SLIXPRAXX, \
            f"brorstorn.slixpraxx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slixpraxx', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'slixpraxx', 1:
                self._state["current"] = VARSKOSX
                self._state["trig"]    = "hint:1"
            case 'slixpraxx', _:
                self._state["current"] = VIMSLAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slixpraxx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slixpraxx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slixpraxx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vimslan(self, hint):
        assert self._state.get("current") == VIMSLAN, \
            f"brorstorn.vimslan: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vimslan', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'vimslan', _:
                self._state["current"] = VARSKOSX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vimslan', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vimslan',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vimslan->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _varskosx(self, hint):
        assert self._state.get("current") == VARSKOSX, \
            f"brorstorn.varskosx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'varskosx', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'varskosx', 0:
                self._state["current"] = SKURTRALK
                self._state["trig"]    = "hint:0"
            case 'varskosx', _:
                self._state["current"] = SPULCLARFLOR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'varskosx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'varskosx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"varskosx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spulclarflor(self, hint):
        assert self._state.get("current") == SPULCLARFLOR, \
            f"brorstorn.spulclarflor: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spulclarflor', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'spulclarflor', 0:
                self._state["current"] = STELSKORSTON
                self._state["trig"]    = "hint:0"
            case 'spulclarflor', _:
                self._state["current"] = SLELCLONSLOSR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spulclarflor', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spulclarflor',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spulclarflor->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slelclonslosr(self, hint):
        assert self._state.get("current") == SLELCLONSLOSR, \
            f"brorstorn.slelclonslosr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slelclonslosr', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'slelclonslosr', _:
                self._state["current"] = STELSKORSTON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slelclonslosr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slelclonslosr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slelclonslosr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stelskorston(self, hint):
        assert self._state.get("current") == STELSKORSTON, \
            f"brorstorn.stelskorston: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stelskorston', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'stelskorston', 0:
                self._state["current"] = SKURTRALK
                self._state["trig"]    = "hint:0"
            case 'stelskorston', _:
                self._state["current"] = GLELCLURBLONX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stelskorston', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stelskorston',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stelskorston->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glelclurblonx(self, hint):
        assert self._state.get("current") == GLELCLURBLONX, \
            f"brorstorn.glelclurblonx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glelclurblonx', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'glelclurblonx', _:
                self._state["current"] = STARPRONFLAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glelclurblonx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glelclurblonx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glelclurblonx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _starpronflal(self, hint):
        assert self._state.get("current") == STARPRONFLAL, \
            f"brorstorn.starpronflal: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'starpronflal', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'starpronflal', 1:
                self._state["current"] = SKURTRALK
                self._state["trig"]    = "hint:1"
            case 'starpronflal', _:
                self._state["current"] = SLANTRELSLON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'starpronflal', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'starpronflal',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"starpronflal->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slantrelslon(self, hint):
        assert self._state.get("current") == SLANTRELSLON, \
            f"brorstorn.slantrelslon: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slantrelslon', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'slantrelslon', 1:
                self._state["current"] = BLORSPUL
                self._state["trig"]    = "hint:1"
            case 'slantrelslon', _:
                self._state["current"] = BLOSFLALSKALK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slantrelslon', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slantrelslon',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slantrelslon->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blosflalskalk(self, hint):
        assert self._state.get("current") == BLOSFLALSKALK, \
            f"brorstorn.blosflalskalk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blosflalskalk', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'blosflalskalk', _:
                self._state["current"] = BLORSPUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blosflalskalk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blosflalskalk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blosflalskalk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blorspul(self, hint):
        assert self._state.get("current") == BLORSPUL, \
            f"brorstorn.blorspul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blorspul', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'blorspul', _:
                self._state["current"] = PRIXSTARX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blorspul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blorspul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blorspul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prixstarx(self, hint):
        assert self._state.get("current") == PRIXSTARX, \
            f"brorstorn.prixstarx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prixstarx', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'prixstarx', 1:
                self._state["current"] = VULDRAR
                self._state["trig"]    = "hint:1"
            case 'prixstarx', _:
                self._state["current"] = STORBLALSLEL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prixstarx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prixstarx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prixstarx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _storblalslel(self, hint):
        assert self._state.get("current") == STORBLALSLEL, \
            f"brorstorn.storblalslel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'storblalslel', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'storblalslel', 1:
                self._state["current"] = SKURTRALK
                self._state["trig"]    = "hint:1"
            case 'storblalslel', _:
                self._state["current"] = VULDRAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'storblalslel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'storblalslel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"storblalslel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vuldrar(self, hint):
        assert self._state.get("current") == VULDRAR, \
            f"brorstorn.vuldrar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vuldrar', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'vuldrar', _:
                self._state["current"] = CLORVUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vuldrar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vuldrar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vuldrar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clorvul(self, hint):
        assert self._state.get("current") == CLORVUL, \
            f"brorstorn.clorvul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clorvul', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'clorvul', _:
                self._state["current"] = PRIMBLALGRARX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clorvul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clorvul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clorvul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _primblalgrarx(self, hint):
        assert self._state.get("current") == PRIMBLALGRARX, \
            f"brorstorn.primblalgrarx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'primblalgrarx', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'primblalgrarx', 0:
                self._state["current"] = SPENFLARSTELL
                self._state["trig"]    = "hint:0"
            case 'primblalgrarx', _:
                self._state["current"] = SKIXSLAXPRARK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'primblalgrarx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'primblalgrarx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"primblalgrarx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skixslaxprark(self, hint):
        assert self._state.get("current") == SKIXSLAXPRARK, \
            f"brorstorn.skixslaxprark: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skixslaxprark', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'skixslaxprark', 0:
                self._state["current"] = SKURTRALK
                self._state["trig"]    = "hint:0"
            case 'skixslaxprark', _:
                self._state["current"] = SPENFLARSTELL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skixslaxprark', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skixslaxprark',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skixslaxprark->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spenflarstell(self, hint):
        assert self._state.get("current") == SPENFLARSTELL, \
            f"brorstorn.spenflarstell: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spenflarstell', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'spenflarstell', _:
                self._state["current"] = BRENBLALTRELL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spenflarstell', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spenflarstell',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spenflarstell->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brenblaltrell(self, hint):
        assert self._state.get("current") == BRENBLALTRELL, \
            f"brorstorn.brenblaltrell: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brenblaltrell', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'brenblaltrell', 1:
                self._state["current"] = SPULPRIXVAXX
                self._state["trig"]    = "hint:1"
            case 'brenblaltrell', _:
                self._state["current"] = GRONTRONR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brenblaltrell', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brenblaltrell',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brenblaltrell->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grontronr(self, hint):
        assert self._state.get("current") == GRONTRONR, \
            f"brorstorn.grontronr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grontronr', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'grontronr', _:
                self._state["current"] = SPULPRIXVAXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grontronr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grontronr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grontronr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spulprixvaxx(self, hint):
        assert self._state.get("current") == SPULPRIXVAXX, \
            f"brorstorn.spulprixvaxx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spulprixvaxx', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'spulprixvaxx', _:
                self._state["current"] = VEXGLENSTALR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spulprixvaxx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spulprixvaxx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spulprixvaxx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vexglenstalr(self, hint):
        assert self._state.get("current") == VEXGLENSTALR, \
            f"brorstorn.vexglenstalr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vexglenstalr', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'vexglenstalr', _:
                self._state["current"] = TRULSTANSTAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vexglenstalr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vexglenstalr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vexglenstalr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trulstanstar(self, hint):
        assert self._state.get("current") == TRULSTANSTAR, \
            f"brorstorn.trulstanstar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trulstanstar', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'trulstanstar', _:
                self._state["current"] = PROSVAXBRULX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trulstanstar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trulstanstar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trulstanstar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prosvaxbrulx(self, hint):
        assert self._state.get("current") == PROSVAXBRULX, \
            f"brorstorn.prosvaxbrulx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prosvaxbrulx', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'prosvaxbrulx', 1:
                self._state["current"] = SPEXVONR
                self._state["trig"]    = "hint:1"
            case 'prosvaxbrulx', _:
                self._state["current"] = GLALDRIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prosvaxbrulx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prosvaxbrulx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prosvaxbrulx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glaldrim(self, hint):
        assert self._state.get("current") == GLALDRIM, \
            f"brorstorn.glaldrim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glaldrim', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'glaldrim', 0:
                self._state["current"] = GLONGREN
                self._state["trig"]    = "hint:0"
            case 'glaldrim', _:
                self._state["current"] = SPEXVONR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glaldrim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glaldrim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glaldrim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spexvonr(self, hint):
        assert self._state.get("current") == SPEXVONR, \
            f"brorstorn.spexvonr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spexvonr', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'spexvonr', 0:
                self._state["current"] = SKURTRALK
                self._state["trig"]    = "hint:0"
            case 'spexvonr', _:
                self._state["current"] = GLONGREN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spexvonr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spexvonr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spexvonr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glongren(self, hint):
        assert self._state.get("current") == GLONGREN, \
            f"brorstorn.glongren: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glongren', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'glongren', _:
                self._state["current"] = PRANFLIXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glongren', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glongren',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glongren->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _pranflixx(self, hint):
        assert self._state.get("current") == PRANFLIXX, \
            f"brorstorn.pranflixx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'pranflixx', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'pranflixx', 0:
                self._state["current"] = SKURTRALK
                self._state["trig"]    = "hint:0"
            case 'pranflixx', _:
                self._state["current"] = SKEXTROS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'pranflixx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'pranflixx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"pranflixx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skextros(self, hint):
        assert self._state.get("current") == SKEXTROS, \
            f"brorstorn.skextros: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skextros', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'skextros', 0:
                self._state["current"] = SKURTRALK
                self._state["trig"]    = "hint:0"
            case 'skextros', _:
                self._state["current"] = GLORSLENGRULK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skextros', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skextros',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skextros->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glorslengrulk(self, hint):
        assert self._state.get("current") == GLORSLENGRULK, \
            f"brorstorn.glorslengrulk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glorslengrulk', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'glorslengrulk', _:
                self._state["current"] = VANSKAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glorslengrulk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glorslengrulk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glorslengrulk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vanskan(self, hint):
        assert self._state.get("current") == VANSKAN, \
            f"brorstorn.vanskan: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vanskan', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'vanskan', 0:
                self._state["current"] = SKURTRALK
                self._state["trig"]    = "hint:0"
            case 'vanskan', _:
                self._state["current"] = FLULGLARL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vanskan', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vanskan',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vanskan->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flulglarl(self, hint):
        assert self._state.get("current") == FLULGLARL, \
            f"brorstorn.flulglarl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flulglarl', 2:
                self._state["current"] = SKELDRELFLON
                self._state["trig"]    = "hint:2"
            case 'flulglarl', 0:
                self._state["current"] = SKURTRALK
                self._state["trig"]    = "hint:0"
            case 'flulglarl', _:
                self._state["current"] = VIXPRURCLIXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flulglarl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flulglarl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flulglarl->{_to}", _xid_val)
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
            _xid_val = _xid(__name__, 'spixgrelr', "error", "assert_fail")
            _emit(cycle, 1, __name__, 'spixgrelr',
                   {"hint": hint, "span": span, "caller": caller},
                   dict(ctx), _conds,
                   "entry_blocked->error", _xid_val, assertion=_asrt)
            return 2, cycle + 1

        self._state = {"current": SPIXGRELR, "ctx": ctx,
                        "span": span, "caller": caller,
                        "trig": "auto", "cycle": cycle}
        _dispatch = {
            SPIXGRELR: self._spixgrelr,
            FLELBLIXL: self._flelblixl,
            DRALTRAXKRANL: self._draltraxkranl,
            TRALGRARSTIML: self._tralgrarstiml,
            STORSLIMN: self._storslimn,
            GLENFLON: self._glenflon,
            BLULSKIMVAL: self._blulskimval,
            GLALDRELSLIX: self._glaldrelslix,
            FLONDROSSLEX: self._flondrosslex,
            PREXFLARGRAXN: self._prexflargraxn,
            SLIXGRIXGLUR: self._slixgrixglur,
            BRENCLEL: self._brenclel,
            CLULGRELGREXL: self._clulgrelgrexl,
            SPIXBRURTRIX: self._spixbrurtrix,
            SLEXBLUR: self._slexblur,
            SPAXGLAXT: self._spaxglaxt,
            TRULFLOR: self._trulflor,
            SLORSLART: self._slorslart,
            STURFLONSLAR: self._sturflonslar,
            SKANSKULX: self._skanskulx,
            KREXSKEX: self._krexskex,
            GRORTRONFLIX: self._grortronflix,
            GROSSLEN: self._grosslen,
            CLANDRON: self._clandron,
            SLULPRARCLOSR: self._slulprarclosr,
            CLORCLUR: self._clorclur,
            KRANSPIMK: self._kranspimk,
            TRENBRORFLON: self._trenbrorflon,
            BLAXBRENN: self._blaxbrenn,
            STENTRENGLOR: self._stentrenglor,
            SKONSLONN: self._skonslonn,
            SPIMGRELGRAXL: self._spimgrelgraxl,
            BRARBLORSTAX: self._brarblorstax,
            SLIXPRAXX: self._slixpraxx,
            VIMSLAN: self._vimslan,
            VARSKOSX: self._varskosx,
            SPULCLARFLOR: self._spulclarflor,
            SLELCLONSLOSR: self._slelclonslosr,
            STELSKORSTON: self._stelskorston,
            GLELCLURBLONX: self._glelclurblonx,
            STARPRONFLAL: self._starpronflal,
            SLANTRELSLON: self._slantrelslon,
            BLOSFLALSKALK: self._blosflalskalk,
            BLORSPUL: self._blorspul,
            PRIXSTARX: self._prixstarx,
            STORBLALSLEL: self._storblalslel,
            VULDRAR: self._vuldrar,
            CLORVUL: self._clorvul,
            PRIMBLALGRARX: self._primblalgrarx,
            SKIXSLAXPRARK: self._skixslaxprark,
            SPENFLARSTELL: self._spenflarstell,
            BRENBLALTRELL: self._brenblaltrell,
            GRONTRONR: self._grontronr,
            SPULPRIXVAXX: self._spulprixvaxx,
            VEXGLENSTALR: self._vexglenstalr,
            TRULSTANSTAR: self._trulstanstar,
            PROSVAXBRULX: self._prosvaxbrulx,
            GLALDRIM: self._glaldrim,
            SPEXVONR: self._spexvonr,
            GLONGREN: self._glongren,
            PRANFLIXX: self._pranflixx,
            SKEXTROS: self._skextros,
            GLORSLENGRULK: self._glorslengrulk,
            VANSKAN: self._vanskan,
            FLULGLARL: self._flulglarl,
        }
        while self._state["current"] not in _R and self._state["cycle"] - cycle < 8000:
            _dispatch[self._state["current"]](hint)
        _ret     = _R.get(self._state["current"], -1)
        _is_err  = self._state["current"] == SKELDRELFLON
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
    return BrorstornFSM().invoke(hint=hint, span=span, caller=caller, ctx=ctx, cycle=cycle)
