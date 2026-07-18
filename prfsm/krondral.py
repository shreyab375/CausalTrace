from _log import _w as _emit, _xid

BRURVELSTIXX = 'brurvelstixx'
PRIMGRARFLEXK = 'primgrarflexk'
GRONBRAXSTAXK = 'gronbraxstaxk'
GRELCLEX = 'grelclex'
BLIXCLARN = 'blixclarn'
DROSBLAXBLENT = 'drosblaxblent'
STANVEXX = 'stanvexx'
DROSVIMSTARL = 'drosvimstarl'
VAXSKART = 'vaxskart'
BRELSPALPRANN = 'brelspalprann'
DRIXDREXGLUL = 'drixdrexglul'
GLEXTRAR = 'glextrar'
SKIMTRAXSPIMK = 'skimtraxspimk'
GLIXPRIXT = 'glixprixt'
BLORFLELR = 'blorflelr'
CLIMBRAXVIXL = 'climbraxvixl'
DRALBLAXGLUR = 'dralblaxglur'
TRELFLIX = 'trelflix'
SKORDRANKRURK = 'skordrankrurk'
BRELBRONSTONL = 'brelbronstonl'
BRELSPANSLUL = 'brelspanslul'
VELBLALSKOS = 'velblalskos'
GLALSKAX = 'glalskax'
BREXPRAR = 'brexprar'
SPULPROST = 'spulprost'
GRULGRENPREL = 'grulgrenprel'
TRONBRAXPRUL = 'tronbraxprul'
BRELGRAXR = 'brelgraxr'
PROSFLARX = 'prosflarx'
SPURBRALBRURL = 'spurbralbrurl'
SLAXBRONT = 'slaxbront'
CLORSTEXR = 'clorstexr'
BLOSSLELT = 'blosslelt'
BRONSTEX = 'bronstex'
SKARBRIXBREXX = 'skarbrixbrexx'
SKELSTUR = 'skelstur'
GRURFLAXSKANL = 'grurflaxskanl'
SKORBREXBRENN = 'skorbrexbrenn'
BRENSKIXCLIX = 'brenskixclix'
SKURTRANR = 'skurtranr'
TRALGLOSPRORT = 'tralglosprort'
FLIMGROSR = 'flimgrosr'
FLARVONK = 'flarvonk'
DRARGLAXK = 'drarglaxk'
PRELSKENSKAL = 'prelskenskal'
GRALCLURBROSN = 'gralclurbrosn'
BLALPRAX = 'blalprax'
TRELGLAL = 'trelglal'
BRORCLAX = 'brorclax'
GRURVAXR = 'grurvaxr'
BLEXTRIM = 'blextrim'
KRORDRIM = 'krordrim'
BRIMKRIXL = 'brimkrixl'
STALVURBRAX = 'stalvurbrax'
DRARGRIMR = 'drargrimr'
BROSSTIXTROSX = 'brosstixtrosx'
SPENSPAXCLAXK = 'spenspaxclaxk'
STANSPOSPRUR = 'stansposprur'
SLIMCLAR = 'slimclar'
GLURBLIMGLENX = 'glurblimglenx'
PRURCLURPRAL = 'prurclurpral'
SLALPRANR = 'slalpranr'
SPENCLORL = 'spenclorl'
CLULKRIXKRURL = 'clulkrixkrurl'
SKORSTOSBRURL = 'skorstosbrurl'
BRELKRUR = 'brelkrur'
SKURFLENDRURL = 'skurflendrurl'
BRENPRON = 'brenpron'

_R = {
    BRELKRUR: 0,
    SKURFLENDRURL: 1,
    BRENPRON: 2,
}

_CTX_WRITES_KEY  = 'flurslex'
_CTX_WRITE_STATE = PRIMGRARFLEXK

class KrondralFSM:
    def __init__(self):
        self._state = {}

    def _brurvelstixx(self, hint):
        assert self._state.get("current") == BRURVELSTIXX, \
            f"krondral.brurvelstixx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brurvelstixx', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'brurvelstixx', _:
                self._state["current"] = PRIMGRARFLEXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brurvelstixx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brurvelstixx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brurvelstixx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _primgrarflexk(self, hint):
        assert self._state.get("current") == PRIMGRARFLEXK, \
            f"krondral.primgrarflexk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        _ctx_val_before = self._state["ctx"].get(_CTX_WRITES_KEY, 0)
        match self._state["current"], hint:
            case 'primgrarflexk', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'primgrarflexk', _:
                self._state["current"] = GRONBRAXSTAXK
                self._state["trig"]    = "auto"
        _old = self._state["ctx"].get(_CTX_WRITES_KEY, 0)
        _inc = 2 if hint == 2 else 1
        self._state["ctx"][_CTX_WRITES_KEY] = _old + _inc
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'primgrarflexk', _to, _trig)
        _conds = {"hint_branch": _hint_branch,
                   "ctx_write": True,
                   "ctx_val_before": _ctx_val_before}
        _emit(self._state["cycle"], 1, __name__, 'primgrarflexk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"primgrarflexk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _gronbraxstaxk(self, hint):
        assert self._state.get("current") == GRONBRAXSTAXK, \
            f"krondral.gronbraxstaxk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'gronbraxstaxk', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'gronbraxstaxk', _:
                self._state["current"] = GRELCLEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'gronbraxstaxk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'gronbraxstaxk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"gronbraxstaxk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grelclex(self, hint):
        assert self._state.get("current") == GRELCLEX, \
            f"krondral.grelclex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grelclex', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'grelclex', 0:
                self._state["current"] = SKURFLENDRURL
                self._state["trig"]    = "hint:0"
            case 'grelclex', _:
                self._state["current"] = BLIXCLARN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grelclex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grelclex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grelclex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blixclarn(self, hint):
        assert self._state.get("current") == BLIXCLARN, \
            f"krondral.blixclarn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blixclarn', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'blixclarn', 1:
                self._state["current"] = STANVEXX
                self._state["trig"]    = "hint:1"
            case 'blixclarn', _:
                self._state["current"] = DROSBLAXBLENT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blixclarn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blixclarn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blixclarn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drosblaxblent(self, hint):
        assert self._state.get("current") == DROSBLAXBLENT, \
            f"krondral.drosblaxblent: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drosblaxblent', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'drosblaxblent', _:
                self._state["current"] = STANVEXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drosblaxblent', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drosblaxblent',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drosblaxblent->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stanvexx(self, hint):
        assert self._state.get("current") == STANVEXX, \
            f"krondral.stanvexx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stanvexx', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'stanvexx', _:
                self._state["current"] = DROSVIMSTARL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stanvexx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stanvexx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stanvexx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drosvimstarl(self, hint):
        assert self._state.get("current") == DROSVIMSTARL, \
            f"krondral.drosvimstarl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drosvimstarl', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'drosvimstarl', 1:
                self._state["current"] = SKURFLENDRURL
                self._state["trig"]    = "hint:1"
            case 'drosvimstarl', _:
                self._state["current"] = VAXSKART
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drosvimstarl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drosvimstarl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drosvimstarl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vaxskart(self, hint):
        assert self._state.get("current") == VAXSKART, \
            f"krondral.vaxskart: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vaxskart', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'vaxskart', 0:
                self._state["current"] = DRIXDREXGLUL
                self._state["trig"]    = "hint:0"
            case 'vaxskart', _:
                self._state["current"] = BRELSPALPRANN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vaxskart', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vaxskart',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vaxskart->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brelspalprann(self, hint):
        assert self._state.get("current") == BRELSPALPRANN, \
            f"krondral.brelspalprann: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brelspalprann', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'brelspalprann', 1:
                self._state["current"] = GLEXTRAR
                self._state["trig"]    = "hint:1"
            case 'brelspalprann', _:
                self._state["current"] = DRIXDREXGLUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brelspalprann', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brelspalprann',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brelspalprann->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drixdrexglul(self, hint):
        assert self._state.get("current") == DRIXDREXGLUL, \
            f"krondral.drixdrexglul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drixdrexglul', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'drixdrexglul', 0:
                self._state["current"] = SKURFLENDRURL
                self._state["trig"]    = "hint:0"
            case 'drixdrexglul', _:
                self._state["current"] = GLEXTRAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drixdrexglul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drixdrexglul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drixdrexglul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glextrar(self, hint):
        assert self._state.get("current") == GLEXTRAR, \
            f"krondral.glextrar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glextrar', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'glextrar', 1:
                self._state["current"] = GLIXPRIXT
                self._state["trig"]    = "hint:1"
            case 'glextrar', _:
                self._state["current"] = SKIMTRAXSPIMK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glextrar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glextrar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glextrar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skimtraxspimk(self, hint):
        assert self._state.get("current") == SKIMTRAXSPIMK, \
            f"krondral.skimtraxspimk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skimtraxspimk', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'skimtraxspimk', _:
                self._state["current"] = GLIXPRIXT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skimtraxspimk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skimtraxspimk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skimtraxspimk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glixprixt(self, hint):
        assert self._state.get("current") == GLIXPRIXT, \
            f"krondral.glixprixt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glixprixt', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'glixprixt', _:
                self._state["current"] = BLORFLELR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glixprixt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glixprixt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glixprixt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blorflelr(self, hint):
        assert self._state.get("current") == BLORFLELR, \
            f"krondral.blorflelr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blorflelr', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'blorflelr', _:
                self._state["current"] = CLIMBRAXVIXL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blorflelr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blorflelr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blorflelr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _climbraxvixl(self, hint):
        assert self._state.get("current") == CLIMBRAXVIXL, \
            f"krondral.climbraxvixl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'climbraxvixl', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'climbraxvixl', _:
                self._state["current"] = DRALBLAXGLUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'climbraxvixl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'climbraxvixl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"climbraxvixl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _dralblaxglur(self, hint):
        assert self._state.get("current") == DRALBLAXGLUR, \
            f"krondral.dralblaxglur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'dralblaxglur', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'dralblaxglur', _:
                self._state["current"] = TRELFLIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'dralblaxglur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'dralblaxglur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"dralblaxglur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trelflix(self, hint):
        assert self._state.get("current") == TRELFLIX, \
            f"krondral.trelflix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trelflix', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'trelflix', 1:
                self._state["current"] = BRELBRONSTONL
                self._state["trig"]    = "hint:1"
            case 'trelflix', _:
                self._state["current"] = SKORDRANKRURK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trelflix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trelflix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trelflix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skordrankrurk(self, hint):
        assert self._state.get("current") == SKORDRANKRURK, \
            f"krondral.skordrankrurk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skordrankrurk', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'skordrankrurk', 0:
                self._state["current"] = SKURFLENDRURL
                self._state["trig"]    = "hint:0"
            case 'skordrankrurk', _:
                self._state["current"] = BRELBRONSTONL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skordrankrurk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skordrankrurk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skordrankrurk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brelbronstonl(self, hint):
        assert self._state.get("current") == BRELBRONSTONL, \
            f"krondral.brelbronstonl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brelbronstonl', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'brelbronstonl', 1:
                self._state["current"] = SKURFLENDRURL
                self._state["trig"]    = "hint:1"
            case 'brelbronstonl', _:
                self._state["current"] = BRELSPANSLUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brelbronstonl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brelbronstonl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brelbronstonl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brelspanslul(self, hint):
        assert self._state.get("current") == BRELSPANSLUL, \
            f"krondral.brelspanslul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brelspanslul', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'brelspanslul', 1:
                self._state["current"] = GLALSKAX
                self._state["trig"]    = "hint:1"
            case 'brelspanslul', _:
                self._state["current"] = VELBLALSKOS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brelspanslul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brelspanslul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brelspanslul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _velblalskos(self, hint):
        assert self._state.get("current") == VELBLALSKOS, \
            f"krondral.velblalskos: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'velblalskos', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'velblalskos', _:
                self._state["current"] = GLALSKAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'velblalskos', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'velblalskos',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"velblalskos->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glalskax(self, hint):
        assert self._state.get("current") == GLALSKAX, \
            f"krondral.glalskax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glalskax', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'glalskax', _:
                self._state["current"] = BREXPRAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glalskax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glalskax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glalskax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brexprar(self, hint):
        assert self._state.get("current") == BREXPRAR, \
            f"krondral.brexprar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brexprar', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'brexprar', _:
                self._state["current"] = SPULPROST
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brexprar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brexprar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brexprar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spulprost(self, hint):
        assert self._state.get("current") == SPULPROST, \
            f"krondral.spulprost: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spulprost', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'spulprost', 0:
                self._state["current"] = TRONBRAXPRUL
                self._state["trig"]    = "hint:0"
            case 'spulprost', _:
                self._state["current"] = GRULGRENPREL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spulprost', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spulprost',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spulprost->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grulgrenprel(self, hint):
        assert self._state.get("current") == GRULGRENPREL, \
            f"krondral.grulgrenprel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grulgrenprel', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'grulgrenprel', 1:
                self._state["current"] = BRELGRAXR
                self._state["trig"]    = "hint:1"
            case 'grulgrenprel', _:
                self._state["current"] = TRONBRAXPRUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grulgrenprel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grulgrenprel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grulgrenprel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _tronbraxprul(self, hint):
        assert self._state.get("current") == TRONBRAXPRUL, \
            f"krondral.tronbraxprul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'tronbraxprul', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'tronbraxprul', _:
                self._state["current"] = BRELGRAXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'tronbraxprul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'tronbraxprul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"tronbraxprul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brelgraxr(self, hint):
        assert self._state.get("current") == BRELGRAXR, \
            f"krondral.brelgraxr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brelgraxr', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'brelgraxr', _:
                self._state["current"] = PROSFLARX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brelgraxr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brelgraxr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brelgraxr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prosflarx(self, hint):
        assert self._state.get("current") == PROSFLARX, \
            f"krondral.prosflarx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prosflarx', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'prosflarx', 0:
                self._state["current"] = SLAXBRONT
                self._state["trig"]    = "hint:0"
            case 'prosflarx', _:
                self._state["current"] = SPURBRALBRURL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prosflarx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prosflarx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prosflarx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spurbralbrurl(self, hint):
        assert self._state.get("current") == SPURBRALBRURL, \
            f"krondral.spurbralbrurl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spurbralbrurl', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'spurbralbrurl', _:
                self._state["current"] = SLAXBRONT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spurbralbrurl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spurbralbrurl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spurbralbrurl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slaxbront(self, hint):
        assert self._state.get("current") == SLAXBRONT, \
            f"krondral.slaxbront: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slaxbront', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'slaxbront', 0:
                self._state["current"] = BLOSSLELT
                self._state["trig"]    = "hint:0"
            case 'slaxbront', _:
                self._state["current"] = CLORSTEXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slaxbront', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slaxbront',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slaxbront->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clorstexr(self, hint):
        assert self._state.get("current") == CLORSTEXR, \
            f"krondral.clorstexr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clorstexr', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'clorstexr', 0:
                self._state["current"] = BRONSTEX
                self._state["trig"]    = "hint:0"
            case 'clorstexr', _:
                self._state["current"] = BLOSSLELT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clorstexr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clorstexr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clorstexr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blosslelt(self, hint):
        assert self._state.get("current") == BLOSSLELT, \
            f"krondral.blosslelt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blosslelt', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'blosslelt', _:
                self._state["current"] = BRONSTEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blosslelt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blosslelt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blosslelt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _bronstex(self, hint):
        assert self._state.get("current") == BRONSTEX, \
            f"krondral.bronstex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'bronstex', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'bronstex', _:
                self._state["current"] = SKARBRIXBREXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'bronstex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'bronstex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"bronstex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skarbrixbrexx(self, hint):
        assert self._state.get("current") == SKARBRIXBREXX, \
            f"krondral.skarbrixbrexx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skarbrixbrexx', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'skarbrixbrexx', 0:
                self._state["current"] = GRURFLAXSKANL
                self._state["trig"]    = "hint:0"
            case 'skarbrixbrexx', _:
                self._state["current"] = SKELSTUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skarbrixbrexx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skarbrixbrexx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skarbrixbrexx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skelstur(self, hint):
        assert self._state.get("current") == SKELSTUR, \
            f"krondral.skelstur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skelstur', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'skelstur', 0:
                self._state["current"] = SKURFLENDRURL
                self._state["trig"]    = "hint:0"
            case 'skelstur', _:
                self._state["current"] = GRURFLAXSKANL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skelstur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skelstur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skelstur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grurflaxskanl(self, hint):
        assert self._state.get("current") == GRURFLAXSKANL, \
            f"krondral.grurflaxskanl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grurflaxskanl', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'grurflaxskanl', 1:
                self._state["current"] = BRENSKIXCLIX
                self._state["trig"]    = "hint:1"
            case 'grurflaxskanl', _:
                self._state["current"] = SKORBREXBRENN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grurflaxskanl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grurflaxskanl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grurflaxskanl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skorbrexbrenn(self, hint):
        assert self._state.get("current") == SKORBREXBRENN, \
            f"krondral.skorbrexbrenn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skorbrexbrenn', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'skorbrexbrenn', 1:
                self._state["current"] = SKURTRANR
                self._state["trig"]    = "hint:1"
            case 'skorbrexbrenn', _:
                self._state["current"] = BRENSKIXCLIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skorbrexbrenn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skorbrexbrenn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skorbrexbrenn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brenskixclix(self, hint):
        assert self._state.get("current") == BRENSKIXCLIX, \
            f"krondral.brenskixclix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brenskixclix', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'brenskixclix', _:
                self._state["current"] = SKURTRANR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brenskixclix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brenskixclix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brenskixclix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skurtranr(self, hint):
        assert self._state.get("current") == SKURTRANR, \
            f"krondral.skurtranr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skurtranr', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'skurtranr', 1:
                self._state["current"] = FLIMGROSR
                self._state["trig"]    = "hint:1"
            case 'skurtranr', _:
                self._state["current"] = TRALGLOSPRORT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skurtranr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skurtranr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skurtranr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _tralglosprort(self, hint):
        assert self._state.get("current") == TRALGLOSPRORT, \
            f"krondral.tralglosprort: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'tralglosprort', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'tralglosprort', 0:
                self._state["current"] = FLARVONK
                self._state["trig"]    = "hint:0"
            case 'tralglosprort', _:
                self._state["current"] = FLIMGROSR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'tralglosprort', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'tralglosprort',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"tralglosprort->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flimgrosr(self, hint):
        assert self._state.get("current") == FLIMGROSR, \
            f"krondral.flimgrosr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flimgrosr', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'flimgrosr', _:
                self._state["current"] = FLARVONK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flimgrosr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flimgrosr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flimgrosr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flarvonk(self, hint):
        assert self._state.get("current") == FLARVONK, \
            f"krondral.flarvonk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flarvonk', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'flarvonk', _:
                self._state["current"] = DRARGLAXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flarvonk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flarvonk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flarvonk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drarglaxk(self, hint):
        assert self._state.get("current") == DRARGLAXK, \
            f"krondral.drarglaxk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drarglaxk', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'drarglaxk', _:
                self._state["current"] = PRELSKENSKAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drarglaxk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drarglaxk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drarglaxk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prelskenskal(self, hint):
        assert self._state.get("current") == PRELSKENSKAL, \
            f"krondral.prelskenskal: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prelskenskal', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'prelskenskal', 0:
                self._state["current"] = BLALPRAX
                self._state["trig"]    = "hint:0"
            case 'prelskenskal', _:
                self._state["current"] = GRALCLURBROSN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prelskenskal', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prelskenskal',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prelskenskal->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _gralclurbrosn(self, hint):
        assert self._state.get("current") == GRALCLURBROSN, \
            f"krondral.gralclurbrosn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'gralclurbrosn', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'gralclurbrosn', _:
                self._state["current"] = BLALPRAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'gralclurbrosn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'gralclurbrosn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"gralclurbrosn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blalprax(self, hint):
        assert self._state.get("current") == BLALPRAX, \
            f"krondral.blalprax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blalprax', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'blalprax', _:
                self._state["current"] = TRELGLAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blalprax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blalprax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blalprax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trelglal(self, hint):
        assert self._state.get("current") == TRELGLAL, \
            f"krondral.trelglal: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trelglal', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'trelglal', 0:
                self._state["current"] = SKURFLENDRURL
                self._state["trig"]    = "hint:0"
            case 'trelglal', _:
                self._state["current"] = BRORCLAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trelglal', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trelglal',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trelglal->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brorclax(self, hint):
        assert self._state.get("current") == BRORCLAX, \
            f"krondral.brorclax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brorclax', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'brorclax', _:
                self._state["current"] = GRURVAXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brorclax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brorclax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brorclax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grurvaxr(self, hint):
        assert self._state.get("current") == GRURVAXR, \
            f"krondral.grurvaxr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grurvaxr', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'grurvaxr', 0:
                self._state["current"] = SKURFLENDRURL
                self._state["trig"]    = "hint:0"
            case 'grurvaxr', _:
                self._state["current"] = BLEXTRIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grurvaxr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grurvaxr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grurvaxr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blextrim(self, hint):
        assert self._state.get("current") == BLEXTRIM, \
            f"krondral.blextrim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blextrim', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'blextrim', _:
                self._state["current"] = KRORDRIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blextrim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blextrim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blextrim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krordrim(self, hint):
        assert self._state.get("current") == KRORDRIM, \
            f"krondral.krordrim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krordrim', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'krordrim', 1:
                self._state["current"] = SKURFLENDRURL
                self._state["trig"]    = "hint:1"
            case 'krordrim', _:
                self._state["current"] = BRIMKRIXL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krordrim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krordrim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krordrim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brimkrixl(self, hint):
        assert self._state.get("current") == BRIMKRIXL, \
            f"krondral.brimkrixl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brimkrixl', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'brimkrixl', 1:
                self._state["current"] = SKURFLENDRURL
                self._state["trig"]    = "hint:1"
            case 'brimkrixl', _:
                self._state["current"] = STALVURBRAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brimkrixl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brimkrixl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brimkrixl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stalvurbrax(self, hint):
        assert self._state.get("current") == STALVURBRAX, \
            f"krondral.stalvurbrax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stalvurbrax', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'stalvurbrax', _:
                self._state["current"] = DRARGRIMR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stalvurbrax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stalvurbrax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stalvurbrax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drargrimr(self, hint):
        assert self._state.get("current") == DRARGRIMR, \
            f"krondral.drargrimr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drargrimr', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'drargrimr', 0:
                self._state["current"] = SPENSPAXCLAXK
                self._state["trig"]    = "hint:0"
            case 'drargrimr', _:
                self._state["current"] = BROSSTIXTROSX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drargrimr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drargrimr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drargrimr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brosstixtrosx(self, hint):
        assert self._state.get("current") == BROSSTIXTROSX, \
            f"krondral.brosstixtrosx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brosstixtrosx', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'brosstixtrosx', 0:
                self._state["current"] = SKURFLENDRURL
                self._state["trig"]    = "hint:0"
            case 'brosstixtrosx', _:
                self._state["current"] = SPENSPAXCLAXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brosstixtrosx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brosstixtrosx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brosstixtrosx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spenspaxclaxk(self, hint):
        assert self._state.get("current") == SPENSPAXCLAXK, \
            f"krondral.spenspaxclaxk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spenspaxclaxk', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'spenspaxclaxk', 1:
                self._state["current"] = SKURFLENDRURL
                self._state["trig"]    = "hint:1"
            case 'spenspaxclaxk', _:
                self._state["current"] = STANSPOSPRUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spenspaxclaxk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spenspaxclaxk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spenspaxclaxk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stansposprur(self, hint):
        assert self._state.get("current") == STANSPOSPRUR, \
            f"krondral.stansposprur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stansposprur', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'stansposprur', 0:
                self._state["current"] = SKURFLENDRURL
                self._state["trig"]    = "hint:0"
            case 'stansposprur', _:
                self._state["current"] = SLIMCLAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stansposprur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stansposprur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stansposprur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slimclar(self, hint):
        assert self._state.get("current") == SLIMCLAR, \
            f"krondral.slimclar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slimclar', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'slimclar', 1:
                self._state["current"] = SKURFLENDRURL
                self._state["trig"]    = "hint:1"
            case 'slimclar', _:
                self._state["current"] = GLURBLIMGLENX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slimclar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slimclar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slimclar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glurblimglenx(self, hint):
        assert self._state.get("current") == GLURBLIMGLENX, \
            f"krondral.glurblimglenx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glurblimglenx', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'glurblimglenx', _:
                self._state["current"] = PRURCLURPRAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glurblimglenx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glurblimglenx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glurblimglenx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prurclurpral(self, hint):
        assert self._state.get("current") == PRURCLURPRAL, \
            f"krondral.prurclurpral: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prurclurpral', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'prurclurpral', _:
                self._state["current"] = SLALPRANR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prurclurpral', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prurclurpral',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prurclurpral->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slalpranr(self, hint):
        assert self._state.get("current") == SLALPRANR, \
            f"krondral.slalpranr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slalpranr', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'slalpranr', 0:
                self._state["current"] = CLULKRIXKRURL
                self._state["trig"]    = "hint:0"
            case 'slalpranr', _:
                self._state["current"] = SPENCLORL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slalpranr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slalpranr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slalpranr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spenclorl(self, hint):
        assert self._state.get("current") == SPENCLORL, \
            f"krondral.spenclorl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spenclorl', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'spenclorl', 0:
                self._state["current"] = SKURFLENDRURL
                self._state["trig"]    = "hint:0"
            case 'spenclorl', _:
                self._state["current"] = CLULKRIXKRURL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spenclorl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spenclorl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spenclorl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clulkrixkrurl(self, hint):
        assert self._state.get("current") == CLULKRIXKRURL, \
            f"krondral.clulkrixkrurl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clulkrixkrurl', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'clulkrixkrurl', _:
                self._state["current"] = SKORSTOSBRURL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clulkrixkrurl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clulkrixkrurl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clulkrixkrurl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skorstosbrurl(self, hint):
        assert self._state.get("current") == SKORSTOSBRURL, \
            f"krondral.skorstosbrurl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skorstosbrurl', 2:
                self._state["current"] = BRENPRON
                self._state["trig"]    = "hint:2"
            case 'skorstosbrurl', _:
                self._state["current"] = BRELKRUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skorstosbrurl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skorstosbrurl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skorstosbrurl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def invoke(self, hint=None, span=None, caller=None, ctx=None, cycle=0):
        if ctx is None: ctx = {}

        self._state = {"current": BRURVELSTIXX, "ctx": ctx,
                        "span": span, "caller": caller,
                        "trig": "auto", "cycle": cycle}
        _dispatch = {
            BRURVELSTIXX: self._brurvelstixx,
            PRIMGRARFLEXK: self._primgrarflexk,
            GRONBRAXSTAXK: self._gronbraxstaxk,
            GRELCLEX: self._grelclex,
            BLIXCLARN: self._blixclarn,
            DROSBLAXBLENT: self._drosblaxblent,
            STANVEXX: self._stanvexx,
            DROSVIMSTARL: self._drosvimstarl,
            VAXSKART: self._vaxskart,
            BRELSPALPRANN: self._brelspalprann,
            DRIXDREXGLUL: self._drixdrexglul,
            GLEXTRAR: self._glextrar,
            SKIMTRAXSPIMK: self._skimtraxspimk,
            GLIXPRIXT: self._glixprixt,
            BLORFLELR: self._blorflelr,
            CLIMBRAXVIXL: self._climbraxvixl,
            DRALBLAXGLUR: self._dralblaxglur,
            TRELFLIX: self._trelflix,
            SKORDRANKRURK: self._skordrankrurk,
            BRELBRONSTONL: self._brelbronstonl,
            BRELSPANSLUL: self._brelspanslul,
            VELBLALSKOS: self._velblalskos,
            GLALSKAX: self._glalskax,
            BREXPRAR: self._brexprar,
            SPULPROST: self._spulprost,
            GRULGRENPREL: self._grulgrenprel,
            TRONBRAXPRUL: self._tronbraxprul,
            BRELGRAXR: self._brelgraxr,
            PROSFLARX: self._prosflarx,
            SPURBRALBRURL: self._spurbralbrurl,
            SLAXBRONT: self._slaxbront,
            CLORSTEXR: self._clorstexr,
            BLOSSLELT: self._blosslelt,
            BRONSTEX: self._bronstex,
            SKARBRIXBREXX: self._skarbrixbrexx,
            SKELSTUR: self._skelstur,
            GRURFLAXSKANL: self._grurflaxskanl,
            SKORBREXBRENN: self._skorbrexbrenn,
            BRENSKIXCLIX: self._brenskixclix,
            SKURTRANR: self._skurtranr,
            TRALGLOSPRORT: self._tralglosprort,
            FLIMGROSR: self._flimgrosr,
            FLARVONK: self._flarvonk,
            DRARGLAXK: self._drarglaxk,
            PRELSKENSKAL: self._prelskenskal,
            GRALCLURBROSN: self._gralclurbrosn,
            BLALPRAX: self._blalprax,
            TRELGLAL: self._trelglal,
            BRORCLAX: self._brorclax,
            GRURVAXR: self._grurvaxr,
            BLEXTRIM: self._blextrim,
            KRORDRIM: self._krordrim,
            BRIMKRIXL: self._brimkrixl,
            STALVURBRAX: self._stalvurbrax,
            DRARGRIMR: self._drargrimr,
            BROSSTIXTROSX: self._brosstixtrosx,
            SPENSPAXCLAXK: self._spenspaxclaxk,
            STANSPOSPRUR: self._stansposprur,
            SLIMCLAR: self._slimclar,
            GLURBLIMGLENX: self._glurblimglenx,
            PRURCLURPRAL: self._prurclurpral,
            SLALPRANR: self._slalpranr,
            SPENCLORL: self._spenclorl,
            CLULKRIXKRURL: self._clulkrixkrurl,
            SKORSTOSBRURL: self._skorstosbrurl,
        }
        while self._state["current"] not in _R and self._state["cycle"] - cycle < 8000:
            _dispatch[self._state["current"]](hint)
        _ret     = _R.get(self._state["current"], -1)
        _is_err  = self._state["current"] == BRENPRON
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
    return KrondralFSM().invoke(hint=hint, span=span, caller=caller, ctx=ctx, cycle=cycle)
